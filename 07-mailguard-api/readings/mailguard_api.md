# Reading — MailGuard API

## Learning objectives

1. Sketch a small HTTP API that stores ordered hold/allow/reject rules.
2. Evaluate a message against those rules with **first-match-wins** semantics.
3. Cover happy path and edge cases with automated tests.

## Short intro

MailGuard’s product thread needs a **rules API**: operators create rules; the service decides whether an outbound message is allowed, held for review, or rejected. This module is a thin FastAPI-shaped service with an in-memory store and a pure evaluation function you can unit-test without standing up a database.

Keep the public vocabulary vendor-neutral: rules, holds, allow, reject — not a commercial product clone.

## Videos (verified)

1. **[FastAPI tutorial overview](https://www.youtube.com/watch?v=0QRcFgKecYg)** — freeCodeCamp  
   Why it helps: fast tour of routes, models, and docs UI.

## Read these (verified)

1. [FastAPI — First steps](https://fastapi.tiangolo.com/tutorial/first-steps/) — routing and OpenAPI.
2. [Pydantic — Models](https://docs.pydantic.dev/latest/concepts/models/) — request/response shapes.
3. [pytest — Get Started](https://docs.pytest.org/en/stable/getting-started.html) — tests as contract.
4. Challenge Gym [`hold_rules`](../../01-challenge-gym/readings/hold_rules.md) — same decision vocabulary.

## Keep in mind

Production APIs add authn/z, persistence, pagination, and audit logs. Your kata stays small on purpose.

## Next step

Continue with the worksheet from the downloads on this page. The quiz is required after you attempt the worksheet and tests.
