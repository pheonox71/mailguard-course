from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal

Decision = Literal["hold", "allow", "reject"]


@dataclass(frozen=True, slots=True)
class Message:
    sender: str
    recipients: tuple[str, ...]
    subject: str
    body: str


@dataclass(frozen=True, slots=True)
class Rule:
    name: str
    decision: Decision
    recipient_domain: str | None = None
    contains: str | None = None
    require_external: bool = False


def _domain(addr: str) -> str:
    return addr.rsplit("@", 1)[-1].lower() if "@" in addr else ""


def is_external(sender_domain: str, recipient: str) -> bool:
    return _domain(recipient) != sender_domain.lower()


def matches(rule: Rule, msg: Message) -> bool:
    sender_domain = _domain(msg.sender)
    if rule.require_external:
        if not any(is_external(sender_domain, r) for r in msg.recipients):
            return False
    if rule.recipient_domain is not None:
        want = rule.recipient_domain.lower()
        if want == "":
            return False
        if not any(_domain(r) == want for r in msg.recipients):
            return False
    if rule.contains is not None:
        needle = rule.contains.lower()
        hay = (msg.subject + "\n" + msg.body).lower()
        if needle not in hay:
            return False
    return (
        rule.require_external
        or rule.recipient_domain is not None
        or rule.contains is not None
    )


def evaluate(msg: Message, rules: Iterable[Rule], *, default: Decision = "allow") -> Decision:
    for rule in rules:
        if matches(rule, msg):
            return rule.decision
    return default


def held_queue(messages: Iterable[Message], rules: Iterable[Rule]) -> list[Message]:
    return [m for m in messages if evaluate(m, rules) == "hold"]
