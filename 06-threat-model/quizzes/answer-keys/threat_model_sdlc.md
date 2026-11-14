# Quiz answer key — threat model sdlc

Use only after attempting the quiz questions.

1. Spoofing (attacker acts as the operator via stolen session) and Elevation of privilege (release is a privileged action). Spoofing is about *who you appear to be*; Elevation is about *what that identity can do* — MFA/session binding mitigates spoofing; least privilege / step-up auth constrains elevation.
2. What are we working on? (scope/assets) · What can go wrong? (abuse stories) · What are we doing about it? (mitigations/gaps) · Did we do a good job? (verify, not assume).
3. SSDF/ASVS give *evidence-shaped* targets (practice + verification class + artifact you can show). SAMM can orient which practice to improve next, but finishing a student table is literacy — not an assessed maturity certification.
4. Information disclosure (and LINDDUN Data disclosure / Linking): prioritize least-privilege read of held bodies + retention/redaction of audits before long retention of full content.
5. Spoofing (fake/compromised operator without strong auth), Elevation (release powers), Repudiation if no immutable audit of who released what — MFA + audit close the first and third.
6. Distinct STRIDE categories tied to concrete elements/data flows — a generic catch-all cannot map to mitigations or prove coverage.
