# Reading — Hold / approve / release

## Learning objectives

1. Model a first-class hold queue with explicit state transitions.
2. Separate **approve** (human decision) from **release** (send onward).
3. Reject illegal transitions instead of silently no-oping.

## Short intro

An email-security gateway often **holds** outbound mail for review. Operators approve or reject; only approved items are released to the next hop. Keep vocabulary vendor-neutral: hold, approve, release, reject.

Persistence (Postgres + SQLAlchemy/Alembic) belongs in your stretch lab — the kata stays a pure state machine you can unit-test.

## Read these (verified)

1. [FastAPI — Path operations](https://fastapi.tiangolo.com/tutorial/path-operations/)
2. [SQLAlchemy 2.0 — ORM quick start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
3. [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## Next step

Assignment → `hold_state` + `rule_actions` katas → quiz.
