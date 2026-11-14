"""REFERENCE SOLUTION — peek only if stuck.

Educational path: stdlib base64/json decode + claim checks (iss/aud/exp/nonce)
and an alg allow-list that rejects ``none``. ``fetch_jwks`` shows the HTTP
shape for production signature verify (match ``kid``, then verify RS256/ES256)
without shipping RSA crypto in this kata.
"""

from __future__ import annotations

import base64
import json
import time
import urllib.error
import urllib.request
from typing import Any


def _b64url_decode(segment: str) -> bytes:
    pad = "=" * (-len(segment) % 4)
    return base64.urlsafe_b64decode(segment + pad)


def decode_jwt_unverified(token: str) -> tuple[dict[str, Any], dict[str, Any], str]:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("malformed JWT: need header.payload.signature")
    header_b64, payload_b64, sig_b64 = parts
    try:
        header = json.loads(_b64url_decode(header_b64))
        payload = json.loads(_b64url_decode(payload_b64))
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError("malformed JWT JSON") from exc
    if not isinstance(header, dict) or not isinstance(payload, dict):
        raise ValueError("JWT header/payload must be objects")
    return header, payload, sig_b64


def validate_id_token_claims(
    token: str,
    *,
    expected_iss: str,
    expected_aud: str | list[str],
    expected_nonce: str | None = None,
    now: int | None = None,
    allowed_algs: tuple[str, ...] = ("RS256", "ES256"),
    clock_skew_seconds: int = 60,
) -> dict[str, Any]:
    header, payload, _sig = decode_jwt_unverified(token)
    alg = header.get("alg")
    if alg is None or str(alg).lower() == "none" or alg not in allowed_algs:
        raise ValueError(f"disallowed alg: {alg!r}")
    if payload.get("iss") != expected_iss:
        raise ValueError("iss mismatch")
    aud = payload.get("aud")
    allowed = {expected_aud} if isinstance(expected_aud, str) else set(expected_aud)
    aud_values = {aud} if isinstance(aud, str) else set(aud or [])
    if not aud_values.intersection(allowed):
        raise ValueError("aud mismatch")
    exp = payload.get("exp")
    if not isinstance(exp, (int, float)):
        raise ValueError("exp missing")
    ts = int(time.time() if now is None else now)
    if ts > int(exp) + clock_skew_seconds:
        raise ValueError("token expired")
    if expected_nonce is not None and payload.get("nonce") != expected_nonce:
        raise ValueError("nonce mismatch")
    return payload


def fetch_jwks(jwks_url: str, *, timeout: float = 5.0) -> dict[str, Any]:
    req = urllib.request.Request(jwks_url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 — lab URL chosen by student
            data = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as exc:
        raise ValueError(f"JWKS fetch failed: {exc}") from exc
    if not isinstance(data, dict) or "keys" not in data:
        raise ValueError("JWKS missing keys")
    return data
