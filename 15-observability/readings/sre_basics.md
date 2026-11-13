# Reading — SRE basics (SLI / SLO / error budgets / postmortem)

## Learning objectives

1. Define **SLI**, **SLO**, and **error budget** and relate them to MailGuard’s hold pipeline.
2. Prefer user-visible indicators (e.g. successful release within N seconds) over vanity metrics.
3. Write a short **blameless postmortem** from telemetry.

**Why this matters.** Observability without objectives becomes dashboard tourism: lots of charts, no decision rule. When hold enqueue or release latency silently degrades, operators and users notice before vanity counters do. Site Reliability Engineering (**SRE**) popularized measuring reliability with Service Level Indicators (**SLI**s), targeting them with Service Level Objectives (**SLO**s), and spending **error budgets** when reality misses the target — then learning via postmortems. On the job, email/identity on-call uses those budgets to choose “ship features” vs “freeze and harden.”

**How it works.**

1. Pick user-visible **SLIs** (e.g. fraction of release API calls completing in &lt; 30s; hold-enqueue success rate).
2. Set an **SLO** over a window (e.g. 99% over 28 days).
3. The **error budget** is the allowed failure fraction (here ~1%). Burn it → pause risky launches; recover budget → resume feature work.
4. Emit signals (metrics/traces/logs via OpenTelemetry-class tooling) so you can prove burn and write a **blameless** postmortem (systems/process fixes, not blame).

```text
User journey → SLI events (good/bad) → SLO compliance → error budget left?
                                                      ↓ burned
                                            reliability work / freeze
```

Trade-off: tight SLOs create more freezes; loose SLOs hide user pain. Prefer fewer meaningful SLIs over dozens of vanity gauges.

## Short intro

SRE vocabulary turns telemetry into release policy — not just pretty graphs.

## Videos (verified)

1. **[SLIs, SLOs, SLAs, oh my! (class SRE implements DevOps)](https://www.youtube.com/watch?v=tEylFyxbDLE)** — Google Cloud Tech  
   Why it helps: canonical vocabulary with examples.

2. **[Risk and Error Budgets (class SRE implements DevOps)](https://www.youtube.com/watch?v=y2ILKr8kCJU)** — Google Cloud Tech  
   Why it helps: how error budgets drive release vs reliability trade-offs; pair with written postmortem culture chapter.

Prefer the Google SRE book chapters below if a video moves.

## Annotated practice

When you wire metrics later:

```text
# Why count good/bad release events — not “CPU looks fine”:
# decisions need user-visible success criteria
release_success{le="30s"} / release_attempts
```

Alert on **burn rate over a window**, not every single failure — why: avoid pager fatigue that trains people to ignore real incidents.

## Read these (verified)

1. [Google SRE Book — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — SLI/SLO/error budgets.
2. [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — blameless learning.
3. [OpenTelemetry docs — Concepts](https://opentelemetry.io/docs/concepts/) — signals you will emit in this module.
4. [Google — CRE life lessons / SLOs](https://cloud.google.com/blog/products/gcp/sre-fundamentals-slis-slas-and-slos) — short companion.

## Next step

Continue with the assignment from the downloads on this page.
