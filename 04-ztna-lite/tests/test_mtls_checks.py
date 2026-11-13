from katas.mtls_checks import cn_matches, revoked, require_mtls

def test_cn():
    assert cn_matches("admin.example", "admin.example")

def test_crl():
    assert revoked("AB", {"AB", "CD"})
    assert not revoked("ZZ", {"AB"})

def test_header():
    assert require_mtls({"x-client-cert-verified": "SUCCESS"})
    assert not require_mtls({})
