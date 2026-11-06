# Workers Compensation and Injury Management Regulations 2024 (WA) -- baseline encoding, the injured worker

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (reg 20, the worker's own
duty to give notice of remunerated work; reg 53, the insured last employer's duty to pass a hearing loss claim to its
insurer) run by `EVALTRACE` inside exported questions that take only plain facts. No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

This is the first encoding of the Regulations as a subject of their own. The Act's baseline
(`subjects/au/wa/workers-compensation-and-injury-management-act-2023/encodings/baseline-2026-10/`) already reads regs 4,
13-16, 18, 19, 22, 23, 24, 90, 122 and 134 for the Act's own questions; nothing there was touched. Regs 4, 19, 22, 23,
24, 122 and 134 are encoded again here, as the Regulations' own provisions, so that this encoding stands on its own; the
stable `l4` cannot IMPORT across subjects in any case. The two encodings agree on those figures.

## Edition

Workers Compensation and Injury Management Regulations 2024, compilation version 00-c0-00, current from 30 June 2026
(mrdoc 49606, retrieved 19 October 2026), deposited at `../../registers/source-bundle/mrdoc_49606.txt` (text sha256
a2df35ab...5f9ac304 as recorded in its `.meta.json`). Its compilation table ends with the Amendment Regulations 2026 (SL 2026/35), whose reg 4 comes into
operation on 1 July 2027 and is not in the deposit. The Act (mrdoc 48940) was read, not encoded, for ss 10, 11, 32, 58,
65, 66, 74, 86, 90 and 538, which these regulations serve.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wcimr-dates.l4` | 0 | 0 | 0 | 0 |
| `wcimr-amounts.l4` | 0 | 0 | 0 | 0 |
| `wcimr-diseases.l4` | 0 | 0 | 0 | 0 |
| `wcimr-claims.l4` | 0 | 0 | 0 | 0 |
| `wcimr-hearing.l4` | 0 | 0 | 0 | 0 |
| `wcimr-cases-amounts.l4` | 0 | 0 | 34 | 34 |
| `wcimr-cases-diseases.l4` | 0 | 0 | 53 | 53 |
| `wcimr-cases-claims.l4` | 0 | 0 | 52 | 52 |
| `wcimr-cases-hearing.l4` | 0 | 0 | 57 | 57 |

196 assertions, all satisfied. Every expected value was worked by hand from the text, with the edges: every qualifying
period at and one below its line (4 and 12 weeks; 6, 12, 24, 60 months), 30 June and 1 July 2024 (reg 8), 15 and 16
February 2020 (reg 9), 31 January and 1 February 2022 and 5 and 6 May 2023 (reg 10), 12 and 13 November 2013 (reg 11),
the 7-day periods counted both ways (reg 20 "beginning on", reg 53 "after"), day 14 and 15 and day 119 and 120 (regs 56,
57), the 3 months and 12 months "ending on" a day (regs 43, 51), exactly 2 years (reg 44), 27 and 28 days (reg 81), 13
and 14 days and a fourth specialist (reg 88), 85 dB(A) and 140 dB(C) exactly (reg 40), 10% and 9.9%, 5% and 4% (regs 46,
51), month ends (30 November plus 3 months), half a cent and 50 cents (regs 4, 35(2)), and an index that falls (s 538(5)).

## Seat

**The injured worker** (for regs 7-10 and 65-66, also the worker's dependants after a death caused by the injury). Every
exported question is one the worker would ask: "Is my disease taken to be from my employment?", "By when must I give
notice of remunerated work?", "Can I be required to attend this case conference?", "Who must pay for my hearing test?",
"May I give my claim to the insurer myself?", "By when must I be paid?". Duties the regulations put on the insurer, the
employer, WorkCover WA or an assessor (regs 19, 22, 53, 56, 57, 61, 74, 81, 88, 92) are encoded as what they mean for the
worker. No other seat is written: the employer's and insurer's duties here are procedural and the worker's questions
cover them.

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** The regulations are themselves the number-setting instrument.
  The index figures they use (Perth CPI, WA Wage Price Index, ABS average weekly earnings) and last year's amounts are
  published elsewhere and are not deposited: inputs. Starting figures ($181, $13 994, 55 cents, $139, $149, $11 739,
  $530 724, $252 724) and the methods are encoded.
- **The actors the text names.** The worker, the employer and last employer, the insurer and self-insurer, the treating
  medical practitioner, the ENT specialist and authorised audiologist, the arbitrator, the Director, WorkCover WA.
- **A judgment handed to someone else answered conditionally.** Whether hours are reasonable (regs 81, 88), whether the
  employer proves the disease was not from employment (Act s 10(2)), whether the work is of the kind Schedule 1 describes:
  inputs.
- **Definitions worked out, borrowed terms asked.** Noisy employment (reg 40), initial and further hearing loss, the
  last employer (reg 51), the qualifying periods (reg 6) are worked out. "Prisoner" (Prisons Act 1981), AHPRA registration,
  DSM-5, NATA accreditation are asked.
- **One case.** One worker, one injury or disease, one claim.
- **The text's own terms with a plain gloss,** in each input's `@desc`.
- **Operative provisions in, machinery out.** See Scope.

## Scope

**In.** Reg 4 (rounding); Part 2: regs 5-11 and Schedule 1 (all 51 items; item 25 as its two limbs); Part 4: regs 19-22,
23-26, 29, 30(1), 32 (all 11 services), 34, 35, 37, 39, 40(1)-(2), 41, 43, 44, 46, 48, 51, 53, 54, 56, 57, 59(2), 60(1),
61, 65, 66; Part 5: regs 74, 81, 88 (Part 6 Div 1); Part 6: regs 91-92; Part 8: reg 108; Part 9: regs 120, 122; Part 11:
reg 134.

**Out, and why.**
- Part 1 regs 1-3 (citation, commencement, definitions: the definitions used are quoted where used).
- Part 3, regs 12-18 (who is a worker): encoded in the Act's baseline; Schedule 2 with them.
- Regs 27, 28, 30(2) (the approved form for the employer's notices and confirmation): no fact the worker states turns on
  them. Reg 31 (a definition), reg 33 (what satisfies the arbitrator for a special increase; the Act's baseline asks it as
  an input), regs 36 and 38 (what rehabilitation services are reasonably necessary or may be provided: lists for
  providers).
- Regs 42, 45, 47, 49 (who may test and assess, and how): folded into the inputs of regs 41 and 51 as "done under the
  regulations". Reg 52 (the last employer deals with the claim as if wholly liable; the worker must give information):
  52(1)-(2) are noted under reg 51, 52(3) is a duty with no time. Regs 55, 58, 62-64 (WorkCover WA's copy, uninsured
  employers, apportionment between employers, the NIHL register): between employers, insurers and WorkCover WA.
- Reg 59(1), (3)-(5) and 60(2)-(4) (the insurer's application, what goes with it, the arbitrator's powers): the worker's
  side, 59(2) and 60(1), is in.
- Reg 67 (discharging the child allowance by a payment to WorkCover WA): its formula did not survive conversion (the
  deposit has the "where" list but not the formula) and it is a payment by the employer.
- Regs 68-72 (registering settlement agreements): procedure for the Director.
- Regs 73, 75-80, 82-87 (injury management systems, return to work programs, conduct of case conferences, certificates of
  capacity, rehabilitation provider approval): duties on employers, doctors and providers with no deadline the worker
  meets. Reg 74 is in.
- Reg 89, 90 (who may request and pays for an impairment assessment): reg 90 is in the Act's baseline.
- Part 7 (insurance, licensing, the policy in Schedule 3), Part 8 regs 106, 107, 109 and Division 2 (authorised agents,
  witness allowances, costs assessment), reg 121 (the Director registers the election), Part 10 (electronic lodgment),
  Part 12 (inspectors, infringements, adjacent areas, registered agents; Schedules 4-7), Part 13 (transitional NIHL
  provisions for claims before 2024 and loss before 1991): machinery, or not the worker's.

## Forks (one line each, for the reviewer)

- **F1** Day counting. "Within n days after" a day: the day excluded, last day = day + n (Interpretation Act 1984 (WA)
  s 61). "Within 7 days beginning on" (reg 20) and "the period of n days beginning on" (regs 19, 21(6), 22, 57): the day
  included, so 7 days end on day + 6 and the day after 120 days is day + 120; reg 57's notice must come "before" that day,
  so by day + 119. "The period of n months ending on" a day (regs 43(1)(b), 51(5)) begins the day after the same day n
  months earlier. Other reading: count "beginning on" the same as "after".
- **F2** Indexation. "The percentage by which the [index] varies" is taken exactly (later index / earlier index), not as a
  published percentage rounded to one decimal place; reg 4 then rounds the amount. Other reading: use the ABS-published
  percentage.
- **F3** Reg 108, 6% per annum: simple interest on a 365-day year, rounded to the dollar by reg 4. Other reading: no
  rounding, or a day count the arbitrator fixes.
- **F4** `Is my disease taken to be from my employment`: a disease not in Schedule 1 answers FALSE ("s 10 gives no
  presumption"), not NOTHING, though Schedule 1 is not closed with "only"; s 10(5) still lets the link be proved.
- **F5** `Is my COVID-19 taken to be from my employment`: a living worker never diagnosed on a reg 9(4) test has no reg
  9(3) day, so reg 9(5) is not met: FALSE. Other reading: fall back on reg 7.
- **F6** "Not more than once every 4 weeks" (reg 81) and "more frequently than once every 2 weeks" (reg 88): measured
  from the last conference or examination the worker was required to attend; 28 and 14 days are within the limit. Other
  reading: a rolling window.
- **F7** Reg 44 against reg 43(1): where the employer has paid for a test less than 2 years earlier, `Who must pay for my
  hearing test` answers "not settled by the text" (finding 2). Reg 48 follows reg 43(1)(a), (b) for the NIHL assessment
  without reg 44's limit, so the employer pays for the assessment.
- **F8** Reg 43(1)(b) "employed by that noisy employer within a period of 3 months ending on the day" of the test: read as
  the last day of the noisy employment falling in that period.
- **F9** Reg 74 "on the request of a worker": no request, no duty (JUST FALSE). Reg 39, 37(2), 30(1), 32 (another
  service), 81 and 88 within their limits: NOTHING, the text pointing elsewhere (s 165, s 180, s 66(2)(a), s 71(1)) or
  not closing its list.

## What the Regulations turn out to say (findings)

1. **Two ways of counting 7 days.** Reg 20(1)(b) gives the worker 7 days "beginning on" the later day (last day = day +
   6), while regs 21(2), 53, 55, 56, 61 and 92 count "after" (last day = day + 7). A worker who reads "7 days" the second
   way gives notice of remunerated work one day late. Asserted (16 and 17 May 2026).
2. **Reg 44 leaves a gap.** Reg 43(1) puts the cost of an audiological test on the current or last noisy employer, and on
   the worker only "if paragraph (a) or (b) does not apply". Reg 44 says a noisy employer "must pay ... not more frequently
   than once every 2 years". For a second test within 2 years, (a) or (b) still applies, so (c) does not put the cost on
   the worker, yet reg 44 relieves the employer. The text does not say who pays. Asserted as "not settled by the text".
3. **"Liability decision notice" in reg 60(1).** Reg 60(1) speaks of "a liability decision notice", the Act's term for a
   s 28 notice, while the hearing loss notice is defined in reg 56 as an "NIHL liability decision notice" and reg 59(1)
   uses that term. Read as the NIHL notice, since it refers to reg 56(2)(b)(i)-(iii).
4. **Given or received.** Reg 56 runs 14 days from the claim being "given to" the insurer; reg 57(1) runs 120 days from
   the day the insurer "receives" it. Reg 54(3) and 56(6) fix the giving; nothing fixes receipt. Encoded as the same day.
5. **Uneven rounding of travel rates.** Reg 35(2) rounds the per-kilometre rate to the cent "despite regulation 4"; the
   meals and accommodation rate in reg 35(3) is left to reg 4 and rounds to the whole dollar.
6. **Reg 9(3) and a living worker.** COVID-19's injury day exists only on a diagnosis on a NATA test result or a death; a
   worker diagnosed otherwise (for example on a rapid antigen test) gets no reg 9(3) day, and reg 9(5) cannot be met.
   Asserted (fork F5).
7. **Lung cancer by two routes.** Primary site lung cancer is a firefighter disease with a 15-year qualifying period (reg
   11) and, under Schedule 1 item 26, a prescribed disease after 5 years' exposure to diesel exhaust, soot or the other
   agents. A firefighter may meet the second first; the two presumptions are separate and both are encoded.
8. **Reg 67's formula is missing from the deposit.** The deposited text has the definitions of C, W and N but not the
   formula itself. A `mrdoc_49606.formulas.md` sidecar from the authorised PDF is needed before reg 67 can be encoded.

## Before relying on it

- The index figures and last year's amounts are inputs: check them against WorkCover WA's published amounts. The cases use
  illustrative indices.
- Compare with the authorised text (the deposit is a conversion of the Word document) and with SL 2026/35 reg 4 from
  1 July 2027.
- Have a lawyer check forks F1-F9 and finding 2.
- No independent test pass has been run.
