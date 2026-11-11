# Module 0 — Syllabus

Orientation for **mailguard-course**: ordered modules, rough hours, progress checkboxes, and **done when** criteria.

**Numbering rule:** Folders `01`–`14` stay stable. New high-priority literacy modules use `15`+ so existing links and progress checkboxes do not break. Some topics **extend** an existing folder (readings/worksheets inside `01`, `03`, `06`, `08`, `12`, `13`) instead of inventing a parallel number.

**Phases**

| Phase | Modules | Est. hours (sum) |
|-------|---------|------------------|
| **A — Survey** | `01`–`08`, `10`, `15`, `16` | ~95–120 h |
| **B — Stretch** | `09` (opt.), `11`–`14`, `17`, `18` (opt.) | ~50–65 h |
| **Capstone polish** | Cross-cutting demo + rubric | ~8–12 h |

Work top → bottom for Phase A. Phase B can overlap once MailGuard core API, admin, CI, and infra exist. Modules `15`–`16` are Phase A foundations (email auth + threat model) that pair with `09`/`10`. Module `17` follows identity work in `13`. Module `18` is optional portfolio polish.

**Authorship:** Course structure, readings, stubs, tests, quizzes, and rubrics are AI-generated. Worksheet answers and kata implementations are filled in by the student (on the `work` branch — see root README).

**Related:** [PREREQUISITES.md](./PREREQUISITES.md) · [GLOSSARY.md](./GLOSSARY.md) · [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md)

---

## How to use this syllabus

1. Confirm [prerequisites](./PREREQUISITES.md), skim the [glossary](./GLOSSARY.md).
2. For each module: open its README → readings → worksheet → implement → tests / demo → self-check quiz (when present).
3. Tick the checkbox when that module’s **Done when** is met from *your* work (not by copying `solutions/`).
4. Capstone readiness is judged by [CAPSTONE-RUBRIC.md](./CAPSTONE-RUBRIC.md), not by finishing every stretch folder.

Hours are **solo student estimates** (CS background, Python-strong). They include reading + worksheets + implementation + a short writeup — not calendar deadlines.

---

## Module checklist

### Phase A

- [ ] **01 — Challenge Gym** · ~8–10 h · [`01-challenge-gym/`](./01-challenge-gym/)  
  **Done when:** All Challenge Gym tests green from *your* `katas/` (incl. **crypto_hygiene**); ≤1 page trade-offs; self-check quizzes attempted after each reading.

- [ ] **02 — MailGuard API** · ~12–16 h · [`02-mailguard-api/`](./02-mailguard-api/)  
  **Done when:** CRUD + hold/release; rules unit-tested; architecture notes in the module README.

- [ ] **03 — MailGuard MFA (+ passkeys)** · ~10–12 h · [`03-mailguard-mfa/`](./03-mailguard-mfa/)  
  **Done when:** Enroll/verify TOTP; one-time recovery codes; no secrets in git; **passkeys / WebAuthn** worksheet + quiz done.

- [ ] **04 — MailGuard Admin** · ~12–16 h · [`04-mailguard-admin/`](./04-mailguard-admin/)  
  **Done when:** Rules + hold queue usable end-to-end against the API; TypeScript strict; a few component/e2e tests.

- [ ] **05 — MailGuard Worker** · ~10–12 h · [`05-mailguard-worker/`](./05-mailguard-worker/)  
  **Done when:** Local queue demo behind an interface; short Python-vs-Go contract note.

- [ ] **06 — Secure Drop (+ cloud-share DLP)** · ~10–12 h · [`06-secure-drop/`](./06-secure-drop/)  
  **Done when:** Upload → object storage → time-limited link + audit log demo; **cloud-share DLP** worksheet done (visibility / revoke / audit).

- [ ] **07 — CI + AWS** · ~8–10 h · [`07-ci-aws/`](./07-ci-aws/)  
  **Done when:** PR CI green (lint/test/image as applicable); one documented cloud deploy; no secrets in git.

- [ ] **08 — Infra (+ IAM posture)** · ~12–14 h · [`08-infra/`](./08-infra/)  
  **Done when:** `compose up` demos the MailGuard story; Terraform `plan` documented; **IAM / misconfig** checklist completed for *your* resources.

- [ ] **10 — Security notes** · ~6–8 h · [`10-security-notes/`](./10-security-notes/)  
  **Done when:** ≥5 lab notes mapped to MailGuard mitigations; no attacks on real systems.

- [ ] **15 — Email authentication** · ~6–8 h · [`15-email-auth/`](./15-email-auth/)  
  **Done when:** SPF/DKIM/DMARC + SMTP/TLS literacy worksheet done; `dmarc_policy` kata tests green; can explain `p=none→reject` and aggregate reports.

- [ ] **16 — Threat model / secure SDLC** · ~5–7 h · [`16-threat-model/`](./16-threat-model/)  
  **Done when:** STRIDE-lite table for hold/release (≥6 rows); SAMM self-check paragraph; privacy note on held content.

### Phase B (stretch)

- [ ] **09 — Phish Lite** *(optional)* · ~6–8 h · [`09-phish-lite/`](./09-phish-lite/)  
  **Done when:** Quiz → results chart; README states learning-purpose honesty.

- [ ] **11 — K8s local** · ~10–12 h · [`11-k8s-local/`](./11-k8s-local/)  
  **Done when:** App healthy on kind/minikube; probes + resource requests; README names managed K8s / GitOps as next steps.

- [ ] **12 — Observability (+ SRE)** · ~10–12 h · [`12-observability/`](./12-observability/)  
  **Done when:** Local stack shows golden signals; **SLI/SLO/error budget** worksheet + one blameless postmortem from telemetry; alert *idea* documented.

- [ ] **13 — OIDC / access (+ identity depth)** · ~10–12 h · [`13-oidc-access/`](./13-oidc-access/)  
  **Done when:** Happy-path OIDC login + protected route/API; **SAML vs OIDC**, device-cert concepts, and password-manager-for-non-SSO worksheet done; logout/revocation notes; no inflated SSO claims.

- [ ] **17 — ZTNA lite** · ~3–5 h · [`17-ztna-lite/`](./17-ztna-lite/)  
  **Done when:** VPN vs ZTNA diagram + compare table; can explain identity-bound app access without claiming a commercial mesh deploy.

- [ ] **14 — GitOps + policy** · ~6–8 h · [`14-gitops-policy/`](./14-gitops-policy/)  
  **Done when:** CI fails on a deliberate bad manifest; sync flow explained with a short diagram.

- [ ] **18 — OSS + security UX** *(optional)* · ~3–6 h · [`18-oss-ux-stretch/`](./18-oss-ux-stretch/)  
  **Done when:** Either an upstream issue/PR note **or** a security-warning UX redesign + reflection.

---

## Suggested order (detail)

```text
Module 0 (this file + prereqs + glossary)
  → 01 Challenge Gym (incl. crypto_hygiene after the three preview katas)
  → 02 API → 03 MFA (+ passkeys reading) → 04 Admin
  → 05 Worker → 06 Secure Drop (+ cloud-share DLP)
  → 07 CI/AWS → 08 Infra (+ IAM posture)
  → 10 Security notes (can start anytime after 01)
  → 15 Email auth (SPF/DKIM/DMARC) → 16 Threat model / SSDLC
  → Capstone polish (rubric)
  → optional 09
  → 11 → 12 (+ SRE) → 13 (+ identity depth) → 17 ZTNA → 14
  → optional 18 OSS / security UX
```

**Why `15`/`16` after `10`:** email-domain authentication and formal threat modeling deepen the security-notes story without renumbering `11`–`14`. **Why `17` after `13`:** ZTNA builds on identity literacy (OIDC/SAML) rather than replacing it.

Quizzes ship under Challenge Gym and each extended/new module the same way — see [`01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md`](./01-challenge-gym/quizzes/README-01-challenge-gym-quizzes.md).
