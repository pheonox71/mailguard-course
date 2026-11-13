"""Minimal SCIM filter subset (RFC 7644): eq on userName / active."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class User:
    id: str
    user_name: str
    active: bool


def parse_eq_filter(expression: str) -> tuple[str, str]:
    """Parse `attr eq "value"` or `attr eq true|false`. Raise ValueError otherwise."""
    raise NotImplementedError


def apply_filter(users: list[User], expression: str) -> list[User]:
    raise NotImplementedError
