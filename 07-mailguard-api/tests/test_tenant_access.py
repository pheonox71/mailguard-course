from katas.tenant_access import HoldRecord, get_hold


def _store() -> dict[str, HoldRecord]:
    return {
        "h1": HoldRecord(id="h1", tenant_id="tenant-a", state="held"),
        "h2": HoldRecord(id="h2", tenant_id="tenant-b", state="approved"),
    }


def test_same_tenant_get_200():
    status, hold = get_hold(_store(), "h1", "tenant-a")
    assert status == 200
    assert hold is not None
    assert hold.id == "h1"


def test_cross_tenant_get_prefer_404():
    status, hold = get_hold(_store(), "h2", "tenant-a", prefer_404=True)
    assert status == 404
    assert hold is None


def test_cross_tenant_get_403():
    status, hold = get_hold(_store(), "h2", "tenant-a", prefer_404=False)
    assert status == 403
    assert hold is None


def test_missing_hold_404():
    status, hold = get_hold(_store(), "missing", "tenant-a")
    assert status == 404
    assert hold is None
