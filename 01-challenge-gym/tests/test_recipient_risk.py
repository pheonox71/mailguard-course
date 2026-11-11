"""Tests for the recipient-risk kata."""

from __future__ import annotations

import pytest

from katas.recipient_risk import classify, normalize_email


def test_normalize_email():
    assert normalize_email("  Alice@Hennge.Example ") == "alice@hennge.example"
    assert normalize_email("not-an-email") is None
    assert normalize_email("a@b") is None  # domain needs a dot


def test_classify_mixed_should_hold():
    report = classify(
        ["alice@hennge.example", "bob@partner.com", "Alice@hennge.example"],
        internal_domain="hennge.example",
    )
    assert report.internal == ("alice@hennge.example",)
    assert report.external == ("bob@partner.com",)
    assert report.invalid == ()
    assert report.mixed is True
    assert report.should_hold is True


def test_classify_all_internal_ok():
    report = classify(
        ["a@hennge.example", "b@hennge.example"],
        internal_domain="hennge.example",
    )
    assert report.external == ()
    assert report.should_hold is False


def test_invalid_triggers_hold():
    report = classify(["ok@hennge.example", "bad"], internal_domain="hennge.example")
    assert report.invalid == ("bad",)
    assert report.should_hold is True


def test_empty_internal_domain_raises():
    with pytest.raises(ValueError):
        classify(["a@b.com"], internal_domain="  ")
