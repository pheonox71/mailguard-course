# Quiz — Basic auth client

1. Why must credentials be Base64-encoded as a single `username:password` string rather than encoding each part separately?
2. Why is Base64 in the Basic header *not* a security control by itself?
3. Scenario: server_unix=1000, client_unix=1040, max_skew=30 — is skew OK? What fails operationally if you set max_skew too high?
4. Spot-the-bug: `base64(username) + ":" + base64(password)` for the header payload. What is wrong, and what breaks for the server?
5. Why require TLS (HTTPS) when sending Basic auth?
6. Why parse JSON with an explicit `token` presence check instead of `.get` silently defaulting?
