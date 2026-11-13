# Assignment — IAM / misconfig posture

**Language / tooling:** **Terraform** (AWS) and **Docker Compose** for infra plans — not application JavaScript. Checklist answers are written Markdown.

## Checklist (mark yes/no/n/a on *your* plan)

| Control | Y/N/NA | Evidence |
|---------|--------|----------|
| No long-lived access keys in git | | |
| Bucket default deny public | | |
| Role for app has only needed actions | | |
| CI uses OIDC/short-lived creds or documented exception | | |
| Admin-equivalent policy not attached to runtime role | | |
| Secrets via env/secret store, not Terraform state jokes | | |

## Intentional misconfig (lab only)

1. Describe one misconfig you could introduce locally (e.g. public-read ACL on a *lab* bucket).
2. How would you detect it (console, `plan`, policy check, Scout/Prowler-class tool — name one)?
3. Remediation steps.

## Shared responsibility (3 sentences)

What the provider covers vs what you cover for object storage used by Secure Drop.
