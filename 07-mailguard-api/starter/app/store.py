"""Simple in-memory persistence for the starter API.

Reuse the rules engine (Rule/Message + matches/evaluate) so HTTP routes do not
fork first-match-wins semantics. MemoryStore adds a lock for concurrent demos.
Swap this for Postgres in a stretch lab — keep the evaluate path pure.

By default the API imports from ``katas/`` (what the student implements).
Set ``MAILGUARD_USE_SOLUTIONS=1`` to allow ``solutions/`` (CI demos / peek path).
When that flag is set and a kata stub still raises ``NotImplementedError``,
evaluate/matches fall back to the reference implementation and log clearly.
"""

from __future__ import annotations

import logging
import os
from threading import Lock
from typing import Iterable

_log = logging.getLogger(__name__)

_USE_SOLUTIONS = os.environ.get("MAILGUARD_USE_SOLUTIONS") == "1"

if _USE_SOLUTIONS:
    from katas import rules_engine as _kata
    from solutions import rules_engine as _sol

    Decision = _sol.Decision
    Message = _sol.Message
    Rule = _sol.Rule

    def matches(rule: Rule, msg: Message) -> bool:
        try:
            return _kata.matches(rule, msg)
        except NotImplementedError:
            _log.warning(
                "katas.rules_engine.matches is not implemented; "
                "falling back to solutions/ (MAILGUARD_USE_SOLUTIONS=1)"
            )
            return _sol.matches(rule, msg)

    def evaluate(
        msg: Message,
        rules: Iterable[Rule],
        *,
        default: Decision = "allow",
    ) -> Decision:
        try:
            return _kata.evaluate(msg, rules, default=default)
        except NotImplementedError:
            _log.warning(
                "katas.rules_engine.evaluate is not implemented; "
                "falling back to solutions/ (MAILGUARD_USE_SOLUTIONS=1)"
            )
            return _sol.evaluate(msg, rules, default=default)

    _log.info("rules engine: solutions/ enabled (MAILGUARD_USE_SOLUTIONS=1)")
else:
    from katas.rules_engine import Decision, Message, Rule, evaluate, matches

# Stable names used by the router / OpenAPI layer.
RuleRecord = Rule
MessageIn = Message

__all__ = [
    "Decision",
    "MemoryStore",
    "MessageIn",
    "RuleRecord",
    "evaluate",
    "matches",
]


class MemoryStore:
    def __init__(self) -> None:
        self._rules: list[Rule] = []
        self._lock = Lock()

    def add_rule(self, rule: Rule) -> Rule:
        with self._lock:
            self._rules.append(rule)
            return rule

    def list_rules(self) -> list[Rule]:
        with self._lock:
            return list(self._rules)

    def get_rule(self, rule_id: str) -> Rule | None:
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
