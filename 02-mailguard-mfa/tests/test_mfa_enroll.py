import time

import pyotp

from katas.mfa_enroll import (
    MAX_FAILED_ATTEMPTS,
    consume_recovery,
    enroll,
    verify_totp,
)


def test_enroll_has_secret_and_codes():
    e = enroll(recovery_count=3)
    assert e.secret
    assert len(e.recovery_codes) == 3
    assert e.last_used_step is None
    assert e.failed_attempts == 0
    assert e.locked is False


def test_verify_totp_roundtrip():
    e = enroll()
    totp = pyotp.TOTP(e.secret)
    code = totp.at(int(time.time()))
    assert verify_totp(e, code) is True
    assert verify_totp(e, "000000") is False


def test_totp_replay_rejected():
    """RFC 6238 §5.2 — accept N, then reject N-1 and N (not equality-only)."""
    e = enroll()
    totp = pyotp.TOTP(e.secret)
    step_n = 1_700_000_000 // totp.interval
    t_n = step_n * totp.interval
    t_prev = (step_n - 1) * totp.interval
    code_n = totp.at(t_n)
    code_prev = totp.at(t_prev)
    assert verify_totp(e, code_n, for_time=t_n) is True
    assert e.last_used_step == step_n
    assert verify_totp(e, code_prev, for_time=t_prev) is False
    assert verify_totp(e, code_n, for_time=t_n) is False


def test_throttle_lockout():
    """Too many failed verifies lock the enrollment (NIST SP 800-63B throttle)."""
    e = enroll()
    for _ in range(MAX_FAILED_ATTEMPTS):
        assert verify_totp(e, "000000", for_time=1_700_000_000) is False
    assert e.locked is True
    totp = pyotp.TOTP(e.secret)
    good = totp.at(1_700_000_030)
    assert verify_totp(e, good, for_time=1_700_000_030) is False


def test_recovery_one_time():
    e = enroll(recovery_count=1)
    code = e.recovery_codes[0]
    assert consume_recovery(e, code) is True
    assert consume_recovery(e, code) is False
