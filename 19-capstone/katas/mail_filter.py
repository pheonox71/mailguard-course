"""Capstone mail filter — table-driven hold/allow/reject."""

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


def is_external(sender_domain: str, recipient: str) -> bool:
    raise NotImplementedError


def matches(rule: Rule, msg: Message) -> bool:
    raise NotImplementedError


def evaluate(msg: Message, rules: Iterable[Rule], *, default: Decision = "allow") -> Decision:
    raise NotImplementedError


def held_queue(messages: Iterable[Message], rules: Iterable[Rule]) -> list[Message]:
    """Messages that evaluate to hold."""
    raise NotImplementedError
