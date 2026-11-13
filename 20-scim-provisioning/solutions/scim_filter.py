"""REFERENCE SOLUTION."""

from __future__ import annotations

import re
from dataclasses import dataclass

@dataclass
class User:
    id: str
    user_name: str
    active: bool

_EQ = re.compile(r'^(\w+)\s+eq\s+(true|false|"[^"]*")$', re.I)

def parse_eq_filter(expression: str) -> tuple[str, str]:
    m = _EQ.match(expression.strip())
    if not m:
        raise ValueError("unsupported filter")
    attr, raw = m.group(1), m.group(2)
    if raw.lower() in {"true", "false"}:
        return attr, raw.lower()
    return attr, raw[1:-1]

def apply_filter(users: list[User], expression: str) -> list[User]:
    attr, value = parse_eq_filter(expression)
    attr_l = attr.lower()
    out: list[User] = []
    for u in users:
        if attr_l == "username" and u.user_name == value:
            out.append(u)
        elif attr_l == "active":
            want = value == "true"
            if u.active == want:
                out.append(u)
        else:
            raise ValueError("unsupported attr")
    return out
