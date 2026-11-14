from katas.oidc_checks import is_safe_redirect, parse_code, state_matches

def test_safe_redirect():
    assert is_safe_redirect("https://app.example/cb", allowed_roots=("https://app.example/",))
    assert not is_safe_redirect("https://evil.example/cb", allowed_roots=("https://app.example/",))


def test_safe_redirect_rejects_sibling_host_prefix_trick():
    """Prefix matching on the string must not accept evil sibling hosts."""
    allowed = ("https://app.example.com",)
    assert is_safe_redirect("https://app.example.com/cb", allowed_roots=allowed)
    assert not is_safe_redirect(
        "https://app.example.com.evil.com/cb",
        allowed_roots=allowed,
    )

def test_state_matches():
    assert state_matches("abc", "abc")
    assert not state_matches("abc", "xyz")

def test_parse_code():
    assert parse_code("https://app.example/cb?code=one&state=s") == "one"
    assert parse_code("https://app.example/cb?error=access_denied") is None
