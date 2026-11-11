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
    assert p.rua == ()
    assert p.ruf == ()
    assert p.adkim == "r"
    assert p.aspf == "r"


def test_parse_full_record():
    txt = (
        "v=DMARC1; p=quarantine; sp=reject; pct=50; "
        "rua=mailto:dmarc@example.com,mailto:agg@example.org; "
        "ruf=mailto:forensic@example.com; adkim=s; aspf=s"
    )
    p = parse_dmarc_record(txt)
    assert p.policy == "quarantine"
    assert p.subdomain_policy == "reject"
    assert p.percentage == 50
    assert p.rua == ("mailto:dmarc@example.com", "mailto:agg@example.org")
    assert p.ruf == ("mailto:forensic@example.com",)
    assert p.adkim == "s"
    assert p.aspf == "s"


def test_tag_names_case_insensitive():
    p = parse_dmarc_record("V=DMARC1; P=none")
    assert p.policy == "none"


def test_missing_or_bad_raises():
    with pytest.raises(ValueError):
        parse_dmarc_record("")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1; p=allow")
    with pytest.raises(ValueError):
        parse_dmarc_record("v=DMARC1; p=reject; pct=120")


def test_explains_spoofing_gap():
    none = parse_dmarc_record("v=DMARC1; p=none")
    msg = explains_spoofing_gap(none).lower()
    assert "monitor" in msg or "none" in msg
    partial = parse_dmarc_record("v=DMARC1; p=reject; pct=25")
    assert "25" in explains_spoofing_gap(partial) or "partial" in explains_spoofing_gap(partial).lower()
