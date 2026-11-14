# Answer key — Email threats beyond auth

1. BIMI is a brand indicator tied to DMARC enforcement — it does not inspect attachments or URLs for malice.
2. TLS-RPT (and STS reports) show who fails TLS/policy while `testing`; only after clean reports do you set `enforce` so legitimate senders are not dropped blindly.
3. A path attacker can strip STARTTLS; STS/DANE raise policy so senders refuse cleartext/wrong certs instead of silently downgrading.
4. Attachment sandboxing / content controls — authentication of the domain does not equal safe payload.
5. Cleartext interstitial and public PII logs enable theft and phishing of the rewriter itself; use HTTPS, minimize logs, protect storage.
6. DNSSEC + TLSA operational burden (key rollover, DNSSEC correctness); MTA-STS uses HTTPS policy host many teams already know how to run.
