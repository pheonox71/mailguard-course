"""Expiring share links + audit + revoke indirection."""

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
    raise NotImplementedError


def is_download_allowed(share: Share, *, now: float | None = None) -> bool:
    raise NotImplementedError


def revoke(share: Share, audit: AuditStore) -> None:
    raise NotImplementedError
