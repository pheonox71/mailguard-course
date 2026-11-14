# Quiz answer key — identity depth

Use only after attempting the quiz questions.

1. Many classical enterprise apps only speak SAML assertions; OIDC-only plans leave those apps on passwords or brittle custom bridges.
2. Legacy apps, vendors without federation, cost/time — password managers (and break-glass processes) fill the gap until SSO arrives.
3. Device cert/posture answers “is this endpoint trusted enough?”; passkeys answer “is this user asserting at this RP?” — related keys, different problems.
4. e.g. phishing unlock, malware on client, overshared vault folders, weak master password, poor rotation — crypto strength does not stop those.

5. CSRF / login CSRF — attacker can bind the victim’s session to the attacker’s IdP login; `state` binds the callback to the browser that started the flow.

6. Use exact redirect URI matching (or strict path allow-list), not naive prefix matching — prefixes enable open redirect / code theft to sibling hosts.

7. Tokens in JS storage are exfiltratable via XSS; a BFF keeps tokens server-side and issues only an HTTP-only session cookie to the browser ([RFC 10017](https://www.rfc-editor.org/rfc/rfc10017)). Cookie sessions still need CSRF defenses (SameSite, anti-CSRF token, etc.) on state-changing requests — BFF does not remove CSRF, it changes where tokens live.
