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


@dataclass
class AuditStore:
    events: list[str] = field(default_factory=list)

    def record(self, event: str) -> None:
        self.events.append(event)


def create_share(object_key: str, *, ttl_seconds: int, now: float | None = None) -> Share:
    ts = time.time() if now is None else now
    return Share(token=secrets.token_urlsafe(16), object_key=object_key, expires_at=ts + ttl_seconds)


def is_download_allowed(share: Share, *, now: float | None = None) -> bool:
    ts = time.time() if now is None else now
    return (not share.revoked) and ts <= share.expires_at


def revoke(share: Share, audit: AuditStore) -> None:
    share.revoked = True
    audit.record(f"revoke:{share.token}")
