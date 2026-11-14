"""Validate that a Deployment-like dict has probes, requests, and non-root context."""

from __future__ import annotations

from typing import Any


def has_probes(deployment: dict[str, Any]) -> bool:
    raise NotImplementedError


def has_requests(deployment: dict[str, Any]) -> bool:
    raise NotImplementedError


def has_run_as_non_root(deployment: dict[str, Any]) -> bool:
    """True if pod or every container sets securityContext.runAsNonRoot."""
    raise NotImplementedError


def probes_are_split(deployment: dict[str, Any]) -> bool:
    """True when readiness and liveness httpGet paths differ (e.g. /readyz vs /livez)."""
    raise NotImplementedError
