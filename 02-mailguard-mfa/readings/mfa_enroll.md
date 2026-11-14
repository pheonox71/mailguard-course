# Reading — TOTP enroll and recovery codes

## Learning objectives

1. Enroll a TOTP secret and verify codes with a small clock window.
2. Issue **one-time recovery codes** and consume them safely.
3. Reject **replay** of a just-accepted code (`last_used_step`) and **throttle** failed guesses to lockout.
4. Keep secrets out of git; document what production still needs (attestation, hashed recovery at rest).

**Why this matters.** MFA enrollment is where secrets are born. A leaked base32 secret, a reusable recovery code, or a phished TOTP that still works a second time is as bad as no MFA. Without enroll → verify-once-per-step → recover, helpdesk resets and live-code phishing become account-takeover paths. On the job, identity and email-admin portals implement the same lifecycle before they federate to passkeys.

**How it works.**

1. Generate a high-entropy **shared secret** (base32 for authenticator apps).
2. Show the student a provisioning URI / QR (lab) so the app can compute TOTP.
3. **Verify** a current code before marking enrollment complete (proves the secret was stored).
4. On success, record **`last_used_step`** (time-step index). Reject any later verify whose matching step is **`<= last_used_step`** — not only equality. A ±1 skew window otherwise still accepts step N−1 after N succeeded. [RFC 6238 §5.2](https://www.rfc-editor.org/rfc/rfc6238#section-5.2) requires one-time use after successful validation.
5. Count failed verifies; after `MAX_FAILED_ATTEMPTS`, set **`locked`** so further codes (even valid ones) fail until an out-of-band unlock — throttle/lockout per [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html) authenticator guidance.
6. Issue **recovery codes** (random, single-use); store only hashes in production.
7. On lost device: consume one recovery code, then force re-enrollment — never email a new TOTP secret in the clear.

```text
enroll → verify TOTP (record last_used_step) → store hashed recovery
replay same or older step → reject
too many wrong codes → locked
lost phone → consume_recovery once → re-enroll
```

### Worked example

Contract shape (see `katas/mfa_enroll.py`):

```python
enrollment = enroll(recovery_count=5)   # secret + 5 codes
assert verify_totp(enrollment, code_from_app) is True
assert verify_totp(enrollment, code_from_app) is False  # same/older step = replay
assert consume_recovery(enrollment, enrollment.recovery_codes[0]) is True
assert consume_recovery(enrollment, enrollment.recovery_codes[0]) is False  # one-time
```

### Common misconceptions / what goes wrong

- **“Commit a demo secret for classmates.”** Even “test” secrets in git get copy-pasted into real apps — use local-only fixtures and `.env`.
- **“Recovery codes can be reused until we rotate.”** Reuse enables silent takeover after phishing one code.
- **“Verify is optional if the QR scanned.”** Without a challenge code, you may have stored a secret the user never controlled.
- **“`valid_window` already stops replay.”** The window only covers clock skew; without `last_used_step`, a phished live code still works twice. Equality-only `last_used_step` still leaves N−1 open after N.
- **“TOTP enroll finishes MFA.”** Passkeys/WebAuthn resist phishing better — see the passkeys reading.

## Videos (verified)

1. **[Make Your Accounts Safer with Multifactor Authentication (MFA)](https://www.youtube.com/watch?v=XIlF2qkav5c)** — CISA  
   Why it helps: places MFA factors in plain language before you implement enroll.

## Read these (verified)

1. [RFC 6238 — TOTP](https://www.rfc-editor.org/rfc/rfc6238)
2. [OWASP — MFA](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)
3. Module 01 `totp_verify` reading (shared secret + window)

## Next step

[`../assignments/mfa_enroll.md`](../assignments/mfa_enroll.md) → implement `katas/mfa_enroll.py` → [`../quizzes/mfa_enroll.md`](../quizzes/mfa_enroll.md).
