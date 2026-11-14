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
  {"id": "r1", "recipient_domain": "external.example", "decision": "hold"},
  {"id": "r2", "contains": "SECRET", "decision": "reject"}
]
```

A rule with **no predicates** (neither `recipient_domain` nor `contains`) **never matches**. Use the evaluate call’s documented **default** (usually `allow`) when nothing matches — do not invent a catch-all empty `match: {}` rule.

```http
POST /evaluate
{"to": "user@external.example", "subject": "Q3", "body": "hi"}

→ 200 {"decision": "hold", "matched_rule": "r1"}
```

If a broad allow rule were listed *before* the domain hold, the same message would silently allow — **order is policy**.

**On the job.** Email DLP and identity-adjacent gateways expose the same pattern: policy CRUD + evaluate on the message path. Interviewers care that you can explain first-match vs scoring, why pure evaluation is testable, and what an in-memory store cannot prove in production — vendor-neutral skills for any cloud mail or SaaS security API.

### Rules engine import: katas vs solutions

**Why.** The FastAPI starter (`starter/app/store.py`) must call the same `matches` / `evaluate` contract the tests cover. Importing `solutions/` by default would ship answer code into every local run and every Module 13/14 demo image — students would never exercise their own stubs, and the container would leak reference implementations. Keeping the default on `katas/` makes the API fail closed on unfinished work (`NotImplementedError`) until the student implements the engine.

**How.**

1. Default: `store.py` imports from `katas.rules_engine` (your stubs).
2. Opt-in reference path: set environment variable `MAILGUARD_USE_SOLUTIONS=1`. Then the starter loads `solutions/` and, if a kata function still raises `NotImplementedError`, falls back to the reference implementation and logs a clear warning that fallback happened.
3. Docker image (`Dockerfile`): copies `katas/` always; copies then **removes** `solutions/` unless you build with `--build-arg INCLUDE_SOLUTIONS=1` (which also sets `MAILGUARD_USE_SOLUTIONS` in the image). Default `mailguard-api:local` therefore does not ship answers.
4. Course CI proves reference correctness by copying `solutions/` over `katas/` before pytest (same pattern as other modules) — after that copy, the default kata import is the reference code for that job.

```bash
# Student / default demo image (katas only)
docker build -t mailguard-api:local .

# Demo before the kata is finished (includes solutions + enables fallback)
docker build --build-arg INCLUDE_SOLUTIONS=1 -t mailguard-api:local .
# or locally without Docker:
MAILGUARD_USE_SOLUTIONS=1 uvicorn starter.app.main:app --port 8000
```

## Short intro

MailGuard’s product thread needs a **rules API**: operators create rules; the service decides whether an outbound message is allowed, held for review, or rejected. This module is a thin FastAPI-shaped service with an in-memory store and a pure evaluation function you can unit-test without standing up a database.

Keep the public vocabulary vendor-neutral: rules, holds, allow, reject — not a commercial product clone.

### Common misconceptions / what goes wrong

- **“Last-match or score-sum is the same as first-match.”** Different semantics produce different outcomes for the same rule list; document and test the one you chose.
- **“Evaluation inside the route handler is fine.”** Mixing HTTP and policy makes edge-case tests slow and fragile; pure `evaluate(rules, message)` is the contract.
- **“In-memory means production-ready.”** Restarts wipe rules; two API instances disagree. Production needs authn/z, persistence, pagination, and audit logs — the kata stays small **why:** prove the decision engine before infrastructure hides policy bugs.
- **“No match → hold for safety.”** Maybe — but only if documented. Silent defaults are how missends (or false blocks) ship.

## Videos (verified)

1. **[FastAPI Tutorial for Beginners – Full Course](https://www.youtube.com/watch?v=VirndPTeRaw)** — Tech With Tim (2025)  
   Why it helps: routes, models, docs UI, and a runnable API shape that matches this module’s starter.


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
