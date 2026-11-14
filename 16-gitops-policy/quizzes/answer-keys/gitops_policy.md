# Quiz answer key — GitOps + policy

Use only after attempting the quiz questions.

1. Git (the declared manifests/config). Live-only state is unreviewable and unreproducible after emergency kubectl edits.
2. Pull: agent in-cluster fetches git and reconciles; push: CI/CD applies kubectl/helm from outside with pipeline credentials.
3. Stops unsafe desired state from becoming live; faster feedback on the PR that introduced the bug.
4. Kyverno, OPA/Gatekeeper, Conftest, etc. — validate YAML against rules (e.g. require readinessProbe) and fail the check/admission.
5. Cluster drifted from git; sync/reconcile missing or paused. Repair by syncing (or fixing git then syncing) — not by quietly leaving the cluster as source of truth.
6. Non-reproducible deploys; surprise supply-chain updates when the tag moves.
7. Admission catches apply paths that skip CI; digests name exact bits so verify/attest cannot be fooled by a retargeted tag.
