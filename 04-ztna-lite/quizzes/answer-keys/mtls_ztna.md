# Answer key — mTLS / ZTNA

1. Without client auth, any TCP client that reaches the port can complete a server-authenticated TLS session — stolen URLs/cookies or unauthenticated clients still speak.
2. No — name binding ties the cert to the expected identity; skipping it accepts “any trusted CA leaf.”
3. Header spoofing bypasses mTLS — attackers inject SUCCESS without presenting a valid client cert.
4. Implementation patterns / ZTA building blocks for a local lab — literacy, not a vendor purchase.
5. Distribution lag, scale, downtime failure modes — stolen or revoked certs remain trusted until lists update.
6. Literacy + local lab with a private CA / proxy is enough; mesh is optional stretch.
