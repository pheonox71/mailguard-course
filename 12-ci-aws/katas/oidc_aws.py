"""GitHub Actions OIDC → AWS role assumptions (no long-lived keys)."""

from __future__ import annotations


def role_trust_ok(
    sub: str,
    *,
    repo: str,
    ref_prefix: str = "refs/heads/",
    owner_id: str | None = None,
    repo_id: str | None = None,
) -> bool:
    """True if JWT ``sub`` matches the repo and a ref under ``ref_prefix``.

    Accept either subject form GitHub may mint:

    - Name-based: ``repo:<owner>/<name>:ref:<ref>``
    - Immutable IDs: ``repo:<owner>@<owner_id>/<name>@<repo_id>:ref:<ref>``

    When ``owner_id`` / ``repo_id`` are provided, the immutable form must use
    those IDs. When omitted, any numeric IDs in an ``ORG@id/REPO@id`` subject
    are accepted as long as the name parts match ``repo``.
    """
    raise NotImplementedError


def forbids_static_aws_keys(env_names: list[str]) -> bool:
    """True if env list does NOT include classic static AWS key var names."""
    raise NotImplementedError


def ecs_service_name(project: str, env: str) -> str:
    """Return '{project}-{env}-svc' lowercase; raise on empty parts."""
    raise NotImplementedError
