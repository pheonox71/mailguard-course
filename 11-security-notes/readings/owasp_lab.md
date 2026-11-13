# Reading — OWASP Top 10 / API Top 10 lab

## Learning objectives

1. Map findings from a **local-only** lab (OWASP Juice Shop or crAPI) to Top 10 / API Top 10.
2. Tie each finding to a MailGuard mitigation.
3. Add supply-chain CI hints: pip-audit, govulncheck, Dependabot, Syft SBOM.

**Why this matters.** Broken access control on hold release (IDOR / BOLA) ships silent cross-tenant leaks; injection and misconfiguration turn a rules API into an incident. Supply-chain CVEs in Python/Go deps ship unnoticed if CI never runs `pip-audit` / `govulncheck` or produces an **SBOM** (Software Bill of Materials). Labs without mitigations teach tourism; mapping to MailGuard teaches transfer. Corporate shared clusters are out of scope — unauthorized testing is not a learning feature.

**How it works.** Reproduce a finding locally → label with Top 10 / API Top 10 (e.g. A01:2021 Broken Access Control; API1:2023 BOLA) → write the MailGuard fix (authz on hold id, input validation, least privilege). For supply chain: CI runs dependency audits; **Syft** (or similar) emits an SBOM so when a CVE drops you can answer “are we affected?” quickly.

```
Local Juice Shop / crAPI → categorize → MailGuard mitigation
CI: pip-audit / govulncheck / Dependabot + Syft SBOM
```

**On the job.** AppSec reviews of email/identity APIs start with access control and injection; platform teams expect SBOM + audit in CI. This module is that workflow in miniature — vendor-neutral.

## Short intro

Map local lab findings to named categories and ship mitigations you can show. Never attack systems you do not own. Local containers only.

## Read these (verified)

1. [OWASP Top 10](https://owasp.org/www-project-top-ten/)
2. [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/)
3. [pip-audit](https://pypi.org/project/pip-audit/) · [govulncheck](https://go.dev/security/vuln/) · [Syft](https://github.com/anchore/syft)

## Keep in mind

Never attack systems you do not own. Local containers only.

## Next step

Continue with the assignment (`owasp_map` kata). The quiz is required after you attempt the assignment and tests.
