# Reading — Hold rules (`hold_rules`)

## Learning objectives

By the end of this kata’s reading + worksheet + implementation, you should be able to:

1. Describe email Data Loss Prevention (DLP) as ordered policy: match conditions → action (allow / hold-suspend / reject-discard).
2. Implement **first-match-wins** evaluation over a small rule list without inventing a Domain-Specific Language (DSL).
3. Connect the toy engine to real product language (HENNGE DLP; Purview / Workspace DLP) so you can explain trade-offs in an interview.

## Short intro

Email DLP products sit between sender and recipient and apply **policy**: allow, temporarily hold (suspend), or reject/discard. Admins express rules; engines evaluate messages in a defined order. This kata is a **tiny** version of that idea — domain and substring predicates, **first match wins**, no DSL. The point is clear specs and concise Python, not a production rule language.

HENNGE’s email DLP team describes exactly this product shape: rules that allow, suspend, or discard to prevent costly mis-sends of sensitive information.

## Videos (verified)

1. **[What is Data Loss Prevention (DLP)?](https://www.youtube.com/watch?v=meWpZCmV0dg)** — Google Workspace  
   Why it helps: short official intro to DLP as **rules** that scan content and enforce an action when a rule matches.

2. **[Data Loss Prevention across endpoints, apps, & services | Microsoft Purview](https://www.youtube.com/watch?v=hvqq8L_0kgI)** — Microsoft Mechanics  
   Why it helps: shows how one DLP policy idea spans email and other channels — same “inspect → match → act” loop as this kata, at product scale.

3. **[Plan and design Data Loss Prevention (DLP) Policies | SC-401 | Episode 5](https://www.youtube.com/watch?v=Agp8I97XHlk)** — Microsoft Learn  
   Why it helps: policy design (what to monitor, where, conditions, actions) maps cleanly onto ordered hold/allow/reject rules.

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
