from __future__ import annotations

def availability(success: int, total: int) -> float:
    if total <= 0:
        raise ValueError("total")
    return success / total

def error_budget_remaining(*, slo: float, availability: float, window_events: int) -> float:
    allowed_fail_frac = 1.0 - slo
    used_fail_frac = 1.0 - availability
    return (allowed_fail_frac - used_fail_frac) * window_events
