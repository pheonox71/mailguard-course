# Reading — Security notes

## Learning objectives

1. Map findings to OWASP Top 10 / API Top 10 categories.
2. Tie each finding to a MailGuard mitigation you can show in-repo.
3. Stay ethical: local labs only; no attacks on systems you do not own.

**Why this matters.** Vague “we should be careful” does not survive a security review or an interview. Unmapped screenshots of a vulnerable lab do not prove you can fix a rules API. Without ethics boundaries, “practice” becomes unauthorized access. Security notes exist so each risk has a **name**, a **category**, and a **mitigation you can show** — the same discipline used in email, identity, and cloud SaaS engineering.

**How it works.** Run an intentionally vulnerable app (e.g. OWASP Juice Shop) **only on localhost**. For each finding: title → OWASP Top 10 or API Top 10 category → MailGuard mitigation (authn, hold rules, least privilege, input validation) → evidence path in your notes. Prefer five solid mapped notes over a laundry list of unrelated CVEs. CWE Top 25 helps when you need finer defect vocabulary.

```
Local lab finding → OWASP/API category → MailGuard mitigation → evidence
         ↑ never point tools at systems you do not own
```

**On the job.** Writing actionable findings tied to product mitigations is how AppSec and product security communicate. Vendor-neutral OWASP/API Top 10 literacy transfers across gateways, admin APIs, and cloud identity surfaces.

## Short intro

Security notes turn vague “we should be careful” into **named risks + concrete fixes**. Use a local intentionally vulnerable app (e.g. OWASP Juice Shop) *only on localhost*, capture findings, and map them to MailGuard controls (authn, hold rules, least privilege, input validation).

## Read these (verified)

1. [OWASP Top 10](https://owasp.org/www-project-top-ten/)
2. [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/)
3. [OWASP Juice Shop — Getting Started](https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html)
4. [CWE Top 25](https://cwe.mitre.org/top25/)

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment.
