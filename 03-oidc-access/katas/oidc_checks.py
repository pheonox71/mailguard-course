"""OIDC redirect / state helpers (literacy lab)."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse


def is_safe_redirect(uri: str, *, allowed_roots: tuple[str, ...]) -> bool:
    """True if uri starts with one of allowed_roots (exact prefix)."""
    raise NotImplementedError


def state_matches(saved: str, returned: str) -> bool:
    """Constant-time equality for OAuth state."""
    raise NotImplementedError


def parse_code(callback_url: str) -> str | None:
    """Extract ?code= from a callback URL."""
    raise NotImplementedError
