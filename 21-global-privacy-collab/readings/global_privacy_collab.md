# Reading — Global collaboration & privacy

## Learning objectives

1. Collaborate across timezones: async updates, explicit handoffs, inclusive meeting hygiene.
2. Compare major privacy laws at a literacy level: **GDPR**, **CCPA/CPRA**, **APPI**, **LGPD**, **PIPL**.
3. Connect privacy duties to MailGuard hold/release (minimization, access, retention, cross-border caution).

**Why this matters.** Hold queues can contain personal data (message bodies, recipients, attachments). A support engineer in another country asking for “just paste the held mail” can create a cross-border transfer problem. Global teams that only schedule meetings at one region’s afternoon quietly exclude others and slow incident response. On the job, email/identity SaaS work is multi-region by default — privacy literacy and async handoffs are operational skills, not soft extras.

**How it works.**

1. **Collaboration:** prefer written async handoffs with timezone stamps; rotate meeting hours or default to async; explicit owner for the next action.
2. **Privacy literacy:** General Data Protection Regulation (**GDPR**), California Consumer Privacy Act / California Privacy Rights Act (**CCPA/CPRA**), Japan’s Act on the Protection of Personal Information (**APPI**), Brazil’s Lei Geral de Proteção de Dados (**LGPD**), China’s Personal Information Protection Law (**PIPL**) — different scopes and breach-notification expectations; cite primary sources, do not memorize every article.
3. **MailGuard link:** minimize what the hold store keeps, restrict who can release/read, define retention, and check transfer rules before foreign support access.

```text
Incident spanning TZ A/B → async handoff note → least-privilege access check
                         → privacy regime checklist → notify / refuse as needed
```

### Worked example

Cross-border support request checklist (literacy-level — verify against primary sources before compliance claims):

```text
Request: “Support in Region B needs the held message PDF for ticket 123.”
1. What data? (headers only vs body/attachments — minimize)
2. Who needs access? (named role, time-boxed — least privilege)
3. Transfer / lawful basis? (check GDPR / CPRA / APPI / LGPD / PIPL as applicable)
4. Retention? (delete export after ticket; do not leave in chat forever)
5. Handoff note (UTC timestamps + next owner) if IR spans timezones
→ If checks fail: refuse paste; escalate privacy/security — do not “just send the PDF”
```

### Common misconceptions / what goes wrong

- **“Support overseas is the same as local admin access.”** Cross-border transfer and access rules may block casual paste of hold contents.
- **“Always-on meetings at one region’s 15:00 is inclusive.”** Fixed slots exclude others; rotate or default to async with explicit owners.
- **“Memorizing every article is the skill.”** Literacy + knowing where to cite ([GDPR.eu](https://gdpr.eu/), [CPPA](https://cppa.ca.gov/), [PPC](https://www.ppc.go.jp/en/), [ANPD](https://www.gov.br/anpd/pt-br)) beats trivia.
- **“Hold queues are ‘just logs.’”** Bodies and attachments are personal data with retention and access duties.

## Keep in mind

No language-learning drills. No employer-specific culture decks. Focus on professional norms that travel: clarity, respect for local holidays/time, and privacy-by-design.

## Read these (verified)

1. [GDPR.eu overview](https://gdpr.eu/) (prefer EUR-Lex for normative text)
2. [California CPPA — CCPA/CPRA](https://cppa.ca.gov/)
3. [Japan PPC English](https://www.ppc.go.jp/en/)
4. [Brazil ANPD (LGPD)](https://www.gov.br/anpd/pt-br)
5. Optional PIPL overview from reputable legal summaries — verify against official PRC texts when making compliance claims.

## On the job

Interview scenarios often ask: “Support overseas needs hold contents — what do you check first?” Lawful basis / transfer / least privilege / retention beats “sure, here’s the PDF.”

## Next step

Assignments → kata → quiz.
