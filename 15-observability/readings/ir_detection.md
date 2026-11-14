# Reading — Incident response & detection

## Learning objectives

1. Apply **NIST SP 800-61 Rev. 3** as a **CSF 2.0** community profile — not the Rev. 2 four-phase checklist alone.
2. Triage identity alerts (e.g. impossible travel) at a conceptual level.
3. Write a **blameless English postmortem** (impact, timeline, actions) — no secondary-language summary line required.

**Why this matters.** Hold-queue privacy incidents, missend+revoke events, and admin “impossible travel” alerts do not wait for a perfect runbook. Without a shared vocabulary, teams skip preparation work under **Govern / Identify / Protect**, thrash during **Respond**, and write blame-heavy writeups that do not prevent recurrence. On the job, email and identity security teams are expected to triage signals quickly, contain access, and document impact in clear English for legal/privacy partners.

**How it works.** National Institute of Standards and Technology (**NIST**) [SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025) is titled as a **Cybersecurity Framework (CSF) 2.0 Community Profile**. It embeds incident response across CSF 2.0 functions rather than replacing them with a standalone four-box lifecycle.

**Historical note (Rev. 2):** SP 800-61 Rev. 2 taught a familiar four-phase story — *Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity*. That language still appears in many runbooks; treat it as history when reading older materials.

**CSF 2.0 functions (current r3 framing):**

| CSF 2.0 function | IR-oriented focus for MailGuard-shaped events |
|------------------|-----------------------------------------------|
| **Govern** | Roles, policies, privacy duties for held content |
| **Identify** | Assets (hold queue, admin IdP, keys) and risk context |
| **Protect** | Hardening, least privilege, logging readiness before incidents |
| **Detect** | Alerts (impossible travel, anomalous hold access) |
| **Respond** | Contain sessions/keys, freeze risky releases, communicate |
| **Recover** | Restore service under least privilege; improve detections |

For MailGuard-shaped events:

1. **Govern / Identify / Protect** — logging, roles, contacts, SLIs that show hold/release health (the “preparation” work Rev. 2 named explicitly).
2. **Detect** — alert on anomalous admin sign-in (e.g. impossible travel) or sudden hold-queue access.
3. **Respond** — revoke sessions/keys, freeze risky releases, limit who can read held content; eradicate the cause (stolen token, misconfig).
4. **Recover** — restore service under least privilege; blameless postmortem with impact, timeline, root causes, and owners for actions.

```text
Signal → Detect/triage → Respond (contain + eradicate)
      → Recover service → postmortem + Govern/Protect improvements
```

Trade-off: aggressive auto-lockouts reduce attacker dwell time but can lock out legitimate travelers — document human review paths. Keep Endpoint Detection and Response (**EDR**) / Managed Detection and Response (**MDR**) discussion vendor-neutral.

### Worked example

Impossible-travel triage sketch (conceptual):

```text
Alert: admin Ada signed in from Region A at 10:00 UTC and Region B at 10:25 UTC
1. Detect — confirm IdP sign-in logs; check VPN/known travel; score severity
2. Respond — revoke active sessions / refresh tokens; temp step-up MFA; freeze hold-queue export
3. Notify — if held mail may contain personal data, loop privacy/security (why: transfer + access duties)
4. Recover / Govern — timeline, impact (accounts/queues touched), detection gap, owners + due dates
```

### Case study — Okta support HAR / session tokens (2023)

**Why this matters.** Session tokens that leak into support artifacts are as powerful as a password reset — and they often bypass MFA until revoked.

**What happened (verified):** Between late September and mid-October 2023, an unauthorized party accessed Okta’s support case-management system and obtained HTTP Archive (**HAR**) files that contained **live session tokens**. Okta tracked the access publicly and **revoked** those session tokens (notably on 17 Oct 2023, with a follow-up revocation pass) so stolen sessions could not keep acting as the victim ([Okta — Tracking Unauthorized Access](https://sec.okta.com/articles/2023/10/tracking-unauthorized-access-oktas-support-system/); [root-cause writeup](https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause/)).

**How you apply it (vendor-neutral):**

1. Treat HAR / browser-export / support-bundle files as **credential material** — never paste them into tickets, chat, or shared drives.
2. On suspected exposure: **revoke sessions and refresh tokens first**, then rotate related secrets; investigate only after containment.
3. Prefer redacted logs and short-lived tokens so a support artifact ages out quickly.

### Common misconceptions / what goes wrong

- **“800-61r3 is still the Rev. 2 four phases.”** Rev. 3 is a CSF 2.0 profile — map Detect / Respond / Recover (with Govern / Identify / Protect for readiness), and cite Rev. 2 only as historical language.
- **“Jump straight to eradication.”** Without containment first, stolen sessions keep reading hold queues while you “investigate.”
- **“Auto-lockout every impossible-travel alert.”** Legitimate travel and VPN exit nodes create false positives — document human review so on-call does not disable detection.
- **“HAR files are just debugging.”** They can embed live session cookies/tokens — the 2023 Okta support incident is the teaching case for revoke-first.
- **“Postmortem = name who clicked.”** Blame-heavy writeups do not prevent recurrence; fix logging, access, and playbooks ([NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).
- **“EDR/MDR brand names are the course.”** Concepts matter; stay vendor-neutral and keep detection artifacts in English.


## Videos (verified)

1. **[Overview - NIST Cybersecurity Framework 2.0](https://www.youtube.com/watch?v=f-6J7-WqcGE)** — Optic Cyber  
   Why it helps: CSF 2.0 backdrop for SP 800-61r3.

## Keep in mind

EDR/MDR are concepts here — stay vendor-neutral. Detection content is English-only for course artifacts.

## Read these (verified)

1. [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (CSF 2.0 Community Profile)
2. [NIST CSF 2.0](https://www.nist.gov/cyberframework)
3. [Okta — Tracking Unauthorized Access to Okta’s Support System (2023)](https://sec.okta.com/articles/2023/10/tracking-unauthorized-access-oktas-support-system/) — HAR / session-token revocation lesson
4. Existing module SRE / golden signals reading
5. Cloud identity sign-in log docs for the IdP you use in lab

## On the job

Interview and IR drills ask for **how** you decide severity and **why** you notify privacy/security stakeholders when held mail may contain personal data — not just which button you clicked in a vendor console.

## Next step

`ir_triage` kata → assignment → quiz.
