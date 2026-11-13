# Reading — File / cloud-share DLP

## Learning objectives

1. Explain why **email hold** alone does not cover files shared via cloud links.
2. List controls: link visibility (org / specific users / public), expiry, app-level revoke, download audit. Note: a raw S3 **presigned URL** cannot be revoked individually — it stays valid until expiry (or until signing credentials / object policy are revoked). Real share-DLP revoke needs app-level indirection.
3. Relate Secure Drop’s expiring link to a minimal share-DLP story.

**Why this matters.** Outbound email hold catches messages on the mail path; it does nothing when someone pastes an “anyone with the link” URL into chat. Without visibility limits, expiry, revoke, and download audit, missent shares stay reachable until someone notices. Presigned URLs feel like revoke-able magic — until you learn a raw S3 presign is a **bearer** link that cannot be killed one-by-one. That trade-off is why production share-DLP puts an app check in front of short-lived presigns.

**How it works.** A share object records owner, visibility, `expires_at`, optional `revoked_at`, and audit events. Download flow: client hits **your** app → check not expired/revoked + authorized → issue a **short-lived** storage URL (or stream) → log who/when/object id (not file bytes). Email hold and share-DLP are complementary: hold is about SMTP content; share-DLP is about object links after the fact.

```
Upload → ShareLink (visibility, expiry, revoked_at)
Download → app authz check → short-lived fetch → audit metadata
Missend → set revoked_at → further downloads fail
```

**On the job.** Cloud Drive/SharePoint/S3-backed secure transfer shows up in every email and collaboration security review. Explaining why email DLP ≠ link DLP — and why revoke needs indirection — is vendor-neutral literacy for SaaS and cloud security roles.

## Short intro

Outbound email DLP catches messages and attachments on the mail path. People also paste cloud-share URLs into chat or leave “anyone with the link” open. File / cloud-share DLP is about **governing those shares**: who can open them, for how long, and what the audit log shows when someone downloads.

## Videos (verified)

Credited DLP overview talks rotate often — prefer the written links below. Optional: search YouTube for “Data Loss Prevention explained” from IBM Technology / NIST-oriented channels and confirm the title matches before watching.

Prefer written vendor-neutral docs below if a video ID drifts.

## Read these (verified)

1. [OWASP — File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — upload risks adjacent to secure drop.
2. [NIST SP 800-171 / access control concepts](https://csrc.nist.gov/pubs/sp/800/171/r3/final) — skim access-control family vocabulary (optional depth).
3. [Google Workspace — Manage external sharing for your organization](https://support.google.com/a/answer/60781) — org-level Drive/Docs link sharing controls (generic literacy).
4. [Microsoft Learn — SharePoint / OneDrive sharing overview](https://learn.microsoft.com/en-us/sharepoint/external-sharing-overview) — external sharing concepts (read for patterns, not product lock-in).
5. [AWS — Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) — mechanism behind many expiring links (bearer URLs; max lifetime and revoke limits).

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment.
