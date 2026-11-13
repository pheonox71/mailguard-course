from katas.pr_hygiene import conventional_commit_ok, pr_too_large, flags_secret_path

def test_conventional():
    assert conventional_commit_ok("feat: add hold release")
    assert not conventional_commit_ok("updated stuff")

def test_size():
    assert pr_too_large(30) is True
    assert pr_too_large(3) is False

def test_secrets():
    assert flags_secret_path("app/.env")
    assert flags_secret_path("certs/server.pem")
    assert not flags_secret_path("README.md")
