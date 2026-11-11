# Worksheet — `recipient_risk`

**Order:** skim [readings/recipient_risk.md](../readings/recipient_risk.md) → answer below in writing → read `tests/test_recipient_risk.py` → implement `katas/recipient_risk.py` → `pytest tests/test_recipient_risk.py -q`

Peek at `solutions/recipient_risk.py` only after a real attempt.

## Concepts to understand

- **Missend risk**: sending to internal *and* external recipients in one go is a common DLP / email-security hold signal.
- **Normalize before compare**: strip + lowercase so `Alice@Mailguard.Example` and `alice@mailguard.example` are the same person.
- **Simple address shape only**: this kata is `local@domain` with a dot in the domain — not full RFC 5322 / display names.
- **`RiskReport`**: already provides `mixed` and `should_hold`. Your job is to fill `normalize_email` and `classify` correctly so those properties light up.

## Short questions (write answers before coding)

1. Why hold on *invalid* addresses as well as mixed internal/external?
2. Should duplicate normalized addresses appear twice in `internal` / `external`? What about the original invalid string `"bad"`?
3. What must `classify` do if `internal_domain` is `"  "` (whitespace)?

## REPL warm-up

```python
# Sketch normalize rules yourself first, then try:
candidates = ["  Alice@Mailguard.Example ", "not-an-email", "a@b", "ok@mailguard.example"]
for c in candidates:
    s = c.strip().lower()
    print(repr(c), "→", s, "| @ count:", s.count("@"))
```

Think through: exactly one `@`? non-empty local? domain contains `.`?

```python
# After implement:
# from katas.recipient_risk import classify
# classify(["alice@mailguard.example", "bob@partner.com"], internal_domain="mailguard.example")
```

## Implement

`RiskReport` (including properties) stays as given. Implement `normalize_email` and `classify`.

## When to run pytest

```bash
pytest tests/test_recipient_risk.py -q
# or the whole gym:
pytest -q
```

Expect failures until both functions work. Full suite green = Challenge Gym Phase A done for this folder.
