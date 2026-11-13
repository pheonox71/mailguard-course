# Reading — ZTNA lite

## Learning objectives

1. Define **Zero Trust** as “never trust, always verify” with continuous evaluation — not a single product SKU.
2. Contrast network-level **VPN** admission with application-level **ZTNA**.
3. Name Policy Engine / Policy Enforcement Point ideas from National Institute of Standards and Technology (**NIST**) SP 800-207 at a high level.

**Why this matters.** Classical VPN admission parks a client on a flat corporate LAN. After credential theft or malware, **lateral movement** reaches many internal services. Without per-app verification, “we have SSO” still leaves a wide network path open. On the job, cloud and identity teams pair IdPs with Zero Trust Network Access (**ZTNA**) so contractors and admins reach *one* app, not the whole estate.

Classical remote access: join a VPN, then reach wide internal ranges. If malware or a stolen laptop lands on that network, **lateral movement** is easier. ZTNA aims to grant access to *specific applications* after verifying user identity, often device posture, and context — ideally without parking the client on a flat corporate LAN.

**How it works.**

1. User requests an application (not “the corporate network”).
2. Identity is verified (often MFA / OIDC via an IdP); device posture and context may be collected.
3. A **policy engine** (NIST SP 800-207 vocabulary) evaluates allow/deny for *that* app and session.
4. A **policy enforcement point** grants a narrow path to the application — ideally without broad LAN admission.
5. Evaluation continues (session risk, posture change); access is not a one-time VPN ticket for the whole estate.

```text
VPN:   Client → VPN concentrator → flat LAN → many services
ZTNA:  Client → identity/posture → Policy Engine → PEP → one app
```

MailGuard modules already practice app identity (TOTP, OIDC). ZTNA is the *network/access path* story that enterprises pair with identity providers.

![Side-by-side contrast of VPN network admission versus ZTNA application-level access with policy engine](images/ztna-vs-vpn.svg)

*Figure. VPN admits the client onto a broad LAN (lateral movement risk). ZTNA checks identity/posture/context, then a Policy Engine / Enforcement Point grants **per-app** access — notice “never trust, always verify,” not a single product SKU. Original course diagram (CC0).*

### Worked example

```text
Request: contractor needs https://admin.mail.example (only)
Signals: OIDC login + MFA OK; device posture = managed; location = expected country
Policy:  allow app=admin.mail.example; deny lateral routes to hr-db.internal
PEP:     issues app-scoped access; no RFC1918 “full tunnel” to 10.0.0.0/8
```

Same user on a classical VPN might route to `hr-db.internal` after a phish; ZTNA never admitted that path.

### Common misconceptions / what goes wrong

- **“Zero Trust is a product SKU we can buy once.”** It is an architecture of continuous verification (NIST SP 800-207); products implement pieces.
- **“SSO means we already have Zero Trust.”** SSO authenticates the user to an app; without per-app enforcement you may still have VPN-style lateral paths.
- **“ZTNA replaces MFA.”** ZTNA consumes identity/MFA (and often posture); it does not make weak auth strong.
- **“After first admit, trust the session forever.”** Continuous evaluation is the point — posture loss or risk change should revoke or step-up.

## Videos (verified)

1. **[What Is Zero Trust Architecture (ZTA)? NIST 800-207 Explained](https://www.youtube.com/watch?v=5Kq64vOgE10)**  
   Why it helps: policy engine vs enforcement point vocabulary.

2. **[Zero Trust, Before The Cloud (Bsides-style talk)](https://www.youtube.com/watch?v=M0Pb8GNxWl8)** — Ben Lintern  
   Why it helps: identity-aware networking vs “VPN then flat access,” with practical skepticism.

## Read these (verified)

1. [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — abstract + section on ZTA components.
2. [NIST Zero Trust Architecture portal](https://www.nist.gov/publications/zero-trust-architecture) — publication landing.
3. [NCSC (UK) — Zero trust architecture design principles](https://www.ncsc.gov.uk/collection/zero-trust-architecture) — pragmatic principles.
4. [Cloudflare Learning — What is ZTNA?](https://www.cloudflare.com/learning/access-management/what-is-ztna/) — plain-language ZTNA vs VPN (vendor learning site; read for concepts).

## Quiz (required)
[`../quizzes/ztna_lite.md`](../quizzes/ztna_lite.md)
