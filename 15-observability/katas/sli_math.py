"""Tiny SLI / error-budget helpers."""

from __future__ import annotations

def availability(success: int, total: int) -> float:
    raise NotImplementedError

def error_budget_remaining(*, slo: float, availability: float, window_events: int) -> float:
    """Return remaining error budget as event count (can be negative)."""
    raise NotImplementedError
