from katas.outbox import HoldRow, MemoryTxn, OutboxRow, apply_hold_change_with_outbox


def test_hold_and_outbox_same_transaction():
    txn = MemoryTxn()
    apply_hold_change_with_outbox(
        txn,
        hold_id="h1",
        new_state="approved",
        payload={"id": "h1", "event": "hold.approved"},
    )
    assert txn.committed is True
    assert txn.holds["h1"].state == "approved"
    assert len(txn.outbox) == 1
    row = txn.outbox[0]
    assert row.published is False
    assert row.payload == {"id": "h1", "event": "hold.approved"}


def test_rollback_leaves_neither_hold_nor_outbox():
    txn = MemoryTxn()
    txn.stage_hold(HoldRow(id="h1", state="held"))
    txn.stage_outbox(OutboxRow(id="o1", payload={"id": "h1"}, published=False))
    txn.rollback()
    assert txn.holds == {}
    assert txn.outbox == []
    assert txn.committed is False
