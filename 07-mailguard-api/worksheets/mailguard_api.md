# Worksheet — MailGuard API

**Language:** Python 3 + FastAPI + pytest.

**Order:** skim the reading → answer below → read `tests/` → implement `katas/` → `pytest -q`.

## Concepts

- **Rule:** named decision (`hold` / `allow` / `reject`) with optional recipient-domain and substring predicates.
- **Evaluate:** first matching rule wins; otherwise a documented default.
- **API surface (conceptual):** create rule, list rules, evaluate message — even if your kata focuses on the engine first.

## Short questions

1. Why keep evaluation as a pure function separate from HTTP handlers?
2. What should happen when two rules match and the hold rule is listed first?
3. Name one production gap of an in-memory rule store.

## Done when

Answers written; tests green from *your* `katas/` implementations.
