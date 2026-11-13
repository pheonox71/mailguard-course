# Quiz — CI + AWS

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. **Why** does CI on every PR matter for a hold/allow rules engine more than “we’ll test before the big demo”?
2. Expand **CI** and **OIDC** (in the deploy sense), then explain **how** OIDC deploy differs from storing long-lived AWS keys.
3. Name one least-privilege choice for a deploy role and **why** it shrinks blast radius.
4. **How** should a PR workflow for MailGuard’s Python core be ordered (setup → …), and **why** run tests before any deploy/image-push job?
5. **Scenario:** A workflow prints `echo $AWS_SECRET_ACCESS_KEY` for debugging. What fails, and **why** is log redaction alone not enough?
6. **Spot the bug / why:** `permissions: write-all` on a public fork PR workflow. What can go wrong and how would you tighten it?
