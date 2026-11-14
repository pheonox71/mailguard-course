"""MailGuard API starter — run with uvicorn from the module root.

```bash
cd 07-mailguard-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# From repo module root so `starter.app` imports resolve:
uvicorn starter.app.main:app --reload --port 8000
# Open http://127.0.0.1:8000/docs and http://127.0.0.1:8000/healthz
```

Clients (store, queue producer, future DB pools) are created in FastAPI
**lifespan** — not as module-level globals that open sockets at import time.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from starter.app.queue_producer import InMemoryQueueProducer
from starter.app.routers.health import router as health_router
from starter.app.routers.rules import build_rules_router
from starter.app.store import MemoryStore


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncIterator[None]:
    """Create request-scoped shared clients on startup; release on shutdown.

    Stretch: open a DB engine / ElasticMQ publisher here and close them in the
    ``finally`` path. Keep imports cheap so pytest can call ``create_app()``
    without side effects at module import.
    """
    store = getattr(application.state, "store", None) or MemoryStore()
    producer = getattr(application.state, "queue_producer", None) or InMemoryQueueProducer()
    application.state.store = store
    application.state.queue_producer = producer
    # Outbox deepen (Module 09): drain unpublished rows → producer.enqueue(...)
    try:
        yield
    finally:
        # In-memory lab clients need no close; real HTTP/DB/SQS clients would.
        application.state.queue_producer = None


def create_app(store: MemoryStore | None = None) -> FastAPI:
    memory = store or MemoryStore()
    application = FastAPI(
        title="MailGuard API",
        version="0.1.0",
        lifespan=lifespan,
    )
    application.state.store = memory
    application.state.queue_producer = InMemoryQueueProducer()
    application.include_router(health_router)
    application.include_router(build_rules_router(memory))
    return application


app = create_app()
