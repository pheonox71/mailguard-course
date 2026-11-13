# Quiz answer key — cloud iam posture

Use only after attempting the quiz questions.

1. Identity and Access Management.
2. Violates least privilege; blast radius on compromise is huge.
3. Provider secures the cloud platform; customer secures accounts, data, identities, configs *in* the cloud.
4. Since April 2023 new buckets have Block Public Access on and ACLs disabled (Bucket owner enforced) by default. Today's realistic misconfig is turning BPA off and adding a bucket policy with `"Principal": "*"`, or over-broad presign/role permissions (or a leaked long-lived key).

5. Rotate/revoke credentials; remove from history if possible; use remote state with access controls; scrub git.

6. Public read/write exposure of objects — world-accessible data.
