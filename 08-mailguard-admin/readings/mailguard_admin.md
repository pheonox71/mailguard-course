# Reading — MailGuard Admin

## Learning objectives

1. Describe an operator UI for rules and held messages.
2. Keep TypeScript strict for form models and queue rows.
3. Call a rules API without embedding secrets in the frontend.

**Why this matters.** The API can be correct and still fail operators: unclear Approve/Release, missing audit cues, or XSS via raw HTML subjects turns a hold queue into an attack surface. Secrets in the SPA bundle are stolen once and reused forever. Admin UIs are where identity, least privilege, and email-content handling meet the human — skipping TypeScript strictness and XSS hygiene is how “internal tool” incidents start.

**How it works.**

1. A Vue 3 + TypeScript SPA talks to the Module 07 rules/hold API over HTTPS.
2. Forms validate rule fields (predicates, action) before submit.
3. The hold queue renders rows with **text** bindings — not `innerHTML` — so attacker-controlled subjects cannot inject script ([OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)).
4. Dangerous actions (approve / release / reject) need accessible names, focus order, and an explicit confirm dialog that meets **WCAG 2.2** keyboard/focus rules (`role="dialog"`, `aria-modal`, Escape to dismiss, focus moves into the dialog and returns on close, visible `:focus-visible`).
5. Auth uses short-lived session cookies or a **Backend-for-Frontend (BFF)** — never long-lived cloud tokens in git or the browser bundle. [RFC 10017](https://www.rfc-editor.org/rfc/rfc10017) recommends BFF for browser-based OAuth clients: the SPA gets an HTTP-only session cookie; the BFF holds tokens and calls APIs. Cookie sessions still need **CSRF** defenses (SameSite, anti-CSRF tokens) on state-changing requests.
6. This module’s graded kata is a small TypeScript helper for validating rule forms and formatting hold-queue rows — enough to prove TS discipline before you wire the full UI.

```
Operator browser (Vue SPA) → HTTPS → MailGuard API → holds / rules
         ↑ never embed long-lived API keys here
```

### Worked example

Formatting a hold-queue row safely (conceptual):

```ts
type HoldRow = {
  id: string;
  state: "held" | "approved" | "rejected" | "released";
  subject: string; // may contain attacker-controlled text
};

function rowLabel(h: HoldRow): string {
  // Why: return plain text for the template — Vue text interpolation escapes HTML
  return `${h.id} · ${h.state} · ${h.subject}`;
}

// Template: {{ rowLabel(hold) }}  — safe
// Avoid: v-html="hold.subject"   — XSS if subject is <img onerror=...>
```

Approve dialog (WCAG 2.2 focus / keyboard — see [`../starter/src/App.vue`](../starter/src/App.vue)):

```text
Open Approve → focus moves into dialog (Cancel)
Tab / Shift+Tab cycle actions · Escape closes · focus returns to opener
role="dialog" aria-modal="true" aria-labelledby=title · :focus-visible ring
Subject still via text binding inside the dialog (never v-html)
```

**On the job.** Security products live or die on operator clarity: release is irreversible, subjects may contain attacker-controlled strings, and auditors ask who clicked what. Vendor-neutral skills — strict TS models, XSS-safe rendering, accessible confirmations — transfer to any cloud identity or DLP console.

## Short intro

The admin is the human control surface for MailGuard: list rules, inspect held messages, approve/release or reject. Prefer a Vue 3 + TypeScript SPA against the Module 07 API. This module’s graded kata is a small TypeScript helper for validating rule forms and formatting hold-queue rows — enough to prove TS discipline before you wire the full UI.

### Common misconceptions / what goes wrong

- **“Internal tools do not need XSS care.”** Held subjects and addresses are untrusted input; `innerHTML` / `v-html` turns the queue into a script host.
- **“Strict TypeScript slows demos.”** Untyped form state is how allow/hold labels swap; the kata exists to prove discipline before a full SPA.
- **“Cloud API keys in `.env` shipped to the client are OK.”** Anything in the SPA bundle is readable; use session/BFF patterns ([RFC 10017](https://www.rfc-editor.org/rfc/rfc10017)).
- **“BFF removes CSRF entirely.”** Moving tokens server-side still leaves cookie-authenticated POSTs CSRF-vulnerable unless you add SameSite / anti-CSRF controls (same RFC).
- **“Confirm dialogs are optional UX.”** Release is irreversible; accessible confirm reduces miss-clicks and documents intent for audit.
- **“Focus can stay on the page behind the modal.”** WCAG 2.2 expects operable keyboard focus inside the dialog and a return path — trap/cycle Tab, Escape dismisses, restore focus on close.


## Videos (verified)

1. **[Vue.js Course for Beginners](https://www.youtube.com/watch?v=FXpIoQ_rT_c)**  
   Why it helps: admin SPA patterns for hold queues.

## Read these (verified)

1. [Vue 3 — Introduction](https://vuejs.org/guide/introduction.html)
2. [TypeScript — Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
3. [MDN — Form validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)
4. [OWASP — XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
5. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — focus visible / not obscured; keyboard operable dialogs.
6. [RFC 10017 — OAuth 2.0 for Browser-Based Apps](https://www.rfc-editor.org/rfc/rfc10017) — BFF + CSRF for the admin SPA.

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment and tests.
