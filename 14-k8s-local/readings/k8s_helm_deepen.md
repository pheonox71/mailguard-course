# Reading — kind + Helm/Kustomize deepen

## Learning objectives

1. Run the app on kind/minikube with probes and requests.
2. Prefer Helm or Kustomize overlays for env differences.
3. Name managed Kubernetes + GitOps as the production next step.

**Why this matters.** Copy-pasting raw YAML per environment (dev/stage/prod) drifts: one cluster gets probes, another does not. **Helm** charts and **Kustomize** overlays keep a shared base and patch only what must change (replicas, image tag, ingress host). Without that discipline, “works on kind” silently differs from “what we shipped.” On the job, platform teams expect env overlays — and then GitOps (Module 16) to sync them.

**How it works.**

1. Keep **base** manifests for Deployment/Service/probes shared across environments.
2. Express env diffs with **Helm** `values.yaml` (templates) or **Kustomize** overlays (patches).
3. **Render** first (`helm template` / `kustomize build`) so template errors fail before the cluster mutates.
4. Install into the local cluster and verify Ready pods.
5. Later: managed Kubernetes (EKS/GKE/AKS-class) replaces the DIY control plane; a pull agent (Argo CD-class) replaces laptop `kubectl apply`.

```text
base YAML → Helm values / Kustomize overlay → rendered manifests → cluster
```

Trade-off: raw YAML is easiest to read for one file; overlays scale when env diffs grow. Prefer overlays over forked copies.

### Worked example

Dev vs prod image tag via Helm values (conceptual):

```yaml
# values-dev.yaml
image:
  repository: mailguard-api
  tag: "local"          # Why pin: reproducible restarts on kind
replicaCount: 1
```

```bash
# Why render before install: catch template errors without mutating the cluster
helm template myapp ./chart -f values-dev.yaml | kubectl apply -f -

# Or Kustomize:
kubectl apply -k overlays/dev   # Why -k: build overlay then apply in one step
```

### Common misconceptions / what goes wrong

- **“Fork the whole YAML tree per env.”** Drift is inevitable — overlays/charts exist so probes and security fields stay in one base.
- **“Helm install without template is faster.”** Rendering first catches missing values and bad YAML before you break the cluster.
- **“Overlays replace GitOps.”** Env packaging is necessary but not sufficient; Module 16 adds sync + policy so prod is not another laptop apply.
- **“`:latest` in values is fine for prod.”** Mutable tags make rollbacks and incident timelines guesswork — pin digests or immutable tags.

## Read these (verified)

1. [Kubernetes probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
2. [Helm](https://helm.sh/docs/) / [Kustomize](https://kustomize.io/)
3. [kind](https://kind.sigs.k8s.io/)

## Next step

`helm_values_check` kata → quiz in module 16 for GitOps pull vs push.
