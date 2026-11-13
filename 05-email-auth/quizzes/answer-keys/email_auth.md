# Quiz answer key — email auth

Use only after attempting the quiz questions.

1. **Simple Mail Transfer Protocol** — no; TLS encrypts the hop, authorization needs SPF/DKIM/DMARC alignment.
2. SPF: authorized senders in DNS; DKIM: signed content/headers; DMARC: policy + alignment + reporting for the visible From domain.
3. Aggregate pass/fail reports (usually XML) for operators.
4. Hold/DLP address *your* outbound mistakes; DMARC addresses *spoofing of domains* at receivers.
5. Update SPF (and/or DKIM) for the ESP, confirm reports clean up, then tighten policy.
