# Answer key — SCIM

1. System for Cross-domain Identity Management. IdP clients create/update/deactivate Users/Groups on the app via a standard HTTP API.
2. elevated — lingering access after termination enables abuse; slow joins mostly create tickets, not attacker footholds.
3. Access paths remain (forwarding, delegated access); deprovision incomplete until those are cleared too.
4. IdPs query existing users/groups before create/update to avoid duplicates and to PATCH the right id.
5. JIT creates on first SSO; SCIM pushes lifecycle continuously. JIT alone is insufficient when leavers never SSO again and need timely disable.
6. Schema (7643) and protocol (7644) evolve independently — apps implement HTTP ops from **RFC 7644**; **RFC 7643** is resources/schemas. Splitting lets protocol clients stay stable when schemas extend.
