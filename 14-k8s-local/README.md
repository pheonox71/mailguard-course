# 14 — K8s local

**Language:** Kubernetes YAML. Est. 8-10h.

Deploy the MailGuard app shape to kind/minikube with split probes, PSS restricted-shaped `securityContext`, resource requests, and a default-deny NetworkPolicy (+ DNS allow).

## Workflow

1. [`readings/k8s_local.md`](./readings/k8s_local.md)
2. Assignment → validate manifests with the kata
3. Build + `kind load docker-image mailguard-api:local-dev`, then apply Deployment/Service/NetworkPolicy (or Kustomize overlay)
4. [`readings/k8s_helm_deepen.md`](./readings/k8s_helm_deepen.md) → deepen assignment + quiz
5. Required quizzes

## Starter

- `starter/deployment.yaml` + `starter/service.yaml` + `starter/networkpolicy.yaml`
- `starter/kustomize/base` + `starter/kustomize/overlays/dev`
- `starter/chart/` (Helm) — `helm template` / `helm upgrade --install` after `kind load`

**Done when:** app healthy on kind/minikube; split probes + requests + `runAsNonRoot`; NetworkPolicy applied (kind ≥ 0.24 enforces; older kind needs Calico); overlay rendered; README notes GitOps/admission as Module 16 deepen.

## Trade-offs / harden next

- Local cluster ≠ production managed Kubernetes.
- **NetworkPolicy is taught here** (default-deny + DNS). kind **≥ 0.24** kindnet enforces NetworkPolicy; on kind **< 0.24**, install Calico (or similar) or upgrade kind.
- Admission / Conftest / Kyverno deepen in Module 16 (including `runAsNonRoot` Rego already aligned with these manifests).
- Prefer **Gateway API** (or another maintained ingress controller) for stretch HTTP routing — do **not** recommend the retired community **ingress-nginx** controller (best-effort ended ~March 2026).
