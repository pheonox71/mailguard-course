import test from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { formatHoldRow, validateRuleForm } from '../katas/rule_form.ts'

/** Simulate Vue/DOM text binding: textContent preserves bytes; innerHTML escapes tags. */
function renderSubjectAsText(subject: string): { text: string; childElementCount: number; innerHTML: string } {
  const innerHTML = subject
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
  return { text: subject, childElementCount: 0, innerHTML }
}

test('rejects empty name and decision', () => {
  const res = validateRuleForm({ name: ' ', decision: '' })
  assert.equal(res.ok, false)
  assert.ok(res.errors.length > 0)
})

test('accepts domain rule', () => {
  const res = validateRuleForm({
    name: 'ext',
    decision: 'hold',
    recipientDomain: 'partner.example',
  })
  assert.equal(res.ok, true)
})

test('requires at least one predicate', () => {
  const res = validateRuleForm({ name: 'noop', decision: 'reject' })
  assert.equal(res.ok, false)
})

test('formatHoldRow is plain text', () => {
  assert.equal(formatHoldRow('<b>hi</b>', 'a@b.example'), 'a@b.example — <b>hi</b>')
})

test('malicious subject stays text under textContent binding (XSS render)', () => {
  // Mirrors App.vue {{ row.subject }} — text nodes, not innerHTML / v-html.
  const subject = '<img src=x onerror="alert(1)">'
  const label = formatHoldRow(subject, 'attacker@evil.example')
  assert.equal(label, `attacker@evil.example — ${subject}`)

  const rendered = renderSubjectAsText(subject)
  assert.equal(rendered.childElementCount, 0, 'text binding must not create HTML elements')
  assert.equal(rendered.text, subject)
  assert.match(rendered.innerHTML, /&lt;img/)
  assert.doesNotMatch(rendered.innerHTML, /<img\b/i)
})

test('App.vue uses text binding for subjects and ships XSS fixture', () => {
  const here = dirname(fileURLToPath(import.meta.url))
  const vue = readFileSync(join(here, '../starter/src/App.vue'), 'utf8')
  assert.match(vue, /\{\{\s*row\.subject\s*\}\}/)
  assert.doesNotMatch(vue, /v-html\s*=/)
  assert.match(vue, /onerror/)
  assert.match(vue, /role="dialog"/)
  assert.match(vue, /aria-modal="true"/)
})
