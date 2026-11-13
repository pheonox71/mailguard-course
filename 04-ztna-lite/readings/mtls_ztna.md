# Reading — mTLS, device certs, ZTNA

## Learning objectives

1. Issue a lab client certificate from a private CA (`openssl` or `step-ca`).
2. Enforce mTLS in front of the admin (nginx/Caddy) and discuss CRL/OCSP pain.
3. Tie identity-bound access to ZTNA ideas; read **NIST SP 1800-35**.

**Why this matters.** Server TLS alone proves the *server* to the client. Without mutual TLS (mTLS) or another device signal, any client that reaches the port can speak — stolen cookies or a leaked URL may be enough. On the job, admin consoles and ZTNA-style admission often require a client certificate so only enrolled devices complete the handshake; revocation (CRL/OCSP) is the hard operational part.

**How it works.**

1. Stand up a **private CA** (lab: `openssl` or `step-ca`) and define who may receive client certificates.
2. Issue a **client certificate** (and private key) to an enrolled device or user.
3. Configure the reverse proxy (nginx/Caddy) to **require and verify** the client cert during the TLS handshake for the admin vhost.
4. On successful verify, optionally forward identity headers to the app; reject the handshake otherwise.
5. Operate **revocation** (CRL and/or OCSP): document lag — a stolen cert stays trusted until revocation data is published and fetched. Map the admission signal to ZTNA: identity + device proof → per-app access ([NIST SP 1800-35](https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture) for patterns, not a commercial mesh mandate).

```text
Client --TLS+client cert--> Proxy (verify vs private CA) --headers?--> Admin app
                \-- fail handshake if cert missing/untrusted/revoked
```

### Worked example

```text
# Conceptual checks a proxy performs (lab):
TLS ClientHello + Certificate message presents CN=device-42, issuer=Lab Client CA
Proxy: chain to Lab Client CA? ✔
       notAfter still valid?   ✔
       CRL/OCSP status?        good (or "unknown" — decide fail-open vs fail-closed)
Result: handshake completes; X-Client-DN: CN=device-42 forwarded
```

Why CA → issue → require that order: without a CA and issued cert first, “require client cert” only produces handshake failures you cannot debug.

### Common misconceptions / what goes wrong

- **“Server HTTPS already proves the client.”** Server TLS authenticates the server; without mTLS (or another client proof) any TCP client can still connect.
- **“Revocation is automatic once we issue certs.”** CRL/OCSP lag and fail-open defaults leave stolen certs trusted — document the workflow.
- **“mTLS replaces SSO/MFA.”** It is a strong *device* signal; user identity still comes from the IdP for ZTNA-style admission.
- **“Any client cert in the trust store is fine forever.”** Missing rotation/revocation turns a lost laptop into a permanent admin key.

## Read these (verified)

1. [NIST SP 1800-35 — Implementing a ZTA](https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture)
2. [step-ca](https://smallstep.com/docs/step-ca/)
3. [Mozilla — TLS client auth overview](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security)

## Lab idea

Private CA → client cert → require certificate on the admin vhost; document revocation workflow.

Why that order: without a CA and issued cert first, “require client cert” only produces handshake failures you cannot debug.

## Next step

`mtls_checks` kata → assignment → quiz.
