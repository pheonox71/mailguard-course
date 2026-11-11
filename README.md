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

When the course is updated, changes land on `main` first, then merge `main` → `work` so progress keeps the new material without putting answers on the blank fork.

| Folder | Phase | Teaches | Career / skill focus |
|--------|-------|---------|----------------------|
| [`01-challenge-gym/`](./01-challenge-gym/) | A | Concise Python + TOTP/pytest + **crypto hygiene** | MFA/OTP literacy; HMAC/AEAD misuse avoidance |
| `02-mailguard-api/` | A→B | FastAPI DLP-ish rule API | Identity / access-policy style backend |
| [`03-mailguard-mfa/`](./03-mailguard-mfa/) | A→B | MFA/OTP + **passkeys / WebAuthn** literacy | MFA challenge theme; phishing-resistant factors |
| `04-mailguard-admin/` | A→B | TypeScript/Vue admin | Full-stack SaaS admin UX |
| `05-mailguard-worker/` | A→B | Go worker / queue path | Secure-transfer–shaped workers |
| [`06-secure-drop/`](./06-secure-drop/) | A→B | Secure file transfer + **cloud-share DLP** | Backend / share-link governance |
| `07-ci-aws/` | A→B | GitHub Actions + AWS deploy | DevOps + cloud deploy |
| [`08-infra/`](./08-infra/) | A→B | Compose + Terraform + **IAM posture** | Platform / least-privilege IaC |
| `09-phish-lite/` | B opt. | Svelte phishing quiz | Security awareness frontend |
| `10-security-notes/` | A→B | OWASP → MailGuard mitigations | Threat notes for the MailGuard thread |
| [`15-email-auth/`](./15-email-auth/) | A | **SPF / DKIM / DMARC** + SMTP/TLS | Email domain authentication |
| [`16-threat-model/`](./16-threat-model/) | A | **STRIDE / lightweight secure SDLC** | Threat modeling before capstone |
| `11-k8s-local/` | B | kind/minikube deploy | Platform / Kubernetes basics |
| [`12-observability/`](./12-observability/) | B | Metrics/logs/traces + **SRE (SLI/SLO)** | Platform observability + reliability |
| [`13-oidc-access/`](./13-oidc-access/) | B | OIDC + **SAML / device certs / password vault** literacy | Identity & access depth |
| [`17-ztna-lite/`](./17-ztna-lite/) | B | **ZTNA** vs VPN concepts | Zero-trust access literacy |
| `14-gitops-policy/` | B | GitOps + policy-as-code concepts | GitOps / policy engines |
| [`18-oss-ux-stretch/`](./18-oss-ux-stretch/) | B opt. | **OSS contribution** + security UX notes | Collaboration / portfolio signals |

**Progression note:** `01`–`14` keep their numbers. `15`–`18` add high-priority literacy without reshuffling earlier folders — see [SYLLABUS.md](./SYLLABUS.md).

**Status:** `01-challenge-gym/` and new/extended literacy modules (`03` passkeys, `06` share-DLP, `08` IAM, `12` SRE, `13` identity depth, `15`–`18`) ship readings/worksheets/quizzes (plus katas where noted). Remaining product folders are still implementation-planned. Public display name: **mailguard-course**.

**How to run (Challenge Gym):**

```bash
cd 01-challenge-gym
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

**Email-auth kata:**

```bash
cd 15-email-auth
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
