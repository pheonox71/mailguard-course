from katas.mail_filter import Message, Rule, evaluate, held_queue, is_external, matches

INTERNAL = Message(
    sender="alice@mailguard.example",
    recipients=("bob@mailguard.example",),
    subject="standup notes",
    body="see you at 10",
)
EXTERNAL = Message(
    sender="alice@mailguard.example",
    recipients=("eve@partner.example",),
    subject="Q4 forecast",
    body="confidential numbers",
)
BAD_ADDR = Message(
    sender="alice@mailguard.example",
    recipients=("not-an-email",),
    subject="hi",
    body="x",
)

def test_external_helper():
    assert is_external("mailguard.example", "eve@partner.example") is True
    assert is_external("mailguard.example", "bob@mailguard.example") is False

def test_keyword_reject():
    rules = [Rule("secret", "reject", contains="confidential")]
    assert evaluate(EXTERNAL, rules) == "reject"

def test_external_hold():
    rules = [Rule("ext", "hold", require_external=True)]
    assert matches(rules[0], EXTERNAL) is True
    assert evaluate(EXTERNAL, rules) == "hold"
    assert evaluate(INTERNAL, rules, default="allow") == "allow"

def test_empty_domain_predicate_never_matches():
    rules = [Rule("bad", "hold", recipient_domain="")]
    assert matches(rules[0], EXTERNAL) is False
    assert evaluate(BAD_ADDR, rules, default="allow") == "allow"

def test_held_queue():
    rules = [Rule("ext", "hold", require_external=True)]
    held = held_queue([INTERNAL, EXTERNAL], rules)
    assert held == [EXTERNAL]

def test_first_match():
    rules = [
        Rule("ext", "hold", recipient_domain="partner.example"),
        Rule("secret", "reject", contains="confidential"),
    ]
    assert evaluate(EXTERNAL, rules) == "hold"
