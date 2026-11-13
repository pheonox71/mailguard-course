from __future__ import annotations
from typing import Any

def compose_has_service(doc: dict[str, Any], name: str) -> bool:
    return name in (doc.get("services") or {})
