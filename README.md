# MailGuard Course

**Live site:** [MailGuard Course on GitHub Pages](https://pheonox71.github.io/mailguard-course/)

> **AI assistance notice:** This course's content was researched and compiled with AI assistance. It has been reviewed for accuracy, but verify anything important against the linked primary sources (RFCs, official docs).

Student-facing course for cloud-security skills: setup → identity / MFA → email authentication → DLP-minded product work → cloud / platform practice. Readings render in the browser; assignments, tests, and **required** quizzes download for offline work.

Assignment answers, filled quiz PDFs, and kata implementations are filled in by the student.

**Student work folder:** Completed personal assignments and filled quiz PDFs live under [`my-work/`](./my-work/) (`my-work/assignments/`, `my-work/quizzes/`) in this repository. They are **not** accessible from the course website — the site never links to or serves those files.

---

## Who it’s for

Students with CS fundamentals and comfort in Python who want a survey path across backend, frontend, and platform/infra — without employer branding in public materials.

---

## Course flow

1. **Module 00 — Setup** — install and version-check tools (Windows / macOS / Linux).
2. **Language / tool primers** (read-only, Module 00 style) appear immediately **before** the first module that uses that stack (Bash, Python, HTTP, SQL, TypeScript/Vue, Go, Docker, GitHub Actions, Terraform, Kubernetes YAML, Svelte). No assignments, quizzes, or downloads — progress checkbox only.
3. **Modules 01–22** (plus primers and capstone **19**) — each build topic: **read on-site** → **assignment** → **tests** (when present) → **required quiz PDF** → separate **quiz answer key**. Primers stay read-only (mark complete only).
4. Mark topics/modules complete in the browser (progress stored locally; resume CTA in the nav).
5. Save finished assignments and filled quizzes under `my-work/` in the repo (not on the site).

Every module (including primers) is listed as **est. 8-10h**.

---

## Site features

- **Live site:** [MailGuard Course on GitHub Pages](https://pheonox71.github.io/mailguard-course/)
- Home / syllabus in learning order (Module 00 → capstone) with progress checkmarks
- On-site rendered readings (including captioned diagrams where present)
- Learning objectives at the top of each module page
- Download buttons for assignments, tests, quiz PDFs (questions only), and separate answer keys
- Next / previous module navigation; resume CTA + reset progress (localStorage)
- Glossary page with terms linked from readings; client-side search
- Light/dark theme toggle (persisted) and print-friendly reading styles
- Language / tooling chip per module (stack languages only)
- `my-work/` is never linked or served by the site

---

## Run the site locally

```bash
cd site
npm start
```

Open **http://127.0.0.1:5173/**

`npm start` runs `prepare-readings` then a static server. To rebuild assignment/test/quiz packs (including fillable quiz PDFs):

```bash
cd site
pip3 install -r scripts/requirements.txt   # once
npm run prepare-downloads
npm start
```

The static server is rooted at `site/` only — parent folders such as `my-work/` are never served.

---

## Repo layout

| Path | Role |
|------|------|
| [`00-setup/`](./00-setup/) … [`22-collab-review/`](./22-collab-review/) | Modules in learning order (includes `*a`/`*b`/`*c` language/tool primers; capstone is `19`) |
| [`site/`](./site/) | Student website (readings UI + downloads) |
| [`my-work/`](./my-work/) | Student’s completed assignments & quiz PDFs (not on the site) |
| [`SYLLABUS.md`](./SYLLABUS.md) · [`PREREQUISITES.md`](./PREREQUISITES.md) · [`GLOSSARY.md`](./GLOSSARY.md) · [`CAPSTONE-RUBRIC.md`](./CAPSTONE-RUBRIC.md) | Module 0 orientation |

---

## Secrets hygiene

- Do not commit live credentials. Copy [`.env.example`](./.env.example) to `.env` for local config (gitignored).
- Optional local hook: `pip install pre-commit && pre-commit install` — runs **gitleaks** before each commit (see [CONTRIBUTING.md](./CONTRIBUTING.md)).
- CI runs gitleaks on every push. Known lesson **test fixtures** (TOTP demo key, local compose password) are allowlisted in [`.gitleaks.toml`](./.gitleaks.toml) and marked in-code as non-secrets.

## GitHub Pages

The course site is published from `site/` on pushes to `main` (GitHub Actions):

[MailGuard Course on GitHub Pages](https://pheonox71.github.io/mailguard-course/)

Only `site/` is published. The workflow never links to or serves `my-work/`.
