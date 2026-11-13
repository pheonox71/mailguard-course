# Quiz answer key — ztna lite

Use only after attempting the quiz questions.

1. Once on the LAN, many internal services are reachable; ZTNA admits a specific app after identity/posture/context checks instead of the whole network.
2. Sessions, device posture, and risk change over time; one-shot login leaves stale trust until timeout.
3. The engine evaluates policy inputs (identity, context) to allow/deny/revoke; the enforcement point applies that decision on the path.
4. OIDC is application identity; ZTNA is about the access path / per-app admission model — related but not the same layer.

5. Per-app access bound to identity/device posture instead of broad network admission — reduces lateral reach if the contractor endpoint is compromised.

6. SSO is identity at the app; ZTNA also addresses the access path, continuous evaluation, and lateral movement.
