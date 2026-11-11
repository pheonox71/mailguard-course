"""DMARC policy kata — parse a Domain-based Message Authentication Reporting
and Conformance (DMARC) DNS TXT record into structured fields.

Literacy drill: understand p=, rua=, ruf=, adkim=, aspf= — do not talk to live
DNS from tests. Implement the stubs. Read worksheets/dmarc_policy.md and
tests/test_dmarc_policy.py before coding. Peek at solutions/ only if stuck.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Alignment = Literal["r", "s"]  # relaxed | strict
Policy = Literal["none", "quarantine", "reject"]


@dataclass(frozen=True, slots=True)
class DmarcPolicy:
    version: str
    policy: Policy
    subdomain_policy: Policy | None
    percentage: int
    rua: tuple[str, ...]
    ruf: tuple[str, ...]
    adkim: Alignment
    aspf: Alignment


def parse_dmarc_record(txt: str) -> DmarcPolicy:
    """Parse a DMARC TXT value (e.g. 'v=DMARC1; p=reject; rua=mailto:a@b').

    Rules for this kata:
    - Require `v=DMARC1` (case-insensitive tag names; version value exact DMARC1).
    - Require `p` in {none, quarantine, reject}.
    - Optional `sp` same enum; default None if absent.
    - Optional `pct` integer 0–100; default 100 if absent.
    - Optional `rua` / `ruf`: comma-separated URIs → tuples (strip whitespace).
    - Optional `adkim` / `aspf`: `r` or `s`; default `r` if absent.
    - Ignore unknown tags.
    - Raise ValueError on missing v/p, bad enums, bad pct, or empty input.
    """
    raise NotImplementedError("implement parse_dmarc_record — see worksheets/dmarc_policy.md")


def explains_spoofing_gap(policy: DmarcPolicy) -> str:
    """One short coaching string for operators.

    - p=none → monitoring only; spoofed mail can still inbox.
    - p=quarantine → many receivers junk/spam spoofed mail.
    - p=reject → receivers should reject failing mail.
    Mention if pct < 100 that rollout is partial.
    """
    raise NotImplementedError("implement explains_spoofing_gap — see worksheets/dmarc_policy.md")
