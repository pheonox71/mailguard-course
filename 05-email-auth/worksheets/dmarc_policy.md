# Worksheet — `dmarc_policy`

**Order:** email_auth reading + worksheet → this page → `tests/test_dmarc_policy.py` → implement stub.

## Concepts

- Tags are `;`-separated `name=value` pairs. Tag **names** are case-insensitive.
- Required: `v=DMARC1`, `p=none|quarantine|reject`.
- Defaults in this kata: `pct=100`, `adkim=r`, `aspf=r`, empty `rua`/`ruf`, no `sp`.

## Short questions

1. What does `adkim=s` change versus `adkim=r` at a high level?
2. Why might `pct=25` appear during a rollout?

## Implement

Fill `parse_dmarc_record` and `explains_spoofing_gap`. Ignore unknown tags. Raise `ValueError` on empty input, missing/invalid `v` or `p`, bad `pct`.

```bash
pytest tests/test_dmarc_policy.py -q
```
