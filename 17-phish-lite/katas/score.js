/** Ethical phishing-training metrics (no credential capture). */

export function scoreAnswers(answers, key) {
  throw new Error('implement scoreAnswers')
}

export function reportVsClickRatio(reported, clicked) {
  throw new Error('implement reportVsClickRatio')
}

export function reportRate(uniqueReporters, delivered) {
  throw new Error('implement reportRate')
}

export function clickRate(uniqueClickers, delivered) {
  throw new Error('implement clickRate')
}

export function timeToReportSeconds(sentAt, reportedAt) {
  throw new Error('implement timeToReportSeconds')
}

export function ethicalSimOk({ consent, capturesCredentials }) {
  throw new Error('implement ethicalSimOk')
}
