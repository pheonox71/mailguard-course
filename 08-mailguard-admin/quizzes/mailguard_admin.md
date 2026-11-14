# Quiz — MailGuard Admin

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. **Why:** Why is TypeScript `strict` useful for rule forms (vs catching everything only at runtime in the browser)?
2. **Why / how (RFC 10017):** Where should long-lived API tokens *not* live, what **BFF** pattern replaces them for a SPA calling a rules API, and why CSRF defenses still matter with cookie sessions?
3. **Scenario:** An operator releases a held message from the admin. Which audit fields would you log, and **why** is “previous state → new state” more useful than only “released”?
4. **Spot the bug / why:** `innerHTML = message.subject` in the hold queue. What is the risk, and what safer approach should you use?
5. **How / a11y:** Name one accessibility requirement for an Approve/Release control and **why** icon-only buttons fail operators using assistive tech.
6. **Trade-off:** Why might you confirm “Release” with a second step even though it slows the happy path?
