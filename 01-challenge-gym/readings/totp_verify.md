# Reading — TOTP verify (`totp_verify`)

## Learning objectives

By the end of this kata’s reading + worksheet + implementation, you should be able to:

1. Explain TOTP as HOTP with a time-derived counter (shared secret + time step → short code).
2. State why a small verification **window** exists (clock skew) and what it does *not* replace (rate limits, replay controls).
3. Verify codes with `pyotp` instead of hand-rolling HMAC — and point to RFC 6238 / OWASP MFA literacy in an interview.

## Short intro

Time-based one-time passwords (TOTP) let a server and an authenticator app compute the same short code from a **shared secret** and the **current time** (usually a 30-second step). You do **not** need to reimplement HMAC-SHA1 for a short challenge — understand the model, then use a well-regarded library (`pyotp`) to verify codes, including a small **window** for clock skew. Production MFA still needs replay protection, rate limits, and secret storage discipline; those belong later (`03-mailguard-mfa/`).

HENNGE’s Admission Challenge explicitly pairs a short coding task with **MFA/OTP research**, and prefers elegant solutions over over-engineering.

## Videos (verified)

1. **[2FA: Two Factor Authentication](https://www.youtube.com/watch?v=ZXFYT-BG2So)** — Computerphile (feat. Dr Mike Pound)  
   Why it helps: crisp mental model of MFA factors (know / have / are) before you touch libraries.

2. **[How HOTP and TOTP work](https://www.youtube.com/watch?v=46AKWNOJ3-Y)** — loops  
   Why it helps: walks HMAC → truncation → counter vs Unix-time step, plus the validation **window** you’ll use in `verify`.

3. **[A Tale of Two Factors: A Deep Dive into Two Factor Authentication](https://www.youtube.com/watch?v=4wZ9jM4coV4)** — Kelley Robinson @ PyGotham 2019  
   Why it helps: compares SMS vs TOTP soft tokens and includes Python-oriented TOTP implementation notes aligned with this kata.

## Read these (verified)

### Specs & library

1. [RFC 6238 — TOTP: Time-Based One-Time Password Algorithm](https://datatracker.ietf.org/doc/html/rfc6238) — the standard behind authenticator apps (period, digits, time counter).
2. [RFC 4226 — HOTP](https://datatracker.ietf.org/doc/html/rfc4226) — TOTP builds on HOTP; skim security requirements / throttling ideas.
3. [PyOTP documentation](https://pyauth.github.io/pyotp/) — `TOTP.verify(..., valid_window=...)`, provisioning URIs; prefer this over reinventing crypto.

### Concepts & security literacy

4. [MDN — One-time passwords (OTP)](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication/OTP) — email/SMS/TOTP comparison; why TOTP is preferred among OTP channels.
5. [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) — MFA factors, threats, practical controls.

### Why this kata exists (HENNGE)

6. [Demystifying HENNGE’s Hiring Process](https://hennge.com/global/info/henka/interview/202406-demystifying_hennges_hiring_process/) — backend challenge: short task + MFA/OTP research; concise > over-engineered.
7. [HENNGE One](https://hennge.com/global/service/one/) — Identity Edition / MFA as product context (literacy, not a clone).
8. [GIP](https://recruit.hennge.com/en/gip/) — early-career path and challenge culture.
9. [Access Control JD (Python)](https://recruit.hennge.com/en/mid-career-ngh/senior-software-engineer-python-web-dev-hennge-access-control/) — identity / access policy career signal (years bars are separate).

## Optional deepeners

- [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html) — authenticator guidance at a high level (linked from PyOTP’s reading list).
- Skim only: security considerations sections inside RFC 6238 / 4226 once the kata is green.
