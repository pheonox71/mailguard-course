# Assignment — Mail flow + aggregates

1. Why SPF fails after your gateway relays — and why DMARC might still pass (aligned DKIM). What would break if the gateway also stripped DKIM?
2. When do you need ARC — what intermediary failure mode is it answering?
3. Why distinguish journaling vs transport rules — one sentence each on *purpose*, not product clicks.
4. From an aggregate table, how do you spot a legit but unaligned ESP — what next step before tightening `p=`?
5. Why do bulk-sender mandates typically require SPF/DKIM/DMARC at minimum — what receiver problem are they reducing?
