# Module 0 — Syllabus

Orientation for **mailguard-course**: ordered modules, rough hours, progress checkboxes, and **done when** criteria. Work top → bottom for Phase A (`01`–`08`, `10`). Phase B (`09`, `11`–`14`) can overlap once the MailGuard core API, admin, CI, and infra exist.

**Authorship:** Course structure, readings, stubs, tests, quizzes, and rubrics are AI-generated. Worksheet answers and kata implementations are filled in by the learner (on the `work` branch — see root README).

**Related:** [PREREQUISITES.md](./PREREQUISITES.md) · [GLOSSARY.md](./GLOSSARY.md) · [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md)

---

## How to use this syllabus

1. Confirm [prerequisites](./PREREQUISITES.md), skim the [glossary](./GLOSSARY.md).
2. For each module: open its README → readings → worksheet → implement → tests / demo → self-check quiz (when present).
3. Tick the checkbox when that module’s **Done when** is met from *your* work (not by copying `solutions/`).
4. Capstone readiness is judged by [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md), not by finishing every stretch folder.

Hours are **solo learner estimates** (CS background, Python-strong). They include reading + worksheets + implementation + a short writeup — not calendar deadlines.

---

## Progress overview

| Phase | Modules | Est. hours (sum) |
|-------|---------|------------------|
| **A — Survey** | `01`–`08`, `10` | ~80–100 h |
| **B — Stretch** | `09` (opt.), `11`–`14` | ~40–50 h |
| **Capstone polish** | Cross-cutting demo + rubric | ~8–12 h |

---

## Module checklist

### Phase A

- [ ] **01 — Challenge Gym** · ~6–8 h · [`01-challenge-gym/`](./01-challenge-gym/)  
  **Done when:** All Challenge Gym tests green from *your* `katas/`; ≤1 page trade-offs; self-check quizzes attempted after each reading.

- [ ] **02 — MailGuard API** · ~12–16 h · [`02-mailguard-api/`](./02-mailguard-api/)  
  **Done when:** CRUD + hold/release; rules unit-tested; architecture notes in the module README.

- [ ] **03 — MailGuard MFA** · ~8–10 h · [`03-mailguard-mfa/`](./03-mailguard-mfa/)  
  **Done when:** Enroll/verify TOTP; one-time recovery codes; no secrets in git.

- [ ] **04 — MailGuard Admin** · ~12–16 h · [`04-mailguard-admin/`](./04-mailguard-admin/)  
  **Done when:** Rules + hold queue usable end-to-end against the API; TypeScript strict; a few component/e2e tests.

- [ ] **05 — MailGuard Worker** · ~10–12 h · [`05-mailguard-worker/`](./05-mailguard-worker/)  
  **Done when:** Local queue demo behind an interface; short Python-vs-Go contract note.

- [ ] **06 — Secure Drop** · ~8–10 h · [`06-secure-drop/`](./06-secure-drop/)  
  **Done when:** Upload → object storage → time-limited link + audit log demo (MinIO/LocalStack OK).

- [ ] **07 — CI + AWS** · ~8–10 h · [`07-ci-aws/`](./07-ci-aws/)  
  **Done when:** PR CI green (lint/test/image as applicable); one documented cloud deploy; no secrets in git.

- [ ] **08 — Infra** · ~10–12 h · [`08-infra/`](./08-infra/)  
  **Done when:** `compose up` demos the MailGuard story; Terraform `plan` documented for bucket/IAM/queue (or equivalent).

- [ ] **10 — Security notes** · ~6–8 h · [`10-security-notes/`](./10-security-notes/)  
  **Done when:** ≥5 lab notes mapped to MailGuard mitigations; no attacks on real systems.

### Phase B (stretch)

- [ ] **09 — Phish Lite** *(optional)* · ~6–8 h · [`09-phish-lite/`](./09-phish-lite/)  
  **Done when:** Quiz → results chart; README states learning-purpose honesty.

- [ ] **11 — K8s local** · ~10–12 h · [`11-k8s-local/`](./11-k8s-local/)  
  **Done when:** App healthy on kind/minikube; probes + resource requests; README names managed K8s / GitOps as next steps.

- [ ] **12 — Observability** · ~8–10 h · [`12-observability/`](./12-observability/)  
  **Done when:** Local stack shows golden signals for API + worker; one failure story diagnosed via telemetry; alert *idea* documented.

- [ ] **13 — OIDC / access policy** · ~8–10 h · [`13-oidc-access/`](./13-oidc-access/)  
  **Done when:** Happy-path OIDC login + protected route/API; logout/revocation notes; no inflated SSO claims.

- [ ] **14 — GitOps + policy** · ~6–8 h · [`14-gitops-policy/`](./14-gitops-policy/)  
  **Done when:** CI fails on a deliberate bad manifest; sync flow explained with a short diagram.

---

## Suggested order (detail)

```text
Module 0 (this file + prereqs + glossary)
  → 01 Challenge Gym
  → 02 API → 03 MFA → 04 Admin
  → 05 Worker → 06 Secure Drop
  → 07 CI/AWS → 08 Infra
  → 10 Security notes (can start anytime after 01)
  → Capstone polish (rubric)
  → optional 09; then 11 → 12 → 13 → 14
```

Quizzes ship first under Challenge Gym; later modules should add `quizzes/` the same way — see [`01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md`](./01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md).
