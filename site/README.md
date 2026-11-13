# MailGuard Course — student website

Student-facing site for **MailGuard Course** (cloud-security learning). Browse the syllabus, **read module readings in the browser**, then download worksheets, tests, and fillable quiz PDFs to complete offline.

Finished student work is **not** stored or served by this site. Save completed worksheets and filled quiz PDFs under the course-repo path `my-work/` (the static site never links to or serves that folder).

## Run locally (fast preview)

```bash
cd site
npm run prepare-readings   # copies readings + images into content/ (no PDF build)
python3 -m http.server 5173 --bind 127.0.0.1
```

Or in one step:

```bash
cd site
npm start
```

Open **http://127.0.0.1:5173/** then **Module 01**: http://127.0.0.1:5173/module.html?id=01-challenge-gym

No Node package install is required for the site itself (markdown is rendered in the browser via a CDN import).

## Full download packs (worksheets / tests / quiz PDFs)

```bash
cd site
pip3 install -r scripts/requirements.txt   # once (reportlab for fillable PDFs)
npm run prepare-downloads                  # slower — also refreshes readings
```

| Asset | Behavior |
|-------|----------|
| Readings | Rendered on each module page from `content/<module>/readings/` |
| Worksheets | Single `.md` download, or `worksheets.zip` when a module has several |
| Tests | `tests.zip` of `test_*.py` (plus `__init__.py` when present); Module 01 also offers per-topic test files |
| Quiz PDFs | Fillable AcroForm PDFs (questions only) — answer keys are stripped / never included |

Modules without worksheet/test/quiz assets still appear in the syllabus; topic pages still show readings when present.

## Layout

```text
site/
  index.html                 # brand hero + syllabus
  module.html                # readings + downloads per module
  assets/styles.css
  js/
  content/                   # generated readings (fast path)
  data/catalog.json          # generated
  downloads/                 # generated worksheets/tests/quizzes
  scripts/course-meta.mjs
  scripts/prepare-readings.mjs
  scripts/prepare-downloads.mjs
  scripts/quiz_md_to_pdf.py
```
