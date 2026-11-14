# Reading — SAML 2.0 + OIDC lab deepen

## Learning objectives

1. Run **Keycloak** locally as an IdP (lab only).
2. Contrast auth-code + **PKCE** (OIDC) with SAML SP/IdP-initiated flows.
3. Check assertion conditions: audience, recipient/ACS, time window, InResponseTo, signature present.
4. Know headline attacks: XML Signature Wrapping, unsigned assertions, open redirects; OAuth mix-up / redirect URI mismatch.

**Why this matters.** Federation bugs are not theoretical: unsigned assertions, loose ACS/redirect matching, and missing PKCE turn “we have SSO” into account takeover. Without checking audience, time windows, and InResponseTo, replay and mix-up attacks succeed. On the job, identity engineers validate these conditions every time a new app joins the IdP.

**How it works.**

**SAML (SP-initiated shape):**

1. User hits the SP; SP redirects to the IdP (often with `RelayState`).
2. IdP authenticates the user and returns a signed XML assertion (POST or redirect binding) to the Assertion Consumer Service (**ACS**).
3. SP verifies: signature present and trusted, **audience**, **recipient/ACS**, time window (`NotOnOrAfter` + skew), and **InResponseTo** (binds to the authn request).
4. On success, SP creates an application session.

**OIDC auth-code + PKCE (RFC 7636):**

1. Client creates `code_verifier` / `code_challenge` and redirects to the IdP authorize endpoint with an exact **redirect_uri**.
2. User authenticates; IdP returns an authorization `code` to that redirect URI.
3. Client redeems the code at the token endpoint, proving possession of `code_verifier`.
4. Client validates tokens (issuer, audience, signature, nonce where used). Exact redirect matching and issuer checks blunt mix-up (RFC 9700).
5. For browser apps, prefer a **Backend-for-Frontend (BFF)** that keeps tokens server-side and uses cookie sessions with CSRF defenses ([RFC 10017](https://www.rfc-editor.org/rfc/rfc10017)) rather than storing access tokens in JavaScript storage.

Lab IdPs like Keycloak let you break and fix these checks safely.

### Worked example

```text
SAML condition checklist (fixture-style):
  ✔ Signature: RSA-SHA256 over Assertion, cert matches IdP metadata
  ✔ Audience:  https://sp.example.com/metadata
  ✔ Recipient: https://sp.example.com/acs
  ✔ Time:      NotOnOrAfter = now+5m, skew allowance ±2m
  ✔ InResponseTo: matches AuthnRequest ID _abc123

OIDC token request (shape):
  POST /token
  grant_type=authorization_code
  code=SplxlOBeZQQYbYS6WxSbIA
  redirect_uri=https://app.example.com/callback   # must match authorize request exactly
  code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

If `redirect_uri` differs by a trailing slash, honest clients fail closed — and open redirect / mix-up bugs get blocked when registration enforces exact match.

### Common misconceptions / what goes wrong

- **“Signature on the Response is enough; skip Assertion checks.”** XML Signature Wrapping and unsigned assertions exploit incomplete verification — check the assertion the SP will trust (OWASP SAML cheat sheet).
- **“PKCE is only for mobile.”** Public and many confidential clients use PKCE so a stolen code alone is useless (RFC 7636 / RFC 9700).
- **“Clock skew of a few minutes can be ignored.”** Too-tight windows lock out users; too-loose windows widen replay — document skew like cert rollover.
- **“IdP-initiated SAML is always safer.”** Without careful RelayState/ACS handling it enables open redirects; treat it as an operational choice with controls, not a free upgrade.


## Videos (verified)

1. **[OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)**  
   Why it helps: OIDC vs related flows literacy.

## Read these (verified)

1. [OASIS SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)
2. [OWASP SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
3. [RFC 7636 — PKCE](https://www.rfc-editor.org/rfc/rfc7636)
4. [RFC 9700 — OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700)
5. [RFC 10017 — OAuth 2.0 for Browser-Based Apps](https://www.rfc-editor.org/rfc/rfc10017) — BFF + CSRF for browser clients.
6. [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
7. [Keycloak — Getting started](https://www.keycloak.org/guides#getting-started)

## Keep in mind

Certificate rollover, clock skew, RelayState, and single logout are operational details — document them in the assignment even when the kata uses fixtures. Why: production outages from skew/rollover look like “SSO is down,” not like a coding bug.

## Next step

`saml_checks` + `pkce` katas → quiz.
