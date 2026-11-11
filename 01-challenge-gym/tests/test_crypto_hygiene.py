"""Tests for the crypto hygiene kata."""

from __future__ import annotations

import os

import pytest

from katas.crypto_hygiene import aead_open, aead_seal, integrity_ok, integrity_tag

KEY = b"k" * 32
MSG = b"hold-pipeline-audit-event"


def test_integrity_tag_stable_hex():
    tag = integrity_tag(KEY, MSG)
    assert isinstance(tag, str)
    assert len(tag) == 64
    assert tag == integrity_tag(KEY, MSG)


def test_integrity_ok_accepts_and_rejects():
    tag = integrity_tag(KEY, MSG)
    assert integrity_ok(KEY, MSG, tag) is True
    assert integrity_ok(KEY, MSG, "00" * 32) is False
    assert integrity_ok(KEY, b"other", tag) is False
    assert integrity_ok(KEY, MSG, "not-hex") is False


def test_empty_key_raises_on_tag():
    with pytest.raises(ValueError):
        integrity_tag(b"", MSG)


def test_aead_roundtrip():
    blob = aead_seal(KEY, MSG, aad=b"mailguard-v1")
    assert len(blob) > 12
    assert aead_open(KEY, blob, aad=b"mailguard-v1") == MSG


def test_aead_rejects_wrong_aad_or_key():
    blob = aead_seal(KEY, MSG, aad=b"v1")
    with pytest.raises(ValueError):
        aead_open(KEY, blob, aad=b"v2")
    other = os.urandom(32)
    with pytest.raises(ValueError):
        aead_open(other, blob, aad=b"v1")


def test_aead_key_length():
    with pytest.raises(ValueError):
        aead_seal(b"short", MSG)
    with pytest.raises(ValueError):
        aead_open(b"short", b"\x00" * 28)
