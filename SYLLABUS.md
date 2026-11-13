# Module 0 — Syllabus

Orientation for **mailguard-course**: ordered modules, rough hours, progress checkboxes, and **done when** criteria. Work top → bottom through Phase A. Phase B can overlap once the MailGuard API, admin, CI, and infra exist.

**Authorship:** Course structure, readings, stubs, tests, quizzes, and rubrics are AI-generated. Worksheet answers, filled quiz PDFs, and kata implementations are filled in by the student under [`my-work/`](./my-work/) (see root README).

**Related:** [PREREQUISITES.md](./PREREQUISITES.md) · [GLOSSARY.md](./GLOSSARY.md) · [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md)

---

## How to use this syllabus

1. Confirm [prerequisites](./PREREQUISITES.md), skim the [glossary](./GLOSSARY.md).
2. Start with Module **00** (setup). For each later module: open its README → on-site reading → worksheet → implement → tests / demo → **required quiz** (questions PDF) → separate answer key.
3. Tick the checkbox when that module’s **Done when** is met from *your* work (not by copying `solutions/`).
4. Capstone readiness is judged by [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md), not by finishing every stretch folder.

Hours are **solo student estimates** (CS background, Python-strong). They include reading + worksheets + implementation + a short writeup — not calendar deadlines.

---

## Progress overview

| Phase | Modules | Est. hours (sum) |
|-------|---------|------------------|
| **A — Core path** | `00`–`13` | est. 8-10h each |
| **B — Stretch** | `14`–`16`, optional `17`–`18` | est. 8-10h each |
| **Capstone polish** | Cross-cutting demo + rubric | ~8–12 h |

---

## Module checklist

### Foundations

- [ ] **00 — Setup / getting ready** · est. 8-10h · [`00-setup/`](./00-setup/)  
  **Done when:** Core tools install and version-check; worksheet checklist + required quiz completed under `my-work/`.

- [ ] **01 — Challenge Gym** · est. 8-10h · [`01-challenge-gym/`](./01-challenge-gym/)  
  **Done when:** All Challenge Gym tests green from *your* `katas/` (incl. crypto hygiene); ≤1 page trade-offs; required quizzes completed after each reading (answer keys checked afterward).

### Identity & access

- [ ] **02 — MailGuard MFA** · est. 8-10h · [`02-mailguard-mfa/`](./02-mailguard-mfa/)  
  **Done when:** Enroll/verify TOTP; one-time recovery codes; no secrets in git; passkeys / WebAuthn worksheet + quiz done.

- [ ] **03 — OIDC / access policy** · est. 8-10h · [`03-oidc-access/`](./03-oidc-access/)  
  **Done when:** Happy-path OIDC login + protected route/API; SAML vs OIDC, device-cert concepts, and password-manager-for-non-SSO worksheet done; logout/revocation notes; no inflated SSO claims.

- [ ] **04 — ZTNA lite** · est. 8-10h · [`04-ztna-lite/`](./04-ztna-lite/)  
  **Done when:** VPN vs ZTNA diagram + compare table; can explain identity-bound app access without claiming a commercial mesh deploy.

### Email & DLP literacy

- [ ] **05 — Email authentication** · est. 8-10h · [`05-email-auth/`](./05-email-auth/)  
  **Done when:** SPF/DKIM/DMARC + SMTP/TLS literacy worksheet done; `dmarc_policy` kata tests green; can explain `p=none→reject` and aggregate reports.

- [ ] **06 — Threat model / secure SDLC** · est. 8-10h · [`06-threat-model/`](./06-threat-model/)  
  **Done when:** STRIDE-lite table for hold/release (≥6 rows); SAMM self-check paragraph; privacy note on held content.

### Product build (MailGuard)

- [ ] **07 — MailGuard API** · est. 8-10h · [`07-mailguard-api/`](./07-mailguard-api/)  
  **Done when:** CRUD + hold/release; rules unit-tested; architecture notes in the module README.

- [ ] **08 — MailGuard Admin** · est. 8-10h · [`08-mailguard-admin/`](./08-mailguard-admin/)  
  **Done when:** Rules + hold queue usable end-to-end against the API; TypeScript strict; a few component/e2e tests.

- [ ] **09 — MailGuard Worker** · est. 8-10h · [`09-mailguard-worker/`](./09-mailguard-worker/)  
  **Done when:** Local queue demo behind an interface; short Python-vs-Go contract note.

- [ ] **10 — Secure Drop** · est. 8-10h · [`10-secure-drop/`](./10-secure-drop/)  
  **Done when:** Upload → object storage → time-limited link + audit log demo; cloud-share DLP worksheet done (visibility / revoke / audit).

- [ ] **11 — Security notes** · est. 8-10h · [`11-security-notes/`](./11-security-notes/)  
  **Done when:** ≥5 lab notes mapped to MailGuard mitigations; no attacks on real systems.

### Cloud & platform

- [ ] **12 — CI + AWS** · est. 8-10h · [`12-ci-aws/`](./12-ci-aws/)  
  **Done when:** PR CI green (lint/test/image as applicable); one documented cloud deploy; no secrets in git.

- [ ] **13 — Infra** · est. 8-10h · [`13-infra/`](./13-infra/)  
  **Done when:** `compose up` demos the MailGuard story; Terraform `plan` documented; IAM / misconfig checklist completed for *your* resources.

### Phase B (stretch)

- [ ] **14 — K8s local** · est. 8-10h · [`14-k8s-local/`](./14-k8s-local/)  
  **Done when:** App healthy on kind/minikube; probes + resource requests; README names managed K8s / GitOps as next steps.

- [ ] **15 — Observability** · est. 8-10h · [`15-observability/`](./15-observability/)  
  **Done when:** Local stack shows golden signals; SLI/SLO/error budget worksheet + one blameless postmortem from telemetry; alert *idea* documented.

- [ ] **16 — GitOps + policy** · est. 8-10h · [`16-gitops-policy/`](./16-gitops-policy/)  
  **Done when:** CI fails on a deliberate bad manifest; sync flow explained with a short diagram.

- [ ] **17 — Phish Lite** *(optional)* · est. 8-10h · [`17-phish-lite/`](./17-phish-lite/)  
  **Done when:** Quiz → results chart; README states learning-purpose honesty.

- [ ] **18 — OSS + security UX** *(optional)* · est. 8-10h · [`18-oss-ux-stretch/`](./18-oss-ux-stretch/)  
  **Done when:** Either an upstream issue/PR note **or** a security-warning UX redesign + reflection.

---

## Suggested order

```text
Module 0 (this file + prereqs + glossary)
  → 01 Challenge Gym
  → 02 MFA (+ passkeys) → 03 OIDC / identity depth → 04 ZTNA lite
  → 05 Email auth → 06 Threat model
  → 07 API → 08 Admin → 09 Worker → 10 Secure Drop → 11 Security notes
  → 12 CI/AWS → 13 Infra
  → Capstone polish (rubric)
  → 14 K8s → 15 Observability → 16 GitOps
  → optional 17 Phish Lite; optional 18 OSS / security UX
```

Quizzes follow the Challenge Gym pattern — see [`01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md`](./01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md).
