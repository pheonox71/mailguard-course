# 19 — Capstone: Mail filter end-to-end

Bring the MailGuard thread together: a small outbound **mail filter** the student can demo end-to-end, plus a downloadable self-grading worksheet against the course rubric.

**Language / tooling:** Python 3 + pytest for the filter core; optional curl/httpie for the demo path. Est. 8-10h.

## Learning objectives

- Assemble hold / allow / reject into one runnable demo path
- Show tests that fail on stubs and pass on the student’s implementation
- Self-grade against Must / Stretch rubric rows with honest evidence links
- Package a stranger-friendly README for the capstone demo

## Deliverables

1. Runnable filter (CLI or tiny API) that classifies sample outbound messages
2. Automated tests for the rule engine
3. Completed [`worksheets/capstone_self_grade.md`](./worksheets/capstone_self_grade.md) saved under `my-work/worksheets/`
4. Short demo notes (commands + expected output)

## Workflow

1. Read [`readings/capstone_mail_filter.md`](./readings/capstone_mail_filter.md) on the site
2. Worksheet — self-grade + demo checklist
3. Implement stubs under `katas/` until tests pass (when present)
4. Required quiz PDF, then separate answer key

## Done when

- Demo path documented and runnable from a clean checkout of *your* work
- Worksheet self-grade shows all Must rows honest **yes** (or explicitly deferred with reasons)
- Required quiz completed under `my-work/quizzes/`
