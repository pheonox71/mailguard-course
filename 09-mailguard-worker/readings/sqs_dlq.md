# Reading — Queue consumer + DLQ

## Learning objectives

1. Consume work from a queue behind an interface (LocalStack SQS in lab).
2. Make processing idempotent; route poison messages to a **dead-letter queue**.
3. Share a JSON contract with the API module.

## Read these (verified)

1. [AWS SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
2. [LocalStack SQS](https://docs.localstack.cloud/user-guide/aws/sqs/)
3. [encoding/json](https://pkg.go.dev/encoding/json)

## Next step

Implement `ShouldDLQ` / `ParseQueueMessage`, then run `go test ./...`.
