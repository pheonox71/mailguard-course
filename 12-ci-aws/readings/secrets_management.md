# Reading — Practical secrets management

## Learning objectives

1. Prefer cloud **Secrets Manager / SSM Parameter Store** (or equivalent) over plaintext env in git.
2. Use **SOPS** (or similar) for encrypted-at-rest secrets in git when needed.
3. Plan **rotation** and least-privilege access to secret material.

**Why this matters.** Long-lived keys in repositories and chat logs are a top incident class for CI and cloud mail/identity workloads. Without a secrets store and rotation story, every laptop and Actions runner becomes a potential leak. On the job, reviewers ask where the secret lives, who can read it, and how often it rotates.

**How it works.**

1. Classify secrets (DB passwords, API tokens, webhook HMAC keys) — never commit real values.
2. Store production secrets in a managed store (**AWS Secrets Manager** or **SSM SecureString**).
3. Grant IAM roles (OIDC deploy role / task role) `GetSecretValue` / `ssm:GetParameter` on *named* resources only.
4. For git-held config, encrypt with **SOPS** + KMS/age so the ciphertext can live in-repo while keys stay in KMS.
5. Rotate on a schedule and on suspicion; update consumers via redeploy, not by editing old commits.

```text
Developer → (no plaintext in git)
CI OIDC role → Secrets Manager / SSM → runtime env / file mount
Optional: SOPS ciphertext in git → decrypt with KMS in CI
```

### Worked example

IAM fragment (conceptual — tighten ARNs to your account):

```json
{
  "Effect": "Allow",
  "Action": ["secretsmanager:GetSecretValue"],
  "Resource": ["arn:aws:secretsmanager:REGION:ACCOUNT:secret:mailguard/prod/*"]
}
```

SOPS sketch (do not commit real keys):

```bash
# Encrypt a plaintext values file for git (age or KMS backend in real labs).
# Why --output / a separate path: shell redirection (`> secrets.enc.yaml`) truncates
# the target *before* sops reads it when input and output are the same path —
# you would encrypt an empty file and lose the plaintext. Prefer --output, or
# write ciphertext to a different name.
sops --encrypt --age "$AGE_PUBLIC_KEY" --output secrets.enc.yaml secrets.yaml
# Equivalent: sops --encrypt --age "$AGE_PUBLIC_KEY" secrets.yaml > secrets.enc.yaml
```

### Common misconceptions / what goes wrong

- **“`.env` in the repo is fine if gitignored on my machine.”** Teammates and CI will copy it; use examples with placeholders only.
- **“Base64 is encryption.”** Encoding is not confidentiality.
- **“Redirect ciphertext onto the same path as the plaintext input.”** `sops … secrets.yaml > secrets.yaml` truncates the file first; use `--output` or a distinct ciphertext filename.
- **“Rotation means wait for expiry.”** Also rotate after personnel changes and suspected leaks.
- **“The deploy role can read all secrets.”** Scope to named prefixes; separate task role from deploy role.

## Read these (verified)

1. [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/)
2. [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
3. [SOPS](https://github.com/getsops/sops)

## Next step

Document where *your* lab secrets live (local `.env` vs cloud store) in the Module 12/13 assignments — never paste real values into the course repo.
