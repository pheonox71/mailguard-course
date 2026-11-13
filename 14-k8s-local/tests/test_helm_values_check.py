from katas.helm_values_check import has_resources, has_probes

def test_resources():
    ok = [{"resources": {"requests": {"cpu": "10m", "memory": "32Mi"}}, "readinessProbe": {}}]
    assert has_resources(ok)
    assert has_probes(ok)
    assert not has_resources([{"resources": {"requests": {"cpu": "10m"}}}])
