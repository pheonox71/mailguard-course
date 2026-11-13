"""Map a short finding label to an OWASP-ish category key."""

from __future__ import annotations

CATEGORIES = {
    "idor": "broken_access_control",
    "sqli": "injection",
    "xss": "injection",
    "missing_auth": "auth_failure",
    "default_secret": "security_misconfiguration",
}


def map_finding(label: str) -> str:
    """Return category key for a known label; raise KeyError if unknown."""
    raise NotImplementedError("implement map_finding")
