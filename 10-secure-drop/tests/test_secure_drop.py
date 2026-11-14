"""Educational fixtures — demo OTP values (not live secrets)."""
from katas.secure_drop import (
    REFERRER_POLICY,
    AuditStore,
    create_share,
    is_download_allowed,
    is_landing_allowed,
    redeem_download,
    revoke,
    verify_recipient_otp,
)
import pytest

def test_create_and_allow():
    now = 1_700_000_000.0
    s = create_share("obj/a", ttl_seconds=60, now=now)
    assert is_download_allowed(s, now=now + 30) is True

def test_expiry():
    now = 1_700_000_000.0
    s = create_share("obj/a", ttl_seconds=10, now=now)
    assert is_download_allowed(s, now=now + 11) is False

def test_revoke():
    now = 1_700_000_000.0
    s = create_share("obj/a", ttl_seconds=60, now=now)
    audit = AuditStore()
    revoke(s, audit)
    assert is_download_allowed(s, now=now + 1) is False
    assert any("revoke" in e for e in audit.events)

def test_recipient_otp():
    now = 1_700_000_000.0
    s = create_share("obj/a", ttl_seconds=60, now=now, recipient_email="a@b.co", otp="123456")
    assert verify_recipient_otp(s, "123456") is True
    assert verify_recipient_otp(s, "000000") is False

def test_otp_requires_recipient():
    with pytest.raises(ValueError):
        create_share("obj/a", ttl_seconds=60, now=0, otp="123456")

def test_landing_non_consuming():
    now = 1_700_000_000.0
    s = create_share("obj/a", ttl_seconds=60, now=now)
    assert is_landing_allowed(s, now=now + 1) is True
    assert s.redeemed is False
    assert REFERRER_POLICY == "no-referrer"

def test_redeem_once():
    now = 1_700_000_000.0
    s = create_share("obj/a", ttl_seconds=60, now=now)
    audit = AuditStore()
    assert redeem_download(s, audit, now=now + 1) is True
    assert s.redeemed is True
    assert any("redeem" in e for e in audit.events)
    assert redeem_download(s, audit, now=now + 2) is False

def test_landing_after_revoke():
    now = 1_700_000_000.0
    s = create_share("obj/a", ttl_seconds=60, now=now)
    audit = AuditStore()
    revoke(s, audit)
    assert is_landing_allowed(s, now=now + 1) is False
    assert redeem_download(s, audit, now=now + 1) is False
