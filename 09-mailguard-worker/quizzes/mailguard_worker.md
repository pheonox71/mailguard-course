# Quiz — MailGuard Worker

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. Expand **DLQ**.
2. Why are queue consumers often **idempotent**?
3. Name one advantage of a queue interface over calling a cloud SDK everywhere.
4. What decision vocabulary must stay shared with the Python API?
5. **Scenario:** A worker crashes after applying a hold but before deleting the queue message. What happens on restart with at-least-once delivery?
6. **Spot the bug:** the worker logs the full message body including attachments to stdout in production. What is wrong?
