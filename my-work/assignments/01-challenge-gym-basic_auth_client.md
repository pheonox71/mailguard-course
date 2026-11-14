# Assignment — Basic auth client

1. Why encode `user:pass` as one Base64 blob for the Authorization header — show the full header and explain what breaks if you Base64 each field separately.
2. Why is Basic auth over cleartext HTTP unsafe, and what fails on the job if a lab “works” only on `http://`?
3. Scenario: the JSON body is an array instead of an object. What should the client do and why (fail closed vs `.get` defaults)?
4. Pick a max_skew for TOTP + API skew — defend 30s vs 120s (usability vs accepting stale clocks / wider replay).
5. Why avoid committing passwords when publishing a gist — name two concrete practices and what each prevents.
