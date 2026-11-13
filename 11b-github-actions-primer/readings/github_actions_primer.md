# GitHub Actions primer

**Why this matters.** Reviews catch some bugs; **CI** catches the rest on every push. Module 12 expects a workflow that runs tests (and optionally builds an image) **without** committing cloud secrets.

**How it works.** A YAML file under `.github/workflows/` declares **when** to run (`on:`), **jobs** on runners, and **steps** (checkout, setup language, test). Secrets stay in the host’s secret store; prefer **OIDC to cloud roles** over long-lived keys when you deploy.

This primer has no assignment, quiz, or download pack.

---

## What GitHub Actions is

**GitHub Actions** is GitHub’s integrated CI/CD: workflows as code beside your repository.

## Why industry uses it

Same git history as the product; PR checks block merges; matrix tests across languages. Security teams care that workflows are pinned, least-privileged, and secret-clean.

## Key concepts for Module 12

| Concept | Why you care |
|---------|----------------|
| `on: pull_request` | Test before merge |
| jobs / steps | Clear failure logs |
| `GITHUB_TOKEN` / secrets | Credentials never in YAML git history |
| Pinning actions (awareness) | Prefer immutable versions/SHAs in real pipelines |

## Install and run

1. A [GitHub](https://github.com/signup) account and a repo you control
2. No local daemon required — workflows run on GitHub-hosted runners (or self-hosted later)

Skim: [GitHub Actions documentation](https://docs.github.com/en/actions).

## Tiny hands-on example

```yaml
# Conceptual minimal workflow — Module 12 expands this for real tests
name: primer-ci
on:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Why: prove the runner clone worked before real tests"
```

**How:** A PR event starts a VM, checks out your commit, then runs steps — replace the `echo` with `pytest` / `go test` / `npm test` in Module 12.

## Official docs

1. [GitHub Actions docs](https://docs.github.com/en/actions)
2. [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
3. [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`12-ci-aws`).

This primer has **no** assignment, quiz, or download pack.
