# Assignment — `dmarc_policy`

**Language:** Python 3 + pytest (implement `katas/dmarc_policy.py`).

**Order:** email_auth reading + assignment → this page → `tests/test_dmarc_policy.py` → implement stub.

## Concepts

- Tags are `;`-separated `name=value` pairs. Tag **names** are case-insensitive.
- Required: `v=DMARC1` **as the first tag**, plus `p=none|quarantine|reject`.
- Defaults in this kata: `pct=100` (legacy), `t=n` (no test mode), `adkim=r`, `aspf=r`, empty `rua`/`ruf`, no `sp`/`np`/`psd`.
- RFC 9989 removed `pct` and added `t` (test mode), `np` (non-existent subdomain policy), and `psd`. Still parse legacy `pct` when present.

## Short questions

1. What does `adkim=s` change versus `adkim=r` at a high level?
2. What replaced `pct` in RFC 9989 and why?

## Implement

Fill `parse_dmarc_record` and `explains_spoofing_gap`. Ignore unknown tags. Raise `ValueError` on empty input, missing/invalid `v` or `p`, `v` not first, bad `pct`/`t`/`psd`.

```bash
pytest tests/test_dmarc_policy.py -q
```
