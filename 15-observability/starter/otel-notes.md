# Local telemetry sketch

- Golden signals for hold pipeline: traffic (msgs/min), errors (hold failures), latency (evaluate p95), saturation (queue depth).
- Ship one structured log line: `{"event":"hold_applied","rule":"...","msg_id":"..."}`.
- Optional: Prometheus counter `mailguard_holds_total`.
