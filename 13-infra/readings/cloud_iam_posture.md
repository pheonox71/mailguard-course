# Reading — Cloud IAM & misconfiguration posture

## Learning objectives

1. Explain Identity and Access Management (**IAM**) as identities + permissions + resources.
2. Apply a least-privilege review to a MailGuard bucket/queue role.
3. Describe shared responsibility at a high level (provider secures cloud; you secure *in* cloud).

**Why this matters.** Broken cloud IAM — public storage, wildcard `*` actions, root-like keys in CI — causes real incidents more often than exotic crypto bugs. Hold queues, Secure Drop objects, and worker roles all inherit whatever permissions you grant. Without a posture checklist, Terraform/`apply` can look “green” while leaving world-readable buckets or admin-equivalent runtime roles. On the job, cloud-security and identity teams review IAM before they review application code.

**How it works.**

1. IAM binds **principals** (users, roles, services) to **actions** on **resources** via policies.
2. Least privilege means the MailGuard API/worker role can read/write only the buckets and queues it needs — not `s3:*` / `iam:*` on `*`.
3. Shared responsibility: the provider secures the platform (datacenters, hypervisor, managed control planes); you secure accounts, identities, network exposure, encryption choices, and data *in* the cloud.
4. Practice the review against Module 13 Terraform/Compose (and the Module 12 CI deploy identity) — National Institute of Standards and Technology (**NIST**) vocabulary welcome; no cert wall.

```text
Identity (role) → Policy (Allow/Deny actions) → Resource (bucket/queue)
                      ↑
              CI OIDC / app runtime assumes this role
```

Trade-offs: broad roles ship features faster and explode blast radius; narrow roles need more planning when new queues appear. Prefer plan-time checks over “we’ll tighten later.”

### Worked example

Runtime role for a hold-queue worker (conceptual — tighten ARNs to your account):

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "HoldQueueOnly",
    "Effect": "Allow",
    "Action": [
      "sqs:ReceiveMessage",
      "sqs:DeleteMessage",
      "sqs:GetQueueAttributes"
    ],
    "Resource": "arn:aws:sqs:REGION:ACCOUNT:mailguard-hold"
  }]
}
```

Why not `sqs:*` on `*`: a compromised worker should not purge unrelated queues or create new ones. Pair with bucket **Block Public Access** on and no `Principal: "*"` object policies.

### Common misconceptions / what goes wrong

- **“Terraform applied cleanly, so IAM is fine.”** Apply success only means the API accepted the config — public buckets and `Action: "*"` still plan “green.”
- **“Shared responsibility means the cloud vendor owns my data exposure.”** The provider secures the *cloud*; you secure identities, policies, and data *in* the cloud.
- **“CI deploy role and app runtime role can be the same admin role.”** Separate them: deploy updates services; runtime talks to queues/buckets — compromise of the API process must not rewrite IAM.
- **“We’ll tighten wildcards after launch.”** Wildcard permissions rarely shrink later; posture checks belong in `plan`/CI, not a backlog ticket.

## Short intro

Broken cloud IAM (public storage, wildcard `*` actions, root-like keys in CI) causes real incidents more often than exotic crypto bugs. This reading prepares a checklist you will run against your Module 13 Terraform/Compose (and the Module 12 CI deploy identity) — National Institute of Standards and Technology (**NIST**) vocabulary welcome; no cert wall.

## Videos (verified)

1. Prefer [AWS IAM User Guide — Introduction](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) first (authoritative). Optional video: search freeCodeCamp / AWS “IAM explained” and confirm the current title before watching.  
   Why it helps: users/roles/policies mental model.

2. Optional: search “cloud misconfiguration public S3” conference talks for incident stories — treat as case studies, not product ads.

Prefer official IAM docs below if videos move.

## Annotated posture moves

| Check | Why that way |
|-------|----------------|
| No long-lived keys in git | History/forks leak; prefer OIDC / short-lived creds |
| Bucket Block Public Access on | Default-deny stops accidental `Principal: "*"` exposure |
| Runtime role ≠ admin | Compromise of the API process should not rewrite IAM |
| Secrets in a store / env, not state jokes | Terraform state can contain sensitive values — lock down remote state |

Example mindset for a lab-only misconfig: turn Block Public Access off and add a public bucket policy — then detect with `terraform plan`, a policy scanner, or a Scout/Prowler-class tool, and remediate. Why intentionally break a *lab* bucket: muscle memory for detection before production.

## Read these (verified)

1. [AWS IAM — User guide (roles & policies)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) — core model.
2. [AWS — Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
3. [CIS Amazon Web Services Foundations Benchmark](https://www.cisecurity.org/benchmark/amazon_web_services) — awareness of common hardened baselines (download may require form; skim public summaries OK).
4. [NIST CSF overview](https://www.nist.gov/cyberframework) — identify/protect framing without exam prep.
5. [OWASP — Cloud Native Application Security Top 10](https://owasp.org/projects/cloud-native-application-security-top-10) — cloud-native risks adjacent to IAM/misconfig posture (also see [CI/CD Security Top 10](https://owasp.org/www-project-top-10-ci-cd-security-risks/)).

## Next step

Continue with the assignment from the downloads on this page.
