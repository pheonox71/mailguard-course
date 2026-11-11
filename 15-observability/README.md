# 15 — Observability (+ SRE basics)

Metrics / logs / traces for MailGuard API + worker, extended with Site Reliability Engineering (**SRE**) basics: Service Level Indicator (**SLI**), Service Level Objective (**SLO**), error budgets, and a lightweight postmortem.

## What this teaches

- Golden signals for hold pipeline components
- Defining 2–3 SLIs and an SLO with an error budget story
- Writing one incident postmortem from telemetry (blameless tone)

## Start here

1. [`readings/sre_basics.md`](./readings/sre_basics.md)
2. Quiz → worksheet (SLIs + postmortem template)
3. Wire local metrics/logs/traces; narrate one failure

**Done when:** telemetry shows golden signals; SLI/SLO worksheet done; one failure diagnosed via telemetry; alert *idea* documented.
