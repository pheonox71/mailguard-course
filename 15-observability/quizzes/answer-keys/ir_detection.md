# Answer key — IR / detection

1. govern; recover. Without Govern/Identify/Protect readiness (logging, contacts, roles — what Rev. 2 called “preparation”), Detect and Respond become improvisation during a privacy-sensitive event.
2. Yes. Check VPN/travel tickets, MFA strength, impossible concurrent sessions, and whether the admin actually accessed hold content — then contain (revoke session) if suspicious.
3. Not blameless / not actionable — recurrence is likely because no system fix was owned.
4. SP 800-61r3 — a CSF 2.0 Community Profile (not the Rev. 2 four-phase checklist alone). Shared function names reduce handoff confusion across timezones and vendors.
5. No — English postmortems only; the course stays English-only for artifacts.
6. Course is product-shaped skill building, not a vendor pitch; mechanisms transfer across tools.
7. Revoke active sessions / refresh tokens first (containment), then investigate. HARs can embed live cookies/tokens — treat them like credentials (Okta 2023 support HAR lesson).
8. High-cardinality + secret leakage into scrapes/remote-write/screenshots — label with coarse enums only (e.g. `decision`), never email or session ids.
