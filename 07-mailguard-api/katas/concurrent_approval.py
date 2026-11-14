"""One-winner concurrent approve (optimistic UPDATE WHERE state='held').

Two operators can race on the same held message. Only the first successful
`UPDATE … WHERE state='held'` must win (rowcount == 1); the loser gets 0.
"""

from __future__ import annotations

import threading
from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass
class HoldRow:
    id: str
    state: str


@dataclass
class HoldStore:
    """In-memory holds. Use `lock` around check-and-set so races stay one-winner.

    `race_window` is a no-op by default. Call it after you observe state and
    before you write so the concurrent test can inject a delay and widen the
    race (still safe when held under `lock`).
    """

    rows: dict[str, HoldRow] = field(default_factory=dict)
    lock: threading.Lock = field(default_factory=threading.Lock)
    race_window: Callable[[], None] = field(default=lambda: None)

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

    Hold `store.lock` for the whole check-and-set. After reading state (and
    deciding it is still 'held'), call `store.race_window()` before writing.
    """
    raise NotImplementedError
