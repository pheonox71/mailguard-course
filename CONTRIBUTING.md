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

## CI — solutions vs learner katas

Course content CI (`.github/workflows/course-ci.yml`) has two complementary paths:

| Job family | What it runs | When it fails the workflow |
|------------|--------------|----------------------------|
| **`solutions-*`** | Copies `solutions/` over `katas/` (or worker files), then runs the module tests | **Yes** — proves the shipped tests and reference solutions stay valid |
| **`learner-katas`** | Runs the same tests against the committed `katas/` stubs via [`scripts/run_learner_katas.sh`](./scripts/run_learner_katas.sh) | **No** — always exits 0 after printing a per-module pass/fail table |

**Why this split.** Students implement stubs gradually. Gating merge/deploy on unfinished `NotImplementedError` stubs would keep CI red for most of the course. The solutions jobs are the correctness gate for the *course materials*; the learner job is a progress report (and a place to spot accidental stub breakage) without failing GitHub Pages deploy or the overall course CI for modules not started yet.

**Locally:**

```bash
# Prove tests + solutions (same idea as solutions-* jobs)
cd 03-oidc-access && cp solutions/*.py katas/ && pytest -q

# See stub status without copying solutions
./scripts/run_learner_katas.sh
```

Every push and pull request also runs the **Secret scan** workflow (gitleaks). The build fails on findings outside the allowlist.
