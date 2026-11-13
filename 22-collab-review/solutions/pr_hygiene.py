"""REFERENCE SOLUTION."""

from __future__ import annotations

import re

_CONV = re.compile(
    r"^(feat|fix|docs|chore|refactor|test|ci)(\(.+\))?:\s+\S+"
)


def conventional_commit_ok(subject: str) -> bool:
    return bool(_CONV.match(subject.strip()))


def pr_too_large(files_changed: int, *, max_files: int = 25) -> bool:
    return files_changed > max_files


def flags_secret_path(path: str) -> bool:
    name = path.rsplit("/", 1)[-1].lower()
    if name == ".env" or name == "id_rsa":
        return True
    return name.endswith(".pem") or name.endswith(".p12")
