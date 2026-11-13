"""REFERENCE SOLUTION."""

from __future__ import annotations

from typing import Literal

Phase = Literal["preparation", "detection", "analysis", "containment", "eradication", "recovery", "postincident"]


def phase_order() -> tuple[Phase, ...]:
    return (
        "preparation",
        "detection",
        "analysis",
        "containment",
        "eradication",
        "recovery",
        "postincident",
    )


def impossible_travel(prev_country: str, next_country: str, hours_apart: float) -> bool:
    return prev_country.strip().upper() != next_country.strip().upper() and hours_apart < 2


def postmortem_has_blameless_sections(text: str) -> bool:
    t = text.lower()
    return all(k in t for k in ("impact", "timeline", "actions"))
