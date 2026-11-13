from katas.workflow_checks import finds_forbidden_secret, requires_test_job

def test_detects_secret():
    assert finds_forbidden_secret("export AWS_SECRET_ACCESS_KEY=x") is True
    assert finds_forbidden_secret("pytest -q") is False

def test_requires_test_job():
    assert requires_test_job(["lint", "unit-test"]) is True
    assert requires_test_job(["build"]) is False
