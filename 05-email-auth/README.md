# 05 — Email authentication (SPF / DKIM / DMARC)

**Language:** Python 3 + pytest for the `dmarc_policy` kata.

SMTP/TLS literacy plus domain authentication — what outbound hold/DLP cannot solve alone when attackers spoof lookalike mail.

**Learn-by-building:** stub in `katas/`, contract in `tests/`, guided by `readings/` + `assignments/`. Reference in `solutions/`.

## What this teaches

- Simple Mail Transfer Protocol (**SMTP**) hop model vs Transport Layer Security (**TLS**) on a hop
- Sender Policy Framework (**SPF**), DomainKeys Identified Mail (**DKIM**), Domain-based Message Authentication, Reporting and Conformance (**DMARC**)
- Reading `p=` / `rua=` policies and aggregate-report *literacy* (no live third-party probing required)
- Mapping spoofing → Business Email Compromise (**BEC**) risk → why MailGuard holds are complementary

## Workflow

1. [`readings/email_auth.md`](./readings/email_auth.md) → quiz → [`assignments/email_auth.md`](./assignments/email_auth.md)
2. [`assignments/dmarc_policy.md`](./assignments/dmarc_policy.md) → read tests → implement `katas/dmarc_policy.py`
3. `pytest -q`

```bash
cd 05-email-auth
python3 -m venv .venv && source .venv/bin/activate
# Windows PowerShell: py -3 -m venv .venv ; .venv\Scripts\Activate.ps1
# Windows cmd.exe: .venv\Scripts\activate.bat
pip install -r requirements.txt
pytest -q
```

**Done when:** tests green from *your* kata; assignment answers saved under `my-work/assignments/`; you can explain SPF/DKIM/DMARC and `p=none→reject` in an interview without notes.

## Trade-offs / harden next

- Kata parses policy text only — not live DNS or XML aggregate schemas.
- No DKIM signature verification lab (library + key fetch) — add later if targeting mail-sec roles.
