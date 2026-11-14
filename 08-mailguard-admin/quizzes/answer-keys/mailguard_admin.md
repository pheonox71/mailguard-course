# Quiz answer key — MailGuard Admin

Use only after attempting the quiz questions.

1. Catches missing fields/wrong unions at compile time before runtime surprises — hold vs allow typos become build failures, not missends.
2. Not in the public SPA bundle or git. Prefer a Backend-for-Frontend that holds tokens server-side and issues an HTTP-only session cookie to the browser ([RFC 10017](https://www.rfc-editor.org/rfc/rfc10017)). Cookie sessions still need CSRF defenses (SameSite, anti-CSRF token) on state-changing requests — moving tokens out of JS storage does not remove CSRF.
3. Operator id, message id, previous state, new state, timestamp, reason if required. State transition proves the machine was followed (e.g. approved→released), not just a button label.
4. XSS if subject contains HTML/JS; use textContent or a framework text binding (Vue `{{ }}` / `v-text`), never raw HTML for untrusted mail fields.
5. Clear accessible name (not icon-only); visible focus. Icon-only leaves screen-reader users without “Approve” vs “Reject” — wrong irreversible action.
6. Release is high-impact / hard to undo; a confirm reduces accidental clicks at acceptable cost for privileged actions.
