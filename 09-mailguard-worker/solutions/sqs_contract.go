package worker

import (
	"encoding/json"
	"fmt"
)

// QueueMessage is the JSON contract shared with the API (07).
// Attempt models SQS ApproximateReceiveCount for redrive / DLQ decisions.
// Keep bodies under the SQS 1 MiB message-size limit.
type QueueMessage struct {
	ID      string `json:"id"`
	Subject string `json:"subject"`
	Body    string `json:"body"`
	Attempt int    `json:"attempt"` // ≈ ApproximateReceiveCount when wired to SQS
}

// ShouldDLQ: attempt ≈ ApproximateReceiveCount; maxAttempts ≈ maxReceiveCount.
func ShouldDLQ(attempt, maxAttempts int) bool {
	if maxAttempts < 1 {
		return true
	}
	return attempt >= maxAttempts
}

// ParseQueueMessage: idempotent consumers key side effects on ID, not Attempt.
func ParseQueueMessage(raw []byte) (QueueMessage, error) {
	var m QueueMessage
	if err := json.Unmarshal(raw, &m); err != nil {
		return QueueMessage{}, err
	}
	if m.ID == "" {
		return QueueMessage{}, fmt.Errorf("id required")
	}
	return m, nil
}
