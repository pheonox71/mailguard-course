# 03 — MailGuard MFA (+ passkeys / WebAuthn literacy)

Multi-Factor Authentication (**MFA**) on the MailGuard API path: Time-based One-Time Password (**TOTP**) enroll/verify + recovery codes (implementation planned), with a **passkeys / Web Authentication (WebAuthn)** reading track for phishing-resistant MFA.

**Authorship:** AI-generated readings/worksheets/quizzes. The student fills worksheets on `work`. Implementation stubs land as the API module matures — start with literacy + Challenge Gym TOTP kata.

## What this teaches

- TOTP enroll/verify and one-time recovery codes (secrets never in git)
- Why TOTP can still be phished (prompted codes) vs **WebAuthn** / passkeys (origin-bound)
- How this module pairs with `13` (OIDC) and `01` (`totp_verify`)

## Layout

| Path | Role |
|------|------|
| `readings/` | MFA + passkeys intros + credited videos |
| `quizzes/` | Self-checks |
| `worksheets/` | Guided questions before implementation |

## Start here

1. [`readings/passkeys_webauthn.md`](./readings/passkeys_webauthn.md) (can run in parallel with API work)
2. Quiz → worksheet
3. When coding: enroll/verify TOTP against the API; store secrets outside git

**Done when:** enroll/verify TOTP works; recovery codes one-time; passkeys worksheet completed; no secrets in git.

## Trade-offs / harden next

- Passkeys track is literacy-first (browser WebAuthn); full ceremony demo is optional stretch.
- Production needs attestation policy, backup strategies, and rate limits — document gaps honestly.
