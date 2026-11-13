# Reading — Identity depth (SAML, device certs, password managers)

## Learning objectives

1. Compare **SAML** and **OIDC** for enterprise single sign-on (**SSO**) at a high level.
2. Explain device certificates / posture as *additional signals*, not magic.
3. Threat-model an enterprise password manager for apps that still use passwords (non-SSO).

**Why this matters.** Enterprises rarely run “OIDC only.” Without SAML literacy, device-posture signals, and a threat model for password managers on non-SSO apps, identity work stops at the happy path and fails in real estates of legacy apps. On the job, cloud and email-security admins still federate with both SAML and OIDC, and still protect vaults where SSO never arrived.

**How it works.** An Identity Provider (**IdP**) authenticates the user, then federates to apps: **OIDC** (identity layer on OAuth 2.0, typically JWT-shaped tokens) or **SAML** (XML assertions, classical enterprise SSO). Device certificates / posture add *signals* for admission — they do not replace user auth. Where SSO is missing, password managers reduce reuse but introduce vault, phishing-unlock, and shared-folder risks you must model.

![Identity provider federating SSO to applications via OIDC JSON tokens or SAML XML assertions](images/oidc-vs-saml.svg)

*Figure. One IdP, two common SSO wires: **OIDC** (identity layer on OAuth 2.0, JWT-shaped tokens) vs **SAML** (XML assertions). Notice the coding path here is OIDC-shaped, while enterprises still run both. Original course diagram (CC0).*

## Videos (verified)

1. **[OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)** — OktaDev  
   Why it helps: OIDC as identity layer on OAuth — revisit before SAML compare.

2. Prefer the OWASP SAML + OAuth cheat sheets below for the SAML vs OIDC compare (video IDs bitrot). Optional: search “SAML vs OIDC” from IdP vendor developer channels and cross-check against OWASP.

Prefer written RFCs/docs below if videos move.

## Read these (verified)

1. [OWASP — SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
2. [OWASP — OAuth 2.0 / OIDC related cheat sheets](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
3. [OASIS — SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) — assertions, bindings, and SSO flows.
4. [MDN — Authentication overview](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication) — browser auth landscape; for mTLS see [Cloudflare Learning — What is mutual TLS?](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/).
5. [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) (final, 31 Jul 2025; incorporates syncable authenticators / passkeys) — authenticators & federation high-level. Companion HTML: [pages.nist.gov/800-63-4](https://pages.nist.gov/800-63-4/sp800-63b.html).
6. [OWASP — Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — why vaults beat spreadsheets (for apps still on passwords). For server-side password hashing see [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).

## Quiz (required)
[`../quizzes/identity_depth.md`](../quizzes/identity_depth.md)
