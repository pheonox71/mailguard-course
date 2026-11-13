# Reading — mTLS, device certs, ZTNA

## Learning objectives

1. Issue a lab client certificate from a private CA (`openssl` or `step-ca`).
2. Enforce mTLS in front of the admin (nginx/Caddy) and discuss CRL/OCSP pain.
3. Tie identity-bound access to ZTNA ideas; read **NIST SP 1800-35**.

**Why this matters.** Server TLS alone proves the *server* to the client. Without mutual TLS (mTLS) or another device signal, any client that reaches the port can speak — stolen cookies or a leaked URL may be enough. On the job, admin consoles and ZTNA-style admission often require a client certificate so only enrolled devices complete the handshake; revocation (CRL/OCSP) is the hard operational part.

**How it works.** A private CA issues client certificates. The reverse proxy (nginx/Caddy) requires and verifies the client cert during TLS, then (optionally) forwards identity headers only after a successful verify. Map that admission signal to ZTNA: identity + device proof → per-app access. Document CRL/OCSP lag — stale revocation lists leave stolen certs trusted. Lab only: follow [NIST SP 1800-35](https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture) for implementation patterns, not a commercial mesh mandate.

## Read these (verified)

1. [NIST SP 1800-35 — Implementing a ZTA](https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture)
2. [step-ca](https://smallstep.com/docs/step-ca/)
3. [Mozilla — TLS client auth overview](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security)

## Lab idea

Private CA → client cert → require certificate on the admin vhost; document revocation workflow.

Why that order: without a CA and issued cert first, “require client cert” only produces handshake failures you cannot debug.

## Next step

`mtls_checks` kata → assignment → quiz.
