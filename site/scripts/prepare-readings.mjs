#!/usr/bin/env node
/**
 * Fast path: copy reading markdown (+ images) into site/content and
 * refresh catalog.json reading entries — no quiz PDF generation.
 *
 * Use this for site preview. Run prepare-downloads when you need
 * worksheet / test / quiz PDF packs.
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
    return {
      ...meta,
      hasModuleDir,
      worksheets: preserveDownloads ? prev.worksheets || [] : [],
      worksheetsZip: preserveDownloads ? prev.worksheetsZip ?? null : null,
      worksheetSingle: preserveDownloads ? prev.worksheetSingle ?? null : null,
      tests: preserveDownloads ? prev.tests || [] : [],
      testsZip: preserveDownloads ? prev.testsZip ?? null : null,
      quizzes: preserveDownloads ? prev.quizzes || [] : [],
      quizzesZip: preserveDownloads ? prev.quizzesZip ?? null : null,
      quizzesPdfZip: preserveDownloads ? prev.quizzesPdfZip ?? null : null,
      quizSingle: preserveDownloads ? prev.quizSingle ?? null : null,
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
  const withReadings = modules.filter((m) => m.readings.length).length
  console.log(
    `Prepared readings for ${modules.length} modules (${withReadings} with on-site readings) → content/`,
  )
  return catalog
}

const isMain =
  process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href

if (isMain) {
  prepareReadings()
}
