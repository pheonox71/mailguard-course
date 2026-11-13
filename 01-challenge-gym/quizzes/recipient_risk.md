# Quiz — Recipient risk

Complete after [`../readings/recipient_risk.md`](../readings/recipient_risk.md). Complete the quiz, then check the separate answer key.

1. Why classify recipients as internal / external / invalid before deciding hold — what fails if you only check “any external address exists”?
2. Why can a **mixed** internal+external recipient set be a missend signal even when every address is individually valid?
3. Why contrast accidental missend with **BEC** when both care about “verify the recipient”?
4. Why normalize (e.g. lowercase domain) before comparing addresses — what false outcome appears without it?
5. Why does this kata deliberately skip full RFC 5322 parsing — what trade-off is that?
6. **Scenario:** Org domain `mailguard.example`. Recipients `Alex@MailGuard.Example` and `vendor@other.example` — mixed or not? Why?
