# Worksheet — `totp_verify`

**Order:** skim [readings/totp_verify.md](../readings/totp_verify.md) → answer below in writing → read `tests/test_totp_verify.py` → implement `katas/totp_verify.py` → `pytest tests/test_totp_verify.py -q`

Peek at `solutions/totp_verify.py` only after a real attempt.

## Concepts to understand

- **TOTP** (RFC 6238): a shared secret + current time → a short numeric code that rotates every **30 seconds**.
- **Shared secret**: usually base32 (Google Authenticator–style). Both sides must agree on it.
- **Time step / window**: clocks drift. A `window` of `1` means “accept this step ± one neighbor” (±30s each side with the usual 30s period).
- **Library vs crypto from scratch**: hiring guidance cares that you *understand* OTP; reimplementing HMAC-SHA1 is usually the wrong trade for a short challenge. Prefer `pyotp`.

## Short questions (write answers before coding)

1. Why is a 6-digit code alone not enough authentication if someone can replay a freshly captured code forever?
2. What should `verify_totp` do if `window` is negative? If `code` is `"12345"` or `"abcdef"`?
3. In one sentence: what does `for_time` buy you in tests that “use wall-clock now” cannot?

## REPL warm-up

```bash
cd 01-challenge-gym
source .venv/bin/activate   # after pip install -r requirements.txt
python
```

```python
import pyotp
secret = "JBSWY3DPEHPK3PXP"  # test-only secret
totp = pyotp.TOTP(secret)
code = totp.at(1_700_000_000)
print(code)
print(totp.verify(code, for_time=1_700_000_000, valid_window=0))
print(totp.verify(code, for_time=1_700_000_000 + 30, valid_window=0))
print(totp.verify(code, for_time=1_700_000_000 + 30, valid_window=1))
```

Notice how `valid_window` changes acceptance for an adjacent step.

## Implement

Fill in `verify_totp` and `current_code` in `katas/totp_verify.py`. Keep behavior aligned with the docstrings and tests — reject bad input early; raise on negative `window`.

## When to run pytest

```bash
pytest tests/test_totp_verify.py -q
```

Expect failures (`NotImplementedError`) until both functions work. Green for this file = first kata done. Then move to `hold_rules`.
