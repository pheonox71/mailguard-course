# Quiz answer key — CI + AWS

Use only after attempting the quiz questions.

1. Rules regressions and dependency breaks otherwise reach `main`/demos unnoticed; CI gives a repeatable gate on every change.
2. Continuous Integration; OpenID Connect federation for short-lived cloud creds. OIDC exchanges a workflow identity token for temporary cloud credentials; static keys sit in secrets/history until rotated and leak more easily.
3. e.g. deploy only to one account/region/service; no `IAM:*`; no `s3:*` on all buckets — compromise of CI cannot re-admin the whole cloud account.
4. Checkout → setup language → install deps → pytest/lint (then optional image). Tests must fail the PR before anything is published or deployed.
5. Secrets appear in logs for anyone with log access; redaction misses forks, artifacts, and already-exfiltrated lines — rotate and stop echoing secrets.
6. Fork PRs could abuse write permissions (supply-chain / token theft). Prefer least `permissions:` (e.g. `contents: read`) and avoid secrets on untrusted fork workflows.
