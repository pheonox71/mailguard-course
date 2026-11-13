# Answer key — SAML + OIDC

1. Short time windows, InResponseTo (SP-initiated), one-time assertion IDs / replay cache, audience/recipient checks.
2. Reject with skew=60 (now >= not_on_or_after + skew).
3. Open redirect / assertion injection to sibling paths.
4. SHA-256, then base64url without padding.
5. Exact redirect URI matching / issuer validation / PKCE.
6. Unsigned assertions can be forged by anyone who can POST to the ACS.
