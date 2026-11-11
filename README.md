# hennge-learning

CS grad choosing a year of deliberate challenge — building [HENNGE One](https://hennge.com/global/service/one/)–shaped skills in public (Identity / DLP / secure transfer): Python → TypeScript/Vue → Go → AWS/Terraform/CI → K8s / observability / OIDC.

**Why:** Transformation through learning and challenge — ship hard problems, raise the bar, document trade-offs. Near-term: stronger [GIP Full-Stack](https://recruit.hennge.com/en/gip/) reapplication. Long-run: same MailGuard thread + real experience toward a [direct engineering hire](https://recruit.hennge.com/en/mid-career-ngh/) when year bars are met. Honest tenure; ambitious craft.

**Thread:** **MailGuard** — outbound message & file guard (Identity / DLP / Secure Transfer–shaped learning, not a product clone).

| Folder | Phase | Teaches | HENNGE signal |
|--------|-------|---------|---------------|
| [`01-challenge-gym/`](./01-challenge-gym/) | A | Concise Python + TOTP/pytest under a challenge bar | [Hiring process interview](https://hennge.com/global/info/henka/interview/202406-demystifying_hennges_hiring_process/) |
| `02-mailguard-api/` | A→B | FastAPI DLP-ish rule API | [Access Control](https://recruit.hennge.com/en/mid-career-ngh/senior-software-engineer-python-web-dev-hennge-access-control/) |
| `03-mailguard-mfa/` | A→B | MFA/OTP on the API | [GIP](https://recruit.hennge.com/en/gip/) · MFA challenge theme |
| `04-mailguard-admin/` | A→B | TypeScript/Vue admin | [GIP](https://recruit.hennge.com/en/gip/) |
| `05-mailguard-worker/` | A→B | Go worker / queue path | Secure Transfer–shaped workers |
| `06-secure-drop/` | A→B | Secure file transfer lite | [Secure Transfer](https://recruit.hennge.com/en/mid-career-ngh/senior-software-engineer-backend-infra-hennge-secure-transfer/) |
| `07-ci-aws/` | A→B | GitHub Actions + AWS deploy | GIP DevOps + mid-career cloud |
| `08-infra/` | A→B | Compose + Terraform | [Platform](https://recruit.hennge.com/en/mid-career-ngh/platform-engineer/) |
| `09-phish-lite/` | B opt. | Svelte phishing quiz | [Tadrill](https://recruit.hennge.com/en/mid-career-ngh/senior-frontend-engineer-svelte-tadrill/) |
| `10-security-notes/` | A→B | OWASP → MailGuard mitigations | [HENNGE One](https://hennge.com/global/service/one/) |
| `11-k8s-local/` | B | kind/minikube deploy | [Platform Engineer](https://recruit.hennge.com/en/mid-career-ngh/platform-engineer/) |
| `12-observability/` | B | Metrics/logs/traces | Platform observability prefs |
| `13-oidc-access/` | B | OIDC + access policy lite | Identity Edition literacy |
| `14-gitops-policy/` | B | GitOps + policy-as-code concepts | ArgoCD / Kyverno on Platform JD |

**Status:** `01-challenge-gym/` is implemented locally. Remaining folders are planned — see the learning series plan. GitHub remote `pheonox71/hennge-learning` is not live yet.

**How to run (latest):**

```bash
cd 01-challenge-gym
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
