# Module 0 — Syllabus

Orientation for **mailguard-course**: ordered modules, rough hours, progress checkboxes, and **done when** criteria. Work top → bottom through Phase A. Phase B can overlap once the MailGuard API, admin, CI, and infra exist.

Worksheet answers, filled quiz PDFs, and kata implementations are filled in by the student under [`my-work/`](./my-work/) (see root README). Course content uses AI assistance — see the notice on the site and README.

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
  **Done when:** Core tools install and version-check; Module 00 marked complete on the site (no worksheet or quiz for this module).

- [ ] **01 — Challenge Gym** · est. 8-10h · [`01-challenge-gym/`](./01-challenge-gym/)  
  **Done when:** All Challenge Gym tests green from *your* `katas/` (incl. crypto hygiene); ≤1 page trade-offs; required quizzes completed after each reading (answer keys checked afterward).

### Identity & access

- [ ] **02 — MailGuard MFA** · est. 8-10h · [`02-mailguard-mfa/`](./02-mailguard-mfa/)  
  **Done when:** Enroll/verify TOTP; one-time recovery codes; no secrets in git; passkeys / WebAuthn worksheet + quiz done.

- [ ] **03 — OIDC / access policy** · est. 8-10h · [`03-oidc-access/`](./03-oidc-access/)  
  **Done when:** OIDC + PKCE helpers green; SAML assertion-check kata green; Keycloak lab notes; SAML vs OIDC worksheet; logout/revocation notes; no inflated SSO claims.

- [ ] **04 — ZTNA lite** · est. 8-10h · [`04-ztna-lite/`](./04-ztna-lite/)  
  **Done when:** VPN vs ZTNA diagram + compare table; mTLS checks kata green; NIST SP 1800-35 reading noted; no commercial mesh required.

### Email & DLP literacy

- [ ] **05 — Email authentication** · est. 8-10h · [`05-email-auth/`](./05-email-auth/)  
  **Done when:** SPF/DKIM/DMARC literacy done; `dmarc_policy` + `dmarc_aggregate` + `mail_flow` katas green; ARC/gateway placement explained.

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
  **Done when:** Upload → expiring link + recipient OTP + revoke-after-missend; PPAP-as-global-anti-pattern worksheet done.

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

- [ ] **20 — SCIM / JIT provisioning** · est. 8-10h · [`20-scim-provisioning/`](./20-scim-provisioning/)  
  **Done when:** SCIM filter + joiner-mover-leaver katas green; deprovisioning worksheet + quiz done.

- [ ] **21 — Global collaboration & privacy** · est. 8-10h · [`21-global-privacy-collab/`](./21-global-privacy-collab/)  
  **Done when:** Timezone/collaboration + privacy-regime worksheets done; `privacy_tags` green; quiz done. English only — no language-learning track.

- [ ] **22 — Git & code review** · est. 8-10h · [`22-collab-review/`](./22-collab-review/)  
  **Done when:** `pr_hygiene` green; security review checklist worksheet + quiz done (practice repo optional).



## Suggested order

Capstone polish sits **after Phase A (00–13)** and **before Phase B stretch (14–18)**. Module folder `19-capstone/` keeps that number so Phase B folders stay stable — treat 19 as “after 13 in the learning path,” not “after 18.”

```text
Module 0 (this file + prereqs + glossary)
  → 01 Challenge Gym
  → 02 MFA (+ passkeys) → 03 OIDC / identity depth → 04 ZTNA lite
  → 05 Email auth → 06 Threat model
  → 07 API → 08 Admin → 09 Worker → 10 Secure Drop → 11 Security notes
  → 12 CI/AWS → 13 Infra
  → Capstone polish (19 — rubric / mail filter)
  → Phase B stretch: 14 K8s → 15 Observability → 16 GitOps
  → optional 17 Phish Lite; optional 18 OSS / security UX
  → 20 SCIM → 21 Global privacy/collab → 22 Git/code review
```

Quizzes follow the Challenge Gym pattern — see [`01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md`](./01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md).

### Capstone

- [ ] **19 — Capstone: mail filter** · est. 8-10h · [`19-capstone/`](./19-capstone/)  
  **Done when:** Runnable mail-filter demo with tests; self-grade worksheet completed; required quiz done.
