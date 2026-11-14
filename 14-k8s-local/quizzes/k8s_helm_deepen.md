# Quiz — kind + Kustomize / Helm deepen

Complete after the deepen reading. Check the separate answer key only after you attempt every item.

1. Expand **base** vs **overlay** in one sentence each, and explain **how** they cooperate for MailGuard’s API Deployment.
2. **Why** render with `helm template` / `kubectl kustomize` before applying to a cluster?
3. **How** does `kind load docker-image mailguard-api:local` change what the kubelet can pull, step by step?
4. Name one advantage of Kustomize overlays and one of Helm values for env diffs — and **when** you might prefer each.
5. **Scenario:** readiness probe is only in the prod overlay, not the base. Dev ships without readiness. What fails **how**, and **why** does that argue for shared bases?
6. **Spot the bug / why:** overlay patches `replicas: 3` but leaves `image: mailguard-api:latest`. What risk remains after a “successful” apply?
7. Managed Kubernetes (EKS/GKE/AKS-class) replaces which responsibility of kind, and **why** does that matter for production claims?
8. **Why** are overlays necessary but not sufficient for production — what does Module 16 (GitOps/policy) still add?
