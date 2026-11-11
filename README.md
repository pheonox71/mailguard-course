# mailguard-course

CS grad choosing a year of deliberate challenge — building **cloud security SaaS** skills in public (identity / MFA, email DLP & missend prevention, secure transfer): Python → TypeScript/Vue → Go → AWS/Terraform/CI → K8s / observability / OIDC.

**Why:** Transformation through learning and challenge — ship hard problems, raise the bar, document trade-offs. Career prep for cloud security / identity / DLP engineering roles. Honest tenure; ambitious craft.

**Thread:** **MailGuard** — outbound message & file guard (identity / DLP / secure-transfer–shaped learning, not a product clone).

**Authorship:** Course structure, readings, stubs, and tests are AI-generated. Worksheets answers and kata implementations are filled in by Chance.

| Folder | Phase | Teaches | Career / skill focus |
|--------|-------|---------|----------------------|
| [`01-challenge-gym/`](./01-challenge-gym/) | A | Concise Python + TOTP/pytest under a challenge bar | MFA/OTP literacy; elegant short solutions |
| `02-mailguard-api/` | A→B | FastAPI DLP-ish rule API | Identity / access-policy style backend |
| `03-mailguard-mfa/` | A→B | MFA/OTP on the API | MFA challenge theme |
| `04-mailguard-admin/` | A→B | TypeScript/Vue admin | Full-stack SaaS admin UX |
| `05-mailguard-worker/` | A→B | Go worker / queue path | Secure-transfer–shaped workers |
| `06-secure-drop/` | A→B | Secure file transfer lite | Backend / secure sharing |
| `07-ci-aws/` | A→B | GitHub Actions + AWS deploy | DevOps + cloud deploy |
| `08-infra/` | A→B | Compose + Terraform | Platform / infra-as-code |
| `09-phish-lite/` | B opt. | Svelte phishing quiz | Security awareness frontend |
| `10-security-notes/` | A→B | OWASP → MailGuard mitigations | Threat models for the MailGuard thread |
| `11-k8s-local/` | B | kind/minikube deploy | Platform / Kubernetes basics |
| `12-observability/` | B | Metrics/logs/traces | Platform observability |
| `13-oidc-access/` | B | OIDC + access policy lite | Identity & access literacy |
| `14-gitops-policy/` | B | GitOps + policy-as-code concepts | GitOps / policy engines |

**Status:** `01-challenge-gym/` is implemented locally. Remaining folders are planned. Public display name: **mailguard-course**.

**How to run (latest):**

```bash
cd 01-challenge-gym
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
