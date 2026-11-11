"""REFERENCE SOLUTION — peek only if stuck. Not imported by tests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Alignment = Literal["r", "s"]
Policy = Literal["none", "quarantine", "reject"]

_POLICIES = {"none", "quarantine", "reject"}
_ALIGN = {"r", "s"}


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
    if not txt or not txt.strip():
        raise ValueError("empty DMARC record")

    tags: dict[str, str] = {}
    for part in txt.split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"malformed tag: {part!r}")
        name, value = part.split("=", 1)
        tags[name.strip().lower()] = value.strip()

    version = tags.get("v")
    if version != "DMARC1":
        raise ValueError("v=DMARC1 required")

    policy = tags.get("p", "").lower()
    if policy not in _POLICIES:
        raise ValueError("p must be none|quarantine|reject")

    sp_raw = tags.get("sp")
    subdomain: Policy | None
    if sp_raw is None:
        subdomain = None
    else:
        sp = sp_raw.lower()
        if sp not in _POLICIES:
            raise ValueError("sp must be none|quarantine|reject")
        subdomain = sp  # type: ignore[assignment]

    pct = 100
    if "pct" in tags:
        try:
            pct = int(tags["pct"])
        except ValueError as exc:
            raise ValueError("pct must be an integer") from exc
        if pct < 0 or pct > 100:
            raise ValueError("pct must be 0–100")

    def uris(key: str) -> tuple[str, ...]:
        raw = tags.get(key)
        if not raw:
            return ()
        return tuple(u.strip() for u in raw.split(",") if u.strip())

    adkim = tags.get("adkim", "r").lower()
    aspf = tags.get("aspf", "r").lower()
    if adkim not in _ALIGN or aspf not in _ALIGN:
        raise ValueError("adkim/aspf must be r|s")

    return DmarcPolicy(
        version="DMARC1",
        policy=policy,  # type: ignore[arg-type]
        subdomain_policy=subdomain,
        percentage=pct,
        rua=uris("rua"),
        ruf=uris("ruf"),
        adkim=adkim,  # type: ignore[arg-type]
        aspf=aspf,  # type: ignore[arg-type]
    )


def explains_spoofing_gap(policy: DmarcPolicy) -> str:
    base = {
        "none": "p=none is monitoring only — spoofed mail can still reach inboxes.",
        "quarantine": "p=quarantine asks receivers to junk/spam failing mail.",
        "reject": "p=reject asks receivers to reject failing mail.",
    }[policy.policy]
    if policy.percentage < 100:
        return f"{base} Partial rollout: pct={policy.percentage}."
    return base
