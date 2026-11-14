export function scoreAnswers(answers, key) {
  if (!Array.isArray(answers) || !Array.isArray(key) || answers.length !== key.length) {
    throw new Error('length mismatch')
  }
  let correct = 0
  for (let i = 0; i < key.length; i++) {
    if (answers[i] === key[i]) correct++
  }
  return { correct, total: key.length, pct: correct / key.length }
}

export function reportVsClickRatio(reported, clicked) {
  const denom = reported + clicked
  if (denom <= 0) return 0
  return reported / denom
}

export function reportRate(uniqueReporters, delivered) {
  if (delivered <= 0) return 0
  return uniqueReporters / delivered
}

export function clickRate(uniqueClickers, delivered) {
  if (delivered <= 0) return 0
  return uniqueClickers / delivered
}

export function timeToReportSeconds(sentAt, reportedAt) {
  const dt = reportedAt - sentAt
  if (dt < 0) throw new Error('negative')
  return dt
}

export function ethicalSimOk({ consent, capturesCredentials }) {
  return Boolean(consent) && capturesCredentials === false
}
