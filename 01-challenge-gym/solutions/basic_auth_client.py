"""REFERENCE SOLUTION — peek only if stuck."""

from __future__ import annotations

import base64
import json
from typing import Any


def basic_auth_header(username: str, password: str) -> str:
    if not username:
        raise ValueError("username required")
    raw = f"{username}:{password}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def parse_token_response(body: str) -> dict[str, Any]:
    data = json.loads(body)
    if not isinstance(data, dict):
        raise ValueError("expected object")
    token = data.get("token")
    if not isinstance(token, str) or not token:
        raise ValueError("missing token")
    return data


def skew_ok(server_unix: int, client_unix: int, *, max_skew: int = 30) -> bool:
    return abs(server_unix - client_unix) <= max_skew
