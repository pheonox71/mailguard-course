# 03 — OIDC / access policy (+ identity depth)

Happy-path OpenID Connect (**OIDC**) login + protected routes, extended with **SAML** comparison, device-certificate *concepts*, and enterprise **password manager** literacy for non-SSO apps.

## What this teaches

- OIDC login + logout/revocation notes (no inflated SSO claims)
- Security Assertion Markup Language (**SAML**) vs OIDC federation comparison
- Device posture / client certificates as *concepts* (not a PKI build)
- Why non-SSO apps still need a vault / password manager threat model

## Start here

1. [`readings/identity_depth.md`](./readings/identity_depth.md) → quiz → worksheet
2. Pair with `02` passkeys reading and `04` ZTNA

**Done when:** OIDC demo + identity-depth worksheet; honest claims only.

## Coding lab

```bash
cd 03-oidc-access
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Implement `katas/oidc_checks.py` (redirect allow-list, state check, code parse).
