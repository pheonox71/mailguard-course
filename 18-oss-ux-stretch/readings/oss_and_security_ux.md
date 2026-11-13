# Reading — OSS contribution & security UX

## Learning objectives

1. Describe a respectful OSS contribution loop (read contributing guide → issue → minimal PR → respond to review).
2. List three qualities of a good **security warning** in an admin UI (clarity, action, no alarm fatigue).
3. Explain why phishing *simulations* need consent/honesty framing when used for learning.

**Why this matters.** Solo repos do not prove you can collaborate on security-sensitive code. Weak warning UX (scary modals users click through forever) creates alarm fatigue and missends still ship. Career-prep portfolios that show “I can collaborate beyond a solo repo” often include a small upstream contribution and evidence you care how humans meet security controls. On the job, mail/identity admin UIs live or die on clear hold/release warnings — not denser red banners.

**How it works.**

1. **OSS loop:** read `CONTRIBUTING` → find/create issue → minimal PR with test plan → respond to review.
2. **Security UX:** state the risk, the consequence, and the primary/secondary actions; avoid permanent one-click dismiss of critical warnings.
3. **Training honesty:** learning UIs disclose purpose; never harvest credentials (ties to Module 17).

```text
Read guide → reproduce → small PR → CI + review → merge
Hold UI: clear consequence → confirm release → audit log
```

Trade-off: more friction on release can prevent missend but slows legitimate ops — design confirmations that match severity.

## Short intro

MailGuard’s admin hold/release flow is a natural place to practice warning copy and confirmation UX.

## Videos (verified)

Prefer the written Open Source Guides + NN/g + Chromium enamel links below (contribution and warning-UX video IDs bitrot quickly).  
Optional: search YouTube for “usable security warnings” / “alarm fatigue security UX” from academic or browser-team talks and confirm the current title before watching.

Prefer written links if a video moves.

## Annotated contribution commands

```bash
# Why fork + branch: keep proposed changes reviewable and reversible
git checkout -b fix/hold-warning-copy
# Why tests/screenshots in the PR: reviewers verify without guessing
```

## Read these (verified)

1. [GitHub — Open Source Guides: How to contribute](https://opensource.guide/how-to-contribute/) — practical contribution path (issue → PR → review).
2. [First Contributions](https://github.com/firstcontributions/first-contributions) — friendly first-PR practice (optional sandbox).
3. [NN/g — Error Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/) — clear, actionable messages (apply carefully to security warnings).
4. [Chromium — Permission UX / quiet UI notes](https://www.chromium.org/Home/chromium-security/enamel/) — browser-team thinking on interruptions (skim).
5. [OWASP — Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — only for “don’t train users into unsafe clicks” mindset when designing phishing *education* UIs.

## Next step

Continue with the assignment from the downloads on this page.
