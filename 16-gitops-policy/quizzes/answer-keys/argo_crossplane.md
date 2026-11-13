# Answer key — Argo / Crossplane

1. Pull — an in-cluster controller compares live state to git and syncs toward the desired revision.
2. Push — credentials and apply actions live outside the cluster; laptop tokens are weakly audited and easy to misuse.
3. Privilege escalation / host access risk after escape; block via policy (Pod Security / Kyverno deny).
4. A namespaced request for composed cloud infrastructure — reviewable Kubernetes API objects instead of ad-hoc console clicks.
5. Stop bad desired-state from rolling out; rollback after impact still burned error budget and risked data.
6. Kyverno or Conftest — run against changed manifests in CI and fail the PR on violations.
