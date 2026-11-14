from katas.mtls_checks import (
    cn_matches,
    revoked,
    require_mtls,
    san_identity_ok,
    trust_proxy_identity,
)


def test_cn():
    assert cn_matches("admin.example", "admin.example")


def test_san_identity_rfc9525():
    assert san_identity_ok(["admin.example", "admin.mail.example"], "admin.mail.example")
    assert not san_identity_ok(["other.example"], "admin.mail.example")


def test_crl():
    assert revoked("AB", {"AB", "CD"})
    assert not revoked("ZZ", {"AB"})


def test_header():
    assert require_mtls({"x-client-cert-verified": "SUCCESS"})
    assert not require_mtls({})


def test_spoofed_identity_headers_from_non_proxy():
    spoofed = {
        "x-client-cert-verified": "SUCCESS",
        "x-client-dn": "CN=attacker",
    }
    assert trust_proxy_identity(spoofed, from_trusted_proxy=False) is False
    assert trust_proxy_identity(spoofed, from_trusted_proxy=True) is True
