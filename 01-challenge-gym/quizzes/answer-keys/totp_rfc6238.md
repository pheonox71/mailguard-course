# Answer key — Parametrized TOTP

1. RFC 4226 §5.3 defines that offset so implementations interoperate; a fixed position would disagree with authenticators and Appendix B.
2. Errata: seed length must match the hash (32 / 64 bytes for SHA-256/512). Wrong key → wrong HMAC → wrong codes.
3. Smaller X rotates codes faster (less replay window) but increases clock-boundary friction; larger X is more forgiving and more replayable.
4. Reusing the 20-byte SHA-1 seed instead of the 64-byte SHA-512 seed — truncation math can be correct while the HMAC input key is wrong.
5. Offsets become wrong → codes never match Appendix B / real authenticators.
6. Forces a signed-positive 31-bit integer for interop and to avoid sign/endian surprises across languages.
7. Interop with RFC vectors and authenticators; Go: `encoding/binary` (`binary.BigEndian.PutUint64`).
