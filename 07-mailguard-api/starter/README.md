# MailGuard API starter

Minimal FastAPI app with:

- `GET /healthz`
- Rules CRUD (`POST/GET/DELETE /rules`)
- `POST /evaluate` (first-match-wins; bare rules never match)

Persistence is an in-memory store (`starter/app/store.py`). Swap for Postgres in a stretch lab.

The store imports the rules engine from `katas/` by default. Set
`MAILGUARD_USE_SOLUTIONS=1` only when you intentionally want the reference
implementation (and optional `NotImplementedError` fallback). The module
`Dockerfile` is multi-stage: default target has no `solutions/`; use
`docker build --target with-solutions` when you intentionally want the
reference engine in the image (avoids `COPY`+`rm` layer leakage).

## Run locally

```bash
cd 07-mailguard-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn starter.app.main:app --reload --port 8000
```

## Queue producer (module 09 contract)

`app/queue_producer.py` enqueues JSON messages shaped like the Go worker contract
`{id, subject, body, attempt}`. Default backend is in-memory (optional file spill).
For a local SQS-compatible broker, start
`09-mailguard-worker/starter/docker-compose.queue.yml` and follow the boto3
comments in `queue_producer.py`.

## Tests

HTTP contract tests live in `../tests/test_api_http.py` (TestClient).
