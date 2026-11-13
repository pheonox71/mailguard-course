# Quiz — Basic auth client

1. Basic credentials are encoded with which scheme before Base64?
2. RFC 7617 example user `Aladdin` uses what password in the classic header example?
3. Scenario: server_unix=1000, client_unix=1040, max_skew=30 — is skew OK?
4. Spot-the-bug: `base64(username) + ":" + base64(password)` for the header payload. What is wrong?
5. Name one safer transport requirement when using Basic auth.
6. Why parse JSON with an explicit `token` presence check instead of `.get` silently defaulting?
