"""REFERENCE SOLUTION."""

from __future__ import annotations

import re

FORBIDDEN = {"AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"}

# repo:ORG/REPO:ref:...  OR  repo:ORG@123/REPO@456:ref:...
_SUB_RE = re.compile(
    r"^repo:(?P<owner>[^/:@]+)(?:@(?P<owner_id>\d+))?/"
    r"(?P<name>[^/:@]+)(?:@(?P<repo_id>\d+))?:"
    r"(?P<claim>.+)$"
)


def role_trust_ok(
    sub: str,
    *,
    repo: str,
    ref_prefix: str = "refs/heads/",
    owner_id: str | None = None,
    repo_id: str | None = None,
) -> bool:
    m = _SUB_RE.match(sub)
    if not m:
        return False
    want_owner, _, want_name = repo.partition("/")
    if not want_owner or not want_name:
        return False
    if m.group("owner") != want_owner or m.group("name") != want_name:
        return False

    has_ids = m.group("owner_id") is not None or m.group("repo_id") is not None
    if has_ids:
        # Immutable form requires both IDs.
        if m.group("owner_id") is None or m.group("repo_id") is None:
            return False
        if owner_id is not None and m.group("owner_id") != str(owner_id):
            return False
        if repo_id is not None and m.group("repo_id") != str(repo_id):
            return False
    elif owner_id is not None or repo_id is not None:
        # Caller asked for ID-pinned trust; name-only subjects do not match.
        return False

    claim = m.group("claim")
    if not claim.startswith("ref:"):
        return False
    ref = claim[len("ref:") :]
    return ref.startswith(ref_prefix)


def forbids_static_aws_keys(env_names: list[str]) -> bool:
    return not any(n in FORBIDDEN for n in env_names)


def ecs_service_name(project: str, env: str) -> str:
    if not project.strip() or not env.strip():
        raise ValueError("project and env required")
    return f"{project.strip().lower()}-{env.strip().lower()}-svc"
