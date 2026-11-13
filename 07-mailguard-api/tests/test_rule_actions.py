import pytest
from katas.rule_actions import normalize_action, describe

def test_allow():
    a = normalize_action("allow")
    assert a.kind == "allow"
    assert describe(a) == "allow"

def test_auto_bcc():
    a = normalize_action("auto_bcc", "archive@example.com")
    assert a.bcc == "archive@example.com"
    assert "archive@example.com" in describe(a)

def test_auto_bcc_requires_address():
    with pytest.raises(ValueError):
        normalize_action("auto_bcc", None)

def test_delete():
    assert describe(normalize_action("delete")) == "delete matching messages"
