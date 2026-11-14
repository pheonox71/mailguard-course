"""OIDC redirect / state helpers (literacy lab)."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse


def is_safe_redirect(uri: str, *, allowed_roots: tuple[str, ...]) -> bool:
    """True if uri is under an allowed root with host-boundary checks.

    Naive string prefix matching is unsafe: an allow-list entry of
    ``https://app.example.com`` must **not** accept
    ``https://app.example.com.evil.com/...``. Compare scheme and host
    (and port) exactly, then require the path to start with the allowed
    path (or match an exact registered redirect URI).
    """
    raise NotImplementedError


def state_matches(saved: str, returned: str) -> bool:
    """Constant-time equality for OAuth state."""
    raise NotImplementedError


def parse_code(callback_url: str) -> str | None:
    """Extract ?code= from a callback URL."""
    raise NotImplementedError
