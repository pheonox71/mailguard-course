# Assignment — SQS + DLQ

1. **What** does “at-least-once” delivery imply for your handler — **why** can’t you assume exactly-once?
2. **When** should a message move to the DLQ vs retry? State the rule in terms of attempt count.
3. Sketch the JSON fields shared with module 07 — **why** each field exists.
4. **How** do you avoid double-sending mail on redelivery?
5. Name one **ElasticMQ** tip for local SQS demos (compose under `starter/`) and **why** it beats pointing the kata at a real cloud account first. (Optional: LocalStack is another SQS-compatible option — not the course default.)
6. Map kata `attempt` to SQS `ApproximateReceiveCount` / redrive, explain visibility timeout as a **lease**, and note the **1 MiB** message-size limit + **AWS SDK Go v2** only.
