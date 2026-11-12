# Capstone rubric — portfolio-ready MailGuard

What “end-to-end MailGuard” means for this course: a **coherent public thread** a recruiter or engineer can clone, run, and understand — not a vendor product clone and not inflated tenure claims.

**Authorship:** AI-generated rubric. Evidence is the student’s implementations, demos, and writeups.

Use this after Phase A is largely green; Phase B items raise the ceiling but are not all required for a credible portfolio story.

---

## Pass bar (portfolio-ready)

You meet the capstone when **all Must** rows are honest **yes**, and at least **two** Stretch rows are **yes**.

### Must — story & honesty

| # | Criterion | Evidence |
|---|-----------|----------|
| M1 | **Thread is clear** | Root README states MailGuard as outbound message & file guard; folder table matches shipped modules. |
| M2 | **Authorship is clear** | README states AI-generated course + student-filled worksheets/katas. |
| M3 | **Runnable demo path** | Documented commands bring up enough of API (+ admin or curl) to show hold/allow/reject on a sample message. |
| M4 | **Tests are real** | Core Python (and other shipped code) has automated tests that fail on stubs and pass on your implementations. |
| M5 | **Secrets hygiene** | No live secrets in git; `.env.example` or docs explain required config. |
| M6 | **Trade-offs written** | Each shipped module has ≤1 page “trade-offs / harden next” with at least one production gap. |
| M7 | **No fake seniority** | Copy avoids “senior,” invented years, or “we built enterprise SSO” claims beyond what the repo shows. |

### Must — product shape (MailGuard core)

| # | Criterion | Evidence |
|---|-----------|----------|
| M8 | **Rule engine** | Hold/allow/reject (or equivalent) with tests; first-match or documented evaluation order. |
| M9 | **Identity touch** | MFA/OTP path exists (gym +/or `02`) with enroll/verify literacy in README or notes. |
| M10 | **Operator surface** | Admin UI *or* scripted operator flow to list held items and release/reject. |
| M11 | **Async or transfer path** | Either Go worker applying rules *or* Secure Drop-style expiring link + audit — preferably both over time. |
| M12 | **CI signal** | PR (or push) CI runs tests for at least one core service; badge or documented workflow. |

### Stretch — Horizon B polish

| # | Criterion | Evidence |
|---|-----------|----------|
| S1 | **Infra as code** | Terraform (or equivalent) for at least storage/IAM/queue; `plan` documented. |
| S2 | **Cloud deploy** | One real or carefully faked-local cloud deploy path documented (`12`). |
| S3 | **Local K8s** | Manifests run on kind/minikube with probes/requests (`14`). |
| S4 | **Observability + SRE** | Metrics/logs/traces enough to narrate one failed hold pipeline; SLI/SLO or postmortem worksheet (`15`). |
| S5 | **OIDC lite** | Happy-path federated login on admin or API + revocation notes (`03`). |
| S6 | **GitOps / policy** | CI rejects a bad manifest; sync story diagrammed (`16`). |
| S7 | **Security notes mapped** | Lab notes explicitly tied to mitigations you implemented (`11`). |
| S8 | **Email auth literacy** | SPF/DKIM/DMARC worksheet or `05` kata green; spoofing vs hold-rules gap explained. |
| S9 | **Threat model** | STRIDE-lite table for hold/release (`06`) attached or linked. |
| S10 | **Identity / access depth** | Passkeys *or* SAML/ZTNA worksheet evidence (`02` / `03` / `04`) without inflated claims. |
| S11 | **OSS or security UX** *(optional)* | Upstream issue/PR note or warning-UX redesign (`18`). |

---

## Scoring guide (self-check)

| Level | Meaning |
|-------|---------|
| **Not ready** | Any Must is missing, or demo only works on the author’s machine with undocumented steps. |
| **Portfolio-ready** | All Must yes; two+ Stretch yes; stranger can follow README in one sitting for a happy path. |
| **Strong stretch** | Most Stretch yes; failure story + production-gap notes read as engineering judgment. |

Mark yourself honestly:

- [ ] Not ready  
- [ ] Portfolio-ready  
- [ ] Strong stretch  

---

## Demo script (suggested 5 minutes)

1. **Problem:** “Outbound mail/file mistakes and policy holds.”  
2. **Show rule:** Create/edit a hold rule; send a message that matches; show held state.  
3. **Show identity:** Verify a TOTP (or point at MFA module tests).  
4. **Show operator action:** Release or reject from admin/script.  
5. **Show one ops artifact:** CI badge, Compose, Terraform plan, or a metric/log line.  
6. **Close:** One trade-off you would harden next — and what the rubric still marks as Stretch.

---

## Anti-goals (do not chase for the rubric)

- Cloning a commercial DLP/email product’s UI or branding  
- Certificate walls without linked modules  
- Office-hours / “ask the author” FAQ for other students — this course is self-serve  
- Editing answers into the blank module `worksheets/` / quiz sources instead of saving finished work under `my-work/`

When in doubt, prefer a smaller green demo over a larger unfinished monorepo.
