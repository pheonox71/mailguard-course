"""REFERENCE SOLUTION."""

from __future__ import annotations

from typing import Literal

CsfFunction = Literal["govern", "identify", "protect", "detect", "respond", "recover"]
LegacyPhase = Literal[
    "preparation",
    "detection",
    "analysis",
    "containment",
    "eradication",
    "recovery",
    "postincident",
]
Phase = CsfFunction


def csf_function_order() -> tuple[CsfFunction, ...]:
    return ("govern", "identify", "protect", "detect", "respond", "recover")


def phase_order() -> tuple[Phase, ...]:
    return csf_function_order()


def legacy_rev2_phases() -> tuple[str, ...]:
    return (
        "preparation",
        "detection_analysis",
        "containment_eradication_recovery",
        "postincident",
    )


def impossible_travel(prev_country: str, next_country: str, hours_apart: float) -> bool:
    return prev_country.strip().upper() != next_country.strip().upper() and hours_apart < 2


def postmortem_has_blameless_sections(text: str) -> bool:
    t = text.lower()
    return all(k in t for k in ("impact", "timeline", "actions"))
