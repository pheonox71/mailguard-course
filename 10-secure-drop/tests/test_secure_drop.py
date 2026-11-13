import time
from katas.secure_drop import AuditStore, create_share, is_download_allowed, revoke

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
