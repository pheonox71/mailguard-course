# Reading — Email authentication & SMTP/TLS literacy

## Learning objectives

1. Explain Simple Mail Transfer Protocol (**SMTP**) as the store-and-forward *sending* protocol, and why Transport Layer Security (**TLS**) on SMTP encrypts a hop but does **not** by itself prove the `From:` domain is legitimate. Server-to-server STARTTLS is **opportunistic**: an active attacker can strip it, and certificates are often not validated. **MTA-STS** (RFC 8461) or **DANE** (RFC 7672) make TLS required and authenticated for a receiving domain, and **TLS-RPT** (RFC 8460) reports failures. Implicit TLS (port 465) applies to client submission (RFC 8314), not MX-to-MX.
2. Distinguish Sender Policy Framework (**SPF**), DomainKeys Identified Mail (**DKIM**), and Domain-based Message Authentication, Reporting and Conformance (**DMARC**) — what each checks and how they combine. DMARC passes if **at least one** of SPF or DKIM passes **and** aligns with the visible `From:`.
3. Read a DMARC DNS policy (`p=`, `rua=`, and RFC 9989 tags such as `t=` / `np=` / `psd=`) and say what hold/DLP rules **cannot** fix alone when attackers spoof lookalike mail.

## Short intro

MailGuard’s hold rules catch *outbound* mistakes (missend, policy). Attackers also **spoof inbound or lookalike domains**. SPF publishes which hosts may send for the **envelope sender (MAIL FROM / Return-Path) or HELO domain** — it does **not** check the header `From:`. DKIM adds a cryptographic signature over selected headers/body with a public key in DNS. DMARC adds the **alignment** check that ties SPF or DKIM to the visible `From:` domain, tells receivers what to do on failure (`p=`), and where to send aggregate reports (`rua`).

![SPF, DKIM, and DMARC checks from sending MTA through receiving MTA with DNS-published controls](images/spf-dkim-dmarc.svg)

*Figure. SMTP+TLS protects the hop; **SPF** authorizes envelope hosts, **DKIM** signs content, **DMARC** aligns results with the visible `From:` and sets `p=` policy. Notice hold/DLP and domain auth solve different problems (outbound mistakes vs inbound spoof). Original course diagram (CC0).*

**SMTP + TLS** literacy: encrypting the pipe (TLS) stops casual eavesdropping on that hop; it does not replace SPF/DKIM/DMARC. Between MTAs, STARTTLS is opportunistic unless MTA-STS or DANE enforces authenticated TLS. Domain authentication is how receivers decide “did this domain authorize this message?”

## Videos (verified)

1. **[SPF, DKIM and DMARC Protocols Explained](https://www.youtube.com/watch?v=2eR6996cQvY)** — PowerDMARC  
   Why it helps: end-to-end picture of the three DNS-published controls receivers combine.

2. **[Email Trust and Antispoofing: DKIM, SPF, and DMARC](https://www.youtube.com/watch?v=ZFg691hXDzk)** — Salesforce Support  
   Why it helps: operator-oriented setup narrative (`p=none` → stricter policies) without requiring their product.

3. **[Set up email authentication](https://www.youtube.com/watch?v=YdWgHAcD91E)** — Google Workspace  
   Why it helps: SPF/DKIM publish steps and where DMARC fits for modern receivers.

## Read these (verified)

1. [RFC 7208 — SPF](https://datatracker.ietf.org/doc/html/rfc7208) — skim abstract + mechanism overview (MAIL FROM / HELO identity).
2. [RFC 6376 — DKIM](https://datatracker.ietf.org/doc/html/rfc6376) — signature + public key in DNS.
3. [RFC 9989 — DMARC](https://www.rfc-editor.org/info/rfc9989) — current protocol (Standards Track; obsoletes RFC 7489 and RFC 9091). Companion: [RFC 9990](https://www.rfc-editor.org/info/rfc9990) (aggregate reports), [RFC 9991](https://www.rfc-editor.org/info/rfc9991) (failure reports). RFC 9989 removes `pct`/`rf`/`ri` and adds `t` (test mode), `np`, and `psd`; the Public Suffix List is replaced by a DNS tree walk.
4. [DMARC.org overview](https://dmarc.org/overview/) — plain-language diagram.
5. [Cloudflare Learning — What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/) — concise comparison.
6. [Google — Email sender guidelines](https://support.google.com/a/answer/81126) — modern receiver expectations (SPF/DKIM/DMARC).
7. [Cloudflare Learning — What is SMTP?](https://www.cloudflare.com/learning/email-security/what-is-smtp/) — SMTP + why encryption ≠ authentication.
8. [RFC 8461 — MTA-STS](https://datatracker.ietf.org/doc/html/rfc8461) · [RFC 8460 — TLS-RPT](https://datatracker.ietf.org/doc/html/rfc8460) · [RFC 7672 — DANE for SMTP](https://datatracker.ietf.org/doc/html/rfc7672) — authenticated/required SMTP TLS and failure reporting.

### Aggregate reports (DMARC report literacy)

Receivers email XML **aggregate reports** to `rua=` addresses summarizing pass/fail by source IP. Operators use them to find legitimate senders missing SPF/DKIM (or alignment) before flipping `p=reject`. This course does not require a live domain — parse policies in the kata and describe what a report would tell you on the assignment.

## Next step

Continue with the assignment from the downloads on this page. The quiz is required after you attempt the assignment and tests.
