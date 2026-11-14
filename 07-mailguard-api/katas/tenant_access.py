"""Tenant-scoped hold GET.

Implement `get_hold` so cross-tenant reads fail closed (prefer 404 to avoid id oracles).
"""

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
    """Return (status, hold).

    - Missing hold → 404
    - Cross-tenant → 404 when prefer_404 else 403
    - Same tenant → 200 with the record
    """
    raise NotImplementedError
