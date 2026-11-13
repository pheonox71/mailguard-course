# Assignment — SAML + OIDC deepen

1. Why list checks that stop assertion replay (time window, InResponseTo, audience/ACS, one-time IDs) — what still fails if you only check the signature?
2. Why is unsigned assertion acceptance dangerous even “on a private network”?
3. Generate a PKCE verifier and S256 challenge (note values). Why must the verifier be high-entropy and not reused?
4. SP-initiated vs IdP-initiated: who creates the request ID, and why does InResponseTo matter more on one path?
5. Sketch Keycloak realm + client settings for a confidential web app with a PKCE option — why lab IdPs still need exact redirect URIs.
