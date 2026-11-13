from katas.mail_flow import spf_after_gateway, dmarc_may_still_pass, arc_needed

def test_spf():
    assert spf_after_gateway(True) == "likely_fail"

def test_dmarc_dkim():
    assert dmarc_may_still_pass(True) is True
    assert dmarc_may_still_pass(False) is False

def test_arc():
    assert arc_needed(0) is False
    assert arc_needed(2) is True
