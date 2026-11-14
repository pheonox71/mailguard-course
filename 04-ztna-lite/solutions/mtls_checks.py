"""REFERENCE SOLUTION."""

from __future__ import annotations


def cn_matches(cert_cn: str, expected_host: str) -> bool:
    return cert_cn.strip().lower() == expected_host.strip().lower()


def san_identity_ok(sans: list[str], expected_dns: str) -> bool:
    want = expected_dns.strip().lower()
    return any(s.strip().lower() == want for s in sans)


def revoked(serial: str, crl_serials: set[str]) -> bool:
    return serial in crl_serials


def require_mtls(headers: dict[str, str]) -> bool:
    return headers.get("x-client-cert-verified", "").upper() == "SUCCESS"


def trust_proxy_identity(
    headers: dict[str, str],
    *,
    from_trusted_proxy: bool,
) -> bool:
    if not from_trusted_proxy:
        return False
    return require_mtls(headers)
