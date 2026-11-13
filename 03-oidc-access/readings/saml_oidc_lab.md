# Reading — SAML 2.0 + OIDC lab deepen

## Learning objectives

1. Run **Keycloak** locally as an IdP (lab only).
2. Contrast auth-code + **PKCE** (OIDC) with SAML SP/IdP-initiated flows.
3. Check assertion conditions: audience, recipient/ACS, time window, InResponseTo, signature present.
4. Know headline attacks: XML Signature Wrapping, unsigned assertions, open redirects; OAuth mix-up / redirect URI mismatch.

## Read these (verified)

1. [OASIS SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)
2. [OWASP SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
3. [RFC 7636 — PKCE](https://www.rfc-editor.org/rfc/rfc7636)
4. [RFC 9700 — OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700)
5. [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
6. [Keycloak — Getting started](https://www.keycloak.org/guides#getting-started)

## Keep in mind

Certificate rollover, clock skew, RelayState, and single logout are operational details — document them in the worksheet even when the kata uses fixtures.

## Next step

`saml_checks` + `pkce` katas → quiz.
