"""REFERENCE SOLUTION — TOTP enroll / verify + recovery + replay/throttle."""

from __future__ import annotations

import secrets
import time
from dataclasses import dataclass, field

import pyotp

MAX_FAILED_ATTEMPTS = 5
_VALID_WINDOW = 1


@dataclass
class Enrollment:
    secret: str
    recovery_codes: list[str] = field(default_factory=list)
    used_recovery: set[str] = field(default_factory=set)
    last_used_step: int | None = None
    failed_attempts: int = 0
    locked: bool = False


def enroll(*, recovery_count: int = 5) -> Enrollment:
    secret = pyotp.random_base32()
    codes = [secrets.token_hex(4) for _ in range(recovery_count)]
    return Enrollment(secret=secret, recovery_codes=codes)


def _matching_step(totp: pyotp.TOTP, code: str, unix_time: int) -> int | None:
    """Return the time-step index that produced ``code``, or None."""
    step = unix_time // totp.interval
    for offset in range(-_VALID_WINDOW, _VALID_WINDOW + 1):
        candidate = step + offset
        if totp.at(candidate * totp.interval) == code:
            return candidate
    return None


def verify_totp(enrollment: Enrollment, code: str, *, for_time: int | None = None) -> bool:
    if enrollment.locked:
        return False

    totp = pyotp.TOTP(enrollment.secret)
    unix_time = int(time.time()) if for_time is None else for_time

    if for_time is not None:
        # Exact-step path used by tests that pin wall-clock.
        if totp.at(for_time) != code:
            enrollment.failed_attempts += 1
            if enrollment.failed_attempts >= MAX_FAILED_ATTEMPTS:
                enrollment.locked = True
            return False
        step = for_time // totp.interval
    else:
        step = _matching_step(totp, code, unix_time)
        if step is None:
            enrollment.failed_attempts += 1
            if enrollment.failed_attempts >= MAX_FAILED_ATTEMPTS:
                enrollment.locked = True
            return False

    # RFC 6238 §5.2 — do not accept the same OTP/step after a successful verify.
    if enrollment.last_used_step is not None and step == enrollment.last_used_step:
        return False

    enrollment.last_used_step = step
    enrollment.failed_attempts = 0
    return True


def consume_recovery(enrollment: Enrollment, code: str) -> bool:
    if code not in enrollment.recovery_codes or code in enrollment.used_recovery:
        return False
    enrollment.used_recovery.add(code)
    return True
