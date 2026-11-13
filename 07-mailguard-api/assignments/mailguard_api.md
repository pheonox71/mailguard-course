# Assignment — MailGuard API

**Language:** Python 3 + FastAPI + pytest.

**Order:** skim the reading → answer below → read `tests/` → implement `katas/` → `pytest -q`.

## Concepts

- **Rule:** named decision (`hold` / `allow` / `reject`) with optional recipient-domain and substring predicates.
- **Evaluate:** first matching rule wins; otherwise a documented default.
- **API surface (conceptual):** create rule, list rules, evaluate message — even if your kata focuses on the engine first.

## Short questions (why / how / scenario)

1. **Why** keep evaluation as a pure function separate from HTTP handlers?
2. **Scenario:** two rules match and the hold rule is listed first — what happens, and **why** must operators care about list order?
3. Name one production gap of an in-memory rule store and **why** the kata still starts there.
4. **How** would you explain first-match-wins vs a “highest severity wins” engine to a teammate — trade-off in one sentence?

When you run tests, prefer `pytest -q` from the module directory **why:** fail fast on the evaluate contract before polishing routes.

## Done when

Answers written; tests green from *your* `katas/` implementations.
