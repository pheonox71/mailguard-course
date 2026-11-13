"""Tiny PR hygiene helpers."""

from __future__ import annotations


def conventional_commit_ok(subject: str) -> bool:
    """True if subject matches type: summary with known type prefix."""
    raise NotImplementedError


def pr_too_large(files_changed: int, *, max_files: int = 25) -> bool:
    raise NotImplementedError


def flags_secret_path(path: str) -> bool:
    """True for obvious secret filenames (.env, id_rsa, *.pem)."""
    raise NotImplementedError
