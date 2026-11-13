# Quiz answer key — recipient risk

Use only after attempting the quiz questions.

1. **Internal**, **external**, and **invalid** (against the org domain / simple `local@domain` rules).
2. A message meant for colleagues may also leave the org — classic autocomplete / CC mistake that DLP holds can interrupt.
3. **Business Email Compromise** — attacker-driven fraud (spoof/hijack); missend is usually accidental wrong recipient. Same “verify the recipient” habit, different threat model.
4. Domains are case-insensitive in practice; naive string compare false-negatives “same” addresses.
5. Full **RFC 5322** / display-name parsing — only simple `local@domain` here.
6. **Mixed** — after normalization, one internal (`alex@mailguard.example`) and one external.
