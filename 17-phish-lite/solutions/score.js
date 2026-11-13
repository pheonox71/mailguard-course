export function scoreAnswers(answers, key) {
  let n = 0
  for (let i = 0; i < key.length; i++) if (answers[i] === key[i]) n++
  return n
}

export function reportRate(reported, clicked) {
  const total = reported + clicked
  if (total === 0) return 0
  return reported / total
}
