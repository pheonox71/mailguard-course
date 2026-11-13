# Reading — Argo CD, policy-as-code, Crossplane intro

## Learning objectives

1. Explain **pull** GitOps (Argo CD app-of-apps) vs push pipelines.
2. Fail CI on bad manifests with Kyverno or Conftest.
3. Sketch a Crossplane claim for cloud resources (generic intro).

**Why this matters.** As services multiply (API, worker, admin UI), one flat folder of manifests becomes unreviewable. **App-of-apps** patterns let a root Application own child apps so each team’s repo/path stays clear. Without policy, privileged pods or missing probes still sync “successfully.” **Crossplane** (awareness-level here) brings cloud resources into the same Kubernetes control loop via claims — useful when identity/mail infra should be requested like any other API object. On the job, platform interviews often contrast pull vs push and ask how bad YAML is blocked.

**How it works.**

1. **Argo CD** (pull): controller compares live state to git; syncs when drifted.
2. **App-of-apps**: root Application manifests point at child Applications (API, worker, …).
3. **Policy-as-code**: Conftest/Kyverno reject privileged pods, `:latest`, missing probes in CI or admission.
4. **Crossplane claim**: a namespaced custom resource requests composed cloud infra (bucket/queue) without every app team learning raw cloud consoles — Terraform remains valid; Crossplane is another composition style.

```text
Root App → Child App (api) → Deployment/Service in git
         → Child App (worker)
CI: conftest/kyverno on PR  →  Argo sync only green desired state
```

Recovering from a bad sync: revert the git commit (desired state), let the agent reconcile — why git-first: the fix is reviewable and replayable, not a one-off kubectl bandage.

## Read these (verified)

1. [Argo CD docs](https://argo-cd.readthedocs.io/)
2. [Kyverno](https://kyverno.io/) / [Conftest](https://www.conftest.dev/)
3. [Crossplane docs](https://docs.crossplane.io/)

## Next step

`gitops_mode` kata + existing policy_check → quiz.
