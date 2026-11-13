"""Tests for the TOTP verify kata."""

from __future__ import annotations

import pytest

from katas.totp_verify import current_code, verify_totp

# TEST FIXTURE ONLY — well-known public pyotp/RFC demo base32 key.
# Not a live credential. Do not use outside unit tests. (gitleaks allowlisted)
SECRET = "JBSWY3DPEHPK3PXP"
FIXED_TIME = 1_700_000_000.0


def test_accepts_current_code():
    code = current_code(SECRET, for_time=FIXED_TIME)
    assert verify_totp(SECRET, code, for_time=FIXED_TIME, window=0) is True


def test_rejects_wrong_code():
    assert verify_totp(SECRET, "000000", for_time=FIXED_TIME, window=0) is False


def test_rejects_malformed_code():
    assert verify_totp(SECRET, "abcdef", for_time=FIXED_TIME) is False
    assert verify_totp(SECRET, "12345", for_time=FIXED_TIME) is False
    assert verify_totp(SECRET, "", for_time=FIXED_TIME) is False


def test_window_tolerates_adjacent_step():
    # Code for previous 30s step should pass with window=1, fail with window=0.
    earlier = FIXED_TIME - 30
    code = current_code(SECRET, for_time=earlier)
    assert verify_totp(SECRET, code, for_time=FIXED_TIME, window=1) is True
    assert verify_totp(SECRET, code, for_time=FIXED_TIME, window=0) is False


def test_negative_window_raises():
    with pytest.raises(ValueError):
        verify_totp(SECRET, "123456", window=-1)
