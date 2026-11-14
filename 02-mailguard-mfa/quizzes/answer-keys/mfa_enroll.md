# Answer key — TOTP enroll / recovery

1. Confirms the user (or their app) actually holds the shared secret — otherwise you store a secret nobody can use, or the wrong one.
2. Store salted hashes (or equivalent); plaintext recovery codes in the DB are stealable in a dump and bypass MFA.
3. One-time consume — the stolen code cannot be replayed; force re-enrollment afterward.
4. After a successful validation, reject that step and any older one (`step <= last_used_step`) — equality-only leaves a skew-window hole where N−1 still works after N.
5. Shared demo secrets get reused in real systems; treat fixtures as local-only and never commit live MFA material.
6. Phishing of prompted codes / real-time relay — origin-bound passkeys resist lookalike domains.
7. Online guessing of 6-digit codes is cheap; lockout after N failures (NIST SP 800-63B-style throttle) stops brute force at the verify endpoint.
