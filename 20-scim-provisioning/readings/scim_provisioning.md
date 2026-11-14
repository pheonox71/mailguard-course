# Reading — SCIM / JIT / directories

## Learning objectives

1. Describe SCIM 2.0 resources, filtering, and PATCH (RFC 7643/7644) plus **cursor pagination** ([RFC 9865](https://www.rfc-editor.org/rfc/rfc9865)).
2. Contrast JIT vs SCIM vs directory sync (e.g. Entra Connect patterns), including **Entra vs Okta PATCH** quirks.
3. Explain why **`active: false` must kill sessions/tokens/caches**, and why deprovisioning latency often matters more than provisioning speed.

**Why this matters.** Joiner speed feels like a helpdesk win; **leaver lag** is a security incident waiting to happen — ex-employees who still reach hold queues, admin consoles, or mailbox forwards. System for Cross-domain Identity Management (**SCIM**) 2.0 standardizes create/update/deactivate across SaaS apps. Just-In-Time (**JIT**) provisioning creates users on first single sign-on (**SSO**) but may not tear them down promptly. On the job, identity engineers are measured on deprovision SLAs as much as onboarding UX.

**How it works.**

1. **[RFC 7643](https://www.rfc-editor.org/rfc/rfc7643)** defines resources (User, Group) and schemas; **[RFC 7644](https://www.rfc-editor.org/rfc/rfc7644)** defines the HTTP protocol (`/Users`, filters, PATCH).
2. An Identity Provider (**IdP**) (or broker) POSTs/PATCHes users into the app’s SCIM endpoint; clients often **filter** first (`userName eq …`) to avoid duplicates.
3. **[RFC 9865](https://www.rfc-editor.org/rfc/rfc9865)** (Oct 2025) adds **cursor-based pagination** (`cursor` / `count` query params; `nextCursor` / `previousCursor` in list responses) for SCIM providers whose stores already page by cursor — index `startIndex` alone does not fit every backend.
4. **JIT:** account appears at first SSO — simple, but lifecycle depends on later hooks.
5. **Directory sync** (e.g. Entra Connect-class): continuous sync from on-prem/cloud directories — different operational model than app-level SCIM.
6. Deprovision: `active: false` must **kill sessions, refresh/API tokens, and auth caches** in the same handler — plus revoke app roles, forwarding, and group grants. A disabled flag with a live session is still an incident.

```text
IdP lifecycle event → SCIM POST/PATCH/DELETE → app account state
                 ↘ JIT on first SSO (create only unless hooked)
PATCH active=false → revoke sessions + tokens + caches (same request path)
```

Trade-off: SCIM needs a correct endpoint and filter support; JIT is faster to ship and weaker on leavers unless you add lifecycle jobs.

### Worked example

Filter-then-create (IdP-style) against a lab `/Users` endpoint:

```http
GET /Users?filter=userName%20eq%20%22ada@example.com%22
Authorization: Bearer <scim-token>
```

```http
POST /Users
Content-Type: application/scim+json

{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "ada@example.com",
  "active": true,
  "emails": [{ "value": "ada@example.com", "primary": true }]
}
```

Why filter first: IdPs query before create/update to avoid duplicates ([RFC 7644](https://www.rfc-editor.org/rfc/rfc7644)). Why `active: false` on leave is not enough alone: **kill sessions, tokens, and caches in the same handler**, then clear roles/forwarding.

### `active: false` must kill access now

```text
On SCIM PATCH/PUT that sets active → false (or equivalent deactivate):
  1. Persist active=false (audit who/when)
  2. Revoke app sessions + refresh tokens + API tokens for that user
  3. Invalidate auth caches / local JWT allow-lists
  4. Drop privileged roles / hold-queue grants / mailbox forwards
If you only flip the flag, a still-valid session keeps reading held mail.
```

### Entra vs Okta PATCH semantics (interop)

IdPs do **not** send identical PATCH bodies for the same logical change. Normalize before apply:

| Topic | Microsoft Entra ID (typical) | Okta (typical) |
|-------|------------------------------|----------------|
| When PATCH is used | Most user/group attribute updates | OIN: PATCH for activate/deactivate/password (+ some group ops); AIW integrations often **PUT** everything |
| `op` casing | Often capitalized (`Replace` / `Add` / `Remove`) unless compliance flag enabled | Usually lowercase (`replace`) |
| `active` value | Historically string `"True"` / `"False"` by default; boolean with [compliance flag](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/application-provisioning-config-problem-scim-compatibility) | Boolean `true` / `false` in common shapes |
| Member remove | Default `path: "members"` + value array can wipe **all** members if mis-handled; filtered path with flag | Often filtered `members[value eq "…"]` |

**How:** lowercase `op`, coerce `active` to bool, expand path-less `value` objects, rewrite unsafe member removals, apply the whole PATCH in one transaction. Test against **both** IdPs — passing one does not prove the other.

### Cursor pagination (RFC 9865)

```http
GET /Users?count=10&cursor=
# Response includes Resources + nextCursor when more pages exist
GET /Users?count=10&cursor=<nextCursor-from-previous>
```

**Why:** Large directories and cursor-native stores cannot always use RFC 7644 index pagination alone. Advertise support in `ServiceProviderConfig` per the RFC; reject expired/invalid cursors with the documented `scimType` errors.

### Common misconceptions / what goes wrong

- **“Fast join latency means identity is secure.”** Leaver lag (T+24h still active on hold queues) is the usual incident — measure deprovision SLAs.
- **“JIT replaces SCIM.”** JIT creates on first SSO; without lifecycle hooks it does not tear down promptly.
- **“Setting `active=false` closes all access.”** Sessions, API tokens, auth caches, mailbox forwards, and group grants can outlive a disabled flag unless the deactivate path kills them.
- **“One IdP’s PATCH shape is universal.”** Entra and Okta differ on `op` case, `active` typing, PUT vs PATCH, and group-member remove — normalize and dual-test.
- **“Any filter string is fine.”** Incomplete filter support causes duplicate users or failed sync — support the subset IdPs actually send.
- **“Index pagination is always enough.”** Cursor backends need [RFC 9865](https://www.rfc-editor.org/rfc/rfc9865) `cursor` / `nextCursor` — do not invent a private paging scheme.

## Lab idea

Minimal FastAPI SCIM `/Users` endpoint passing a subset of filters; deactivate path that revokes a fake session store; optionally validate against a vendor SCIM test harness.

## Read these (verified)

1. [RFC 7643 — SCIM core](https://www.rfc-editor.org/rfc/rfc7643)
2. [RFC 7644 — SCIM protocol](https://www.rfc-editor.org/rfc/rfc7644)
3. [RFC 9865 — SCIM cursor-based pagination](https://www.rfc-editor.org/rfc/rfc9865)
4. [Microsoft Entra — SCIM overview](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups)
5. [Microsoft Entra — SCIM 2.0 compliance known issues](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/application-provisioning-config-problem-scim-compatibility)
6. [Google Workspace — Admin SDK Directory API](https://developers.google.com/admin-sdk/directory)

## On the job

Mail-security products inherit every account the IdP still believes is active. Ask “what happens at T+24h after termination?” before celebrating join latency.

## Next step

Assignments → katas → quiz.
