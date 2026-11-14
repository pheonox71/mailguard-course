# Answer key — SCIM

1. System for Cross-domain Identity Management. IdP clients create/update/deactivate Users/Groups on the app via a standard HTTP API.
2. elevated — lingering access after termination enables abuse; slow joins mostly create tickets, not attacker footholds.
3. Live sessions/tokens/caches (and often forwarding) still authorize hold-queue/admin access — deactivate must revoke them in the same path.
4. IdPs query existing users/groups before create/update to avoid duplicates and to PATCH the right id.
5. JIT creates on first SSO; SCIM pushes lifecycle continuously. JIT alone is insufficient when leavers never SSO again and need timely disable.
6. Schema (7643) and protocol (7644) evolve independently — apps implement HTTP ops from **RFC 7644**; **RFC 7643** is resources/schemas. Splitting lets protocol clients stay stable when schemas extend.
7. Examples: Entra capitalized `Replace` / string `"False"` for `active` vs Okta lowercase + boolean; Okta AIW often PUT-everything vs Entra PATCH-heavy; Entra default member-remove shape. Normalize `op` case, coerce `active`, rewrite unsafe member paths, dual-test.
8. Cursor-based pagination (`cursor`/`count`, `nextCursor`/`previousCursor`) for cursor-native stores — client sends empty/omitted `cursor` first, then passes `nextCursor` back until absent.
