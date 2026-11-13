"""Educational fixtures — RFC 7617 Basic auth example values (not live secrets)."""
import pytest
from katas.basic_auth_client import basic_auth_header, parse_token_response, skew_ok

def test_basic_header():
    # "Aladdin:open sesame" classic RFC 7617 example → QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    assert basic_auth_header("Aladdin", "open sesame") == "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=="

def test_empty_user():
    with pytest.raises(ValueError):
        basic_auth_header("", "x")

def test_parse_token():
    assert parse_token_response('{"token":"abc","expires_in":60}')["token"] == "abc"

def test_parse_missing_token():
    with pytest.raises(ValueError):
        parse_token_response('{"ok":true}')

def test_skew():
    assert skew_ok(100, 120, max_skew=30) is True
    assert skew_ok(100, 140, max_skew=30) is False
