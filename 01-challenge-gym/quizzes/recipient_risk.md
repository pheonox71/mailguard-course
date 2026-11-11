# Self-check — Recipient risk

Complete after [`../readings/recipient_risk.md`](../readings/recipient_risk.md). Attempt before opening the answer key.

1. What three recipient classes does this kata care about relative to an org domain?
2. Why can a **mixed** internal+external recipient set be a missend signal?
3. Expand **BEC** and contrast it briefly with an accidental missend.
4. Why normalize (e.g. lowercase domain) before comparing addresses?
5. What address parsing gap does this kata deliberately accept?
6. **Scenario:** Org domain `mailguard.example`. Recipients `Alex@MailGuard.Example` and `vendor@other.example` — mixed or not? Why?

---

## Answer key (try first)

1. **Internal**, **external**, and **invalid** (against the org domain / simple `local@domain` rules).
2. A message meant for colleagues may also leave the org — classic autocomplete / CC mistake that DLP holds can interrupt.
3. **Business Email Compromise** — attacker-driven fraud (spoof/hijack); missend is usually accidental wrong recipient. Same “verify the recipient” habit, different threat model.
4. Domains are case-insensitive in practice; naive string compare false-negatives “same” addresses.
5. Full **RFC 5322** / display-name parsing — only simple `local@domain` here.
6. **Mixed** — after normalization, one internal (`alex@mailguard.example`) and one external.
