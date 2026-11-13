"""Expiring share links + audit + revoke + recipient OTP gate."""

from __future__ import annotations

from dataclasses import dataclass, field
import secrets
import time


@dataclass
class Share:
    token: str
    object_key: str
    expires_at: float
    revoked: bool = False
    recipient_email: str | None = None
    otp_hash: str | None = None


@dataclass
class AuditStore:
    events: list[str] = field(default_factory=list)

    def record(self, event: str) -> None:
        self.events.append(event)


def create_share(
    object_key: str,
    *,
    ttl_seconds: int,
    now: float | None = None,
    recipient_email: str | None = None,
    otp: str | None = None,
) -> Share:
    """Create share. If otp provided, require recipient_email and store otp hash."""
    raise NotImplementedError


def is_download_allowed(share: Share, *, now: float | None = None) -> bool:
    raise NotImplementedError


def revoke(share: Share, audit: AuditStore) -> None:
    """Revoke after missend — immediately blocks download."""
    raise NotImplementedError


def verify_recipient_otp(share: Share, otp: str) -> bool:
    """Constant-time compare against stored hash. False if no OTP configured."""
    raise NotImplementedError
