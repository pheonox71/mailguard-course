# Quiz answer key — cloud share dlp

Use only after attempting the quiz questions.

1. Data Loss Prevention — e.g. “anyone with the link” cloud file still reachable.
2. Visibility limits, expiry, revoke, audit/download logging (any three).
3. Time-limited access without making the object world-readable forever. A raw S3 presigned URL is a bearer link: it stays valid until it expires (console ≤ 12 h; CLI/SDK with IAM-user SigV4 ≤ 7 days; with role/STS credentials it dies when the session ends). You cannot revoke one URL alone — kill early only by revoking signing credentials or denying access by policy. App-level revoke needs indirection (check `revoked_at`, then issue a short-lived presign per download).
4. No — different problem (transfer/share vs domain spoofing).
