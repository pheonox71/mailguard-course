# Reading — Email threats beyond SPF/DKIM/DMARC

## Learning objectives

1. Place **BIMI**, **MTA-STS**, **TLS-RPT**, and **DANE** next to SPF/DKIM/DMARC without confusing logos for authentication.
2. Analyze phishing **headers** and attachment risk at a literacy level (sandboxing concepts).
3. Contrast **S/MIME / PGP** end-to-end crypto with **time-of-click** URL rewriting.

**Why this matters.** DMARC can pass and the message can still be hostile: malicious attachments, credential links, or downgraded SMTP TLS. Without transport policy (MTA-STS/DANE), reporting (TLS-RPT), and human-layer controls, “we have DMARC” becomes a false sense of safety. On the job, email-security reviews ask what you do *after* authentication succeeds.

**How it works.**

1. **SPF/DKIM/DMARC** answer “is this domain authorized for this message path?”
2. **BIMI** can show a logo when DMARC is enforced — brand indicator, not a crypto proof by itself.
3. **MTA-STS** publishes a policy so sending MTAs prefer STS-validated TLS to your MX; **TLS-RPT** receives failure reports.
4. **DANE** (DNSSEC + TLSA) binds MX certs in DNS — powerful where DNSSEC is real; operationally heavier.
5. **Header analysis** (Received, Authentication-Results, URL paths) supports phishing triage without attacking third parties.
6. **Attachment sandboxing** detonates or statically inspects files off the user desktop.
7. **S/MIME/PGP** encrypt/sign content end-to-end; **time-of-click** rewriting proxies links at click time (privacy/availability trade-offs).

```text
Auth (SPF/DKIM/DMARC) → transport policy (MTA-STS/DANE) → content controls
                      → human triage (headers) → sandbox / rewrite / E2E crypto
```

### Worked example

MTA-STS policy host sketch (conceptual):

```text
# DNS: _mta-sts.example.com TXT "v=STSv1; id=20261114"
# HTTPS: https://mta-sts.example.com/.well-known/mta-sts.txt
version: STSv1
mode: enforce
mx: mail.example.com
max_age: 86400
```

Why reports (`rua` for DMARC, TLS-RPT for STS) before `enforce`: you learn which senders break before you drop them.

### Common misconceptions / what goes wrong

- **“BIMI proves the message is safe.”** BIMI is a brand indicator tied to DMARC enforcement — not malware scanning.
- **“TLS on port 25 is enough.”** Opportunistic TLS can be stripped; MTA-STS/DANE raise the bar for SMTP hop security.
- **“Sandboxing means zero risk.”** Evasion and time bombs exist; combine with type blocks and user reporting.
- **“URL rewriting is free.”** It breaks some links, centralizes click metadata, and must not become a phishing page itself.

## Videos (verified)

1. **[CertMike Explains DMARC, DKIM and SPF](https://www.youtube.com/watch?v=Q8NUW3CZRvw)** — Mike Chapple  
   Why it helps: refreshes Module 05 so the “beyond auth” controls have a base.

## Read these (verified)

1. [MTA-STS (RFC 8461)](https://www.rfc-editor.org/rfc/rfc8461)
2. [TLS-RPT (RFC 8460)](https://www.rfc-editor.org/rfc/rfc8460)
3. [BIMI Group — overview](https://bimigroup.org/)
4. [DANE (RFC 6698)](https://www.rfc-editor.org/rfc/rfc6698)
5. [S/MIME (RFC 8551)](https://www.rfc-editor.org/rfc/rfc8551)

## Lab idea — MTA-STS / TLS-RPT

1. Publish a **testing** STS policy (`mode: testing`) for a lab domain you control.
2. Configure TLS-RPT so failure reports have somewhere to go.
3. Move to `enforce` only after reports look clean.
4. Document who owns DNS + HTTPS for `mta-sts.` — split ownership is a common outage.

## Next step

Assignment + required quiz. Stay vendor-neutral: mechanisms over product names.
