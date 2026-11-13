# Quiz — Mail flow + DMARC analytics

1. Why does MX placement control inbound delivery entry, and how does an outbound smart-host change SPF outcomes for the same org?
2. Scenario: SPF fail, DKIM pass aligned — can DMARC pass? Why does that matter after a gateway relay?
3. Spot-the-bug: gateway strips DKIM-Signature when rewriting bodies but keeps SPF pass assumptions. What fails downstream and why?
4. Why climb the policy ladder (`none → quarantine → reject`) using aggregate reports instead of jumping to reject?
5. Why does ARC exist — what authentication problem do intermediaries create that ARC aims to carry forward?
6. Why keep an aiosmtpd lab offline / local-only?
