"""REFERENCE SOLUTION."""

from __future__ import annotations


def has_resources(containers: list[dict]) -> bool:
    for c in containers:
        req = (c.get("resources") or {}).get("requests") or {}
        if "cpu" not in req or "memory" not in req:
            return False
    return bool(containers)


def has_probes(containers: list[dict]) -> bool:
    return bool(containers) and all("readinessProbe" in c for c in containers)
