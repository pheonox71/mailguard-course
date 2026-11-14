# Assignment — MailGuard Worker

## Short questions (why / how / scenario)

1. **Why** put a Go interface in front of the queue client?
2. **Scenario:** processing the same message twice (at-least-once delivery) — what should happen, and what must *not* happen?
3. Write 3–5 sentences: Python API vs Go worker responsibilities — **how** the JSON contract keeps them aligned.
4. **Why** prefer `go test ./...` from the module root before wiring ElasticMQ (or cloud SQS with AWS SDK Go v2)?

## Done when

Answers written; `go test ./...` green from your code.
