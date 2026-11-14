"""Incident response triage helpers (NIST SP 800-61r3 / CSF 2.0 literacy)."""

from __future__ import annotations

from typing import Literal

# CSF 2.0 function names used by SP 800-61r3 (not the Rev. 2 four-phase labels).
CsfFunction = Literal["govern", "identify", "protect", "detect", "respond", "recover"]

# Historical Rev. 2 phase labels — still seen in older runbooks.
LegacyPhase = Literal[
    "preparation",
    "detection",
    "analysis",
    "containment",
    "eradication",
    "recovery",
    "postincident",
]

# Back-compat alias for tests/quizzes that still say "Phase".
Phase = CsfFunction


def csf_function_order() -> tuple[CsfFunction, ...]:
    """Return CSF 2.0 functions in the order SP 800-61r3 profiles IR work."""
    raise NotImplementedError


def phase_order() -> tuple[Phase, ...]:
    """Alias of csf_function_order (r3 uses CSF functions, not Rev. 2 phases)."""
    raise NotImplementedError


def legacy_rev2_phases() -> tuple[str, ...]:
    """Historical Rev. 2 lifecycle labels (for literacy only)."""
    raise NotImplementedError


def impossible_travel(prev_country: str, next_country: str, hours_apart: float) -> bool:
    """Lab heuristic: different countries and hours_apart < 2 → flag."""
    raise NotImplementedError


def postmortem_has_blameless_sections(text: str) -> bool:
    """True if English postmortem mentions impact, timeline, and actions."""
    raise NotImplementedError
