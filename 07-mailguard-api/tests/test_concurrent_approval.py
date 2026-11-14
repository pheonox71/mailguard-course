import threading
import time

from katas.concurrent_approval import HoldRow, HoldStore, try_approve

# Widen the check-then-set window so an unlocked read/write reliably races.
_RACE_SLEEP_S = 0.02
_CONCURRENT_ROUNDS = 20


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
        store.race_window = lambda: time.sleep(_RACE_SLEEP_S)
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
