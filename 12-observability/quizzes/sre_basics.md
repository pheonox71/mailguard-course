# Self-check — SRE basics

1. Expand **SLI**, **SLO**, and (optionally) **SLA**.
2. What is an **error budget** for?
3. Name one bad vanity metric for MailGuard.
4. What does “blameless” mean in a postmortem?

---

## Answer key (try first)

1. Service Level Indicator; Service Level Objective; Service Level Agreement (external contract — often stricter/legal).
2. Quantifies allowed unreliability; guides when to invest in reliability vs features.
3. e.g. “lines of Go written” or raw request count without success criteria.
4. Focus on systems/process fixes, not punishing individuals.
