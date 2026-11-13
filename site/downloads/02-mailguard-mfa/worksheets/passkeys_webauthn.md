# Worksheet — Passkeys / WebAuthn

**Language:** Conceptual worksheet. Any coded demo later should use **Python** (e.g. FastAPI) for the relying-party server — not a random frontend-only stack.

## Short questions

1. What binds a WebAuthn credential to a site so a phishing clone fails?
2. List two TOTP operational pains passkeys aim to reduce (and one new operational pain passkeys introduce).
3. For MailGuard admin, when might you still keep TOTP or recovery codes after enabling passkeys?
4. Draw the registration ceremony in 5 boxes (user, browser, authenticator, RP server, DB).

## Optional demo (stretch)

Using a local demo (e.g. webauthn.io or a minimal FastAPI example you write later), register and assert a credential on `localhost`. Note OS/browser constraints. Do **not** call this “enterprise SSO.”
