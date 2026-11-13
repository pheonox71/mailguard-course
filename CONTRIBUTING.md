# Contributing

## Secrets hygiene

- Never commit live credentials, API keys, tokens, or private keys.
- Use `.env` locally (gitignored). Copy from [`.env.example`](./.env.example) when you need a template.
- Course lessons may include **marked test fixtures** (for example a well-known TOTP demo key or a local-only compose password). Those are not production secrets; do not reuse them elsewhere.

## Pre-commit (gitleaks)

Scan for accidental secrets before each commit:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

Config: [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) (gitleaks). Allowlisted educational fixtures live in [`.gitleaks.toml`](./.gitleaks.toml).

## CI

Every push and pull request runs the **Secret scan** workflow (gitleaks). The build fails on findings outside the allowlist.
