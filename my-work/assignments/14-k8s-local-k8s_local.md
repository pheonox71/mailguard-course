# Assignment — K8s local

1. Which probe should fail before sending traffic (readiness vs liveness)? Explain **how** each affects endpoints vs restarts.
2. **Why** set requests even on a laptop cluster? What goes wrong without them under a memory leak?
3. Paste `kubectl get pods` output (redact names if needed) after a healthy deploy. Annotate what “Ready” means **mechanically**.
4. List two production capabilities you have **not** automated yet (e.g. GitOps sync, NetworkPolicy) and **why** claiming them now would be dishonest.

## Done when

Manifest checks pass; cluster shows Ready pods; quiz done.
