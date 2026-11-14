# Answer key — SQS + DLQ

1. No — only when `attempt >= 5`. Strict `>` never DLQs the final attempt; poison messages retry forever. Kata `attempt` models SQS `ApproximateReceiveCount`; `maxAttempts` models `maxReceiveCount` on the redrive policy.
2. Visibility timeout is a lease — when it expires the message reappears (at-least-once). Add idempotency (dedupe on message/hold id) so side effects apply once.
3. Attempt == max never DLQs; poison messages retry forever (or until manual intervention).
4. Prevent field drift and silent parse failures between Python producers and Go consumers.
5. Message ID / hold ID / outbound SMTP Message-ID — stable per logical work item; timestamps collide and change.
6. Humans can inspect, fix, and replay; delete loses forensic evidence and the original payload.
7. ElasticMQ is SQS-compatible without cloud credentials/cost (course default). Max message size is **1 MiB**. Use **AWS SDK for Go v2** only (not v1).
