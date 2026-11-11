# 15 — Email authentication (SPF / DKIM / DMARC)

SMTP/TLS literacy plus domain authentication — what outbound hold/DLP cannot solve alone when attackers spoof lookalike mail.

**Learn-by-building:** stub in `katas/`, contract in `tests/`, guided by `readings/` + `worksheets/`. Reference in `solutions/`.

## What this teaches

- Simple Mail Transfer Protocol (**SMTP**) hop model vs Transport Layer Security (**TLS**) on a hop
- Sender Policy Framework (**SPF**), DomainKeys Identified Mail (**DKIM**), Domain-based Message Authentication, Reporting and Conformance (**DMARC**)
- Reading `p=` / `rua=` policies and aggregate-report *literacy* (no live third-party probing required)
- Mapping spoofing → Business Email Compromise (**BEC**) risk → why MailGuard holds are complementary

## Workflow

1. [`readings/email_auth.md`](./readings/email_auth.md) → quiz → [`worksheets/email_auth.md`](./worksheets/email_auth.md)
2. [`worksheets/dmarc_policy.md`](./worksheets/dmarc_policy.md) → read tests → implement `katas/dmarc_policy.py`
3. `pytest -q`

```bash
cd 15-email-auth
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

**Done when:** tests green from *your* kata; worksheet answers recorded on `work`; you can explain SPF/DKIM/DMARC and `p=none→reject` in an interview without notes.

## Trade-offs / harden next

- Kata parses policy text only — not live DNS or XML aggregate schemas.
- No DKIM signature verification lab (library + key fetch) — add later if targeting mail-sec roles.
