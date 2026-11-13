from __future__ import annotations

import secrets
from dataclasses import dataclass, field

import pyotp


@dataclass
class Enrollment:
    secret: str
    recovery_codes: list[str] = field(default_factory=list)
    used_recovery: set[str] = field(default_factory=set)


def enroll(*, recovery_count: int = 5) -> Enrollment:
    secret = pyotp.random_base32()
    codes = [secrets.token_hex(4) for _ in range(recovery_count)]
    return Enrollment(secret=secret, recovery_codes=codes)


def verify_totp(enrollment: Enrollment, code: str, *, for_time: int | None = None) -> bool:
    totp = pyotp.TOTP(enrollment.secret)
    if for_time is None:
        return bool(totp.verify(code, valid_window=1))
    return totp.at(for_time) == code


def consume_recovery(enrollment: Enrollment, code: str) -> bool:
    if code not in enrollment.recovery_codes or code in enrollment.used_recovery:
        return False
    enrollment.used_recovery.add(code)
    return True
