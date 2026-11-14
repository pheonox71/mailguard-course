# Assignment — Email threats beyond auth

1. For **BIMI**, **MTA-STS**, **TLS-RPT**, and **DANE**, write one sentence each on **what problem it solves** that SPF/DKIM/DMARC alone do not.
2. Sketch an **MTA-STS** policy in `testing` then `enforce` — what evidence (TLS-RPT) do you want before enforce, and **why**?
3. Given a phishing sample **in a lab mailbox you own**, list five header fields you would inspect and **why** each matters (do not attack third-party systems).
4. Compare **attachment sandboxing** vs **block-by-type** — one benefit and one failure mode each.
5. When would you prefer **S/MIME/PGP** over **time-of-click URL rewriting**, and when is rewriting the better trade-off for a hold-queue product’s users?
6. **Spot the risk:** A gateway rewrites links to `https://click.example/…` but the landing page is HTTP and shows no SIMULATION/security notice. What goes wrong?
