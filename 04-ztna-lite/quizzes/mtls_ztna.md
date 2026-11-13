# Quiz — mTLS / ZTNA

1. Why does mTLS add client authentication beyond server TLS — what attack still works if only the server presents a cert?
2. Scenario: cert CN mismatches host — should `cn_matches` pass? Why check name binding at all?
3. Spot-the-bug: proxy sets client-cert-verified=SUCCESS without verifying the cert. What fails and why?
4. Why does NIST SP 1800-35 matter for this lab more than “buy a mesh” — what are you learning?
5. Why is OCSP/CRL operationally painful — what security property fails when revocation lags?
6. Why is a commercial mesh deploy *not* required to finish this module?
