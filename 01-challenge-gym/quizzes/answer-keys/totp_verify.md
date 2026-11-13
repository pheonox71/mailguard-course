# Quiz answer key — totp verify

Use only after attempting the quiz questions.

1. A static secret alone is a reusable password; the time counter makes codes short-lived so a captured code expires.
2. TOTP is HOTP where the counter comes from time instead of a stored incrementing counter — both sides can compute without syncing a counter DB.
3. Window covers modest **clock skew** / boundary crossing. It does **not** replace rate limits, lockout, or replay tracking.
4. Avoid subtle crypto bugs; keep the challenge focused on understanding OTP + clean API use.
5. Online guessing (no throttle) and replaying a just-used code within the step/window (no replay store).
6. Sometimes. 45 s ≈ 1.5 steps; with `valid_window=1` it verifies in **half** of cases depending on where in the step the server is. The window tolerates ±1 step, not arbitrary skew.
