from __future__ import annotations

import hmac
from urllib.parse import parse_qs, urlparse


def _origin_and_path(url: str) -> tuple[str, str, str, str | int | None] | None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    # netloc already includes host:port when present
    path = parsed.path or "/"
    return parsed.scheme, parsed.hostname or "", path, parsed.port


def is_safe_redirect(uri: str, *, allowed_roots: tuple[str, ...]) -> bool:
    """True if uri is under an allowed root with host-boundary checks."""
    got = _origin_and_path(uri)
    if got is None:
        return False
    scheme, host, path, port = got
    for root in allowed_roots:
        allowed = _origin_and_path(root if "://" in root else f"https://{root}")
        if allowed is None:
            continue
        a_scheme, a_host, a_path, a_port = allowed
        if scheme != a_scheme or host != a_host or port != a_port:
            continue
        # Exact URI root, or path under the allowed path prefix at a boundary.
        if path == a_path.rstrip("/") or path.startswith(a_path if a_path.endswith("/") else a_path + "/"):
            return True
        if a_path in {"", "/"} and path.startswith("/"):
            return True
    return False


def state_matches(saved: str, returned: str) -> bool:
    return hmac.compare_digest(saved, returned)


def parse_code(callback_url: str) -> str | None:
    q = parse_qs(urlparse(callback_url).query)
    vals = q.get("code") or []
    return vals[0] if vals else None
