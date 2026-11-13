# Reading — SCIM / JIT / directories

## Learning objectives

1. Describe SCIM 2.0 resources and filtering (RFC 7643/7644).
2. Contrast JIT vs SCIM vs directory sync (e.g. Entra Connect patterns).
3. Explain why **deprovisioning latency** often matters more than provisioning speed.

## Read these (verified)

1. [RFC 7643 — SCIM core](https://www.rfc-editor.org/rfc/rfc7643)
2. [RFC 7644 — SCIM protocol](https://www.rfc-editor.org/rfc/rfc7644)
3. [Microsoft Entra — SCIM overview](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups)
4. [Google Workspace — Admin SDK Directory API](https://developers.google.com/admin-sdk/directory)

## Lab idea

Minimal FastAPI SCIM `/Users` endpoint passing a subset of filters; optionally validate against a vendor SCIM test harness.

## Next step

Worksheets → katas → quiz.
