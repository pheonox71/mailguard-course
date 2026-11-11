# 01 — Challenge Gym

Admission-challenge muscle: short, elegant Python with tests; MFA/OTP concepts without overbuilding.

## What this teaches

- Correct, concise Python under a challenge-style bar (small modules, clear specs)
- `pytest` as proof the code does what the README claims
- TOTP verify with a library (RFC 6238) — understand MFA/OTP, don’t reinvent crypto
- Tiny string/rule engines that preview MailGuard hold / missend thinking

## Where HENNGE said it matters

- Backend Admission Challenge: short task + MFA/OTP research; elegant > over-engineered — [Demystifying HENNGE’s hiring process](https://hennge.com/global/info/henka/interview/202406-demystifying_hennges_hiring_process/)
- Early-career stack and challenge culture — [GIP](https://recruit.hennge.com/en/gip/)
- Screening values challenge quality and learning agility — [FAQ for screening process](https://recruit.hennge.com/faq-for-screening-process/)

Related reading: [OWASP MFA Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html), [MDN OTP](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication/OTP).

## Katas

| Module | Lines (approx.) | Idea |
|--------|-----------------|------|
| `katas/totp_verify.py` | ~45 | Verify a 6-digit TOTP (`pyotp`); window for clock skew |
| `katas/hold_rules.py` | ~70 | Ordered hold/allow/reject rules on message text/domains |
| `katas/recipient_risk.py` | ~70 | Normalize emails; flag mixed internal/external missends |

## How to run

```bash
cd 01-challenge-gym
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

**Done when:** all tests green; one TOTP verify kata (library OK); trade-offs below fit on one page.

## Trade-offs / what I’d harden next

- **Library vs from-scratch TOTP:** used `pyotp` on purpose — hiring guidance emphasizes understanding OTP, not reimplementing HMAC. A from-scratch version would burn challenge budget and risk subtle bugs.
- **Hold rules are deliberately dumb:** domain equality + substring only. No regex DSL, no priority weights. First match wins — easy to reason about in an interview; too coarse for production DLP.
- **Recipient risk is local@domain only:** no RFC 5322 / display-name parsing. Enough for a kata; real mail needs a proper address parser.
- **No rate limits / replay store on TOTP:** production MFA needs used-code tracking and lockout. Out of scope here; belongs in `03-mailguard-mfa/`.

**Production gap (Horizon B):** Secure Transfer / Access Control bars still demand multi-year delivery of auth’d services, threat models, and ops — this gym only proves challenge-shaped Python + MFA literacy.
