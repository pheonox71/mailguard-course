# Reading — Identity depth (SAML, device certs, password managers)

## Learning objectives

1. Compare **SAML** and **OIDC** for enterprise single sign-on (**SSO**) at a high level.
2. Explain device certificates / posture as *additional signals*, not magic.
3. Threat-model an enterprise password manager for apps that still use passwords (non-SSO).

## Short intro

Module 13’s coding path is OIDC-shaped. Enterprises still run Security Assertion Markup Language (**SAML**) for many apps, issue device certificates for posture, and deploy password managers where SSO never arrived. This reading builds interview literacy without claiming you built a full Identity Provider (**IdP**).

## Videos (verified)

1. **[OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)** — OktaDev  
   Why it helps: OIDC as identity layer on OAuth — revisit before SAML compare.

2. Prefer the OWASP SAML + OAuth cheat sheets below for the SAML vs OIDC compare (video IDs bitrot). Optional: search “SAML vs OIDC” from IdP vendor developer channels and cross-check against OWASP.

Prefer written RFCs/docs below if videos move.

## Read these (verified)

1. [OWASP — SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
2. [OWASP — OAuth 2.0 / OIDC related cheat sheets](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
3. [Oasis — SAML Wiki / overview](https://wiki.oasis-open.org/security/FrontPage) — skim what assertions are.
4. [MDN — Client certificates (TLS)](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication) — adjacent posture ideas; pair with org device-management docs.
5. [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html) — authenticators & federation high-level.
6. [OWASP — Credential Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Storage_Cheat_Sheet.html) — why vaults beat spreadsheets (for apps still on passwords).

## Self-check

[`../quizzes/identity_depth.md`](../quizzes/identity_depth.md)
