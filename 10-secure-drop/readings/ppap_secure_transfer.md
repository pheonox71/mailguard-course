# Reading — Insecure password-ZIP transfer → Secure Drop

## Learning objectives

1. Explain the **global** insecure pattern: password-protected archive in one message, password in another on the **same channel**.
2. Why it fails: same-channel secrecy, blocks malware scanning, abused by malware loaders historically.
3. Prefer portal-style secure transfer: link + **recipient OTP**, expiry, and **revoke-after-missend**.

**Why this matters.** Sending a passworded ZIP and the password on the **same email channel** looks like encryption theater: anyone who compromised the mailbox gets both. Gateways cannot malware-scan encrypted archives, which is why loaders historically abused the pattern. Some regions nicknamed it “PPAP”; treat it as a **worldwide** anti-pattern, not a culture lesson. Secure Drop-style delivery exists because expiry, recipient proof, and **revoke-after-missend** beat hoping the wrong recipient deletes a ZIP.

**How it works.** Upload the file to object storage; create a share with expiry and a **hashed** recipient OTP (compare with a constant-time helper such as `hmac.compare_digest`). Recipient proves possession of OTP → short-lived download. On missend, operator **revokes** immediately so the link fails even if the URL was copied. Prefer this over same-channel ZIP+password; S/MIME or portal encryption may fit when you need end-to-end crypto with different threat models.

```
Sender uploads → Secure Drop link + OTP challenge
Recipient OTP OK → download → audit
Missend → revoke → further downloads fail
```

**On the job.** Secure file transfer and email DLP reviews always ask: can you revoke after missend, and can scanners see content? Answering with portal+OTP+revoke (and knowing ZIP+password fails) is core email/cloud security literacy.

## Short intro

Some regions nicknamed this pattern “PPAP”; treat it as a **worldwide** anti-pattern, not a culture lesson. Secure Drop-style delivery converts attachments to expiring download URLs with verification and revocation.

## Read these (verified)

1. [IIJ — PPAP report (English)](https://www.iij.ad.jp/en/dev/iir/pdf/iir_vol51_report_EN.pdf) — historical context
2. Module Secure Drop reading + object-storage [presigned URL docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) for mechanism limits
3. [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

## Next step

Continue with the assignment (extend Secure Drop with recipient OTP + revoke). The quiz is required after you attempt the assignment.
