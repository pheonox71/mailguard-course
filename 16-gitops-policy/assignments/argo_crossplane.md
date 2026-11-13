# Assignment — GitOps deepen

1. Pull vs push GitOps in one paragraph — emphasize **how** sync happens, not just slogans.
2. Draw app-of-apps with two child apps. **Why** split API vs worker instead of one mega-app?
3. Write a Conftest-style rule idea that blocks privileged pods. Explain **why** that rule belongs in CI/admission for mail/identity workloads.
4. What problem does Crossplane solve vs plain Terraform-only workflows? Name one trade-off.
5. **How** do you recover from a bad sync the GitOps way (git-first), and why not only `kubectl delete` by hand?
