"""REFERENCE SOLUTION."""

from __future__ import annotations

FORBIDDEN = {"AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"}


def role_trust_ok(sub: str, *, repo: str, ref_prefix: str = "refs/heads/") -> bool:
    prefix = f"repo:{repo}:ref:"
    if not sub.startswith(prefix):
        return False
    ref = sub[len(prefix) :]
    return ref.startswith(ref_prefix)


def forbids_static_aws_keys(env_names: list[str]) -> bool:
    return not any(n in FORBIDDEN for n in env_names)


def ecs_service_name(project: str, env: str) -> str:
    if not project.strip() or not env.strip():
        raise ValueError("project and env required")
    return f"{project.strip().lower()}-{env.strip().lower()}-svc"
