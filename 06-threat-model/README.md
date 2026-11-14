# 06 — Threat modeling & lightweight secure SDLC

name threats on the MailGuard hold path, tie them to mitigations you already built, and run a short secure Software Development Life Cycle (**SDLC**) self-check.

**No office-hours FAQ** — self-serve readings, assignment, quiz. The student saves finished work under [`../my-work/`](../my-work/).

## What this teaches

- **STRIDE**-lite (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) on a concrete feature
- Optional privacy lens (**LINDDUN**-lite awareness — Linking, Identifying, Non-repudiation, Detecting, Data disclosure, Unawareness & unintervenability, Non-compliance)
- Lightweight secure SDLC evidence via **NIST SSDF** and **OWASP ASVS**, with optional Open Worldwide Application Security Project (**OWASP**) Software Assurance Maturity Model (**SAMM**) *awareness* — not a certification wall

## Workflow

1. [`readings/threat_model_sdlc.md`](./readings/threat_model_sdlc.md)
2. [`quizzes/threat_model_sdlc.md`](./quizzes/threat_model_sdlc.md)
3. [`assignments/threat_model_sdlc.md`](./assignments/threat_model_sdlc.md) — produce a one-page threat table for MailGuard hold/release

**Done when:** assignment table has ≥6 STRIDE rows mapped to MailGuard mitigations or explicit “not yet”; one SSDF/ASVS evidence mapping (SAMM optional); no attacks on real systems.

## Trade-offs

- Diagram-and-table literacy, not a full threat-modeling tool chain.
- SSDF/ASVS are evidence maps; SAMM is optional self-score awareness — honesty beats inflated maturity claims.
