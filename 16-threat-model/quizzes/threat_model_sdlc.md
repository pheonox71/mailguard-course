# Self-check — Threat modeling / SSDLC

1. Expand **STRIDE** (list the six words).
2. What are Shostack’s “four questions” at a high level?
3. Expand **SAMM**. Is finishing this worksheet a SAMM certification?
4. Give one MailGuard example of **Information disclosure**.
5. **Scenario:** Operators can release holds without MFA. Which STRIDE categories light up first?

---

## Answer key (try first)

1. Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
2. What are we working on? What can go wrong? What are we doing about it? Did we do a good job?
3. **Software Assurance Maturity Model** — no; this is literacy/self-assessment only.
4. e.g. unauthorized read of held message bodies or overly verbose logs.
5. Spoofing (fake operator) and Elevation of privilege (release powers without strong auth); maybe Repudiation if no audit.
