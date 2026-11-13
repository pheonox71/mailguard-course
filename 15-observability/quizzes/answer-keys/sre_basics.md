# Quiz answer key — sre basics

Use only after attempting the quiz questions.

1. Service Level Indicator (measured good/bad events); Service Level Objective (target over a window); Service Level Agreement: an external contract with consequences (refunds or credits) if missed. It is usually **looser** than the internal SLO. Teams set the SLO tighter so they get warned before they breach the SLA. SLI feeds the math; SLO sets the target; SLA is the customer contract.
2. Quantifies allowed unreliability; when burned, pause risky feature work so reliability can recover — otherwise you keep shipping into an already failing user experience.
3. e.g. “lines of Go written” or raw request count without success criteria — neither reflects whether holds/releases succeeded for users.
4. Focus on systems/process fixes, not punishing individuals. Blame-first discourages honest timelines and under-reporting of near misses.
5. Pause risky feature launches; prioritize reliability work until budget recovers — protects users and preserves the SLO as a real policy.
6. Alert noise / fatigue; people ignore pages. Use SLO burn alerts over windows instead of one-off failures.
