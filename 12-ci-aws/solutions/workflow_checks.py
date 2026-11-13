from __future__ import annotations

FORBIDDEN_PATTERNS = (
    "AWS_SECRET_ACCESS_KEY",
    "BEGIN RSA PRIVATE KEY",
    "ghp_",
)

def finds_forbidden_secret(text: str) -> bool:
    return any(p in text for p in FORBIDDEN_PATTERNS)

def requires_test_job(job_names: list[str]) -> bool:
    return any("test" in n.lower() for n in job_names)
