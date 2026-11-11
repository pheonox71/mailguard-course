"""Tests for the recipient-risk kata."""

from __future__ import annotations

import pytest

from katas.recipient_risk import classify, normalize_email


def test_normalize_email():
    assert normalize_email("  Alice@Mailguard.Example ") == "alice@mailguard.example"
    assert normalize_email("not-an-email") is None
    assert normalize_email("a@b") is None  # domain needs a dot


def test_classify_mixed_should_hold():
    report = classify(
        ["alice@mailguard.example", "bob@partner.com", "Alice@mailguard.example"],
        internal_domain="mailguard.example",
    )
    assert report.internal == ("alice@mailguard.example",)
    assert report.external == ("bob@partner.com",)
    assert report.invalid == ()
    assert report.mixed is True
    assert report.should_hold is True


def test_classify_all_internal_ok():
    report = classify(
        ["a@mailguard.example", "b@mailguard.example"],
        internal_domain="mailguard.example",
    )
    assert report.external == ()
    assert report.should_hold is False


def test_invalid_triggers_hold():
    report = classify(["ok@mailguard.example", "bad"], internal_domain="mailguard.example")
    assert report.invalid == ("bad",)
    assert report.should_hold is True


def test_empty_internal_domain_raises():
    with pytest.raises(ValueError):
        classify(["a@b.com"], internal_domain="  ")
