# Reading — Security notes

## Learning objectives

1. Map findings to OWASP Top 10 / API Top 10 categories.
2. Tie each finding to a MailGuard mitigation you can show in-repo.
3. Stay ethical: local labs only; no attacks on systems you do not own.

**Why this matters.** Vague “we should be careful” does not survive a security review or an interview. Unmapped screenshots of a vulnerable lab do not prove you can fix a rules API. Without ethics boundaries, “practice” becomes unauthorized access. Security notes exist so each risk has a **name**, a **category**, and a **mitigation you can show** — the same discipline used in email, identity, and cloud SaaS engineering.

**How it works.**

1. Run an intentionally vulnerable app (e.g. OWASP Juice Shop) **only on localhost** ([Juice Shop getting started](https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html)).
2. Capture a finding with a short title and evidence (screenshot path / request id in your notes).
3. Label it with [OWASP Top 10](https://owasp.org/www-project-top-ten/) or [API Security Top 10](https://owasp.org/API-Security/).
4. Map to a MailGuard mitigation you can show (authn, hold rules, least privilege, input validation).
5. Prefer five solid mapped notes over a laundry list of unrelated CVEs. Use [CWE Top 25](https://cwe.mitre.org/top25/) when you need finer defect vocabulary.

```
Local lab finding → OWASP/API category → MailGuard mitigation → evidence
         ↑ never point tools at systems you do not own
```

### Worked example

One security-note row:

| Field | Example |
|-------|---------|
| Title | IDOR on order endpoint returns another user’s data |
| Category | API1:2023 Broken Object Level Authorization (BOLA) |
| MailGuard mitigation | Authz check: caller may only release/approve holds in their tenant; tests for cross-id 403 |
| Evidence | `notes/juice-idor.png` + request showing `/api/Orders/7` with victim id |
| Ethics | Local Docker only; no corporate/shared targets |

**On the job.** Writing actionable findings tied to product mitigations is how AppSec and product security communicate. Vendor-neutral OWASP/API Top 10 literacy transfers across gateways, admin APIs, and cloud identity surfaces.

## Short intro

Security notes turn vague “we should be careful” into **named risks + concrete fixes**. Use a local intentionally vulnerable app (e.g. OWASP Juice Shop) *only on localhost*, capture findings, and map them to MailGuard controls (authn, hold rules, least privilege, input validation).

### Common misconceptions / what goes wrong

- **“A CVE list counts as notes.”** Without category + product mitigation, reviewers cannot act; map to MailGuard controls you can show.
- **“Screenshots alone prove understanding.”** Notes need the OWASP/API label and the fix path — tourism vs transfer.
- **“Shared staging is fine for practice.”** Unauthorized testing is out of scope; local containers only.
- **“Everything is A01.”** Mis-labeling hides the real fix (e.g. injection vs access control); use the right Top 10 / API row.

## Read these (verified)

1. [OWASP Top 10](https://owasp.org/www-project-top-ten/)
2. [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/)
3. [OWASP Juice Shop — Getting Started](https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html)
4. [CWE Top 25](https://cwe.mitre.org/top25/)

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment.
