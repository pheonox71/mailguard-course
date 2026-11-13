"""REFERENCE SOLUTION."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ActionKind = Literal["allow", "hold", "reject", "auto_bcc", "delete"]


@dataclass(frozen=True)
class RuleAction:
    kind: ActionKind
    bcc: str | None = None


_KINDS = {"allow", "hold", "reject", "auto_bcc", "delete"}


def normalize_action(kind: str, bcc: str | None = None) -> RuleAction:
    k = kind.strip().lower()
    if k not in _KINDS:
        raise ValueError("unknown action")
    if k == "auto_bcc":
        if not bcc or "@" not in bcc:
            raise ValueError("auto_bcc requires bcc address")
        return RuleAction("auto_bcc", bcc=bcc.strip())
    return RuleAction(k)  # type: ignore[arg-type]


def describe(action: RuleAction) -> str:
    if action.kind == "auto_bcc":
        return f"auto-bcc to {action.bcc}"
    if action.kind == "delete":
        return "delete matching messages"
    return action.kind
