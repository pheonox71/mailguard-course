"""REFERENCE SOLUTION."""

from __future__ import annotations

from typing import Literal

Event = Literal["join", "move", "leave"]

def deprovision_priority(event: Event) -> int:
    return {"join": 1, "move": 2, "leave": 3}[event]

def stale_access_risk(hours_since_leave: float, *, sla_hours: float = 24.0) -> str:
    if hours_since_leave <= sla_hours:
        return "ok"
    if hours_since_leave <= sla_hours * 2:
        return "elevated"
    return "critical"
