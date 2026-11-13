# Terraform / HCL primer

**Why this matters.** Clicking a cloud console does not review well and drifts silently. **Terraform** expresses buckets, IAM, and queues as code so Module 13 can `plan` changes before they hit a real account.

**How it works.** You write **HCL** (HashiCorp Configuration Language) describing desired resources. `terraform plan` shows a diff; `apply` mutates cloud APIs; **state** maps real IDs back to your config — and must not be committed when it contains secrets.

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
| Remote state (awareness) | Team sharing without git-stored secrets |

## Install and run

1. [Terraform install](https://developer.hashicorp.com/terraform/install)
2. Check: `terraform version`

You do not need cloud credentials for this primer — Module 13 documents plan against *your* resources or local stand-ins.

## Tiny hands-on example

```hcl
# Conceptual — do not apply without credentials and a backend you own
terraform {
  required_version = ">= 1.5"
}

# Why: a local_file resource proves HCL parses without a cloud account
resource "local_file" "primer" {
  filename = "${path.module}/primer-note.txt"
  content  = "mailguard terraform primer\n"
}
```

```bash
mkdir -p /tmp/mg-tf-primer && cd /tmp/mg-tf-primer
# paste the HCL into main.tf, then:
terraform init
terraform plan
```

**How:** `init` installs providers; `plan` shows it would create a local file — same discipline as planning IAM/bucket changes later.

## Official docs

1. [Terraform intro](https://developer.hashicorp.com/terraform/intro)
2. [Terraform install](https://developer.hashicorp.com/terraform/install)
3. [HCL language resources](https://developer.hashicorp.com/terraform/language)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`13-infra`).

This primer has **no** assignment, quiz, or download pack.
