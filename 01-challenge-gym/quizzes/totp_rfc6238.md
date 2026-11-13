# Quiz — Parametrized TOTP

1. Why does dynamic truncation take the offset from the **last** HMAC byte (low nibble) instead of a fixed position?
2. Why do Appendix B SHA-256/512 vectors fail if you reuse the 20-byte SHA-1 seed? (errata)
3. Counter is floor((t − T0) / X). Why does choosing X (the step) trade usability against how long a stolen code stays valid?
4. Scenario: your SHA-512 tests fail only for Appendix B — what seed-length mistake is most likely, and why does truncation look fine meanwhile?
5. Spot-the-bug: using the low 4 bits of `digest[0]` as the offset (instead of the last byte). What fails and why?
6. Why must the truncated value clear the high bit (`& 0x7F`)?
7. Why pack the counter as an 8-byte **big-endian** integer before HMAC (and which Go package does that packing)?
