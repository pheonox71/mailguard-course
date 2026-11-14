import pytest
from katas.oidc_aws import role_trust_ok, forbids_static_aws_keys, ecs_service_name


def test_trust_main():
    assert role_trust_ok(
        "repo:acme/mailguard:ref:refs/heads/main",
        repo="acme/mailguard",
    )


def test_trust_rejects_other_repo():
    assert not role_trust_ok(
        "repo:evil/mailguard:ref:refs/heads/main",
        repo="acme/mailguard",
    )


def test_trust_immutable_owner_repo_ids():
    """GitHub immutable subject: ORG@owner-id/REPO@repo-id."""
    sub = "repo:acme@123456/mailguard@789012:ref:refs/heads/main"
    assert role_trust_ok(sub, repo="acme/mailguard")
    assert role_trust_ok(
        sub,
        repo="acme/mailguard",
        owner_id="123456",
        repo_id="789012",
    )
    assert not role_trust_ok(
        sub,
        repo="acme/mailguard",
        owner_id="999999",
        repo_id="789012",
    )
    # Name-based sub must not satisfy an ID-pinned trust policy.
    assert not role_trust_ok(
        "repo:acme/mailguard:ref:refs/heads/main",
        repo="acme/mailguard",
        owner_id="123456",
        repo_id="789012",
    )


def test_forbids_keys():
    assert forbids_static_aws_keys(["AWS_REGION", "ROLE_ARN"]) is True
    assert forbids_static_aws_keys(["AWS_ACCESS_KEY_ID"]) is False


def test_ecs_name():
    assert ecs_service_name("MailGuard", "Prod") == "mailguard-prod-svc"


def test_ecs_empty():
    with pytest.raises(ValueError):
        ecs_service_name("", "prod")
