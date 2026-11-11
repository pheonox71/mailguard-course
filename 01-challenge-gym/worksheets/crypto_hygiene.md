# Worksheet — `crypto_hygiene`

**Order:** skim [readings/crypto_hygiene.md](../readings/crypto_hygiene.md) → answer below in writing → read `tests/test_crypto_hygiene.py` → implement `katas/crypto_hygiene.py` → `pytest tests/test_crypto_hygiene.py -q`

Peek at `solutions/crypto_hygiene.py` only after a real attempt.

## Concepts to understand

- **HMAC** (Hash-based Message Authentication Code): secret key + message → tag. Detects tampering *if* the key stays secret.
- **AEAD** (Authenticated Encryption with Associated Data): ciphertext that fails open if modified; optional **AAD** (associated data) is authenticated but not encrypted (e.g. a version string).
- **TLS / certificates**: everyday AEAD + public-key identity for connections — you configure and verify; you do not reimplement.
- **Key lifecycle**: generate with a CSPRNG → store outside git → rotate → revoke/destroy. Wrong length keys should fail loudly.

## Short questions (write answers before coding)

1. Why is `sha256(message)` alone insufficient to detect an attacker who can rewrite both the message *and* a stored hash?
2. What goes wrong if you reuse the same AES-GCM **nonce** with the same key for two different plaintexts?
3. In one sentence: what does “authenticated” buy you in AEAD that “encrypt-only” does not?
4. Name two key-lifecycle steps you would document for a MailGuard webhook HMAC secret.

## REPL warm-up

```bash
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
