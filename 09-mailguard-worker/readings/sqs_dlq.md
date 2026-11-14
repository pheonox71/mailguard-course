# Reading — Queue consumer + DLQ

## Learning objectives

1. Consume work from a queue behind an interface (LocalStack SQS in lab).
2. Make processing idempotent; route poison messages to a **dead-letter queue**.
3. Share a JSON contract with the API module.

**Why this matters.** Poison messages that never succeed will retry forever without a **dead-letter queue (DLQ)** — burning compute and blocking the main queue’s visibility window. Handlers that are not idempotent double-send mail on redelivery after a crash. Field drift between API JSON and Go structs causes silent parse failures in production. DLQs exist so humans can inspect failures without losing the original payload.

**How it works.**

1. A consumer **receives** a message (visibility timeout hides it from other workers).
2. It **processes** the payload (parse JSON, apply decision, side effects).
3. On success it **deletes** the message.
4. On failure the message becomes visible again (**at-least-once** redelivery; attempt count increments).
5. After `maxReceiveCount` / max attempts, the broker moves it to a **DLQ** ([SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)).
6. Your kata’s `ShouldDLQ(attempt, maxAttempts)` encodes that threshold (typically `attempt >= maxAttempts`). Idempotency keys (message id / hold id) prevent double side effects. Parse shared JSON carefully — same fields as Module 07.

```
Main queue → worker
   │ fail / redeliver (attempt++)
   └─ attempt >= max → DLQ (inspect, fix, replay)
```

### Worked example

Threshold helper + a poison payload:

```go
// ShouldDLQ: move to DLQ when attempt reaches max (inclusive)
func ShouldDLQ(attempt, maxAttempts int) bool {
    return attempt >= maxAttempts // why: attempt==max means last try failed
}
```

| attempt | maxAttempts | ShouldDLQ? |
|---------|-------------|------------|
| 1 | 3 | false (retry) |
| 2 | 3 | false (retry) |
| 3 | 3 | **true** → DLQ |

```json
{
  "id": "",
  "subject": "poison",
  "body": "bad",
  "attempt": 5
}
```

If `id` is empty, `ParseQueueMessage` must error — that poison payload retries until DLQ rather than blocking the main queue forever. Fix the producer; do not silently invent an id.

**On the job.** SQS-style DLQs are standard in cloud mail and identity pipelines. Knowing when to DLQ vs retry — and how LocalStack demos the same shape — is day-to-day platform security engineering, not a single-vendor trick.

## Short intro

Queue consumers must survive crashes and bad payloads. Idempotency plus a DLQ turns “retry forever” into “park and investigate.”

### Common misconceptions / what goes wrong

- **“Use `attempt > maxAttempts`.”** Off-by-one leaves one extra burn on the main queue (or never DLQs); the kata expects `>=` — test both edges.
- **“DLQ means delete the problem.”** DLQ parks the payload for humans; without inspection/replay you just move the outage.
- **“Redelivery is rare.”** Crashes and timeouts are normal; non-idempotent handlers double-send.
- **“LocalStack is optional busywork.”** Proving the interface locally catches contract bugs before cloud credentials and cost enter the story.

## Local queue compose

Bring up an SQS-compatible broker on your laptop (ElasticMQ):

```bash
cd 09-mailguard-worker/starter
docker compose -f docker-compose.queue.yml up
```

- Compose file: [`../starter/docker-compose.queue.yml`](../starter/docker-compose.queue.yml)
- Config (main + DLQ): [`../starter/elasticmq.conf`](../starter/elasticmq.conf)
- API endpoint: `http://127.0.0.1:9324`
- Queues: `mailguard-hold` → DLQ `mailguard-hold-dlq` after `maxReceiveCount = 3`

Module 07 can enqueue the shared JSON contract via
[`../../07-mailguard-api/starter/app/queue_producer.py`](../../07-mailguard-api/starter/app/queue_producer.py)
(in-memory by default; comments show the ElasticMQ/LocalStack boto3 shape).


## Videos (verified)

1. **[Amazon SQS DLQ Setup Guide](https://www.youtube.com/watch?v=p4t0-_POkrI)**  
   Why it helps: redrive / DLQ mental model (pair with local ElasticMQ).

## Read these (verified)

1. [AWS SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
2. [LocalStack SQS](https://docs.localstack.cloud/user-guide/aws/sqs/)
3. [ElasticMQ](https://github.com/softwaremill/elasticmq) — SQS-compatible local broker used by the compose file above
4. [encoding/json](https://pkg.go.dev/encoding/json)

## Next step

Continue with the assignment, then implement `ShouldDLQ` / `ParseQueueMessage` and run `go test ./...` (**why:** red/green on the threshold and contract before wiring real SQS).
