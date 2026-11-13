# Quiz answer key — Security notes

Use only after attempting the quiz questions.

1. Keeps portfolio evidence honest and actionable — proves transfer to the product thread, not a laundry list of unrelated CVEs.
2. No — local labs / systems you own only. Juice Shop/crAPI on localhost (or your containers) replaces production targets.
3. Broken access control / IDOR-style authorization failure — enforce object-level authz on hold ids (tenant/owner checks) before return/release.
4. Ethics (public target), OWASP category, mitigation, and reproducible local evidence — without them the note is neither safe nor useful.
5. Cross-tenant data/release impact usually dwarfs UI XSS on a low-privilege view — still fix XSS, but triage access control first for gateways.
6. e.g. Broken Access Control (release another tenant’s hold) · Injection (rule predicate / query abuse) · Security Misconfiguration (open admin) · Identification/Auth failures (no MFA on release) — any two reasoned.
