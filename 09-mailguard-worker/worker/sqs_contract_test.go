package worker

import "testing"

func TestShouldDLQ(t *testing.T) {
	if ShouldDLQ(2, 3) {
		t.Fatal("attempt 2 of 3 should not DLQ")
	}
	if !ShouldDLQ(3, 3) {
		t.Fatal("attempt 3 of 3 should DLQ")
	}
}

func TestParseQueueMessage(t *testing.T) {
	msg, err := ParseQueueMessage([]byte(`{"id":"a","subject":"s","body":"b","attempt":1}`))
	if err != nil {
		t.Fatal(err)
	}
	if msg.ID != "a" || msg.Attempt != 1 {
		t.Fatalf("unexpected %+v", msg)
	}
	if _, err := ParseQueueMessage([]byte(`{"id":"","subject":"s"}`)); err == nil {
		t.Fatal("expected error on empty id")
	}
}
