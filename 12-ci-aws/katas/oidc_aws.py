"""GitHub Actions OIDC → AWS role assumptions (no long-lived keys)."""

from __future__ import annotations


def role_trust_ok(sub: str, *, repo: str, ref_prefix: str = "refs/heads/") -> bool:
    """True if JWT `sub` matches repo and a branch/tag ref under ref_prefix.

    Expected shape: repo:<owner>/<name>:ref:<ref>
    """
    raise NotImplementedError


def forbids_static_aws_keys(env_names: list[str]) -> bool:
    """True if env list does NOT include classic static AWS key var names."""
    raise NotImplementedError


def ecs_service_name(project: str, env: str) -> str:
    """Return '{project}-{env}-svc' lowercase; raise on empty parts."""
    raise NotImplementedError
