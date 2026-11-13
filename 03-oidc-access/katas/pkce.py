"""OIDC auth-code + PKCE helpers (RFC 7636)."""

from __future__ import annotations


def code_challenge_s256(verifier: str) -> str:
    """BASE64URL(SHA256(verifier)) without padding."""
    raise NotImplementedError


def verifier_length_ok(verifier: str) -> bool:
    """RFC 7636: 43..128 characters from unreserved set (simplified: len only)."""
    raise NotImplementedError
