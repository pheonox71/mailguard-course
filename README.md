# mailguard-course

CS grad choosing a year of deliberate challenge — building **cloud security SaaS** skills in public (identity / MFA, email DLP & missend prevention, secure transfer): Python → TypeScript/Vue → Go → AWS/Terraform/CI → K8s / observability / OIDC.

**Why:** Transformation through learning and challenge — ship hard problems, raise the bar, document trade-offs. Career prep for cloud security / identity / DLP engineering roles. Honest tenure; ambitious craft.

**Thread:** **MailGuard** — outbound message & file guard (identity / DLP / secure-transfer–shaped learning, not a product clone).

**Authorship:** Course structure, readings, stubs, tests, quizzes, and rubrics are AI-generated. Worksheet answers and kata implementations are filled in by the student on the `work` branch (not published on `main`).

**Start here (Module 0):** [SYLLABUS.md](./SYLLABUS.md) · [PREREQUISITES.md](./PREREQUISITES.md) · [GLOSSARY.md](./GLOSSARY.md) · [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md)

**Branches (blank course vs personal progress):**

| Branch | What you get |
|--------|----------------|
| **`main`** | The **blank course** — readings, videos, question-only worksheets, stub katas, tests, and reference solutions. Safe to share or fork as a clean curriculum. |
| **`work`** | The student’s private progress — filled answers under `my-answers/`, completed kata implementations. **Never merge `work` into `main`.** |

When the course is updated, changes land on `main` first, then merge `main` → `work` so progress keeps the new material without putting answers on the blank fork. Details: see Agent Store doc `course-branch-workflow.md` once GitHub is live, or keep answers only on `work`.

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
