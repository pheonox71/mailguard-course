from __future__ import annotations
from typing import Any

def is_deployable(deployment: dict[str, Any]) -> bool:
    containers = deployment.get("spec", {}).get("template", {}).get("spec", {}).get("containers", []) or []
    for c in containers:
        if "readinessProbe" not in c or "livenessProbe" not in c:
            return False
        req = c.get("resources", {}).get("requests") or {}
        if not (req.get("cpu") and req.get("memory")):
            return False
        return True
    return False
