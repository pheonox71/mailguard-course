"""DMARC policy kata — parse a Domain-based Message Authentication Reporting
and Conformance (DMARC) DNS TXT record into structured fields.

Literacy drill: understand p=, rua=, ruf=, adkim=, aspf=, plus RFC 9989 tags
t=, np=, psd= (and legacy pct=). Do not talk to live DNS from tests. Implement
the stubs. Read assignments/dmarc_policy.md and tests/test_dmarc_policy.py
before coding. Peek at solutions/ only if stuck.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Alignment = Literal["r", "s"]  # relaxed | strict
Policy = Literal["none", "quarantine", "reject"]
Psd = Literal["y", "n", "u"]


@dataclass(frozen=True, slots=True)
class DmarcPolicy:
    version: str
    policy: Policy
    subdomain_policy: Policy | None
    percentage: int  # legacy pct= (removed in RFC 9989; still parse when present)
    test_mode: bool  # t=y (RFC 9989)
    nonexistent_policy: Policy | None  # np= (RFC 9989)
    psd: Psd | None  # psd= (RFC 9989)
    rua: tuple[str, ...]
    ruf: tuple[str, ...]
    adkim: Alignment
    aspf: Alignment


def parse_dmarc_record(txt: str) -> DmarcPolicy:
    """Parse a DMARC TXT value (e.g. 'v=DMARC1; p=reject; rua=mailto:a@b').

    Rules for this kata (RFC 9989-shaped, with legacy pct tolerance):
    - `v=DMARC1` MUST be the first tag; otherwise discard (ValueError).
    - Require `v=DMARC1` (case-insensitive tag names; version value exact DMARC1).
    - Require `p` in {none, quarantine, reject}.
    - Optional `sp` same enum; default None if absent.
    - Optional legacy `pct` integer 0–100; default 100 if absent (removed in RFC 9989).
    - Optional `t` in {y, n}; default n → test_mode False. t=y is test mode.
    - Optional `np` same enum as p; default None if absent.
    - Optional `psd` in {y, n, u}; default None if absent.
    - Optional `rua` / `ruf`: comma-separated URIs → tuples (strip whitespace).
    - Optional `adkim` / `aspf`: `r` or `s`; default `r` if absent.
    - Ignore unknown tags.
    - Raise ValueError on missing v/p, bad enums, bad pct/t/psd, or empty input.
    """
    raise NotImplementedError("implement parse_dmarc_record — see assignments/dmarc_policy.md")


def explains_spoofing_gap(policy: DmarcPolicy) -> str:
    """One short coaching string for operators.

    - p=none → monitoring only; spoofed mail can still inbox.
    - p=quarantine → many receivers junk/spam spoofed mail.
    - p=reject → receivers should reject failing mail.
    - If test_mode (t=y): mention modern partial-rollout / next-weaker policy.
    - Else if legacy pct < 100: mention partial rollout via pct.
    """
    raise NotImplementedError("implement explains_spoofing_gap — see assignments/dmarc_policy.md")
