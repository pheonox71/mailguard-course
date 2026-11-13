package worker

// QueueMessage is the JSON contract shared with the API (07).
type QueueMessage struct {
	ID      string `json:"id"`
	Subject string `json:"subject"`
	Body    string `json:"body"`
	Attempt int    `json:"attempt"`
}

// ShouldDLQ reports whether a failed attempt should go to the dead-letter queue.
func ShouldDLQ(attempt, maxAttempts int) bool {
	panic("implement ShouldDLQ")
}

// ParseQueueMessage decodes JSON into QueueMessage; error if id empty.
func ParseQueueMessage(raw []byte) (QueueMessage, error) {
	panic("implement ParseQueueMessage")
}
