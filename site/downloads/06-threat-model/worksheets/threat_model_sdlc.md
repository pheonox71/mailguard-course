# Worksheet — Threat model the MailGuard hold path

**Order:** reading → this worksheet (save finished answers under `my-work/worksheets/`) → self-check quiz PDF when ready.

## Part A — Scope (4 bullets)

1. What asset are you protecting? (e.g. held message content, rule config, operator session)
2. Who are the actors? (sender, external attacker, operator, compromised admin, insider)
3. Trust boundaries? (browser ↔ API, API ↔ DB, worker ↔ queue, object storage)
4. Out of scope for this pass?

## Part B — STRIDE table

Copy and fill (≥6 rows):

| Threat (STRIDE letter) | Abuse story | Impact | Mitigation you have / gap |
|------------------------|-------------|--------|---------------------------|
| S | | | |
| T | | | |
| R | | | |
| I | | | |
| D | | | |
| E | | | |

## Part C — Privacy (LINDDUN-lite)

One paragraph: who can read held bodies and audit logs? Retention? Redaction?

## Part D — SAMM self-check (honest)

Pick **one** OWASP SAMM practice stream. Score yourself 0–1 informally and write the *next* concrete improvement (e.g. “add CI dependency scan” — without claiming enterprise maturity).

## Capstone link

Attach this page (or a PDF export) when you claim security notes / threat literacy on the rubric.
