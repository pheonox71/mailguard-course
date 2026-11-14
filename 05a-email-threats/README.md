# 05a — Email threats beyond SPF/DKIM/DMARC

Vendor-neutral literacy for threats and controls that sit **beside** authentication: BIMI, MTA-STS/TLS-RPT, DANE, phishing-header analysis, attachment sandboxing, S/MIME/PGP, and time-of-click URL rewriting.

**Language / tooling:** Conceptual + light Python helpers. Est. 8-10h.

## What this teaches

- Place BIMI, MTA-STS, TLS-RPT, and DANE relative to SPF/DKIM/DMARC
- Analyze phishing headers without running attacks on real mailboxes
- Compare S/MIME/PGP and time-of-click rewriting trade-offs

## Start here

1. [`readings/email_threats.md`](./readings/email_threats.md)
2. Assignment → required quiz
3. Optional `katas/header_signals.py` if present

**Done when:** assignment + quiz done; you can explain each control’s **why** without naming a single vendor SKU.
