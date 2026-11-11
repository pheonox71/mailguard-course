# MailGuard Course — student website

Student-facing site for **MailGuard Course** (cloud-security learning). Browse the syllabus in order and download worksheets and tests for each module that has them.

## Run locally

```bash
cd site
npm run prepare-downloads   # copies worksheets/tests from the parent course tree
python3 -m http.server 5173 --bind 127.0.0.1
```

Or in one step:

```bash
cd site
npm start
```

Open **http://127.0.0.1:5173/**

No Node package install is required — `prepare-downloads` uses only the Node standard library plus system `zip`.

## What downloads

| Asset | Behavior |
|-------|----------|
| Worksheets | Single `.md` download, or `worksheets.zip` when a module has several |
| Tests | `tests.zip` of `test_*.py` (plus `__init__.py` when present); Module 01 also offers per-topic test files |
| Quizzes | Questions only — answer-key sections are stripped before publishing under `downloads/` |

Modules without worksheet/test assets still appear in the syllabus; the module page notes when downloads are not available yet.

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
```
