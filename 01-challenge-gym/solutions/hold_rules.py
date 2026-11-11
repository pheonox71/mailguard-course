"""REFERENCE SOLUTION — peek only if stuck. Not imported by tests.

Hold-rules kata — tiny string/spec engine for outbound-message holds.
MailGuard preview: given a message and ordered rules, return the first
matching decision. Concise over clever — no plugin system, no DSL parser.
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


def _domain(addr: str) -> str:
    return addr.rsplit("@", 1)[-1].lower() if "@" in addr else ""


def matches(rule: Rule, msg: Message) -> bool:
    """True when every specified predicate on the rule holds."""
    if rule.recipient_domain is not None:
        want = rule.recipient_domain.lower()
        if not any(_domain(r) == want for r in msg.recipients):
            return False
    if rule.contains is not None:
        needle = rule.contains.lower()
        hay = f"{msg.subject}\n{msg.body}".lower()
        if needle not in hay:
            return False
    # A rule with no predicates never matches (avoid accidental catch-alls).
    return rule.recipient_domain is not None or rule.contains is not None


def evaluate(msg: Message, rules: Iterable[Rule], *, default: Decision = "allow") -> Decision:
    """First matching rule wins; otherwise `default`."""
    for rule in rules:
        if matches(rule, msg):
            return rule.decision
    return default
