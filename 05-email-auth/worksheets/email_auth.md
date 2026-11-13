# Worksheet — Email authentication

**Language:** Conceptual answers here; the paired kata (`dmarc_policy`) is **Python 3 + pytest**.

**Order:** read [`../readings/email_auth.md`](../readings/email_auth.md) → answer below → implement `katas/dmarc_policy.py` (see that worksheet) → download the quiz PDF when ready.

## Concepts

- **SMTP** moves mail hop-by-hop; **TLS** on a hop encrypts that connection only (STARTTLS between MTAs is opportunistic unless MTA-STS/DANE enforce it).
- **SPF**: DNS list of hosts allowed to send for the **envelope sender (MAIL FROM / Return-Path) or HELO domain**. It does not check the header `From:`. DMARC adds the **alignment** check that ties SPF or DKIM to the visible `From:`. SPF also usually breaks on forwarding, while DKIM survives it.
- **DKIM** = cryptographic signature; public key in DNS.
- **DMARC** = policy + alignment of the visible `From:` domain with SPF/DKIM results + reporting (`rua`). Passes if **at least one** of SPF or DKIM passes **and** aligns.

## Short questions

1. Why can a MailGuard **outbound hold** rule not stop an attacker who spoofs `ceo@partner.example` to your finance team?
2. What does `p=none` buy you before `p=reject`?
3. In one sentence: what is an aggregate (`rua`) report for?
4. Sketch (bullet list) a lab check: given a practice domain’s TXT records, what three queries would you run?

## Sample DMARC aggregate (toy)

Imagine a daily report row: `source_ip=203.0.113.10`, `spf=fail`, `dkim=fail`, `header_from=example.com`, count=400.
- Is this more likely a malicious spoof, a forgotten marketing ESP, or inconclusive? What would you check next?

## Implement

Parse policies in `katas/dmarc_policy.py` (see tests). Optional stretch: look up a *lab* domain you control — never probe third-party domains aggressively.

```bash
cd 05-email-auth && python3 -m venv .venv && source .venv/bin/activate
# Windows PowerShell: py -3 -m venv .venv ; .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```
