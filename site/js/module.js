const params = new URLSearchParams(location.search)
const id = params.get('id') || '01-challenge-gym'
const root = document.getElementById('module-root')
const crumb = document.getElementById('crumb-current')
const adjacent = document.getElementById('module-adjacent')

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

async function main() {
  const res = await fetch('data/catalog.json')
  if (!res.ok) {
    root.innerHTML =
      '<p class="empty-note">Catalog missing. Run <code>npm run prepare-downloads</code> from <code>site/</code>.</p>'
    return
  }

  const catalog = await res.json()
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

  document.title = `${mod.number} — ${mod.title} · MailGuard Course`
  crumb.textContent = `${mod.number} ${mod.title}`

  const worksheetButtons = []
  if (mod.worksheetsZip) {
    worksheetButtons.push(
      `<a class="btn btn-download" download href="${mod.worksheetsZip}">Download worksheets (zip)</a>`,
    )
  } else if (mod.worksheetSingle) {
    worksheetButtons.push(
      `<a class="btn btn-download" download href="${mod.worksheetSingle.href}">Download worksheet</a>`,
    )
  }

  if (mod.testsZip) {
    worksheetButtons.push(
      `<a class="btn btn-download" download href="${mod.testsZip}">Download tests (zip)</a>`,
    )
  }

  const quizButtons = []
  if (mod.quizzesZip) {
    quizButtons.push(
      `<a class="btn btn-ghost" download href="${mod.quizzesZip}">Download quizzes (questions only)</a>`,
    )
  } else if (mod.quizSingle) {
    quizButtons.push(
      `<a class="btn btn-ghost" download href="${mod.quizSingle.href}">Download quiz (questions only)</a>`,
    )
  }

  const topicRows =
    mod.worksheets.length > 1
      ? `
    <div class="topic-grid" aria-label="Per-topic downloads">
      ${mod.worksheets
        .map((w) => {
          const test = mod.tests.find((t) => t.id === w.id)
          return `
          <div class="topic-item">
            <div>
              <h3>${escapeHtml(titleCase(w.label))}</h3>
              <p>Worksheet${test ? ' and matching tests' : ''}</p>
            </div>
            <div class="download-actions">
              <a class="btn btn-download" download href="${w.href}">Worksheet</a>
              ${
                test
                  ? `<a class="btn btn-download" download href="${test.href}">Test</a>`
                  : ''
              }
            </div>
          </div>`
        })
        .join('')}
    </div>`
      : ''

  const readings =
    mod.readings.length > 0
      ? `
    <div style="margin-top:2rem">
      <h2 style="font-family:var(--font-display);font-size:1.25rem;margin:0">Readings in this module</h2>
      <p class="muted" style="margin:.45rem 0 0">Work through the reading, then use the worksheet as your next step.</p>
      <ul class="reading-list">
        ${mod.readings
          .map(
            (r) =>
              `<li>${escapeHtml(titleCase(r.label))} <span class="muted">(${escapeHtml(r.path)})</span></li>`,
          )
          .join('')}
      </ul>
    </div>`
      : ''

  const empty =
    !mod.worksheets.length && !mod.tests.length
      ? `<p class="empty-note">This module is a build / stretch step. Worksheet and test downloads appear here when those assets exist for the topic.</p>`
      : ''

  root.innerHTML = `
    <p class="module-kicker">${escapeHtml(mod.phase)} · ${escapeHtml(mod.hours)}</p>
    <h1>${escapeHtml(mod.number)} — ${escapeHtml(mod.title)}</h1>
    <p class="module-blurb">${escapeHtml(mod.blurb)}</p>

    <section class="download-panel" aria-label="Downloads">
      <h2>Downloads for students</h2>
      <p>Files come from the course tree. Answer keys are not included in quiz downloads.</p>
      <div class="download-actions">
        ${worksheetButtons.join('') || '<span class="muted">No worksheet pack for this module yet.</span>'}
        ${quizButtons.join('')}
      </div>
      ${topicRows}
      ${empty}
    </section>
    ${readings}
  `

  const prev = catalog.modules[index - 1]
  const next = catalog.modules[index + 1]
  adjacent.innerHTML = `
    ${
      prev
        ? `<a href="module.html?id=${encodeURIComponent(prev.id)}">← ${prev.number} ${escapeHtml(prev.title)}</a>`
        : '<span></span>'
    }
    ${
      next
        ? `<a href="module.html?id=${encodeURIComponent(next.id)}">${next.number} ${escapeHtml(next.title)} →</a>`
        : '<span></span>'
    }
  `
}

main()
