# Terraform / HCL primer

**Why this matters.** Clicking a cloud console does not review well and drifts silently. **Terraform** expresses buckets, IAM, and queues as code so Module 13 can `plan` changes before they hit a real account. On the job, reviewers read the plan — not a console screenshot — when mail/identity infra changes.

**How it works.**

1. Write **HCL** (HashiCorp Configuration Language) describing desired resources (providers + `resource` blocks).
2. Run `terraform init` to download providers declared in the config.
3. Run `terraform plan` to see the create/update/destroy diff **before** any mutation.
4. Run `terraform apply` only when the plan is intentional; **state** maps real IDs back to your config — and must not be committed when it contains secrets.

```text
HCL config → init (providers) → plan (diff) → apply (cloud APIs) → state
```

This primer has no assignment, quiz, or download pack.

---

## What Terraform is

**Terraform** is an infrastructure-as-code tool. Config files commonly use the `.tf` extension and HCL syntax.

## Why industry uses it

Reviewable infra diffs, repeatable environments, and clearer least-privilege IAM stories. Security reviews often start from the plan output, not from a console screenshot.

## Key concepts for Module 13

| Concept | Why you care |
|---------|----------------|
| Providers | Talk to AWS (or others) via APIs |
| Resources | Bucket, queue, IAM policy blocks |
| `plan` vs `apply` | See blast radius before change |
| Remote state (awareness) | Team sharing without git-stored secrets; S3 `use_lockfile` needs TF ≥ 1.10 (versioning recommended) |
| `sensitive` vs write-only/ephemeral | `sensitive` redacts CLI but stays in state; write-only/ephemeral (TF ≥ 1.11) for one-shot secrets |

## Install and run

1. [Terraform install](https://developer.hashicorp.com/terraform/install)
2. Check: `terraform version`

You do not need cloud credentials for this primer — Module 13 documents plan against *your* resources or local stand-ins.

## Tiny hands-on example

### Worked example

Local-only HCL (no cloud account) so `plan` still teaches blast-radius review:

```hcl
# Conceptual — do not apply without credentials and a backend you own
terraform {
  required_version = ">= 1.10" # use_lockfile on S3 backend; ≥1.11 for write-only/ephemeral
}

# Why: a local_file resource proves HCL parses without a cloud account
resource "local_file" "primer" {
  filename = "${path.module}/primer-note.txt"
  content  = "mailguard terraform primer\n"
}
```

```bash
mkdir -p /tmp/mg-tf-primer && cd /tmp/mg-tf-primer
# Why /tmp: keep the primer throwaway; do not mix with real state
# paste the HCL into main.tf, then:
terraform init   # Why: download providers declared in the config
terraform plan   # Why: see the diff before any apply
```

**How:** `init` installs providers; `plan` shows it would create a local file — same discipline as planning IAM/bucket changes later.

### Common misconceptions / what goes wrong

- **“`plan` green means production is safe.”** Plan only shows *this* config’s diff; it does not prove least privilege, public-access blocks, or that remote state is locked down.
- **“Commit `terraform.tfstate` for the team.”** State often holds secrets and resource IDs — use a remote S3 backend with `use_lockfile = true` (versioning recommended) and access control, not git history.
- **“`sensitive = true` keeps secrets out of state.”** It only redacts display; learn write-only/ephemeral (TF ≥ 1.11) for one-shot credentials.
- **“Skip plan and just `apply -auto-approve`.”** You lose the blast-radius review that makes Terraform worth using for mail/identity IAM.


## Videos (verified)

1. **[Learn Terraform (and AWS) by Building a Dev Environment](https://www.youtube.com/watch?v=iRaai1IBlB0)** — freeCodeCamp  
   Why it helps: plan/apply mental model before Module 13.

## Official docs

1. [Terraform intro](https://developer.hashicorp.com/terraform/intro)
2. [Terraform install](https://developer.hashicorp.com/terraform/install)
3. [HCL language resources](https://developer.hashicorp.com/terraform/language)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`13-infra`).

This primer has **no** assignment, quiz, or download pack.
