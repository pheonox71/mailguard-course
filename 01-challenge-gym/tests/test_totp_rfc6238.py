"""Educational fixtures only — RFC 6238 Appendix B vectors (not live secrets).

RFC 6238 Appendix B vectors (+ errata seed lengths).
"""

from __future__ import annotations

import pytest

from katas.totp_rfc6238 import hotp_truncate, totp_rfc6238

# Errata: seed length matches hash (20 / 32 / 64 ASCII bytes).
SEED_SHA1 = b"12345678901234567890"
SEED_SHA256 = b"12345678901234567890123456789012"
SEED_SHA512 = b"1234567890123456789012345678901234567890123456789012345678901234"

# Appendix B — 8-digit TOTP
SHA1_VECTORS = [
    (59, "94287082"),
    (1111111109, "07081804"),
    (1111111111, "14050471"),
    (1234567890, "89005924"),
    (2000000000, "69279037"),
    (20000000000, "65353130"),
]
SHA256_VECTORS = [
    (59, "46119246"),
    (1111111109, "68084774"),
    (1111111111, "67062674"),
    (1234567890, "91819424"),
    (2000000000, "90698825"),
    (20000000000, "77737706"),
]
SHA512_VECTORS = [
    (59, "90693936"),
    (1111111109, "25091201"),
    (1111111111, "99943326"),
    (1234567890, "93441116"),
    (2000000000, "38618901"),
    (20000000000, "47863826"),
]


@pytest.mark.parametrize("t,expected", SHA1_VECTORS)
def test_sha1_appendix_b(t, expected):
    assert totp_rfc6238(SEED_SHA1, t, digits=8, digest="sha1") == expected


@pytest.mark.parametrize("t,expected", SHA256_VECTORS)
def test_sha256_appendix_b(t, expected):
    assert totp_rfc6238(SEED_SHA256, t, digits=8, digest="sha256") == expected


@pytest.mark.parametrize("t,expected", SHA512_VECTORS)
def test_sha512_appendix_b(t, expected):
    assert totp_rfc6238(SEED_SHA512, t, digits=8, digest="sha512") == expected


def test_ten_digit_property():
    code = totp_rfc6238(SEED_SHA512, 1234567890, digits=10, digest="sha512")
    assert len(code) == 10
    assert code.isdigit()
    assert int(code) < 2**31


def test_custom_step_and_t0():
    # With step=1 and t0=t, counter is 0 → deterministic vs step=30.
    a = totp_rfc6238(SEED_SHA1, 100, digits=8, digest="sha1", step=1, t0=100)
    b = totp_rfc6238(SEED_SHA1, 0, digits=8, digest="sha1", step=30, t0=0)
    # counter 0 for both → same HOTP
    assert a == b


def test_hotp_truncate_rejects_bad_digits():
    with pytest.raises(ValueError):
        hotp_truncate(b"\x00" * 20, 5)


def test_bad_step_raises():
    with pytest.raises(ValueError):
        totp_rfc6238(SEED_SHA1, 59, step=0)
