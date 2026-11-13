const KEY = 'mailguard-course-theme'

export function getTheme() {
  const stored = localStorage.getItem(KEY)
  if (stored === 'light' || stored === 'dark') return stored
  return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'
}

export function applyTheme(theme) {
  document.documentElement.dataset.theme = theme
  localStorage.setItem(KEY, theme)
  const btn = document.getElementById('theme-toggle')
  if (btn) {
    btn.textContent = theme === 'light' ? 'Dark mode' : 'Light mode'
    btn.setAttribute('aria-pressed', theme === 'light' ? 'false' : 'true')
  }
}

export function initTheme() {
  applyTheme(getTheme())
  const btn = document.getElementById('theme-toggle')
  if (btn && !btn.dataset.bound) {
    btn.dataset.bound = '1'
    btn.addEventListener('click', () => {
      applyTheme(getTheme() === 'light' ? 'dark' : 'light')
    })
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initTheme)
} else {
  initTheme()
}
