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

func ApplyDecision(d Decision) string {
	switch d {
	case Hold:
		return "held"
	case Allow:
		return "allowed"
	case Reject:
		return "rejected"
	default:
		return "unknown"
	}
}

func ProcessNext(q Queue, decide func(Message) Decision) (string, bool) {
	msg, ok := q.Dequeue()
	if !ok {
		return "", false
	}
	return msg.ID + ":" + ApplyDecision(decide(msg)), true
}
