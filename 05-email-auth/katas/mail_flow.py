"""Cloud mailbox + gateway routing literacy helpers."""

from __future__ import annotations

from typing import Literal

Hop = Literal["mx_inbound", "outbound_smarthost", "journal"]


def spf_after_gateway(gateway_rewrites_mail_from: bool) -> str:
    """Return 'likely_fail' or 'unchanged' for SPF at final receiver."""
    raise NotImplementedError


def dmarc_may_still_pass(dkim_survives: bool) -> bool:
    """DMARC can pass on DKIM alignment even when SPF fails."""
    raise NotImplementedError


def arc_needed(intermediate_hops: int) -> bool:
    """True when intermediate hops >= 1 (lab heuristic)."""
    raise NotImplementedError
