# Reading — OIDC to AWS + ECS

## Learning objectives

1. Prefer **GitHub Actions OIDC** over long-lived `AWS_ACCESS_KEY_ID` secrets.
2. Constrain role trust by `sub` (repo + ref).
3. Sketch an ECS Fargate deploy from CI.

**Why this matters.** Static AWS keys in repository secrets still leak via mis-logged env dumps, overly broad `permissions:`, and compromised maintainers. Federation with OpenID Connect (**OIDC**) issues **short-lived** credentials only when a trusted workflow runs. Without a tight trust policy (`sub` = this repo + `main`), any branch or fork workflow that can request the token becomes a cloud admin path. On the job, cloud-security reviews almost always ask how CI authenticates to the account that runs gateways, queues, and mail workers.

**How it works.**

1. Register GitHub’s OIDC issuer (`token.actions.githubusercontent.com`) as an Identity and Access Management (**IAM**) OIDC provider in AWS.
2. Create an IAM role whose trust policy allows `sts:AssumeRoleWithWebIdentity` only when JWT claims match (commonly `sub` like `repo:ORG/REPO:ref:refs/heads/main`).
3. In Actions, request an ID token, call AssumeRoleWithWebIdentity (often via `aws-actions/configure-aws-credentials`), then push an image and update **Amazon Elastic Container Service (ECS)** on **Fargate** (serverless tasks — no EC2 capacity management for the task itself).
4. Task definition pins image digest/tag, CPU/memory, and task role (least privilege to queues/buckets — not `AdministratorAccess`).

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

Why constrain `sub` to `main`: a feature-branch or fork job must not assume the production deploy role. Why Terraform for the trust: the condition is a reviewable diff — console clicks drift.

### Common misconceptions / what goes wrong

- **“OIDC alone is least privilege.”** Federation only answers *who can assume*; the role’s **permission** policy still decides blast radius (queues, buckets, ECS update). An open trust + admin role is worse than static keys you knew to rotate.
- **“Any `repo:ORG/REPO:*` subject is fine.”** Wildcard refs let a PR from a compromised branch request the token; pin `ref:refs/heads/main` (or an environment-gated subject) for production deploys.
- **“Forks inherit the same deploy path.”** Pull requests from forks may still request OIDC depending on permissions — treat `pull_request_target` and write tokens as high risk; see GitHub’s OIDC hardening docs.
- **“Task role = deploy role.”** The CI deploy role updates the service; the **task** role is what the running mail worker uses — keep them separate so a compromised container cannot redeploy itself as admin.

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
