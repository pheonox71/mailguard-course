"""Tests for id_token claim validation helpers."""

from __future__ import annotations

import base64
import json

import pytest
from katas.jwt_checks import decode_jwt_unverified, validate_id_token_claims


def _b64url(data: dict) -> str:
    raw = json.dumps(data, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def _token(header: dict, payload: dict, sig: str = "sig") -> str:
    return f"{_b64url(header)}.{_b64url(payload)}.{sig}"


def test_decode_roundtrip():
    tok = _token({"alg": "RS256", "typ": "JWT"}, {"iss": "https://idp.example", "sub": "u1"})
    header, payload, sig = decode_jwt_unverified(tok)
    assert header["alg"] == "RS256"
    assert payload["sub"] == "u1"
    assert sig == "sig"


def test_validate_happy_path():
    now = 1_700_000_000
    tok = _token(
        {"alg": "RS256"},
        {
            "iss": "https://idp.example/realms/lab",
            "aud": "mailguard-admin",
            "exp": now + 300,
            "nonce": "n-1",
        },
    )
    claims = validate_id_token_claims(
        tok,
        expected_iss="https://idp.example/realms/lab",
        expected_aud="mailguard-admin",
        expected_nonce="n-1",
        now=now,
    )
    assert claims["aud"] == "mailguard-admin"


def test_reject_bad_aud_and_exp_and_none_alg():
    now = 1_700_000_000
    bad_aud = _token(
        {"alg": "RS256"},
        {"iss": "https://idp.example", "aud": "other", "exp": now + 60},
    )
    with pytest.raises(ValueError, match="aud"):
        validate_id_token_claims(
            bad_aud,
            expected_iss="https://idp.example",
            expected_aud="mailguard-admin",
            now=now,
        )

    expired = _token(
        {"alg": "RS256"},
        {"iss": "https://idp.example", "aud": "mailguard-admin", "exp": now - 120},
    )
    with pytest.raises(ValueError, match="expired"):
        validate_id_token_claims(
            expired,
            expected_iss="https://idp.example",
            expected_aud="mailguard-admin",
            now=now,
        )

    none_alg = _token(
        {"alg": "none"},
        {"iss": "https://idp.example", "aud": "mailguard-admin", "exp": now + 60},
    )
    with pytest.raises(ValueError, match="alg"):
        validate_id_token_claims(
            none_alg,
            expected_iss="https://idp.example",
            expected_aud="mailguard-admin",
            now=now,
        )


def test_nonce_mismatch():
    now = 1_700_000_000
    tok = _token(
        {"alg": "RS256"},
        {
            "iss": "https://idp.example",
            "aud": "mailguard-admin",
            "exp": now + 60,
            "nonce": "a",
        },
    )
    with pytest.raises(ValueError, match="nonce"):
        validate_id_token_claims(
            tok,
            expected_iss="https://idp.example",
            expected_aud="mailguard-admin",
            expected_nonce="b",
            now=now,
        )
