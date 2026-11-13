"""Crypto hygiene kata — use libraries correctly; never invent crypto.

Misuse-focused: HMAC for integrity tags, AEAD for confidentiality+integrity,
reject empty/short keys. Do not implement AES or hashing schemes from scratch.

Implement the stubs. Read assignments/crypto_hygiene.md and
tests/test_crypto_hygiene.py before coding. Peek at solutions/ only if stuck.
"""

from __future__ import annotations

# TODO: imports you need (e.g. hmac, hashlib, os, cryptography AESGCM)


def integrity_tag(key: bytes, message: bytes) -> str:
    """Return hex-encoded HMAC-SHA256 of `message` under `key`.

    Raise ValueError if `key` is empty.
    """
    raise NotImplementedError("implement integrity_tag — see assignments/crypto_hygiene.md")


def integrity_ok(key: bytes, message: bytes, tag_hex: str) -> bool:
    """Return True if `tag_hex` is a valid HMAC-SHA256 for `message` under `key`.

    Use a constant-time compare. Return False for malformed hex or empty key
    (do not raise for bad tag/hex — only raise ValueError for empty key).
    """
    raise NotImplementedError("implement integrity_ok — see assignments/crypto_hygiene.md")


def aead_seal(key: bytes, plaintext: bytes, aad: bytes = b"") -> bytes:
    """Seal with AES-256-GCM. Return nonce (12 bytes) || ciphertext+tag.

    `key` must be exactly 32 bytes. Raise ValueError otherwise.
    Generate a fresh random nonce each call (never reuse nonce with same key).
    """
    raise NotImplementedError("implement aead_seal — see assignments/crypto_hygiene.md")


def aead_open(key: bytes, blob: bytes, aad: bytes = b"") -> bytes:
    """Open a blob from `aead_seal`. Raise ValueError on bad key length,
    truncated blob, or authentication failure.
    """
    raise NotImplementedError("implement aead_open — see assignments/crypto_hygiene.md")
