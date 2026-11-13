#!/usr/bin/env node
/**
 * Fast path: copy reading markdown (+ images) into site/content and
 * refresh catalog.json reading entries — no quiz PDF generation.
 *
 * Use this for site preview. Run prepare-downloads when you need
 * assignment / test / quiz PDF packs.
 */
import {
  mkdirSync,
  rmSync,
  readdirSync,
  readFileSync,
  writeFileSync,
  copyFileSync,
  existsSync,
  statSync,
  cpSync,
} from 'node:fs'
import { join, basename, dirname, relative } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'
import { MODULE_META } from './course-meta.mjs'

const __dirname = dirname(fileURLToPath(import.meta.url))
const SITE_ROOT = join(__dirname, '..')
const COURSE_ROOT = join(SITE_ROOT, '..')
const CONTENT_DIR = join(SITE_ROOT, 'content')
const DATA_DIR = join(SITE_ROOT, 'data')
const CATALOG_PATH = join(DATA_DIR, 'catalog.json')

function listFiles(dir, predicate) {
  if (!existsSync(dir)) return []
  return readdirSync(dir)
    .filter((name) => predicate(name))
    .map((name) => join(dir, name))
    .filter((path) => statSync(path).isFile())
    .sort()
}

function topicLabel(filename) {
  return basename(filename, '.md')
    .replace(/\.py$/, '')
    .replace(/^test_/, '')
    .replace(/_/g, ' ')
}

function ensureDir(path) {
  mkdirSync(path, { recursive: true })
}

function copyReadingsForModule(meta) {
  const moduleDir = join(COURSE_ROOT, meta.id)
  const readingsDir = join(moduleDir, 'readings')
  const readingsSrc = listFiles(
    readingsDir,
    (n) => n.endsWith('.md') && !n.startsWith('README'),
  )
  const outDir = join(CONTENT_DIR, meta.id, 'readings')
  if (existsSync(outDir)) rmSync(outDir, { recursive: true, force: true })
  ensureDir(outDir)

  const readings = []
  for (const src of readingsSrc) {
    const name = basename(src)
    copyFileSync(src, join(outDir, name))
    const id = basename(name, '.md')
    readings.push({
      id,
      label: topicLabel(name),
      path: relative(COURSE_ROOT, src).replace(/\\/g, '/'),
      href: `content/${meta.id}/readings/${name}`,
    })
  }

  const imagesDir = join(readingsDir, 'images')
  if (existsSync(imagesDir) && statSync(imagesDir).isDirectory()) {
    cpSync(imagesDir, join(outDir, 'images'), { recursive: true })
  }

  return { readings, hasModuleDir: existsSync(moduleDir) }
}

export function prepareReadings({ preserveDownloads = true } = {}) {
  ensureDir(CONTENT_DIR)
  ensureDir(DATA_DIR)

  let existing = null
  if (existsSync(CATALOG_PATH)) {
    try {
      existing = JSON.parse(readFileSync(CATALOG_PATH, 'utf8'))
    } catch {
      existing = null
    }
  }

  const byId = new Map((existing?.modules || []).map((m) => [m.id, m]))
  const modules = MODULE_META.map((meta) => {
    const { readings, hasModuleDir } = copyReadingsForModule(meta)
    const prev = byId.get(meta.id) || {}
    const readOnly = Boolean(meta.readOnly)
    return {
      ...meta,
      readOnly,
      hasModuleDir,
      assignments:
        readOnly || !preserveDownloads
          ? []
          : prev.assignments || prev.worksheets || [],
      assignmentsZip:
        readOnly || !preserveDownloads
          ? null
          : prev.assignmentsZip ?? prev.worksheetsZip ?? null,
      assignmentSingle:
        readOnly || !preserveDownloads
          ? null
          : prev.assignmentSingle ?? prev.worksheetSingle ?? null,
      tests: readOnly || !preserveDownloads ? [] : prev.tests || [],
      testsZip: readOnly || !preserveDownloads ? null : prev.testsZip ?? null,
      quizzes: readOnly || !preserveDownloads ? [] : prev.quizzes || [],
      quizzesZip:
        readOnly || !preserveDownloads ? null : prev.quizzesZip ?? null,
      quizzesPdfZip:
        readOnly || !preserveDownloads ? null : prev.quizzesPdfZip ?? null,
      quizSingle:
        readOnly || !preserveDownloads ? null : prev.quizSingle ?? null,
      answerKeysZip:
        readOnly || !preserveDownloads ? null : prev.answerKeysZip ?? null,
      readings,
    }
  })

  const catalog = {
    brand: 'MailGuard Course',
    tagline:
      'Cloud-security learning for students building identity, email DLP, and secure SaaS skills.',
    generatedAt: new Date().toISOString(),
    modules,
  }

  writeFileSync(CATALOG_PATH, JSON.stringify(catalog, null, 2) + '\n')
  writeGlossaryAndSearch(modules)
  const withReadings = modules.filter((m) => m.readings.length).length
  console.log(
    `Prepared readings for ${modules.length} modules (${withReadings} with on-site readings) → content/`,
  )
  return catalog
}

function slugify(term) {
  return term
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
}

function parseGlossaryMarkdown(md) {
  const sections = []
  let current = null
  for (const line of md.split('\n')) {
    const h2 = line.match(/^##\s+(.+)/)
    if (h2) {
      current = { title: h2[1].trim(), terms: [] }
      sections.push(current)
      continue
    }
    const row = line.match(/^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|/)
    if (row && current && !/^\|?\s*-+/.test(line) && !/Term/i.test(row[1])) {
      const raw = row[1].trim()
      const meaning = row[2].trim()
      const paren = raw.match(/^(.+?)\s*\(([A-Z0-9][A-Z0-9/+-]*)\)\s*$/)
      const term = paren ? paren[1].trim() : raw
      const abbrev = paren ? paren[2] : ''
      const id = slugify(abbrev || term)
      current.terms.push({ id, term, abbrev, meaning })
    }
  }
  return sections.filter((s) => s.terms.length)
}

function writeGlossaryAndSearch(modules) {
  const glossaryPath = join(COURSE_ROOT, 'GLOSSARY.md')
  const sections = existsSync(glossaryPath)
    ? parseGlossaryMarkdown(readFileSync(glossaryPath, 'utf8'))
    : []
  writeFileSync(
    join(DATA_DIR, 'glossary.json'),
    JSON.stringify({ generatedAt: new Date().toISOString(), sections }, null, 2) + '\n',
  )

  const entries = []
  for (const mod of modules) {
    entries.push({
      kind: 'module',
      id: mod.id,
      title: `${mod.number} — ${mod.title}`,
      moduleId: mod.id,
      moduleTitle: mod.title,
      topicId: null,
      body: `${mod.blurb} ${(mod.objectives || []).join(' ')} ${mod.language || ''}`,
      snippet: mod.blurb,
    })
    for (const r of mod.readings || []) {
      const fullPath = join(COURSE_ROOT, r.path)
      const body = existsSync(fullPath) ? readFileSync(fullPath, 'utf8') : ''
      entries.push({
        kind: 'reading',
        id: `${mod.id}:${r.id}`,
        title: r.label,
        moduleId: mod.id,
        moduleTitle: `${mod.number} ${mod.title}`,
        topicId: r.id,
        body,
        snippet: body.replace(/\s+/g, ' ').trim().slice(0, 160),
      })
    }
  }
  for (const section of sections) {
    for (const t of section.terms) {
      entries.push({
        kind: 'glossary',
        id: t.id,
        title: t.abbrev ? `${t.abbrev} — ${t.term}` : t.term,
        moduleId: null,
        moduleTitle: section.title,
        topicId: null,
        body: t.meaning,
        snippet: t.meaning.slice(0, 160),
      })
    }
  }
  writeFileSync(
    join(DATA_DIR, 'search-index.json'),
    JSON.stringify({ generatedAt: new Date().toISOString(), entries }, null, 2) + '\n',
  )
  console.log(
    `Glossary: ${sections.reduce((n, s) => n + s.terms.length, 0)} terms; search index: ${entries.length} entries`,
  )
}

const isMain =
  process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href

if (isMain) {
  prepareReadings()
}
