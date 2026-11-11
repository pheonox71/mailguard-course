# 01 — Challenge Gym

Challenge-style muscle: short, elegant Python with tests; MFA/OTP concepts without overbuilding.

**Learn-by-building:** stubs in `katas/`, behavior defined by `tests/`, guided by `worksheets/` + `readings/`. Reference code lives in `solutions/` — peek only if stuck.

## What this teaches

- Correct, concise Python under a challenge-style bar (small modules, clear specs)
- Reading tests as the contract before writing code
- TOTP verify with a library (RFC 6238) — understand MFA/OTP, don’t reinvent crypto
- Tiny string/rule engines that preview MailGuard hold / missend thinking

## Why it matters for career prep

- Short coding tasks that pair implementation with MFA/OTP research; elegant > over-engineered
- Early-career cloud security / SaaS stacks reward challenge quality and learning agility
- Screening and interviews often value clear specs, trade-off writing, and stack familiarity

Related reading: [OWASP MFA Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html), [MDN OTP](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication/OTP).

## Workflow (do not spoil yourself)

For **each** kata, in order:

1. **Readings** — `readings/<kata>.md`: short intro + verified external links (RFC/OWASP/MDN/docs)
2. **Self-check** — `quizzes/<kata>.md`: short quiz after the reading (answer key at bottom)
3. **Worksheet** — `worksheets/<kata>.md`: concepts, short written questions, REPL warm-up
4. **Read tests** — `tests/test_<kata>.py` defines correct behavior
5. **Implement stubs** — fill `katas/<kata>.py` (`NotImplementedError` → real code)
6. **pytest green** — run that file’s tests, then the full suite when all three are done

```bash
pytest tests/test_totp_verify.py -q    # first kata
pytest -q                              # all katas
```

**Do not** open `solutions/` until you have attempted the stub. Solutions are not imported by tests.

Index of readings: [`readings/README-01-challenge-gym-readings.md`](./readings/README-01-challenge-gym-readings.md).  
Index of quizzes: [`quizzes/README-01-challenge-gym-quizzes.md`](./quizzes/README-01-challenge-gym-quizzes.md).

## Layout

| Path | Role |
|------|------|
| `readings/` | Short intros + verified external links per kata |
| `quizzes/` | Short self-checks after each reading (pattern for later modules) |
| `worksheets/` | Guided learning before/while implementing |
| `katas/` | Stubs you implement (`raise NotImplementedError`) |
| `tests/` | Thorough pytest contract — do not weaken these |
| `solutions/` | Reference implementations — peek only if stuck |

## Katas

| Kata | Readings | Quiz | Worksheet | Stub | Tests |
|------|----------|------|-----------|------|-------|
| TOTP verify | [`readings/totp_verify.md`](./readings/totp_verify.md) | [`quizzes/totp_verify.md`](./quizzes/totp_verify.md) | `worksheets/totp_verify.md` | `katas/totp_verify.py` | `tests/test_totp_verify.py` |
| Hold rules | [`readings/hold_rules.md`](./readings/hold_rules.md) | [`quizzes/hold_rules.md`](./quizzes/hold_rules.md) | `worksheets/hold_rules.md` | `katas/hold_rules.py` | `tests/test_hold_rules.py` |
| Recipient risk | [`readings/recipient_risk.md`](./readings/recipient_risk.md) | [`quizzes/recipient_risk.md`](./quizzes/recipient_risk.md) | `worksheets/recipient_risk.md` | `katas/recipient_risk.py` | `tests/test_recipient_risk.py` |

Start with **totp_verify**: open [`readings/totp_verify.md`](./readings/totp_verify.md), then its worksheet.

## How to run

```bash
cd 01-challenge-gym
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

### Expected results

| State | Command | Expect |
|-------|---------|--------|
| Fresh stubs (as shipped) | `pytest -q` | **FAIL** — `NotImplementedError` from unimplemented katas |
| After you implement (or copy a solution into `katas/` to check) | `pytest -q` | **PASS** — 15 tests |

To verify a reference solution without permanently overwriting your work:

```bash
cp solutions/totp_verify.py katas/totp_verify.py
pytest tests/test_totp_verify.py -q   # should PASS
git checkout -- katas/totp_verify.py  # restore stub / your WIP
```

**Done when:** all tests green from *your* implementations in `katas/`; trade-offs below still fit on one page.

## Trade-offs / what I’d harden next

- **Library vs from-scratch TOTP:** use `pyotp` on purpose — challenge-style tasks emphasize understanding OTP, not reimplementing HMAC. A from-scratch version would burn challenge budget and risk subtle bugs.
- **Hold rules are deliberately dumb:** domain equality + substring only. No regex DSL, no priority weights. First match wins — easy to reason about in an interview; too coarse for production DLP.
- **Recipient risk is local@domain only:** no RFC 5322 / display-name parsing. Enough for a kata; real mail needs a proper address parser.
- **No rate limits / replay store on TOTP:** production MFA needs used-code tracking and lockout. Out of scope here; belongs in `03-mailguard-mfa/`.

**Production gap (later phase):** production identity / DLP / secure-transfer SaaS roles still demand multi-year delivery of auth’d services, threat models, and ops — this gym only proves challenge-shaped Python + MFA literacy.
