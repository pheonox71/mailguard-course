# Self-check — Crypto hygiene

Complete after [`../readings/crypto_hygiene.md`](../readings/crypto_hygiene.md). Attempt before opening the answer key.

1. Expand **HMAC** and say what secret it needs that a bare hash does not.
2. Expand **AEAD**. What does the “A” (associated data) typically protect?
3. Expand **TLS**. What does a server **certificate** bind together at a high level?
4. Name one misuse this kata refuses (wrong key length, nonce reuse, inventing a cipher, …).
5. List three **key lifecycle** verbs you should be able to discuss in an interview.
6. **Scenario:** A teammate proposes storing `sha256(api_key)` next to ciphertext “for integrity.” What do you push back with?

---

## Answer key (try first)

1. **Hash-based Message Authentication Code** — needs a secret **key** so only parties with the key can forge tags.
2. **Authenticated Encryption with Associated Data** — AAD is authenticated but not encrypted (headers, version strings, routing metadata).
3. **Transport Layer Security** — certificate binds a **public key** to a **name** (and related fields), signed by a trusted issuer chain.
4. Examples: empty/short AES key; skipping auth; rolling your own mode; comparing HMAC tags with `==` instead of constant-time compare.
5. Generate, store/protect, distribute, rotate, revoke/destroy (any solid three).
6. A hash without a key can be recomputed by anyone who can change the data; use HMAC or AEAD auth, not a bare digest.
