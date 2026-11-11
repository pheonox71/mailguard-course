# Worksheet — `hold_rules`

**Order:** skim [readings/hold_rules.md](../readings/hold_rules.md) → answer below in writing → read `tests/test_hold_rules.py` → implement `katas/hold_rules.py` → `pytest tests/test_hold_rules.py -q`

Peek at `solutions/hold_rules.py` only after a real attempt.

## Concepts to understand

- **Hold / allow / reject**: a tiny policy engine for outbound mail — decide what happens before send.
- **Ordered rules, first match wins**: priority is list order, not weights or scores.
- **Predicates**: each rule may constrain recipient **domain** and/or a **substring** in subject/body. Unspecified predicates are ignored; a rule with *no* predicates must never match (no accidental catch-all).
- **Case folding**: domains and substring checks are case-insensitive in this kata.

## Short questions (write answers before coding)

1. Why is “first match wins” easier to explain in an interview than a scored/weighted rule set?
2. If a rule has `recipient_domain="partner.example"` and `contains="confidential"`, must *both* hold for `matches` to be True?
3. What should `evaluate` return when no rule matches and the caller passes `default="allow"`?

## REPL warm-up

```python
from katas.hold_rules import Message, Rule

msg = Message(
    sender="alice@hennge.example",
    recipients=("bob@partner.example", "carol@hennge.example"),
    subject="Q4 forecast attached",
    body="Please review the confidential numbers.",
)
rule = Rule("ext", "hold", recipient_domain="partner.example")
# After you implement matches:
# from katas.hold_rules import matches, evaluate
# matches(rule, msg)
# evaluate(msg, [rule])
```

Hint for domain extraction: take the part after the last `@`, lowercased. Empty string if there is no `@`.

## Implement

Keep `Message` / `Rule` as given. Implement `matches` and `evaluate` only (helpers are fine).

## When to run pytest

```bash
pytest tests/test_hold_rules.py -q
```

Expect `NotImplementedError` until green. Then move to `recipient_risk`.
