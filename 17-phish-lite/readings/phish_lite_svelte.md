# Reading — Ethical phishing-training app

## Learning objectives

1. Design a **Svelte/SvelteKit**-shaped training UI with consent and **no credential capture**.
2. Prefer **report rate** and time-to-report over vanity click rates.
3. Keep simulations clearly labeled as training — never weaponize against unaware users.

**Why this matters.** A pixel-perfect fake login that POSTs passwords “for scoring” is not training — it is a credential harvester with a story. Organizations also get sued or lose trust when campaigns omit disclosure. Prefer metrics that reward reporting. On the job, usable-security work for mail/identity products sits next to awareness programs; both need the same honesty rule.

**How it works.**

1. Structure SvelteKit routes for consent → scenario → results.
2. Gate the experience on consent and a visible **SIMULATION** label.
3. Score with helpers such as `scoreAnswers` / `reportRate` / `timeToReportSeconds` (see `score.js`); lock ethics with `ethicalSimOk({ consent, capturesCredentials })`.
4. Keep aggregates private; never target real customer mailboxes without notice.
5. Tests (Vitest/Playwright-class) fail if credential capture is enabled or consent is missing.

```text
SvelteKit route: /train → consent banner → scenarios → results (private aggregates)
```

### Worked example

Ethics + metrics helpers (implementations live in the kata; contract shape):

```js
// Why no password fields: capturing secrets is out of scope and unethical here
ethicalSimOk({ consent: true, capturesCredentials: false })  // → true
ethicalSimOk({ consent: true, capturesCredentials: true })   // → false

// reportRate(reported, opportunities) — prefer this over vanity click rates
reportRate(8, 10)  // → 0.8

// timeToReportSeconds(sentAt, reportedAt) — faster reporting is the job skill
```

```text
# Why label “SIMULATION”: users must distinguish training from real IdP pages
```

### Common misconceptions / what goes wrong

- **“We’ll strip password fields after the demo.”** If the form can capture secrets, the ethics gate must fail in tests — do not ship a harvester “temporarily.”
- **“Consent once in a README is enough.”** The UI itself must disclose purpose before scenarios ([NIST SP 800-50](https://csrc.nist.gov/publications/detail/sp/800-50/final)).
- **“Click-through rate is the KPI.”** Report rate and time-to-report align with how people should treat real suspicious mail.
- **“Weaponize against unaware coworkers for realism.”** Unannounced campaigns without policy/consent are out of scope for this course.

## Read these (verified)

1. [SvelteKit docs](https://kit.svelte.dev/docs/introduction)
2. [Vitest](https://vitest.dev/) / [Playwright](https://playwright.dev/)
3. [NIST SP 800-50](https://csrc.nist.gov/publications/detail/sp/800-50/final) — awareness training concepts

## Next step

Extend `score.js` metrics → assignment → quiz. Optional: scaffold a local SvelteKit app outside `my-work` patterns you already use.
