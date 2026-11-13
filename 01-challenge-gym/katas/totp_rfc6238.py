"""Parametrized TOTP / HOTP truncation — RFC 6238 + RFC 4226.

Implement yourself with hmac + struct (no pyotp). Validate against
RFC 6238 Appendix B test vectors and the errata (seed length differs
per hash). Digests: sha1 / sha256 / sha512. Digits: 6–10.
"""

from __future__ import annotations

from typing import Literal

DigestName = Literal["sha1", "sha256", "sha512"]


def hotp_truncate(hmac_digest: bytes, digits: int) -> str:
    """RFC 4226 §5.3 dynamic truncation → zero-padded decimal string.

    Raise ValueError if digits not in 6..10 or digest shorter than 20 bytes.
    """
    raise NotImplementedError


def totp_rfc6238(
    secret: bytes,
    t: int,
    *,
    digits: int = 8,
    digest: DigestName = "sha1",
    step: int = 30,
    t0: int = 0,
) -> str:
    """Return TOTP for unix time `t` (RFC 6238 §4).

    counter = floor((t - t0) / step). HMAC with `digest` over 8-byte big-endian
    counter, then hotp_truncate. Raise ValueError for bad digits/step or t < t0.
    """
    raise NotImplementedError
