# Reading — MailGuard Admin

## Learning objectives

1. Describe an operator UI for rules and held messages.
2. Keep TypeScript strict for form models and queue rows.
3. Call a rules API without embedding secrets in the frontend.

**Why this matters.** The API can be correct and still fail operators: unclear Approve/Release, missing audit cues, or XSS via raw HTML subjects turns a hold queue into an attack surface. Secrets in the SPA bundle are stolen once and reused forever. Admin UIs are where identity, least privilege, and email-content handling meet the human — skipping TypeScript strictness and XSS hygiene is how “internal tool” incidents start.

**How it works.** A Vue 3 + TypeScript SPA talks to the Module 07 rules/hold API over HTTP. Forms validate rule fields before submit; the hold queue renders rows with **text** bindings (not `innerHTML`). Dangerous actions need accessible names, focus, and often confirm. Auth uses short-lived session cookies or a backend-for-frontend — never long-lived cloud tokens in git or the browser bundle. This module’s graded kata is a small TypeScript helper for validating rule forms and formatting hold-queue rows — enough to prove TS discipline before you wire the full UI.

```
Operator browser (Vue SPA) → HTTPS → MailGuard API → holds / rules
         ↑ never embed long-lived API keys here
```

**On the job.** Security products live or die on operator clarity: release is irreversible, subjects may contain attacker-controlled strings, and auditors ask who clicked what. Vendor-neutral skills — strict TS models, XSS-safe rendering, accessible confirmations — transfer to any cloud identity or DLP console.

## Short intro

The admin is the human control surface for MailGuard: list rules, inspect held messages, approve/release or reject. Prefer a Vue 3 + TypeScript SPA against the Module 07 API.

## Read these (verified)

1. [Vue 3 — Introduction](https://vuejs.org/guide/introduction.html)
2. [TypeScript — Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
3. [MDN — Form validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)
4. [OWASP — XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment and tests.
