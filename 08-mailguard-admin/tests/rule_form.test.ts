import test from 'node:test'
import assert from 'node:assert/strict'
import { formatHoldRow, validateRuleForm } from '../katas/rule_form.ts'

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
