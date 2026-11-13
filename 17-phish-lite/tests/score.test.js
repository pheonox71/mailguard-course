import test from 'node:test'
import assert from 'node:assert/strict'
import { reportRate, scoreAnswers } from '../katas/score.js'

test('scores answers', () => {
  assert.equal(scoreAnswers(['a', 'b'], ['a', 'c']), 1)
})

test('report rate', () => {
  assert.equal(reportRate(3, 1), 0.75)
  assert.equal(reportRate(0, 0), 0)
})
