"""HTTP Basic auth JSON client pattern (RFC 7617) — literacy kata.

Build Authorization header and parse a tiny JSON response. Do not ship
real credentials; tests use fixtures only.
"""

from __future__ import annotations

from typing import Any


def basic_auth_header(username: str, password: str) -> str:
    """Return 'Basic <base64(user:pass)>' (UTF-8). Raise ValueError on empty user."""
    raise NotImplementedError


def parse_token_response(body: str) -> dict[str, Any]:
    """Parse JSON object; require non-empty string 'token' key. Raise ValueError otherwise."""
    raise NotImplementedError


def skew_ok(server_unix: int, client_unix: int, *, max_skew: int = 30) -> bool:
    """True if abs(server - client) <= max_skew."""
    raise NotImplementedError
