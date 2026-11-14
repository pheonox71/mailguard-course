# Assignment — TOTP enroll and recovery codes

1. **Why** must enroll generate the secret server-side (or in a HSM-backed service) instead of accepting a user-supplied secret string?
2. **How** does `verify_totp` before “enrollment complete” prevent a broken authenticator pairing?
3. List three storage rules for recovery codes (at rest, in transit, after use) and **why** each rule exists.
4. **Scenario:** Helpdesk emails a fresh TOTP secret after a lost phone. What attack does that enable, and what should happen instead?
5. **Spot the bug:** `consume_recovery` returns True every time the code matches the original list, even after prior success. Fix in words.
6. How does this module’s enroll kata relate to Module 01 `totp_verify` and the passkeys reading — what is still missing for phishing resistance?
