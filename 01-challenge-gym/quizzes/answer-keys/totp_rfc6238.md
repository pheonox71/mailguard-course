# Answer key — Parametrized TOTP

1. The last byte (`digest[-1] & 0x0F`).
2. Eight.
3. The time step (often 30 seconds).
4. Reusing the 20-byte SHA-1 seed instead of the 64-byte SHA-512 seed from the errata.
5. Offsets become wrong → codes never match Appendix B.
6. To force a signed-positive 31-bit integer (interop / avoid sign issues).
7. `encoding/binary` (`binary.BigEndian.PutUint64`).
