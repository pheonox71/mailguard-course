"""Recipient-risk kata — classify To/Cc addresses vs an internal domain.

Challenge-shaped string work: normalize emails, spot external recipients,
and flag likely missends (internal + external mixed on one send).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RiskReport:
    internal: tuple[str, ...]
    external: tuple[str, ...]
    invalid: tuple[str, ...]

    @property
    def mixed(self) -> bool:
        return bool(self.internal) and bool(self.external)

    @property
    def should_hold(self) -> bool:
        """Hold when mixed or any invalid address — missend / bad-input signal."""
        return self.mixed or bool(self.invalid)


def normalize_email(raw: str) -> str | None:
    """Lowercase and strip; return None if it is not a simple local@domain."""
    addr = raw.strip().lower()
    if addr.count("@") != 1:
        return None
    local, domain = addr.split("@")
    if not local or not domain or "." not in domain:
        return None
    return addr


def classify(recipients: list[str], *, internal_domain: str) -> RiskReport:
    """Split recipients into internal / external / invalid for `internal_domain`."""
    home = internal_domain.strip().lower()
    if not home:
        raise ValueError("internal_domain is required")

    internal: list[str] = []
    external: list[str] = []
    invalid: list[str] = []
    seen: set[str] = set()

    for raw in recipients:
        addr = normalize_email(raw)
        if addr is None:
            invalid.append(raw.strip())
            continue
        if addr in seen:
            continue
        seen.add(addr)
        domain = addr.rsplit("@", 1)[-1]
        (internal if domain == home else external).append(addr)

    return RiskReport(
        internal=tuple(internal),
        external=tuple(external),
        invalid=tuple(invalid),
    )
