"""REFERENCE SOLUTION."""

from __future__ import annotations

TOP10 = {
    "broken_access_control": "A01:2021",
    "injection": "A03:2021",
    "ssrf": "A10:2021",
    "auth_failure": "A07:2021",
}

TOP10_2025 = {
    "broken_access_control": "A01:2025",
    "injection": "A05:2025",
    "ssrf": "CWE-918",
    "auth_failure": "A07:2025",
}

API10 = {
    "bola": "API1:2023",
    "broken_auth": "API2:2023",
    "ssrf": "API7:2023",
}


def label_web(finding: str, edition: str = "2021") -> str:
    key = finding.strip().lower()
    table = TOP10_2025 if edition == "2025" else TOP10
    if edition not in ("2021", "2025"):
        raise ValueError("unknown edition")
    if key not in table:
        raise ValueError("unknown")
    return table[key]


def label_api(finding: str) -> str:
    key = finding.strip().lower()
    if key not in API10:
        raise ValueError("unknown")
    return API10[key]


def supply_chain_tools() -> tuple[str, ...]:
    return ("pip-audit", "govulncheck", "dependabot", "syft")
