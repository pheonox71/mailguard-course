# Reading — SRE basics (SLI / SLO / error budgets / postmortem)

## Learning objectives

1. Define **SLI**, **SLO**, and **error budget** and relate them to MailGuard’s hold pipeline.
2. Prefer user-visible indicators (e.g. successful release within N seconds) over vanity metrics.
3. Write a short **blameless postmortem** from telemetry.

## Short intro

Observability without objectives becomes dashboard tourism. Site Reliability Engineering (**SRE**) popularized measuring reliability with Service Level Indicators (**SLI**s), targeting them with Service Level Objectives (**SLO**s), and spending **error budgets** when reality misses the target — then learning via postmortems.

## Videos (verified)

1. **[SRE Classroom — SLIs, SLOs, Error Budgets](https://www.youtube.com/watch?v=tEylFyxbDLE)** — Google Cloud Tech  
   Why it helps: canonical vocabulary with examples.

2. **[Risk and Error Budgets (class SRE implements DevOps)](https://www.youtube.com/watch?v=y2ILKr8kCJU)** — Google Cloud Tech  
   Why it helps: how error budgets drive release vs reliability trade-offs; pair with written postmortem culture chapter.

Prefer the Google SRE book chapters below if a video moves.

## Read these (verified)

1. [Google SRE Book — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — SLI/SLO/error budgets.
2. [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — blameless learning.
3. [OpenTelemetry docs — Concepts](https://opentelemetry.io/docs/concepts/) — signals you will emit in this module.
4. [Google — CRE life lessons / SLOs](https://cloud.google.com/blog/products/gcp/sre-fundamentals-slis-slas-and-slos) — short companion.

## Quiz (required)
[`../quizzes/sre_basics.md`](../quizzes/sre_basics.md)
