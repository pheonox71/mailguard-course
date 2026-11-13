import { withBase } from './base.js'
import { initTheme } from './theme.js'
import { resumeHref, resumeLabel, loadProgress, resetProgress } from './progress.js'

initTheme()

async function main() {
  const [glossaryRes, catalogRes] = await Promise.all([
    fetch(withBase('data/glossary.json')),
    fetch(withBase('data/catalog.json')),
  ])
  const resume = document.getElementById('resume-cta')
  if (catalogRes.ok) {
    const catalog = await catalogRes.json()
    if (resume) {
      resume.href = withBase(resumeHref(catalog.modules))
      resume.textContent = resumeLabel(catalog.modules)
    }
  }
  document.getElementById('reset-progress')?.addEventListener('click', () => {
    if (confirm('Reset all course progress stored in this browser?')) {
      resetProgress()
      location.reload()
    }
  })

  const root = document.getElementById('glossary-root')
  if (!glossaryRes.ok) {
    root.innerHTML = '<p class="empty-note">Glossary data missing. Run <code>npm run prepare-readings</code>.</p>'
    return
  }
  const data = await glossaryRes.json()
  const q = document.getElementById('glossary-filter')
  const render = () => {
    const needle = (q?.value || '').trim().toLowerCase()
    root.innerHTML = data.sections
      .map((section) => {
        const terms = section.terms.filter(
          (t) =>
            !needle ||
            t.term.toLowerCase().includes(needle) ||
            t.abbrev.toLowerCase().includes(needle) ||
            t.meaning.toLowerCase().includes(needle),
        )
        if (!terms.length) return ''
        return `
          <section class="glossary-section">
            <h2>${section.title}</h2>
            <dl>
              ${terms
                .map(
                  (t) => {
                    const label = t.abbrev
                      ? `<abbr title="${t.term}">${t.abbrev}</abbr> — ${t.term}`
                      : t.term
                    return `
                <div class="glossary-item" id="${t.id}">
                  <dt>${label}</dt>
                  <dd>${t.meaning}</dd>
                </div>`
                  },
                )
                .join('')}
            </dl>
          </section>`
      })
      .join('')
  }
  q?.addEventListener('input', render)
  render()
  if (location.hash) {
    document.querySelector(location.hash)?.scrollIntoView({ behavior: 'smooth' })
  }
}

main()
