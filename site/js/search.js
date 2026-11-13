import { withBase } from './base.js'
import { initTheme } from './theme.js'
import { resumeHref, resumeLabel, resetProgress } from './progress.js'

initTheme()

function score(hay, needle) {
  const h = hay.toLowerCase()
  const n = needle.toLowerCase()
  if (!n) return 0
  if (h.includes(n)) return n.length / Math.max(h.length, 1) + (h.startsWith(n) ? 0.5 : 0)
  return 0
}

async function main() {
  const [indexRes, catalogRes] = await Promise.all([
    fetch(withBase('data/search-index.json')),
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

  const out = document.getElementById('search-results')
  const input = document.getElementById('search-input')
  if (!indexRes.ok) {
    out.innerHTML = '<p class="empty-note">Search index missing. Run <code>npm run prepare-readings</code>.</p>'
    return
  }
  const index = await indexRes.json()

  const run = () => {
    const needle = (input.value || '').trim()
    if (needle.length < 2) {
      out.innerHTML = '<p class="muted">Type at least two characters.</p>'
      return
    }
    const hits = index.entries
      .map((e) => ({
        e,
        s: score(e.title, needle) * 3 + score(e.body, needle) + score(e.moduleTitle || '', needle),
      }))
      .filter((x) => x.s > 0)
      .sort((a, b) => b.s - a.s)
      .slice(0, 40)
    if (!hits.length) {
      out.innerHTML = '<p class="muted">No matches.</p>'
      return
    }
    out.innerHTML = hits
      .map(({ e }) => {
        const href =
          e.kind === 'glossary'
            ? withBase(`glossary.html#${e.id}`)
            : withBase(`module.html?id=${encodeURIComponent(e.moduleId)}${e.topicId ? `#topic-${e.topicId}` : ''}`)
        return `<a class="search-hit" href="${href}">
          <span class="phase-label">${e.kind}</span>
          <strong>${e.title}</strong>
          <span class="muted">${e.moduleTitle || ''}</span>
          <p>${e.snippet}</p>
        </a>`
      })
      .join('')
  }
  input?.addEventListener('input', run)
  const params = new URLSearchParams(location.search)
  if (params.get('q')) {
    input.value = params.get('q')
    run()
  }
}

main()
