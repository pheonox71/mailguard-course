# Assignment — Threat model the MailGuard hold path

**Language:** Conceptual (Markdown tables and short answers). No application language is required.

**Order:** reading → assignment under `my-work/assignments/` (blank already there) → required quiz PDF under `my-work/quizzes/`, then separate answer key on the site.

## Part A — Scope (4 bullets)

For each bullet, state **why** that scope choice matters (what fails if you skip it):

1. What asset are you protecting? (e.g. held message content, rule config, operator session)
2. Who are the actors? (sender, external attacker, operator, compromised admin, insider)
3. Trust boundaries? (browser ↔ API, API ↔ DB, worker ↔ queue, object storage)
4. Out of scope for this pass? (and why deferring it is safe *for now*)

## Part B — STRIDE table

Copy and fill (≥6 rows). Prefer **abuse stories + why the mitigation works** over one-word threats:

| Threat (STRIDE letter) | Abuse story (how) | Impact | Mitigation you have / gap (why it helps or what fails without it) |
|------------------------|-------------------|--------|------------------------------------------------------------------|
| S | | | |
| T | | | |
| R | | | |
| I | | | |
| D | | | |
| E | | | |

## Part C — Privacy (LINDDUN-lite)

One paragraph: who can read held bodies and audit logs? Retention? Redaction? **Why** does email-hold content need a stricter disclosure story than a public marketing site?

## Part D — SSDF / ASVS evidence (honest; SAMM optional)

1. Pick **one** STRIDE row from Part B. Map it to a [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) practice *and* an [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) requirement class (e.g. access control, logging). State **what evidence** you could show (test name, SQL pattern, CI job) — not a slogan.
2. *(Optional)* Pick **one** OWASP SAMM practice stream. Score yourself 0–1 informally and write the *next* concrete improvement (e.g. “add CI dependency scan”). Explain **why** that improvement beats claiming a higher maturity level you have not earned.

## Capstone link

Attach this page (or a PDF export) when you claim security notes / threat literacy on the rubric.
