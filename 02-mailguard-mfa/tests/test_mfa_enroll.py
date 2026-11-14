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
    """RFC 6238 §5.2 — same successful step must not verify twice."""
    e = enroll()
    totp = pyotp.TOTP(e.secret)
    t = 1_700_000_000
    code = totp.at(t)
    assert verify_totp(e, code, for_time=t) is True
    assert e.last_used_step == t // totp.interval
    assert verify_totp(e, code, for_time=t) is False


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
