# Reading — CI + cloud deploy

## Learning objectives

1. Run tests (and optionally build an image) on every PR/push.
2. Prefer federated OIDC roles over long-lived cloud keys in git.
3. Document a deploy path a stranger can follow.

## Short intro

Continuous Integration catches broken rules engines before merge. Cloud deploy should use short-lived credentials — GitHub Actions OIDC to a cloud role is the modern default. This module’s kata validates workflow hygiene helpers (detect forbidden secret patterns; require a test job name).

## Read these (verified)

1. [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
2. [GitHub Actions — OIDC with cloud providers](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
3. [AWS — IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
4. [OWASP — CI/CD Security Top 10](https://owasp.org/www-project-top-10-ci-cd-security-risks/)

## Next step

Continue with the assignment from the downloads on this page.
