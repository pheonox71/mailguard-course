from katas.ir_triage import (
    csf_function_order,
    impossible_travel,
    legacy_rev2_phases,
    phase_order,
    postmortem_has_blameless_sections,
)


def test_csf_functions():
    assert csf_function_order()[0] == "govern"
    assert csf_function_order()[-1] == "recover"
    assert phase_order() == csf_function_order()
    assert "detect" in csf_function_order()
    assert "respond" in csf_function_order()


def test_legacy_rev2_named():
    legacy = legacy_rev2_phases()
    assert len(legacy) == 4
    assert legacy[0] == "preparation"
    assert legacy[-1] == "postincident"


def test_travel():
    assert impossible_travel("US", "JP", 1.0) is True
    assert impossible_travel("US", "US", 0.5) is False


def test_postmortem():
    assert postmortem_has_blameless_sections("Impact: none\nTimeline: ...\nActions: rotate keys")
    assert not postmortem_has_blameless_sections("we messed up")
