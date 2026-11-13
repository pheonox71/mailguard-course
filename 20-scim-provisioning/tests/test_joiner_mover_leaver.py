from katas.joiner_mover_leaver import deprovision_priority, stale_access_risk

def test_priority():
    assert deprovision_priority("leave") > deprovision_priority("join")

def test_risk():
    assert stale_access_risk(10, sla_hours=24) == "ok"
    assert stale_access_risk(30, sla_hours=24) == "elevated"
    assert stale_access_risk(50, sla_hours=24) == "critical"
