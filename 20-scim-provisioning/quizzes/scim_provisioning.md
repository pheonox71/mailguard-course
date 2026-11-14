# Quiz — SCIM

1. SCIM stands for? In one sentence, **how** does it move identity lifecycle into an app?
2. **Scenario:** employee left 36h ago, SLA=24h — which risk label does the kata return, and **why** is leave latency higher risk than slow joins?
3. **Spot the bug / why:** provisioning sets `active: false` but leaves sessions, API tokens, and auth caches intact. What access path remains?
4. **Why** is filter support required for many IdP provisioning clients?
5. Name one difference between JIT and SCIM, and **when** JIT alone is insufficient.
6. **Why** split SCIM into a core schema RFC and a separate protocol RFC — and which number is the **protocol** (HTTP operations)?
7. Name one **Entra vs Okta** PATCH interop difference (casing, `active` type, PUT vs PATCH, or group members) and **how** a server should normalize it.
8. **Why / how:** What does [RFC 9865](https://www.rfc-editor.org/rfc/rfc9865) add for SCIM list queries, and how does a client request the next page?
