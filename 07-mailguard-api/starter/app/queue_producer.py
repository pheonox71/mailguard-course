"""Enqueue hold-work messages for the MailGuard worker (module 09).

JSON contract (must match Go ``worker.QueueMessage``):

    {"id": "...", "subject": "...", "body": "...", "attempt": 0}

``attempt`` models SQS ApproximateReceiveCount when a real broker is wired.

Default backend is an in-memory / file queue so the API starter runs without
Docker. In production, prefer a **transactional outbox**: write the hold and an
outbox row in one DB transaction, then let a publisher call ``enqueue`` /
SQS send (see Module 07 reading). Do not treat "HTTP 200 then best-effort
send" as durable.

Comments below show the ElasticMQ (SQS-compatible) shape when you point boto3
at ``http://127.0.0.1:9324`` (course default — see
``09-mailguard-worker/starter/docker-compose.queue.yml``). Keep payloads under
SQS **1 MiB**. Create the boto3 client in FastAPI lifespan, not at import time.
"""

from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class QueueMessage:
    id: str
    subject: str
    body: str
    attempt: int = 0

    def to_json(self) -> str:
        return json.dumps(asdict(self), separators=(",", ":"))


class InMemoryQueueProducer:
    """Lab producer — append messages to an in-process list (and optional file)."""

    def __init__(self, *, spill_path: Path | None = None) -> None:
        self._messages: list[QueueMessage] = []
        self._spill_path = spill_path

    def enqueue(
        self,
        *,
        subject: str,
        body: str,
        message_id: str | None = None,
        attempt: int = 0,
    ) -> QueueMessage:
        if not subject:
            raise ValueError("subject is required")
        msg = QueueMessage(
            id=message_id or str(uuid.uuid4()),
            subject=subject,
            body=body,
            attempt=attempt,
        )
        self._messages.append(msg)
        if self._spill_path is not None:
            self._spill_path.parent.mkdir(parents=True, exist_ok=True)
            with self._spill_path.open("a", encoding="utf-8") as fh:
                fh.write(msg.to_json() + "\n")
        return msg

    @property
    def messages(self) -> list[QueueMessage]:
        return list(self._messages)


def enqueue_hold_message(
    subject: str,
    body: str,
    *,
    producer: InMemoryQueueProducer | None = None,
    message_id: str | None = None,
) -> dict[str, Any]:
    """Convenience helper used by routes/labs — returns the JSON object enqueued."""
    prod = producer or InMemoryQueueProducer()
    msg = prod.enqueue(subject=subject, body=body, message_id=message_id, attempt=0)
    return asdict(msg)


# ---------------------------------------------------------------------------
# Optional: SQS-compatible producer (ElasticMQ default) — sketch only.
# Construct ``client`` in FastAPI lifespan (Module 07 main.py), not here at
# import time. Uncomment and adapt when docker-compose.queue.yml is running.
# Do not put real AWS keys in source control; ElasticMQ ignores auth but the
# SDK still wants local-only placeholders from env.
#
# import boto3
#
# def sqs_enqueue(subject: str, body: str, *, client, queue_url: str) -> dict[str, Any]:
#     payload = QueueMessage(
#         id=str(uuid.uuid4()), subject=subject, body=body, attempt=0
#     )
#     # Outbox publisher path: only call after the DB transaction committed.
#     client.send_message(QueueUrl=queue_url, MessageBody=payload.to_json())
#     return asdict(payload)
# ---------------------------------------------------------------------------
