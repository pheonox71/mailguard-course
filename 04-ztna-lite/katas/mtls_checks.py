"""mTLS / device-cert literacy helpers."""

from __future__ import annotations


def cn_matches(cert_cn: str, expected_host: str) -> bool:
    raise NotImplementedError


def revoked(serial: str, crl_serials: set[str]) -> bool:
    raise NotImplementedError


def require_mtls(headers: dict[str, str]) -> bool:
    """True if client cert verified header marks SUCCESS (lab convention)."""
    raise NotImplementedError
