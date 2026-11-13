# Reading — Mail flow + DMARC aggregate analytics

## Learning objectives

1. Place a cloud **email security gateway** relative to Microsoft 365 / Google Workspace (MX vs outbound smart-host).
2. Explain connectors/transport rules, journaling/archive, ARC (RFC 8617), and why SPF often fails after relay while DMARC may still pass via DKIM.
3. Parse DMARC aggregate reports (RFC 9990-shaped) and recommend the next `p=` step.
4. Know bulk-sender receiver mandates (Google/Yahoo 2024; Outlook.com high-volume expectations).

**Why this matters.** Real mail rarely goes “MUA → final MX” in one hop. Gateways, relays, and journaling rewrite paths so SPF breaks even for legitimate senders — and without aggregate analytics you either stay on `p=none` forever or flip to `p=reject` and break payroll/marketing. On the job, email-security engineers read RFC 9990-shaped reports, preserve DKIM (or ARC), and place MX vs outbound smart-hosts deliberately.

**How it works.** **Inbound:** MX points at the gateway (or workspace); mail is inspected then delivered. **Outbound:** workspace sends via a smart-host/gateway that may rewrite envelope data — SPF often fails after relay, while aligned **DKIM** can still make **DMARC** pass. **ARC** (RFC 8617) helps downstream receivers trust authentication results across intermediaries. Aggregate reports summarize pass/fail by source IP so you climb `none → quarantine → reject` with evidence. Bulk-sender mandates expect SPF/DKIM/DMARC at minimum.

## Read these (verified)

1. [RFC 8617 — ARC](https://www.rfc-editor.org/rfc/rfc8617)
2. [RFC 9990 — DMARC aggregate](https://www.rfc-editor.org/rfc/rfc9990) (and related DMARC reporting RFCs)
3. [Google bulk sender guidelines](https://support.google.com/a/answer/81126)
4. [Outlook.com postmaster](https://postmaster.outlook.com/)
5. [Exchange Online mail flow](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/mail-flow-best-practices)
6. [aiosmtpd](https://aiosmtpd.readthedocs.io/)

## Lab idea

Python **aiosmtpd** relay applying hold rules, then reinjecting allowed mail to MailHog/Mailpit.

Why local-only: an open relay on the public internet becomes abuse infrastructure; the lab proves flow mechanics without sending real mail.

## Next step

`mail_flow` + `dmarc_aggregate` katas → quiz.
