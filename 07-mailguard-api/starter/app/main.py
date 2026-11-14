"""MailGuard API starter — run with uvicorn from the module root.

```bash
cd 07-mailguard-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# From repo module root so `starter.app` imports resolve:
uvicorn starter.app.main:app --reload --port 8000
# Open http://127.0.0.1:8000/docs and http://127.0.0.1:8000/healthz
```
"""

from __future__ import annotations

from fastapi import FastAPI

from starter.app.routers.health import router as health_router
from starter.app.routers.rules import build_rules_router
from starter.app.store import MemoryStore


def create_app(store: MemoryStore | None = None) -> FastAPI:
    memory = store or MemoryStore()
    application = FastAPI(title="MailGuard API", version="0.1.0")
    application.include_router(health_router)
    application.include_router(build_rules_router(memory))
    application.state.store = memory
    return application


app = create_app()
