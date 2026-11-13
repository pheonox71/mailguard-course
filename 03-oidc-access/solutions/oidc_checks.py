from __future__ import annotations

import hmac
from urllib.parse import parse_qs, urlparse


def is_safe_redirect(uri: str, *, allowed_roots: tuple[str, ...]) -> bool:
    return any(uri.startswith(root) for root in allowed_roots)


def state_matches(saved: str, returned: str) -> bool:
    return hmac.compare_digest(saved, returned)


def parse_code(callback_url: str) -> str | None:
    q = parse_qs(urlparse(callback_url).query)
    vals = q.get("code") or []
    return vals[0] if vals else None
