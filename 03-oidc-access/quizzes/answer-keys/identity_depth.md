# Quiz answer key — identity depth

Use only after attempting the quiz questions.

1. Security Assertion Markup Language; OpenID Connect — SAML classically uses XML assertions.
2. Legacy apps, vendors without federation, cost/time to integrate SSO.
3. No — different mechanisms/purposes (device identity/posture vs user WebAuthn credential), though both can be cert/key based.
4. e.g. phishing unlock, malware on client, overshared vault folders, weak master password, poor rotation.

5. CSRF / login CSRF — attacker can bind the victim’s session to the attacker’s IdP login.

6. Use exact redirect URI matching (or strict path allow-list), not naive prefix matching.
