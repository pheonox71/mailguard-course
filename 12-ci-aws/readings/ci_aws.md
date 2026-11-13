# Reading — CI + cloud deploy

## Learning objectives

1. Run tests (and optionally build an image) on every PR/push.
2. Prefer federated OIDC roles over long-lived cloud keys in git.
3. Document a deploy path a stranger can follow.

**Why this matters.** Without Continuous Integration (**CI**), broken hold/allow rules and dependency regressions land on `main` and only surface in a demo or production. Long-lived cloud access keys in git (or even in Actions secrets) are a classic incident source: history, forks, and logs leak them, and rotation is slow. On the job, email and identity SaaS teams treat PR CI plus short-lived deploy credentials as table stakes — not optional polish.

**How it works.** A workflow YAML under `.github/workflows/` declares **when** to run (`on: push` / `pull_request`), **jobs** on runners, and **steps** (checkout → language setup → install → test). Optionally a later job builds a container image. Deploy (if any) should exchange an OpenID Connect (**OIDC**) token for a cloud role instead of storing `AWS_ACCESS_KEY_ID` / secret keys. The kata checks workflow hygiene: forbidden secret-like patterns and a required test job name.

```text
PR/push → runner checkout → install deps → pytest/lint
                ↓ (optional)
         OIDC assume-role → push image / update service
```

## Short intro

Continuous Integration catches broken rules engines before merge. Cloud deploy should use short-lived credentials — GitHub Actions OIDC to a cloud role is the modern default. This module’s kata validates workflow hygiene helpers (detect forbidden secret patterns; require a test job name).

## Mechanism sketch (annotated)

Copy ideas from [`../starter/ci-sample.yml`](../starter/ci-sample.yml) into a workflow you own — never commit live secrets.

```yaml
# Why path filters: skip unrelated modules so CI stays fast and cheap
on:
  pull_request:
    paths: ["07-mailguard-api/**"]
jobs:
  unit-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4   # Why: runner starts empty; need the PR tree
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"    # Why: match the course Python pin
      - run: pip install -r requirements.txt  # Why: reproducible deps before tests
      - run: pytest -q              # Why: contract must fail on stubs / broken rules
```

Prefer pinning third-party Actions by commit SHA in production (supply-chain hardening) — see OWASP CI/CD Security Top 10.

## Read these (verified)

1. [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
2. [GitHub Actions — OIDC with cloud providers](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
3. [AWS — IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
4. [OWASP — CI/CD Security Top 10](https://owasp.org/www-project-top-10-ci-cd-security-risks/)

## On the job

Identity and mail-security products ship often. Reviewers ask: “Did CI run the real tests?” and “Can this deploy role only touch the intended account/service?” Document the deploy path so on-call can replay it without tribal knowledge.

## Next step

Continue with the assignment from the downloads on this page.
