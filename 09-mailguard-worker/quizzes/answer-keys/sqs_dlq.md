# Answer key — SQS + DLQ

1. Dead-letter queue.
2. No — only when attempt >= 5.
3. At-least-once redelivery / duplicate processing.
4. Attempt==max never DLQs; poison messages retry forever.
5. Prevent field drift and silent parse failures.
6. Message ID / hold ID / outbound SMTP Message-ID.
