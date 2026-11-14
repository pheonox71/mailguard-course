# Quiz — Email threats beyond auth

1. **Why** is BIMI not a substitute for malware scanning even when a logo appears?
2. **How** do MTA-STS and TLS-RPT work together when moving from `testing` to `enforce`?
3. **Why** is opportunistic TLS on port 25 insufficient against active downgrade?
4. **Scenario:** DMARC pass, but the PDF attachment macro-bombs a sandbox. What control layer caught what auth missed?
5. **Spot the bug / why:** Time-of-click rewriter serves the interstitial over HTTP and logs raw recipient emails in a public bucket.
6. Name one operational cost of **DANE** that MTA-STS tries to avoid, and **why** that matters for smaller teams.
7. **Why / how (OpenPGP / header protection):** Why cite OpenPGP **RFC 9580** beside S/MIME, and what problem do **RFC 9788 / RFC 9787** (header protection) solve that body-only encryption leaves open?
