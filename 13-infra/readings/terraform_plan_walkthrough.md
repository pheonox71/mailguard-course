# Reading — Terraform plan walkthrough

## Learning objectives

1. Explain **why** `terraform plan` exists before any cloud mutation.
2. Walk **how** init → validate → plan → (optional) apply works for MailGuard storage/queue/IAM.
3. Spot dangerous plan diffs (public bucket, wildcard IAM) before you type `yes`.

**Why this matters.** Clicking “create bucket” in a console does not produce a reviewable diff. Hold-queue workers and Secure Drop objects inherit whatever Identity and Access Management (**IAM**) you attach; a bad apply can leave a public bucket or an admin-equivalent role. `terraform plan` shows the intended create/update/destroy set so a reviewer can reject wildcards *before* the account changes. On the job, platform and security teams read the plan — not a console screenshot — when mail/identity infra changes.

**How it works.**

1. **Write** HCL for provider, (optional) remote backend, and resources (see [`../starter/main.tf.example`](../starter/main.tf.example)).
2. **`terraform init`** downloads providers and configures the backend (local by default; remote S3 with **`use_lockfile = true`** when uncommented — needs Terraform **≥ 1.10**; state-bucket **versioning is recommended**, not required for the lockfile).
3. **`terraform validate`** checks syntax/types without talking to the cloud APIs for mutations.
4. **`terraform plan`** refreshes state, computes a diff, and prints `+` / `~` / `-` actions — still no apply.
5. Only if the plan is least-privilege and Block Public Access is on, run **`terraform apply`** (or apply a saved plan file).
6. Re-run plan after edits; treat unexpected destroys as stop-the-line.
7. Secrets literacy (Terraform **≥ 1.11**): `sensitive = true` redacts CLI display but **still stores** the value in state; **write-only / ephemeral** attributes pass secrets into apply without the ordinary state persistence of regular variables — prefer them for one-shot credentials.

```text
HCL → init (providers/backend) → validate → plan (diff) → apply (mutate)
                                      ↑
                         reject wildcards / public exposure here
```

Trade-off: local state is simplest for a solo lab and easy to lose or leak; remote state with **`use_lockfile`** (TF ≥ 1.10; versioned bucket recommended) is safer for teams than committing state. Legacy DynamoDB lock tables still work but are optional when `use_lockfile` is on. Prefer plan-time review over “apply and fix later.”

### Worked example

Lab-safe walkthrough using the starter example (copy aside; do not commit secrets or real account IDs):

```bash
# Why a private copy: keep course git clean of terraform.tfstate and *.tfvars secrets
cp -r 13-infra/starter /tmp/mailguard-tf && cd /tmp/mailguard-tf
cp main.tf.example main.tf

# Why init first: providers are not vendored in the repo
terraform init

# Why validate before plan: catch typos without needing cloud credentials
terraform validate

# Why pass -var on the CLI for labs: avoids committing tfvars with account specifics
terraform plan \
  -var='bucket_name=mailguard-secure-drop-lab-UNIQUE' \
  -var='environment=dev'

# Read the plan:
#   + aws_s3_bucket.secure_drop
#   + aws_s3_bucket_public_access_block.secure_drop   # must stay true/true/true/true
#   + aws_sqs_queue.hold
#   + aws_iam_role.mailguard_runtime
#   + aws_iam_role_policy.mailguard_runtime           # check Action lists — no "*"
```

Least-privilege IAM shape (also in [`../starter/iam_policy_mailguard.json`](../starter/iam_policy_mailguard.json)):

```json
{
  "Effect": "Allow",
  "Action": ["sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes"],
  "Resource": "arn:aws:sqs:REGION:ACCOUNT_ID:mailguard-hold-dev"
}
```

Why not `sqs:*` on `*`: a compromised worker should not purge unrelated queues. Pair with S3 Block Public Access on.

### Common misconceptions / what goes wrong

- **“Plan is optional if I trust my HCL.”** Apply without plan skips the human diff review — wildcards and public policies still “succeed.”
- **“Terraform applied cleanly, so IAM is fine.”** Apply success only means the API accepted the config; posture is a separate checklist ([`cloud_iam_posture.md`](./cloud_iam_posture.md)).
- **“Commit terraform.tfstate for the team.”** State can hold sensitive attributes; use a remote backend with encryption + **`use_lockfile`** (versioning recommended), never git.
- **“`sensitive = true` means the secret is not in state.”** It only redacts UI; write-only/ephemeral (TF ≥ 1.11) is the literacy for not persisting one-shot secrets the ordinary way.
- **“`Action: \"*\"` is fine for a weekend lab role.”** Lab habits leak into prod; start narrow and add statements when a new queue appears.
- **“Uncomment the S3 backend with placeholder names and apply.”** Backend config must point at buckets *you* own (`use_lockfile` works without versioning; enable versioning for recovery) — placeholders fail loudly; never paste real access keys into HCL.

## Read these (verified)

1. [Terraform — Command: plan](https://developer.hashicorp.com/terraform/cli/commands/plan)
2. [Terraform — Backend: S3](https://developer.hashicorp.com/terraform/language/backend/s3) — `use_lockfile` (TF ≥ 1.10); versioning recommended
3. [Terraform — Sensitive data in state](https://developer.hashicorp.com/terraform/language/state/sensitive-data) · [Ephemeral values](https://developer.hashicorp.com/terraform/language/resources/ephemeral) (TF ≥ 1.11 write-only/ephemeral literacy)
4. [AWS IAM — Policies and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
5. [Amazon S3 — Blocking public access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## Next step

Continue with the [cloud IAM posture assignment](../assignments/cloud_iam_posture.md) against *your* plan output.
