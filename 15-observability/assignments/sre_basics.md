# Assignment — SRE basics for MailGuard

**Language / tooling:** Written SRE assignment (Markdown). When you wire metrics later, use the observability stack you document in Module 15 (Prometheus/OpenTelemetry-class tools) — not a random app framework.

## SLIs (pick 2–3)

For each row, explain **why** this SLI is user-visible (not vanity).

| SLI name | Measurement idea | Good events | Bad events | Why user-visible |
|----------|------------------|-------------|------------|------------------|
| Hold enqueue success | | | | |
| Release latency | | | | |
| Worker processing success | | | | |

## SLO + error budget

1. State one SLO (e.g. “99% of releases complete in &lt; 30s over 28 days”). **How** would you compute compliance from events?
2. What is the error budget in plain language?
3. What product/feature work would you pause if the budget burned — and **why** that work specifically?

## Postmortem (fill after a simulated failure)

- Summary:
- Impact (users/duration):
- Timeline:
- Root causes (technical + process) — **why** each mattered:
- What went well / poorly:
- Action items (owner + due — can be “student / next module”):

## Alert idea

One alert that pages a human vs one that should only ticket — justify **why** each severity (burn rate / user impact).
