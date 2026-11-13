from katas.sli_math import availability, error_budget_remaining

def test_availability():
    assert availability(99, 100) == 0.99

def test_budget():
    # SLO 99% over 1000 events => 10 allowed failures; at 99.5% used 5, remaining 5
    assert abs(error_budget_remaining(slo=0.99, availability=0.995, window_events=1000) - 5.0) < 1e-9
