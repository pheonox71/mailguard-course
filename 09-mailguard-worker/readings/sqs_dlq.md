# Reading — Queue consumer + DLQ

## Learning objectives

1. Consume work from a queue behind an interface (LocalStack SQS in lab).
2. Make processing idempotent; route poison messages to a **dead-letter queue**.
3. Share a JSON contract with the API module.

**Why this matters.** Poison messages that never succeed will retry forever without a **dead-letter queue (DLQ)** — burning compute and blocking the main queue’s visibility window. Handlers that are not idempotent double-send mail on redelivery after a crash. Field drift between API JSON and Go structs causes silent parse failures in production. DLQs exist so humans can inspect failures without losing the original payload.

**How it works.** A consumer receives a message, processes it, then deletes it. If processing fails, the message becomes visible again (**at-least-once**). After `maxReceiveCount` / max attempts, the broker moves it to a DLQ. Your kata’s `ShouldDLQ(attempt, maxAttempts)` encodes that threshold (typically `attempt >= maxAttempts`). Idempotency keys (message id / hold id) prevent double side effects. Parse shared JSON carefully — same fields as Module 07.

```
Main queue → worker
   │ fail / redeliver (attempt++)
   └─ attempt >= max → DLQ (inspect, fix, replay)
```

**On the job.** SQS-style DLQs are standard in cloud mail and identity pipelines. Knowing when to DLQ vs retry — and how LocalStack demos the same shape — is day-to-day platform security engineering, not a single-vendor trick.

## Short intro

Queue consumers must survive crashes and bad payloads. Idempotency plus a DLQ turns “retry forever” into “park and investigate.”

## Read these (verified)

1. [AWS SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
2. [LocalStack SQS](https://docs.localstack.cloud/user-guide/aws/sqs/)
3. [encoding/json](https://pkg.go.dev/encoding/json)

## Next step

Continue with the assignment, then implement `ShouldDLQ` / `ParseQueueMessage` and run `go test ./...` (**why:** red/green on the threshold and contract before wiring real SQS).
