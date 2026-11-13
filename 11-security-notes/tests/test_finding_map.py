from katas.finding_map import map_finding
import pytest

def test_idor():
    assert map_finding("idor") == "broken_access_control"

def test_sqli():
    assert map_finding("sqli") == "injection"

def test_unknown():
    with pytest.raises(KeyError):
        map_finding("not-a-thing")
