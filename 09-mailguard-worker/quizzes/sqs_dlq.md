# Quiz — SQS + DLQ

1. **How / why:** If `maxAttempts=5`, does `attempt=4` go to the DLQ? Explain the threshold rule (`>=` vs `>`).
2. **Scenario:** Handler crashes after side effects but before delete — what delivery risk remains, and what mitigation do you add?
3. **Spot the bug:** DLQ when `attempt > maxAttempts` only (strict greater). What happens to poison messages at `attempt == maxAttempts`?
4. **Why:** Why share a JSON schema/contract with the API instead of “whatever fields we remember”?
5. **How:** Name one idempotency key you could store and **why** that key (not “timestamp”) is a good choice.
6. **Trade-off:** Why park poison messages on a DLQ instead of deleting them after N failures?
