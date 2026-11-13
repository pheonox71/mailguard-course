# Reading — Basic auth JSON client

## Learning objectives

1. Build an HTTP Basic `Authorization` header (RFC 7617).
2. Parse a minimal JSON token response safely.
3. Reason about clock skew when pairing auth with TOTP.

**Why this matters.** Many lab and legacy APIs still gate calls with HTTP Basic. Without understanding how the header is built — and why cleartext HTTP fails — you either leak credentials or silently accept broken token JSON. On the job, pairing Basic (or any password-bearing header) with TOTP and clock-skew checks is a common “authenticated client + MFA” interview and integration pattern.

**How it works.**

1. Form the credential string as `username:password` (one string, colon separator).
2. Base64-encode that **single** string (encoding, not encryption).
3. Send `Authorization: Basic <encoded>` over **TLS only** (RFC 7617).
4. Parse the JSON body as an object and require an explicit `token` field — fail closed if missing or the body is not an object.
5. When the same client also verifies TOTP, compare client/server Unix time against a `max_skew` budget so modest clock drift does not look like an attack.

### Worked example

```text
username:password  →  Base64  →  dXNlcm5hbWU6cGFzc3dvcmQ=

GET /token HTTP/1.1
Host: api.example.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=

HTTP/1.1 200 OK
Content-Type: application/json

{"token":"lab-session-token-example","expires_in":3600}
```

If the body were `{"access":"..."}` without `token`, a fail-closed parser rejects it instead of treating a missing key as success.

### Common misconceptions / what goes wrong

- **“Base64 hides the password.”** Anyone who sees the header can decode it; without TLS the credential is plaintext on the wire.
- **“Any JSON with a string field is a token.”** Accepting the wrong key or a bare string lets broken servers pass; require an object with an explicit `token`.
- **“Client and server clocks must match exactly for TOTP.”** A small `max_skew` budget covers ordinary drift; treating any skew as attack (or ignoring skew entirely) breaks real users or accepts stale codes.

## Read these (verified)

1. [RFC 7617](https://www.rfc-editor.org/rfc/rfc7617)
2. [MDN — Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
3. [httpx Auth](https://www.python-httpx.org/advanced/authentication/) or [requests Auth](https://requests.readthedocs.io/en/latest/user/authentication/)

## Next step

Assignment → `katas/basic_auth_client.py` → quiz.
