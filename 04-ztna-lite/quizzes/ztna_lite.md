# Self-check — ZTNA

1. Expand **ZTNA**. Expand **VPN**.
2. What problem does broad VPN admission create after credential theft?
3. In NIST ZTA language, what does a **policy engine** decide?
4. Does deploying OIDC on MailGuard admin equal a zero-trust network?

---

## Answer key (try first)

1. Zero Trust Network Access; Virtual Private Network.
2. Attacker may reach many internal services (lateral movement) once on the network.
3. Whether to allow/deny/revoke access based on identity, context, policy inputs.
4. No — that’s application identity; ZTNA is about the access path / per-app admission model.
