import { withBase } from './base.js'
import { initTheme } from './theme.js'
import {
  loadProgress,
  saveProgress,
  resumeHref,
  resumeLabel,
  resetProgress,
  isModuleComplete,
} from './progress.js'

initTheme()

const NAME_KEY = 'certificateName'

function quizTopics(mod) {
  return (mod.quizzes || []).map((q) => q.id)
}

function allQuizzesComplete(state, modules) {
  const required = []
  for (const mod of modules) {
    for (const qid of quizTopics(mod)) {
      required.push(`${mod.id}::${qid}`)
    }
  }
  // Modules with no quizzes (e.g. Module 00) do not block on quiz topics.
  if (!required.length) return true
  return required.every((k) => state.completedTopics[k])
}

function allModulesComplete(state, modules) {
  if (!modules.length) return false
  return modules.every((m) => isModuleComplete(state, m.id))
}

function certificateReady(state, modules) {
  return allModulesComplete(state, modules) && allQuizzesComplete(state, modules)
}

async function main() {
  const catalogRes = await fetch(withBase('data/catalog.json'))
  if (!catalogRes.ok) {
    document.getElementById('cert-root').innerHTML =
      '<p class="empty-note">Catalog missing. Run prepare-readings.</p>'
    return
  }
  const catalog = await catalogRes.json()
  const resume = document.getElementById('resume-cta')
  if (resume) {
    resume.href = withBase(resumeHref(catalog.modules))
    resume.textContent = resumeLabel(catalog.modules)
  }
  document.getElementById('reset-progress')?.addEventListener('click', () => {
    if (confirm('Reset all course progress stored in this browser?')) {
      resetProgress()
      location.reload()
    }
  })

  const state = loadProgress()
  const nameInput = document.getElementById('student-name')
  nameInput.value = state.certificateName || localStorage.getItem(NAME_KEY) || ''
  nameInput.addEventListener('change', () => {
    const s = loadProgress()
    s.certificateName = nameInput.value.trim()
    saveProgress(s)
    localStorage.setItem(NAME_KEY, s.certificateName)
    render()
  })

  function render() {
    const s = loadProgress()
    const ready = certificateReady(s, catalog.modules)
    const doneMods = catalog.modules.filter((m) => isModuleComplete(s, m.id)).length
    const quizNeed = catalog.modules.reduce((n, m) => n + quizTopics(m).length, 0)
    const quizDone = catalog.modules.reduce(
      (n, m) => n + quizTopics(m).filter((id) => s.completedTopics[`${m.id}::${id}`]).length,
      0,
    )
    const root = document.getElementById('cert-root')
    const student = (s.certificateName || '').trim() || 'Student'
    root.innerHTML = `
      <p class="muted">Modules marked complete: <strong>${doneMods}</strong> / ${catalog.modules.length}.
      Quiz topics marked complete: <strong>${quizDone}</strong> / ${quizNeed} (modules without quizzes, such as Setup, skip this count).</p>
      ${
        ready
          ? `<div class="certificate-card" id="certificate-card">
              <p class="module-kicker">MailGuard Course</p>
              <h2>Certificate of completion</h2>
              <p>This certifies that</p>
              <p class="cert-name">${student}</p>
              <p>completed every MailGuard Course module in this browser’s progress record (including all required quizzes where a module has them).</p>
              <p class="muted">Generated locally — not a university or employer credential.</p>
              <button type="button" class="btn btn-primary" id="print-cert">Print / save PDF</button>
            </div>`
          : `<p class="empty-note">Mark <strong>every module</strong> complete, and mark each module’s quiz topics complete where quizzes exist, to unlock the certificate. Module 00 has no quiz — use its module checkbox only. Enter your name above — it stays in this browser only.</p>`
      }
    `
    document.getElementById('print-cert')?.addEventListener('click', () => window.print())
  }
  render()
}

main()
