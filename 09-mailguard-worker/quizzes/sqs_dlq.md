# Quiz — SQS + DLQ

1. What does DLQ stand for?
2. If maxAttempts=5, does attempt=4 go to the DLQ?
3. Scenario: handler crashes after side effects but before delete — what delivery risk remains?
4. Spot-the-bug: DLQ when `attempt > maxAttempts` only (strict greater).
5. Why share a JSON schema/contract with the API?
6. Name one idempotency key you could store.
