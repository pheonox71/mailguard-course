import pytest
from katas.owasp_map import label_web, label_api, supply_chain_tools

def test_web():
    assert label_web("ssrf") == "A10:2021"

def test_api():
    assert label_api("bola") == "API1:2023"

def test_tools():
    tools = supply_chain_tools()
    assert "pip-audit" in tools and "syft" in tools

def test_bad():
    with pytest.raises(ValueError):
        label_web("not-a-finding")
