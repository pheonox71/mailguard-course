# Quiz — Cloud IAM posture

1. Expand **IAM**, then explain **how** a role, a policy, and a resource fit together for a MailGuard queue consumer.
2. **Why** is `Action: "*"` on a runtime role a smell (not just “style”)?
3. What is “shared responsibility” in one sentence, and **why** does object-storage exposure usually fall on the customer side?
4. Name one misconfig that could expose Secure Drop objects, and **how** you would detect it before production.
5. **Scenario:** Terraform state with cloud credentials is committed to a public repo. What do you do first, and **why** that order?
6. **Spot the bug / why:** A bucket policy uses `"Principal": "*"` with Block Public Access disabled. What is the risk mechanism?
