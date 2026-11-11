# Self-check — Hold rules

Complete after [`../readings/hold_rules.md`](../readings/hold_rules.md). Attempt before opening the answer key.

1. Expand **DLP** and give the three policy actions this kata models.
2. What does **first-match-wins** mean for an ordered rule list?
3. Why does this kata avoid inventing a **DSL**?
4. Name one real-world product family that uses “inspect → match → act” on email (from the reading links).
5. **Scenario:** Rule 1 holds if subject contains `invoice`; Rule 2 allows domain `partner.example`. A message to `partner.example` with subject `Q4 invoice` — what happens under first-match-wins if Rule 1 is listed first?
6. What should you read as the **contract** before writing the stub implementation?

---

## Answer key (try first)

1. **Data Loss Prevention** — typically **allow**, **hold/suspend**, **reject/discard** (wording may vary by product).
2. Evaluate rules in order; apply the first matching rule’s action and stop.
3. Keep the engine interview-explainable and within a short challenge budget; no mini-language to maintain.
4. e.g. Microsoft Purview DLP or Google Workspace DLP (as linked in the reading).
5. **Hold** — Rule 1 matches first; Rule 2 never runs.
6. The pytest file for that kata (`tests/test_hold_rules.py`).
