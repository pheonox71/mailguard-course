"""REFERENCE SOLUTION — peek only if stuck."""

from __future__ import annotations

import hashlib
import hmac
import struct
from typing import Literal

DigestName = Literal["sha1", "sha256", "sha512"]

_HASH = {
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


def hotp_truncate(hmac_digest: bytes, digits: int) -> str:
    if digits < 6 or digits > 10:
        raise ValueError("digits must be 6..10")
    if len(hmac_digest) < 20:
        raise ValueError("HMAC digest too short for truncation")
    offset = hmac_digest[-1] & 0x0F
    binary = (
        ((hmac_digest[offset] & 0x7F) << 24)
        | ((hmac_digest[offset + 1] & 0xFF) << 16)
        | ((hmac_digest[offset + 2] & 0xFF) << 8)
        | (hmac_digest[offset + 3] & 0xFF)
    )
    otp = binary % (10 ** digits)
    return str(otp).zfill(digits)


def totp_rfc6238(
    secret: bytes,
    t: int,
    *,
    digits: int = 8,
    digest: DigestName = "sha1",
    step: int = 30,
    t0: int = 0,
) -> str:
    if digits < 6 or digits > 10:
        raise ValueError("digits must be 6..10")
    if step <= 0:
        raise ValueError("step must be > 0")
    if t < t0:
        raise ValueError("t must be >= t0")
    if digest not in _HASH:
        raise ValueError("unsupported digest")
    counter = (t - t0) // step
    msg = struct.pack(">Q", counter)
    digest_bytes = hmac.new(secret, msg, _HASH[digest]).digest()
    return hotp_truncate(digest_bytes, digits)
