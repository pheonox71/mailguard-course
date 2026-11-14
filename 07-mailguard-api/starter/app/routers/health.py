"""Liveness / readiness for local demos, Compose, and Kubernetes probes.

Split paths so readiness can fail independently of liveness (Module 14):
- ``/readyz`` — Service traffic gate (dependencies OK)
- ``/livez`` — process alive (restart if stuck)
- ``/healthz`` — kept for Compose / simple demos (same as ready for now)
"""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/readyz")
def readyz() -> dict[str, str]:
    # Stretch: fail when DB/queue clients from lifespan are unavailable.
    return {"status": "ready"}


@router.get("/livez")
def livez() -> dict[str, str]:
    return {"status": "alive"}
