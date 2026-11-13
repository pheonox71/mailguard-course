# Capstone — small mail filter end-to-end

This module closes the course: ship a **coherent demo** of outbound message filtering (hold / allow / reject), prove it with tests, and self-grade against [`../../CAPSTONE-RUBRIC.md`](../../CAPSTONE-RUBRIC.md).

**Why this matters.** Separate labs (rules, API, worker, CI, IAM) do not prove you can tell one story. Hiring managers and portfolio reviewers look for a runnable thread: sample messages in → policy actions out → tests green → honest gaps. Without that integration, skills look like disconnected checklists. On the job, outbound missend prevention is exactly this shape — ordered rules, operator release path, and evidence you did not hard-code secrets.

**How it works.**

1. Define an ordered **rule list** (first-match-wins unless you document another order).
2. Actions: `hold`, `allow`, `reject` on sample fixtures (internal/external, risky recipients, keywords).
3. Prove behavior with **table-driven tests** that fail on empty stubs — why: green stubs would not prove your code.
4. Show an **operator path** (print held queue or approve/release helper).
5. Map each Must rubric row to a file/command; keep Stretch optional and honest.

```text
fixtures → rule engine → hold | allow | reject
                ↓
         pytest contract + short demo notes
```

The student implements the filter and fills the assignment.

Continue with the assignment from the downloads on this page. The quiz is **required**.

---

## What “done” looks like

A stranger can:

1. Read your short demo notes  
2. Run documented commands (annotate **why** each step exists)  
3. See a sample message held, allowed, or rejected by rules you wrote  
4. See tests pass on your implementation  

You are **not** claiming a production mail gateway.

---

## Suggested shape (keep it small)

| Piece | Role | Why that way |
|-------|------|--------------|
| Rule list | Ordered rules; first-match-wins (or document another order) | Predictable, reviewable policy |
| Actions | `hold`, `allow`, `reject` | Matches earlier MailGuard vocabulary |
| Sample messages | 3–5 fixtures covering internal/external, risky recipients, subject keywords | Proves edge cases, not one happy path |
| Tests | Table-driven cases that fail on empty stubs | Contract before implementation theater |
| Operator path | Print held queue *or* a tiny approve/release function | Shows human-in-the-loop, not fire-and-forget |

Reuse ideas from Challenge Gym hold rules, MailGuard API, and threat-model notes — do not paste vendor product claims.

---

## Evidence for the rubric

Map each Must row in `CAPSTONE-RUBRIC.md` to a file path or command in your assignment. Stretch rows are optional ceiling; pick at least two if you want “portfolio-ready” as defined there. **Why map explicitly:** self-grade stops optimistic checkboxes without proof.

---

## Quiz (required)

Download the quiz PDF from the course site, complete it, then check the separate answer key.
