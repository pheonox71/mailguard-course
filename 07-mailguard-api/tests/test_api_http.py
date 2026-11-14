"""HTTP contract for the FastAPI starter (TestClient)."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient  # noqa: E402

from starter.app.main import create_app  # noqa: E402
from starter.app.store import MemoryStore  # noqa: E402


@pytest.fixture()
def client() -> TestClient:
    return TestClient(create_app(MemoryStore()))


def test_healthz(client: TestClient) -> None:
    res = client.get("/healthz")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_rules_crud_and_evaluate(client: TestClient) -> None:
    created = client.post(
        "/rules",
        json={
            "name": "ext",
            "decision": "hold",
            "recipient_domain": "partner.example",
        },
    )
    assert created.status_code == 201
    rule_id = created.json()["id"]

    listed = client.get("/rules")
    assert listed.status_code == 200
    assert any(r["id"] == rule_id for r in listed.json())

    held = client.post(
        "/evaluate",
        json={
            "sender": "alice@mailguard.example",
            "recipients": ["bob@partner.example"],
            "subject": "Q4",
            "body": "hi",
        },
    )
    assert held.status_code == 200
    assert held.json()["decision"] == "hold"

    allowed = client.post(
        "/evaluate",
        json={
            "sender": "alice@mailguard.example",
            "recipients": ["bob@internal.example"],
            "subject": "Q4",
            "body": "hi",
            "default": "allow",
        },
    )
    assert allowed.status_code == 200
    assert allowed.json()["decision"] == "allow"

    deleted = client.delete(f"/rules/{rule_id}")
    assert deleted.status_code == 204
