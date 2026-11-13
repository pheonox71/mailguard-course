# Reading — Parametrized TOTP (RFC 6238)

## Learning objectives

1. Implement HOTP dynamic truncation (RFC 4226 §5.3) yourself.
2. Parametrize TOTP by digest (SHA-1/256/512), digits (6–10), step, and T0.
3. Validate against RFC 6238 Appendix B vectors and the errata on seed lengths.
4. Optionally port the same logic to Go (`crypto/hmac`, `encoding/binary`).

## Short intro

Library wrappers are fine for product MFA — but screening-style tasks often ask you to **derive the counter, HMAC, and truncate** correctly. Appendix B publishes known answers; the errata clarifies that the shared secret length matches the hash (20 / 32 / 64 bytes), not a single 20-byte seed for every digest.

Pair this with the Basic-auth JSON client kata when you need an authenticated call that also tolerates small clock skew.

## Read these (verified)

1. [RFC 4226 — HOTP](https://www.rfc-editor.org/rfc/rfc4226) — §5.3 truncation.
2. [RFC 6238 — TOTP](https://www.rfc-editor.org/rfc/rfc6238) — §4 + Appendix B.
3. [RFC 6238 errata](https://www.rfc-editor.org/errata_search.php?rfc=6238) — seed length per hash.
4. [RFC 7617 — HTTP Basic](https://www.rfc-editor.org/rfc/rfc7617) — Authorization header.

## Keep in mind

Never paste employer challenge text into public repos. Publish only your own generic implementation and keep secrets out of gists.

## Next step

Assignment → implement `katas/totp_rfc6238.py` → optional `go-totp/` → quiz.
