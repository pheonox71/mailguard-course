# 07 — MailGuard API

**Language:** Python 3 + FastAPI + pytest. Est. 8-10h.

Build a small rules API for outbound message decisions: create/list rules, evaluate a message, and hold / allow / reject with tests.

## What this teaches

- FastAPI routes, request/response models, and OpenAPI
- Hold/allow/reject evaluation with first-match-wins order
- pytest + httpx against the API (or pure unit tests on the rule engine)

## Workflow

1. [`readings/mailguard_api.md`](./readings/mailguard_api.md)
2. Assignment → implement `katas/` until tests pass
3. Required quiz PDF, then separate answer key

## Layout

| Path | Role |
|------|------|
| `readings/` | API design intro + verified links |
| `assignments/` | Guided questions before coding |
| `katas/` | Stubs you implement |
| `tests/` | pytest contract |
| `solutions/` | Reference — peek only if stuck |
| `quizzes/` | Required quiz + answer key |

## How to run

```bash
cd 07-mailguard-api
python3 -m venv .venv && source .venv/bin/activate
# Windows: py -3 -m venv .venv ; .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

**Done when:** CRUD + hold/release paths work; rules unit-tested; short architecture notes in this README’s trade-offs section.

## Trade-offs / harden next

- In-memory store only — swap for Postgres + migrations in a later hardening pass.
- No auth on the API yet — wire MFA/OIDC from modules 02–03 before any public deploy.
- First-match-wins is interview-clear; production DLP often needs priority weights and audit diffs.

**Production gap:** real email gateways need durable queues, idempotent writes, and least-privilege deploy identities (modules 09 / 12).
