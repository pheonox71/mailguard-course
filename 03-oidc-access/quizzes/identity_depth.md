# Self-check — Identity depth

1. Expand **SAML** and **OIDC**. Which is XML-assertion heavy in classical enterprise SSO?
2. Why do non-SSO apps still exist in large orgs?
3. Is a device certificate the same as a passkey?
4. Name one password-manager risk that is not “AES is weak.”

---

## Answer key (try first)

1. Security Assertion Markup Language; OpenID Connect — SAML classically uses XML assertions.
2. Legacy apps, vendors without federation, cost/time to integrate SSO.
3. No — different mechanisms/purposes (device identity/posture vs user WebAuthn credential), though both can be cert/key based.
4. e.g. phishing unlock, malware on client, overshared vault folders, weak master password, poor rotation.
