# Reading — Queue consumer + DLQ

## Learning objectives

1. Consume work from a queue behind an interface (**ElasticMQ** as the default local SQS-compatible broker; cloud SQS later).
2. Make processing idempotent; route poison messages to a **dead-letter queue**.
3. Share a JSON contract with the API module.
4. Map kata `attempt` to SQS **`ApproximateReceiveCount`** / redrive, and treat **visibility timeout** as a lease.

**Why this matters.** Poison messages that never succeed will retry forever without a **dead-letter queue (DLQ)** — burning compute and blocking the main queue’s visibility window. Handlers that are not idempotent double-send mail on redelivery after a crash. Field drift between API JSON and Go structs causes silent parse failures in production. DLQs exist so humans can inspect failures without losing the original payload.

**How it works.**

1. A consumer **receives** a message. The broker starts a **visibility timeout** — a **lease**: other workers cannot see the message until the lease expires or the consumer deletes it. If the worker crashes before delete, the lease expires and the message is redelivered (at-least-once).
2. It **processes** the payload (parse JSON, apply decision, side effects). Keep handlers **idempotent** (same message id / hold id → same outcome, no double-send).
3. On success it **deletes** the message (ends the lease).
4. On failure the message becomes visible again (**at-least-once** redelivery). SQS increments **`ApproximateReceiveCount`** on each receive. Your kata field **`attempt`** models that count in the shared JSON contract — when you wire a real client, map `ApproximateReceiveCount` → `attempt` (or compare the attribute directly to `maxReceiveCount`).
5. After `maxReceiveCount` / max attempts, the broker **redrives** the message to a **DLQ** ([SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)). Your kata’s `ShouldDLQ(attempt, maxAttempts)` encodes that threshold (typically `attempt >= maxAttempts`).
6. SQS (and ElasticMQ’s SQS API) caps a message body at **1 MiB** — oversized payloads fail at send time; keep hold metadata small or store blobs elsewhere and pass a pointer.
7. When you add a real AWS client, use **[AWS SDK for Go v2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/welcome.html) only** (`github.com/aws/aws-sdk-go-v2/...`) — do not introduce the legacy v1 SDK.

```
Main queue → worker (visibility lease)
   │ fail / lease expires → redeliver (ApproximateReceiveCount / attempt++)
   └─ attempt >= maxReceiveCount → redrive → DLQ (inspect, fix, replay)
```

### Worked example

Threshold helper + a poison payload:

```go
// ShouldDLQ: move to DLQ when attempt reaches max (inclusive).
// In SQS, attempt ≈ ApproximateReceiveCount; maxAttempts ≈ maxReceiveCount on the redrive policy.
func ShouldDLQ(attempt, maxAttempts int) bool {
    return attempt >= maxAttempts // why: attempt==max means last try failed
}
```

| attempt (≈ ApproximateReceiveCount) | maxAttempts (≈ maxReceiveCount) | ShouldDLQ? |
|---------|-------------|------------|
| 1 | 3 | false (retry) |
| 2 | 3 | false (retry) |
| 3 | 3 | **true** → DLQ / redrive |

```json
{
  "id": "",
  "subject": "poison",
  "body": "bad",
  "attempt": 5
}
```

If `id` is empty, `ParseQueueMessage` must error — that poison payload retries until DLQ rather than blocking the main queue forever. Fix the producer; do not silently invent an id.

**On the job.** SQS-style DLQs are standard in cloud mail and identity pipelines. Knowing when to DLQ vs retry — and how **ElasticMQ** demos the same shape locally — is day-to-day platform security engineering, not a single-vendor trick.

## Short intro

Queue consumers must survive crashes and bad payloads. Idempotency plus a DLQ turns “retry forever” into “park and investigate.”

### Common misconceptions / what goes wrong

- **“Use `attempt > maxAttempts`.”** Off-by-one leaves one extra burn on the main queue (or never DLQs); the kata expects `>=` — test both edges.
- **“DLQ means delete the problem.”** DLQ parks the payload for humans; without inspection/replay you just move the outage.
- **“Visibility timeout is just a sleep.”** It is a **lease**: too short → duplicate consumers; too long → slow recovery after a crash.
- **“`attempt` in JSON is unrelated to SQS.”** In production, prefer `ApproximateReceiveCount` (or keep JSON `attempt` in sync with it) so redrive policy and handler logic agree.
- **“Redelivery is rare.”** Crashes and timeouts are normal; non-idempotent handlers double-send.
- **“Any AWS Go SDK is fine.”** Use **SDK Go v2** only when wiring SQS; v1 is legacy.
- **“Point the kata at a real cloud account first.”** Prefer **ElasticMQ** (compose below) so contract bugs show up without credentials or cost. LocalStack remains an optional SQS-compatible alternative, not the default lab path.

## Local queue compose (ElasticMQ default)

Bring up an SQS-compatible broker on your laptop (**ElasticMQ** is the course default):

```bash
cd 09-mailguard-worker/starter
docker compose -f docker-compose.queue.yml up
```

- Compose file: [`../starter/docker-compose.queue.yml`](../starter/docker-compose.queue.yml)
- Config (main + DLQ): [`../starter/elasticmq.conf`](../starter/elasticmq.conf)
- API endpoint: `http://127.0.0.1:9324`
- Queues: `mailguard-hold` → DLQ `mailguard-hold-dlq` after `maxReceiveCount = 3`
- Message size: stay under **1 MiB** (SQS limit)

Module 07 can enqueue the shared JSON contract via
[`../../07-mailguard-api/starter/app/queue_producer.py`](../../07-mailguard-api/starter/app/queue_producer.py)
(in-memory by default; comments show the ElasticMQ boto3 shape).

### Concurrency tests (Go 1.25+)

When you add concurrent lease / multi-consumer tests, prefer Go **1.25+** [`testing/synctest`](https://pkg.go.dev/testing/synctest) so bubble time and goroutine coordination stay deterministic — avoid flaky `time.Sleep` races in CI.

## Videos (verified)

1. **[Amazon SQS DLQ Setup Guide](https://www.youtube.com/watch?v=p4t0-_POkrI)**  
   Why it helps: redrive / DLQ mental model (pair with local ElasticMQ).

## Read these (verified)

1. [AWS SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — redrive + `maxReceiveCount` / `ApproximateReceiveCount`.
2. [AWS SQS — Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) — lease semantics.
3. [AWS SQS quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html) — **1 MiB** max message size.
4. [ElasticMQ](https://github.com/softwaremill/elasticmq) — SQS-compatible local broker used by the compose file above (course default).
5. [AWS SDK for Go v2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/welcome.html) — use v2 only when wiring real SQS.
6. [encoding/json](https://pkg.go.dev/encoding/json)
7. [testing/synctest](https://pkg.go.dev/testing/synctest) (Go 1.25+) — deterministic concurrency tests.

## Next step

Continue with the assignment, then implement `ShouldDLQ` / `ParseQueueMessage` and run `go test ./...` (**why:** red/green on the threshold and contract before wiring real SQS).
