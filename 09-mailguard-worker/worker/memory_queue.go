package worker

type MemoryQueue struct {
	items []Message
}

func NewMemoryQueue() *MemoryQueue {
	return &MemoryQueue{items: make([]Message, 0)}
}

func (q *MemoryQueue) Enqueue(msg Message) error {
	q.items = append(q.items, msg)
	return nil
}

func (q *MemoryQueue) Dequeue() (Message, bool) {
	if len(q.items) == 0 {
		return Message{}, false
	}
	m := q.items[0]
	q.items = q.items[1:]
	return m, true
}
