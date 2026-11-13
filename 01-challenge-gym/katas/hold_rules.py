"""Hold-rules kata — tiny string/spec engine for outbound-message holds.

MailGuard preview: given a message and ordered rules, return the first
matching decision. Concise over clever — no plugin system, no DSL parser.

Implement the stubs. Read assignments/hold_rules.md and tests/test_hold_rules.py
before coding. Peek at solutions/hold_rules.py only if stuck.
"""

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
    # Match if any recipient domain equals this (case-insensitive), or None.
    recipient_domain: str | None = None
    # Match if subject/body contains this substring (case-insensitive), or None.
    contains: str | None = None


def matches(rule: Rule, msg: Message) -> bool:
    """True when every specified predicate on the rule holds.

    - If `recipient_domain` is set: at least one recipient's domain must equal it
      (case-insensitive; domain = part after `@`).
    - If `contains` is set: subject or body must contain the substring
      (case-insensitive).
    - A rule with no predicates never matches (avoid accidental catch-alls).
    """
    raise NotImplementedError("implement matches — see assignments/hold_rules.md")


def evaluate(msg: Message, rules: Iterable[Rule], *, default: Decision = "allow") -> Decision:
    """First matching rule wins; otherwise `default`."""
    raise NotImplementedError("implement evaluate — see assignments/hold_rules.md")
