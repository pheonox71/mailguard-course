# Worksheet — Parametrized TOTP

1. Write the HOTP truncation steps in your own words (offset byte → 31-bit int → mod 10^digits).
2. Why do Appendix B SHA-256/512 vectors need longer seeds than SHA-1? (errata)
3. Compute counter for t=59, step=30, t0=0.
4. When would you choose 8 digits vs 6 in a lab (not production UX)?
5. Sketch a Go `hmac.New` call with an 8-byte big-endian counter.

REPL warm-up: import hmac, hashlib, struct and HMAC a zero counter with the 20-byte Appendix B seed.
