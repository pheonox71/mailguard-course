# Reading — MailGuard Worker

## Learning objectives

1. Consume queued messages and apply rule decisions.
2. Keep a queue interface so local demos and cloud queues share code.
3. Document the contract with the Python API.

**Why this matters.** Synchronous HTTP-only gateways choke under burst mail and couple every retry to a client timeout. Without a worker, hold persistence, notifications, and release-to-MTA pile into the API process — and a crash mid-send has no clear redelivery story. History of mail pipelines favors async consumers with shared decision vocabulary (`hold` / `allow` / `reject`) so Python and Go do not drift.

**How it works.** The API (or an ingest path) **enqueues** work. A Go **worker** pulls messages, applies the same decision vocabulary as Module 07, performs side effects, then deletes/acks the message. Behind a **queue interface**, local in-memory (or LocalStack) fakes swap for cloud SQS later. Prefer **idempotent** handlers: at-least-once delivery redelivers after crashes. Table-driven `go test` locks the contract.

```
Producer / API → Queue → Go worker → apply decision → side effects → ack
                              ↑ interface: in-memory now, SQS later
```

**On the job.** Cloud email security, identity provisioning, and DLP all use workers + queues. Interviewers ask about idempotency, shared JSON contracts, and why you do not sprinkle cloud SDK calls through every package — vendor-neutral platform skills.

## Short intro

API services accept operator input; **workers** apply decisions asynchronously — hold persistence, notifications, or release to an MTA. This module is a Go worker with an in-memory queue interface and table-driven tests.

## Read these (verified)

1. [Go — Getting Started](https://go.dev/doc/tutorial/getting-started)
2. [Go — testing package](https://pkg.go.dev/testing)
3. [AWS SQS — How it works](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) (conceptual; use a local interface first)

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment and tests.
