# Quiz — DMARC policy helper

Complete after the `dmarc_policy` assignment and kata. Check the separate answer key only after you attempt every item.

1. **Why** does a DMARC record need `v=DMARC1` first — what fails for receivers if the version tag is missing or not first?
2. **How** do `p=` and `sp=` differ, and when would you set them differently?
3. **Why** collect `rua=` aggregate reports before moving to `p=reject`?
4. **Scenario:** Your kata’s parser accepts `p=quarantine` but a record uses `pct=50`. What does `pct` change operationally, and why does a helper still need to surface it?
5. **Spot the bug:** A policy string is `p=reject; v=DMARC1; rua=mailto:dmarc@example.com`. What goes wrong and **why**?
6. **Why** is outbound hold/DLP complementary to DMARC rather than a substitute for `p=` enforcement?
