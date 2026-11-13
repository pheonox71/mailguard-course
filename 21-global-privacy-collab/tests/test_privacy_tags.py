import pytest
from katas.privacy_tags import lookup, flags_for_regions

def test_lookup_gdpr():
    assert "lawful" in lookup("GDPR")

def test_unknown():
    with pytest.raises(ValueError):
        lookup("NOTALAW")

def test_flags():
    assert flags_for_regions(["EU", "JP", "EU"]) == ["GDPR", "APPI"]
