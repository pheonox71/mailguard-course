"""REFERENCE SOLUTION."""

from __future__ import annotations

from typing import Literal

Mode = Literal["pull", "push"]


def classify_sync(tool: str) -> Mode:
    t = tool.strip().lower()
    if t in {"argo", "argocd", "flux"}:
        return "pull"
    if t in {"jenkins-kubectl", "push"}:
        return "push"
    raise ValueError("unknown tool")


def crossplane_claim_name(app: str, env: str) -> str:
    if not app.strip() or not env.strip():
        raise ValueError("required")
    return f"{app.strip().lower()}-{env.strip().lower()}-claim"
