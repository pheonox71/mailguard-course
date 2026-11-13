# Quiz — GitOps + policy

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. What is the desired-state source of truth in GitOps, and **why** is that better than “whatever is live in the cluster”?
2. Pull vs push sync — one sentence each on **how** they differ mechanically.
3. **Why** fail CI on a bad manifest before sync (not only after a failed rollout)?
4. Name one policy-as-code tool family and **how** it stops a missing-probe Deployment.
5. **Scenario:** git says replicas=2 but the cluster still has 5 and nobody synced. Where is drift, and **how** do you repair the GitOps way?
6. **Spot the bug / why:** a policy allows `:latest` tags in production. What risk mechanism follows?
