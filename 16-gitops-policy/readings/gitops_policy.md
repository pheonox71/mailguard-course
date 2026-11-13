# Reading — GitOps + policy

## Learning objectives

1. Diagram pull-based sync of manifests from git.
2. Fail CI on a policy violation (e.g. missing probes).
3. Keep claims proportional to what you automated.

**Why this matters.** Laptop `kubectl apply` does not scale and is hard to audit. Drift appears when someone “just fixed prod” outside git. Policy-as-code stops unsafe desired state (no probes, `:latest`, privileged pods) before it becomes the cluster’s reality. On the job, platform and security teams expect git as the source of truth for what runs mail/identity workloads — and CI gates that reject bad manifests.

**How it works.** GitOps treats git as the desired state; a sync agent applies it. In **pull** mode, an in-cluster agent (Argo CD-class) watches the repo and reconciles. In **push** mode, CI runs `kubectl`/`helm` from outside. Policy tools (Kyverno, OPA/Gatekeeper, Conftest) validate manifests in CI or at admission. This module reuses Module 14 checks and adds a “bad manifest” fixture that must fail.

```text
git commit (desired) → CI policy check → sync agent pulls → cluster matches git
                              ↓ fail
                         PR blocked (bad probes/tags/privileges)
```

Trade-off: pull GitOps needs an agent and RBAC in-cluster; push is simpler to start but credentials live in CI and drift is easier if people apply by hand.

## Short intro

GitOps + policy-as-code turn “hope the YAML is safe” into enforceable gates.

## Annotated checks

```bash
# Why fail CI before sync: stop bad desired-state from rolling out
conftest test fixtures/bad_deployment.yaml -p policy/
# or Kyverno/OPA equivalent — same idea: deny missing probes / privileged pods
```

Keep claims honest: if you only failed a fixture in CI, do not say “production GitOps” yet.

## Read these (verified)

1. [OpenGitOps Principles](https://opengitops.dev/)
2. [Argo CD — Understanding](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/)
3. [Kyverno — Writing policies](https://kyverno.io/docs/writing-policies/) (or Conftest/OPA)
4. [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

## Next step

Continue with the assignment from the downloads on this page.
