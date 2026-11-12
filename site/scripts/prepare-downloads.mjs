#!/usr/bin/env node
/**
 * Copy course worksheets / tests into site/downloads and
 * emit data/catalog.json for the student-facing UI.
 *
 * Quizzes: questions only — answer-key sections are stripped when present.
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

const __dirname = dirname(fileURLToPath(import.meta.url))
const SITE_ROOT = join(__dirname, '..')
const COURSE_ROOT = join(SITE_ROOT, '..')
const OUT_DIR = join(SITE_ROOT, 'downloads')
const DATA_DIR = join(SITE_ROOT, 'data')
const QUIZ_PDF_SCRIPT = join(__dirname, 'quiz_md_to_pdf.py')

const MODULE_META = [
  {
    id: '01-challenge-gym',
    number: '01',
    title: 'Challenge Gym',
    phase: 'Foundations',
    blurb:
      'Short Python katas with pytest contracts — TOTP, hold rules, recipient risk, and crypto hygiene.',
    hours: '8–10 h',
  },
  {
    id: '02-mailguard-mfa',
    number: '02',
    title: 'MailGuard MFA',
    phase: 'Identity & access',
    blurb: 'TOTP enroll/verify, recovery codes, and passkeys / WebAuthn literacy.',
    hours: '10–12 h',
  },
  {
    id: '03-oidc-access',
    number: '03',
    title: 'OIDC / access policy',
    phase: 'Identity & access',
    blurb: 'Happy-path OIDC, SAML comparison, and identity-depth worksheet practice.',
    hours: '10–12 h',
  },
  {
    id: '04-ztna-lite',
    number: '04',
    title: 'ZTNA lite',
    phase: 'Identity & access',
    blurb: 'VPN vs zero-trust access — diagrams and compare tables, no commercial mesh required.',
    hours: '3–5 h',
  },
  {
    id: '05-email-auth',
    number: '05',
    title: 'Email authentication',
    phase: 'Email & DLP literacy',
    blurb: 'SPF, DKIM, DMARC, and a dmarc_policy kata with tests.',
    hours: '6–8 h',
  },
  {
    id: '06-threat-model',
    number: '06',
    title: 'Threat model / secure SDLC',
    phase: 'Email & DLP literacy',
    blurb: 'STRIDE-lite on the hold path plus a lightweight SAMM self-check.',
    hours: '5–7 h',
  },
  {
    id: '07-mailguard-api',
    number: '07',
    title: 'MailGuard API',
    phase: 'Product build',
    blurb: 'FastAPI rules API for hold / allow / reject.',
    hours: '12–16 h',
  },
  {
    id: '08-mailguard-admin',
    number: '08',
    title: 'MailGuard Admin',
    phase: 'Product build',
    blurb: 'TypeScript/Vue admin for rules and the hold queue.',
    hours: '12–16 h',
  },
  {
    id: '09-mailguard-worker',
    number: '09',
    title: 'MailGuard Worker',
    phase: 'Product build',
    blurb: 'Queue worker path for applying MailGuard decisions.',
    hours: '10–12 h',
  },
  {
    id: '10-secure-drop',
    number: '10',
    title: 'Secure Drop',
    phase: 'Product build',
    blurb: 'Expiring share links, audit, and cloud-share DLP literacy.',
    hours: '10–12 h',
  },
  {
    id: '11-security-notes',
    number: '11',
    title: 'Security notes',
    phase: 'Product build',
    blurb: 'OWASP-mapped lab notes tied to MailGuard mitigations.',
    hours: '6–8 h',
  },
  {
    id: '12-ci-aws',
    number: '12',
    title: 'CI + AWS',
    phase: 'Cloud & platform',
    blurb: 'PR CI and a documented cloud deploy — no secrets in git.',
    hours: '8–10 h',
  },
  {
    id: '13-infra',
    number: '13',
    title: 'Infra',
    phase: 'Cloud & platform',
    blurb: 'Compose + Terraform story with IAM / misconfig posture worksheet.',
    hours: '12–14 h',
  },
  {
    id: '14-k8s-local',
    number: '14',
    title: 'K8s local',
    phase: 'Stretch',
    blurb: 'kind/minikube deploy with probes and resource requests.',
    hours: '10–12 h',
  },
  {
    id: '15-observability',
    number: '15',
    title: 'Observability',
    phase: 'Stretch',
    blurb: 'Golden signals plus SLI/SLO and a lightweight postmortem worksheet.',
    hours: '10–12 h',
  },
  {
    id: '16-gitops-policy',
    number: '16',
    title: 'GitOps + policy',
    phase: 'Stretch',
    blurb: 'Sync flow and policy-as-code checks on manifests.',
    hours: '6–8 h',
  },
  {
    id: '17-phish-lite',
    number: '17',
    title: 'Phish Lite',
    phase: 'Optional',
    blurb: 'Optional phishing-awareness quiz UI for learning honesty practice.',
    hours: '6–8 h',
  },
  {
    id: '18-oss-ux-stretch',
    number: '18',
    title: 'OSS + security UX',
    phase: 'Optional',
    blurb: 'Upstream contribution hygiene and security-warning UX reflection.',
    hours: '3–6 h',
  },
]

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
    // Separate answer-key docs (link-only footer)
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
  const readingsSrc = listFiles(
    join(moduleDir, 'readings'),
    (n) => n.endsWith('.md') && !n.startsWith('README'),
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

  const quizzes = []
  if (quizzesSrc.length) {
    const qDir = join(moduleOut, 'quizzes')
    ensureDir(qDir)
    for (const src of quizzesSrc) {
      const name = basename(src)
      const stripped = stripAnswerKey(readFileSync(src, 'utf8'))
      if (/##\s*Answer key/i.test(stripped)) continue
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
      quizzes.push({
        id,
        label: topicLabel(name),
        href: `downloads/${meta.id}/quizzes/${name}`,
        filename: name,
        pdfHref,
        pdfFilename: pdfHref ? pdfName : null,
      })
    }
    const pdfFiles = quizzes
      .filter((q) => q.pdfFilename)
      .map((q) => join(qDir, q.pdfFilename))
    if (pdfFiles.length > 1) {
      const zipPath = join(moduleOut, 'quizzes-pdf.zip')
      zipFiles(qDir, pdfFiles, zipPath)
    }
    if (quizzes.length > 1) {
      const zipPath = join(moduleOut, 'quizzes.zip')
      zipFiles(
        qDir,
        quizzes.map((q) => join(qDir, q.filename)),
        zipPath,
      )
    }
  }

  const readings = readingsSrc.map((src) => ({
    id: basename(src, '.md'),
    label: topicLabel(basename(src)),
    path: relative(COURSE_ROOT, src).replace(/\\/g, '/'),
  }))

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
    readings,
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
console.log(
  `Prepared downloads for ${modules.length} modules (${withWorksheets} with worksheets, ${withTests} with tests, ${withQuizPdfs} quiz PDFs) → downloads/`,
)
