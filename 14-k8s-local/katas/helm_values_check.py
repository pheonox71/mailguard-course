"""Basic Helm/Kustomize hygiene checks for local manifests."""

from __future__ import annotations


def has_resources(containers: list[dict]) -> bool:
    """True if every container has requests.cpu and requests.memory."""
    raise NotImplementedError


def has_probes(containers: list[dict]) -> bool:
    """True if every container defines readinessProbe."""
    raise NotImplementedError
