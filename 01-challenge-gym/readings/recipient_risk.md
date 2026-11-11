# Reading — Recipient risk (`recipient_risk`)

## Learning objectives

By the end of this kata’s reading + worksheet + implementation, you should be able to:

1. Classify recipients as internal / external / invalid against an org domain after simple normalization.
2. Explain why **mixed** or **invalid** recipient sets are a missend / data-loss signal that can feed a hold rule.
3. Distinguish accidental missends from **business email compromise (BEC)** / phishing — same “verify the recipient” habit, different attacker model.

## Short intro

A common missend pattern: a message meant for **internal** colleagues also includes an **external** address (or a typo’d / invalid address). Classifying recipients against an org domain and flagging **mixed** or **invalid** sets is the seed of a hold decision. This kata uses a **simple** `local@domain` normalizer — enough to practice specs and string discipline, not full RFC 5322 parsing.

Pair this with the hold-rules kata: risk signals often feed “should we hold?” policies like those described for HENNGE email DLP.

## Videos (verified)

1. **[FBI Warns of Business Email Compromise Scams](https://www.youtube.com/watch?v=cBcjTJmxgh4)** — FBI – Federal Bureau of Investigation  
   Why it helps: official framing of BEC — lookalike addresses and payment requests; reinforces **verify the recipient** before trusting mail.

2. **[PSA: Business E-Mail Compromise Scams](https://www.youtube.com/watch?v=u3nAeVNSV24)** — FBI – Federal Bureau of Investigation  
   Why it helps: short dramatization of a rushed wire on a suspicious “boss” email — same urgency/missend pressure DLP holds interrupt.

3. **[Recognize and Report Phishing](https://www.youtube.com/watch?v=9pTW-F6V2N0)** — CISA  
   Why it helps: quick checklist for sender/address mismatch and odd urgency — literacy that pairs with programmatic recipient classification.

## Read these (verified)

### Email address handling

1. [OWASP Email Validation and Verification Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html) — normalize before compare; don’t invent brittle regex empires; domain lowercasing.
2. [RFC 5321 — SMTP](https://datatracker.ietf.org/doc/html/rfc5321) — skim address / mailbox concepts (optional depth after the kata is green).
3. [RFC 5322 — Internet Message Format](https://datatracker.ietf.org/doc/html/rfc5322) — full address syntax is richer than this kata; know the gap.

### Missend / DLP motivation

4. [Behind the Code: HENNGE Email DLP team](https://hennge.com/global/info/henka/interview/202408-meet-the-team-html/) — mis-sending sensitive info; rules that allow / suspend / discard.
5. [HENNGE One](https://hennge.com/global/service/one/) — DLP Edition product framing.
6. [NZ Privacy Commissioner — prevent privacy breaches through email](https://www.privacy.org.nz/resources-and-learning/knowledge-base/view/516/) — wrong recipient as a leading breach type.
7. [OVIC — tips to reduce data breaches when sending emails](https://ovic.vic.gov.au/privacy/resources-for-organisations/tips-to-reduce-data-breaches-when-sending-emails/) — verify full addresses; delay-send as a practical control.

### Career signal (honest)

8. [Secure Transfer JD](https://recruit.hennge.com/en/mid-career-ngh/senior-software-engineer-backend-infra-hennge-secure-transfer/) — DLP / secure transfer engineering bar (portfolio ≠ years).
9. [FAQs for Screening Process](https://recruit.hennge.com/faq-for-screening-process/) — challenge quality and stack familiarity matter in screening.

## Keep in mind

Real mail needs proper parsers, display-name handling, and Unicode/IDN awareness (see OWASP). Document that production gap in your trade-offs; don’t pretend the kata is RFC-complete.
