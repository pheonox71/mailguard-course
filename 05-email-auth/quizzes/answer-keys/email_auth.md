# Quiz answer key — email auth

Use only after attempting the quiz questions.

1. **Simple Mail Transfer Protocol** — no; TLS encrypts the hop, authorization needs SPF/DKIM/DMARC alignment.
2. SPF: authorized senders in DNS; DKIM: signed content/headers; DMARC: policy + alignment + reporting for the visible From domain.
3. Aggregate pass/fail reports (usually XML) for operators.
4. Hold/DLP address *your* outbound mistakes; DMARC addresses *spoofing of domains* at receivers.
5. Have the ESP **DKIM-sign with `d=yourdomain`** (aligned), and/or use a custom return-path/bounce domain under your domain so SPF aligns. Adding the ESP to SPF alone does not make DMARC pass if the ESP's envelope domain is its own. Then confirm in `rua` reports and step up `p=`.
