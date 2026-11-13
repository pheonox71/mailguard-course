package worker

type Decision string

const (
	Hold   Decision = "hold"
	Allow  Decision = "allow"
	Reject Decision = "reject"
)

type Message struct {
	ID      string
	Subject string
	Body    string
}

type Queue interface {
	Enqueue(msg Message) error
	Dequeue() (Message, bool)
}

// ApplyDecision returns the worker action label for a decision.
func ApplyDecision(d Decision) string {
	panic("implement ApplyDecision")
}

// ProcessNext dequeues one message and returns a summary line.
func ProcessNext(q Queue, decide func(Message) Decision) (string, bool) {
	panic("implement ProcessNext")
}
