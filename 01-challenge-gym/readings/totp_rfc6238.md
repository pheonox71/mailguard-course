# Reading — Parametrized TOTP (RFC 6238)

## Learning objectives

1. Implement HOTP dynamic truncation (RFC 4226 §5.3) yourself.
2. Parametrize TOTP by digest (SHA-1/256/512), digits (6–10), step, and T0.
3. Validate against RFC 6238 Appendix B vectors and the errata on seed lengths.
4. Optionally port the same logic to Go (`crypto/hmac`, `encoding/binary`).

**Why this matters.** Library wrappers are fine for product MFA — but screening-style tasks (and debugging interop) often require you to **derive the counter, HMAC, and truncate** correctly. Without the RFC 6238 errata on seed lengths, SHA-256/512 vectors fail mysteriously even when truncation looks right. On the job, knowing *how* TOTP is built helps you validate vendor libraries and clock-skew edge cases instead of treating OTP as a black box.

**How it works.** Counter `T = floor((t − T0) / X)` (X usually 30s). HMAC the 8-byte big-endian counter with the shared secret. Dynamic truncation (RFC 4226 §5.3): offset from the **last** HMAC byte’s low nibble; take four bytes; clear the high bit (`& 0x7F`); reduce mod `10^digits`. Appendix B publishes known answers; the errata requires seed length to match the hash (20 / 32 / 64 bytes), not one 20-byte seed for every digest.

## Short note

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
