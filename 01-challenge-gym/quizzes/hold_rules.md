# Quiz — Hold rules

Complete after [`../readings/hold_rules.md`](../readings/hold_rules.md). Complete the quiz, then check the separate answer key.

1. Why do email DLP engines offer hold/suspend and reject — not only allow/deny — and what fails for users if every match is a hard reject?
2. Why does **first-match-wins** on an ordered list make policy reviewable, and what goes wrong if two matching rules both “partially apply”?
3. Why does this kata avoid inventing a **DSL**?
4. Scenario: You reverse the order of two overlapping rules (hold on `invoice` vs allow partner domain). What changes for operators, and why is order part of the policy?
5. **Scenario:** Rule 1 holds if subject contains `invoice`; Rule 2 allows domain `partner.example`. A message to `partner.example` with subject `Q4 invoice` — what happens under first-match-wins if Rule 1 is listed first?
6. Why treat the pytest file as the **contract** before writing the stub — what fails if you invent behavior the tests never assert?
