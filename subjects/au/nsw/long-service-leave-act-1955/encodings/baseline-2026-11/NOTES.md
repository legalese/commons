# Long Service Leave Act 1955 (NSW) -- baseline encoding, the worker

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025
> (corpus document in force 1 July 2024). It is unofficial and may be out of date: amendments after that version are
> missing. Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 in substance. A seat-neutral core
(`lsl-core.l4`) holds every rule, with one regulative rule (the worker must apply within 6 years of the payment falling
due, s 12) run by `EVALTRACE` inside a function that takes only plain facts. The seat layer (`lsl-seat.l4`) asks the
questions and restates no rule. Dates sit in one small module (`lsl-dates.l4`, built-in date functions only, no
daydate, no `YMD`). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.

Answers are named outcomes (enumerations), dates or numbers, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used.
Where the text says no in its own words (the s 3(1) "worker means" definition and its exclusion, s 4(11)(a) "service
... means continuous service", s 4(13)(b)(ii) "only if", s 4(8) "shall not", s 4(2)(a)(iii)'s closed list of reasons)
the outcome begins "no:" (or the amount is 0); where a provision's scope is not met without an "only" (s 15C outside the
prescribed period) it says the provision "does not reach this". Judgments the Act leaves to someone else are inputs.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Limitation Act 1969 baseline does not govern
s 12's window (s 12 sets its own); the stable `l4` cannot IMPORT across subjects in any case.

## Edition

- **Act:** Long Service Leave Act 1955 No 38, corpus document `nsw_legislation:2024-07-01/act-1955-038` (in force
  1 July 2024), deposited at `../../registers/source-bundle/act-1955-038.txt`, from the Open Australian Legal Corpus
  (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Regulations:** none deposited. The Act lets regulations set three numbers this encoding uses: the s 3(2C) annual
  amount (asked as an input), a greater board or lodging value than $15 and $5 (s 3(2)(d); the Act's own figures used),
  and a later end of the COVID-19 period than 30 September 2021 (s 15C(3); the Act's own day used). Finding 4.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lsl-dates.l4` | 0 | 0 | 0 | 0 |
| `lsl-core.l4` | 0 | 0 | 0 | 0 |
| `lsl-seat.l4` | 0 | 0 | 0 | 0 |
| `lsl-cases.l4` | 0 | 0 | 131 | 131 |

Every expected value was worked by hand from the text, with day counts and fractions written beside the cases. Edges:
5, 10 and 15 completed years and the day before; one day not counted delaying the 10th anniversary; a 29 February
start; the 2-month and 12-month return windows to the day and a day over, with a month-end (31 December + 2 months =
28 February); the COVID-19 period's first and last days and the day outside each; one month's notice to the day and a
day late (31 March less a month = 28 February; 29 March 2024 less a month = 29 February 2024); the 6-year recovery
window to the day and a day over, with a 29 February due day; the s 3(2C) threshold met exactly and exceeded by a dollar;
the (5AA) and final-pay caps on a deduction. All 131 were satisfied on the first run.

Negative control, in a scratch copy: with the s 4(11)(a1)(vii) return window lengthened from 2 to 3 months and the
s 12 window from 72 to 73 months, the cases failed exactly the 7 predicted assertions (the two late returns, the two
last days to apply, and the three late applications).

## Seat

**The worker (required)** (`lsl-seat.l4`, 18 questions): the employee claiming long service leave or pay for it, and,
where the worker has died, the personal representative claiming for the estate (s 4(5)(b), (9)). Questions:

- Am I covered? "Does the Act give me long service leave?"; "By when must I elect to come under the Act instead of my
  employer's exempt scheme?"
- My service: "Was my service continuous despite this break, and do its days count?"; "When do I first become
  entitled?"
- How much leave: "How many weeks have I earned?"; "How many weeks am I still owed?"; "What is my weekly ordinary pay?"
- Taking my leave: "Can I take it in separate periods, in advance, or later?"; "With no fixed hours, how many hours is
  one day?"; "How many extra days for public holidays?"; "Was I given enough notice?"
- Being paid: "Can I be paid instead of taking it, and who is paid when employment ends?"; "How much must I be paid for
  untaken leave?"; "How much can be deducted for leave I took in advance?"
- If I am not paid: "By when must I apply to recover it?"; "Is my claim in time?"; "Until when must my employer keep my
  record?"; "What penalty does my employer face, and who can prosecute?"

Provisions addressed to the employer, the Commission or an inspector are encoded as what they mean for the worker. No
employer seat (one would be welcome: s 4(5)(c), 4A, 4B, 8 and 10 bear on employers) and none for the Commission.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulation is deposited, so the Act's own
  figures are used and the one number with no default (s 3(2C)) is an input (finding 4).
- **The actors the text names.** Followed: the worker, the employer, the personal representative, the Industrial
  Relations Commission, the tribunal, the Local Court, the inspector, the union secretary.
- **Judgments answered conditionally.** Followed: "serious and wilful misconduct", "illness, incapacity or domestic or
  other pressing necessity", the tribunal's satisfaction that a bailment is bona fide (s 3(3)), "more favourable"
  (s 5(1)(a)), the employer's agreement, and the averages of pay, bonuses and hours are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "worker" (s 3(1), (3), (4)), "ordinary pay"
  with "prescribed date", "ordinary remuneration", "bonus" and board and lodging (s 3), "service" and continuity
  (s 4(11), (13)), "month" (s 4(2)(a3)), "related" corporations and "transferred" (s 4(13)(b)). Borrowed and asked:
  "employed", award, enterprise agreement, registered worker under the portable schemes.
- **One case:** one worker's service with one employer (carrying over service the Act deems to be with that employer).
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** ss 1, 2, 6, 9, 9A, 11(3), (4), 14, 15, 16, Schedule 1.

## Scope

**In:** s 3 (worker; ordinary pay, with (2), (2A), (2C), (3), (4)); s 4(1), (2)(a), (a3), (b)(ii) (the amount and
deductions); s 4(3), (3AA), (3A), (3B) (taking the leave); s 4(4A) (public holidays); s 4(5)(a)-(c), (5AA), (5A), (5B)
(payment on termination or death, deduction for leave in advance, portable-scheme workers); s 4(8), s 7 (no payment
in lieu, no contracting out); s 4(9) (personal representative); s 4(10), (10A) (notice); s 4(11)(a), (a1), (b), (c)
and s 4(13)(b)-(e) (continuous service, apprenticeships, transmission, related corporations); s 5(1), (2)(a), (c)(i)
(exclusions, exemption and election); s 8(3) (records kept 6 years); s 10(1), s 10A, s 11(1), (2) (penalties and who
prosecutes); s 12(1) (6-year recovery window); s 15C (COVID-19 stand-downs).

**Out, and why:**

- s 4(2)(a2) (service before the 1963 amendment): no worker is likely still in that service; a second pass could add it.
- s 4(2)(b)(i) (leave under an agreement for leave on top of the Act's): folded into the "weeks already taken" input's
  `@desc`, which tells the worker not to count it.
- s 4(4) (annual holidays exclusive of long service leave) and s 4(7) (the three ways leave pay may be paid during
  leave): no calculation turns on them; a pass for the employer's seat could add s 4(7).
- s 4(11)(d), (12) (war service before 1945 and Commonwealth reinstatement rights): historical.
- s 4(13)(f) (no double entitlement where another employer has discharged it): left for a pass on multi-employer
  service.
- s 4A, 4B (the employer's notice to the Long Service Corporation), s 4C (contract cleaning election), s 8(1), (2), (4),
  s 10(2), (3), s 10B, s 12(2) (union proceedings), s 13 (1985 savings for awards): the employer's duties, union
  machinery or spent savings.
- s 5(2)(b), (c)(ii), (iii), (d), (3), (4), s 5A (the Commission's exemption machinery and the 1955 transitional
  election): official machinery; s 5(2)(c)(iii) (benefits on electing out of a scheme) would suit a later pass.
- s 12(1)'s floor ("not earlier than 2 years before the date of assent to the Long Service Leave (Amendment) Act 1980"):
  spent.

## Forks (the text does not say; one reading taken)

- **F1** Months: "n months after" a day ends on the same day of the month n months later, or that month's last day where
  it is shorter; going back a month works the same way.
- **F2** Counting service: the counted start is the first day of service moved forward by the days not counted; n years
  are completed when the day after the last day of service is on or after the nth anniversary of the counted start; a
  part year is the days since the last anniversary over the days in that service year. The worker is entitled on the
  10th anniversary.
- **F3** s 4(11)(a1): the days of a break under (i) (absence under the terms of employment) or (ii) (illness or injury)
  count as service, because the proviso leaves out only the days of breaks under (iii)-(vii).
- **F4** s 15C: a stand-down counts if it began within the prescribed period.
- **F5** The days of a break run from its first day to the day of return (the return day is service).
- **F6** s 4(2)(a)(i)(C): "the number of years service ... completed since the worker last became entitled" counts whole
  years only (finding 2).
- **F7** s 4(2)(a)(ii): for 10 to 15 years on termination, the proportionate amount is the whole amount, with (i)(A)'s
  2 months within it, not added to it (finding 5).
- **F8** s 3: on a tie between the two figures in (a) or (b), the first is taken (which fixes the bonus period in (c));
  s 3(2C)'s "annual amount" is 52 times the weekly ordinary pay without bonuses, board and lodging included.
- **F9** s 5(2)(c)(i) "as the case may require": the 3 months run from the later of the exemption's start and the
  employment's start.
- **F10** s 4(3B): the hours in a day are A divided by B (the formula itself is missing from the deposit: finding 3); on
  a tie of the two averages, the 12 months.
- **F11** s 4(10): "at least one month's notice" is met by notice given on or before the same day of the month one
  month before the leave begins.
- **F12** s 12(1): the 6 years immediately preceding an application made on day A begin on the same day six years
  earlier, so a payment due on day D is in time for an application on or before D plus 6 years.
- **F13** The day a payment "has become due" is asked as a fact (on termination, s 4(5)(a)'s "forthwith" read as the
  day of termination, in the `@desc`).
- **F14** The regulative rule's day 0 is the day the payment fell due.

## What the Act turns out to say (findings)

1. **The text is a corpus copy.** Version in force 1 July 2024, collected 10 March 2025; later amendments are missing.
2. **Part years after 15 years are lost, below 15 they count.** s 4(2)(a)(i)(C) pays on termination for "the number of
   years service ... completed" since the last entitlement, which on its words counts whole years; (ii) and (iii) pay "a
   proportionate amount" on the actual service. Read literally, a worker leaving at 17 years 6 months gets the same
   3.4 months as one leaving at 17 years, while one leaving at 14 years 6 months is paid for the half year. Asserted.
   (Practice may read (C) proportionately; a lawyer should say.)
3. **The s 4(3B) formula is missing.** The deposit reads "calculated as follows--" then a blank line, then "where-- A
   is ... B is ...". The formula did not survive conversion; A divided by B is taken (fork F10) and should be checked
   against the authorised rendering and recorded in a `act-1955-038.formulas.md` sidecar beside the deposit.
4. **Three numbers left to regulations, none deposited.** s 3(2C)'s threshold (asked), s 3(2)(d)'s board and lodging
   values ($15 and $5 "or such greater sum as may be prescribed"; the Act's figures used, which a regulation may have
   raised), and s 15C(3)'s end of the prescribed period (30 September 2021 "or a later day, not later than 31 March
   2022"; the Act's day used). A deposit of the Long Service Leave Regulation would close all three.
5. **s 4(2)(a)(i) and (ii) overlap.** A worker with 10 to 15 years who leaves meets both (i)(A) (2 months for 10 years)
   and (ii) (3 months for 15 years, pro rata); the text does not say whether they add. Read as one amount (fork F7):
   12 years gives 2.4 months, not 4.4. Asserted.
6. **A garbled cross-reference.** s 4(3A) says an advance agreement does not confer an entitlement "for the purposes of
   subsection (2) (A) (i) (B) or (C)"; there is no subsection (2)(A). It must mean (2)(a)(i)(B) or (C). Not asserted.
7. **s 4(3)(b)'s split rules are spent.** s 4(3AA) ("Despite subsection (3)(b)") lets the parties agree to any number of
   periods of at least 1 day, so the 2-, 3- and 4-period limits in s 4(3)(b)(i)-(iii) no longer bind an agreement.
   Asserted (two periods of 1 day).
8. **Portable schemes and s 5(1)(b).** s 5(1)(b) takes s 4 away from a worker whose class has long service leave "by or
   under any Act", but s 4(5A) and (5B) expect registered building and cleaning workers to apply for leave under this
   Act. The encoding answers the two questions separately and does not decide how they fit.

## Before relying on it

- Check the deposited text against the authorised text on legislation.nsw.gov.au, recover the s 4(3B) formula, and
  look for amendments after 1 July 2024.
- Deposit the Long Service Leave Regulation and replace the three Act figures (finding 4).
- Add s 4(2)(a2), s 4(13)(f) and s 5(2)(c)(iii), and an employer's seat.
- An independent test pass and the human gates.
