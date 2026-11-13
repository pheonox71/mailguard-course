"""Tag held-message handling with privacy-regime reminders (literacy)."""

from __future__ import annotations

REGIMES = {
    "GDPR": "EU/EEA personal data; lawful basis + transfer rules",
    "CCPA": "California consumer rights; CPRA expands",
    "APPI": "Japan Act on Protection of Personal Information",
    "LGPD": "Brazil general data protection law",
    "PIPL": "China personal information protection law",
}


def lookup(regime: str) -> str:
    """Return blurb; raise ValueError if unknown."""
    raise NotImplementedError


def flags_for_regions(regions: list[str]) -> list[str]:
    """Map region codes EU|US-CA|JP|BR|CN to regime codes; skip unknown."""
    raise NotImplementedError
