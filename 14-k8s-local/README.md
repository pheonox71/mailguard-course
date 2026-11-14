# 14 — K8s local

**Language:** Kubernetes YAML. Est. 8-10h.

Deploy the MailGuard app shape to kind/minikube with probes and resource requests.

## Workflow

1. [`readings/k8s_local.md`](./readings/k8s_local.md)
2. Assignment → validate manifests with the kata
3. Build + `kind load docker-image mailguard-api:local`, then apply Deployment/Service (or Kustomize overlay)
4. [`readings/k8s_helm_deepen.md`](./readings/k8s_helm_deepen.md) → deepen assignment + quiz
5. Required quizzes

## Starter

- `starter/deployment.yaml` + `starter/service.yaml`
- `starter/kustomize/base` + `starter/kustomize/overlays/dev`
- `starter/chart/` (Helm) — `helm template` / `helm upgrade --install` after `kind load`

**Done when:** app healthy on kind/minikube; probes + requests present; overlay rendered; README notes GitOps as next.

## Trade-offs / harden next

- Local cluster ≠ production managed Kubernetes.
- NetworkPolicy / admission controls come in Module 16.
