# Kubernetes YAML primer

**Why this matters.** Compose is enough for a laptop story; **Kubernetes** is how many teams run the same containers with health probes, restarts, and resource requests. Module 14 puts MailGuard’s shape on kind/minikube before GitOps in Module 16. On the job, API/worker pods for mail and identity services live here — probes and requests are the difference between a quiet restart and a silent outage.

**How it works.** You declare desired state in **YAML** (Deployment, Service, etc.). The control plane reconciles actual pods toward that state. **kubectl** is the CLI; **kind**/**minikube** give you a local cluster without a cloud bill.

This primer has no assignment, quiz, or download pack.

---

## What Kubernetes YAML is

**Kubernetes** schedules containers across nodes. You rarely “SSH and start a process” — you apply manifests that describe replicas, probes, and networking.

## Why industry uses it

Self-healing workloads, consistent deploy APIs across clouds, and a clear path to policy/GitOps. Security teams care about resource limits, probes, and later NetworkPolicy/admission controls.

## Key concepts for Module 14

| Concept | Why you care |
|---------|----------------|
| Pod | Smallest runnable unit (usually one app container) |
| Deployment | Keeps N replicas; rolling updates |
| Service | Stable networking to pods |
| Probes / requests | Readiness and CPU/memory — Module 14 requires these |

## Install and run

1. [kubectl install](https://kubernetes.io/docs/tasks/tools/)
2. Cluster tools wait for Module 14: [kind](https://kind.sigs.k8s.io/docs/user/quick-start/) or [minikube](https://minikube.sigs.k8s.io/docs/start/)

**Check now:** `kubectl version --client`  
Why `--client` only: confirm the CLI is installed without needing a cluster API yet (Module 14 starts the cluster).

## Tiny hands-on example

```yaml
# Conceptual snippet — apply only inside Module 14's cluster
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mailguard-api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mailguard-api
  template:
    metadata:
      labels:
        app: mailguard-api
    spec:
      containers:
        - name: api
          image: example/mailguard-api:primer
          # Why: probes come next in Module 14 — without them traffic may hit a dead process
          ports:
            - containerPort: 8080
```

**How:** The Deployment names a Pod template; Kubernetes creates pods matching the selector — Module 14 adds probes and resource requests on top of this shape.

## Official docs

1. [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/)
2. [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
3. [kubectl cheat sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`14-k8s-local`).

This primer has **no** assignment, quiz, or download pack.
