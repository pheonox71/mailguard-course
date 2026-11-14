# Assignment — mTLS / ZTNA

1. Why prefer ZTNA-shaped access over classic VPN for an admin app — three bullets on lateral movement, identity binding, and blast radius.
2. Why do huge / infrequently distributed CRLs break security *and* ops — what happens to a revoked stolen cert in the gap?
3. Sketch nginx/Caddy mTLS directives you would try locally and annotate **why** verify must happen before trusting identity headers. For Caddy, explain why `mode require` is wrong when a `trust_pool` is configured and what `require_and_verify` adds. What does the untrusted-CA negative lab prove?
4. Which NIST SP covers ZTA implementation patterns in this reading, and why cite it instead of a product blog?
5. How do device certs relate to “admission” style access without naming vendors — what question does the cert answer at handshake time?
