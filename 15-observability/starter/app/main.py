"""Instrumented MailGuard-shaped demo — Prometheus metrics for Module 15.

```bash
cd 15-observability/starter
docker compose -f otel-compose.yml up --build
# Or locally:
#   pip install -r app/requirements.txt
#   uvicorn main:app --app-dir app --port 8000
```

Endpoints:
- `POST /evaluate` — increments hold/allow counters and observes latency
- `GET /metrics` — Prometheus text exposition
- `GET /healthz` — liveness/readiness
"""

from __future__ import annotations

import time
from typing import Any

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from pydantic import BaseModel, Field

app = FastAPI(title="MailGuard observability demo")

# Why only "decision": never put PII, subjects, emails, or tokens in metric labels.
HOLDS = Counter(
    "mailguard_holds_total",
    "Evaluate decisions (hold vs allow)",
    ["decision"],
)
ERRORS = Counter(
    "mailguard_evaluate_errors_total",
    "Evaluate path errors",
)
LATENCY = Histogram(
    "mailguard_evaluate_seconds",
    "Evaluate path latency in seconds",
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5),
)


class EvaluateRequest(BaseModel):
    subject: str = Field(default="", description="Message subject for toy hold heuristics")
    body: str = Field(default="", description="Optional body text")


class EvaluateResponse(BaseModel):
    decision: str
    reason: str


def _decide(subject: str, body: str) -> tuple[str, str]:
    text = f"{subject} {body}".lower()
    # Toy heuristic: wire/transfer language → hold (traffic signal for the lab).
    if any(token in text for token in ("wire", "transfer", "urgent payment", "invoice overdue")):
        return "hold", "subject/body matched hold heuristic"
    return "allow", "no hold heuristic matched"


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/evaluate", response_model=EvaluateResponse)
def evaluate(payload: EvaluateRequest) -> Any:
    started = time.perf_counter()
    try:
        decision, reason = _decide(payload.subject, payload.body)
        HOLDS.labels(decision=decision).inc()
        return EvaluateResponse(decision=decision, reason=reason)
    except Exception:
        ERRORS.inc()
        raise
    finally:
        LATENCY.observe(time.perf_counter() - started)


@app.get("/metrics")
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
