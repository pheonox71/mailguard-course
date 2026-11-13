# Answer key — SAML + OIDC

1. Assertion replay — steal a valid response and POST it again later or to another SP context.
2. Reject with skew=60 (now >= not_on_or_after + skew). Skew tolerates modest clock drift without accepting long-lived assertions forever.
3. Open redirect / assertion accepted for sibling paths — attacker points ACS at a path they control under the same prefix.
4. Stops an eavesdropper who sees the authorize redirect from redeeming a stolen code without the verifier; S256 avoids sending the verifier until the token request.
5. Exact redirect URI matching / issuer validation / PKCE — prevents authorization-code theft and IdP mix-up.
6. Unsigned assertions can be forged by anyone who can POST to the ACS.
