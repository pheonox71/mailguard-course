# Assignment — IAM / misconfig posture

**Language / tooling:** **Terraform** (AWS) and **Docker Compose** for infra plans — not application JavaScript. Checklist answers are written Markdown.

## Checklist (mark yes/no/n/a on *your* plan)

For each row, add a one-line **why** in Evidence (not only a path).

| Control | Y/N/NA | Evidence (+ why) |
|---------|--------|------------------|
| No long-lived access keys in git | | |
| Bucket default deny public | | |
| Role for app has only needed actions | | |
| CI uses OIDC/short-lived creds or documented exception | | |
| Admin-equivalent policy not attached to runtime role | | |
| Secrets via env/secret store, not Terraform state jokes | | |

## Intentional misconfig (lab only)

1. Describe one misconfig you could introduce locally (e.g. public-read ACL on a *lab* bucket). **Why** would that be dangerous if it leaked to a real account?
2. **How** would you detect it (console, `plan`, policy check, Scout/Prowler-class tool — name one)? Why that detector?
3. Remediation steps in order — **why** that order (contain → fix → verify).

## Shared responsibility (3 sentences)

What the provider covers vs what you cover for object storage used by Secure Drop. End with **why it matters on the job** when a hold/attachment bucket is misconfigured.
