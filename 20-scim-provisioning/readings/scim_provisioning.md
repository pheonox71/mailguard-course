# Reading — SCIM / JIT / directories

## Learning objectives

1. Describe SCIM 2.0 resources and filtering (RFC 7643/7644).
2. Contrast JIT vs SCIM vs directory sync (e.g. Entra Connect patterns).
3. Explain why **deprovisioning latency** often matters more than provisioning speed.

**Why this matters.** Joiner speed feels like a helpdesk win; **leaver lag** is a security incident waiting to happen — ex-employees who still reach hold queues, admin consoles, or mailbox forwards. System for Cross-domain Identity Management (**SCIM**) 2.0 standardizes create/update/deactivate across SaaS apps. Just-In-Time (**JIT**) provisioning creates users on first single sign-on (**SSO**) but may not tear them down promptly. On the job, identity engineers are measured on deprovision SLAs as much as onboarding UX.

**How it works.**

1. **RFC 7643** defines resources (User, Group) and schemas; **RFC 7644** defines the HTTP protocol (`/Users`, filters, PATCH).
2. An Identity Provider (**IdP**) (or broker) POSTs/PATCHes users into the app’s SCIM endpoint; clients often **filter** first (`userName eq …`) to avoid duplicates.
3. **JIT:** account appears at first SSO — simple, but lifecycle depends on later hooks.
4. **Directory sync** (e.g. Entra Connect-class): continuous sync from on-prem/cloud directories — different operational model than app-level SCIM.
5. Deprovision: disable login **and** revoke app roles, tokens, forwarding, and group grants — incomplete disable leaves access paths.

```text
IdP lifecycle event → SCIM POST/PATCH/DELETE → app account state
                 ↘ JIT on first SSO (create only unless hooked)
```

Trade-off: SCIM needs a correct endpoint and filter support; JIT is faster to ship and weaker on leavers unless you add lifecycle jobs.

## Lab idea

Minimal FastAPI SCIM `/Users` endpoint passing a subset of filters; optionally validate against a vendor SCIM test harness.

```text
# Why support filter: IdPs query before create/update
GET /Users?filter=userName eq "ada@example.com"
```

## Read these (verified)

1. [RFC 7643 — SCIM core](https://www.rfc-editor.org/rfc/rfc7643)
2. [RFC 7644 — SCIM protocol](https://www.rfc-editor.org/rfc/rfc7644)
3. [Microsoft Entra — SCIM overview](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups)
4. [Google Workspace — Admin SDK Directory API](https://developers.google.com/admin-sdk/directory)

## On the job

Mail-security products inherit every account the IdP still believes is active. Ask “what happens at T+24h after termination?” before celebrating join latency.

## Next step

Assignments → katas → quiz.
