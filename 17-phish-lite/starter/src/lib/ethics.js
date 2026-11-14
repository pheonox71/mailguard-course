/**
 * Ethics gate for phishing-training simulations.
 * Why: a form that can capture secrets is out of scope for this course.
 */
export function ethicalSimOk({ consent, capturesCredentials }) {
  return Boolean(consent) && capturesCredentials === false;
}

/** reportVsClickRatio(reported, clicked) = reported / (reported + clicked) */
export function reportVsClickRatio(reported, clicked) {
  const total = reported + clicked;
  if (total <= 0) return 0;
  return reported / total;
}

/** reportRate(uniqueReporters, delivered) = uniqueReporters / delivered */
export function reportRate(uniqueReporters, delivered) {
  if (delivered <= 0) return 0;
  return uniqueReporters / delivered;
}

/** clickRate(uniqueClickers, delivered) = uniqueClickers / delivered */
export function clickRate(uniqueClickers, delivered) {
  if (delivered <= 0) return 0;
  return uniqueClickers / delivered;
}
