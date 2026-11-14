# Reading — MailGuard Worker

## Learning objectives

1. Consume queued messages and apply rule decisions.
2. Keep a queue interface so local demos and cloud queues share code.
3. Document the contract with the Python API.

**Why this matters.** Synchronous HTTP-only gateways choke under burst mail and couple every retry to a client timeout. Without a worker, hold persistence, notifications, and release-to-MTA pile into the API process — and a crash mid-send has no clear redelivery story. History of mail pipelines favors async consumers with shared decision vocabulary (`hold` / `allow` / `reject`) so Python and Go do not drift.

**How it works.**

1. The API (or an ingest path) **enqueues** work as a JSON message.
2. A Go **worker** pulls messages behind a **queue interface** (in-memory / LocalStack now; cloud SQS later — [SQS overview](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)).
3. The worker applies the same decision vocabulary as Module 07 (`hold` / `allow` / `reject`).
4. It performs side effects (persist hold, notify, release toward an MTA).
5. On success it **acks/deletes** the message; on crash, at-least-once delivery redelivers — so handlers must be **idempotent**.
6. Table-driven `go test` locks the JSON contract with the Python API.

```
Producer / API → Queue → Go worker → apply decision → side effects → ack
                              ↑ interface: in-memory now, SQS later
```

### Worked example

Shared queue message JSON (API producer ↔ Go `QueueMessage` in `worker/sqs_contract.go`):

```json
{
  "id": "msg-42",
  "subject": "Q3 forecast",
  "body": "Confidential numbers…",
  "attempt": 1
}
```

The worker applies hold/allow/reject using the **same decision vocabulary** as Module 07 (rules evaluate / hold state). Do not invent parallel field names like `message_id` / `to` in the queue envelope — keep the Go struct and the producer JSON identical.

```
Receive → ParseQueueMessage → evaluate / apply decision
  hold   → persist hold row (idempotent on id)
  allow  → forward / no-op if already forwarded
  reject → record rejection
→ DeleteMessage / ack (attempt increments on failure; see DLQ reading)
```

**On the job.** Cloud email security, identity provisioning, and DLP all use workers + queues. Interviewers ask about idempotency, shared JSON contracts, and why you do not sprinkle cloud SDK calls through every package — vendor-neutral platform skills.

## Short intro

API services accept operator input; **workers** apply decisions asynchronously — hold persistence, notifications, or release to an MTA. This module is a Go worker with an in-memory queue interface and table-driven tests.

### Common misconceptions / what goes wrong

- **“Ack before side effects finish.”** A crash after ack loses the work; ack after success (and design for duplicate delivery).
- **“Exactly-once is guaranteed.”** Most queues are at-least-once; idempotency keys (`id` / hold id) are mandatory.
- **“Python and Go can invent their own field names.”** Field drift causes silent parse failures; document and test one JSON contract.
- **“The worker can call evaluate with different rules.”** Divergent policy engines are how allow/hold disagree across services — share vocabulary and fixtures.


## Videos (verified)

1. **[Learn Go Programming - Golang Tutorial for Beginners](https://www.youtube.com/watch?v=YS4e4q9oBaU)**  
   Why it helps: Go concurrency/packages backdrop for the worker.

## Read these (verified)

1. [Go — Getting Started](https://go.dev/doc/tutorial/getting-started)
2. [Go — testing package](https://pkg.go.dev/testing)
3. [AWS SQS — How it works](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) (conceptual; use a local interface first)

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment and tests.
