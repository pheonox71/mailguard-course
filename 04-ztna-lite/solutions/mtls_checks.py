"""REFERENCE SOLUTION."""

from __future__ import annotations


def cn_matches(cert_cn: str, expected_host: str) -> bool:
    return cert_cn.strip().lower() == expected_host.strip().lower()


def revoked(serial: str, crl_serials: set[str]) -> bool:
    return serial in crl_serials


def require_mtls(headers: dict[str, str]) -> bool:
    return headers.get("x-client-cert-verified", "").upper() == "SUCCESS"
