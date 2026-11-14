import threading
import time

from katas.concurrent_approval import HoldRow, HoldStore, try_approve

# Widen the check-then-set window so an unlocked read/write reliably races.
# Delay is injected by the test on store reads — student code must not call a hook.
_RACE_SLEEP_S = 0.02
_CONCURRENT_ROUNDS = 20


def _inject_read_delay(store: HoldStore, delay_s: float = _RACE_SLEEP_S) -> None:
    """Replace store.rows so .get / [] return a proxy that sleeps when .state is read.

    Sleeping on the state *read* (not after the dict lookup returns) opens a window
    where two unlocked threads can both observe 'held' before either writes.
    """
    underlying = dict(store.rows)

    class _DelayedRow:
        __slots__ = ("_row",)

        def __init__(self, row: HoldRow) -> None:
            object.__setattr__(self, "_row", row)

        @property
        def id(self) -> str:
            return self._row.id

        @property
        def state(self) -> str:
            # Snapshot first, then sleep so a peer can also observe 'held'
            # before either caller writes (classic TOCTOU window).
            value = self._row.state
            time.sleep(delay_s)
            return value

        @state.setter
        def state(self, value: str) -> None:
            self._row.state = value

    def _wrap(value):
        return value if value is None else _DelayedRow(value)

    class _DelayedRows(dict):
        def get(self, key, default=None):  # noqa: ANN001
            if key in self:
                return _wrap(super().get(key))
            return default

        def __getitem__(self, key):  # noqa: ANN001
            return _wrap(super().__getitem__(key))

    store.rows = _DelayedRows(underlying)


def test_approve_from_held_returns_rowcount_one():
    store = HoldStore()
    store.seed(HoldRow(id="h1", state="held"))
    assert try_approve(store, "h1") == 1
    assert store.get("h1") is not None
    assert store.get("h1").state == "approved"


def test_second_approve_loses_with_rowcount_zero():
    store = HoldStore()
    store.seed(HoldRow(id="h1", state="held"))
    assert try_approve(store, "h1") == 1
    assert try_approve(store, "h1") == 0
    assert store.get("h1").state == "approved"


def test_missing_or_wrong_state_returns_zero():
    store = HoldStore()
    assert try_approve(store, "missing") == 0
    store.seed(HoldRow(id="h2", state="rejected"))
    assert try_approve(store, "h2") == 0


def test_concurrent_approvals_exactly_one_winner():
    """Two threads start together; exactly one approve must win each round."""
    # Probe on the main thread so an unfinished stub raises NotImplementedError
    # cleanly (no PytestUnhandledThreadExceptionWarning from workers).
    probe = HoldStore()
    probe.seed(HoldRow(id="probe", state="held"))
    assert try_approve(probe, "probe") == 1

    for _ in range(_CONCURRENT_ROUNDS):
        store = HoldStore()
        store.seed(HoldRow(id="h1", state="held"))
        _inject_read_delay(store)
        results: list[int] = []
        barrier = threading.Barrier(2)

        def worker() -> None:
            barrier.wait()
            results.append(try_approve(store, "h1"))

        threads = [threading.Thread(target=worker) for _ in range(2)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert sorted(results) == [0, 1], f"expected exactly one winner, got {results}"
        assert store.get("h1").state == "approved"
