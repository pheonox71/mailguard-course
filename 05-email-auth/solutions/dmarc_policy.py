"""REFERENCE SOLUTION — peek only if stuck. Not imported by tests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Alignment = Literal["r", "s"]
Policy = Literal["none", "quarantine", "reject"]
Psd = Literal["y", "n", "u"]

_POLICIES = {"none", "quarantine", "reject"}
_ALIGN = {"r", "s"}
_PSD = {"y", "n", "u"}
_TEST = {"y", "n"}


@dataclass(frozen=True, slots=True)
class DmarcPolicy:
    version: str
    policy: Policy
    subdomain_policy: Policy | None
    percentage: int
    test_mode: bool
    nonexistent_policy: Policy | None
    psd: Psd | None
    rua: tuple[str, ...]
    ruf: tuple[str, ...]
    adkim: Alignment
    aspf: Alignment


def parse_dmarc_record(txt: str) -> DmarcPolicy:
    if not txt or not txt.strip():
        raise ValueError("empty DMARC record")

    parts = [p.strip() for p in txt.split(";") if p.strip()]
    if not parts:
        raise ValueError("empty DMARC record")

    first_name, _, first_value = parts[0].partition("=")
    if first_name.strip().lower() != "v" or first_value.strip() != "DMARC1":
        raise ValueError("v=DMARC1 must be the first tag")

    tags: dict[str, str] = {}
    for part in parts:
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

    def optional_policy(key: str) -> Policy | None:
        raw = tags.get(key)
        if raw is None:
            return None
        value = raw.lower()
        if value not in _POLICIES:
            raise ValueError(f"{key} must be none|quarantine|reject")
        return value  # type: ignore[return-value]

    subdomain = optional_policy("sp")
    nonexistent = optional_policy("np")

    pct = 100
    if "pct" in tags:
        try:
            pct = int(tags["pct"])
        except ValueError as exc:
            raise ValueError("pct must be an integer") from exc
        if pct < 0 or pct > 100:
            raise ValueError("pct must be 0–100")

    t_raw = tags.get("t", "n").lower()
    if t_raw not in _TEST:
        raise ValueError("t must be y|n")
    test_mode = t_raw == "y"

    psd: Psd | None
    if "psd" not in tags:
        psd = None
    else:
        psd_raw = tags["psd"].lower()
        if psd_raw not in _PSD:
            raise ValueError("psd must be y|n|u")
        psd = psd_raw  # type: ignore[assignment]

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
        test_mode=test_mode,
        nonexistent_policy=nonexistent,
        psd=psd,
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
    if policy.test_mode:
        return f"{base} Test mode (t=y): receivers apply the next-weaker policy — modern partial rollout."
    if policy.percentage < 100:
        return f"{base} Partial rollout (legacy pct={policy.percentage})."
    return base
