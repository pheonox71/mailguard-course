# Reading — mTLS, device certs, ZTNA

## Learning objectives

1. Issue a lab client certificate from a private CA (`openssl` or `step-ca`).
2. Enforce mTLS in front of the admin (nginx/Caddy) and discuss CRL/OCSP pain.
3. Tie identity-bound access to ZTNA ideas; read **NIST SP 1800-35**.

## Read these (verified)

1. [NIST SP 1800-35 — Implementing a ZTA](https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture)
2. [step-ca](https://smallstep.com/docs/step-ca/)
3. [Mozilla — TLS client auth overview](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security)

## Lab idea

Private CA → client cert → require certificate on the admin vhost; document revocation workflow.

## Next step

`mtls_checks` kata → worksheet → quiz.
