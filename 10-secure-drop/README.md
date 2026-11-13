# 10 — Secure Drop (+ cloud-share DLP literacy)

Secure file transfer lite: upload → object storage → time-limited link + audit. Extended with **file / cloud-share Data Loss Prevention (DLP)** literacy — visibility, revoke, and audit for shared links beyond email hold.

## What this teaches

- Expiring links + audit instead of raw attachments
- Share-link DLP: who can see a link, revoke, watermark/audit events
- How this complements outbound email holds (`07`/`09`) and email auth (`05`)

## Start here

1. [`readings/cloud_share_dlp.md`](./readings/cloud_share_dlp.md)
2. Quiz → worksheet
3. Build upload → store → expiring link + audit (MinIO/LocalStack OK)

**Done when:** demo of expiring link + audit; cloud-share worksheet done; secrets out of git.

## Coding lab

```bash
cd 10-secure-drop
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
