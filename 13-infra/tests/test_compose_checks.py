from pathlib import Path
import yaml
from katas.compose_checks import compose_has_service

def test_starter_has_api():
    doc = yaml.safe_load(Path("starter/docker-compose.yml").read_text())
    assert compose_has_service(doc, "api")
    assert compose_has_service(doc, "db")
