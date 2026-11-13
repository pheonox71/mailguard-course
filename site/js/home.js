import { withBase } from './base.js'
import { initTheme } from './theme.js'
import {
  loadProgress,
  resetProgress,
  isModuleComplete,
  resumeHref,
  resumeLabel,
} from './progress.js'

initTheme()

const list = document.getElementById('module-list')
const resumeCta = document.getElementById('resume-cta')
const heroResume = document.getElementById('hero-resume')
const progressSummary = document.getElementById('progress-summary')
const resetBtn = document.getElementById('reset-progress')

function assetsHint(mod) {
  const bits = []
  if ((mod.readings || []).length) {
    bits.push(`${mod.readings.length} reading${mod.readings.length > 1 ? 's' : ''}`)
  }
  if (mod.worksheets.length) {
    bits.push(`${mod.worksheets.length} worksheet${mod.worksheets.length > 1 ? 's' : ''}`)
  }
  if (mod.tests.length) {
    bits.push(`${mod.tests.length} test file${mod.tests.length > 1 ? 's' : ''}`)
  }
  const pdfCount = (mod.quizzes || []).filter((q) => q.pdfHref).length
  if (pdfCount) {
    bits.push(`${pdfCount} quiz PDF${pdfCount > 1 ? 's' : ''}`)
  }
  if (mod.language) bits.push(mod.language)
  return bits.length ? bits.join(' · ') : 'Build module'
}

function renderResume(modules) {
  const href = resumeHref(modules)
  const label = resumeLabel(modules)
  if (resumeCta) {
    resumeCta.href = withBase(href)
    resumeCta.textContent = label
  }
  if (heroResume) {
    heroResume.href = withBase(href)
    heroResume.textContent = label
  }
  const state = loadProgress()
  const done = modules.filter((m) => isModuleComplete(state, m.id)).length
  if (progressSummary) {
    progressSummary.textContent = `${done} / ${modules.length} modules marked complete`
  }
}

function renderList(modules) {
  const state = loadProgress()
  list.innerHTML = modules
    .map((mod) => {
      const done = isModuleComplete(state, mod.id)
      return `
    <a class="module-row${done ? ' is-complete' : ''}" href="${withBase(`module.html?id=${encodeURIComponent(mod.id)}`)}">
      <div class="module-num" aria-hidden="true">${done ? '✓' : mod.number}</div>
      <div>
        <span class="phase-label">${mod.phase}</span>
        <h3>${mod.title}${done ? ' <span class="sr-only">(complete)</span>' : ''}</h3>
        <p>${mod.blurb}</p>
      </div>
      <div class="module-meta">
        <div>${mod.hours}</div>
        <div>${assetsHint(mod)}</div>
      </div>
    </a>`
    })
    .join('')
}

async function main() {
  const res = await fetch(withBase('data/catalog.json'))
  if (!res.ok) {
    list.innerHTML =
      '<p class="empty-note">Catalog missing. Run <code>npm run prepare-readings</code> (fast) or <code>npm run prepare-downloads</code> from <code>site/</code>.</p>'
    return
  }
  const catalog = await res.json()
  renderList(catalog.modules)
  renderResume(catalog.modules)

  resetBtn?.addEventListener('click', () => {
    if (!confirm('Reset all course progress stored in this browser?')) return
    resetProgress()
    renderList(catalog.modules)
    renderResume(catalog.modules)
  })
}

main()
