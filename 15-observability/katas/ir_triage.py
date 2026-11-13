"""Incident response triage helpers (NIST SP 800-61r3 literacy)."""

from __future__ import annotations

from typing import Literal

Phase = Literal["preparation", "detection", "analysis", "containment", "eradication", "recovery", "postincident"]


def phase_order() -> tuple[Phase, ...]:
    raise NotImplementedError


def impossible_travel(prev_country: str, next_country: str, hours_apart: float) -> bool:
    """Lab heuristic: different countries and hours_apart < 2 → flag."""
    raise NotImplementedError


def postmortem_has_blameless_sections(text: str) -> bool:
    """True if English postmortem mentions impact, timeline, and actions."""
    raise NotImplementedError
