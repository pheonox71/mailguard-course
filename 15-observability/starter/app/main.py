"""Tiny instrumented demo app — Prometheus /metrics for Module 15.

```bash
cd 15-observability/starter/app
pip install fastapi uvicorn prometheus-client
uvicorn main:app --port 8000
# GET http://127.0.0.1:8000/healthz
# GET http://127.0.0.1:8000/metrics
```
"""

from __future__ import annotations

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

app = FastAPI(title="MailGuard observability demo")
REQUESTS = Counter("mailguard_demo_requests_total", "Demo requests", ["path"])


@app.get("/healthz")
def healthz() -> dict[str, str]:
    REQUESTS.labels(path="/healthz").inc()
    return {"status": "ok"}


@app.get("/metrics")
def metrics() -> Response:
    REQUESTS.labels(path="/metrics").inc()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
