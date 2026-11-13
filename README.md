# MailGuard Course

**Live site:** [https://pheonox71.github.io/mailguard-course/](https://pheonox71.github.io/mailguard-course/)

Student-facing course for cloud-security skills: setup → identity / MFA → email authentication → DLP-minded product work → cloud / platform practice. Readings render in the browser; worksheets, tests, and **required** quizzes download for offline work.

**Authorship:** Course structure, readings, stubs, tests, quizzes, and rubrics are AI-generated. Worksheet answers, filled quiz PDFs, and kata implementations are filled in by the student.

**Student work folder:** Completed personal worksheets and filled quiz PDFs live under [`my-work/`](./my-work/) (`my-work/worksheets/`, `my-work/quizzes/`) in this repository. They are **not** accessible from the course website — the site never links to or serves those files.

---

## Who it’s for

Students with CS fundamentals and comfort in Python who want a survey path across backend, frontend, and platform/infra — without employer branding in public materials.

---

## Course flow

1. **Module 00 — Setup** — install and version-check tools (Windows / macOS / Linux).
2. **Modules 01–18** — each topic: **read on-site** → **worksheet** → **tests** (when present) → **required quiz PDF** → separate **quiz answer key**.
3. Mark topics/modules complete in the browser (progress stored locally; resume CTA in the nav).
4. Save finished worksheets and filled quizzes under `my-work/` in the repo (not on the site).

Every module is listed as **est. 8-10h**.

---

## Site features

- **Live site:** [https://pheonox71.github.io/mailguard-course/](https://pheonox71.github.io/mailguard-course/)
- Home / syllabus in learning order (Module 00 → capstone) with progress checkmarks
- On-site rendered readings (including captioned diagrams where present)
- Learning objectives at the top of each module page
- Download buttons for worksheets, tests, quiz PDFs (questions only), and separate answer keys
- Next / previous module navigation; resume CTA + reset progress (localStorage)
- Glossary page with terms linked from readings; client-side search
- Completion certificate when all quiz topics are marked complete (name stored locally)
- Light/dark theme toggle (persisted) and print-friendly reading / certificate styles
- Language / tooling chip per module (stack languages only)
- `my-work/` is never linked or served by the site

---

## Run the site locally

```bash
cd site
npm start
```

Open **http://127.0.0.1:5173/**

`npm start` runs `prepare-readings` then a static server. To rebuild worksheet/test/quiz packs (including fillable quiz PDFs):

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
| [`00-setup/`](./00-setup/) … [`18-oss-ux-stretch/`](./18-oss-ux-stretch/) | Modules in learning order |
| [`site/`](./site/) | Student website (readings UI + downloads) |
| [`my-work/`](./my-work/) | Student’s completed worksheets & quiz PDFs (not on the site) |
| [`SYLLABUS.md`](./SYLLABUS.md) · [`PREREQUISITES.md`](./PREREQUISITES.md) · [`GLOSSARY.md`](./GLOSSARY.md) · [`CAPSTONE-RUBRIC.md`](./CAPSTONE-RUBRIC.md) | Module 0 orientation |

---

## GitHub Pages

Published from `site/` on pushes to `main` (GitHub Actions). Project URL:

**https://pheonox71.github.io/mailguard-course/**

If the site 404s after the first workflow run, enable Pages in the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
