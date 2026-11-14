# Reading — File / cloud-share DLP

## Learning objectives

1. Explain why **email hold** alone does not cover files shared via cloud links.
2. List controls: link visibility (org / specific users / public), expiry, app-level revoke, download audit. Note: a raw S3 **presigned URL** cannot be revoked individually — it stays valid until expiry (or until signing credentials / object policy are revoked). Real share-DLP revoke needs app-level indirection.
3. Relate Secure Drop’s expiring link to a minimal share-DLP story.

**Why this matters.** Outbound email hold catches messages on the mail path; it does nothing when someone pastes an “anyone with the link” URL into chat. Without visibility limits, expiry, revoke, and download audit, missent shares stay reachable until someone notices. Presigned URLs feel like revoke-able magic — until you learn a raw S3 presign is a **bearer** link that cannot be killed one-by-one. That trade-off is why production share-DLP puts an app check in front of short-lived presigns.

**How it works.**

1. Upload creates a **share object**: owner, visibility (org / specific users / public), `expires_at`, optional `revoked_at`, and audit hooks.
2. Recipient opens a **landing page** (non-consuming): show metadata / OTP challenge **without** minting storage credentials yet. Send `Referrer-Policy: no-referrer` on landing and download responses so the share token / presign query string does not leak via `Referer` to third-party assets.
3. App checks: not expired, not revoked, caller authorized for that visibility.
4. **Redemption** is a separate step: after OTP (if required), the app issues a **short-lived** storage fetch (presign or stream) and log who/when/object id — **not** file bytes ([presigned URL docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)). Treat redemption as one-shot (or tightly capped) so “open landing” ≠ “consume download.”
5. Bound **presigned URL reuse** and **signing-credential lifetime**: a raw S3 presign is reusable by anyone who has the URL until it expires; keep TTL short (minutes). Revoking the *IAM user/role keys* or bucket policy that signed the URL invalidates outstanding presigns — but that is a blunt instrument. Prefer app indirection + short TTL over week-long bearer links.
6. On missend, set `revoked_at` (or equivalent) so further landing/redeem checks fail even if someone copied an old link.
7. Email hold and share-DLP are complementary: hold is about SMTP content; share-DLP is about object links after the fact.

```
Upload → ShareLink (visibility, expiry, revoked_at)
Landing (non-consuming, Referrer-Policy: no-referrer) → OTP?
Redeem → app authz → short-lived presign (minutes) → audit metadata
Missend → set revoked_at → landing + redeem fail
```

### Worked example

Minimal share record + revoke effect:

```json
{
  "share_id": "sh_9f3a",
  "object_key": "drops/q3-forecast.pdf",
  "visibility": "specific_users",
  "allowed": ["alex@example.com"],
  "expires_at": "2026-11-20T00:00:00Z",
  "revoked_at": null
}
```

| Event | App check | Result |
|-------|-----------|--------|
| Alex opens landing before expiry | ok (non-consuming) | OTP form; **no** presign yet; `Referrer-Policy: no-referrer` |
| Alex redeems after OTP | ok | short-lived URL (minutes) + audit row; further redeems capped |
| Public guess of URL | visibility fail | 403 |
| After operator sets `revoked_at` | revoked | 403 even with copied link |
| Raw S3 presign issued for 7 days, no app front | n/a | **reusable bearer** until expiry; **cannot** revoke that URL alone (unless signing credentials / object policy change) |

**On the job.** Cloud Drive/SharePoint/S3-backed secure transfer shows up in every email and collaboration security review. Explaining why email DLP ≠ link DLP — and why revoke needs indirection — is vendor-neutral literacy for SaaS and cloud security roles.

## Short intro

Outbound email DLP catches messages and attachments on the mail path. People also paste cloud-share URLs into chat or leave “anyone with the link” open. File / cloud-share DLP is about **governing those shares**: who can open them, for how long, and what the audit log shows when someone downloads. Note again: a raw object-storage **presigned URL** is a bearer token until expiry (or until signing credentials / object policy change) — real revoke needs an app-level check in front of short-lived fetches.

### Common misconceptions / what goes wrong

- **“Email hold covers Drive links.”** Hold never sees a URL pasted in chat; share visibility/expiry/revoke are a different control plane.
- **“Presigned URL = revocable share.”** Individual S3-style presigns cannot be killed one-by-one; they are **reusable** until expiry (or until signing credentials / object policy are revoked). Use app indirection + short TTL.
- **“Opening the link consumes the download.”** Landing should be non-consuming; redemption is a separate, audited step.
- **“Default Referrer-Policy is fine.”** Landing/download URLs often carry tokens in the path or query; without `Referrer-Policy: no-referrer`, third-party scripts/images can leak them via `Referer`.
- **“Audit should store the file bytes.”** Log metadata (who/when/object id); storing content duplicates sensitive data and expands breach scope.
- **“Public link with a long random path is secret enough.”** Guessing is hard; forwarding is easy — treat “anyone with the link” as public.

## Videos (verified)

Credited DLP overview talks rotate often — prefer the written links below. Optional: search YouTube for “Data Loss Prevention explained” from IBM Technology / NIST-oriented channels and confirm the title matches before watching.

Prefer written vendor-neutral docs below if a video ID drifts.

## Read these (verified)

1. [OWASP — File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — upload risks adjacent to secure drop.
2. [NIST SP 800-171 / access control concepts](https://csrc.nist.gov/pubs/sp/800/171/r3/final) — skim access-control family vocabulary (optional depth).
3. [Google Workspace — Manage external sharing for your organization](https://support.google.com/a/answer/60781) — org-level Drive/Docs link sharing controls (generic literacy).
4. [Microsoft Learn — SharePoint / OneDrive sharing overview](https://learn.microsoft.com/en-us/sharepoint/external-sharing-overview) — external sharing concepts (read for patterns, not product lock-in).
5. [AWS — Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) — bearer URLs; reuse until expiry; lifetime limited by the signing credentials’ permissions and clock; prefer short TTL + app front.
6. [MDN — Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) — use `no-referrer` on share landing/download responses.

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment.
