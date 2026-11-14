# Reading — TOTP enroll and recovery codes

## Learning objectives

1. Enroll a TOTP secret and verify codes with a small clock window.
2. Issue **one-time recovery codes** and consume them safely.
3. Keep secrets out of git; document what production still needs (rate limits, attestation).

**Why this matters.** MFA enrollment is where secrets are born. A leaked base32 secret or reusable recovery code is as bad as no MFA. Without a clear enroll → verify → recover story, helpdesk resets become account-takeover paths. On the job, identity and email-admin portals implement the same lifecycle before they federate to passkeys.

**How it works.**

1. Generate a high-entropy **shared secret** (base32 for authenticator apps).
2. Show the student a provisioning URI / QR (lab) so the app can compute TOTP.
3. **Verify** a current code before marking enrollment complete (proves the secret was stored).
4. Issue **recovery codes** (random, single-use); store only hashes in production.
5. On lost device: consume one recovery code, then force re-enrollment — never email a new TOTP secret in the clear.

```text
enroll(secret + recovery codes) → verify TOTP → store hashed recovery
lost phone → consume_recovery once → re-enroll
```

### Worked example

Contract shape (see `katas/mfa_enroll.py`):

```python
enrollment = enroll(recovery_count=5)   # secret + 5 codes
assert verify_totp(enrollment, code_from_app)
assert consume_recovery(enrollment, enrollment.recovery_codes[0]) is True
assert consume_recovery(enrollment, enrollment.recovery_codes[0]) is False  # one-time
```

### Common misconceptions / what goes wrong

- **“Commit a demo secret for classmates.”** Even “test” secrets in git get copy-pasted into real apps — use local-only fixtures and `.env`.
- **“Recovery codes can be reused until we rotate.”** Reuse enables silent takeover after phishing one code.
- **“Verify is optional if the QR scanned.”** Without a challenge code, you may have stored a secret the user never controlled.
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
