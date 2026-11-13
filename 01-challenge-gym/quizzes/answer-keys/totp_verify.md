# Quiz answer key — totp verify

Use only after attempting the quiz questions.

1. **Time-based One-Time Password** — shared secret + time-derived counter (Unix time ÷ step) → truncated HMAC-based digits.
2. TOTP is HOTP where the counter comes from time instead of a stored incrementing counter.
3. Window covers modest **clock skew** / boundary crossing. It does **not** replace rate limits, lockout, or replay tracking.
4. Avoid subtle crypto bugs; keep the challenge focused on understanding OTP + clean API use.
5. Examples: used-code / replay store, rate limits / lockout, secret-at-rest strategy, recovery-code one-time use.
6. Often **yes** if skew ≤ about one step and the window includes adjacent counters — exact outcome depends on step alignment; the point is window ≠ unlimited skew tolerance.
