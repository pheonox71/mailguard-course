# Reading — K8s local

## Learning objectives

1. Run a Deployment + Service on kind or minikube.
2. Add liveness/readiness probes and CPU/memory requests.
3. Know what you have not automated yet (GitOps, policy).

**Why this matters.** A container that “runs on my laptop” is not enough for a mail/identity API: processes die, dependencies hang, and noisy neighbors steal memory. Without readiness probes, Services send traffic to pods that are not ready; without resource requests, the scheduler cannot place work fairly and a leak can OOM-kill neighbors. On the job, platform and security reviews ask for probes, requests/limits, and an honest gap list (no GitOps yet, no NetworkPolicy yet) before calling a chart “production-shaped.”

**How it works.** You create a local cluster (**kind** or **minikube**), apply YAML for a **Deployment** (Pod template + replica controller) and a **Service** (stable virtual IP/DNS to matching pods). The kubelet runs **probes**: readiness gates Service endpoints; liveness triggers restarts of stuck processes. **Requests** tell the scheduler how much CPU/memory the pod needs. You are not yet doing pull-based GitOps or admission policy — Module 16 covers that.

```text
kubectl apply → API server → controllers create Pods
Pods pass readiness → Endpoints populate → Service routes traffic
liveness fail → kubelet restarts container
```

## Short intro

Containers need orchestration for restarts, probes, and resource requests. Start local (kind/minikube), keep manifests small, and document gaps honestly.

## Annotated local loop

```bash
# Why kind/minikube: practice the API without a cloud bill
kind create cluster   # or: minikube start

# Why apply Deployment+Service together: pods without a Service are hard to reach stably
kubectl apply -f starter/deployment.yaml

# Why get pods: confirm Ready before claiming the demo works
kubectl get pods
```

In the Deployment, set readiness/liveness HTTP paths and `resources.requests` — why: Module 14’s checks expect them; production reviewers will too. Prefer a pinned image tag over `:latest` so restarts are reproducible.

## Read these (verified)

1. [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
2. [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
3. [kind — Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
4. [Resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

## On the job

Email gateways and identity sidecars often run as Deployments. Knowing **how** probes and requests behave under failure is more valuable than memorizing every kubectl flag.

## Next step

Continue with the assignment from the downloads on this page.
