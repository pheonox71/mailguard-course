# 03 — OIDC / access policy (+ identity depth)

Happy-path OpenID Connect (**OIDC**) login + protected routes, extended with **SAML** comparison, device-certificate *concepts*, and enterprise **password manager** literacy for non-SSO apps.

## What this teaches

- OIDC login + logout/revocation notes (no inflated SSO claims)
- Local **Keycloak** lab (realm/client, PKCE, redirect URIs, RP-initiated logout, refresh revoke)
- **id_token** claim checks (`iss` / `aud` / `exp` / `nonce` / `alg`) via `jwt_checks`
- Security Assertion Markup Language (**SAML**) vs OIDC federation comparison
- Device posture / client certificates as *concepts* (not a PKI build)
- Why non-SSO apps still need a vault / password manager threat model

## Start here

1. [`readings/identity_depth.md`](./readings/identity_depth.md) → assignment → quiz
2. [`readings/keycloak_lab.md`](./readings/keycloak_lab.md) (Docker IdP + logout/revocation)
3. [`readings/saml_oidc_lab.md`](./readings/saml_oidc_lab.md)
4. Pair with `02` passkeys reading and `04` ZTNA

**Done when:** OIDC demo + identity-depth assignment; Keycloak lab notes; `jwt_checks` green; honest claims only.

## Coding lab

```bash
cd 03-oidc-access
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Implement:

- `katas/oidc_checks.py` — redirect allow-list, state check, code parse
- `katas/pkce.py` / `katas/saml_checks.py` — as covered in the SAML/OIDC lab
- `katas/jwt_checks.py` — id_token claim validation (+ JWKS fetch helper signature)
