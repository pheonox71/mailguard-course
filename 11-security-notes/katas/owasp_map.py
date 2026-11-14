"""Map lab findings to OWASP Top 10 / API Top 10 labels."""

from __future__ import annotations

TOP10 = {
    "broken_access_control": "A01:2021",
    "injection": "A03:2021",
    "ssrf": "A10:2021",
    "auth_failure": "A07:2021",
}

# Stretch: OWASP Top 10:2025 labels (see security_notes.md mapping table).
# SSRF is folded into A01:2025 Broken Access Control (CWE-918 is a related CWE).
TOP10_2025 = {
    "broken_access_control": "A01:2025",
    "injection": "A05:2025",
    "ssrf": "A01:2025",
    "auth_failure": "A07:2025",
}

API10 = {
    "bola": "API1:2023",
    "broken_auth": "API2:2023",
    "ssrf": "API7:2023",
}


def label_web(finding: str, edition: str = "2021") -> str:
    """Return Top 10 label. Default edition=2021; stretch: edition=\"2025\"."""
    raise NotImplementedError


def label_api(finding: str) -> str:
    raise NotImplementedError


def supply_chain_tools() -> tuple[str, ...]:
    """Return recommended CI tools tuple for this course."""
    raise NotImplementedError
