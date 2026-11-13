# Reading — GitOps + policy

## Learning objectives

1. Diagram pull-based sync of manifests from git.
2. Fail CI on a policy violation (e.g. missing probes).
3. Keep claims proportional to what you automated.

## Short intro

GitOps treats git as the desired state; a sync agent applies it. Policy-as-code stops unsafe manifests before they roll out. This module reuses Module 14 checks and adds a “bad manifest” fixture that must fail.

## Read these (verified)

1. [OpenGitOps Principles](https://opengitops.dev/)
2. [Argo CD — Understanding](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/)
3. [Kyverno — Writing policies](https://kyverno.io/docs/writing-policies/) (or Conftest/OPA)
4. [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

## Next step

Continue with the assignment from the downloads on this page.
