# Quiz answer key — cloud share dlp

Use only after attempting the quiz questions.

1. Hold only sees the mail path; a cloud URL shared in chat/email as a *link* grants access via storage/authz — no hold state applies to that object.
2. Visibility limits (who can open) · expiry (time box) · revoke (kill after missend) · audit/download logging (forensics) — any three with matching failure mode.
3. Time-limited access without making the object world-readable forever. A raw S3 presigned URL is a **reusable bearer** until expiry (or until signing credentials / object policy are revoked — a blunt kill). You cannot revoke one URL alone — app-level revoke needs indirection (check `revoked_at`, then issue a short-lived presign per redeem).
4. No — Secure Drop/share-DLP is transfer/share control; DMARC is domain spoofing / From alignment for mail authentication.
5. Revoke at the indirection layer (`revoked_at`) so new downloads fail even if the URL string is known — download must hit the app check *before* issuing storage access.
6. Sensitive content sprawl; log metadata (who/when/object id) instead of payloads.
7. Landing must not mint/consume the one-time download (prefetch/scanners); redemption is the audited, capped step. Send `Referrer-Policy: no-referrer` so tokens in the URL do not leak via `Referer`.
