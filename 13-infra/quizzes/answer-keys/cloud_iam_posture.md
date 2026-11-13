# Quiz answer key — cloud iam posture

Use only after attempting the quiz questions.

1. Identity and Access Management. A role is the principal the worker assumes; the policy allows specific actions (e.g. `sqs:ReceiveMessage`) on a named queue resource — not unbound `*`.
2. Violates least privilege; any process compromise inherits full API power across services — blast radius is huge.
3. Provider secures the cloud platform; customer secures accounts, data, identities, configs *in* the cloud. Bucket policies/ACLs/keys are customer configuration.
4. Since April 2023 new buckets have Block Public Access on and ACLs disabled (Bucket owner enforced) by default. Today's realistic misconfig is turning BPA off and adding a bucket policy with `"Principal": "*"`, or over-broad presign/role permissions (or a leaked long-lived key). Detect with `terraform plan`/policy scanners (Scout/Prowler-class) and access analyzer-style checks.
5. Rotate/revoke the exposed credentials first (stop ongoing abuse), then remove from git/history where possible, move to remote state with access controls, scrub leftovers.
6. Anyone on the internet can invoke allowed S3 actions on those objects — world-accessible data.
