# Reading — OWASP Top 10 / API Top 10 lab

## Learning objectives

1. Map findings from a **local-only** lab (OWASP Juice Shop or crAPI) to Top 10 / API Top 10.
2. Tie each finding to a MailGuard mitigation.
3. Add supply-chain CI hints: pip-audit, govulncheck, Dependabot, Syft SBOM.

**Why this matters.** Broken access control on hold release (IDOR / BOLA) ships silent cross-tenant leaks; injection and misconfiguration turn a rules API into an incident. Supply-chain CVEs in Python/Go deps ship unnoticed if CI never runs `pip-audit` / `govulncheck` or produces an **SBOM** (Software Bill of Materials). Labs without mitigations teach tourism; mapping to MailGuard teaches transfer. Corporate shared clusters are out of scope — unauthorized testing is not a learning feature.

**How it works.**

1. Reproduce a finding in a **local** Juice Shop / crAPI container only.
2. Label with Top 10 / API Top 10 (e.g. A01:2021 Broken Access Control; API1:2023 BOLA) — [OWASP Top 10](https://owasp.org/www-project-top-ten/), [API Security Top 10](https://owasp.org/API-Security/). Prefer **2025** names in new notes; the kata stretch is `label_web(..., edition="2025")`.
3. Write the MailGuard fix (authz on hold id, input validation, least privilege) you can point to in-repo or in a test.
4. For supply chain: CI runs dependency audits ([pip-audit](https://pypi.org/project/pip-audit/), [govulncheck](https://go.dev/security/vuln/), Dependabot).
5. **Syft** (or similar) emits an **SBOM** so when a CVE drops you can answer “are we affected?” quickly ([Syft](https://github.com/anchore/syft)).
6. Track federal binding operational directives when they affect vuln management: **BOD 22-01** (reduce significant risk of known exploited vulnerabilities) is **revoked / superseded by [BOD 26-04 — Prioritizing Security Updates Based on Risk](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk)** — cite the current directive, not the retired one.

```
Local Juice Shop / crAPI → categorize → MailGuard mitigation
CI: pip-audit / govulncheck / Dependabot + Syft SBOM
```

### Worked example

Mapping + CI sketch:

| Lab finding | Category | MailGuard mitigation |
|-------------|----------|----------------------|
| Change `orderId` in URL, see another user’s order | API1:2023 BOLA | `assert hold.tenant_id == caller.tenant_id` before release; pytest for cross-tenant 403 |
| SQLi in search | A03:2021 Injection | Parameterized queries / ORM binds; never string-format SQL |
| Outdated `requests` with known CVE | Supply chain | `pip-audit` on PR + Syft SBOM artifact |

```yaml
# Conceptual CI fragment — why: fail the PR before a known-bad dep merges
- name: pip-audit
  run: pip-audit -r requirements.txt
- name: sbom
  run: syft dir:. -o spdx-json > sbom.spdx.json
```

**On the job.** AppSec reviews of email/identity APIs start with access control and injection; platform teams expect SBOM + audit in CI. This module is that workflow in miniature — vendor-neutral.

## Short intro

Map local lab findings to named categories and ship mitigations you can show. Never attack systems you do not own. Local containers only.

### Common misconceptions / what goes wrong

- **“IDOR is only a web app bug.”** Hold release by id without tenant checks is the same BOLA class on an API.
- **“SBOM is paperwork.”** Without an inventory you cannot answer CVE blast-radius quickly; Syft (or similar) makes that queryable.
- **“Auditing deps once at kickoff is enough.”** New CVEs land weekly; run audits on every PR.
- **“The lab is the deliverable.”** Tourism without a MailGuard mitigation row fails the learning goal.
- **“BOD 22-01 is still the current CISA directive for this topic.”** It has been **revoked/superseded by BOD 26-04** — update notes and playbooks to the current directive.

## Binding Operational Directives (CVE / KEV literacy)

**Why.** Federal civilian agencies (and many vendors who mirror CISA guidance) used **BOD 22-01** to drive remediation of Known Exploited Vulnerabilities (KEV). Citing a revoked directive in a security note looks stale.

**How.** Treat [BOD 22-01 (revoked)](https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities-revoked) as historical. Current successor: **[BOD 26-04 — Prioritizing Security Updates Based on Risk](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk)** (supersedes and revokes BOD 22-01 and BOD 19-02). Pair SBOM + `pip-audit` / `govulncheck` with KEV awareness so “are we affected?” includes *is this actively exploited?*

## Read these (verified)

1. [OWASP Top 10](https://owasp.org/www-project-top-ten/) · [OWASP Top 10:2025](https://owasp.org/Top10/2025/)
2. [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/)
3. [pip-audit](https://pypi.org/project/pip-audit/) · [govulncheck](https://go.dev/security/vuln/) · [Syft](https://github.com/anchore/syft)
4. [CISA BOD 26-04](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) (supersedes/revokes BOD 22-01)

## Keep in mind

Never attack systems you do not own. Local containers only.

## Next step

Continue with the assignment (`owasp_map` kata). The quiz is required after you attempt the assignment and tests.
