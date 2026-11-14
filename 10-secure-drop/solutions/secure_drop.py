"""REFERENCE SOLUTION."""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import hmac
import secrets
import time

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


def _hash_otp(otp: str) -> str:
    return hashlib.sha256(otp.encode("utf-8")).hexdigest()


def create_share(
    object_key: str,
    *,
    ttl_seconds: int,
    now: float | None = None,
    recipient_email: str | None = None,
    otp: str | None = None,
) -> Share:
    ts = time.time() if now is None else now
    otp_hash = None
    if otp is not None:
        if not recipient_email:
            raise ValueError("recipient_email required with otp")
        otp_hash = _hash_otp(otp)
    return Share(
        token=secrets.token_urlsafe(16),
        object_key=object_key,
        expires_at=ts + ttl_seconds,
        recipient_email=recipient_email,
        otp_hash=otp_hash,
    )


def is_download_allowed(share: Share, *, now: float | None = None) -> bool:
    ts = time.time() if now is None else now
    if share.revoked:
        return False
    return ts <= share.expires_at


def is_landing_allowed(share: Share, *, now: float | None = None) -> bool:
    # Non-consuming: same gate as download; does not require or set redeemed.
    return is_download_allowed(share, now=now)


def redeem_download(share: Share, audit: AuditStore, *, now: float | None = None) -> bool:
    if share.redeemed:
        return False
    if not is_download_allowed(share, now=now):
        return False
    share.redeemed = True
    audit.record(f"redeem:{share.token}")
    return True


def revoke(share: Share, audit: AuditStore) -> None:
    share.revoked = True
    audit.record(f"revoke:{share.token}")


def verify_recipient_otp(share: Share, otp: str) -> bool:
    if not share.otp_hash:
        return False
    return hmac.compare_digest(share.otp_hash, _hash_otp(otp))
