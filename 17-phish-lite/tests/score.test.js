import test from 'node:test'
import assert from 'node:assert/strict'
import {
  scoreAnswers,
  reportVsClickRatio,
  reportRate,
  clickRate,
  timeToReportSeconds,
  ethicalSimOk,
} from '../katas/score.js'

test('score', () => {
  const r = scoreAnswers(['a', 'b'], ['a', 'c'])
  assert.equal(r.correct, 1)
  assert.equal(r.total, 2)
})

test('reportVsClickRatio', () => {
  assert.equal(reportVsClickRatio(3, 1), 0.75)
  assert.equal(reportVsClickRatio(0, 0), 0)
})

test('reportRate and clickRate vs delivered', () => {
  assert.equal(reportRate(30, 100), 0.3)
  assert.equal(clickRate(10, 100), 0.1)
  assert.equal(reportRate(0, 0), 0)
  assert.equal(clickRate(5, 0), 0)
})

test('timeToReport', () => {
  assert.equal(timeToReportSeconds(100, 160), 60)
})

test('ethical', () => {
  assert.equal(ethicalSimOk({ consent: true, capturesCredentials: false }), true)
  assert.equal(ethicalSimOk({ consent: true, capturesCredentials: true }), false)
})
