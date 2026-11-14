# Reading — GitOps + policy

## Learning objectives

1. Diagram pull-based sync of manifests from git.
2. Fail CI on a policy violation (e.g. missing probes).
3. Keep claims proportional to what you automated.

**Why this matters.** Laptop `kubectl apply` does not scale and is hard to audit. Drift appears when someone “just fixed prod” outside git. Policy-as-code stops unsafe desired state (no probes, `:latest`, privileged pods) before it becomes the cluster’s reality. On the job, platform and security teams expect git as the source of truth for what runs mail/identity workloads — and CI gates that reject bad manifests.

**How it works.**

1. Treat git as the **desired state** for Deployments/Services (and related objects).
2. In **pull** mode, an in-cluster agent (Argo CD-class) watches the repo and reconciles drift.
3. In **push** mode, CI runs `kubectl`/`helm` from outside — simpler start, credentials live in CI.
4. Policy tools (Kyverno, OPA/Gatekeeper, Conftest) validate manifests in CI or at admission.
5. This module reuses Module 14 checks and adds a “bad manifest” fixture that must fail — keep claims proportional to what you automated.

```text
git commit (desired) → CI policy check → sync agent pulls → cluster matches git
                              ↓ fail
                         PR blocked (bad probes/tags/privileges)
```

Trade-off: pull GitOps needs an agent and RBAC in-cluster; push is simpler to start but credentials live in CI and drift is easier if people apply by hand.

### Worked example

Fail CI before sync (Conftest-class; Kyverno/OPA equivalent works the same idea). Good shape mirrors [`../fixtures/good_deployment.yaml`](../fixtures/good_deployment.yaml) (probes + pinned tag + requests):

```bash
# Why fail CI before sync: stop bad desired-state from rolling out
# Policies live in this module's policy/ (Rego for Conftest + a Kyverno sketch)
conftest test fixtures/bad_deployment.yaml -p policy/
# Expected: FAIL — missing readinessProbe / :latest
conftest test fixtures/good_deployment.yaml -p policy/
# Expected: PASS
# Live CI gate (repo root): ../../.github/workflows/policy-check.yml
# Nested instructional copy (GitHub does not run it): .github/workflows/policy-check.yml
```

```text
# Sync flow after green CI
PR merge → git desired state updated → agent detects drift → apply → Ready pods
```

Keep claims honest: if you only failed a fixture in CI, do not say “production GitOps” yet.

### Common misconceptions / what goes wrong

- **“GitOps means nobody reviews YAML.”** Git is the source of truth *and* the review surface — policy + humans still gate merges.
- **“Fix prod with kubectl, commit later.”** That is drift; the next sync may overwrite your hotfix — revert/fix in git and let the agent reconcile.
- **“Passing sync equals safe cluster.”** Without policy, privileged pods and missing probes sync “successfully.”
- **“Push and pull are the same risk.”** Push stores deploy credentials in CI; pull needs careful in-cluster RBAC — pick deliberately ([OpenGitOps Principles](https://opengitops.dev/)).

## Short intro

GitOps treats git as the desired state; a sync agent applies it. Policy-as-code stops unsafe manifests before they roll out. This module reuses Module 14 checks and adds a “bad manifest” fixture that must fail. GitOps + policy-as-code turn “hope the YAML is safe” into enforceable gates.


## Videos (verified)

1. **[ArgoCD Tutorial for Beginners | GitOps CD for Kubernetes](https://www.youtube.com/watch?v=MeU5_k9ssrs)** — TechWorld with Nana  
   Why it helps: pull sync mental model.

## Read these (verified)

1. [OpenGitOps Principles](https://opengitops.dev/)
2. [Argo CD — Understanding](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/)
3. [Kyverno — Writing policies](https://kyverno.io/docs/writing-policies/) (or Conftest/OPA)
4. [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

## Next step

Continue with the assignment from the downloads on this page.
