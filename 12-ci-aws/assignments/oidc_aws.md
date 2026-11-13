# Assignment — OIDC → AWS

1. Which JWT claim pins a job to one repository, and **why** is that safer than trusting any GitHub token?
2. **Why** are static access keys riskier in Actions secrets than OIDC role assumption?
3. Draft a trust condition for `refs/heads/main` only. Explain **how** a feature-branch job would fail.
4. Name two ECS task definition fields you would pin for a gateway API, and **why** each matters under compromise or drift.
5. **How** do you “rotate” when using OIDC (vs rotating access keys)? What do you change instead of a secret string?
