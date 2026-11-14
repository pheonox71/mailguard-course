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
4. Bind **service identity to Subject Alternative Name (SAN)** per [RFC 9525](https://www.rfc-editor.org/rfc/rfc9525) (DNS names for hosts). Treat **CN** as an optional *app-chosen client id* after verify — not as the hostname identity check.
5. On successful verify, optionally forward identity headers to the app **only from the trusted proxy**; reject the handshake otherwise. Never trust `X-Client-DN` / `x-client-cert-verified` from a direct client that skipped the proxy.
6. Operate **revocation** (CRL and/or OCSP): document lag — a stolen cert stays trusted until revocation data is published and fetched. Map the admission signal to ZTNA: identity + device proof → per-app access ([NIST SP 1800-35](https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture) for patterns, not a commercial mesh mandate).

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
- **“CN is the hostname identity.”** Modern TLS clients and servers authenticate names via SAN ([RFC 9525](https://www.rfc-editor.org/rfc/rfc9525)); CN is legacy. Apps may still read CN as a lab client id *after* the proxy verified the cert.
- **“If the header says SUCCESS, trust it.”** Spoofed `X-Client-DN` / verify headers from a non-proxy client bypass mTLS — only accept those headers on the proxy→app hop.
- **“Any client cert in the trust store is fine forever.”** Missing rotation/revocation turns a lost laptop into a permanent admin key.

## Read these (verified)

1. [NIST SP 1800-35 — Implementing a ZTA](https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture)
2. [step-ca](https://smallstep.com/docs/step-ca/)
3. [Mozilla — TLS client auth overview](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security)

## Lab idea — openssl (or step-ca) + nginx/Caddy

Private CA → client cert → require certificate on the admin vhost; document revocation workflow.

Why that order: without a CA and issued cert first, “require client cert” only produces handshake failures you cannot debug.

### Option A — openssl lab CA + client cert

```bash
# Lab-only keys — never reuse outside your laptop; do not commit private keys
mkdir -p /tmp/mtls-lab && cd /tmp/mtls-lab
openssl req -x509 -newkey rsa:2048 -nodes -keyout lab-ca.key -out lab-ca.crt \
  -days 365 -subj "/CN=MailGuard Lab Client CA"
openssl req -newkey rsa:2048 -nodes -keyout client.key -out client.csr \
  -subj "/CN=device-42"
openssl x509 -req -in client.csr -CA lab-ca.crt -CAkey lab-ca.key -CAcreateserial \
  -out client.crt -days 90
```

### Option B — step-ca (sketch)

```bash
# After step-ca is initialized in your lab (see smallstep docs):
step ca certificate device-42 client.crt client.key
step certificate inspect client.crt
```

### nginx — require client cert on admin vhost

```nginx
server {
  listen 443 ssl;
  server_name admin.mail.example;
  ssl_certificate     /etc/nginx/tls/server.crt;
  ssl_certificate_key /etc/nginx/tls/server.key;
  ssl_client_certificate /etc/nginx/tls/lab-ca.crt;
  ssl_verify_client on;
  location / {
    proxy_pass http://127.0.0.1:8080;
    proxy_set_header X-Client-DN $ssl_client_s_dn;
  }
}
```

### Caddy — client auth snippet

Use **`require_and_verify`** (not `require`). Caddy’s `require` only demands that a client *presents* a certificate; it does **not** verify the chain. With a `trust_pool`, the documented default is already `require_and_verify` — spell it out so a future config change cannot silently drop verification ([Caddy `tls` directive](https://caddyserver.com/docs/caddyfile/directives/tls)).

```caddy
admin.mail.example {
  tls {
    client_auth {
      mode require_and_verify
      trust_pool file /etc/caddy/lab-ca.crt
    }
  }
  reverse_proxy 127.0.0.1:8080
}
```

Document CRL/OCSP: how you revoke `device-42` and how long clients keep a stolen cert trusted.

### Negative lab — untrusted CA must fail the handshake

Issue a second CA and a client cert from it. Point Caddy’s `trust_pool` only at `lab-ca.crt` (the first CA). Present the untrusted client cert:

```bash
# Second CA + client cert (not in Caddy trust_pool)
openssl req -x509 -newkey rsa:2048 -nodes -keyout evil-ca.key -out evil-ca.crt \
  -days 365 -subj "/CN=Untrusted Lab CA"
openssl req -newkey rsa:2048 -nodes -keyout evil-client.key -out evil-client.csr \
  -subj "/CN=device-evil"
openssl x509 -req -in evil-client.csr -CA evil-ca.crt -CAkey evil-ca.key -CAcreateserial \
  -out evil-client.crt -days 90

# Expect handshake failure (exit non-zero / TLS alert), not HTTP 200:
curl -vk --cert evil-client.crt --key evil-client.key \
  https://admin.mail.example/healthz
```

**Why:** `mode require` would still accept this leaf (any presented cert). `require_and_verify` rejects it because the issuer is outside `trust_pool`.

## Videos (verified)

1. **[Transport Layer Security (TLS) — Computerphile](https://www.youtube.com/watch?v=0TLDTodL7Lc)** — literacy backdrop for client vs server certs  
   Why it helps: clarifies what mTLS adds after ordinary HTTPS.

## Next step

[`../assignments/mtls_ztna.md`](../assignments/mtls_ztna.md) → `mtls_checks` kata → quiz.
