# Answer key — OIDC → AWS

1. Request an OIDC ID token from GitHub, then `AssumeRoleWithWebIdentity` (often via `aws-actions/configure-aws-credentials` with `role-to-assume`). No long-lived access key is stored.
2. No — the trust condition on `sub` / ref does not match, so STS rejects the assume.
3. Reintroduces long-lived keys and defeats OIDC hardening; a leaked secret still grants cloud access outside the workflow identity.
4. No EC2 capacity management for tasks (serverless containers) — fewer OS/patch/scaling knobs for the compute layer of the task.
5. `token.actions.githubusercontent.com` — AWS validates tokens against that issuer’s JWKS; trusting the wrong issuer would accept forged identities.
6. Stable DNS/API naming; avoid case-fold surprises across load balancers, registries, and clients.
