"""REFERENCE SOLUTION — peek only if stuck."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Literal
from uuid import uuid4

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
    id: str = field(default_factory=lambda: uuid4().hex)


def _domain(addr: str) -> str:
    return addr.rsplit("@", 1)[-1].lower() if "@" in addr else ""


def matches(rule: Rule, msg: Message) -> bool:
    if rule.recipient_domain is not None:
        want = rule.recipient_domain.lower()
        if not any(_domain(r) == want for r in msg.recipients):
            return False
    if rule.contains is not None:
        needle = rule.contains.lower()
        hay = f"{msg.subject}\n{msg.body}".lower()
        if needle not in hay:
            return False
    return rule.recipient_domain is not None or rule.contains is not None


def evaluate(msg: Message, rules: Iterable[Rule], *, default: Decision = "allow") -> Decision:
    for rule in rules:
        if matches(rule, msg):
            return rule.decision
    return default


class RuleStore:
    def __init__(self) -> None:
        self._rules: list[Rule] = []

    def add(self, rule: Rule) -> Rule:
        self._rules.append(rule)
        return rule

    def list(self) -> list[Rule]:
        return list(self._rules)

    def get(self, rule_id: str) -> Rule | None:
        for rule in self._rules:
            if rule.id == rule_id:
                return rule
        return None

    def delete(self, rule_id: str) -> bool:
        for i, rule in enumerate(self._rules):
            if rule.id == rule_id:
                del self._rules[i]
                return True
        return False
