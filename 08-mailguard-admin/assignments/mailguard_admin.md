# Assignment — MailGuard Admin

**Language:** Vue 3 + TypeScript.

## Short questions (why / how / scenario)

1. **Why** keep API base URLs and tokens out of committed frontend code? What goes wrong if a token ships in the bundle?
2. **How / a11y:** What accessible label should an “Approve release” button expose to screen readers, and why is “click here” insufficient?
3. Name one XSS risk if you render held message subjects as raw HTML — **scenario:** subject is `<img src=x onerror=...>` — what should the UI do instead?
4. **Why** confirm destructive release even for trusted operators?

When you run the TypeScript kata (`npm test` / package scripts), prefer the module’s configured script **why:** same red/green loop as pytest without ad-hoc `tsc` flags drifting from CI.

## Done when

Answers written; TypeScript kata tests green.
