import threading

from katas.concurrent_approval import HoldRow, HoldStore, try_approve


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
    store = HoldStore()
    store.seed(HoldRow(id="h1", state="held"))
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

    assert sorted(results) == [0, 1]
    assert store.get("h1").state == "approved"
