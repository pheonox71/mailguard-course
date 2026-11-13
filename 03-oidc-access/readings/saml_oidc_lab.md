# Reading — SAML 2.0 + OIDC lab deepen

## Learning objectives

1. Run **Keycloak** locally as an IdP (lab only).
2. Contrast auth-code + **PKCE** (OIDC) with SAML SP/IdP-initiated flows.
3. Check assertion conditions: audience, recipient/ACS, time window, InResponseTo, signature present.
4. Know headline attacks: XML Signature Wrapping, unsigned assertions, open redirects; OAuth mix-up / redirect URI mismatch.

**Why this matters.** Federation bugs are not theoretical: unsigned assertions, loose ACS/redirect matching, and missing PKCE turn “we have SSO” into account takeover. Without checking audience, time windows, and InResponseTo, replay and mix-up attacks succeed. On the job, identity engineers validate these conditions every time a new app joins the IdP.

**How it works.** **SAML:** IdP issues a signed XML assertion; the SP verifies signature, audience, recipient/ACS, time window (`NotOnOrAfter` + skew), and InResponseTo (SP-initiated), then creates a session. **OIDC:** auth-code flow + **PKCE** (RFC 7636) binds the code to the client that started the flow; exact redirect URI matching and issuer checks blunt mix-up (RFC 9700). Lab IdPs like Keycloak let you break and fix these checks safely.

## Read these (verified)

1. [OASIS SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)
2. [OWASP SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
3. [RFC 7636 — PKCE](https://www.rfc-editor.org/rfc/rfc7636)
4. [RFC 9700 — OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700)
5. [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
6. [Keycloak — Getting started](https://www.keycloak.org/guides#getting-started)

## Keep in mind

Certificate rollover, clock skew, RelayState, and single logout are operational details — document them in the assignment even when the kata uses fixtures. Why: production outages from skew/rollover look like “SSO is down,” not like a coding bug.

## Next step

`saml_checks` + `pkce` katas → quiz.
