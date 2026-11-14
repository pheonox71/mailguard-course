# Quiz — K8s local

Complete after the module reading. Check the separate answer key only after you attempt every item.

1. Expand **Deployment** vs **Service** in one sentence each, and explain **how** they cooperate for a MailGuard API.
2. What does a readiness probe (`/readyz`) gate, and **why** is that different from liveness (`/livez`)?
3. **Why** are resource requests useful even on a laptop kind/minikube cluster?
4. Name one difference between kind and a managed cloud Kubernetes service, and **why** that matters for production claims.
5. **Scenario:** liveness probe path `/livez` always returns 500. What happens step by step, and **why**?
6. **Spot the bug / why:** container has no resource requests and a memory leak. What cluster symptom appears and how?
7. **Literacy:** Why set `runAsNonRoot` (PSS restricted shape), what does the starter NetworkPolicy deny/allow (and kindnet caveat), and why avoid recommending community ingress-nginx?
