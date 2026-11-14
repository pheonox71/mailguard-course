# Assignment — SCIM provisioning

1. **Why** does leave/deprovision SLA beat join latency for risk? Give a MailGuard-shaped example (hold queue / admin).
2. Give one JIT vs SCIM trade-off. **When** would you still add SCIM if JIT already “works”?
3. Write a SCIM filter for active users named `ada@`. Explain **how** an IdP uses that filter before create.
4. What happens if a mover changes department groups but not app roles? **Why** is that a security/UX failure mode?
5. Sketch attributes you would map from Entra/Google to MailGuard. For two attributes, **why** the app needs them.
6. List the **session / token / cache** kills that must run when SCIM sets `active: false` — and one **Entra vs Okta PATCH** difference you would normalize.
7. In one sentence each: **why** [RFC 9865](https://www.rfc-editor.org/rfc/rfc9865) cursor pagination exists, and **how** a client walks `nextCursor`.
