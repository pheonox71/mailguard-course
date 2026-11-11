"""Tests for the hold-rules kata."""

from __future__ import annotations

from katas.hold_rules import Message, Rule, evaluate, matches

MSG = Message(
    sender="alice@mailguard.example",
    recipients=("bob@partner.example", "carol@mailguard.example"),
    subject="Q4 forecast attached",
    body="Please review the confidential numbers.",
)


def test_domain_rule_holds_external():
    rules = [Rule("ext", "hold", recipient_domain="partner.example")]
    assert evaluate(MSG, rules) == "hold"


def test_contains_rule_case_insensitive():
    rules = [Rule("secret", "reject", contains="CONFIDENTIAL")]
    assert matches(rules[0], MSG) is True
    assert evaluate(MSG, rules) == "reject"


def test_first_match_wins():
    rules = [
        Rule("ext", "hold", recipient_domain="partner.example"),
        Rule("secret", "reject", contains="confidential"),
    ]
    assert evaluate(MSG, rules) == "hold"


def test_default_when_no_match():
    rules = [Rule("gov", "hold", recipient_domain="gov.example")]
    assert evaluate(MSG, rules, default="allow") == "allow"


def test_empty_predicates_never_match():
    bare = Rule("noop", "reject")
    assert matches(bare, MSG) is False
