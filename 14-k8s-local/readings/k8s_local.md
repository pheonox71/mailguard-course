# Reading — K8s local

## Learning objectives

1. Run a Deployment + Service on kind or minikube.
2. Add liveness/readiness probes and CPU/memory requests.
3. Know what you have not automated yet (GitOps, policy).

**Why this matters.** A container that “runs on my laptop” is not enough for a mail/identity API: processes die, dependencies hang, and noisy neighbors steal memory. Without readiness probes, Services send traffic to pods that are not ready; without resource requests, the scheduler cannot place work fairly and a leak can OOM-kill neighbors. On the job, platform and security reviews ask for probes, requests/limits, and an honest gap list (no GitOps yet, no NetworkPolicy yet) before calling a chart “production-shaped.”

**How it works.**

1. Create a local cluster (**kind** or **minikube**).
2. Apply YAML for a **Deployment** (Pod template + replica controller) and a **Service** (stable virtual IP/DNS to matching pods).
3. The kubelet runs **probes**: readiness gates Service endpoints; liveness triggers restarts of stuck processes.
4. Set **requests** so the scheduler knows how much CPU/memory the pod needs.
5. Document gaps honestly — you are not yet doing pull-based GitOps or admission policy (Module 16).

```text
kubectl apply → API server → controllers create Pods
Pods pass readiness → Endpoints populate → Service routes traffic
liveness fail → kubelet restarts container
```

### Worked example

Probe + requests snippet aligned with [`../starter/deployment.yaml`](../starter/deployment.yaml):

```yaml
containers:
  - name: api
    image: mailguard-api:local   # Why pin a tag: :latest restarts are not reproducible
    ports:
      - containerPort: 8000
    readinessProbe:
      httpGet: { path: /healthz, port: 8000 }
      initialDelaySeconds: 3
      periodSeconds: 5
    livenessProbe:
      httpGet: { path: /healthz, port: 8000 }
      initialDelaySeconds: 10
      periodSeconds: 10
    resources:
      requests: { cpu: 50m, memory: 64Mi }
```

```bash
# Why kind/minikube: practice the API without a cloud bill
kind create cluster   # or: minikube start

# --- kind load step (required for local tags) ---
# Why: kind nodes do not see images that only exist in your host Docker daemon.
# Build the Module 07 image, then import it into the kind cluster before apply.
docker build -t mailguard-api:local ../07-mailguard-api
kind load docker-image mailguard-api:local
# How it works: kind copies the image layers into each node’s container runtime
# so kubelet can start pods with image: mailguard-api:local (no registry pull).

kubectl apply -f starter/deployment.yaml
kubectl apply -f starter/service.yaml
# Or Kustomize overlay (shared base + env patches):
# kubectl apply -k starter/kustomize/overlays/dev
kubectl get pods,svc   # Why: confirm Ready + ClusterIP before claiming the demo works
```

### Common misconceptions / what goes wrong

- **“Liveness and readiness are interchangeable.”** Readiness removes traffic until ready; liveness **restarts** a stuck process. Using liveness for slow startups can crash-loop a healthy app.
- **“No requests is fine on a laptop cluster.”** Without requests the scheduler cannot place fairly; a leak can OOM-kill neighbors — Module 14 checks expect requests.
- **“Pods Running means users are served.”** `Running` ≠ Ready; until readiness passes, the Service may have empty Endpoints.
- **“This is production GitOps.”** Laptop `kubectl apply` is practice — sync agents and policy come in Module 16; keep claims proportional.
- **“`docker build` is enough for kind.”** Without `kind load docker-image` (or a registry the nodes can pull), pods stay `ImagePullBackOff` for `:local` tags.

## Short intro

Containers need orchestration for restarts, probes, and resource requests. Start local (kind/minikube), keep manifests small, and document gaps honestly.


## Videos (verified)

1. **[Kubernetes Course - Full Beginners Tutorial](https://www.youtube.com/watch?v=d6WC5n9G_sM)**  
   Why it helps: kind/minikube backdrop.

## Read these (verified)

1. [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
2. [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
3. [kind — Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
4. [Resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

## On the job

Email gateways and identity sidecars often run as Deployments. Knowing **how** probes and requests behave under failure is more valuable than memorizing every kubectl flag.

## Starter layout

| Path | Role |
|------|------|
| [`../starter/deployment.yaml`](../starter/deployment.yaml) | Standalone Deployment (probes + requests) |
| [`../starter/service.yaml`](../starter/service.yaml) | ClusterIP Service for `mailguard-api` |
| [`../starter/kustomize/`](../starter/kustomize/) | Base + `overlays/dev` for env patches |
| [`../starter/chart/`](../starter/chart/) | Helm chart (`values.yaml` + `values-dev.yaml`) |

## Next step

Continue with the [assignment](../assignments/k8s_local.md). For overlays/Helm deepen, see [`k8s_helm_deepen.md`](./k8s_helm_deepen.md).
