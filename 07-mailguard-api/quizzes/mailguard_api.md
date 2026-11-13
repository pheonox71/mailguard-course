# Quiz — MailGuard API

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. Expand **API** and **CRUD**.
2. What are the three MailGuard decisions this module models?
3. What does **first-match-wins** mean for ordered rules?
4. Why separate pure evaluation from FastAPI route handlers?
5. **Scenario:** Rule 1 rejects if body contains `secret`; Rule 2 holds external domains. A message to `partner.example` with body `secret forecast` — outcome if Rule 1 is first?
6. **Spot the bug:** a handler catches all exceptions and returns HTTP 200 with `{"ok": true}`. What goes wrong for clients and tests?
7. Name one production gap of an in-memory rule store.
