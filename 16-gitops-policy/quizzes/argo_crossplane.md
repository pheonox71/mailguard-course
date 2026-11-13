# Quiz — Argo / Crossplane

1. Is Argo CD primarily pull or push GitOps? Explain **how** reconciliation runs.
2. **Scenario:** CI applies kubectl from a laptop token — pull or push? **Why** is that riskier for audit?
3. **Spot the bug / why:** policy allows privileged pods in a prod namespace. What can an attacker do after container escape?
4. What is a Crossplane claim in one sentence, and **why** might a team prefer claims over every engineer using the cloud console?
5. **Why** fail the pipeline on a bad manifest before sync rather than “let Argo roll it back later”?
6. Name one policy-as-code tool listed in the reading and **how** you would use it on a PR.
