# Quiz — MailGuard API

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. **Why:** Why keep evaluation as a pure function separate from FastAPI route handlers (instead of putting all policy logic inside handlers)?
2. **How:** Walk first-match-wins in order: what stops the walk, and what happens to later matching rules?
3. **Scenario:** Rule 1 rejects if body contains `secret`; Rule 2 holds external domains. A message to `partner.example` with body `secret forecast` — outcome if Rule 1 is listed first? What if Rule 2 were listed first instead, and **why** does order matter on the job?
4. **Scenario:** Two instances of the API run behind a load balancer with an in-memory rule store. An operator adds a hold rule on instance A. What goes wrong for a message evaluated on instance B, and **why** is durable storage the usual fix?
5. **Spot the bug / why:** A handler catches all exceptions and returns HTTP 200 with `{"ok": true}`. What fails for clients, tests, and operators — and why is that worse than a loud 5xx?
6. **Trade-off:** Name one production gap of an in-memory rule store and one reason the kata still starts there.
7. **Why / how:** Why is tenant-scoped authZ (OWASP API1/API3/API5) required beyond “user is logged in,” and why create queue/DB clients in FastAPI lifespan (with an outbox toward Module 09) instead of module-level globals + best-effort enqueue?
