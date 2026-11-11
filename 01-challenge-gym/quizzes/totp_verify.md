# Self-check — TOTP verify

Complete after [`../readings/totp_verify.md`](../readings/totp_verify.md). Attempt before opening the answer key.

1. Expand **TOTP** and state what inputs produce the short code.
2. How does TOTP relate to **HOTP**?
3. Why does `verify` often accept a small **window**? What problem does that *not* solve?
4. Name one reason a challenge-style task prefers a library (e.g. `pyotp`) over hand-rolling **HMAC**.
5. List two production MFA controls that belong later (e.g. in MailGuard MFA), not in this kata.
6. **Scenario:** A user’s phone clock is 45 seconds ahead of the server. With a 30-second step and `valid_window=1`, might a just-generated code still verify? Briefly why.

---

## Answer key (try first)

1. **Time-based One-Time Password** — shared secret + time-derived counter (Unix time ÷ step) → truncated HMAC-based digits.
2. TOTP is HOTP where the counter comes from time instead of a stored incrementing counter.
3. Window covers modest **clock skew** / boundary crossing. It does **not** replace rate limits, lockout, or replay tracking.
4. Avoid subtle crypto bugs; keep the challenge focused on understanding OTP + clean API use.
5. Examples: used-code / replay store, rate limits / lockout, secret-at-rest strategy, recovery-code one-time use.
6. Often **yes** if skew ≤ about one step and the window includes adjacent counters — exact outcome depends on step alignment; the point is window ≠ unlimited skew tolerance.
