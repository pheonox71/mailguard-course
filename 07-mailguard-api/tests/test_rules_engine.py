"""Tests for MailGuard API rules engine."""

from __future__ import annotations

from katas.rules_engine import Message, Rule, RuleStore, evaluate, matches

MSG = Message(
    sender="alice@mailguard.example",
    recipients=("bob@partner.example",),
    subject="Q4 forecast",
    body="Confidential numbers attached.",
)


def test_domain_hold():
    rule = Rule("ext", "hold", recipient_domain="partner.example")
    assert matches(rule, MSG) is True
    assert evaluate(MSG, [rule]) == "hold"


def test_contains_reject_case_insensitive():
    rule = Rule("secret", "reject", contains="CONFIDENTIAL")
    assert evaluate(MSG, [rule]) == "reject"


def test_first_match_wins():
    rules = [
        Rule("ext", "hold", recipient_domain="partner.example"),
        Rule("secret", "reject", contains="confidential"),
    ]
    assert evaluate(MSG, rules) == "hold"


def test_default_when_no_match():
    assert evaluate(MSG, [Rule("gov", "hold", recipient_domain="gov.example")], default="allow") == "allow"


def test_bare_rule_never_matches():
    assert matches(Rule("noop", "reject"), MSG) is False


def test_store_crud():
    store = RuleStore()
    rule = Rule("ext", "hold", recipient_domain="partner.example")
    saved = store.add(rule)
    assert store.get(saved.id) == saved
    assert store.list() == [saved]
    assert store.delete(saved.id) is True
    assert store.get(saved.id) is None
