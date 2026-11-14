# Local telemetry sketch

- Golden signals for hold pipeline: traffic (msgs/min), errors (hold failures), latency (evaluate p95), saturation (queue depth).
- Ship one structured log line: `{"event":"hold_applied","rule":"...","msg_id":"..."}`.
- Lab: `otel-compose.yml` runs `app` (exposes `mailguard_holds_total`, `mailguard_evaluate_errors_total`, `mailguard_evaluate_seconds` on `/metrics`), Prometheus, and an optional OTel collector (`debug` + Prometheus exporters).
- Hit `POST /evaluate` before querying so series exist; reading: [`../readings/otel_prometheus_lab.md`](../readings/otel_prometheus_lab.md).
