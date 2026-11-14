# Reading — Insecure password-ZIP transfer → Secure Drop

## Learning objectives

1. Explain the **global** insecure pattern: password-protected archive in one message, password in another on the **same channel**.
2. Why it fails: same-channel secrecy, blocks malware scanning, abused by malware loaders historically.
3. Prefer portal-style secure transfer: link + **recipient OTP**, expiry, and **revoke-after-missend**.

**Why this matters.** Sending a passworded ZIP and the password on the **same email channel** looks like encryption theater: anyone who compromised the mailbox gets both. Gateways cannot malware-scan encrypted archives, which is why loaders historically abused the pattern. Some regions nicknamed it “PPAP”; treat it as a **worldwide** anti-pattern, not a culture lesson. Secure Drop-style delivery exists because expiry, recipient proof, and **revoke-after-missend** beat hoping the wrong recipient deletes a ZIP.

**How it works.**

1. Sender **uploads** the file to object storage (not as a passworded ZIP in mail).
2. Service creates a share with **expiry** and a **hashed** recipient OTP (never store the OTP in plaintext).
3. Recipient opens a **landing page** (non-consuming) and proves possession of the OTP; compare with a constant-time helper such as `hmac.compare_digest`. Serve landing with `Referrer-Policy: no-referrer`.
4. **Redeem** separately: on success, issue a **short-lived** download (see [presigned URL limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)) and write an audit event. Cap reuse — a week-long presign is a reusable bearer; keep post-OTP fetches to minutes, and remember signing-credential revocation is the blunt way to kill outstanding URLs.
5. On missend, operator **revokes** immediately so further landing/redeem fail even if the URL was copied.
6. Prefer this over same-channel ZIP+password; S/MIME or portal encryption may fit when you need end-to-end crypto with different threat models. Upload risks still apply — skim [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

```
Sender uploads → Secure Drop link
Landing (non-consuming, Referrer-Policy: no-referrer) → OTP challenge
Redeem → short-lived download → audit
Missend → revoke → landing + redeem fail
```

### Worked example

Share + OTP verify (conceptual):

```json
{
  "share_id": "sd_77",
  "object_key": "secure/contract.pdf",
  "expires_at": "2026-11-14T18:00:00Z",
  "otp_hash": "sha256$…",
  "revoked_at": null
}
```

| Step | What happens |
|------|----------------|
| Email A | “Your file is ready: https://drop.example/sd_77” (no password in this channel ideal; OTP out-of-band or separate channel) |
| Landing GET | Non-consuming; headers include `Referrer-Policy: no-referrer` |
| Recipient posts OTP | `compare_digest(hash(input), otp_hash)` → true |
| Redeem | short-lived URL (minutes); audit `{share_id, actor, at}`; second redeem capped/denied |
| Missend | `revoked_at = now` → next landing/OTP/redeem → 403 |

Same-channel ZIP+password failure mode: mailbox compromise yields **both** ciphertext and key; scanners see opaque blobs.

**On the job.** Secure file transfer and email DLP reviews always ask: can you revoke after missend, and can scanners see content? Answering with portal+OTP+revoke (and knowing ZIP+password fails) is core email/cloud security literacy.

## Short intro

Some regions nicknamed this pattern “PPAP”; treat it as a **worldwide** anti-pattern, not a culture lesson. The insecure pattern is a password-protected archive in one message and the password in another on the **same channel** — same-channel secrecy, blocked malware scanning, and historical abuse by malware loaders. Secure Drop-style delivery converts attachments to expiring download URLs with recipient verification and revocation.

### Common misconceptions / what goes wrong

- **“Passworded ZIP is encrypted email.”** Same-channel password delivery collapses the secrecy; it also blinds malware scanners.
- **“Store the OTP in the database in plaintext for support.”** Support can reset; a breach then reprints every code — hash and compare constant-time.
- **“Revoke is optional if expiry is short.”** Missend to the wrong person needs immediate kill; waiting for TTL is still a window of exposure.
- **“Long-lived presign to the object is fine after OTP.”** OTP then a week-long reusable bearer undoes the control; keep post-auth fetches short-lived and remember credential-lifetime limits.
- **“Landing and download are the same GET.”** Separating non-consuming landing from redemption prevents prefetch/bots/email scanners from burning one-time links.
- **“Referrer leakage is only an XSS problem.”** Tokens in URLs leak to third-party hosts via `Referer` unless you set `Referrer-Policy: no-referrer` on landing/download responses.

## Read these (verified)

1. [IIJ — PPAP report (English)](https://www.iij.ad.jp/en/dev/iir/pdf/iir_vol51_report_EN.pdf) — historical context
2. Module Secure Drop reading + object-storage [presigned URL docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) for mechanism limits (reuse + credential lifetime)
3. [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
4. [MDN — Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) — `no-referrer` on share responses

## Next step

Continue with the assignment (extend Secure Drop with recipient OTP + revoke). The quiz is required after you attempt the assignment.
