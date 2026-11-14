# 09 — MailGuard Worker

**Language:** Go. Est. 8-10h.

Queue consumer that applies hold/allow/reject decisions. Local interface first; cloud queue later.

## Workflow

1. [`readings/mailguard_worker.md`](./readings/mailguard_worker.md)
2. Assignment → implement Go stubs until `go test` passes
3. Required quiz

```bash
cd 09-mailguard-worker
go test ./...
```

**Done when:** local queue demo behind an interface; short Python-vs-Go contract note in the assignment.

## Local SQS-compatible queue

```bash
cd starter
docker compose -f docker-compose.queue.yml up
```

See [`readings/sqs_dlq.md`](./readings/sqs_dlq.md) for the DLQ contract and compose path. The API-side producer stub lives in `07-mailguard-api/starter/app/queue_producer.py`.

## Trade-offs / harden next

- In-memory queue for the kata; swap for ElasticMQ/SQS via the compose file above.
- Idempotency and DLQ belong in the harden-next list.
