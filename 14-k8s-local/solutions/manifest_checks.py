from __future__ import annotations
from typing import Any

def _containers(deployment: dict[str, Any]) -> list[dict[str, Any]]:
    return deployment.get("spec", {}).get("template", {}).get("spec", {}).get("containers", []) or []

def _pod_spec(deployment: dict[str, Any]) -> dict[str, Any]:
    return deployment.get("spec", {}).get("template", {}).get("spec", {}) or {}

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

def has_run_as_non_root(deployment: dict[str, Any]) -> bool:
    pod_sc = _pod_spec(deployment).get("securityContext") or {}
    if pod_sc.get("runAsNonRoot") is True:
        return True
    containers = _containers(deployment)
    if not containers:
        return False
    return all((c.get("securityContext") or {}).get("runAsNonRoot") is True for c in containers)

def probes_are_split(deployment: dict[str, Any]) -> bool:
    for c in _containers(deployment):
        ready = ((c.get("readinessProbe") or {}).get("httpGet") or {}).get("path")
        live = ((c.get("livenessProbe") or {}).get("httpGet") or {}).get("path")
        if ready and live and ready != live:
            return True
    return False
