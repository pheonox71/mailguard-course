# Answer key — Basic auth client

1. RFC 7617 defines one credential string; separate Base64 parts are not interoperable and break standard parsers.
2. Base64 is reversible encoding — anyone who sees the header recovers user:pass. Confidentiality needs TLS.
3. No — delta 40 > 30. A huge skew budget accepts very stale clocks and widens replay/TOTP timing abuse.
4. Must Base64 the single `user:pass` string; servers decode once then split on the first `:`.
5. Without TLS the Authorization header is eavesdropped on the wire.
6. Missing tokens should fail closed; silent defaults hide auth bugs and ship clients that think they are authenticated.
