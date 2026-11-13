"""MailGuard API — rules engine kata.

Implement first-match-wins evaluation for hold/allow/reject rules.
Read worksheets/mailguard_api.md and tests before coding.
"""

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


def matches(rule: Rule, msg: Message) -> bool:
    """True when every specified predicate holds; bare rules never match."""
    raise NotImplementedError("implement matches")


def evaluate(msg: Message, rules: Iterable[Rule], *, default: Decision = "allow") -> Decision:
    """First matching rule wins; otherwise default."""
    raise NotImplementedError("implement evaluate")


class RuleStore:
    """Tiny in-memory CRUD used by the API layer."""

    def __init__(self) -> None:
        self._rules: list[Rule] = []

    def add(self, rule: Rule) -> Rule:
        raise NotImplementedError("implement add")

    def list(self) -> list[Rule]:
        raise NotImplementedError("implement list")

    def get(self, rule_id: str) -> Rule | None:
        raise NotImplementedError("implement get")

    def delete(self, rule_id: str) -> bool:
        raise NotImplementedError("implement delete")
