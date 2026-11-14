# Quiz answer key — kind + Kustomize / Helm deepen

Use only after attempting the quiz questions.

1. **Base** holds shared manifests (Deployment/Service/probes/requests). An **overlay** patches env-specific fields (replicas, image tag, namespace). The overlay builds on the base so probes stay consistent while image tags differ.
2. Rendering catches missing values, bad patches, and YAML errors **before** the API server mutates cluster state — fail closed on the laptop, not mid-apply.
3. Docker builds the image into the host daemon; kind nodes have their own container runtime. `kind load docker-image` imports that image into the kind node(s) so `imagePullPolicy` can find `mailguard-api:local-dev` without a registry pull.
4. Kustomize: declarative patches, no template language — good when diffs are small. Helm: values + templates — good when many knobs or chart reuse. Prefer Kustomize for this module’s small API shape; Helm when packaging for others.
5. Dev pods can become `Running` with empty Service Endpoints (or flap) because readiness never gates traffic. Shared bases keep safety fields in one place so env forks cannot drop them.
6. Mutable `:latest` makes rollbacks and incident timelines guesswork — you cannot prove which bits ran. Pin digests or immutable tags even if replica count is correct.
7. You no longer operate the control plane (etcd, API server HA, upgrades). A kind demo does not prove multi-AZ control-plane SLA or provider-managed upgrades.
8. Overlays package env diffs; GitOps/policy add pull-based sync, drift detection, and admission controls so prod is not another laptop `kubectl apply`.
