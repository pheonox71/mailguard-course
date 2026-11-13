# Assignment — Passkeys / WebAuthn

**Language:** Conceptual assignment. Any coded demo later should use **Python** (e.g. FastAPI) for the relying-party server — not a random frontend-only stack.

## Short questions

1. Why does binding a WebAuthn credential to the relying-party domain defeat a phishing clone that TOTP cannot stop?
2. Why might passkeys reduce two TOTP operational pains — and what new operational pain do they introduce (recovery / device loss)?
3. For MailGuard admin, when might you still keep TOTP or recovery codes after enabling passkeys — what fails if you remove every fallback overnight?
4. Draw the registration ceremony in 5 boxes (user, browser, authenticator, RP server, DB) and annotate **why** the challenge must be server-generated.

## Optional demo (stretch)

Using a local demo (e.g. webauthn.io or a minimal FastAPI example you write later), register and assert a credential on `localhost`. Note OS/browser constraints. Why `localhost` is acceptable for a lab but not a substitute for RP ID design in production. Do **not** call this “enterprise SSO.”
