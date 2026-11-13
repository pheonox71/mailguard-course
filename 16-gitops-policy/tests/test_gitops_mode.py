import pytest
from katas.gitops_mode import classify_sync, crossplane_claim_name

def test_pull():
    assert classify_sync("argocd") == "pull"
    assert classify_sync("flux") == "pull"

def test_push():
    assert classify_sync("jenkins-kubectl") == "push"

def test_claim():
    assert crossplane_claim_name("Mail", "Prod") == "mail-prod-claim"

def test_bad():
    with pytest.raises(ValueError):
        classify_sync("unknown")
