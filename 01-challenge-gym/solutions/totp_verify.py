"""REFERENCE SOLUTION — peek only if stuck. Not imported by tests.

TOTP verify kata — understand MFA/OTP without reinventing crypto.
Uses pyotp (RFC 6238). Challenge-style: validate a code against a shared
secret with a small time-step window; reject malformed input early.
"""

from __future__ import annotations

import re

import pyotp

_CODE = re.compile(r"^\d{6}$")


def verify_totp(
    secret: str,
    code: str,
    *,
    for_time: float | None = None,
    window: int = 1,
) -> bool:
    """Return True if `code` is a valid TOTP for `secret`.

    - `secret`: base32 shared secret (Google Authenticator–style).
    - `code`: six-digit user-entered OTP.
    - `for_time`: unix seconds to evaluate (default: now). Useful in tests.
    - `window`: steps to tolerate clock skew (±window * 30s). Must be >= 0.
    """
    if window < 0:
        raise ValueError("window must be >= 0")
    if not secret or not _CODE.match(code.strip()):
        return False

    totp = pyotp.TOTP(secret)
    return totp.verify(code.strip(), for_time=for_time, valid_window=window)


def current_code(secret: str, *, for_time: float | None = None) -> str:
    """Generate the current TOTP for demos and tests (not a production API)."""
    totp = pyotp.TOTP(secret)
    return totp.at(for_time) if for_time is not None else totp.now()
