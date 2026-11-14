"""REFERENCE SOLUTION — tenant-scoped hold GET."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HoldRecord:
    id: str
    tenant_id: str
    state: str = "held"


def get_hold(
    holds: dict[str, HoldRecord],
    hold_id: str,
    caller_tenant: str,
    *,
    prefer_404: bool = True,
) -> tuple[int, HoldRecord | None]:
    hold = holds.get(hold_id)
    if hold is None:
        return 404, None
    if hold.tenant_id != caller_tenant:
        return (404 if prefer_404 else 403), None
    return 200, hold
