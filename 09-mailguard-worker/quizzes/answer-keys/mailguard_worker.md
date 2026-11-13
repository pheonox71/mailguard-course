# Quiz answer key — MailGuard Worker

Use only after attempting the quiz questions.

1. Dead-Letter Queue — messages that fail repeatedly are moved aside for inspection.
2. At-least-once delivery can redeliver; re-applying must not corrupt state.
3. Local tests/fakes; swap cloud providers; clearer boundaries.
4. hold / allow / reject (and rule match order).
5. Message is redelivered; without idempotency you may double-hold or double-notify.
6. Sensitive content leakage via logs; redact or hash; minimize retained body.
