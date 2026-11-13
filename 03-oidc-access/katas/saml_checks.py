"""Validate decoded SAML assertion conditions (fixtures only — no live IdP)."""

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
    raise NotImplementedError


def time_window_ok(assertion: SamlAssertion, now: int, *, skew: int = 60) -> bool:
    raise NotImplementedError


def recipient_ok(assertion: SamlAssertion, acs_url: str) -> bool:
    raise NotImplementedError


def in_response_to_ok(assertion: SamlAssertion, expected_id: str | None) -> bool:
    raise NotImplementedError


def accept_assertion(
    assertion: SamlAssertion,
    *,
    expected_audience: str,
    acs_url: str,
    now: int,
    expected_in_response_to: str | None,
    skew: int = 60,
) -> bool:
    raise NotImplementedError
