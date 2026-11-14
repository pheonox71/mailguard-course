# Quiz — SRE basics

1. Expand **SLI**, **SLO**, and (optionally) **SLA**. For each, give one sentence on **how** it is used in decisions.
2. What is an **error budget** for, and **why** tie it to release freezes?
3. Name one bad vanity metric for MailGuard and **why** it fails as an SLI.
4. What does “blameless” mean in a postmortem, and **why** does blame-first culture hurt detection quality?
5. **Scenario:** Error budget is exhausted mid-week. What ship/freeze behavior is typical, and **why**?
6. **Spot the bug / why:** An alert fires on every single failed request with no burn-rate or window. What goes wrong for on-call?
7. **Why / how:** Why configure **two** burn-rate windows (fast page + slow ticket) instead of a single window on the SLO?
