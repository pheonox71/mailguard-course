import pytest
from katas.scim_filter import User, apply_filter, parse_eq_filter

USERS = [
    User("1", "ada@", True),
    User("2", "bob@", False),
]

def test_parse_username():
    assert parse_eq_filter('userName eq "ada@"') == ("userName", "ada@")

def test_filter_active():
    assert [u.id for u in apply_filter(USERS, "active eq true")] == ["1"]

def test_bad_filter():
    with pytest.raises(ValueError):
        parse_eq_filter("userName co ada")
