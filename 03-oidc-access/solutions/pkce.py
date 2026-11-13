"""REFERENCE SOLUTION."""

from __future__ import annotations

import base64
import hashlib


def code_challenge_s256(verifier: str) -> str:
    digest = hashlib.sha256(verifier.encode("ascii")).digest()
    return base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")


def verifier_length_ok(verifier: str) -> bool:
    return 43 <= len(verifier) <= 128
