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

def active_false_kill_checklist() -> list[str]:
    # Why this order: contain interactive access first, then long-lived secrets, then caches/grants.
    return [
        "revoke_sessions",
        "revoke_refresh_and_api_tokens",
        "invalidate_auth_caches",
        "drop_roles_forwards_and_grants",
    ]
