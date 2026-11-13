# Reading — Basic auth JSON client

## Learning objectives

1. Build an HTTP Basic `Authorization` header (RFC 7617).
2. Parse a minimal JSON token response safely.
3. Reason about clock skew when pairing auth with TOTP.

**Why this matters.** Many lab and legacy APIs still gate calls with HTTP Basic. Without understanding how the header is built — and why cleartext HTTP fails — you either leak credentials or silently accept broken token JSON. On the job, pairing Basic (or any password-bearing header) with TOTP and clock-skew checks is a common “authenticated client + MFA” interview and integration pattern.

**How it works.** Form the credential string as `username:password`, Base64-encode that **single** string, and send `Authorization: Basic <encoded>` (RFC 7617). Over TLS only — Base64 is encoding, not encryption. Parse the JSON body as an object and require an explicit `token` (fail closed if missing). When the same client also verifies TOTP, compare client/server Unix time against a `max_skew` budget so modest clock drift does not look like an attack.

## Read these (verified)

1. [RFC 7617](https://www.rfc-editor.org/rfc/rfc7617)
2. [MDN — Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
3. [httpx Auth](https://www.python-httpx.org/advanced/authentication/) or [requests Auth](https://requests.readthedocs.io/en/latest/user/authentication/)

## Next step

Assignment → `katas/basic_auth_client.py` → quiz.
