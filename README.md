# mailguard-course

CS grad choosing a year of deliberate challenge — building **cloud security SaaS** skills in public (identity / MFA, email DLP & missend prevention, secure transfer): Python → TypeScript/Vue → Go → AWS/Terraform/CI → K8s / observability / OIDC.

**Why:** Transformation through learning and challenge — ship hard problems, raise the bar, document trade-offs. Career prep for cloud security / identity / DLP engineering roles. Honest tenure; ambitious craft.

**Thread:** **MailGuard** — outbound message & file guard (identity / DLP / secure-transfer–shaped learning, not a product clone).

**Authorship:** Course structure, readings, stubs, tests, quizzes, and rubrics are AI-generated. Worksheet answers, filled quiz PDFs, and kata implementations are filled in by the student under [`my-work/`](./my-work/).

**Start here (Module 0):** [SYLLABUS.md](./SYLLABUS.md) · [PREREQUISITES.md](./PREREQUISITES.md) · [GLOSSARY.md](./GLOSSARY.md) · [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md) · student site in [`site/`](./site/)

**Where finished work goes:**

| Path | What you put there |
|------|--------------------|
| [`my-work/worksheets/`](./my-work/worksheets/) | Completed worksheet answers |
| [`my-work/quizzes/`](./my-work/quizzes/) | Filled quiz PDFs from the course site |

Leave blank worksheets/quizzes under each module unchanged. Implement kata stubs in place; keep written answers in `my-work/`.

| Folder | Phase | Teaches | Career / skill focus |
|--------|-------|---------|----------------------|
| [`01-challenge-gym/`](./01-challenge-gym/) | A | Concise Python + TOTP/pytest + crypto hygiene | MFA/OTP literacy; HMAC/AEAD misuse avoidance |
| [`02-mailguard-mfa/`](./02-mailguard-mfa/) | A | MFA/OTP + passkeys / WebAuthn literacy | Phishing-resistant MFA |
| [`03-oidc-access/`](./03-oidc-access/) | A | OIDC + SAML / device certs / password-vault literacy | Identity & access depth |
| [`04-ztna-lite/`](./04-ztna-lite/) | A | ZTNA vs VPN concepts | Zero-trust access literacy |
| [`05-email-auth/`](./05-email-auth/) | A | SPF / DKIM / DMARC + SMTP/TLS | Email domain authentication |
| [`06-threat-model/`](./06-threat-model/) | A | STRIDE / lightweight secure SDLC | Threat modeling before build |
| [`07-mailguard-api/`](./07-mailguard-api/) | A | FastAPI DLP-ish rule API | Identity / access-policy style backend |
| [`08-mailguard-admin/`](./08-mailguard-admin/) | A | TypeScript/Vue admin | Full-stack SaaS admin UX |
| [`09-mailguard-worker/`](./09-mailguard-worker/) | A | Go worker / queue path | Secure-transfer–shaped workers |
| [`10-secure-drop/`](./10-secure-drop/) | A | Secure file transfer + cloud-share DLP | Share-link governance |
| [`11-security-notes/`](./11-security-notes/) | A | OWASP → MailGuard mitigations | Threat notes for the MailGuard thread |
| [`12-ci-aws/`](./12-ci-aws/) | A | GitHub Actions + AWS deploy | DevOps + cloud deploy |
| [`13-infra/`](./13-infra/) | A | Compose + Terraform + IAM posture | Platform / least-privilege IaC |
| [`14-k8s-local/`](./14-k8s-local/) | B | kind/minikube deploy | Platform / Kubernetes basics |
| [`15-observability/`](./15-observability/) | B | Metrics/logs/traces + SRE (SLI/SLO) | Observability + reliability |
| [`16-gitops-policy/`](./16-gitops-policy/) | B | GitOps + policy-as-code concepts | GitOps / policy engines |
| [`17-phish-lite/`](./17-phish-lite/) | B opt. | Svelte phishing quiz | Security awareness frontend |
| [`18-oss-ux-stretch/`](./18-oss-ux-stretch/) | B opt. | OSS contribution + security UX notes | Collaboration / portfolio signals |

**How to run (Challenge Gym):**

```bash
cd 01-challenge-gym
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

**Email-auth kata:**

```bash
cd 05-email-auth
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
