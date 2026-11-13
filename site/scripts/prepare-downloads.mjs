#!/usr/bin/env node
/**
 * Copy course worksheets / tests / quizzes / answer keys into site/downloads and
 * emit data/catalog.json for the student-facing UI.
 *
 * Quiz PDFs are questions only. Answer keys are separate downloads.
 * Readings: delegated to prepare-readings.mjs.
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
} from 'node:fs'
import { join, basename, dirname, relative } from 'node:path'
import { fileURLToPath } from 'node:url'
import { execFileSync } from 'node:child_process'
import { MODULE_META } from './course-meta.mjs'
import { prepareReadings } from './prepare-readings.mjs'

const __dirname = dirname(fileURLToPath(import.meta.url))
const SITE_ROOT = join(__dirname, '..')
const COURSE_ROOT = join(SITE_ROOT, '..')
const OUT_DIR = join(SITE_ROOT, 'downloads')
const DATA_DIR = join(SITE_ROOT, 'data')
const QUIZ_PDF_SCRIPT = join(__dirname, 'quiz_md_to_pdf.py')

function listFiles(dir, predicate) {
  if (!existsSync(dir)) return []
  return readdirSync(dir)
    .filter((name) => predicate(name))
    .map((name) => join(dir, name))
    .filter((path) => statSync(path).isFile())
    .sort()
}

function stripAnswerKey(markdown) {
  const patterns = [
    /\n---\s*\n+##\s*Answer key[\s\S]*$/i,
    /\n##\s*Answer key[\s\S]*$/i,
    /\n##\s*Answers?[\s\S]*$/i,
    /\n+Answer key:\s*\[[\s\S]*$/i,
  ]
  let out = markdown
  for (const re of patterns) {
    const next = out.replace(re, '\n')
    if (next !== out) {
      out = next
      break
    }
  }
  return out.trimEnd() + '\n'
}

function zipFiles(cwd, files, outZip) {
  if (!files.length) return false
  const rels = files.map((f) => relative(cwd, f))
  if (existsSync(outZip)) rmSync(outZip)
  execFileSync('zip', ['-q', '-j', outZip, ...rels], { cwd })
  return true
}

function ensureDir(path) {
  mkdirSync(path, { recursive: true })
}

function topicLabel(filename) {
  return basename(filename, '.md')
    .replace(/\.py$/, '')
    .replace(/^test_/, '')
    .replace(/_/g, ' ')
}

rmSync(OUT_DIR, { recursive: true, force: true })
ensureDir(OUT_DIR)
ensureDir(DATA_DIR)

const modules = []

for (const meta of MODULE_META) {
  const moduleDir = join(COURSE_ROOT, meta.id)
  const moduleOut = join(OUT_DIR, meta.id)
  ensureDir(moduleOut)

  const worksheetsSrc = listFiles(join(moduleDir, 'worksheets'), (n) => n.endsWith('.md'))
  const testsSrc = listFiles(
    join(moduleDir, 'tests'),
    (n) => n.startsWith('test_') && n.endsWith('.py'),
  )
  const quizzesSrc = listFiles(
    join(moduleDir, 'quizzes'),
    (n) => n.endsWith('.md') && !n.startsWith('README'),
  )
  const answerKeysSrc = listFiles(
    join(moduleDir, 'quizzes', 'answer-keys'),
    (n) => n.endsWith('.md'),
  )

  const worksheets = []
  if (worksheetsSrc.length) {
    const wDir = join(moduleOut, 'worksheets')
    ensureDir(wDir)
    for (const src of worksheetsSrc) {
      const name = basename(src)
      copyFileSync(src, join(wDir, name))
      worksheets.push({
        id: basename(name, '.md'),
        label: topicLabel(name),
        href: `downloads/${meta.id}/worksheets/${name}`,
        filename: name,
      })
    }
    if (worksheetsSrc.length > 1) {
      const zipPath = join(moduleOut, 'worksheets.zip')
      zipFiles(
        wDir,
        worksheetsSrc.map((s) => join(wDir, basename(s))),
        zipPath,
      )
    }
  }

  const tests = []
  if (testsSrc.length) {
    const tDir = join(moduleOut, 'tests')
    ensureDir(tDir)
    for (const src of testsSrc) {
      const name = basename(src)
      copyFileSync(src, join(tDir, name))
      tests.push({
        id: basename(name, '.py').replace(/^test_/, ''),
        label: topicLabel(name),
        href: `downloads/${meta.id}/tests/${name}`,
        filename: name,
      })
    }
    const initSrc = join(moduleDir, 'tests', '__init__.py')
    if (existsSync(initSrc)) copyFileSync(initSrc, join(tDir, '__init__.py'))
    const zipPath = join(moduleOut, 'tests.zip')
    const zipInputs = readdirSync(tDir).map((n) => join(tDir, n))
    zipFiles(tDir, zipInputs, zipPath)
  }

  const answerKeyById = new Map()
  if (answerKeysSrc.length) {
    const kDir = join(moduleOut, 'answer-keys')
    ensureDir(kDir)
    for (const src of answerKeysSrc) {
      const name = basename(src)
      copyFileSync(src, join(kDir, name))
      const id = basename(name, '.md')
      answerKeyById.set(id, {
        id,
        label: topicLabel(name),
        href: `downloads/${meta.id}/answer-keys/${name}`,
        filename: name,
      })
    }
    if (answerKeysSrc.length > 1) {
      zipFiles(
        kDir,
        answerKeysSrc.map((s) => join(kDir, basename(s))),
        join(moduleOut, 'answer-keys.zip'),
      )
    }
  }

  const quizzes = []
  if (quizzesSrc.length) {
    const qDir = join(moduleOut, 'quizzes')
    ensureDir(qDir)
    for (const src of quizzesSrc) {
      const name = basename(src)
      const stripped = stripAnswerKey(readFileSync(src, 'utf8'))
      if (/##\s*Answer key/i.test(stripped)) {
        console.warn(`quiz still contains answer key heading: ${meta.id}/${name}`)
      }
      const mdOut = join(qDir, name)
      writeFileSync(mdOut, stripped, 'utf8')
      const id = basename(name, '.md')
      const pdfName = `${id}.pdf`
      const pdfOut = join(qDir, pdfName)
      let pdfHref = null
      try {
        execFileSync('python3', [QUIZ_PDF_SCRIPT, mdOut, pdfOut], {
          stdio: ['ignore', 'pipe', 'pipe'],
        })
        if (existsSync(pdfOut)) {
          pdfHref = `downloads/${meta.id}/quizzes/${pdfName}`
        }
      } catch (err) {
        const detail = err?.stderr?.toString?.() || err?.message || String(err)
        console.warn(`quiz PDF skipped for ${meta.id}/${name}: ${detail.trim()}`)
      }
      const key = answerKeyById.get(id)
      quizzes.push({
        id,
        label: topicLabel(name),
        href: `downloads/${meta.id}/quizzes/${name}`,
        filename: name,
        pdfHref,
        pdfFilename: pdfHref ? pdfName : null,
        answerKeyHref: key?.href || null,
      })
    }
    const pdfFiles = quizzes
      .filter((q) => q.pdfFilename)
      .map((q) => join(qDir, q.pdfFilename))
    if (pdfFiles.length > 1) {
      zipFiles(qDir, pdfFiles, join(moduleOut, 'quizzes-pdf.zip'))
    }
    if (quizzes.length > 1) {
      zipFiles(
        qDir,
        quizzes.map((q) => join(qDir, q.filename)),
        join(moduleOut, 'quizzes.zip'),
      )
    }
  }

  modules.push({
    ...meta,
    hasModuleDir: existsSync(moduleDir),
    worksheets,
    worksheetsZip:
      worksheets.length > 1 ? `downloads/${meta.id}/worksheets.zip` : null,
    worksheetSingle: worksheets.length === 1 ? worksheets[0] : null,
    tests,
    testsZip: tests.length ? `downloads/${meta.id}/tests.zip` : null,
    quizzes,
    quizzesZip: quizzes.length > 1 ? `downloads/${meta.id}/quizzes.zip` : null,
    quizzesPdfZip:
      quizzes.filter((q) => q.pdfHref).length > 1
        ? `downloads/${meta.id}/quizzes-pdf.zip`
        : null,
    quizSingle: quizzes.length === 1 ? quizzes[0] : null,
    answerKeysZip:
      answerKeyById.size > 1 ? `downloads/${meta.id}/answer-keys.zip` : null,
    readings: [],
  })
}

const catalog = {
  brand: 'MailGuard Course',
  tagline:
    'Cloud-security learning for students building identity, email DLP, and secure SaaS skills.',
  generatedAt: new Date().toISOString(),
  modules,
}

writeFileSync(join(DATA_DIR, 'catalog.json'), JSON.stringify(catalog, null, 2) + '\n')

const withWorksheets = modules.filter((m) => m.worksheets.length).length
const withTests = modules.filter((m) => m.tests.length).length
const withQuizPdfs = modules.reduce(
  (n, m) => n + m.quizzes.filter((q) => q.pdfHref).length,
  0,
)
const withKeys = modules.reduce(
  (n, m) => n + m.quizzes.filter((q) => q.answerKeyHref).length,
  0,
)
console.log(
  `Prepared downloads for ${modules.length} modules (${withWorksheets} worksheets, ${withTests} tests, ${withQuizPdfs} quiz PDFs, ${withKeys} answer keys) → downloads/`,
)

prepareReadings({ preserveDownloads: true })
