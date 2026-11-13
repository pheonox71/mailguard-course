# Answer key — PPAP / Secure Drop

1. Attacker who has the mailbox gets both ciphertext and password — same-channel secrecy fails.
2. Revoke (disable link); subsequent download must fail (403/410-style) even if the URL string is known.
3. Prefer hashed OTP + `hmac.compare_digest` (constant-time); never store plaintext OTP — DB leak would otherwise reveal the secret; `==` can also leak via timing on some runtimes.
4. Scanners cannot inspect payloads → blind delivery / malware-friendly channel.
5. No — global insecure practice, not a culture lesson.
6. Limit exposure if the share datastore leaks; compare hashes, not raw secrets.
