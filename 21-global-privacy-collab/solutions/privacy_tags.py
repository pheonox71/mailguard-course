"""REFERENCE SOLUTION."""

from __future__ import annotations

REGIMES = {
    "GDPR": "EU/EEA personal data; lawful basis + transfer rules",
    "CCPA": "California consumer rights; CPRA expands",
    "APPI": "Japan Act on Protection of Personal Information",
    "LGPD": "Brazil general data protection law",
    "PIPL": "China personal information protection law",
}

_REGION = {"EU": "GDPR", "US-CA": "CCPA", "JP": "APPI", "BR": "LGPD", "CN": "PIPL"}


def lookup(regime: str) -> str:
    key = regime.strip().upper()
    if key == "CPRA":
        key = "CCPA"
    if key not in REGIMES:
        raise ValueError("unknown regime")
    return REGIMES[key]


def flags_for_regions(regions: list[str]) -> list[str]:
    out: list[str] = []
    for r in regions:
        code = _REGION.get(r.strip().upper())
        if code and code not in out:
            out.append(code)
    return out
