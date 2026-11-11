const list = document.getElementById('module-list')

function assetsHint(mod) {
  const bits = []
  if (mod.worksheets.length) {
    bits.push(`${mod.worksheets.length} worksheet${mod.worksheets.length > 1 ? 's' : ''}`)
  }
  if (mod.tests.length) {
    bits.push(`${mod.tests.length} test file${mod.tests.length > 1 ? 's' : ''}`)
  }
  return bits.length ? bits.join(' · ') : 'Readings / build module'
}

async function main() {
  const res = await fetch('data/catalog.json')
  if (!res.ok) {
    list.innerHTML =
      '<p class="empty-note">Catalog missing. Run <code>npm run prepare-downloads</code> from <code>site/</code>.</p>'
    return
  }
  const catalog = await res.json()
  list.innerHTML = catalog.modules
    .map(
      (mod) => `
    <a class="module-row" href="module.html?id=${encodeURIComponent(mod.id)}">
      <div class="module-num">${mod.number}</div>
      <div>
        <span class="phase-label">${mod.phase}</span>
        <h3>${mod.title}</h3>
        <p>${mod.blurb}</p>
      </div>
      <div class="module-meta">
        <div>${mod.hours}</div>
        <div>${assetsHint(mod)}</div>
      </div>
    </a>
  `,
    )
    .join('')
}

main()
