# PROGRESS: piece cp6 (Part III, administration, lines 2628-3137 of the Act file)

Written as I go so that a compaction loses nothing.
Status words: DONE = written, run clean, tested; WRITTEN = written, not yet run clean; NEXT = not started.

## The range

Lines 2628-3137 of `R.S.C.-1985-c.-C-8.txt`: Part III heading (2628), ss 91 to 118, Schedule 1 (3101-3121) and Schedule 2 (3123-3136).
The section index lists ss 91 to 118 only; the two Schedules sit inside my range and are mine (they are cited by s 11.1(2), s 11.2 and s 113.1).
No enactment, assent or commencement date is in the range (checked: the only dates are "October 1", "January 1", "June 1" rules in ss 113.1 and 114 and the years in the Schedules).

## Method (so that I do not rediscover it after a compaction)

- L4_BIN is in the task; every command is `L4=<that path>`, run by absolute path, JL4_LIBRARY_PATH unset.
- Quote lines are made by `srcrefs.py quote`: I write `@@QUOTE N M` placeholders in a draft and expand them with an inline python call that runs `srcrefs.py quote RAW N M` (reads the file; nothing retyped).
- After each module: `l4 check`, `srcrefs.py check --refs RAW file`, then a `cp6-tests-<module>.l4` with hand-worked expected values; the count of `#ASSERT` lines must equal the count of "assertion satisfied".
- Rules are named `s N(x) — ...` (em dash) for the Act; helpers with no provision carry no prefix; types and constructors are specific phrases; types start `cp6 `.
- Duties are a yes/no "the duty arises" rule plus a DATE "last day" rule (the core's s 3(2) shape); no DEONTIC values.
- Fork ids are `C6-F<n>`; the list is below and must be copied into NOTES.md `## Fork register`.

## Modules (all flat in this folder)

| module | provisions | tests file | state |
| --- | --- | --- | --- |
| `cp6-interpretation.l4` | s 91; s 104(1), (2) | `cp6-tests-interpretation.l4` (37) | DONE |
| `cp6-administration.l4` | ss 92 to 94 | `cp6-tests-administration.l4` (17) | DONE |
| `cp6-record-of-earnings.l4` | ss 95 to 97 | `cp6-tests-record-of-earnings.l4` (66) | DONE |
| `cp6-social-insurance-number.l4` | ss 98 to 100 (101 inert) | `cp6-tests-social-insurance-number.l4` (87) | DONE |
| `cp6-offences.l4` | ss 102, 103 | `cp6-tests-offences.l4` (35) | DONE |
| `cp6-information.l4` | ss 104.1, 105, 106, 107 (107(3) inert) | `cp6-tests-information.l4` (76) | DONE |
| `cp6-accounts.l4` | ss 107.1 to 111.1, 118 | `cp6-tests-accounts.l4` (80) | DONE |
| `cp6-schedules.l4` | Schedules 1 and 2 | `cp6-tests-schedules.l4` (48) | DONE |
| `cp6-provinces-and-consent.l4` | ss 113, 114, 113.1(12) | `cp6-tests-provinces-and-consent.l4` (88) | DONE |
| `cp6-rates-review.l4` | s 113.1 | `cp6-tests-rates-review.l4` (138) | DONE |
| `cp6-statements-and-reports.l4` | ss 112, 115, 117 (and 115(1.1)(c) to (e), (1.1) contents) | `cp6-tests-statements-and-reports.l4` (92) | DONE |
| `cp6-seat.l4`, `cp6-cases-seat.l4` | layer 2: 57 questions | 122 case assertions | DONE |
| `NOTES.md` | all ten headings the brief names | | DONE (`## What check.sh prints` filled from the last run: 886 satisfied, 0 errors, 0 failed, 0 refused) |

## Decisions taken (with the provision that licenses each)

Fork register so far (copy into NOTES.md):

- C6-F1 s 95 "(a); (b); and (c)": the three purposes are alternatives (information needed for any one is kept), because the Record is the body of records that makes all three possible.
- C6-F2 s 97(1) "after four years have elapsed from the end of the year": 31 December of the fourth year after is still open; the next day is not.
- C6-F3 s 96(1) "Subject to ... any agreement entered into under section 105": NOTHING when an agreement governs (its terms are not read).
- C6-F4 s 97(2.1) says "paragraph 105(1)(a)", section 105 has no subsection (1): read as paragraph 105(a).
- C6-F5 s 98(2) "within thirty days after he reaches eighteen years of age or becomes employed ..., as the case may be": the thirty days run from the later of the two.
- C6-F6 ages in ss 98(2), 98(5) go through s 2(2) with `any other provision` (s 98 is not on the exception list): the first day of the month after the month of the eighteenth birthday.
- C6-F7 s 98(5) "the employer shall maintain a record of the Social Insurance Number of each employee": each employee the employer employs in pensionable employment (not only those to whom (2) applies).
- C6-F8 s 99(2)(b) when both later events have happened (becomes employed; first day payment is due): the earlier governs.
- C6-F9 "within thirty days of / after d": d plus 30 days; the text sets no earliest day for an application filed under s 98(1).
- C6-F10 the prescribed form and manner of the Social Insurance Number application: no Regulation among the inputs prescribes them (reg 88 only says the Minister may cause a number to be assigned); yes/no inputs through the core's s 2(1) "prescribed".
- C6-F11 s 99(1) "in the presence of two witnesses": at least two.
- C6-F12 s 103(1) "within, but not later than, five years after": the fifth anniversary is still in time; month-end clamping as in the core's F1.
- C6-F13 s 104.1(2) "any other person or body": a person or body other than a public officer of a body named in s 104.1(1).

- C6-F14 s 4(1)(a) names Part III: the Part III provisions about employees in pensionable employment (98(2), 98(5), 98(6), 99(2)) do not apply to employment in a province with a comprehensive plan unless s 4(2) applies.
- C6-F15 s 114(1) territories recognised by the names "Yukon", "the Northwest Territories", "Nunavut".
- C6-F16 s 114(2) "any notice": one notice year as input.
- C6-F17 whether s 114(4) reaches a regulation under 113.1(6): the text does not say; NOTHING.
- C6-F18 s 113.1(1) review periods begin in 1998 and every third year; (11.146) periods begin 2028, 2037, 2046, ...
- C6-F19 s 113.1(11.14) a tie rounds half up (the language's ROUND is half-even).
- C6-F20 s 115(1.1)(c) to (e) "combining" the (i) and (ii) rates is adding.
- C6-F21 s 113.1(11.05)(b)(ii) the self-employed rate is twice the employers' rate as rounded under (11.14).

Other decisions:

- Schedules are in my range (3101-3136) though the section index stops at s 118. Schedule 1/2 rates are fractions (`1.9%`); years outside the printed tables return NOTHING.
- Agreement-making powers (ss 100(1), 105, 107(1), 107(4), 111.1, 113(3)) are encoded as small yes/no rules, not inert; inert is kept for regulation-making powers (s 101(1)(a) to (e), s 107(3), s 113.1(6), s 113.1(11.144), s 113.1(14)) and the Statutory Instruments Act exemption (s 113.1(9)), the s 91 "Investment Board" citation and headings.
- Regulations among the inputs touch Part III in four places only: reg 37(4) (prescribed individual for "public officer", piece cr2), reg 39 and 40 (application for a statement under s 96(1); notice of a reduction under s 97(4), piece cr2), reg 88 (Minister may cause a number to be assigned, piece cr1). All are taken as inputs.

## Files written

Layer 1: cp6-schedules.l4, cp6-interpretation.l4, cp6-administration.l4, cp6-record-of-earnings.l4, cp6-social-insurance-number.l4, cp6-offences.l4, cp6-information.l4, cp6-accounts.l4, cp6-provinces-and-consent.l4, cp6-rates-review.l4, cp6-statements-and-reports.l4, and a cp6-tests-<module>.l4 for each (eleven).
Layer 2: cp6-seat.l4, cp6-cases-seat.l4.
Reports: NOTES.md, PROGRESS.md.
Scratch outputs went to the session scratchpad only; no probe file is left in this folder.

## State at the end of the 2026-10-24 run

All files in the list above are written. `check.sh` printed 886 satisfied, 0 errors, 0 failed, 0 refused over 29 modules; `srcrefs.py check --refs` printed 0 problems; `l4 check` on each of the 24 `cp6-*.l4` files printed `Check succeeded`. The final report to the lead was sent after this file was written.
