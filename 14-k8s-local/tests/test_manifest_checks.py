from pathlib import Path
import yaml
from katas.manifest_checks import has_probes, has_requests, has_run_as_non_root, probes_are_split

def _load():
    return yaml.safe_load(Path("starter/deployment.yaml").read_text())

def test_starter_has_probes():
    assert has_probes(_load()) is True

def test_starter_has_requests():
    assert has_requests(_load()) is True

def test_starter_run_as_non_root():
    assert has_run_as_non_root(_load()) is True

def test_starter_probes_split():
    assert probes_are_split(_load()) is True

def test_missing_probes():
    d = _load()
    d["spec"]["template"]["spec"]["containers"][0].pop("readinessProbe")
    d["spec"]["template"]["spec"]["containers"][0].pop("livenessProbe")
    assert has_probes(d) is False
