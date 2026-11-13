# Assignment — `crypto_hygiene`

**Language:** Python 3 + pytest (implement `katas/crypto_hygiene.py`; use the standard library / well-known crypto APIs — do not invent algorithms).

**Order:** skim [readings/crypto_hygiene.md](../readings/crypto_hygiene.md) → answer below in writing → read `tests/test_crypto_hygiene.py` → implement `katas/crypto_hygiene.py` → `pytest tests/test_crypto_hygiene.py -q`

Peek at `solutions/crypto_hygiene.py` only after a real attempt.

## Concepts to understand

- **HMAC** (Hash-based Message Authentication Code): secret key + message → tag. Detects tampering *if* the key stays secret.
- **AEAD** (Authenticated Encryption with Associated Data): ciphertext that fails open if modified; optional **AAD** (associated data) is authenticated but not encrypted (e.g. a version string).
- **TLS / certificates**: everyday AEAD + public-key identity for connections — you configure and verify; you do not reimplement.
- **Key lifecycle**: generate with a CSPRNG → store outside git → rotate → revoke/destroy. Wrong length keys should fail loudly.

## Short questions (write answers before coding)

1. Why is `sha256(message)` alone insufficient to detect an attacker who can rewrite both the message *and* a stored hash?
2. Why is reusing the same AES-GCM **nonce** with the same key catastrophic — what property collapses?
3. Why does “authenticated” in AEAD matter on the job versus encrypt-only modes that still look “encrypted” in logs?
4. Why document rotate + revoke (not only generate) for a MailGuard webhook HMAC secret — what fails after a leak if you only generate once?
5. Scenario: ciphertext verifies with AAD `v1` but a proxy strips the version header. What should open do and why?

## REPL warm-up

```bash
# Why: cryptography + hmac must come from the course venv, not a random global install
cd 01-challenge-gym
source .venv/bin/activate
python
```

```python
import hmac, os
from hashlib import sha256
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = b"k" * 32
msg = b"hello"
print(hmac.new(key, msg, sha256).hexdigest())

nonce = os.urandom(12)
blob = nonce + AESGCM(key).encrypt(nonce, msg, b"v1")
print(AESGCM(key).decrypt(blob[:12], blob[12:], b"v1"))
```

## Implement

Fill `integrity_tag`, `integrity_ok`, `aead_seal`, and `aead_open` in `katas/crypto_hygiene.py`. Match docstrings and tests.

## When to run pytest

```bash
pytest tests/test_crypto_hygiene.py -q
```
