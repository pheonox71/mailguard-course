# Quiz answer key — CI + AWS

Use only after attempting the quiz questions.

1. Continuous Integration; OpenID Connect federation for short-lived cloud creds.
2. Keys leak via repo history/forks/logs and are hard to rotate; prefer OIDC.
3. e.g. deploy only to one account/region/service; no IAM:* ; no s3:* on all buckets.
4. At least unit tests (pytest); ideally lint too.
5. Secrets in logs; anyone with log access gets the key.
6. Fork PRs could abuse write permissions (supply-chain / token theft).
