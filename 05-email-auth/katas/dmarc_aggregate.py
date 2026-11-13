"""Parse a tiny RFC 9990-shaped DMARC aggregate XML fixture → tables."""

from __future__ import annotations

from dataclasses import dataclass
from xml.etree import ElementTree as ET


@dataclass(frozen=True)
class SourceRow:
    source_ip: str
    count: int
    disposition: str
    dkim: str
    spf: str


def parse_aggregate(xml_text: str) -> list[SourceRow]:
    """Parse <record> rows from a compact aggregate report fixture."""
    raise NotImplementedError


def classify_source(row: SourceRow) -> str:
    """Return 'aligned' | 'legit_unaligned' | 'spoof' heuristics for the lab."""
    raise NotImplementedError


def next_policy_step(current: str) -> str:
    """none→quarantine→reject; reject stays reject. ValueError otherwise."""
    raise NotImplementedError
