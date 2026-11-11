# Reading — Cloud IAM & misconfiguration posture

## Learning objectives

1. Explain Identity and Access Management (**IAM**) as identities + permissions + resources.
2. Apply a least-privilege review to a MailGuard bucket/queue role.
3. Describe shared responsibility at a high level (provider secures cloud; you secure *in* cloud).

## Short intro

Broken cloud IAM (public storage, wildcard `*` actions, root-like keys in CI) causes real incidents more often than exotic crypto bugs. This reading prepares a checklist you will run against module 08 infra — National Institute of Standards and Technology (**NIST**) vocabulary welcome; no cert wall.

## Videos (verified)

1. Prefer [AWS IAM User Guide — Introduction](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) first (authoritative). Optional video: search freeCodeCamp / AWS “IAM explained” and confirm the current title before watching.  
   Why it helps: users/roles/policies mental model.

2. Optional: search “cloud misconfiguration public S3” conference talks for incident stories — treat as case studies, not product ads.

Prefer official IAM docs below if videos move.

## Read these (verified)

1. [AWS IAM — User guide (roles & policies)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) — core model.
2. [AWS — Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
3. [CIS Amazon Web Services Foundations Benchmark](https://www.cisecurity.org/benchmark/amazon_web_services) — awareness of common hardened baselines (download may require form; skim public summaries OK).
4. [NIST CSF overview](https://www.nist.gov/cyberframework) — identify/protect framing without exam prep.
5. [OWASP — Cloud Security](https://owasp.org/www-project-cloud-security/) — project landing / cheat-adjacent material.

## Self-check

[`../quizzes/cloud_iam_posture.md`](../quizzes/cloud_iam_posture.md)
