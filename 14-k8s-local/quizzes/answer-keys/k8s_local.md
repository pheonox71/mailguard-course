# Quiz answer key — K8s local

Use only after attempting the quiz questions.

1. Deployment manages Pod replicas/rollouts; Service provides a stable network endpoint to Pods. The Service selects Deployment pods by labels so clients keep one DNS/IP while pods restart.
2. Readiness gates whether the Pod receives Service traffic; liveness decides whether to restart a stuck container. A pod can be alive but not ready (e.g. still warming).
3. Builds the habit the scheduler needs; without requests, placement is guesswork and noisy-neighbor effects still appear under load.
4. You operate the control plane locally vs provider-managed control plane/SLA — local demos do not prove HA, upgrades, or multi-AZ behavior.
5. Kubelet marks the probe failed and restarts the container repeatedly (CrashLoop-like churn) — because liveness failure means “kill and recreate,” not “stop routing only.”
6. Node pressure / OOMKills; other workloads may be evicted because the leak unbounded memory without requests/limits guidance.
