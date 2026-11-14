# 13 — Infra (+ cloud IAM / misconfig posture)

**Language / tooling:** Terraform (AWS) + Docker Compose — not application JavaScript.

Compose + Terraform for the MailGuard story, extended with Identity and Access Management (**IAM**) least-privilege review and intentional misconfig detection literacy.

## What this teaches

- `compose up` demos; Terraform `plan` for bucket/IAM/queue (or equivalent)
- Least-privilege IAM checklists; shared-responsibility awareness
- Spotting common misconfigs (public buckets, admin-equivalent roles, long-lived keys in git)

## Start here

1. [`readings/container_images.md`](./readings/container_images.md) — build `mailguard-api:local` / worker images
2. [`readings/terraform_plan_walkthrough.md`](./readings/terraform_plan_walkthrough.md) — init → validate → plan
3. [`readings/cloud_iam_posture.md`](./readings/cloud_iam_posture.md)
4. Quiz → assignment (checklist against your Terraform/Compose)
5. Infra as code for storage/IAM/queue

**Done when:** compose demo + Terraform plan documented; IAM assignment checklist completed for *your* resources.

## Starter

See `starter/docker-compose.yml`, `starter/main.tf.example` (provider + commented remote backend + S3/SQS/IAM), and `starter/iam_policy_mailguard.json` / `.tf.hcl`. Run `pytest -q` after implementing `katas/compose_checks.py`.
