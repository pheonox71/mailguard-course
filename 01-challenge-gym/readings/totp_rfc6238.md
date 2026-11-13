# Reading — Parametrized TOTP (RFC 6238)

## Learning objectives

1. Implement HOTP dynamic truncation (RFC 4226 §5.3) yourself.
2. Parametrize TOTP by digest (SHA-1/256/512), digits (6–10), step, and T0.
3. Validate against RFC 6238 Appendix B vectors and the errata on seed lengths.
4. Optionally port the same logic to Go (`crypto/hmac`, `encoding/binary`).

**Why this matters.** Library wrappers are fine for product MFA — but screening-style tasks (and debugging interop) often require you to **derive the counter, HMAC, and truncate** correctly. Without the RFC 6238 errata on seed lengths, SHA-256/512 vectors fail mysteriously even when truncation looks right. On the job, knowing *how* TOTP is built helps you validate vendor libraries and clock-skew edge cases instead of treating OTP as a black box.

Appendix B publishes known answers; the errata clarifies that the shared secret length matches the hash (20 / 32 / 64 bytes), not a single 20-byte seed for every digest.

**How it works.**

1. Choose parameters: digest (SHA-1 / SHA-256 / SHA-512), `digits` (6–10), time step `X` (usually 30s), and epoch offset `T0` (usually 0).
2. Derive counter `T = floor((t − T0) / X)` from Unix time `t`.
3. Encode `T` as an 8-byte **big-endian** integer; compute `HMAC(K, counter_bytes)` with the shared secret `K`.
4. **Dynamic truncation** (RFC 4226 §5.3): take the low nibble of the **last** HMAC byte as offset; read four bytes from that offset; clear the high bit (`& 0x7FFFFFFF`); reduce mod `10^digits`.
5. Compare to Appendix B vectors — and use the errata seed lengths (20 / 32 / 64 bytes) so SHA-256/512 cases match.

```text
t, T0, X  →  T = floor((t-T0)/X)
K, T      →  HMAC → truncate → N-digit code
```

### Worked example

RFC 6238 Appendix B style (SHA-1, 8 digits, step 30, T0=0) — shape of the evaluation:

```text
t = 59
T = floor((59 - 0) / 30) = 1
counter (8-byte BE) = 00 00 00 00 00 00 00 01
HMAC-SHA1(K, counter) → 20-byte digest
offset = digest[-1] & 0x0f
code = (packed_4_bytes & 0x7fffffff) % 10**8
```

Use the Appendix B published codes as the oracle. If SHA-256 vectors disagree, check seed length first (errata: 32-byte seed for SHA-256, not the 20-byte SHA-1 seed).

### Common misconceptions / what goes wrong

- **“One 20-byte seed works for every digest in Appendix B.”** The errata requires seed length to match the hash; wrong length makes SHA-256/512 vectors fail even with correct truncation.
- **“Truncate from the first HMAC byte.”** Dynamic truncation uses the **last** byte’s low nibble as the offset — using the wrong end silently mismatches every vector.
- **“Little-endian counter is fine on x86.”** The RFC counter is big-endian; native endianness bugs pass local toys and fail Appendix B.
- **“Digits and step are always 6 and 30.”** Parametrized TOTP must honor the configured digits/step/T0 or interop with authenticators breaks.

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
