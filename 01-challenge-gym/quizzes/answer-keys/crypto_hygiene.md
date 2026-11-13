# Quiz answer key — crypto hygiene

Use only after attempting the quiz questions.

1. **Hash-based Message Authentication Code** — needs a secret **key** so only parties with the key can forge tags.
2. **Authenticated Encryption with Associated Data** — AAD is authenticated but not encrypted (headers, version strings, routing metadata).
3. **Transport Layer Security** — certificate binds a **public key** to a **name** (and related fields), signed by a trusted issuer chain.
4. Examples: empty/short AES key; skipping auth; rolling your own mode; comparing HMAC tags with `==` instead of constant-time compare.
5. Generate, store/protect, distribute, rotate, revoke/destroy (any solid three).
6. A hash without a key can be recomputed by anyone who can change the data; use HMAC or AEAD auth, not a bare digest.
