# 15 — Observability (+ SRE basics)

Metrics / logs / traces for MailGuard API + worker, extended with Site Reliability Engineering (**SRE**) basics: Service Level Indicator (**SLI**), Service Level Objective (**SLO**), error budgets, and a lightweight postmortem.

## What this teaches

- Golden signals for hold pipeline components
- Defining 2–3 SLIs and an SLO with an error budget story
- Writing one incident postmortem from telemetry (blameless tone)

## Start here

1. [`readings/otel_prometheus_lab.md`](./readings/otel_prometheus_lab.md) — compose + `/metrics`
2. [`readings/sre_basics.md`](./readings/sre_basics.md)
3. Quiz → assignment (SLIs + postmortem template)
4. Wire local metrics/logs/traces; narrate one failure

**Done when:** telemetry shows golden signals; SLI/SLO assignment done; one failure diagnosed via telemetry; alert *idea* documented.

## Starter lab

```bash
cd 15-observability/starter
docker compose -f otel-compose.yml up --build
curl -s localhost:8000/metrics | head
```

## Coding lab (katas)

```bash
cd 15-observability && python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pytest -q
```
