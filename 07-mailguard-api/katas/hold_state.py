"""Hold → approve → release state machine for an email-gateway queue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

State = Literal["held", "approved", "released", "rejected"]
Action = Literal["approve", "release", "reject"]


@dataclass
class HoldItem:
    id: str
    state: State


def apply_action(item: HoldItem, action: Action) -> HoldItem:
    """Apply a legal transition; raise ValueError on illegal moves.

    Legal: held→approved (approve), held→rejected (reject),
    approved→released (release), approved→rejected (reject).
    """
    raise NotImplementedError


def can_release(item: HoldItem) -> bool:
    """True only when state is approved."""
    raise NotImplementedError
