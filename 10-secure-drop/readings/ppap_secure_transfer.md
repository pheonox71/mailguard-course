# Reading — Insecure password-ZIP transfer → Secure Drop

## Learning objectives

1. Explain the **global** insecure pattern: password-protected archive in one message, password in another on the **same channel**.
2. Why it fails: same-channel secrecy, blocks malware scanning, abused by malware loaders historically.
3. Prefer portal-style secure transfer: link + **recipient OTP**, expiry, and **revoke-after-missend**.

## Short intro

Some regions nicknamed this pattern “PPAP”; treat it as a **worldwide** anti-pattern, not a culture lesson. Secure Drop-style delivery converts attachments to expiring download URLs with verification and revocation.

## Read these (verified)

1. [IIJ — PPAP report (English)](https://www.iij.ad.jp/en/dev/iir/pdf/iir_vol51_report_EN.pdf) — historical context
2. Module Secure Drop reading + object-storage presigned URL docs for your cloud
3. [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

## Next step

Extend Secure Drop with recipient OTP + revoke → quiz.
