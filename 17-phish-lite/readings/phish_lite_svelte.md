# Reading — Ethical phishing-training app

## Learning objectives

1. Design a **Svelte/SvelteKit**-shaped training UI with consent and **no credential capture**.
2. Prefer **report rate** and time-to-report over vanity click rates.
3. Keep simulations clearly labeled as training — never weaponize against unaware users.

**Why this matters.** A pixel-perfect fake login that POSTs passwords “for scoring” is not training — it is a credential harvester with a story. Organizations also get sued or lose trust when campaigns omit disclosure. Prefer metrics that reward reporting. On the job, usable-security work for mail/identity products sits next to awareness programs; both need the same honesty rule.

**How it works.** Svelte/SvelteKit structures routes and components for consent → scenario → results. Scoring code (e.g. `score.js`) computes report rate = reports / opportunities (and optionally time-to-report). Tests (Vitest/Playwright-class) lock ethics helpers such as `ethicalSimOk`. Never target real customer mailboxes without notice.

```text
SvelteKit route: /train → consent banner → scenarios → results (private aggregates)
```

Annotated mindset for any form field:

```text
# Why no password inputs: capturing secrets is out of scope and unethical here
# Why label “SIMULATION”: users must distinguish training from real IdP pages
```

## Read these (verified)

1. [SvelteKit docs](https://kit.svelte.dev/docs/introduction)
2. [Vitest](https://vitest.dev/) / [Playwright](https://playwright.dev/)
3. [NIST SP 800-50](https://csrc.nist.gov/publications/detail/sp/800-50/final) — awareness training concepts

## Next step

Extend `score.js` metrics → assignment → quiz. Optional: scaffold a local SvelteKit app outside `my-work` patterns you already use.
