"""Tests for the DMARC policy kata."""

from __future__ import annotations

import pytest

from katas.dmarc_policy import explains_spoofing_gap, parse_dmarc_record


def test_parse_minimal_reject():
    p = parse_dmarc_record("v=DMARC1; p=reject")
    assert p.version == "DMARC1"
    assert p.policy == "reject"
    assert p.subdomain_policy is None
    assert p.percentage == 100
    assert p.test_mode is False
    assert p.nonexistent_policy is None
    assert p.psd is None
    assert p.rua == ()
    assert p.ruf == ()
    assert p.adkim == "r"
    assert p.aspf == "r"


def test_parse_full_record_rfc9989_and_legacy_pct():
    txt = (
        "v=DMARC1; p=quarantine; sp=reject; pct=50; t=y; np=none; psd=y; "
        "rua=mailto:dmarc@example.com,mailto:agg@example.org; "
        "ruf=mailto:forensic@example.com; adkim=s; aspf=s"
    )
    p = parse_dmarc_record(txt)
    assert p.policy == "quarantine"
    assert p.subdomain_policy == "reject"
    assert p.percentage == 50
    assert p.test_mode is True
    assert p.nonexistent_policy == "none"
    assert p.psd == "y"
    assert p.rua == ("mailto:dmarc@example.com", "mailto:agg@example.org")
    assert p.ruf == ("mailto:forensic@example.com",)
    assert p.adkim == "s"
    assert p.aspf == "s"


def test_tag_names_case_insensitive():
    p = parse_dmarc_record("V=DMARC1; P=none")
    assert p.policy == "none"


def test_v_must_be_first_tag():
    with pytest.raises(ValueError):
        parse_dmarc_record("p=reject; v=DMARC1")


def test_missing_or_bad_raises():
    with pytest.raises(ValueError):
        parse_dmarc_record("")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1; p=allow")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1; p=reject; pct=120")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1; p=reject; t=maybe")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1; p=reject; psd=x")


def test_explains_spoofing_gap():
    none = parse_dmarc_record("v=DMARC1; p=none")
    msg = explains_spoofing_gap(none).lower()
    assert "monitor" in msg or "none" in msg
    partial = parse_dmarc_record("v=DMARC1; p=reject; pct=25")
    partial_msg = explains_spoofing_gap(partial)
    assert "25" in partial_msg or "partial" in partial_msg.lower()
    test_mode = parse_dmarc_record("v=DMARC1; p=reject; t=y")
    test_msg = explains_spoofing_gap(test_mode).lower()
    assert "t=y" in test_msg or "test" in test_msg or "weaker" in test_msg
