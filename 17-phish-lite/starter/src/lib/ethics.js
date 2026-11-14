/**
 * Ethics gate for phishing-training simulations.
 * Why: a form that can capture secrets is out of scope for this course.
 */
export function ethicalSimOk({ consent, capturesCredentials }) {
  return Boolean(consent) && capturesCredentials === false;
}

/** reportRate(reported, clicked) = reported / (reported + clicked) */
export function reportRate(reported, clicked) {
  const total = reported + clicked;
  if (total <= 0) return 0;
  return reported / total;
}
