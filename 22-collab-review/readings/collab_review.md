# Reading — Git & code review

## Learning objectives

1. Open small, reviewable PRs with clear English descriptions.
2. Review for security: secrets, authz, input validation, dangerous defaults.
3. Use conventional commits, CODEOWNERS, and CI logs effectively.
4. Write a one-page design note / RFC-style proposal.

**Why this matters.** Large mixed PRs hide auth bugs; vague commits block bisect; approving a PEM in `config/` creates a breach. MailGuard-shaped changes (hold/release, identity, CI) need reviewers who ask **why** and **how**, not only “LGTM.” On the job, collaboration skills are how secure changes land without silent regressions.

**How it works.**

1. Branch → small commits with [Conventional Commits](https://www.conventionalcommits.org/) subjects (`feat:`, `fix:`, `docs:` …).
2. Open a PR with intent, risk, and test plan; keep diff focused (split refactors from auth).
3. **CODEOWNERS** routes required reviewers by path ([GitHub — About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)).
4. Reviewers check secrets, authz, validation, dangerous defaults; CI logs triage red jobs before merge.
5. For larger ideas, write a one-page design/RFC before coding — why: align threat model and UX before sunk cost.

```text
idea → short RFC → small PR → CI → security-minded review → merge
```

Trade-off: tiny PRs add merge overhead but cut review risk; mega-PRs feel faster and ship hidden footguns.

### Worked example

Security-minded PR review checklist item:

```text
PR review — MailGuard-shaped change
[ ] Intent / risk / test plan filled in (why this change, how verified)
[ ] No secrets (*.pem, API keys, long-lived cloud keys) in the diff
[ ] Authz: who can hold/release/read? defaults fail closed?
[ ] Input validation on new API fields
[ ] CI: read the failing job log before re-running blindly
[ ] Split: refactor commits separate from auth/policy commits
```

```bash
# Why conventional subject: changelog + bisect clarity
git commit -m "fix: require readinessProbe on api deployment"

# Why block *.pem in PRs: secrets in git outlive the PR tab
```

Do **not** rewrite course `main` history to “practice rebase games.”

### Common misconceptions / what goes wrong

- **“LGTM on a mega-PR is fine if CI is green.”** Auth bugs hide in large mixed diffs; split refactors from security-sensitive changes ([OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/)).
- **“Re-run CI without reading logs.”** Blind retries waste time; the failing contract usually names the file.
- **“CODEOWNERS is optional ceremony.”** Path-based owners are how teams force review on identity/mail/IAM paths.
- **“Force-pushing rewritten `main` teaches git.”** History rewrite on shared main is out of scope and harmful — practice on personal branches.

## Read these (verified)

1. [Conventional Commits](https://www.conventionalcommits.org/)
2. [GitHub — About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
3. [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/)

## On the job

Security reviews of identity and mail features start with: secrets? authz? input validation? defaults? — then style.

## Next step

Assignment → kata → quiz. Practice repo optional.
