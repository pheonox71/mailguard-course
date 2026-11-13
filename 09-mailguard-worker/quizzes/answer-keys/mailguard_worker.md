# Quiz answer key — MailGuard Worker

Use only after attempting the quiz questions.

1. At-least-once can redeliver after crashes; re-applying must not double-hold, double-notify, or double-send.
2. Local tests/fakes; swap providers; clearer boundaries. Without it, every unit test needs cloud creds and SDK mocks explode.
3. hold / allow / reject (and rule match order). Drift means API says hold while worker allows — silent policy holes.
4. Message is redelivered; without idempotency you may double-hold or double-notify. Handler should key off message/hold id and no-op safely if already applied.
5. Sensitive content leakage via logs; redact or hash; minimize retained body.
6. Tiny demos / ultra-low volume — you give up independent scale, clearer retries/DLQ, and deploy isolation.
