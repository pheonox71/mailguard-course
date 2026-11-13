# Reading — Mail flow + DMARC aggregate analytics

## Learning objectives

1. Place a cloud **email security gateway** relative to Microsoft 365 / Google Workspace (MX vs outbound smart-host).
2. Explain connectors/transport rules, journaling/archive, ARC (RFC 8617), and why SPF often fails after relay while DMARC may still pass via DKIM.
3. Parse DMARC aggregate reports (RFC 9990-shaped) and recommend the next `p=` step.
4. Know bulk-sender receiver mandates (Google/Yahoo 2024; Outlook.com high-volume expectations).

## Read these (verified)

1. [RFC 8617 — ARC](https://www.rfc-editor.org/rfc/rfc8617)
2. [RFC 9990 — DMARC aggregate](https://www.rfc-editor.org/rfc/rfc9990) (and related DMARC reporting RFCs)
3. [Google bulk sender guidelines](https://support.google.com/a/answer/81126)
4. [Outlook.com postmaster](https://postmaster.outlook.com/)
5. [Exchange Online mail flow](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/mail-flow-best-practices)
6. [aiosmtpd](https://aiosmtpd.readthedocs.io/)

## Lab idea

Python **aiosmtpd** relay applying hold rules, then reinjecting allowed mail to MailHog/Mailpit.

## Next step

`mail_flow` + `dmarc_aggregate` katas → quiz.
