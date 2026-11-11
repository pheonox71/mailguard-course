"""REFERENCE SOLUTION — peek only if stuck. Not imported by tests.

Crypto hygiene kata — HMAC integrity + AES-GCM AEAD via standard libraries.
"""

from __future__ import annotations

import hmac
import os
from hashlib import sha256

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

_NONCE_LEN = 12


def integrity_tag(key: bytes, message: bytes) -> str:
    if not key:
        raise ValueError("key must be non-empty")
    return hmac.new(key, message, sha256).hexdigest()


def integrity_ok(key: bytes, message: bytes, tag_hex: str) -> bool:
    if not key:
        raise ValueError("key must be non-empty")
    try:
        expected = bytes.fromhex(tag_hex)
    except ValueError:
        return False
    actual = hmac.new(key, message, sha256).digest()
    return hmac.compare_digest(actual, expected)


def aead_seal(key: bytes, plaintext: bytes, aad: bytes = b"") -> bytes:
    if len(key) != 32:
        raise ValueError("AES-256-GCM key must be 32 bytes")
    nonce = os.urandom(_NONCE_LEN)
    ct = AESGCM(key).encrypt(nonce, plaintext, aad)
    return nonce + ct


def aead_open(key: bytes, blob: bytes, aad: bytes = b"") -> bytes:
    if len(key) != 32:
        raise ValueError("AES-256-GCM key must be 32 bytes")
    if len(blob) < _NONCE_LEN + 16:
        raise ValueError("ciphertext blob too short")
    nonce, ct = blob[:_NONCE_LEN], blob[_NONCE_LEN:]
    try:
        return AESGCM(key).decrypt(nonce, ct, aad)
    except Exception as exc:  # noqa: BLE001 — map auth failures to ValueError
        raise ValueError("aead authentication failed") from exc
