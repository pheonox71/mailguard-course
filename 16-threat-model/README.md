# 16 — Threat modeling & lightweight secure SDLC

Before (or while) polishing the capstone: name threats on the MailGuard hold path, tie them to mitigations you already built, and run a short secure Software Development Life Cycle (**SDLC**) self-check.

**No office-hours FAQ** — self-serve readings, worksheet, quiz. AI-generated course materials; the student fills worksheets on the `work` branch.

## What this teaches

- **STRIDE**-lite (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) on a concrete feature
- Optional privacy lens (**LINDDUN**-lite awareness — Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Non-compliance)
- Lightweight secure SDLC / Open Worldwide Application Security Project (**OWASP**) Software Assurance Maturity Model (**SAMM**) *awareness* — not a certification wall

## Workflow

1. [`readings/threat_model_sdlc.md`](./readings/threat_model_sdlc.md)
2. [`quizzes/threat_model_sdlc.md`](./quizzes/threat_model_sdlc.md)
3. [`worksheets/threat_model_sdlc.md`](./worksheets/threat_model_sdlc.md) — produce a one-page threat table for MailGuard hold/release

**Done when:** worksheet table has ≥6 STRIDE rows mapped to MailGuard mitigations or explicit “not yet”; one SAMM/self-assessment paragraph; no attacks on real systems.

## Trade-offs

- Diagram-and-table literacy, not a full threat-modeling tool chain.
- SAMM is self-score awareness only — honesty beats inflated maturity claims.
