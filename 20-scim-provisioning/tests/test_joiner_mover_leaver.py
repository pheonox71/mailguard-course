from katas.joiner_mover_leaver import (
    active_false_kill_checklist,
    deprovision_priority,
    stale_access_risk,
)

def test_priority():
    assert deprovision_priority("leave") > deprovision_priority("join")

def test_risk():
    assert stale_access_risk(10, sla_hours=24) == "ok"
    assert stale_access_risk(30, sla_hours=24) == "elevated"
    assert stale_access_risk(50, sla_hours=24) == "critical"

def test_active_false_kills_sessions_tokens_caches():
    steps = active_false_kill_checklist()
    assert steps[0] == "revoke_sessions"
    assert "revoke_refresh_and_api_tokens" in steps
    assert "invalidate_auth_caches" in steps
    assert steps[-1] == "drop_roles_forwards_and_grants"
