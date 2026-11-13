"""Joiner / mover / leaver risk helpers."""

from __future__ import annotations

from typing import Literal

Event = Literal["join", "move", "leave"]


def deprovision_priority(event: Event) -> int:
    """Higher means more urgent. leave > move > join."""
    raise NotImplementedError


def stale_access_risk(hours_since_leave: float, *, sla_hours: float = 24.0) -> str:
    """Return 'ok' | 'elevated' | 'critical' based on SLA breach."""
    raise NotImplementedError
