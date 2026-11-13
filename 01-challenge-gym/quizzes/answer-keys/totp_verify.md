# Quiz answer key — totp verify

Use only after attempting the quiz questions.

1. **Time-based One-Time Password** — shared secret + time-derived counter (Unix time ÷ step) → truncated HMAC-based digits.
2. TOTP is HOTP where the counter comes from time instead of a stored incrementing counter.
3. Window covers modest **clock skew** / boundary crossing. It does **not** replace rate limits, lockout, or replay tracking.
4. Avoid subtle crypto bugs; keep the challenge focused on understanding OTP + clean API use.
5. Examples: used-code / replay store, rate limits / lockout, secret-at-rest strategy, recovery-code one-time use.
6. Sometimes. 45 s = 1.5 steps, so the phone's counter is ahead by 1 *or* 2 depending on where in the 30 s step the server is. With `valid_window=1` it verifies in **half** of cases (when the skew rounds to 1 step). The window tolerates ±1 step, not arbitrary skew.
