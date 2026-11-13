# Reading — kind + Helm/Kustomize deepen

## Learning objectives

1. Run the app on kind/minikube with probes and requests.
2. Prefer Helm or Kustomize overlays for env differences.
3. Name managed Kubernetes + GitOps as the production next step.

**Why this matters.** Copy-pasting raw YAML per environment (dev/stage/prod) drifts: one cluster gets probes, another does not. **Helm** charts and **Kustomize** overlays keep a shared base and patch only what must change (replicas, image tag, ingress host). Without that discipline, “works on kind” silently differs from “what we shipped.” On the job, platform teams expect env overlays — and then GitOps (Module 16) to sync them.

**How it works.** Base manifests describe Deployment/Service/probes. Kustomize `kustomization.yaml` lists resources + patches; Helm templates values (`values.yaml`) into charts. You render or install into the local cluster, still verifying Ready pods. Managed Kubernetes (EKS/GKE/AKS-class) later replaces the DIY control plane; a pull agent (Argo CD-class) replaces laptop `kubectl apply`.

```text
base YAML → Helm values / Kustomize overlay → rendered manifests → cluster
```

Trade-off: raw YAML is easiest to read for one file; overlays scale when env diffs grow. Prefer overlays over forked copies.

## Annotated commands

```bash
# Why render before install: catch template errors without mutating the cluster
helm template myapp ./chart -f values-dev.yaml | kubectl apply -f -

# Or Kustomize:
kubectl apply -k overlays/dev   # Why -k: build overlay then apply in one step
```

## Read these (verified)

1. [Kubernetes probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
2. [Helm](https://helm.sh/docs/) / [Kustomize](https://kustomize.io/)
3. [kind](https://kind.sigs.k8s.io/)

## Next step

`helm_values_check` kata → quiz in module 16 for GitOps pull vs push.
