# Quiz answer key — passkeys webauthn

Use only after attempting the quiz questions.

1. The user can type the live code into an attacker-controlled page that proxies login — possession of the authenticator does not bind the code to the real origin.
2. The authenticator signs a challenge scoped to the relying-party RP ID (registrable domain); a phishing origin should not receive a usable assertion.
3. Without a planned recovery path, lost-device lockouts force unsafe resets; email-only reset means mailbox takeover enrolls a new factor and locks out the user.
4. TOTP is shared-secret OTP literacy; WebAuthn is public-key, origin-bound ceremonies — different threat model and implementation surface.

5. Attacker with mailbox access can enroll a new factor and lock out the user.

6. Credentials may be scoped incorrectly / fail; spoofing or broken auth depending on misconfig — RP ID must be a valid registrable domain for the app.
