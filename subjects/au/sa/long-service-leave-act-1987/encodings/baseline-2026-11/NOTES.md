# Long Service Leave Act 1987 (SA) -- baseline encoding, the worker's seat

> **Warning.** The text encoded here is the South Australian register's current version of the Act (1.7.2017) and of
> the Long Service Leave Regulations 2017 (1.9.2017), as the register's **unauthorised** RTFs, fetched on 6 November
> 2026; the authorised versions are the PDFs on legislation.sa.gov.au. Unlike the South Australian baselines taken from
> the Open Australian Legal Corpus (collected 10 March 2025), these texts came from the official register, because its
> bot challenge had lifted. They may still be or go out of date: check legislation.sa.gov.au before relying on
> anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`salsl-core.l4`) holds every rule, with five regulative rules, each run by
`EVALTRACE` inside a function that takes only plain facts:

- `s 8(4)(b)`: PARTY the employer MUST pay the payment in lieu WITHIN 0 days of the termination (or of the personal
  representative's request) LEST BREACH;
- `s 10(6)`: PARTY the employer MUST give the Form 2 statement WITHIN the days to the day before the leave starts LEST
  BREACH (maximum penalty $200);
- `s 12(1)`: PARTY the employer MUST grant the leave or make the payment WITHIN the days stated in the inspector's
  notice LEST BREACH (s 12(6)(a), $5 000);
- `s 13(4)`: PARTY the applicant MUST apply to SAET WITHIN three years of the termination LEST BREACH ("an order cannot
  be made");
- `s 14(1)`: PARTY the worker SHANT engage in other employment in place of the employment WITHIN the days of the leave
  LEST BREACH ($1 000).

The seat layer (`salsl-seat.l4`) asks the questions and restates no rule. Dates sit in one small module
(`salsl-dates.l4`, built-in date functions only, no daydate, no `YMD`). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`.

**Why this Act.** It is one of the State long service leave Acts that the claims list names generically, beside
employment and discrimination claims: the Fair Work Act 2009 (Cth) leaves State long service leave in place for most
workers, and a worker's claim for unpaid leave, a payment on termination or an order from the South Australian
Employment Tribunal (SAET) runs under it. The Act is short (17 sections), so **the whole operative Act** is encoded;
only machinery and transitional provisions are left out (listed below).

Answers are named outcomes (enumerations, some carrying weeks, dollars, a date or a paragraph reference), not
`MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used and the 2026-11-04 and 2026-11-05 rulings are followed in substance
only: where the text says no in its own words (a "means" definition, "does not apply", "is not entitled ... if", "only
arises", an "if" or "where" condition, a period fixed in its own words, a closed list such as s 8(2)) the outcome begins
"no"; where a provision's own scope does not reach the case and the Act says nothing more (s 4(1), s 6(1) for a break
the worker brought about, s 13(2) for someone it does not name, s 14(1) outside the leave) the outcome says the
provision "does not reach this" (rule (c) of the 2026-11-05 ruling on periods, "where" and scope limits). Judgments the
Act leaves to SAET or an inspector are inputs. No pipeline, no coverage table, no independent test pass, no human
gate. **Not for public use as advice.**

This is the first encoding of the Act; nothing existing was touched. No requirement ledger exists for South Australia,
so no ledger line is opened or closed.

## Edition

- **Act:** Long Service Leave Act 1987 (SA), No 73 of 1987, version 1.7.2017 (last amended by the Statutes Amendment
  (South Australian Employment Tribunal) Act 2016), the register's current version on 6 November 2026, deposited at
  `../../registers/source-bundle/long-service-leave-act-1987.txt`.
- **Regulations:** Long Service Leave Regulations 2017, version 1.9.2017, deposited at
  `subjects/au/sa/long-service-leave-regulations-2017/registers/source-bundle/`. They set no number the Act uses; they
  prescribe the forms: reg 4(1), (2) and Form 1 (the record), reg 4(3) and Form 2 (the statement before leave, s 10(6)),
  reg 4(4) and Form 3 (the statement on cashing out, s 10(7)). They are named in the answers. The stable `l4` cannot
  IMPORT across subjects, so nothing is imported.
- The 2015 amending Act's transitional clause applies the s 3(4) disregarding rule to leave taken or paid on or after
  19 November 2015, including for absences before then; every case here is after that day.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `salsl-dates.l4` | 0 | 0 | 0 | 0 |
| `salsl-core.l4` | 0 | 0 | 0 | 0 |
| `salsl-seat.l4` | 0 | 0 | 0 | 0 |
| `salsl-cases.l4` | 0 | 0 | 171 | 171 |

Negative control: on a scratch copy, with the s 6(1)(i) window changed from two months to three and the s 7(3) notice
from 60 days to 59, the cases failed exactly the 8 predicted assertions (2 for s 6(1)(i), 6 for s 7(3)); the scratch
copy was discarded.

Every expected value was worked by hand from the text, with day counts written beside the date cases. Edges: 10 years
and 9 (and 9.99); 7 years and 6 (and 6.9); the anniversary and the day before, from 1 March and from 29 February;
two months from 31 December (to 28 February) and from 15 June, and the day after; 12 months from 29 February; 60 days
before 1 March in 2027 and in the leap year 2028; 91 days of leave across February in both; the day before leave and
its first day (s 10(6)); the leave's last day and the day after (s 14(1)); the day of termination and the day after,
and the day of a personal representative's request (s 8(4)(b)); 13 and 14 days, review on the 14th and 15th day
(s 12); three years from 15 March and from 29 February, and the day after (ss 10(2)(c), 13(4), 15(2)); s 5(6) using up
the entitlement exactly; a zero divisor in s 3(2).

## Seat

**The worker (required)** (`salsl-seat.l4`, 23 questions): the person employed under a contract of service who has
earned, or is earning, long service leave; for the questions a death raises (s 5(5), s 8(4)(b), s 13(2)(b)), the
worker's **personal representative**, asking on the worker's behalf. Every question is one that person would ask:
"Does the Act cover me?", "Does my service accrue under the Act?", "Did this break keep my service continuous?", "Does
this other period count as my service?", "How many completed years of service do I have?", "Am I entitled to long
service leave?", "Can I cash out my long service leave?", "What is my ordinary weekly rate of pay?", "How much should I
be paid for my leave?", "Is the way I am paid for my leave allowed?", "What more am I owed after a change in my rate?",
"Did I get enough notice of my leave?", "What is the last day of my leave?", "Did I get my leave statement in time?",
"May I work another job while on leave?", "What am I owed when my service ends?", "Was my payment on termination on
time?", "How much can my employer deduct for leave taken in advance?", "Can I see my long service leave records?",
"Can I apply to SAET for my leave or payment?", "Will SAET accept my account without records?", "By when must my
employer comply with the inspector?", "What is the fine and the time to prosecute?". Provisions addressed to the
employer, an inspector or SAET are encoded as what they mean for the worker: a payment due, a statement owed by a day,
an order that may be made, a penalty and a last day to prosecute.

No seat for the employer (an employer seat would be welcome as a second layer: ss 5, 7(6), 8, 10, 12(2), (3), 14(2)
give the employer duties and rights), and none for SAET or an inspector.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulations 2017 are named where they
  prescribe the forms of the record and statements (they set no number). The Fair Work Act 2009 (Cth), the Return to
  Work Act 2014, the Corporations Act 2001 and the Fair Work Act 1994 (SA) are named, not encoded; what they decide is
  asked as a fact.
- **The actors the text names.** Followed: the worker, the employer, the personal representative, the registered
  association, the inspector, SAET, the complainant in a prosecution.
- **Judgments answered conditionally.** Followed: SAET's order "to the contrary" (s 6(1)(a)), whether a break was
  brought about "in an attempt to avoid an obligation" (s 6(1)(b)), "serious and wilful misconduct" and "unlawfully
  terminated" (s 5(4)), "in place of the employment" (s 14(1)), whether SAET "considers that in fairness to the worker
  it should" (s 13(3)), "proper records" (s 13(3)) and the "fair and reasonable monetary value" of accommodation (s
  3(2)(c)) are inputs. "As soon as practicable (taking into consideration the needs of the employer's business)" (s
  7(1)) is not decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "worker" and "service" (s 3(1)), "related"
  employers (s 3(3)), the "ordinary weekly rate of pay" (s 3(2), (4)), "the relevant date" (by the input's wording),
  "individual agreement" (as the condition of s 5(1a)). Asked: "contract of service", "fair work instrument",
  "corresponding law", "related corporations", "work injury", "registered association".
- **One case:** one worker's service with one employer (and the employers related to it).
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** see Scope.

## Scope

**In:** s 3(1) (agreement, award, corresponding law, individual agreement, long service leave entitlement, related
corporations, the relevant date, service, worker), s 3(2), (3), (4); s 4; s 5(1)-(7); s 6(1)-(4); s 7(3), (4)(c), (d),
(6), (7); s 8(1)-(4); s 9(3), (5) (in the coverage answer); s 10(1), (2a), (4) (penalties only), s 10(2)(c), (5), (6),
(7); s 11(3) (penalty only); s 12(1)-(4), (6), (7); s 13(1)-(4); s 14(1), (2) (penalty); s 15; s 16; Regulations reg 4
and Forms 2 and 3 (named).

**Out, and why:**

- s 1 (short title), s 17 (regulations), the Regulations' regs 1-3 and Schedule 2: machinery.
- s 7(1), (2), (4)(a), (b): hortatory ("should be granted ... as soon as practicable", "should be taken in one
  continuous period") and permissive agreements; named in finding 1, not encoded as questions.
- s 9(1), (2), (4), (6): SAET's power to make and revoke exemption determinations; an official's power. Whether a
  determination applies is asked as a fact.
- s 10(1) (what the record holds), (2)(a), (b), (3), (4): the employer's record-keeping duties; their penalties are in
  the offence question. Form 1 of the Regulations is named only.
- s 11(1), (2), (4): an inspector's powers and the privilege against self-incrimination; a witness's or employer's
  seat would take them.
- s 12(2)-(4) are encoded only as they bear on the worker (suspension of the notice).
- Schedule cl 2 (transitional provisions for service before 1 January 1988, the 1967 Act and its exemptions) and the
  2016 amending Act's s 118 (transfer to SAET): of historic reach only. Cl 2(1) (earlier service counts if it continued
  after 1 January 1988) is taken as given.

## Forks (the text does not say; one reading taken)

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 6(1)(i), 6(3), 10(2)(c), 13(4), 15(2) "two months", "12 months", "three years" -- `plus months`,
  `plus years` -- the same day of the month that many months later (the day itself not counted), or that month's last
  day where shorter (31 December + 2 months = 28 February; 29 February 2024 + 3 years = 28 February 2027) -- the next
  day (1 March), or periods of 61, 365 or 1,095 days. Asserted.
- **F2** s 5(7) "completed years of service" -- `the completed years from` -- both the first and the last day count,
  so a year completes at the end of the day before the anniversary; from 29 February the anniversary in a common year is
  1 March; days not counted (s 6(2)) move the first day later, days added (s 6(3), (4)) earlier -- the anniversary day
  itself as the end of the year; 365-day years. Asserted.
- **F3** s 4(1) -- `the s 4 answer for` -- service outside the three paragraphs is "not reached" -- a flat no (the
  list is not closed with "only").
- **F4** s 6(1)(i) "re-employed by the employer within two months" -- `the s 6 answer for` -- from the first day of
  the break; outside it the answer is no (a "where" condition, rule (b) of the 2026-11-05 ruling) -- from the last day
  worked; or "not reached". Asserted.
- **F5** s 6(1)(d), (f) -- `the s 6 answer for` -- an absence through illness or injury is (d) and counts in full, even
  if it is also leave (paid or unpaid sick leave) -- (f), so that s 6(2) leaves it out of the count. The person chooses
  the paragraph; the reading is in the `@desc`.
- **F6** s 5(2), (3) with s 5(6) -- `the s 5 termination answer for`, `the s 5(1) answer for` -- weeks owed are 1.3 a
  completed year less weeks taken or paid, never below 0 -- the s 5(3) payment without deduction (leaving s 7(6) to do
  all the work). Asserted, with finding 5.
- **F7** s 3(2)(a), (b), (4) "12 months", "three years" -- `the s 3(2) rate for` -- the person states the weeks counted
  (about 52 or 156 after disregarding weeks) and the earnings or hours in them -- the encoding counting the weeks from
  dates (52 or 52.14; 156 or 156.43).
- **F8** s 7(3) "at least 60 days notice of the date from which leave is to be taken" -- `the s 7(3) answer for notice
  on` -- notice on a day counts if the leave starts 60 or more days later (1 March 2027 needs notice by 31 December
  2026) -- 60 clear days (by 30 December). Asserted.
- **F9** s 8(3), (3a)(b) "reflected", "reflects the variation" -- `the s 8(3) answer for` -- the change in the weekly
  rate times the weeks of leave after it; for s 8(3) a fall is reflected too (a negative difference) -- only rises
  reflected. Asserted.
- **F10** s 8(4)(b) "immediately on the termination", "on request" -- the s 8(4)(b) rule -- on the day of the
  termination (or of the request): WITHIN 0 -- within a reasonable time, or the next pay day. Asserted.
- **F11** s 12(1) "within a period (not being less than 14 days) stated in the notice" -- the s 12(1) rule -- counted
  from the day the employer received the notice -- from the day of the notice.
- **F12** s 10(5) "his or her employer" -- `the s 10 records answer for` -- a former worker is told the records must be
  kept and that the Act does not say whether the right to inspect survives -- the right reaches a former employer for
  the three years of s 10(2)(c).
- **F13** s 12(3) "must be made within 14 days" -- `the s 12 answer for a notice received on` -- an application for
  review made after the 14th day does not suspend the notice under s 12(4) -- any application suspends it until SAET
  dismisses it. Asserted.
- **F14** s 6(1) for a break the worker brought about (a resignation, then re-employment) -- `the s 6 answer for` --
  "not reached; check another paragraph" -- a flat no, since s 3(1) requires "continuous" service. Asserted.
- **F15** the deadline helper -- `the deadline answer for` -- an act done before the clock starts (a payment the day
  before the termination) is taken as done on day 0, in time; a statement given on the first day of leave is not given
  "before the leave is taken" -- a payment before termination is not one "on the termination". Asserted.

## What the Act turns out to say (findings)

1. **"Should", not "must", for taking leave.** s 7(1)-(3) say leave "should be granted ... as soon as practicable",
   "should be taken in one continuous period", and the employer "should give ... at least 60 days notice". None is a
   duty with a penalty; s 13(1)(a) lets SAET order leave where a worker "is not granted long service leave in
   accordance with this Act", but whether a departure from a "should" is "not in accordance" is not said. The notice
   question reports the 60 days as what the employer "should give", and asserts it.
2. **13 weeks for 10 years is 1.3 weeks a year.** s 5(1)(a) and (b) together give exactly 1.3 weeks for each completed
   year from 10 years (15 years: 19.5 weeks), the same rate as the s 5(3) pro-rata payment. Asserted.
3. **Misconduct does not cost a worker with 10 years anything.** s 5(4) takes away only the s 5(3) payment (7 to 10
   years). From 10 years, s 5(2) pays "where the service ... is terminated", however it ends. Asserted.
4. **A death between 7 and 10 years is paid.** s 5(5) treats death as a termination and vests "the worker's entitlement
   under this section" in the personal representative, so s 5(3) pays (8 years: 10.4 weeks); s 8(4)(b) makes it due on
   the representative's request. Asserted.
5. **ss 5(6) and 7(6) fit together.** For leave taken in advance (s 7(4)(d)) and service ending before it accrues, s
   5(6) reduces the termination payment to nothing and s 7(6) lets the employer recover only the excess over what the
   worker would have had: at 8 years with 13 weeks taken at $1,000, the deduction is $2,600 and the worker keeps
   $10,400, the s 5(3) amount. Asserted (fork F6).
6. **Any part-time spell puts the worker on averaging.** s 3(2)(b) applies "if during the whole or part of the period
   of three years" the worker was hourly, casual, part-time or had varied hours; a single changed roster triggers
   three-year averaging. A casual is "not to be regarded as being paid at a penalty rate", so the casual loading stays
   in the hourly rate. Accommodation is added for leave and on termination but not for cashing out (s 8(3a)(a)).
   Asserted.
7. **The inspector's 14 days and the review's 14 days coincide.** A notice may give as few as 14 days (s 12(1)), and an
   application for review "must be made within 14 days of the receipt" (s 12(3)): with a 14-day notice the employer must
   comply or seek review by the same day. A notice giving fewer than 14 days is outside s 12(1). Asserted.
8. **A former worker's records.** Records must be kept for three years after the service ends (s 10(2)(c)), and SAET
   applications may be made for three years (s 13(4)), but s 10(5) gives the right to inspect to "a worker" against
   "his or her employer". s 13(3) (the worker's account accepted unless disproved) is the remedy where records were not
   kept. Fork F12.
9. **Register slips.** The legislative history says ss 9 and 12 were amended by "63/2017"; the amending Act is No 63 of
   2016 (the Statutes Amendment (South Australian Employment Tribunal) Act 2016), so this reads as a typing error in
   the table. s 3(2)(b)(ii) reads "the workers ordinary hours" without an apostrophe. Gaps in numbering (s 2, s 7(5), s
   12(5), s 13(5), Schedule cl 1) are repeals left unrenumbered, not errors.
10. **"Enterprise agreement" is the State one.** s 3(1) defines it under the Fair Work Act 1994 (SA); s 16(b) excludes
    workers with an entitlement under a Commonwealth "fair work instrument". Whether a given award or agreement gives
    "a long service leave entitlement" is asked as a fact; worth checking against the Fair Work Act 2009 (Cth) s 113 and
    its transitional instruments before relying on the answer.

## Before relying on it

Check the text against the authorised PDFs and the register's current version; have a lawyer review the forks
(especially F4, F5, F6, F10 and F12) and findings 1, 5 and 10; encode the employer's seat (ss 5, 7(6), 8, 10, 12, 14(2))
as a second layer over `salsl-core.l4`; run an independent test pass; deployment to Legalese Cloud is for a person with
access.
