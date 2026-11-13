from katas.ir_triage import phase_order, impossible_travel, postmortem_has_blameless_sections

def test_phases():
    assert phase_order()[0] == "preparation"
    assert phase_order()[-1] == "postincident"

def test_travel():
    assert impossible_travel("US", "JP", 1.0) is True
    assert impossible_travel("US", "US", 0.5) is False

def test_postmortem():
    assert postmortem_has_blameless_sections("Impact: none\nTimeline: ...\nActions: rotate keys")
    assert not postmortem_has_blameless_sections("we messed up")
