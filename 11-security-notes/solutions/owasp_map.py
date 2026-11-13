"""REFERENCE SOLUTION."""

from __future__ import annotations

TOP10 = {
    "broken_access_control": "A01:2021",
    "injection": "A03:2021",
    "ssrf": "A10:2021",
    "auth_failure": "A07:2021",
}

API10 = {
    "bola": "API1:2023",
    "broken_auth": "API2:2023",
    "ssrf": "API7:2023",
}


def label_web(finding: str) -> str:
    key = finding.strip().lower()
    if key not in TOP10:
        raise ValueError("unknown")
    return TOP10[key]


def label_api(finding: str) -> str:
    key = finding.strip().lower()
    if key not in API10:
        raise ValueError("unknown")
    return API10[key]


def supply_chain_tools() -> tuple[str, ...]:
    return ("pip-audit", "govulncheck", "dependabot", "syft")
