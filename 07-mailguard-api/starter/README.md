# MailGuard API starter

Minimal FastAPI app with:

- `GET /healthz`
- Rules CRUD (`POST/GET/DELETE /rules`)
- `POST /evaluate` (first-match-wins; bare rules never match)

Persistence is an in-memory store (`starter/app/store.py`). Swap for Postgres in a stretch lab.

## Run locally

```bash
cd 07-mailguard-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn starter.app.main:app --reload --port 8000
```

## Tests

HTTP contract tests live in `../tests/test_api_http.py` (TestClient).
