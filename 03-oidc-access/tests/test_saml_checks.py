from katas.saml_checks import SamlAssertion, accept_assertion, time_window_ok

ACS = "https://app.example/acs"
AUD = "https://app.example"

def _a(**kw):
    base = dict(
        audience=AUD,
        recipient=ACS,
        in_response_to="id-1",
        not_before=1000,
        not_on_or_after=2000,
        signed=True,
    )
    base.update(kw)
    return SamlAssertion(**base)

def test_accept_happy():
    assert accept_assertion(
        _a(), expected_audience=AUD, acs_url=ACS, now=1500, expected_in_response_to="id-1"
    )

def test_reject_unsigned():
    assert not accept_assertion(
        _a(signed=False), expected_audience=AUD, acs_url=ACS, now=1500, expected_in_response_to="id-1"
    )

def test_time_skew():
    assert time_window_ok(_a(), 995, skew=60)  # within skew before not_before
    assert not time_window_ok(_a(), 900, skew=60)

def test_audience_mismatch():
    assert not accept_assertion(
        _a(), expected_audience="other", acs_url=ACS, now=1500, expected_in_response_to="id-1"
    )
