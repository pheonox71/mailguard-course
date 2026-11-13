# Quiz — OIDC → AWS

1. **How** does GitHub Actions obtain AWS credentials without storing access keys, and which action/family is commonly used?
2. **Scenario:** JWT `sub` is `repo:acme/app:ref:refs/heads/feat` but the IAM trust allows only `refs/heads/main`. Should `AssumeRoleWithWebIdentity` succeed? **Why?**
3. **Spot the bug / why:** A workflow still exports `AWS_SECRET_ACCESS_KEY` from repository secrets “just in case” beside OIDC.
4. **Why** does Fargate shrink ops surface vs EC2-backed ECS for a small API task?
5. Name the GitHub OIDC issuer host used with AWS, and **why** AWS must trust that issuer specifically.
6. **Why** prefer lowercase service names in naming helpers (DNS/API), not just style preference?
