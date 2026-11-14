"""One-winner concurrent approve (optimistic UPDATE WHERE state='held').

Two operators can race on the same held message. Only the first successful
`UPDATE … WHERE state='held'` must win (rowcount == 1); the loser gets 0.
"""

from __future__ import annotations

import threading
from dataclasses import dataclass, field


@dataclass
class HoldRow:
    id: str
    state: str


@dataclass
class HoldStore:
    """In-memory holds. Use `lock` around check-and-set so races stay one-winner."""

    rows: dict[str, HoldRow] = field(default_factory=dict)
    lock: threading.Lock = field(default_factory=threading.Lock)

    def seed(self, hold: HoldRow) -> None:
        with self.lock:
            self.rows[hold.id] = HoldRow(id=hold.id, state=hold.state)

    def get(self, hold_id: str) -> HoldRow | None:
        with self.lock:
            row = self.rows.get(hold_id)
            return None if row is None else HoldRow(id=row.id, state=row.state)


def try_approve(store: HoldStore, hold_id: str) -> int:
    """Approve only while state is still 'held'.

    Equivalent to:
      UPDATE holds SET state='approved' WHERE id=? AND state='held'
    Return the rowcount: 1 if this caller won, 0 otherwise (missing, already
    approved/rejected/released, or lost the race).

    Hold `store.lock` for the whole check-and-set (read state, then write).
    """
    raise NotImplementedError
