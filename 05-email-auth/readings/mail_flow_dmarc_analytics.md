# Reading — Mail flow + DMARC aggregate analytics

## Learning objectives

1. Place a cloud **email security gateway** relative to Microsoft 365 / Google Workspace (MX vs outbound smart-host).
2. Explain connectors/transport rules, journaling/archive, ARC (RFC 8617), and why SPF often fails after relay while DMARC may still pass via DKIM.
3. Parse DMARC aggregate reports (RFC 9990-shaped) and recommend the next `p=` step.
4. Know bulk-sender receiver mandates (Google/Yahoo 2024; Outlook.com high-volume expectations).

**Why this matters.** Real mail rarely goes “MUA → final MX” in one hop. Gateways, relays, and journaling rewrite paths so SPF breaks even for legitimate senders — and without aggregate analytics you either stay on `p=none` forever or flip to `p=reject` and break payroll/marketing. On the job, email-security engineers read RFC 9990-shaped reports, preserve DKIM (or ARC), and place MX vs outbound smart-hosts deliberately.

**How it works.**

1. **Inbound placement.** MX for the domain points at the security gateway (or directly at the workspace). Mail is inspected (spam, malware, policy), then delivered into the mailbox store.
2. **Outbound placement.** The workspace sends via a smart-host / gateway connector. Envelope data or the connecting IP may change after relay — SPF for the original MAIL FROM often fails at the final receiver.
3. **Authentication across intermediaries.** Aligned **DKIM** (signature survives if headers/body are preserved) can still make **DMARC** pass when SPF fails. **ARC** (RFC 8617) seals prior authentication results so downstream receivers can trust them across hops.
4. **Aggregate feedback.** Receivers send XML aggregate reports (RFC 9990-shaped) to `rua=` summarizing pass/fail by source IP. Operators climb `none → quarantine → reject` only when reports show legitimate senders are covered.
5. **Bulk-sender mandates.** High-volume senders are expected to publish SPF/DKIM/DMARC at minimum (see Google/Yahoo 2024 guidance and Outlook.com postmaster expectations).

```text
Inbound:  Internet → [gateway MX] → workspace
Outbound: workspace → smart-host/gateway → Internet MX
Auth:     SPF often fails after relay; aligned DKIM (± ARC) can still pass DMARC
```

### Worked example

A marketing ESP sends as `news@example.com` from `198.51.100.50`. Aggregate report row (shape simplified):

```text
<source_ip>198.51.100.50</source_ip>
<count>1200</count>
<policy_evaluated>
  <disposition>none</disposition>
  <dkim>pass</dkim>
  <spf>fail</spf>
</policy_evaluated>
<header_from>example.com</header_from>
```

SPF fails because the ESP IP is not in `example.com`’s SPF (or the envelope domain differs). DKIM `d=example.com` aligns with `From:`, so DMARC can still pass. Next `p=` step: keep `p=none` until every high-volume source shows aligned pass; then move to `quarantine`, then `reject`.

### Common misconceptions / what goes wrong

- **“SPF failed, so the mail is forged.”** After a legitimate relay, SPF often fails while aligned DKIM still authorizes the message for DMARC.
- **“Gateway in the path always breaks DMARC.”** Gateways break SPF when they change the connecting IP/envelope; they break DMARC only if they also invalidate or strip aligned DKIM (or you lack ARC where needed).
- **“Aggregate reports are optional fluff.”** Without them you guess which IPs are yours; flipping `p=reject` blind breaks real senders.
- **“ARC replaces SPF/DKIM.”** ARC conveys prior results across intermediaries; receivers still need a trustworthy ARC chain and underlying authentication story.

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
