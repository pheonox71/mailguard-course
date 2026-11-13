"""Tiny CI hygiene helpers."""

from __future__ import annotations

FORBIDDEN_PATTERNS = (
    "AWS_SECRET_ACCESS_KEY",
    "BEGIN RSA PRIVATE KEY",
    "ghp_",
)


def finds_forbidden_secret(text: str) -> bool:
    raise NotImplementedError


def requires_test_job(job_names: list[str]) -> bool:
    """True if any job name contains 'test' (case-insensitive)."""
    raise NotImplementedError
