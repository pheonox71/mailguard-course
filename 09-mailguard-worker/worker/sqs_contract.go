package worker

// QueueMessage is the JSON contract shared with the API (07).
// Attempt models SQS ApproximateReceiveCount for redrive / DLQ decisions
// (see ShouldDLQ). Keep bodies under the SQS 1 MiB message-size limit.
type QueueMessage struct {
	ID      string `json:"id"`
	Subject string `json:"subject"`
	Body    string `json:"body"`
	Attempt int    `json:"attempt"` // ≈ ApproximateReceiveCount when wired to SQS
}

// ShouldDLQ reports whether a failed attempt should go to the dead-letter queue.
// Map: attempt ≈ ApproximateReceiveCount; maxAttempts ≈ queue maxReceiveCount.
// Prefer >= so the final failed receive redrives instead of retrying forever.
func ShouldDLQ(attempt, maxAttempts int) bool {
	panic("implement ShouldDLQ")
}

// ParseQueueMessage decodes JSON into QueueMessage; error if id empty.
// Idempotent consumers key side effects on ID (hold id), not on Attempt.
func ParseQueueMessage(raw []byte) (QueueMessage, error) {
	panic("implement ParseQueueMessage")
}
