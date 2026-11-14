# Quiz — TOTP enroll / recovery

1. **Why** verify a live TOTP code before marking enrollment complete?
2. **How** should recovery codes be stored at rest in production, and **why** not plaintext?
3. **Scenario:** An attacker phishes one recovery code. What property of `consume_recovery` limits the damage?
4. **Spot the bug / why:** Enrollment commits `secret = "JBSWY3DPEHPK3PXP"` into the course repo “for demos.”
5. Name one threat TOTP enroll does **not** solve that passkeys/WebAuthn address.
6. **Why** rate-limit verify attempts on the enroll/verify endpoints?
