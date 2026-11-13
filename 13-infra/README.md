# 13 — Infra (+ cloud IAM / misconfig posture)

**Language / tooling:** Terraform (AWS) + Docker Compose — not application JavaScript.

Compose + Terraform for the MailGuard story, extended with Identity and Access Management (**IAM**) least-privilege review and intentional misconfig detection literacy.

## What this teaches

- `compose up` demos; Terraform `plan` for bucket/IAM/queue (or equivalent)
- Least-privilege IAM checklists; shared-responsibility awareness
- Spotting common misconfigs (public buckets, admin-equivalent roles, long-lived keys in git)

## Start here

1. [`readings/cloud_iam_posture.md`](./readings/cloud_iam_posture.md)
2. Quiz → worksheet (checklist against your Terraform/Compose)
3. Infra as code for storage/IAM/queue

**Done when:** compose demo + Terraform plan documented; IAM worksheet checklist completed for *your* resources.
