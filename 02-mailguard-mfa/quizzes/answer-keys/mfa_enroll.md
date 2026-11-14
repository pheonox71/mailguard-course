# Answer key — TOTP enroll / recovery

1. Confirms the user (or their app) actually holds the shared secret — otherwise you store a secret nobody can use, or the wrong one.
2. Store salted hashes (or equivalent); plaintext recovery codes in the DB are stealable in a dump and bypass MFA.
3. One-time consume — the stolen code cannot be replayed; force re-enrollment afterward.
4. Shared demo secrets get reused in real systems; treat fixtures as local-only and never commit live MFA material.
5. Phishing of prompted codes / real-time relay — origin-bound passkeys resist lookalike domains.
6. Online guessing of 6-digit codes is cheap without throttles and lockouts.
