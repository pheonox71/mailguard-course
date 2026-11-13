from katas.pkce import code_challenge_s256, verifier_length_ok

def test_s256_known():
    # RFC 7636 appendix B
    v = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
    assert code_challenge_s256(v) == "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM"

def test_length():
    assert verifier_length_ok("x" * 43)
    assert not verifier_length_ok("short")
