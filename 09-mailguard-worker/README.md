# 09 — MailGuard Worker

**Language:** Go. Est. 8-10h.

Queue consumer that applies hold/allow/reject decisions. Local interface first; cloud queue later.

## Workflow

1. [`readings/mailguard_worker.md`](./readings/mailguard_worker.md)
2. Worksheet → implement Go stubs until `go test` passes
3. Required quiz

```bash
cd 09-mailguard-worker
go test ./...
```

**Done when:** local queue demo behind an interface; short Python-vs-Go contract note in the worksheet.

## Trade-offs / harden next

- In-memory queue for the kata; swap for SQS/compatible later.
- Idempotency and DLQ belong in the harden-next list.
