package worker

import "testing"

func TestApplyDecision(t *testing.T) {
	if ApplyDecision(Hold) != "held" {
		t.Fatalf("hold label")
	}
	if ApplyDecision(Allow) != "allowed" {
		t.Fatalf("allow label")
	}
	if ApplyDecision(Reject) != "rejected" {
		t.Fatalf("reject label")
	}
}

func TestProcessNext(t *testing.T) {
	q := NewMemoryQueue()
	_ = q.Enqueue(Message{ID: "1", Subject: "hi", Body: "x"})
	summary, ok := ProcessNext(q, func(Message) Decision { return Hold })
	if !ok || summary != "1:held" {
		t.Fatalf("got %v %q", ok, summary)
	}
	_, ok = ProcessNext(q, func(Message) Decision { return Allow })
	if ok {
		t.Fatalf("expected empty queue")
	}
}
