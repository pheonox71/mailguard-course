# Answer key — Basic auth client

1. `username:password` (colon-separated) then Base64 — not separately.
2. `open sesame`.
3. No — delta 40 > 30.
4. Must Base64 the single `user:pass` string, not each part.
5. TLS (HTTPS) so the header is not eavesdropped.
6. Missing tokens should fail closed; silent defaults hide auth bugs.
