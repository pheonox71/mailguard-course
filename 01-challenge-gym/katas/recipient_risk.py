"""Recipient-risk kata — classify To/Cc addresses vs an internal domain.

Challenge-shaped string work: normalize emails, spot external recipients,
and flag likely missends (internal + external mixed on one send).

Implement the stubs. Read assignments/recipient_risk.md and
tests/test_recipient_risk.py before coding. Peek at
solutions/recipient_risk.py only if stuck.
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
    """Lowercase and strip; return None if it is not a simple local@domain.

    Valid for this kata: exactly one `@`, non-empty local, non-empty domain
    that contains a `.`.
    """
    raise NotImplementedError("implement normalize_email — see assignments/recipient_risk.md")


def classify(recipients: list[str], *, internal_domain: str) -> RiskReport:
    """Split recipients into internal / external / invalid for `internal_domain`.

    - Normalize each address; invalids keep a stripped original form in `invalid`.
    - Compare domain to `internal_domain` (strip + lower).
    - Deduplicate normalized addresses (first wins).
    - Raise ValueError if `internal_domain` is empty/whitespace.
    """
    raise NotImplementedError("implement classify — see assignments/recipient_risk.md")
