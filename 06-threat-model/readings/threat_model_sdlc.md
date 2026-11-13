# Reading — Threat modeling & lightweight secure SDLC

## Learning objectives

1. Apply a **STRIDE**-lite pass to MailGuard’s hold/release path (who can spoof an operator? tamper with rules? deny the queue?).
2. Relate findings to mitigations you already ship (MFA, audit logs, first-match rules, CI) and gaps you document honestly.
3. Skim **OWASP SAMM** as a maturity *map*, not a certificate — pick one practice to improve next.

**Why this matters.** Shipping hold/release without naming abuse stories leaves gaps that MFA, audits, and CI cannot invent for you. Teams that skip threat modeling discover spoofed operators, silent rule tampering, and held-body disclosure in production — after users are affected. A lightweight pass costs a page of Markdown; a missed elevation path costs incident response.

**How it works.** Threat modeling asks four questions (Shostack): what are we working on → what can go wrong → what are we doing about it → did we do a good job? **STRIDE** (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) is a Microsoft-origin checklist that maps each abuse story to a concrete element (session, rule store, queue). Secure Software Development Life Cycle (**SDLC**) means those questions recur in requirements, design, implementation, test, and operate — not only in a final pen-test fantasy. **LINDDUN** is a privacy-oriented sibling; for MailGuard, focus on disclosure of held message bodies and audit access. **OWASP SAMM** (Software Assurance Maturity Model) maps five business functions (Governance, Design, Implementation, Verification, Operations) so you pick *one* practice to improve — not claim enterprise maturity.

**On the job.** Email and identity gateways always have privileged operator actions (release, rule edit). Interviewers and security reviews expect you to walk a trust-boundary diagram and name STRIDE rows with mitigations or honest gaps — vendor-neutral vocabulary that transfers across cloud mail and SaaS admin consoles.

## Short intro

Threat modeling asks “what can go wrong?” before or while you build. Secure Software Development Life Cycle (**SDLC**) means security activities show up in requirements, design, implementation, test, and operate — not only in a final pen-test fantasy.

**STRIDE** is still useful interview vocabulary. Prefer a short table over a unused enterprise tool: six abuse stories tied to MailGuard’s hold path beat a blank “we follow best practices.”

![STRIDE-lite checklist with example questions for a hold and release path](images/stride-lite.svg)

*Figure. Six STRIDE categories as a lightweight checklist on the hold/release path. Notice each tile pairs a threat question with a mitigation you may already ship (MFA, audit logs, least privilege) — document gaps honestly. Original course diagram (CC0).*

### Trade-offs

| Approach | When it helps | Cost / limit |
|----------|---------------|--------------|
| STRIDE-lite table | Fast feature reviews | Misses privacy-specific linking threats (use LINDDUN-lite) |
| Full threat-modeling tools | Regulated programs | Overhead for a student kata |
| Pen-test only at the end | Finds some bugs | Too late for design-level trust boundaries |

## Videos (verified)

1. **[Threatmodcon keynote (segment)](https://www.youtube.com/watch?v=4ngYKVAs22c)** — Adam Shostack  
   Why it helps: threat modeling as a practice; pairs with the four-question frame in writing.

2. **[Keynote: Stop Trying to "Manage Risk"](https://www.youtube.com/watch?v=THSfJIlPGPk)** — Adam Shostack  
   Why it helps: connects threat modeling judgment to delivery — not spreadsheet theater.

Also skim: [Shostack + Associates — threat modeling beginner guide](https://adam.shostack.org/resources/threat-modeling) (four questions).

## Read these (verified)

1. [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling) — community overview.
2. [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — practical steps.
3. [Microsoft — STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) — threat categories reference.
4. [OWASP SAMM](https://owasp.org/www-project-samm/) — five business functions: **Governance**, Design, Implementation, Verification, Operations (15 practices).
5. [LINDDUN](https://www.linddun.org/) — privacy threat categories (skim).
6. [Shostack four-question frame (GitHub)](https://github.com/adamshostack/4QuestionFrame) — one-pager.

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment.
