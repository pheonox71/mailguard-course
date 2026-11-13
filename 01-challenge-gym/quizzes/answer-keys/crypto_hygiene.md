# Quiz answer key — crypto hygiene

Use only after attempting the quiz questions.

1. Without a key anyone who can change the message can recompute the digest; HMAC tags are forgeable only with the secret.
2. Attackers can swap metadata (version, tenant id, routing) while keeping a valid body ciphertext; AAD binds that metadata to the seal.
3. Certificates bind a public key to a name via a trusted chain so clients can authenticate the server without a pre-shared password per site.
4. Nonce reuse with AES-GCM catastrophically breaks confidentiality/authenticity; invented modes skip decades of review and fail subtly.
5. Store (secret in git) and rotate/revoke failed — any past commit or clone holder can forge webhook tags forever until rotated and revoked.
6. A hash without a key can be recomputed by anyone who can change the data; use HMAC or AEAD auth, not a bare digest.
