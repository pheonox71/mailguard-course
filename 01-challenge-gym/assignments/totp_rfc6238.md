# Assignment — Parametrized TOTP

1. Walk HOTP truncation in your own words (offset byte → 31-bit int → mod 10^digits) and say **why** each step exists for interop.
2. Why do Appendix B SHA-256/512 vectors need longer seeds than SHA-1? (errata) What fails if you ignore it?
3. Compute counter for t=59, step=30, t0=0 — then explain why that formula (not wall-clock formatting) is what authenticators share.
4. When would you choose 8 digits vs 6 in a lab (not production UX), and what security/usability trade-off are you making?
5. Sketch a Go `hmac.New` call with an 8-byte big-endian counter and say why endianness matters for RFC vectors.

REPL warm-up: import hmac, hashlib, struct and HMAC a zero counter with the 20-byte Appendix B seed — why start from a known vector before your own tests.
