# Quiz — MailGuard Worker

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. **Why:** Why are queue consumers often **idempotent** under at-least-once delivery?
2. **Why:** Name one advantage of a queue **interface** over calling a cloud SDK in every package — what fails without that boundary?
3. **How:** What decision vocabulary must stay shared with the Python API, and **why** does drift hurt?
4. **Scenario:** A worker crashes after applying a hold but before deleting the queue message. What happens on restart with at-least-once delivery, and how should the handler behave?
5. **Spot the bug / why:** The worker logs the full message body including attachments to stdout in production. What is wrong?
6. **Trade-off:** When would you keep processing in the API process instead of a worker — and what do you give up?
