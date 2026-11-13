# Quiz answer key — email auth

Use only after attempting the quiz questions.

1. TLS encrypts a hop; it does not authorize the domain in `From:`. SPF/DKIM/DMARC let receivers decide whether the domain authorized the message (anti-spoof).
2. SPF never looked at header `From:`; without DMARC alignment, a pass for an unrelated envelope domain does not validate the address users see.
3. Reports reveal legitimate senders missing SPF/DKIM/alignment; skipping them causes false rejects and emergency rollbacks when `p=` tightens.
4. Hold/DLP address *your* outbound mistakes; DMARC addresses *spoofing of domains* at receivers — different directions and threat models.

5. Have the ESP **DKIM-sign with `d=yourdomain`** (aligned), and/or use a custom return-path/bounce domain under your domain so SPF aligns. Adding the ESP to SPF alone does not make DMARC pass if the ESP's envelope domain is its own. Then confirm in `rua` reports and step up `p=`.

6. The record is discarded — `v=DMARC1` must be the first tag.
