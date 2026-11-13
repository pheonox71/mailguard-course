# 12 — CI + AWS

**Language:** GitHub Actions YAML + cloud deploy notes. Est. 8-10h.

PR/push CI for tests/lint/image, plus a documented cloud deploy path with **no secrets in git**. Prefer OIDC to cloud roles over long-lived keys.

## Workflow

1. [`readings/ci_aws.md`](./readings/ci_aws.md)
2. Worksheet → fill `katas/workflow_checks.py` tests
3. Optional: add a real workflow under `.github/workflows/` for a service you own
4. Required quiz

**Done when:** CI green for at least one core service; one documented cloud deploy; no secrets in git.

## Trade-offs / harden next

- Sample workflow is educational — pin actions by SHA in production.
- Deploy identity must be least-privilege; document what it cannot do.
