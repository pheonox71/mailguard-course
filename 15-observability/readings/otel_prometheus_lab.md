# Reading — OpenTelemetry + Prometheus lab

## Learning objectives

1. Expose at least one **Prometheus** metric from a tiny MailGuard-shaped API (Prometheus **3.x** path in compose).
2. Explain **how** scrape configs and `/metrics` cooperate, and when **native OTLP push** is a better fit than scrape.
3. Map golden signals (traffic, errors, latency, saturation) to hold-pipeline counters/histograms.

**Why this matters.** Logs alone do not tell you whether hold-enqueue latency is burning an error budget. Metrics give aggregatable SLI events; traces explain a single slow release. Without a local scrape path, “we will add observability later” stays aspirational. On the job, email/identity on-call expects named counters and latency histograms before paging on vibes.

**How it works.**

1. The app increments **counters** / observes **histograms** on the evaluate path.
2. It exposes Prometheus text format at **`GET /metrics`**.
3. **Prometheus 3.x** scrapes that path on an interval (see `starter/prometheus/prometheus.yml`). Compose maps `host.docker.internal` to the Docker host so Prometheus can scrape the published `:8000` port on Linux and Desktop alike.
4. Optionally, an **OpenTelemetry (OTel) collector** receives OTLP and re-exports metrics (compose service `otel-collector`) — useful when many languages speak OTLP but you still want Prometheus. The lab collector uses the **`debug`** exporter (the old `logging` exporter was removed).
5. **Compare push vs scrape:** scrape (`/metrics` ← Prometheus) is pull-based and fits long-lived services in this lab. **Native OTLP push** (app/SDK → collector or a Prometheus OTLP receiver) fits short-lived jobs and multi-language fleets already on OTel — but you must size the collector and still avoid high-cardinality labels.
6. You query Prometheus (`rate()`, histograms) and feed SLI/SLO math from Module 15’s SRE reading.

```text
evaluate() → counters/histograms → /metrics
                                      ↑ scrape (Prometheus 3.x)
                                 Prometheus ← (optional) OTel collector ← OTLP push
```

Trade-off: app-exposed `/metrics` is the simplest lab; OTLP push + collector adds a hop but standardizes export across languages. Prefer working scrapes over a perfect topology diagram.

### Worked example

```bash
cd 15-observability/starter
docker compose -f otel-compose.yml up --build

# Why hit evaluate: create time series before opening the UI
curl -s -X POST localhost:8000/evaluate -H 'content-type: application/json' \
  -d '{"subject":"urgent wire transfer"}'
curl -s localhost:8000/metrics | grep mailguard_holds_total

# Prometheus UI: http://localhost:9090
# Example query: rate(mailguard_holds_total[1m])
```

Metric names in [`../starter/app/main.py`](../starter/app/main.py):

| Metric | Golden signal |
|--------|----------------|
| `mailguard_holds_total{decision=...}` | Traffic (hold/allow volume) |
| `mailguard_evaluate_errors_total` | Errors |
| `mailguard_evaluate_seconds` | Latency |

Saturation (queue depth) belongs on the worker/SQS side — document it even if this lab stub does not emit it yet.

### Common misconceptions / what goes wrong

- **“Dashboards without scrape targets are observability.”** If Prometheus has no job for the API, charts are empty — verify `/metrics` and `up == 1` first.
- **“Traces replace metrics for SLOs.”** Traces explain individuals; SLOs need aggregatable good/bad events (usually metrics).
- **“Export every debug gauge.”** High-cardinality labels (`msg_id`, emails) explode series cost — label by decision/rule class, not message id.
- **“Put PII or tokens in metric labels.”** Never label with email addresses, subject lines, bearer tokens, session ids, or API keys — they leak into scrapes, remote-write sinks, and screenshots. Use coarse enums (`decision=hold|allow`) as in [`../starter/app/main.py`](../starter/app/main.py).
- **“OTel collector alone scrapes the app.”** In this compose file the collector receives OTLP; Prometheus still scrapes `/metrics` (and optionally the collector’s exporter). Wire an OTLP SDK when you leave the lab stub.

## Read these (verified)

1. [Prometheus — Getting started](https://prometheus.io/docs/prometheus/latest/getting_started/)
2. [OpenTelemetry — Collector](https://opentelemetry.io/docs/collector/)
3. [Prometheus Python client](https://prometheus.github.io/client_python/)
4. [Google SRE — Golden signals](https://sre.google/sre-book/monitoring-distributed-systems/)

## Next step

Run the compose lab, then continue with the [SRE basics assignment](../assignments/sre_basics.md) using real series from `/metrics`.
