import test from 'node:test'
import assert from 'node:assert/strict'
import { scoreAnswers, reportRate, timeToReportSeconds, ethicalSimOk } from '../katas/score.js'

test('score', () => {
  const r = scoreAnswers(['a', 'b'], ['a', 'c'])
  assert.equal(r.correct, 1)
  assert.equal(r.total, 2)
})

test('reportRate', () => {
  assert.equal(reportRate(3, 1), 0.75)
  assert.equal(reportRate(0, 0), 0)
})

test('timeToReport', () => {
  assert.equal(timeToReportSeconds(100, 160), 60)
})

test('ethical', () => {
  assert.equal(ethicalSimOk({ consent: true, capturesCredentials: false }), true)
  assert.equal(ethicalSimOk({ consent: true, capturesCredentials: true }), false)
})
