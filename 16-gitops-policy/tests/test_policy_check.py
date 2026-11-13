from pathlib import Path
import yaml
from katas.policy_check import is_deployable

def test_good_passes():
    d = yaml.safe_load(Path("fixtures/good_deployment.yaml").read_text())
    assert is_deployable(d) is True

def test_bad_fails():
    d = yaml.safe_load(Path("fixtures/bad_deployment.yaml").read_text())
    assert is_deployable(d) is False
