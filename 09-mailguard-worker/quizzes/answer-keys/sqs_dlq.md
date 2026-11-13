# Answer key — SQS + DLQ

1. No — only when `attempt >= 5`. Strict `>` never DLQs the final attempt; poison messages retry forever.
2. At-least-once redelivery / duplicate processing — add idempotency (dedupe key) so side effects apply once.
3. Attempt == max never DLQs; poison messages retry forever (or until manual intervention).
4. Prevent field drift and silent parse failures between Python producers and Go consumers.
5. Message ID / hold ID / outbound SMTP Message-ID — stable per logical work item; timestamps collide and change.
6. Humans can inspect, fix, and replay; delete loses forensic evidence and the original payload.
