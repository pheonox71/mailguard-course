# Self-check — Cloud IAM posture

1. Expand **IAM**.
2. Why is `Action: "*"` on a runtime role a smell?
3. What is “shared responsibility” in one sentence?
4. Name one misconfig that could expose Secure Drop objects.

---

## Answer key (try first)

1. Identity and Access Management.
2. Violates least privilege; blast radius on compromise is huge.
3. Provider secures the cloud platform; customer secures accounts, data, identities, configs *in* the cloud.
4. Public bucket / world-readable object ACL / leaked presign secret — examples.
