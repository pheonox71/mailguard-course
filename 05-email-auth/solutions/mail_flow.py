"""REFERENCE SOLUTION."""

from __future__ import annotations

def spf_after_gateway(gateway_rewrites_mail_from: bool) -> str:
    return "likely_fail" if gateway_rewrites_mail_from else "unchanged"

def dmarc_may_still_pass(dkim_survives: bool) -> bool:
    return dkim_survives

def arc_needed(intermediate_hops: int) -> bool:
    return intermediate_hops >= 1
