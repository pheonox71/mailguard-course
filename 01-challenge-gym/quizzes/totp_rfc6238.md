# Quiz — Parametrized TOTP

1. Dynamic truncation uses which byte of the HMAC to pick the offset?
2. Appendix B publishes codes with how many digits?
3. Counter formula is floor((t − T0) / X). What is X usually?
4. Scenario: your SHA-512 tests fail only for Appendix B — what seed-length mistake is most likely?
5. Spot-the-bug: using the low 4 bits of `digest[0]` as the offset (instead of the last byte). What breaks?
6. Why must the truncated value clear the high bit (`& 0x7F`)?
7. Optional Go port: which package packs the counter as big-endian uint64?
