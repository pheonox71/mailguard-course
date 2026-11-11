# Reading — Hold rules (`hold_rules`)

## Short intro

Email DLP products sit between sender and recipient and apply **policy**: allow, temporarily hold (suspend), or reject/discard. Admins express rules; engines evaluate messages in a defined order. This kata is a **tiny** version of that idea — domain and substring predicates, **first match wins**, no DSL. The point is clear specs and concise Python, not a production rule language.

HENNGE’s email DLP team describes exactly this product shape: rules that allow, suspend, or discard to prevent costly mis-sends of sensitive information.

## Read these (verified)

### Product / domain context (HENNGE)

1. [Behind the Code: HENNGE Email DLP team](https://hennge.com/global/info/henka/interview/202408-meet-the-team-html/) — allow / suspend / discard; rules; missend prevention; Go workers / Vue / AWS stack notes for later folders.
2. [HENNGE One](https://hennge.com/global/service/one/) — DLP Edition: protection, detection, response for email and sharing.
3. [Secure Transfer JD](https://recruit.hennge.com/en/mid-career-ngh/senior-software-engineer-backend-infra-hennge-secure-transfer/) — backend/infra role on HENNGE One DLP Edition (years bars are separate).
4. [Demystifying HENNGE’s Hiring Process](https://hennge.com/global/info/henka/interview/202406-demystifying_hennges_hiring_process/) — challenge bar: short, elegant solutions.

### Engineering craft for this kata

5. [Python `dataclasses`](https://docs.python.org/3/library/dataclasses.html) — frozen message/rule records as used in the stub.
6. [pytest — Get Started](https://docs.pytest.org/en/stable/getting-started.html) — tests are the contract; run them often.

### Missend / privacy literacy (why “hold” exists)

7. [NZ Privacy Commissioner — prevent privacy breaches through email](https://www.privacy.org.nz/resources-and-learning/knowledge-base/view/516/) — wrong recipient is a top reported breach; check recipients; delays/reminders help.
8. [OVIC — tips to reduce data breaches when sending emails](https://ovic.vic.gov.au/privacy/resources-for-organisations/tips-to-reduce-data-breaches-when-sending-emails/) — human error, verify full addresses, delay-send patterns.

## Keep in mind

Production DLP adds attachment inspection, admin UX, queues, and richer matching. Your kata stays dumb on purpose — interview-explainable order and predicates first.
