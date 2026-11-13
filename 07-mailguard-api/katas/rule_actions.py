"""Rule actions beyond hold/allow/reject: auto-bcc and delete-on-condition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ActionKind = Literal["allow", "hold", "reject", "auto_bcc", "delete"]


@dataclass(frozen=True)
class RuleAction:
    kind: ActionKind
    bcc: str | None = None  # required when kind == auto_bcc


def normalize_action(kind: str, bcc: str | None = None) -> RuleAction:
    """Validate and return RuleAction. Raise ValueError on bad input."""
    raise NotImplementedError


def describe(action: RuleAction) -> str:
    """One-line operator description."""
    raise NotImplementedError
