"""REFERENCE SOLUTION."""

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
    root = ET.fromstring(xml_text)
    rows: list[SourceRow] = []
    for rec in root.findall("record"):
        row = SourceRow(
            source_ip=rec.findtext("row/source_ip", default=""),
            count=int(rec.findtext("row/count", default="0")),
            disposition=rec.findtext("row/policy_evaluated/disposition", default=""),
            dkim=rec.findtext("row/policy_evaluated/dkim", default=""),
            spf=rec.findtext("row/policy_evaluated/spf", default=""),
        )
        rows.append(row)
    return rows


def classify_source(row: SourceRow) -> str:
    if row.dkim == "pass" or row.spf == "pass":
        return "aligned"
    if row.disposition == "none" and row.count > 0:
        return "legit_unaligned"
    return "spoof"


def next_policy_step(current: str) -> str:
    order = ["none", "quarantine", "reject"]
    if current not in order:
        raise ValueError("bad policy")
    i = order.index(current)
    return order[min(i + 1, len(order) - 1)]
