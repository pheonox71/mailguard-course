# Capstone — small mail filter end-to-end

This module closes the course: ship a **coherent demo** of outbound message filtering (hold / allow / reject), prove it with tests, and self-grade against [`../../CAPSTONE-RUBRIC.md`](../../CAPSTONE-RUBRIC.md).

The student implements the filter and fills the worksheet.

Continue with the worksheet from the downloads on this page. The quiz is **required**.

---

## What “done” looks like

A stranger can:

1. Read your short demo notes  
2. Run documented commands  
3. See a sample message held, allowed, or rejected by rules you wrote  
4. See tests pass on your implementation  

You are **not** claiming a production mail gateway.

---

## Suggested shape (keep it small)

| Piece | Role |
|-------|------|
| Rule list | Ordered rules; first-match-wins (or document another order) |
| Actions | `hold`, `allow`, `reject` |
| Sample messages | 3–5 fixtures covering internal/external, risky recipients, subject keywords |
| Tests | Table-driven cases that fail on empty stubs |
| Operator path | Print held queue *or* a tiny approve/release function |

Reuse ideas from Challenge Gym hold rules, MailGuard API, and threat-model notes — do not paste vendor product claims.

---

## Evidence for the rubric

Map each Must row in `CAPSTONE-RUBRIC.md` to a file path or command in your worksheet. Stretch rows are optional ceiling; pick at least two if you want “portfolio-ready” as defined there.

---

## Quiz (required)

Download the quiz PDF from the course site, complete it, then check the separate answer key.
