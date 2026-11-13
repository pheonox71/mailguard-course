# Reading — Email authentication & SMTP/TLS literacy

## Learning objectives

1. Explain Simple Mail Transfer Protocol (**SMTP**) as the store-and-forward *sending* protocol, and why Transport Layer Security (**TLS**) on SMTP (STARTTLS / implicit TLS) encrypts the hop but does **not** by itself prove the `From:` domain is legitimate.
2. Distinguish Sender Policy Framework (**SPF**), DomainKeys Identified Mail (**DKIM**), and Domain-based Message Authentication, Reporting and Conformance (**DMARC**) — what each checks and how they combine.
3. Read a DMARC DNS policy (`p=`, `rua=`) and say what hold/DLP rules **cannot** fix alone when attackers spoof lookalike mail.

## Short intro

MailGuard’s hold rules catch *outbound* mistakes (missend, policy). Attackers also **spoof inbound or lookalike domains**. SPF publishes which hosts may send for a domain (DNS TXT). DKIM adds a cryptographic signature over selected headers/body with a public key in DNS. DMARC tells receivers what to do when SPF/DKIM fail alignment with the visible `From:` domain, and where to send aggregate reports (`rua`).

![SPF, DKIM, and DMARC checks from sending MTA through receiving MTA with DNS-published controls](images/spf-dkim-dmarc.svg)

*Figure. SMTP+TLS protects the hop; **SPF** authorizes hosts, **DKIM** signs content, **DMARC** aligns results with the visible `From:` and sets `p=` policy. Notice hold/DLP and domain auth solve different problems (outbound mistakes vs inbound spoof). Original course diagram (CC0).*

**SMTP + TLS** literacy: encrypting the pipe (TLS) stops casual eavesdropping on that hop; it does not replace SPF/DKIM/DMARC. Domain authentication is how receivers decide “did this domain authorize this message?”

## Videos (verified)

1. **[SPF, DKIM and DMARC Protocols Explained](https://www.youtube.com/watch?v=2eR6996cQvY)** — PowerDMARC  
   Why it helps: end-to-end picture of the three DNS-published controls receivers combine.

2. **[Email Trust and Antispoofing: DKIM, SPF, and DMARC](https://www.youtube.com/watch?v=vDxorQtmkhw)** — Salesforce Support  
   Why it helps: operator-oriented setup narrative (`p=none` → stricter policies) without requiring their product.

3. **[Set up email authentication](https://www.youtube.com/watch?v=YdWgHAcD91E)** — Google Workspace  
   Why it helps: SPF/DKIM publish steps and where DMARC fits for modern receivers.

## Read these (verified)

1. [RFC 7208 — SPF](https://datatracker.ietf.org/doc/html/rfc7208) — skim abstract + mechanism overview.
2. [RFC 6376 — DKIM](https://datatracker.ietf.org/doc/html/rfc6376) — signature + public key in DNS.
3. [RFC 7489 — DMARC](https://datatracker.ietf.org/doc/html/rfc7489) — alignment, policies, reporting.
4. [DMARC.org overview](https://dmarc.org/overview/) — plain-language diagram.
5. [Cloudflare Learning — What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/) — concise comparison.
6. [Google — Email sender guidelines](https://support.google.com/a/answer/81126) — modern receiver expectations (SPF/DKIM/DMARC).
7. [Cloudflare Learning — What is SMTP?](https://www.cloudflare.com/learning/email-security/what-is-smtp/) — SMTP + why encryption ≠ authentication.

### Aggregate reports (Domain Protection–shaped literacy, generic)

Receivers email XML **aggregate reports** to `rua=` addresses summarizing pass/fail by source IP. Operators use them to find legitimate senders missing SPF/DKIM before flipping `p=reject`. This course does not require a live domain — parse policies in the kata and describe what a report would tell you on the worksheet.

## Self-check

After this reading: [`../quizzes/email_auth.md`](../quizzes/email_auth.md).
