"""Simple in-memory persistence for the starter API.

Reuse the rules engine (Rule/Message + matches/evaluate) so HTTP routes do not
fork first-match-wins semantics. MemoryStore adds a lock for concurrent demos.
Swap this for Postgres in a stretch lab — keep the evaluate path pure.
"""

from __future__ import annotations

from threading import Lock

from solutions.rules_engine import Decision, Message, Rule, evaluate, matches

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
