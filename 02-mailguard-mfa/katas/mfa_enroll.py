"""TOTP enroll / verify + one-time recovery codes."""

from __future__ import annotations

import secrets
from dataclasses import dataclass, field


@dataclass
class Enrollment:
    secret: str
    recovery_codes: list[str] = field(default_factory=list)
    used_recovery: set[str] = field(default_factory=set)


def enroll(*, recovery_count: int = 5) -> Enrollment:
    """Create a base32 secret and one-time recovery codes."""
    raise NotImplementedError


def verify_totp(enrollment: Enrollment, code: str, *, for_time: int | None = None) -> bool:
    """Verify a TOTP code for the enrollment secret."""
    raise NotImplementedError


def consume_recovery(enrollment: Enrollment, code: str) -> bool:
    """Return True once if code is an unused recovery code."""
    raise NotImplementedError
