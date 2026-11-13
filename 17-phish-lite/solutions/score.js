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

export function reportRate(reported, clicked) {
  const denom = reported + clicked
  if (denom <= 0) return 0
  return reported / denom
}

export function timeToReportSeconds(sentAt, reportedAt) {
  const dt = reportedAt - sentAt
  if (dt < 0) throw new Error('negative')
  return dt
}

export function ethicalSimOk({ consent, capturesCredentials }) {
  return Boolean(consent) && capturesCredentials === false
}
