import { marked } from 'https://cdn.jsdelivr.net/npm/marked@12.0.2/lib/marked.esm.js'
import { withBase } from './base.js'
import { initTheme } from './theme.js'
import {
  loadProgress,
  markModuleVisited,
  setModuleComplete,
  setTopicComplete,
  isModuleComplete,
  isTopicComplete,
  resumeHref,
  resumeLabel,
  resetProgress,
} from './progress.js'
import { initGlossaryTooltips } from './glossary-tooltip.js'

initTheme()

let glossaryTerms = []

const params = new URLSearchParams(location.search)
const id = params.get('id') || '00-setup'
const root = document.getElementById('module-root')
const crumb = document.getElementById('crumb-current')
const adjacent = document.getElementById('module-adjacent')
const resumeCta = document.getElementById('resume-cta')
const resetBtn = document.getElementById('reset-progress')

function titleCase(label) {
  return label.replace(/\b\w/g, (c) => c.toUpperCase())
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
}

function readingBase(href) {
  const parts = href.split('/')
  parts.pop()
  return parts.join('/')
}

function resolveAssetUrl(src, base) {
  if (!src || /^(https?:|data:|mailto:|#)/i.test(src)) return src
  if (src.startsWith('/')) return src
  return `${base}/${src}`.replace(/\/{2,}/g, '/')
}

function enhanceFigures(html, base) {
  const wrap = document.createElement('div')
  wrap.innerHTML = html
  wrap.querySelectorAll('img').forEach((img) => {
    const src = img.getAttribute('src') || ''
    img.setAttribute('src', resolveAssetUrl(src, base))
    img.loading = 'lazy'
    const caption = (img.getAttribute('alt') || '').trim()
    if (!caption) return
    if (img.parentElement?.tagName === 'FIGURE') {
      let figcap = img.parentElement.querySelector('figcaption')
      if (!figcap) {
        figcap = document.createElement('figcaption')
        img.parentElement.appendChild(figcap)
      }
      figcap.textContent = caption
      return
    }
    const figure = document.createElement('figure')
    figure.className = 'reading-figure'
    img.replaceWith(figure)
    figure.appendChild(img)
    const figcap = document.createElement('figcaption')
    figcap.textContent = caption
    figure.appendChild(figcap)
  })
  wrap.querySelectorAll('a[href]').forEach((a) => {
    const href = a.getAttribute('href') || ''
    if (/^(https?:)?\/\//i.test(href) || href.startsWith('mailto:')) {
      a.setAttribute('target', '_blank')
      a.setAttribute('rel', 'noopener noreferrer')
    } else if (!href.startsWith('#') && !href.startsWith('mailto:')) {
      a.setAttribute('href', resolveAssetUrl(href, base))
    }
  })
  return wrap.innerHTML
}

function linkGlossaryTerms(html) {
  if (!glossaryTerms.length) return html
  const wrap = document.createElement('div')
  wrap.innerHTML = html
  const skip = new Set([
    'A',
    'CODE',
    'PRE',
    'ABBR',
    'SCRIPT',
    'STYLE',
    'H1',
    'H2',
    'H3',
    'H4',
    'H5',
    'H6',
    'FIGCAPTION',
    'KBD',
    'SAMP',
  ])
  const terms = [...glossaryTerms]
    .filter((t) => t.abbrev && t.abbrev.length >= 2)
    .sort((a, b) => b.abbrev.length - a.abbrev.length)
  const linked = new Set()
  const walk = (node) => {
    if (node.nodeType === Node.ELEMENT_NODE) {
      if (skip.has(node.tagName)) return
      ;[...node.childNodes].forEach(walk)
      return
    }
    if (node.nodeType !== Node.TEXT_NODE) return
    const text = node.nodeValue
    if (!text || !/\S/.test(text)) return
    for (const t of terms) {
      if (linked.has(t.id)) continue
      const re = new RegExp(`\\b(${t.abbrev.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})\\b`)
      const m = re.exec(text)
      if (!m) continue
      const span = document.createElement('span')
      span.appendChild(document.createTextNode(text.slice(0, m.index)))
      const a = document.createElement('a')
      a.href = withBase(`glossary.html#${t.id}`)
      a.className = 'glossary-ref'
      a.setAttribute('data-glossary-id', t.id)
      a.setAttribute('data-glossary-term', t.term || '')
      a.setAttribute('data-glossary-abbrev', t.abbrev || '')
      a.setAttribute('data-glossary-meaning', t.meaning || '')
      a.textContent = m[1]
      span.appendChild(a)
      span.appendChild(document.createTextNode(text.slice(m.index + m[0].length)))
      node.replaceWith(span)
      linked.add(t.id)
      ;[...span.childNodes].forEach(walk)
      return
    }
  }
  walk(wrap)
  return wrap.innerHTML
}

/** Drop authorship bylines, raw quiz/assignment footer lines; strip (`id`) from titles. */
function polishReadingHtml(html) {
  const wrap = document.createElement('div')
  wrap.innerHTML = html
  wrap.querySelectorAll('p').forEach((p) => {
    const text = (p.textContent || '').trim()
    if (/^Authorship:/i.test(text)) p.remove()
  })
  wrap.querySelectorAll('a[href]').forEach((a) => {
    const href = a.getAttribute('href') || ''
    if (!/\/(quizzes|assignments)\//.test(href) && !/\.\.\/(quizzes|assignments)\//.test(href)) return
    const p = a.closest('p')
    if (!p) return
    const text = p.textContent || ''
    if (/after this reading|continue with the assignment/i.test(text) || /quizzes\/|assignments\//.test(text)) {
      const heading = p.previousElementSibling
      if (heading && /^H[1-6]$/.test(heading.tagName) && /quiz|next step/i.test(heading.textContent || '')) {
        heading.remove()
      }
      p.remove()
    }
  })
  wrap.querySelectorAll('h1, h2, h3').forEach((h) => {
    h.textContent = h.textContent.replace(/\s*\(`[^`]+`\)\s*/g, '').replace(/\s+/g, ' ').trim()
  })
  return wrap.innerHTML
}

async function loadReadingHtml(reading) {
  if (!reading?.href) {
    return `<p class="empty-note">Reading file not prepared. Run <code>npm run prepare-readings</code> from <code>site/</code>.</p>`
  }
  try {
    const res = await fetch(withBase(reading.href))
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const md = await res.text()
    const raw = marked.parse(md, { async: false })
    const enhanced = enhanceFigures(raw, readingBase(reading.href))
    return linkGlossaryTerms(polishReadingHtml(enhanced))
  } catch {
    return `<p class="empty-note">Could not load <code>${escapeHtml(reading.href)}</code>. Run <code>npm run prepare-readings</code>.</p>`
  }
}

function downloadButtonsForTopic(mod, topicId) {
  const assignment = mod.assignments.find((w) => w.id === topicId)
  const test = mod.tests.find((t) => t.id === topicId)
  const quiz = mod.quizzes.find((q) => q.id === topicId)
  const buttons = []
  if (assignment) {
    buttons.push(
      `<a class="btn btn-download" download href="${withBase(assignment.href)}">Download assignment</a>`,
    )
  }
  if (quiz?.pdfHref) {
    buttons.push(
      `<a class="btn btn-download" download href="${withBase(quiz.pdfHref)}">Quiz</a>`,
    )
  } else if (quiz?.href) {
    buttons.push(
      `<a class="btn btn-download" download href="${withBase(quiz.href)}">Quiz</a>`,
    )
  }
  if (quiz?.answerKeyHref) {
    buttons.push(
      `<a class="btn btn-download btn-key" download href="${withBase(quiz.answerKeyHref)}">Quiz Answer Key</a>`,
    )
  }
  if (test) {
    buttons.push(
      `<a class="btn btn-download" download href="${withBase(test.href)}">Tests</a>`,
    )
  }
  return buttons
}

async function main() {
  const [res, glossRes] = await Promise.all([
    fetch(withBase('data/catalog.json')),
    fetch(withBase('data/glossary.json')),
  ])
  if (!res.ok) {
    root.innerHTML =
      '<p class="empty-note">Catalog missing. Run <code>npm run prepare-readings</code> (fast) or <code>npm run prepare-downloads</code> from <code>site/</code>.</p>'
    return
  }

  if (glossRes.ok) {
    const gloss = await glossRes.json()
    glossaryTerms = gloss.sections.flatMap((s) => s.terms)
  }

  const catalog = await res.json()
  if (resumeCta) {
    resumeCta.href = withBase(resumeHref(catalog.modules))
    resumeCta.textContent = resumeLabel(catalog.modules)
  }
  resetBtn?.addEventListener('click', () => {
    if (!confirm('Reset all course progress stored in this browser?')) return
    resetProgress()
    location.reload()
  })

  const index = catalog.modules.findIndex((m) => m.id === id)
  const mod = catalog.modules[index]

  if (!mod) {
    document.title = 'Module not found — MailGuard Course'
    crumb.textContent = 'Not found'
    root.innerHTML = `
      <h1>Module not found</h1>
      <p class="muted">That module id is not in the syllabus. <a href="index.html#syllabus">Back to syllabus</a>.</p>
    `
    return
  }

  markModuleVisited(mod.id)
  document.title = `${mod.number} — ${mod.title} · MailGuard Course`
  crumb.textContent = `${mod.number} ${mod.title}`

  const assignmentButtons = []
  if (mod.assignmentsZip) {
    assignmentButtons.push(
      `<a class="btn btn-download" download href="${withBase(mod.assignmentsZip)}">Download assignments (zip)</a>`,
    )
  } else if (mod.assignmentSingle) {
    assignmentButtons.push(
      `<a class="btn btn-download" download href="${withBase(mod.assignmentSingle.href)}">Download assignment</a>`,
    )
  }

  if (mod.testsZip) {
    assignmentButtons.push(
      `<a class="btn btn-download" download href="${withBase(mod.testsZip)}">Download tests (zip)</a>`,
    )
  }

  const quizButtons = []
  if (mod.quizzesPdfZip) {
    quizButtons.push(
      `<a class="btn btn-download" download href="${withBase(mod.quizzesPdfZip)}">Download quizzes (PDF zip)</a>`,
    )
  } else {
    const singlePdf = mod.quizzes.find((q) => q.pdfHref)
    if (singlePdf?.pdfHref) {
      quizButtons.push(
        `<a class="btn btn-download" download href="${withBase(singlePdf.pdfHref)}">Quiz</a>`,
      )
    }
  }
  if (mod.answerKeysZip) {
    quizButtons.push(
      `<a class="btn btn-download btn-key" download href="${withBase(mod.answerKeysZip)}">Quiz Answer Keys (zip)</a>`,
    )
  } else {
    const singleKey = mod.quizzes.find((q) => q.answerKeyHref)
    if (singleKey?.answerKeyHref) {
      quizButtons.push(
        `<a class="btn btn-download btn-key" download href="${withBase(singleKey.answerKeyHref)}">Quiz Answer Key</a>`,
      )
    }
  }

  const topicIds = [
    ...new Set([
      ...mod.readings.map((r) => r.id),
      ...mod.assignments.map((w) => w.id),
      ...mod.quizzes.map((q) => q.id),
      ...mod.tests.map((t) => t.id),
    ]),
  ]

  let state = loadProgress()
  const topicSections = []
  for (const topicId of topicIds) {
    const reading = mod.readings.find((r) => r.id === topicId)
    const label =
      reading?.label ||
      mod.assignments.find((w) => w.id === topicId)?.label ||
      mod.quizzes.find((q) => q.id === topicId)?.label ||
      mod.tests.find((t) => t.id === topicId)?.label ||
      topicId
    const buttons = downloadButtonsForTopic(mod, topicId)
    const readingHtml = reading
      ? await loadReadingHtml(reading)
      : `<p class="muted">No on-site reading for this topic yet.</p>`
    const topicDone = isTopicComplete(state, mod.id, topicId)
    const topicHint = buttons.length
      ? 'Read on this page, then download the assignment, required quiz, and tests. Use the answer key only after you attempt the quiz.'
      : 'Read on this page, then mark the topic complete when you finish.'
    const downloadsBlock = buttons.length
      ? `<div class="topic-downloads">
          <h3>Downloads</h3>
          <div class="download-actions">${buttons.join('')}</div>
        </div>`
      : ''

    topicSections.push(`
      <article class="topic-block" id="topic-${escapeHtml(topicId)}" data-topic="${escapeHtml(topicId)}">
        <header class="topic-block-header">
          <div class="topic-title-row">
            <h2>${escapeHtml(titleCase(label))}</h2>
            <label class="progress-toggle">
              <input type="checkbox" data-topic-complete="${escapeHtml(topicId)}" ${topicDone ? 'checked' : ''} />
              Topic complete
            </label>
          </div>
          <p class="muted">${topicHint}</p>
        </header>
        <div class="reading-body">${readingHtml}</div>
        ${downloadsBlock}
      </article>
    `)
  }

  const packEmpty =
    !mod.assignments.length && !mod.tests.length && !mod.quizzes.some((q) => q.pdfHref || q.href)
  const readingsEmpty = !mod.readings.length
  const moduleDone = isModuleComplete(state, mod.id)

  const aiNotice =
    mod.id === '00-setup'
      ? `<aside class="ai-notice" role="note" aria-label="AI assistance notice">
          <strong>AI assistance notice.</strong>
          This course's content was researched and compiled with AI assistance. It has been reviewed for accuracy, but verify anything important against the linked primary sources (RFCs, official docs).
        </aside>`
      : ''

  root.innerHTML = `
    ${aiNotice}
    <p class="module-kicker">${escapeHtml(mod.phase)} · ${escapeHtml(mod.hours)}</p>
    <h1>${escapeHtml(mod.number)} — ${escapeHtml(mod.title)}</h1>
    <p class="module-blurb">${escapeHtml(mod.blurb)}</p>
    <p class="language-chip"><span>Language / tooling</span> ${escapeHtml(mod.language || 'See module README')}${
      mod.languageDetail
        ? ` — <span class="language-detail">${escapeHtml(mod.languageDetail)}</span>`
        : ''
    }</p>
    ${
      (mod.objectives || []).length
        ? `<section class="objectives" aria-label="Learning objectives">
            <h2>Learning objectives</h2>
            <ul>${mod.objectives.map((o) => `<li>${escapeHtml(o)}</li>`).join('')}</ul>
          </section>`
        : ''
    }
    <label class="progress-toggle module-complete-toggle">
      <input type="checkbox" id="module-complete" ${moduleDone ? 'checked' : ''} />
      Mark module complete
    </label>

    ${
      packEmpty
        ? readingsEmpty
          ? `<p class="empty-note">This module is a build / stretch step. Readings and downloads appear here when those assets exist.</p>`
          : ''
        : `<section class="download-panel" aria-label="Module download packs">
      <h2>Module download packs</h2>
      <p>Required path: read on-site → assignment → tests (when present) → <strong>required quiz</strong>. Quiz PDFs are fillable questions only; answer keys are separate downloads. Save finished work under <code>my-work/</code>.</p>
      <div class="download-actions">
        ${assignmentButtons.join('') || '<span class="muted">No assignment pack for this module yet.</span>'}
        ${quizButtons.join('')}
      </div>
    </section>`
    }

    <section class="topics" aria-label="Topics">
      <h2 class="topics-heading">Topics</h2>
      ${
        topicSections.join('') ||
        `<p class="empty-note">No topics with readings or downloads yet for this module.</p>`
      }
    </section>
  `

  initGlossaryTooltips(root)

  root.querySelector('#module-complete')?.addEventListener('change', (e) => {
    setModuleComplete(mod.id, e.target.checked)
    if (resumeCta) {
      resumeCta.href = withBase(resumeHref(catalog.modules))
      resumeCta.textContent = resumeLabel(catalog.modules)
    }
  })
  root.querySelectorAll('[data-topic-complete]').forEach((input) => {
    input.addEventListener('change', (e) => {
      const topicId = e.target.getAttribute('data-topic-complete')
      setTopicComplete(mod.id, topicId, e.target.checked)
      markModuleVisited(mod.id, topicId)
    })
  })

  const hash = location.hash.replace(/^#topic-/, '')
  if (hash) {
    markModuleVisited(mod.id, hash)
    document.getElementById(`topic-${hash}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  const prev = catalog.modules[index - 1]
  const next = catalog.modules[index + 1]
  adjacent.innerHTML = `
    ${
      prev
        ? `<a href="${withBase(`module.html?id=${encodeURIComponent(prev.id)}`)}">← ${prev.number} ${escapeHtml(prev.title)}</a>`
        : '<span></span>'
    }
    ${
      next
        ? `<a href="${withBase(`module.html?id=${encodeURIComponent(next.id)}`)}">${next.number} ${escapeHtml(next.title)} →</a>`
        : '<span></span>'
    }
  `
}

main()
