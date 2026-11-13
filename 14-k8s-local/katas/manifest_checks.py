"""Validate that a Deployment-like dict has probes and requests."""

from __future__ import annotations

from typing import Any


def has_probes(deployment: dict[str, Any]) -> bool:
    raise NotImplementedError


def has_requests(deployment: dict[str, Any]) -> bool:
    raise NotImplementedError
