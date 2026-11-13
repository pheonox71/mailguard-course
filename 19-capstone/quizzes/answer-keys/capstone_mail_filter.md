# Quiz answer key — capstone mail filter

Use only after attempting the quiz questions.

1. **hold**, **allow**, **reject** (or equivalent wording used in the thread). Hold enables human review for ambiguous/risky sends instead of silent loss or silent delivery.
2. Evaluate rules in order; stop at the first match and apply that action. Putting a broad `allow` above a specific `hold` can bypass safety checks — order is policy.
3. So the suite is a real contract — green on empty stubs would not prove the student’s code.
4. Under **`my-work/`** (`assignments/` and `quizzes/`) — not on the website — so personal completed work stays private while the course materials stay generic.
5. Examples: clear thread/story, runnable demo, real tests, secrets hygiene, trade-offs, rule engine, identity touch, operator surface, CI signal (any two Must themes). Reviewers need evidence, not slogans.
6. **Secrets hygiene (M5)** — move secrets to env / `.env.example` docs; never commit live credentials. Mail/identity demos that leak keys become incidents.
