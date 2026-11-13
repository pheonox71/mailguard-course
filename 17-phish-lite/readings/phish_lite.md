# Reading — Phish Lite

## Learning objectives

1. Build a small awareness quiz UI (Svelte preferred).
2. Label the experience as a learning simulation.
3. Prefer report-rate metrics over “gotcha” humiliation.

**Why this matters.** Phishing remains a top initial-access path into mail and identity systems. Awareness tools help — but badly designed simulations harvest passwords, shame clickers, or train people to distrust IT. Without clear learning labels and report-focused metrics, you optimize for “gotchas” instead of healthy reporting culture. On the job, security teams are judged on whether people **report** suspicious mail quickly, not only on raw click rates.

**How it works.** A small UI presents labeled training scenarios, scores answers, and computes metrics such as **report rate** and time-to-report. Ethics gates: informed participants, no real password capture, clear debrief. The graded kata scores quiz answers and computes a simple report-rate metric.

```text
Consent / disclosure → scenario quiz → optional “report” action
                    → score + report-rate (not public shame boards)
```

Trade-off: hyper-realistic login clones teach recognition but cross into credential-capture risk — this course forbids that pattern.

## Short intro

Keep ethics first: informed participants, no real password capture, clear debrief.

## Read these (verified)

1. [Svelte tutorial](https://svelte.dev/tutorial)
2. [NIST SP 800-50 — Awareness training concepts](https://csrc.nist.gov/pubs/sp/800/50/final) (awareness framing)
3. [APWG — Phishing activity](https://apwg.org/) (industry context)

## On the job

When designing training for people who handle held mail or admin consoles, honesty and metrics beat cinematic fake login pages.

## Next step

Continue with the assignment from the downloads on this page.
