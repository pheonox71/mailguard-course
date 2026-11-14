import pytest
from katas.owasp_map import label_web, label_api, supply_chain_tools

def test_web():
    assert label_web("ssrf") == "A10:2021"

def test_web_edition_2025_stretch():
    assert label_web("injection", edition="2025") == "A05:2025"
    assert label_web("broken_access_control", edition="2025") == "A01:2025"
    assert label_web("auth_failure", edition="2025") == "A07:2025"
    # SSRF folds into A01:2025 Broken Access Control (related CWE-918).
    assert label_web("ssrf", edition="2025") == "A01:2025"

def test_api():
    assert label_api("bola") == "API1:2023"

def test_tools():
    tools = supply_chain_tools()
    assert "pip-audit" in tools and "syft" in tools

def test_bad():
    with pytest.raises(ValueError):
        label_web("not-a-finding")
