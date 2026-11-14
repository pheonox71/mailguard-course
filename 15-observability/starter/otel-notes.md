# Local telemetry sketch

- Golden signals for hold pipeline: traffic (msgs/min), errors (hold failures), latency (evaluate p95), saturation (queue depth).
- Ship one structured log line: `{"event":"hold_applied","rule":"...","msg_id":"..."}`.
- Lab: `otel-compose.yml` + `app/` exposes `mailguard_holds_total` on `/metrics`.
- Reading: [`../readings/otel_prometheus_lab.md`](../readings/otel_prometheus_lab.md).
