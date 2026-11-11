"""TOTP verify kata — understand MFA/OTP without reinventing crypto.

Uses pyotp (RFC 6238). Challenge-style: validate a code against a shared
secret with a small time-step window; reject malformed input early.

Implement the stubs. Read worksheets/totp_verify.md and tests/test_totp_verify.py
before coding. Peek at solutions/totp_verify.py only if stuck.
"""

from __future__ import annotations

# TODO: imports you need (e.g. re, pyotp)


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

    Raise ValueError if `window` is negative.
    Return False for empty secret or malformed code (not exactly six digits).
    """
    raise NotImplementedError("implement verify_totp — see worksheets/totp_verify.md")


def current_code(secret: str, *, for_time: float | None = None) -> str:
    """Generate the current TOTP for demos and tests (not a production API)."""
    raise NotImplementedError("implement current_code — see worksheets/totp_verify.md")
