from pathlib import Path
import yaml
from katas.manifest_checks import has_probes, has_requests, has_run_as_non_root, probes_are_split

def _load():
    return yaml.safe_load(Path("starter/deployment.yaml").read_text())

def _load_all(path: str):
    return list(yaml.safe_load_all(Path(path).read_text()))

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

def test_starter_security_context_and_networkpolicy():
    """Executable coverage: Deployment non-root + NetworkPolicy default-deny shape."""
    dep = _load()
    pod_sc = dep["spec"]["template"]["spec"].get("securityContext") or {}
    ctr_sc = dep["spec"]["template"]["spec"]["containers"][0].get("securityContext") or {}
    assert pod_sc.get("runAsNonRoot") is True or ctr_sc.get("runAsNonRoot") is True

    docs = [d for d in _load_all("starter/networkpolicy.yaml") if d]
    kinds = {d.get("kind") for d in docs}
    assert "NetworkPolicy" in kinds
    assert any(
        d.get("metadata", {}).get("name") == "mailguard-api-default-deny"
        and "Ingress" in (d.get("spec") or {}).get("policyTypes", [])
        and "Egress" in (d.get("spec") or {}).get("policyTypes", [])
        for d in docs
    )
    assert any(
        d.get("metadata", {}).get("name") == "mailguard-api-allow-dns-and-svc"
        and (d.get("spec") or {}).get("ingress")
        and (d.get("spec") or {}).get("egress")
        for d in docs
    )
