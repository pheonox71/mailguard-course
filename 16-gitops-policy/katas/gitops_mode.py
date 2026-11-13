"""GitOps literacy: pull vs push; Crossplane claim naming."""

from __future__ import annotations

from typing import Literal

Mode = Literal["pull", "push"]


def classify_sync(tool: str) -> Mode:
    """argo/flux → pull; jenkins-kubectl → push. ValueError otherwise."""
    raise NotImplementedError


def crossplane_claim_name(app: str, env: str) -> str:
    """Return '{app}-{env}-claim' lowercase."""
    raise NotImplementedError
