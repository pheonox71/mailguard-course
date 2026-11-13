# Assignment — SRE basics for MailGuard

**Language / tooling:** Written SRE assignment (Markdown). When you wire metrics later, use the observability stack you document in Module 15 (Prometheus/OpenTelemetry-class tools) — not a random app framework.

## SLIs (pick 2–3)

| SLI name | Measurement idea | Good events | Bad events |
|----------|------------------|-------------|------------|
| Hold enqueue success | | | |
| Release latency | | | |
| Worker processing success | | | |

## SLO + error budget

1. State one SLO (e.g. “99% of releases complete in < 30s over 28 days”).
2. What is the error budget in plain language?
3. What product/feature work would you pause if the budget burned?

## Postmortem (fill after a simulated failure)

- Summary:
- Impact (users/duration):
- Timeline:
- Root causes (technical + process):
- What went well / poorly:
- Action items (owner + due — can be “student / next module”):

## Alert idea

One alert that pages a human vs one that should only ticket — justify.
