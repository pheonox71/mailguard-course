# Reading — Phish Lite

## Learning objectives

1. Build a small awareness quiz UI (Svelte preferred).
2. Label the experience as a learning simulation.
3. Prefer report-rate metrics over “gotcha” humiliation.

**Why this matters.** Phishing remains a top initial-access path into mail and identity systems. Awareness tools help — but badly designed simulations harvest passwords, shame clickers, or train people to distrust IT. Without clear learning labels and report-focused metrics, you optimize for “gotchas” instead of healthy reporting culture. On the job, security teams are judged on whether people **report** suspicious mail quickly, not only on raw click rates.

**How it works.**

1. Disclose purpose up front (consent / learning label) so participants know this is training.
2. Present labeled scenarios (quiz UI — Svelte preferred); score answers without collecting real passwords.
3. Offer a **report** action and compute **report rate** (and optionally time-to-report).
4. Debrief clearly; avoid public shame boards.
5. The graded kata scores quiz answers and computes a simple report-rate metric.

```text
Consent / disclosure → scenario quiz → optional “report” action
                    → score + report-rate (not public shame boards)
```

Trade-off: hyper-realistic login clones teach recognition but cross into credential-capture risk — this course forbids that pattern.

### Worked example

Report-rate metric (same idea as `score.js` in this module’s kata):

```text
report_rate = reported / (reported + clicked)
# Example: reportRate(3, 1) → 0.75  (three reports, one click-without-report)
# “clicked” here means non-report outcomes that still count toward the denom.
# Why prefer this over vanity click rates alone: rewards the behavior you want on real mail.
```

Ethics gate checklist:

```text
[ ] Consent / “SIMULATION” label visible before scenarios
[ ] No password / secret input fields
[ ] Results are private aggregates — not a public shame board
[ ] Debrief explains what “good” looks like (report quickly)
```

### Common misconceptions / what goes wrong

- **“Higher click rates mean better training.”** Click bait without reporting culture trains fear; report rate and time-to-report measure the job skill ([NIST SP 800-50](https://csrc.nist.gov/pubs/sp/800/50/final)).
- **“Fake login pages that POST passwords are OK if labeled in fine print.”** Capturing credentials is out of scope and unethical here — do not build harvesters.
- **“Public leaderboards of who failed motivate people.”** Humiliation destroys trust in IT and suppresses future reporting.
- **“Awareness replaces SPF/DKIM/DMARC and hold rules.”** Training is one layer; mail authentication and outbound hold still matter.

## Short intro

Phishing awareness tools train people to spot risky messages. Keep ethics first: informed participants, no real password capture, clear debrief. The graded kata scores quiz answers and computes a simple report-rate metric.


## Videos (verified)

1. **[Svelte Tutorial for Beginners](https://www.youtube.com/watch?v=3TVy6GdtNuQ)**  
   Why it helps: UI stack for the awareness quiz.

## Read these (verified)

1. [Svelte tutorial](https://svelte.dev/tutorial)
2. [NIST SP 800-50 — Awareness training concepts](https://csrc.nist.gov/pubs/sp/800/50/final) (awareness framing)
3. [APWG — Phishing activity](https://apwg.org/) (industry context)

## On the job

When designing training for people who handle held mail or admin consoles, honesty and metrics beat cinematic fake login pages.

## Next step

Continue with the assignment from the downloads on this page.
