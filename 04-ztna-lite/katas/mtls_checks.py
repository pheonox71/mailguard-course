"""mTLS / device-cert literacy helpers."""

from __future__ import annotations


def cn_matches(cert_cn: str, expected_host: str) -> bool:
    raise NotImplementedError


def san_identity_ok(sans: list[str], expected_dns: str) -> bool:
    """True if expected_dns appears in the certificate SAN list (case-insensitive)."""
    raise NotImplementedError


def revoked(serial: str, crl_serials: set[str]) -> bool:
    raise NotImplementedError


def require_mtls(headers: dict[str, str]) -> bool:
    """True if client cert verified header marks SUCCESS (lab convention)."""
    raise NotImplementedError


def trust_proxy_identity(
    headers: dict[str, str],
    *,
    from_trusted_proxy: bool,
) -> bool:
    """Honor proxy-injected identity headers only when the peer is a trusted proxy."""
    raise NotImplementedError
