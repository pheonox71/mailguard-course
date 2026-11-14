"""Hold + outbox in one transaction.

Implement `apply_hold_change_with_outbox` so the hold state change and outbox
row commit together (same transactional unit). Helper types below are given.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field


@dataclass
class OutboxRow:
    id: str
    payload: dict
    published: bool = False


@dataclass
class HoldRow:
    id: str
    state: str


@dataclass
class MemoryTxn:
    holds: dict[str, HoldRow] = field(default_factory=dict)
    outbox: list[OutboxRow] = field(default_factory=list)
    committed: bool = False
    _pending_holds: dict[str, HoldRow] = field(default_factory=dict)
    _pending_outbox: list[OutboxRow] = field(default_factory=list)

    def stage_hold(self, hold: HoldRow) -> None:
        self._pending_holds[hold.id] = hold

    def stage_outbox(self, row: OutboxRow) -> None:
        self._pending_outbox.append(row)

    def commit(self) -> None:
        self.holds.update(self._pending_holds)
        self.outbox.extend(self._pending_outbox)
        self._pending_holds.clear()
        self._pending_outbox.clear()
        self.committed = True

    def rollback(self) -> None:
        self._pending_holds.clear()
        self._pending_outbox.clear()
        self.committed = False


def apply_hold_change_with_outbox(
    txn: MemoryTxn,
    *,
    hold_id: str,
    new_state: str,
    payload: dict,
) -> None:
    """Stage hold + outbox, then commit so both land or neither does.

    Use `uuid` for the outbox row id; leave `published=False` until a publisher drains it.
    """
    raise NotImplementedError
