"""REFERENCE SOLUTION."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Literal

State = Literal["held", "approved", "released", "rejected"]
Action = Literal["approve", "release", "reject"]


@dataclass
class HoldItem:
    id: str
    state: State


_TRANSITIONS: dict[tuple[State, Action], State] = {
    ("held", "approve"): "approved",
    ("held", "reject"): "rejected",
    ("approved", "release"): "released",
    ("approved", "reject"): "rejected",
}


def apply_action(item: HoldItem, action: Action) -> HoldItem:
    key = (item.state, action)
    if key not in _TRANSITIONS:
        raise ValueError(f"illegal {action} from {item.state}")
    return replace(item, state=_TRANSITIONS[key])


def can_release(item: HoldItem) -> bool:
    return item.state == "approved"
