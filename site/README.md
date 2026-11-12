# MailGuard Course — student website

Student-facing site for **MailGuard Course** (cloud-security learning). Browse the syllabus in order and download worksheets, tests, and fillable quiz PDFs for each module that has them.

Finished student work is **not** stored in this site. Save completed worksheets and filled quiz PDFs under [`../my-work/`](../my-work/) in the course repo.

## Run locally

```bash
cd site
npm run prepare-downloads   # copies worksheets/tests and builds quiz PDFs
python3 -m http.server 5173 --bind 127.0.0.1
```

Or in one step:

```bash
cd site
npm start
```

Open **http://127.0.0.1:5173/**

No Node package install is required — `prepare-downloads` uses the Node standard library, system `zip`, and Python **reportlab** for fillable quiz PDFs:

```bash
pip3 install -r scripts/requirements.txt
```

## What downloads

| Asset | Behavior |
|-------|----------|
| Worksheets | Single `.md` download, or `worksheets.zip` when a module has several |
| Tests | `tests.zip` of `test_*.py` (plus `__init__.py` when present); Module 01 also offers per-topic test files |
| Quiz PDFs | Fillable AcroForm PDFs (questions only) — answer keys are stripped / never included |
| Quiz markdown | Questions-only `.md` copies remain under `downloads/` for reference |

Modules without worksheet/test/quiz assets still appear in the syllabus; the module page notes when downloads are not available yet.

## Regenerate downloads

```bash
cd site
pip3 install -r scripts/requirements.txt   # once
npm run prepare-downloads
```

This rebuilds `downloads/` and `data/catalog.json` from the parent course modules (including quiz PDFs via `scripts/quiz_md_to_pdf.py`).

## Layout

```text
site/
  index.html                 # brand hero + syllabus
  module.html                # per-module downloads
  assets/styles.css
  js/
  data/catalog.json          # generated
  downloads/                 # generated from course modules
  scripts/prepare-downloads.mjs
  scripts/quiz_md_to_pdf.py
  scripts/requirements.txt
```
