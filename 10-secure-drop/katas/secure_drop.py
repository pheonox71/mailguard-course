"""Expiring share links + audit + revoke + recipient OTP gate.

Landing is non-consuming; redemption is a separate step that marks the share
redeemed (one-shot download). HTTP responses for landing/download should send
``Referrer-Policy: no-referrer`` so tokens in the URL do not leak via Referer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import secrets
import time

# Send on landing + download/redeem HTTP responses (literacy constant for labs).
REFERRER_POLICY = "no-referrer"


@dataclass
class Share:
    token: str
    object_key: str
    expires_at: float
    revoked: bool = False
    redeemed: bool = False
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
    """Policy gate: not revoked, not expired (does not mark redeemed)."""
    raise NotImplementedError


def is_landing_allowed(share: Share, *, now: float | None = None) -> bool:
    """Non-consuming landing check — same policy as download; does not redeem."""
    raise NotImplementedError


def redeem_download(share: Share, audit: AuditStore, *, now: float | None = None) -> bool:
    """Consuming redemption: allow once, mark redeemed, audit. False if blocked."""
    raise NotImplementedError


def revoke(share: Share, audit: AuditStore) -> None:
    """Revoke after missend — immediately blocks landing and redeem."""
    raise NotImplementedError


def verify_recipient_otp(share: Share, otp: str) -> bool:
    """Constant-time compare against stored hash. False if no OTP configured."""
    raise NotImplementedError
