from __future__ import annotations
from typing import Any

def _containers(deployment: dict[str, Any]) -> list[dict[str, Any]]:
    return deployment.get("spec", {}).get("template", {}).get("spec", {}).get("containers", []) or []

def has_probes(deployment: dict[str, Any]) -> bool:
    for c in _containers(deployment):
        if "readinessProbe" in c and "livenessProbe" in c:
            return True
    return False

def has_requests(deployment: dict[str, Any]) -> bool:
    for c in _containers(deployment):
        req = c.get("resources", {}).get("requests") or {}
        if req.get("cpu") and req.get("memory"):
            return True
    return False
