"""REFERENCE SOLUTION."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SamlAssertion:
    audience: str
    recipient: str
    in_response_to: str | None
    not_before: int
    not_on_or_after: int
    signed: bool


def audience_ok(assertion: SamlAssertion, expected_audience: str) -> bool:
    return assertion.audience == expected_audience


def time_window_ok(assertion: SamlAssertion, now: int, *, skew: int = 60) -> bool:
    return (assertion.not_before - skew) <= now < (assertion.not_on_or_after + skew)


def recipient_ok(assertion: SamlAssertion, acs_url: str) -> bool:
    return assertion.recipient == acs_url


def in_response_to_ok(assertion: SamlAssertion, expected_id: str | None) -> bool:
    return assertion.in_response_to == expected_id


def accept_assertion(
    assertion: SamlAssertion,
    *,
    expected_audience: str,
    acs_url: str,
    now: int,
    expected_in_response_to: str | None,
    skew: int = 60,
) -> bool:
    if not assertion.signed:
        return False
    return (
        audience_ok(assertion, expected_audience)
        and recipient_ok(assertion, acs_url)
        and time_window_ok(assertion, now, skew=skew)
        and in_response_to_ok(assertion, expected_in_response_to)
    )
