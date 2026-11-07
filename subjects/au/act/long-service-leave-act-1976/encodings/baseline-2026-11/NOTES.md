# Long Service Leave Act 1976 (ACT) -- baseline encoding, the employee

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for: the provisions a claimant meets. The Act is short (about 54,000 characters with its endnotes), so
it is encoded whole apart from the machinery. No encoding of this Act existed, so this is a new baseline at
`encodings/baseline-2026-11/`. Three files:

- `lsl-dates.l4` -- date helpers only (built-in date functions, no daydate, no `YMD`);
- `lsl-employee.l4` -- 25 exported questions, three regulative rules (DEONTIC functions);
- `lsl-employee-cases.l4` -- worked cases.

The duties with deadlines are regulative rules, run by `EVALTRACE` inside questions that take only plain facts:

- the employer's written notice of the day long service leave starts, at least 60 days before (s 6 (2));
- the employer's payment for the leave credit within 90 days after employment ends (s 11A (4));
- the employer's compliance with an authorised officer's notice within 28 days after receiving it (s 13E).

Each `LEST BREACH BY` the employer carries the offence as its reason. Time in those rules is counted in day serials
(`DATE_SERIAL`), so a rule's deadline is the last day's serial; the cases confirm that an act on the last day fulfils it.

## Edition

- **Act:** Long Service Leave Act 1976 (ACT), A1976-27, Republication No 29 (R29), effective 19 November 2025, last
  amended by A2025-30, as deposited at `../../registers/source-bundle/A1976-27.txt` (converted 2026-11-06 from the
  register's DOCX, which the register marks as an unauthorised version; the authorised text is the register's PDF).
  The s 2F formula is an image in the DOCX and was transcribed from the authorised PDF at deposit (total payable ÷ 52).
- **Numbers set elsewhere:** none. The Act makes no regulation that sets its numbers (s 18 is the bare power, and no
  regulation is deposited). Penalty units (s 133 of the Legislation Act 2001: $160 an individual, $810 a corporation at
  the republication date) are only named in answers, not computed.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read. A deliberately wrong assertion (s 11A, 10,401 for 10,400) was run once in a scratch copy, since deleted, and showed
as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lsl-dates.l4` | 0 | 0 | 0 | 0 |
| `lsl-employee.l4` | 0 | 0 | 0 | 0 |
| `lsl-employee-cases.l4` | 0 | 0 | 125 | 125 |

Every exported question has cases, with the edges: the 2-month and 6-month return windows on their last day and the day
after (from 31 August, 6 months is 28 February); 14 and 15 days of illness leave; an apprenticeship ending 30 June with
service starting 30 June and 1 July a year later; the Act's own example (Fiona: 10 years from 1 January 1992 with 9 months
uncounted falls due on 1 October 2002); the day before and the day of the 7th anniversary, with and without uncounted
time; a start on 29 February; 6, 7, 9 and 10 years of leave; untaken leave of 0.2, 0.8, 0.95 and 1 month for the 4-week
test; notice on the 60th day before leave and the day after; the 90th day after employment ends and the 91st; 59, 60, 72,
83 and 84 months for pro rata; retiring at 64 and 65, and at an award's age of 60 and one year short; the 28th day after a
notice to comply and the 29th.

**No mirror cases.** One seat.

## Seat

**The employee** (`lsl-employee.l4`): a person employed in the ACT (full-time, part-time, casual, on piecework or by
commission, not a public employee or MLA staff) who claims long service leave, pay for it, pay instead of it when the
employment ends, or pro rata pay; after the employee's death, the **legal personal representative** who claims the
payment (ss 11A (2) (d), 11C (1) (d)), who asks the same questions with the dead employee's facts. "Am I covered?", "Does
this break count against my service?", "Does my earlier employer's service count?", "When do I become entitled, and to
how much?", "Must my employer let me take it, and tell me 60 days ahead?", "At what rate, and how, must I be paid?", "What
am I owed when my job ends, and by when?", "Can someone represent me at the complaint conference?", "Did my employer
comply with the notice to comply?", "Does my award change this?".

The employer is the text's actor; what it did is asked as a fact. The registrar of long service leave and the
authorised officer get no seat: their powers appear only as what the employee meets (the conference, the notice to
comply). No employer seat was written.

### Defaults followed

- **The Act alone:** no instrument sets its numbers; none is brought in.
- **The text's actors:** the employee, the employer, the legal personal representative, the authorised officer.
- **Judgments as inputs, never decided:** whether a domestic or other pressing necessity justified resigning, whether
  misconduct was serious and wilful (s 11C (1) (a)); whether an award right is more advantageous (s 14 (2)); "as soon as
  practicable" (s 6 (1), s 8 (3)) is stated in the answer, not decided.
- **The Act's own definitions in L4:** employee, continuous service, period of service, ordinary remuneration, minimum
  retiring age, long service leave credit. Borrowed terms asked as facts: whether a person is employed at all, public
  employee, associated company, award, agreement, approved training contract.
- **One case:** one employment with one employer (with service carried across by ss 10, 10A, 11).
- **The Act's terms, glossed** in `@desc` and comments.
- **Machinery out:** see Scope.

## Scope

**In:** s 2C; ss 2D, 2E, 2EA; s 2F; s 2G; s 3; s 4; s 6; s 7; s 8; s 9; s 10; s 10A; s 11; s 11A; s 11C; s 11D;
s 12 (2); s 13D (4); s 13E (with ss 13F, 13G only in a comment); s 14; the dictionary definitions of employee,
continuous service, ordinary remuneration and salary or wages.

**Out, and why:**

- ss 1-2B (name, dictionary, notes, Criminal Code): formal.
- s 12 (1) and (3) (what the record must contain; inspection by an authorised officer): duties the employee never has to
  apply; only how long the record is kept (s 12 (2)) is a question the employee or estate asks.
- ss 12A-13CE, 13J, 13K (definitions for part 3, the registrar's appointment, authorised officers, identity cards, entry,
  directions, self-incrimination, warnings, immunity, delegation): machinery and officials' powers.
- ss 13D (1)-(3), (5) (referral of complaints and the officer's power to call a conference): an official's powers; the
  part the employee meets, representation (s 13D (4)), is in.
- ss 13F, 13G (the employer's internal and ACAT review of a notice to comply): the employer's remedies; finding 7.
- s 18 (regulation-making power): machinery.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 6 months after the day", "within 2 months after the day", "within 1 year after the day", "7 years after
  the day" (s 2G (2) (b), (e); dictionary, continuous service (d); s 12 (2)) -- `the day ... months after` -- the
  corresponding day of the later month, or that month's last day if it has none (29 February + 7 years = 28 February);
  the day of the event excluded -- the Legislation Act 2001 (not deposited) may count otherwise.
- **F2** ss 3, 2G (5) -- `the day ... years of service are completed from`, `the completed years of service` -- the
  entitlement falls due on the anniversary of the start moved on by the uncounted time, whole months first, then days,
  as the Act's own example in s 2G counts it ("falls due on 1 October 2002") -- "arises at the end of the period"
  (s 3 (3)) read as the end of the day before the anniversary, one day earlier.
- **F3** s 2G (2) (a), (b), (e) -- `s 2G -- what does this break do to my service` -- a dispute with no return on the
  settlement terms falls to (e) (return within 2 months); a stand-down not re-employed within 6 months is broken, since
  (e)'s 2 months is shorter -- (a) and (b) as complete codes for their kinds of break, so a failure is broken at once.
  A break no head saves is answered "continuity broken" as the text's no (the "if" of each head fails) -- the Act never
  says in terms that any break breaks continuity, so NOTHING-kind.
- **F4** ss 3, 4, 11A (1) -- `the months of leave for`, `s 11A -- how much am I owed ...` -- before 7 years there is no
  leave, so no credit, and s 11A pays nothing (s 11C deals with 5 to 7 years) -- s 4 says leave "accrues" at 1/5 of a
  month a year from the start, and s 11A's credit is "the amount of long service leave that has accrued", which would
  give pay for any service on any ending (finding 1).
- **F5** s 6 (1) (a) "4 weeks or more" -- `s 6 -- must my employer grant my leave` -- 1 month or more of untaken leave
  is 4 weeks or more, less than 28/31 of a month is not, and in between the answer is NOTHING-kind -- a fixed conversion
  (for example 52/12 weeks a month, under which 4 weeks is about 0.92 of a month).
- **F6** s 6 (2) "at least 60 days before the date" -- `s 6 (2) -- the last day for written notice of my leave` -- the
  notice day is 60 or more days before the start day (leave from 1 March 2027: notice by 31 December 2026) -- 60 clear
  days (by 30 December 2026).
- **F7** s 7 (3) -- `s 7 -- my weekly rate of pay ...` -- the fifth of 5 years' salary or wages is a yearly figure,
  turned to a weekly rate by dividing by 52 (as s 2F counts a year) -- a yearly figure applied pro rata by days of leave.
- **F8** ss 7, 11A (3), 11C (2), 11D -- `the pay for ... months of leave at` -- a month of leave is paid as 52/12 weeks of
  ordinary remuneration -- the remuneration of the actual calendar month or months the leave would have covered.
- **F9** s 11C (2) "the number of years or months of service completed" -- `s 11C -- how much pro rata ...` -- counted in
  completed months (6 years 11 months = 83/120 of 2 months) -- counted in completed years (5 years whatever the months),
  which pays less.
- **F10** s 12 (2) "for 7 years after the day" -- `s 12 (2) -- until when must my employer keep my records` -- the day
  returned is the day 7 years after (the anniversary) -- the day before it.
- **F11** s 11A (4) "within 90 days after the day" and s 13E (1) "within 28 days after the day" -- the regulative rules --
  the 90th (28th) day after is the last day -- the same day moved off a weekend or public holiday by the Legislation Act.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries NOTHING-kind tags (who is employed at all; an apprenticeship ending more than a year before; a
portable scheme without an election; less than 4 weeks or an uncertain 4 weeks in s 6 (1); s 8 (3) with leave paid in a
way s 8 (1) does not allow). Most questions answer with a choice from a list: the answer marked "NOTHING-kind" is the
NOTHING answer, and the answers marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 11C (1) "Where ... (a) ... (b) ..." fails -- the text's no (rule (b)); s 11A (2) "Where ... (b) the person
had a long service leave credit" fails -- the text's no; s 2G (1) "period of service means" -- the text's no for an
unconnected employer; the dictionary "employee ... does not include" -- the text's no; s 13D (4) "Except with the consent
... not entitled" -- the text's no; the dictionary "continuous service ... includes" -- outside the list, NOTHING-kind.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 3 | employee | right (entitlement) | `s 3`, `s 4` questions |
| s 6 (1) | employer | duty to grant (offence) | `s 6 -- must my employer grant my leave` |
| s 6 (2) | employer | duty with deadline (offence) | DEONTIC `the employer must give 60 days' written notice` |
| s 8 (1) | employer | duty (offence) | `s 8 -- is the way I am paid ...` |
| s 11A (2), (4) | employer | duty with deadline (offence) | DEONTIC `the employer must pay the leave credit within 90 days` |
| s 11C (1) | employer | duty, no deadline, no offence | `s 11C` questions |
| s 12 (2) | employer | duty (offence) | `s 12 (2)` question |
| s 13D (4) | employee | no-right without consent | `s 13D` question |
| s 13E (2) | employer | duty with deadline (offence) | DEONTIC `the employer must comply with the notice within 28 days` |

## What the Act turns out to say

1. **s 4 and s 11A read literally would pay leave for any service.** s 4: leave "accrues at the rate of 1/5 of a month's
   leave for each year of service"; s 11A (1): the credit is the leave "that has accrued ... less the amount ...
   granted", payable when employment "ceases for any reason". Read alone, an employee leaving after 2 years would have a
   credit of 0.4 month, and s 11C (5 to 7 years, only for listed reasons) would be pointless. The encoding reads accrual
   as giving no leave before the 7-year entitlement in s 3 (fork F4). Asserted (s 11A, 6 years: 0).
2. **The s 2G example still speaks of 10 years.** "Her 10 years long service leave falls due on 1 October 2002": the
   entitlement now arises at 7 years (s 3 (1)), and the pro rata rule (s 11C (2)) still counts against 10 years and
   2 months. The arithmetic of the example is right for 10 years and is asserted; it no longer illustrates the first
   entitlement, which for Fiona would fall due on 1 June 1999 (7 years from 1 January 1992, plus the 5 months of
   absences before then; her injury absence from 1 August 1999 comes later).
3. **s 7 (2) multiplies hours by "the ordinary remuneration of the employee on that day".** That is meaningful only as an
   hourly rate; the encoding asks for the hourly rate.
4. **s 7 (3) gives a yearly amount.** "dividing by 5 the total amount of salary or wages paid ... in the period of 5 years"
   gives a year's pay, not a rate for the period of leave; the Act does not say how it is turned into pay for the leave
   (fork F7). It also uses salary or wages, not ordinary remuneration, so allowances and bonuses drop out.
5. **s 11A (3) points to s 7 but s 11D overrides it.** s 11A (3) pays what "would have been payable ... under section 7";
   s 11D then says the amount "shall be calculated" at the rate immediately before the employment ended, with
   part-time hours averaged over the last 12 months. The s 7 (3) averaging for a recent move to part-time is therefore
   not used on termination. The encoding follows s 11D.
6. **s 11C has no deadline and no offence.** s 11A (4) makes late payment of the leave credit an offence after 90 days;
   s 11C, the pro rata payment, says only that "the employer shall pay", with no time and no penalty.
7. **The Act does not say whether a review stops the 28 days.** s 13F and s 13G let the employer seek review of a notice
   to comply, but the Act does not say whether the requirement is stayed meanwhile; the s 13E question takes no account
   of a review.
8. **Months and weeks are mixed.** Leave is measured in months (s 4), the grant duty in weeks (s 6 (1) (a)), and pay by
   the week (s 2F, s 7 (2), s 11D (b)), with no conversion in the Act (forks F5, F8). Because the first entitlement is
   1.4 months, the 4-week test always holds when the entitlement first arises; it only matters once leave has been taken.
9. **s 13K cites a heading that does not exist.** It refers to "section 13F (Review of directions by registrar)"; s 13F is
   headed "Internal review by registrar". Not encoded (machinery); noted only.
10. **s 2D and s 2E speak of an employee who "was registered", s 2EA of one who "is registered".** The difference is
   not encoded; the question asks whether the employee was registered and elected.

## Before this is worth relying on

- The Legislation Act 2001 (ACT) for counting periods ("within ... after the day", "at least 60 days before"), for
  "month", and for moving a last day off a weekend or holiday (forks F1, F6, F11).
- A lawyer's view on forks F2, F3, F4, F5, F7, F8, F9 and findings 1, 4, 5; an independent test pass and a human gate.
- Fair Work Act 2009 (Cth) s 113 and the National Employment Standards, which keep state and territory long service leave
  laws but can be displaced by some pre-modern awards and agreements: not read here; s 14 is answered on the Act's own
  terms.
- Read with: the Long Service Leave (Portable Schemes) Act 2009 (ACT) subject beside this one (ss 2D, 2E, 2EA).
