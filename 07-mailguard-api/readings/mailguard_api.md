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
6. Persistence and pagination stay out of the kata on purpose — stretch labs add Postgres later. Production still needs **tenant-scoped authorization** (see deepen below), not only “is the caller logged in?”
7. Create HTTP clients, DB pools, and queue producers in a FastAPI **lifespan** (startup/shutdown), not as module-level globals that open sockets at import time.
8. Toward Module 09: prefer a **transactional outbox** (write hold + outbox row in one DB transaction; a publisher drains the outbox to the queue) over “HTTP commit then best-effort enqueue.”

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
3. Docker image (`Dockerfile`): multi-stage build. Default target copies `katas/` only — **`solutions/` never enter those layers** (a `COPY` + `rm` would still leave answer files in earlier layers recoverable by image history). Opt-in: `docker build --target with-solutions` copies `solutions/` and sets `MAILGUARD_USE_SOLUTIONS=1` only in that stage.
4. Course CI proves reference correctness by copying `solutions/` over `katas/` before pytest (same pattern as other modules) — after that copy, the default kata import is the reference code for that job.

```bash
# Student / default demo image (katas only; no solutions layers)
docker build -t mailguard-api:local .

# Demo before the kata is finished (with-solutions stage)
docker build --target with-solutions -t mailguard-api:local .
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
- **“Authn alone is enough.”** Broken object/function authorization (OWASP API1 / API5) and unconstrained resource use (API3) still leak cross-tenant holds — scope every hold id to the caller’s tenant.
- **“Open the DB/queue client at import.”** Module-level globals complicate tests and leak connections; use FastAPI lifespan.

## Tenant-scoped authZ (deepen)

**Why.** A valid JWT that can read *any* hold id is still a broken access control. [OWASP API Security Top 10](https://owasp.org/API-Security/) **API1** (Broken Object Level Authorization), **API3** (Broken Object Property Level Authorization / unconstrained resource consumption depending on edition wording), and **API5** (Broken Function Level Authorization) are the usual mail-gateway failures: tenant A releases tenant B’s hold, or a reviewer calls an admin-only reject.

**How.**

1. Authenticate the caller (OIDC from Module 03 / BFF from RFC 10017).
2. Bind every hold/rule row to a **tenant_id** (and often a role).
3. On every read/mutate path: `WHERE id = ? AND tenant_id = ?` (or equivalent) — never trust a client-supplied tenant alone.
4. Deny cross-tenant and cross-role with **403/404** (prefer 404 to avoid id oracle), not a silent empty success.

## Transactional outbox → Module 09

**Why.** `INSERT hold` then `sqs.send_message` can succeed in the DB and fail on the queue (or the process can crash between them). Workers then never see the work, or you retry and double-enqueue without an idempotency key.

**How.**

1. In one DB transaction: write the hold (or state change) **and** an **outbox** row (`payload`, `created_at`, `published_at=null`).
2. Commit.
3. A publisher (same process loop or sidecar) reads unpublished outbox rows and sends to ElasticMQ/SQS, then marks `published_at`.
4. Module 09 consumers stay **idempotent** on message/hold id (see `09` readings).

Sketch lives in [`../starter/app/queue_producer.py`](../starter/app/queue_producer.py) — treat enqueue as the *publisher* side of an outbox, not as “fire and forget inside the request with no durability.”

## FastAPI lifespan for clients

**Why.** Import-time `boto3.client(...)` / engine globals make pytest order-dependent and skip clean shutdown.

**How.** Use `@asynccontextmanager` lifespan on `FastAPI` to create store/queue/DB resources on startup and close them on shutdown (see [`../starter/app/main.py`](../starter/app/main.py)).

## Videos (verified)

1. **[FastAPI Tutorial for Beginners – Full Course](https://www.youtube.com/watch?v=VirndPTeRaw)** — Tech With Tim (2025)  
   Why it helps: routes, models, docs UI, and a runnable API shape that matches this module’s starter.


## Read these (verified)

1. [FastAPI — First steps](https://fastapi.tiangolo.com/tutorial/first-steps/) — routing and OpenAPI.
2. [FastAPI — Lifespan events](https://fastapi.tiangolo.com/advanced/events/) — startup/shutdown for clients (not module-level globals).
3. [Pydantic — Models](https://docs.pydantic.dev/latest/concepts/models/) — request/response shapes.
4. [pytest — Get Started](https://docs.pytest.org/en/stable/getting-started.html) — tests as contract.
5. [OWASP API Security Top 10](https://owasp.org/API-Security/) — tenant-scoped authZ (API1 / API3 / API5).
6. Challenge Gym [`hold_rules`](../../01-challenge-gym/readings/hold_rules.md) — same decision vocabulary.

## Keep in mind

Production APIs add **tenant-scoped** authn/z, persistence, pagination, audit logs, lifespan-managed clients, and an outbox toward Module 09. Your kata stays small on purpose — **why:** prove the decision engine before wiring infrastructure that hides policy bugs.

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment and tests.

## Phase 3 deepen

Add Postgres persistence in your lab environment, plus the `hold_state` and `rule_actions` katas for approve/release and auto-bcc/delete actions.
