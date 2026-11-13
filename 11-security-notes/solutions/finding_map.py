from __future__ import annotations

CATEGORIES = {
    "idor": "broken_access_control",
    "sqli": "injection",
    "xss": "injection",
    "missing_auth": "auth_failure",
    "default_secret": "security_misconfiguration",
}

def map_finding(label: str) -> str:
    key = label.strip().lower()
    if key not in CATEGORIES:
        raise KeyError(label)
    return CATEGORIES[key]
