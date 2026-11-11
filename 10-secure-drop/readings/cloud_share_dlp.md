# Reading — File / cloud-share DLP

## Learning objectives

1. Explain why **email hold** alone does not cover files shared via cloud links.
2. List controls: link visibility (org / specific users / public), expiry, revoke, download audit.
3. Relate Secure Drop’s expiring link to a minimal share-DLP story.

## Short intro

Outbound email DLP catches messages and attachments on the mail path. People also paste cloud-share URLs into chat or leave “anyone with the link” open. File / cloud-share DLP is about **governing those shares**: who can open them, for how long, and what the audit log shows when someone downloads.

## Videos (verified)

Credited DLP overview talks rotate often — prefer the written links below. Optional: search YouTube for “Data Loss Prevention explained” from IBM Technology / NIST-oriented channels and confirm the title matches before watching.

Prefer written vendor-neutral docs below if a video ID drifts.

## Read these (verified)

1. [OWASP — File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — upload risks adjacent to secure drop.
2. [NIST SP 800-171 / access control concepts](https://csrc.nist.gov/pubs/sp/800/171/r3/final) — skim access-control family vocabulary (optional depth).
3. [Google Workspace — shared drive / link sharing overview](https://support.google.com/a/answer/7587183) — real-world link visibility language (generic literacy).
4. [Microsoft Learn — SharePoint / OneDrive sharing overview](https://learn.microsoft.com/en-us/sharepoint/external-sharing-overview) — external sharing concepts (read for patterns, not product lock-in).
5. [AWS — Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) — mechanism behind many expiring links.

## Self-check

[`../quizzes/cloud_share_dlp.md`](../quizzes/cloud_share_dlp.md)
