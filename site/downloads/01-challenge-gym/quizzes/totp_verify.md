# Self-check — TOTP verify

Complete after [`../readings/totp_verify.md`](../readings/totp_verify.md). Attempt before opening the answer key.

1. Expand **TOTP** and state what inputs produce the short code.
2. How does TOTP relate to **HOTP**?
3. Why does `verify` often accept a small **window**? What problem does that *not* solve?
4. Name one reason a challenge-style task prefers a library (e.g. `pyotp`) over hand-rolling **HMAC**.
5. List two production MFA controls that belong later (e.g. in MailGuard MFA), not in this kata.
6. **Scenario:** A user’s phone clock is 45 seconds ahead of the server. With a 30-second step and `valid_window=1`, might a just-generated code still verify? Briefly why.
7. **What is a rate limit?** In MFA/TOTP verify, what does it limit, and why does that matter?
8. **What are replay controls?** What do they track, and why are they needed after a code verifies?
