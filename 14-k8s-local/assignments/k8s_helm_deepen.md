# Assignment — kind + Kustomize / Helm deepen

Complete after [`../readings/k8s_helm_deepen.md`](../readings/k8s_helm_deepen.md). Answer the blank copy already under `my-work/assignments/` (do not edit this module file).

1. **Why** keep Deployment probes and resource requests in a shared **base**, then patch only replicas/image in an overlay? What drifts if you fork the whole YAML tree per environment?
2. Render the dev overlay without mutating the cluster. Paste (or summarize) the command you used and **how** `kubectl kustomize` / `kubectl apply -k` differs from raw `kubectl apply -f`.
3. Walk **how** a kind image load works step by step for `mailguard-api:local-dev`. Why does `docker build` alone not make the image visible inside the kind nodes?
4. **Scenario:** prod overlay accidentally sets `image: mailguard-api:latest`. What goes wrong at rollback time, and **why** pin digests or immutable tags instead?
5. Name two production capabilities this local overlay still lacks (e.g. GitOps sync, NetworkPolicy) and **why** claiming them after a kind demo would be dishonest.
6. Optional stretch: sketch a Helm `values-dev.yaml` vs `values-prod.yaml` for replicaCount + image.tag, and explain **how** `helm template` catches missing values before install.

## Done when

- Dev overlay renders; pods Ready on kind/minikube after image load
- Answers explain why/how (not only command names)
- Quiz [`../quizzes/14-k8s-local-k8s_helm_deepen.pdf`](../quizzes/14-k8s-local-k8s_helm_deepen.pdf) attempted before the answer key
