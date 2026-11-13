/**
 * Project Pages live under /mailguard-course/; local preview uses /.
 */
export function siteBase() {
  const parts = location.pathname.split('/').filter(Boolean)
  if (parts[0] === 'mailguard-course') return '/mailguard-course/'
  return '/'
}

export function withBase(path) {
  if (!path) return path
  if (/^(https?:|data:|mailto:|#)/i.test(path)) return path
  const base = siteBase()
  const cleaned = String(path).replace(/^\.\//, '').replace(/^\//, '')
  return `${base}${cleaned}`
}

export function injectBaseTag() {
  if (document.querySelector('base')) return
  const el = document.createElement('base')
  el.href = siteBase()
  document.head.prepend(el)
}

injectBaseTag()
