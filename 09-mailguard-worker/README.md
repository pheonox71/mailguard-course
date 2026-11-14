# 09 — MailGuard Worker

**Language:** Go (1.25+). Est. 8-10h.

Queue consumer that applies hold/allow/reject decisions. In-memory interface first; **ElasticMQ** for local SQS API; cloud SQS with **AWS SDK Go v2** later.

## Workflow

1. [`readings/mailguard_worker.md`](./readings/mailguard_worker.md) + [`readings/sqs_dlq.md`](./readings/sqs_dlq.md)
2. Assignment → implement Go stubs until `go test` passes
3. Required quiz

```bash
cd 09-mailguard-worker
go test ./...
```

**Done when:** local queue demo behind an interface; short Python-vs-Go contract note in the assignment.

## Local SQS-compatible queue (ElasticMQ default)

```bash
cd starter
docker compose -f docker-compose.queue.yml up
```

See [`readings/sqs_dlq.md`](./readings/sqs_dlq.md) for:

- `attempt` vs SQS **`ApproximateReceiveCount`** / redrive
- visibility timeout as a **lease**
- idempotent consumers
- **1 MiB** max message size
- AWS SDK Go **v2** only
- Go 1.25 **`testing/synctest`** for concurrency tests

The API-side producer stub lives in `07-mailguard-api/starter/app/queue_producer.py`.

## Trade-offs / harden next

- In-memory queue for the kata; swap for ElasticMQ via the compose file above, then cloud SQS (SDK Go v2).
- Idempotency, visibility lease tuning, and DLQ inspection belong in the harden-next list.
