"""TOTP enroll / verify + one-time recovery codes.

Replay: after a successful verify, reject that time-step and any older
step (``step <= last_used_step``) — RFC 6238 §5.2. Equality-only checks
leave a clock-skew window hole. Throttle: lock after too many failures
(NIST SP 800-63B authenticator throttling).
"""

from __future__ import annotations

import secrets
from dataclasses import dataclass, field

# Max failed verify_totp attempts before lockout (lab throttle).
MAX_FAILED_ATTEMPTS = 5


@dataclass
class Enrollment:
    secret: str
    recovery_codes: list[str] = field(default_factory=list)
    used_recovery: set[str] = field(default_factory=set)
    last_used_step: int | None = None
    failed_attempts: int = 0
    locked: bool = False


def enroll(*, recovery_count: int = 5) -> Enrollment:
    """Create a base32 secret and one-time recovery codes."""
    raise NotImplementedError


def verify_totp(enrollment: Enrollment, code: str, *, for_time: int | None = None) -> bool:
    """Verify a TOTP code for the enrollment secret.

    Rejects when locked, when the matching step is ``<= last_used_step``
    (replay / older step in the skew window), or when the code is wrong
    (and increments failure count).
    """
    raise NotImplementedError


def consume_recovery(enrollment: Enrollment, code: str) -> bool:
    """Return True once if code is an unused recovery code."""
    raise NotImplementedError
