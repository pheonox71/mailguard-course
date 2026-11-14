"""OIDC id_token claim checks (educational JWT decode + validation)."""

from __future__ import annotations

from typing import Any


def decode_jwt_unverified(token: str) -> tuple[dict[str, Any], dict[str, Any], str]:
    """Decode JWT header and payload without verifying the signature.

    Returns ``(header, payload, signature_b64)``. Reject malformed tokens.
    """
    raise NotImplementedError


def validate_id_token_claims(
    token: str,
    *,
    expected_iss: str,
    expected_aud: str | list[str],
    expected_nonce: str | None = None,
    now: int | None = None,
    allowed_algs: tuple[str, ...] = ("RS256", "ES256"),
    clock_skew_seconds: int = 60,
) -> dict[str, Any]:
    """Validate id_token claims: alg allow-list (reject ``none``), iss, aud, exp, nonce.

    Signature verification against JWKS is a separate production step — see
    ``fetch_jwks``. Raise a clear error on any failed check.
    """
    raise NotImplementedError


def fetch_jwks(jwks_url: str, *, timeout: float = 5.0) -> dict[str, Any]:
    """Fetch a JSON Web Key Set from ``jwks_url`` (for conceptual JWKS wiring).

    Production verifiers match ``header['kid']`` to a JWK and verify the JWT
    signature before trusting claims. Implement a stdlib HTTP GET that returns
    the parsed JWKS object.
    """
    raise NotImplementedError
