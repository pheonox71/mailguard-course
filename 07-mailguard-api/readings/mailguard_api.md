# Reading — MailGuard API

## Learning objectives

1. Sketch a small HTTP API that stores ordered hold/allow/reject rules.
2. Evaluate a message against those rules with **first-match-wins** semantics.
3. Cover happy path and edge cases with automated tests.

**Why this matters.** Without a rules API, operators cannot encode “hold external domains” or “reject secret substrings” as durable policy — every decision becomes a one-off script. First-match-wins without tests drifts into silent allow; an in-memory-only store vanishes on restart and cannot support multi-instance or audit. History of mail gateways is full of policy engines that grew from ad-hoc filters; a thin, tested evaluate function is the trade-off that keeps the kata honest before Postgres and authn.

**How it works.**

1. Operators **create** ordered rules (predicates + decision: `hold` / `allow` / `reject`).
2. On evaluate, the service walks the list **top-down**.
3. Stop at the **first** match; return that decision (or a documented default if none match).
4. Keep evaluation as a **pure function** separate from FastAPI handlers so pytest covers edge cases without HTTP.
5. Pydantic models shape requests; OpenAPI documents the surface ([FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/)).
6. Persistence, authn/z, and pagination stay out of the kata on purpose — stretch labs add Postgres later.

```
Client → POST /rules  → store (ordered list)
Client → POST /evaluate(message) → walk rules → first match → decision
```

### Worked example

Rules and one evaluate call (conceptual JSON):

```json
[
  {"id": "r1", "match": {"recipient_domain": "external.example"}, "action": "hold"},
  {"id": "r2", "match": {"body_contains": "SECRET"}, "action": "reject"},
  {"id": "r3", "match": {}, "action": "allow"}
]
```

```http
POST /evaluate
{"to": "user@external.example", "subject": "Q3", "body": "hi"}

→ 200 {"decision": "hold", "matched_rule": "r1"}
```

If `r1` were listed *after* a blanket allow, the same message would silently allow — **order is policy**.

**On the job.** Email DLP and identity-adjacent gateways expose the same pattern: policy CRUD + evaluate on the message path. Interviewers care that you can explain first-match vs scoring, why pure evaluation is testable, and what an in-memory store cannot prove in production — vendor-neutral skills for any cloud mail or SaaS security API.

## Short intro

MailGuard’s product thread needs a **rules API**: operators create rules; the service decides whether an outbound message is allowed, held for review, or rejected. This module is a thin FastAPI-shaped service with an in-memory store and a pure evaluation function you can unit-test without standing up a database.

Keep the public vocabulary vendor-neutral: rules, holds, allow, reject — not a commercial product clone.

### Common misconceptions / what goes wrong

- **“Last-match or score-sum is the same as first-match.”** Different semantics produce different outcomes for the same rule list; document and test the one you chose.
- **“Evaluation inside the route handler is fine.”** Mixing HTTP and policy makes edge-case tests slow and fragile; pure `evaluate(rules, message)` is the contract.
- **“In-memory means production-ready.”** Restarts wipe rules; two API instances disagree. Production needs authn/z, persistence, pagination, and audit logs — the kata stays small **why:** prove the decision engine before infrastructure hides policy bugs.
- **“No match → hold for safety.”** Maybe — but only if documented. Silent defaults are how missends (or false blocks) ship.

## Videos (verified)

1. **[FastAPI tutorial overview](https://www.youtube.com/watch?v=0QRcFgKecYg)** — freeCodeCamp  
   Why it helps: fast tour of routes, models, and docs UI.

## Read these (verified)

1. [FastAPI — First steps](https://fastapi.tiangolo.com/tutorial/first-steps/) — routing and OpenAPI.
2. [Pydantic — Models](https://docs.pydantic.dev/latest/concepts/models/) — request/response shapes.
3. [pytest — Get Started](https://docs.pytest.org/en/stable/getting-started.html) — tests as contract.
4. Challenge Gym [`hold_rules`](../../01-challenge-gym/readings/hold_rules.md) — same decision vocabulary.

## Keep in mind

Production APIs add authn/z, persistence, pagination, and audit logs. Your kata stays small on purpose — **why:** prove the decision engine before wiring infrastructure that hides policy bugs.

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment and tests.

## Phase 3 deepen

Add Postgres persistence in your lab environment, plus the `hold_state` and `rule_actions` katas for approve/release and auto-bcc/delete actions.
