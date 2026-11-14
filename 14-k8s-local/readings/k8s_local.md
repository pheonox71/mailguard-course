# Reading — K8s local

## Learning objectives

1. Run a Deployment + Service on kind or minikube with **PSS restricted-shaped** `securityContext`.
2. Split **readiness** (`/readyz`) and **liveness** (`/livez`) probes; set CPU/memory requests (and limits).
3. Apply a **default-deny NetworkPolicy** with DNS allow; know kindnet limits.
4. Prefer unique tags / digests (never `:latest`); avoid recommending retired **ingress-nginx**.

**Why this matters.** A container that “runs on my laptop” is not enough for a mail/identity API: processes die, dependencies hang, and noisy neighbors steal memory. Without readiness probes, Services send traffic to pods that are not ready; without resource requests, the scheduler cannot place work fairly and a leak can OOM-kill neighbors. Running as root with a writable rootfs fails Pod Security Standards **restricted**. On the job, platform and security reviews ask for probes, requests/limits, non-root, NetworkPolicy, and an honest gap list (GitOps/admission deepen in Module 16) before calling a chart “production-shaped.”

**How it works.**

1. Create a local cluster (**kind** or **minikube**).
2. Apply YAML for a **Deployment** (Pod template + replica controller) and a **Service** (stable virtual IP/DNS to matching pods).
3. Set **pod + container `securityContext`** toward PSS restricted: `runAsNonRoot`, numeric non-root UID, `allowPrivilegeEscalation: false`, drop all capabilities, `seccompProfile: RuntimeDefault`, `readOnlyRootFilesystem` (+ `emptyDir` for `/tmp`). This aligns with Module 16 Rego requiring `runAsNonRoot`.
4. The kubelet runs **split probes**: readiness (`/readyz`) gates Service endpoints; liveness (`/livez`) restarts a stuck process — do not conflate them on one path forever.
5. Set **requests** (and limits) so the scheduler knows how much CPU/memory the pod needs.
6. Apply **NetworkPolicy**: default-deny for the app pods, then allow same-namespace ingress to port 8000 and DNS egress to `kube-system` (UDP/TCP 53). **kindnet** (kind’s default CNI) may not fully enforce NetworkPolicy — install Calico (or similar) for a real policy lab, or document the gap.
7. Document remaining gaps — pull-based GitOps and admission policy deepen in Module 16. For HTTP ingress stretch, prefer **Gateway API** or another maintained controller — the community **ingress-nginx** controller’s best-effort support ended ~March 2026; do not recommend it for new work.

```text
kubectl apply → API server → controllers create Pods (non-root)
Pods pass /readyz → Endpoints populate → Service routes traffic
/livez fail → kubelet restarts container
NetworkPolicy: default-deny + DNS allow (+ kindnet caveat)
```

### Worked example

Probe + securityContext snippet aligned with [`../starter/deployment.yaml`](../starter/deployment.yaml):

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 10001
  seccompProfile: { type: RuntimeDefault }
containers:
  - name: api
    image: mailguard-api:local-dev   # Why unique tag: never :latest; prefer digests in registries
    securityContext:
      runAsNonRoot: true
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities: { drop: ["ALL"] }
    readinessProbe:
      httpGet: { path: /readyz, port: 8000 }
    livenessProbe:
      httpGet: { path: /livez, port: 8000 }
    resources:
      requests: { cpu: 50m, memory: 64Mi }
```

```bash
# Why kind/minikube: practice the API without a cloud bill
kind create cluster   # or: minikube start

# --- kind load step (required for local tags) ---
# Why: kind nodes do not see images that only exist in your host Docker daemon.
# Default build = katas only (no solutions/ layers). /readyz + /livez for probes.
#   docker build --target with-solutions -t mailguard-api:local-dev ../07-mailguard-api
docker build -t mailguard-api:local-dev ../07-mailguard-api
kind load docker-image mailguard-api:local-dev

kubectl apply -f starter/deployment.yaml
kubectl apply -f starter/service.yaml
kubectl apply -f starter/networkpolicy.yaml
# Or Kustomize overlay (includes NetworkPolicy in base):
# kubectl apply -k starter/kustomize/overlays/dev
kubectl get pods,svc,networkpolicy
```

### Common misconceptions / what goes wrong

- **“Liveness and readiness are interchangeable.”** Readiness removes traffic until ready; liveness **restarts** a stuck process. Using liveness for slow startups can crash-loop a healthy app — keep `/readyz` and `/livez` separate.
- **“No requests is fine on a laptop cluster.”** Without requests the scheduler cannot place fairly; a leak can OOM-kill neighbors — Module 14 checks expect requests.
- **“Pods Running means users are served.”** `Running` ≠ Ready; until readiness passes, the Service may have empty Endpoints.
- **“NetworkPolicy only exists in Module 16.”** Default-deny + DNS is taught **here**; Module 16 deepens admission/GitOps.
- **“kindnet enforces every NetworkPolicy.”** Often it does not — verify with a CNI that documents NetworkPolicy (e.g. Calico) or note the lab limitation.
- **“`:latest` or a mutable tag is fine.”** Prefer unique tags locally and **digests** in registries.
- **“Use ingress-nginx for stretch.”** Community ingress-nginx best-effort ended ~March 2026 — prefer **Gateway API** or another maintained ingress controller.
- **“`docker build` is enough for kind.”** Without `kind load docker-image` (or a registry the nodes can pull), pods stay `ImagePullBackOff` for local tags.

## Short intro

Containers need orchestration for restarts, probes, non-root securityContext, NetworkPolicy, and resource requests. Start local (kind/minikube), keep manifests small, and document gaps honestly.


## Videos (verified)

1. **[Kubernetes Course - Full Beginners Tutorial](https://www.youtube.com/watch?v=d6WC5n9G_sM)**  
   Why it helps: kind/minikube backdrop.

## Read these (verified)

1. [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
2. [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
3. [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — restricted profile shape
4. [NetworkPolicies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
5. [Gateway API](https://gateway-api.sigs.k8s.io/) — prefer over retired community ingress-nginx for stretch
6. [kind — Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
7. [Resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

## On the job

Email gateways and identity sidecars often run as Deployments. Knowing **how** probes, NetworkPolicy, and non-root contexts behave under failure is more valuable than memorizing every kubectl flag.

## Starter layout

| Path | Role |
|------|------|
| [`../starter/deployment.yaml`](../starter/deployment.yaml) | Deployment (split probes + PSS securityContext + requests) |
| [`../starter/service.yaml`](../starter/service.yaml) | ClusterIP Service for `mailguard-api` |
| [`../starter/networkpolicy.yaml`](../starter/networkpolicy.yaml) | Default-deny + DNS allow (kindnet caveat) |
| [`../starter/kustomize/`](../starter/kustomize/) | Base + `overlays/dev` for env patches |
| [`../starter/chart/`](../starter/chart/) | Helm chart (`values.yaml` + `values-dev.yaml`) |

## Next step

Continue with the [assignment](../assignments/k8s_local.md). For overlays/Helm deepen, see [`k8s_helm_deepen.md`](./k8s_helm_deepen.md).
