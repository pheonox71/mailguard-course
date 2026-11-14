# Reading — Local Keycloak lab (OIDC + logout / revocation)

## Learning objectives

1. Run **Keycloak** locally with Docker as a lab Identity Provider (**IdP**).
2. Create a realm and a public OpenID Connect (**OIDC**) client with **Proof Key for Code Exchange (PKCE)**, exact redirect URIs, and a logout redirect.
3. Practice **RP-initiated logout** and **refresh-token revocation** so “logout” is more than clearing a cookie.
4. Connect the lab to `jwt_checks` (id_token claims) and the PKCE / redirect katas.

**Why this matters.** SSO demos that only show “login works” hide the hard parts: redirect URI mismatches, missing PKCE, and sessions that survive after the user thinks they logged out. Without a local IdP you cannot safely break and fix those controls. On the job, cloud and email-admin portals federate to real IdPs — Keycloak in Docker is a vendor-neutral way to rehearse realm/client config, logout, and token revocation before you touch production tenants.

**How it works.**

1. Start Keycloak in Docker (dev mode is fine for a laptop lab; never expose it to the internet).
2. Create a **realm** (isolated tenant of users, clients, and keys) separate from the built-in `master` realm.
3. Register a **client** for MailGuard admin (or a local callback app): public client, standard flow + PKCE (S256), exact **Valid redirect URIs**, and a **Valid post logout redirect URI**.
4. Run an authorization-code + PKCE login; redeem the code; validate the **id_token** (`iss`, `aud`, `exp`, `nonce`, `alg`) — see the `jwt_checks` kata.
5. **Log out / revoke:** call RP-initiated logout so the IdP session ends, and revoke refresh tokens so silent renew cannot mint new access tokens after logout.

```text
Browser → Keycloak authorize (PKCE) → redirect_uri?code=…
App → token endpoint (code + code_verifier) → id_token + refresh_token
App validates id_token claims (+ JWKS signature in production)
Later: RP-initiated logout and/or refresh_token revoke
```

### Worked example

**1. Start Keycloak (Docker).** Use a lab-only admin password from your environment — do not commit real credentials.

```bash
# Lab only — bind to localhost. Set KC_BOOTSTRAP_ADMIN_PASSWORD in your shell
# to a local throwaway value (never a production secret).
# Current Keycloak docs use KC_BOOTSTRAP_ADMIN_USERNAME / KC_BOOTSTRAP_ADMIN_PASSWORD.
# Older guides used KEYCLOAK_ADMIN / KEYCLOAK_ADMIN_PASSWORD — those names are obsolete.
docker run --rm -p 127.0.0.1:8080:8080 \
  -e KC_BOOTSTRAP_ADMIN_USERNAME=admin \
  -e KC_BOOTSTRAP_ADMIN_PASSWORD \
  quay.io/keycloak/keycloak:26.0 start-dev
```

Open `http://127.0.0.1:8080` → Administration Console → sign in with the lab admin you set.

**2. Realm + client (OIDC, PKCE).**

| Setting | Lab value (example) |
|---------|---------------------|
| Realm | `mailguard-lab` |
| Client ID | `mailguard-admin` |
| Client authentication | Off (public client) |
| Standard flow | On |
| Direct access grants | Off (avoid password grant in the lab) |
| PKCE method | S256 |
| Valid redirect URIs | `http://127.0.0.1:3000/callback` (exact) |
| Valid post logout redirect URIs | `http://127.0.0.1:3000/` |
| Web origins | `http://127.0.0.1:3000` |

**3. Discovery document (shape).** After the realm exists:

```text
http://127.0.0.1:8080/realms/mailguard-lab/.well-known/openid-configuration
```

Note `authorization_endpoint`, `token_endpoint`, `end_session_endpoint`, `revocation_endpoint`, and `jwks_uri`.

**4. RP-initiated logout (shape).** Relying Party (**RP**) redirects the browser to the IdP end-session endpoint with `id_token_hint` and `post_logout_redirect_uri` that matches registration. Why: clearing the app cookie alone leaves the IdP SSO session alive — the next visit may silently sign the user back in.

**5. Refresh-token revocation (shape).** `POST` to the revocation endpoint with `token=<refresh_token>&token_type_hint=refresh_token` (and client auth if the client is confidential). Why: stolen refresh tokens otherwise keep minting access tokens after “logout.”

### Common misconceptions / what goes wrong

- **“Wildcard redirect URIs are fine for labs, so they are fine in prod.”** Open redirects and token theft follow loose matching — register exact URIs (RFC 9700).
- **“Logout = delete the session cookie.”** Without IdP logout and/or refresh-token revoke, SSO and refresh keep the user effectively signed in.
- **“PKCE is optional for a public SPA.”** Stolen authorization codes are usable without the verifier; turn on S256 for public clients (RFC 7636).
- **“id_token signature is enough; skip iss/aud/nonce.”** Mix-up and replay succeed when claims are not checked — pair JWKS verify with claim checks (`jwt_checks`).
- **“Put access tokens in localStorage for the SPA.”** Prefer a **Backend-for-Frontend (BFF)** with HTTP-only session cookies and CSRF defenses ([RFC 10017](https://www.rfc-editor.org/rfc/rfc10017)) — browser-held bearer tokens are XSS-exfiltratable.

## Videos (verified)

1. **[OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)** — OktaDev  
   Why it helps: mental model for authorize → code → tokens before you click through Keycloak screens.

2. **[Keycloak + Docker Compose: Setup & Authentication Tutorial](https://www.youtube.com/watch?v=WGcgiegv0W0)**  
   Why it helps: realm and client UI orientation; cross-check every click against current Keycloak docs (UI moves between versions).

Prefer the Keycloak guides below if a video moves.

## Read these (verified)

1. [Keycloak — Getting started](https://www.keycloak.org/guides#getting-started)
2. [OpenID Connect Core 1.0 — ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken)
3. [OpenID Connect RP-Initiated Logout 1.0](https://openid.net/specs/openid-connect-rpinitiated-1_0.html)
4. [RFC 7009 — OAuth 2.0 Token Revocation](https://www.rfc-editor.org/rfc/rfc7009)
5. [RFC 7636 — PKCE](https://www.rfc-editor.org/rfc/rfc7636)
6. [RFC 9700 — OAuth 2.0 Security BCP](https://www.rfc-editor.org/rfc/rfc9700)
7. [RFC 10017 — OAuth 2.0 for Browser-Based Apps](https://www.rfc-editor.org/rfc/rfc10017) — BFF + CSRF for SPAs talking to this lab IdP.

## Next step

Implement [`../katas/jwt_checks.py`](../katas/jwt_checks.py) until `pytest -q` is green, then revisit logout/revocation notes in [`identity_depth.md`](./identity_depth.md). Pair with [`saml_oidc_lab.md`](./saml_oidc_lab.md) for SAML vs OIDC.
