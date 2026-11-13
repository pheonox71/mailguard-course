# Answer key — OWASP lab

1. BOLA / API1:2023-style broken object authz — login proves *a* user; object authz proves *this* user may act on *this* hold.
2. Supply-chain CVEs ship unnoticed — no signal in CI, no gate before deploy.
3. Whether your images/deps include the affected package/version — triage speed without manual archaeology.
4. No — local-only; run Juice Shop/crAPI on your machine/containers you own.
5. Proves learning transfers to the product thread (MailGuard mitigations), not tourism.
6. SSRF — allowlist destinations, block link-local/metadata IPs, no raw user URLs to cloud metadata; treat webhooks as untrusted input.
