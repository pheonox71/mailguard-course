"""Simple in-memory persistence for the starter API.

Swap this for Postgres in a stretch lab — keep the evaluate path pure.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from threading import Lock
from typing import Literal
from uuid import uuid4

Decision = Literal["hold", "allow", "reject"]


@dataclass(frozen=True, slots=True)
class RuleRecord:
    name: str
    decision: Decision
    recipient_domain: str | None = None
    contains: str | None = None
    id: str = field(default_factory=lambda: uuid4().hex)


@dataclass(frozen=True, slots=True)
class MessageIn:
    sender: str
    recipients: tuple[str, ...]
    subject: str
    body: str


def _domain(addr: str) -> str:
    return addr.rsplit("@", 1)[-1].lower() if "@" in addr else ""


def matches(rule: RuleRecord, msg: MessageIn) -> bool:
    """True when every specified predicate holds; bare rules never match."""
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


def evaluate(msg: MessageIn, rules: list[RuleRecord], *, default: Decision = "allow") -> Decision:
    for rule in rules:
        if matches(rule, msg):
            return rule.decision
    return default


class MemoryStore:
    def __init__(self) -> None:
        self._rules: list[RuleRecord] = []
        self._lock = Lock()

    def add_rule(self, rule: RuleRecord) -> RuleRecord:
        with self._lock:
            self._rules.append(rule)
            return rule

    def list_rules(self) -> list[RuleRecord]:
        with self._lock:
            return list(self._rules)

    def get_rule(self, rule_id: str) -> RuleRecord | None:
        with self._lock:
            for rule in self._rules:
                if rule.id == rule_id:
                    return rule
            return None

    def delete_rule(self, rule_id: str) -> bool:
        with self._lock:
            for i, rule in enumerate(self._rules):
                if rule.id == rule_id:
                    del self._rules[i]
                    return True
            return False
