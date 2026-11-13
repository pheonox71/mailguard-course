/**
 * Accessible glossary popovers for first-occurrence .glossary-ref links.
 * Hover / keyboard focus / first tap opens; Escape, blur, and outside tap dismiss.
 * Click still navigates to the glossary entry (second tap on touch after open).
 */

const TOOLTIP_ID = 'glossary-tooltip'
const OPEN_ATTR = 'data-glossary-open'
const TOUCH_ARMED = 'data-glossary-touch-armed'

let activeAnchor = null
let tooltipEl = null

function ensureTooltip() {
  if (tooltipEl && document.body.contains(tooltipEl)) return tooltipEl
  tooltipEl = document.getElementById(TOOLTIP_ID)
  if (!tooltipEl) {
    tooltipEl = document.createElement('div')
    tooltipEl.id = TOOLTIP_ID
    tooltipEl.className = 'glossary-tooltip'
    tooltipEl.setAttribute('role', 'tooltip')
    tooltipEl.hidden = true
    document.body.appendChild(tooltipEl)
  }
  return tooltipEl
}

function termPayload(anchor) {
  const term = anchor.getAttribute('data-glossary-term') || ''
  const meaning = anchor.getAttribute('data-glossary-meaning') || ''
  const abbrev = anchor.getAttribute('data-glossary-abbrev') || anchor.textContent.trim()
  return { term, meaning, abbrev }
}

function positionTooltip(anchor, tip) {
  tip.hidden = false
  tip.style.left = '0px'
  tip.style.top = '0px'
  const rect = anchor.getBoundingClientRect()
  const tipRect = tip.getBoundingClientRect()
  const margin = 8
  let left = rect.left + rect.width / 2 - tipRect.width / 2
  let top = rect.bottom + margin
  const maxLeft = window.innerWidth - tipRect.width - margin
  left = Math.max(margin, Math.min(left, maxLeft))
  if (top + tipRect.height > window.innerHeight - margin) {
    top = rect.top - tipRect.height - margin
  }
  if (top < margin) top = margin
  tip.style.left = `${Math.round(left + window.scrollX)}px`
  tip.style.top = `${Math.round(top + window.scrollY)}px`
}

function showTooltip(anchor) {
  const tip = ensureTooltip()
  const { term, meaning, abbrev } = termPayload(anchor)
  if (!term && !meaning) return
  const title = term || abbrev
  tip.innerHTML = `<p class="glossary-tooltip-term">${escapeHtml(title)}${
    abbrev && term && abbrev !== term
      ? ` <span class="glossary-tooltip-abbrev">(${escapeHtml(abbrev)})</span>`
      : ''
  }</p><p class="glossary-tooltip-def">${escapeHtml(meaning)}</p>`
  tip.hidden = false
  tip.setAttribute('aria-hidden', 'false')
  positionTooltip(anchor, tip)
  if (activeAnchor && activeAnchor !== anchor) {
    activeAnchor.removeAttribute(OPEN_ATTR)
    activeAnchor.removeAttribute('aria-describedby')
    activeAnchor.removeAttribute(TOUCH_ARMED)
  }
  activeAnchor = anchor
  anchor.setAttribute(OPEN_ATTR, 'true')
  anchor.setAttribute('aria-describedby', TOOLTIP_ID)
}

function hideTooltip() {
  const tip = ensureTooltip()
  tip.hidden = true
  tip.setAttribute('aria-hidden', 'true')
  tip.innerHTML = ''
  if (activeAnchor) {
    activeAnchor.removeAttribute(OPEN_ATTR)
    activeAnchor.removeAttribute('aria-describedby')
    activeAnchor.removeAttribute(TOUCH_ARMED)
    activeAnchor = null
  }
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
}

function isTouchLike(event) {
  return event.pointerType === 'touch' || event.pointerType === 'pen'
}

export function initGlossaryTooltips(root = document) {
  ensureTooltip()
  const anchors = root.querySelectorAll('a.glossary-ref')
  anchors.forEach((a) => {
    if (a.dataset.glossaryBound === '1') return
    a.dataset.glossaryBound = '1'
    a.removeAttribute('title')

    a.addEventListener('pointerenter', (e) => {
      if (isTouchLike(e)) return
      showTooltip(a)
    })
    a.addEventListener('pointerleave', (e) => {
      if (isTouchLike(e)) return
      if (activeAnchor === a) hideTooltip()
    })
    a.addEventListener('focus', () => showTooltip(a))
    a.addEventListener('blur', () => {
      // Defer so focus moving into tooltip/other UI can cancel if needed.
      requestAnimationFrame(() => {
        if (document.activeElement !== a && activeAnchor === a) hideTooltip()
      })
    })
    a.addEventListener('click', (e) => {
      // Touch / coarse pointers: first tap opens tooltip; second tap navigates.
      if (!window.matchMedia('(hover: none)').matches) return
      if (!a.hasAttribute(OPEN_ATTR)) {
        e.preventDefault()
        showTooltip(a)
        a.setAttribute(TOUCH_ARMED, '1')
        return
      }
      hideTooltip()
    })
  })

  if (!document.body.dataset.glossaryTooltipGlobal) {
    document.body.dataset.glossaryTooltipGlobal = '1'
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') hideTooltip()
    })
    document.addEventListener(
      'pointerdown',
      (e) => {
        if (!activeAnchor) return
        const tip = ensureTooltip()
        if (activeAnchor.contains(e.target) || tip.contains(e.target)) return
        hideTooltip()
      },
      true,
    )
    window.addEventListener(
      'scroll',
      () => {
        if (activeAnchor) positionTooltip(activeAnchor, ensureTooltip())
      },
      { passive: true },
    )
    window.addEventListener('resize', () => {
      if (activeAnchor) positionTooltip(activeAnchor, ensureTooltip())
    })
  }
}
