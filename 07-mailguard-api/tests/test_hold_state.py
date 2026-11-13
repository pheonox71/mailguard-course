import pytest
from katas.hold_state import HoldItem, apply_action, can_release

def test_approve_then_release():
    item = HoldItem("1", "held")
    item = apply_action(item, "approve")
    assert item.state == "approved"
    assert can_release(item)
    item = apply_action(item, "release")
    assert item.state == "released"

def test_reject_from_held():
    assert apply_action(HoldItem("1", "held"), "reject").state == "rejected"

def test_illegal_release_from_held():
    with pytest.raises(ValueError):
        apply_action(HoldItem("1", "held"), "release")

def test_cannot_release_until_approved():
    assert can_release(HoldItem("1", "held")) is False
