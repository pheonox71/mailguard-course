# Reading — Incident response & detection

## Learning objectives

1. Apply **NIST SP 800-61r3** lifecycle language to MailGuard incidents.
2. Triage identity alerts (e.g. impossible travel) at a conceptual level.
3. Write a **blameless English postmortem** (impact, timeline, actions) — no secondary-language summary line required.

**Why this matters.** Hold-queue privacy incidents, missend+revoke events, and admin “impossible travel” alerts do not wait for a perfect runbook. Without a shared lifecycle vocabulary, teams skip preparation, thrash during containment, and write blame-heavy writeups that do not prevent recurrence. On the job, email and identity security teams are expected to triage signals quickly, contain access, and document impact in clear English for legal/privacy partners.

**How it works.** National Institute of Standards and Technology (**NIST**) SP 800-61r3 frames incident response as a lifecycle (preparation → detection/analysis → containment/eradication/recovery → post-incident activity). For MailGuard-shaped events:

1. **Preparation** — logging, roles, contacts, SLIs that show hold/release health.
2. **Detection** — alert on anomalous admin sign-in (e.g. impossible travel) or sudden hold-queue access.
3. **Containment** — revoke sessions/keys, freeze risky releases, limit who can read held content.
4. **Post-incident** — blameless postmortem with impact, timeline, root causes (tech + process), and owners for actions.

```text
Signal → triage (false positive?) → contain access → eradicate cause
      → recover service → postmortem + detection improvements
```

Trade-off: aggressive auto-lockouts reduce attacker dwell time but can lock out legitimate travelers — document human review paths. Keep Endpoint Detection and Response (**EDR**) / Managed Detection and Response (**MDR**) discussion vendor-neutral.

## Keep in mind

EDR/MDR are concepts here — stay vendor-neutral. Detection content is English-only for course artifacts.

## Read these (verified)

1. [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
2. Existing module SRE / golden signals reading
3. Cloud identity sign-in log docs for the IdP you use in lab

## On the job

Interview and IR drills ask for **how** you decide severity and **why** you notify privacy/security stakeholders when held mail may contain personal data — not just which button you clicked in a vendor console.

## Next step

`ir_triage` kata → assignment → quiz.
