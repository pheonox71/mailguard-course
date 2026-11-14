# Reading — OIDC to AWS + ECS

## Learning objectives

1. Prefer **GitHub Actions OIDC** over long-lived `AWS_ACCESS_KEY_ID` secrets.
2. Constrain role trust by `sub` (repo + ref) — and know **both** name-based and **immutable owner/repo-ID** subject forms.
3. Prefer pinning with `job_workflow_ref` and/or a GitHub **environment** claim when a ref alone is too broad.
4. Sketch an ECS Fargate deploy from CI.

**Why this matters.** Static AWS keys in repository secrets still leak via mis-logged env dumps, overly broad `permissions:`, and compromised maintainers. Federation with OpenID Connect (**OIDC**) issues **short-lived** credentials only when a trusted workflow runs. Without a tight trust policy (`sub` = this repo + `main`), any branch or fork workflow that can request the token becomes a cloud admin path. On the job, cloud-security reviews almost always ask how CI authenticates to the account that runs gateways, queues, and mail workers.

**How it works.**

1. Register GitHub’s OIDC issuer (`token.actions.githubusercontent.com`) as an Identity and Access Management (**IAM**) OIDC provider in AWS.
2. Create an IAM role whose trust policy allows `sts:AssumeRoleWithWebIdentity` only when JWT claims match.
3. Match the **`sub` format your repo actually mints** ([GitHub OIDC reference — immutable subject claims](https://docs.github.com/en/actions/reference/security/oidc)):
   - **Name-based (legacy default for older repos):** `repo:ORG/REPO:ref:refs/heads/main`
   - **Immutable (default for repos created after 2026-07-15, or after opt-in / rename/transfer):** `repo:ORG@OWNER-ID/REPO@REPO-ID:ref:refs/heads/main`  
     Numeric owner/repo IDs survive namespace recycle and rename; update AWS trust conditions when you opt in or create new repos.
4. Tighten further with **`job_workflow_ref`** (reusable/deploy workflow path) and/or **`environment`** (protected GitHub Environment) so a random workflow file on `main` cannot assume the deploy role.
5. In Actions, set workflow `permissions:` so the job can mint an OIDC token — at minimum `id-token: write` (and usually `contents: read`). Without `id-token: write`, `configure-aws-credentials` cannot request the JWT.
6. Request an ID token, call AssumeRoleWithWebIdentity (often via `aws-actions/configure-aws-credentials`), then push an image and update **Amazon Elastic Container Service (ECS)** on **Fargate** (serverless tasks — no EC2 capacity management for the task itself).
7. Task definition pins image digest/tag, CPU/memory, and task role (least privilege to queues/buckets — not `AdministratorAccess`).

```text
GitHub job → OIDC JWT → AWS STS AssumeRoleWithWebIdentity
       → short-lived keys → ECR push / ECS service update
```

Trade-off vs long-lived keys: slightly more IAM/OIDC setup up front; far less key-rotation and leak blast radius. Trade-off vs “deploy from a laptop”: CI is auditable and repeatable; laptop tokens are not.

### Worked example

Trust fragment (conceptual — align with [`../starter/oidc-aws-ecs.tf.example`](../starter/oidc-aws-ecs.tf.example); do not apply blindly):

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Federated": "arn:aws:iam::ACCOUNT:oidc-provider/token.actions.githubusercontent.com" },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {
        "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
      },
      "StringLike": {
        "token.actions.githubusercontent.com:sub": "repo:ORG/REPO:ref:refs/heads/main"
      }
    }
  }]
}
```

Example `sub` shapes (pin the tightest that fits the job; use immutable IDs when your repo mints them):

| Intent | Example `sub` |
|--------|----------------|
| Production deploys from `main` only (name-based) | `repo:ORG/REPO:ref:refs/heads/main` |
| Same, immutable owner/repo IDs | `repo:ORG@123456/REPO@456789:ref:refs/heads/main` |
| A protected GitHub Environment | `repo:ORG/REPO:environment:production` (or immutable ID form) |
| A single workflow file | Also constrain `job_workflow_ref` (path to the reusable/deploy workflow) in the trust policy |

Minimal Actions permissions for the deploy job:

```yaml
permissions:
  id-token: write   # required to mint the OIDC JWT
  contents: read
```

Why constrain `sub` to `main`: a feature-branch or fork job must not assume the production deploy role. Why Terraform for the trust: the condition is a reviewable diff — console clicks drift.
### Common misconceptions / what goes wrong

- **“OIDC alone is least privilege.”** Federation only answers *who can assume*; the role’s **permission** policy still decides blast radius (queues, buckets, ECS update). An open trust + admin role is worse than static keys you knew to rotate.
- **“Any `repo:ORG/REPO:*` subject is fine.”** Wildcard refs let a PR from a compromised branch request the token; pin `ref:refs/heads/main` (or an environment-gated subject) for production deploys.
- **“Name-based `sub` always matches.”** Repos on the immutable format (post–2026-07-15 creates / opt-in) mint `ORG@id/REPO@id` — a trust policy that only lists the old name-based string fails closed (or, after a rename, drifts). Teach both forms and pin `job_workflow_ref` / `environment` where possible.
- **“Forks inherit the same deploy path.”** Pull requests from forks may still request OIDC depending on permissions — treat `pull_request_target` and write tokens as high risk; see GitHub’s OIDC hardening docs.
- **“Task role = deploy role.”** The CI deploy role updates the service; the **task** role is what the running mail worker uses — keep them separate so a compromised container cannot redeploy itself as admin.


## Videos (verified)

1. **[GitHub Actions Certification – Full Course](https://www.youtube.com/watch?v=Tz7FsunBbfQ)**  
   Why it helps: OIDC permissions context in Actions.

## Read these (verified)

1. [GitHub Actions — OIDC with AWS](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
2. [AWS ECS on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
3. [Terraform AWS provider — IAM OIDC](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_openid_connect_provider)

## Starter sketch (do not apply blindly)

See [`../starter/oidc-aws-ecs.tf.example`](../starter/oidc-aws-ecs.tf.example). Why Terraform here: the trust condition and role are reviewable diffs — console clicks drift. Why constrain `sub`: so a feature-branch job cannot assume the production deploy role.

## On the job

Mail/identity services often land on ECS/Kubernetes behind CI. Interview and incident questions converge on the same mechanism: **who can assume the deploy role, from which repo/ref, and what can that role do afterward?**

## Next step

`oidc_aws` kata + starter Terraform sketch → quiz.
