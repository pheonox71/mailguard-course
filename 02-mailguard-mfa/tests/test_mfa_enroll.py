import time
import pyotp
from katas.mfa_enroll import consume_recovery, enroll, verify_totp

def test_enroll_has_secret_and_codes():
    e = enroll(recovery_count=3)
    assert e.secret
    assert len(e.recovery_codes) == 3

def test_verify_totp_roundtrip():
    e = enroll()
    totp = pyotp.TOTP(e.secret)
    code = totp.at(int(time.time()))
    assert verify_totp(e, code) is True
    assert verify_totp(e, "000000") is False

def test_recovery_one_time():
    e = enroll(recovery_count=1)
    code = e.recovery_codes[0]
    assert consume_recovery(e, code) is True
    assert consume_recovery(e, code) is False
