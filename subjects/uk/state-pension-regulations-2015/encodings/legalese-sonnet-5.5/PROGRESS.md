# PROGRESS (State Pension Regulations 2015, S.I. 2015/173; run porridge-uk-spr)

Re-read this file, NOTES.md and the text (`../../registers/source-bundle/uksi-2015-173.txt`, 582 lines) after any compaction, not a summary.

## Method (decided before writing any L4)

- Single encoder, stable `l4` 1.6.98 (path and sha256 in encoding.json), `JL4_LIBRARY_PATH` unset.
- Quotes are expanded mechanically: a marker line `-- @@Q N-M` in a working `.l4` is replaced by `python3 -I srcrefs.py quote RAW N M`.
  The expander lives in the session scratchpad, not in the deposit.
- Probe files live in the session scratchpad (`spr-probe/`), never in the deposit.
- Libraries are embedded in the binary; `daydate` offers `Date d m y`, `add months`, `add years`, `Day`, `DATE_SERIAL`, `DATE_YEAR`.
  `days between` is NOT in daydate (it is in actus-daycount); subtract `DATE_SERIAL`s instead.
  `length` does not exist; `count`, `any`, `max`, `min`, `CEILING`, `FLOOR` do.
  A GIVEN with two parameters must put each on its own line (a comma after `LIST OF DATE` is a parse error).
- The brief names `references/drafting-patterns.md`, `references/source-patterns/` and `references/dialects.md` of writing-l4-rules; the SKILLS_DIR copy does not contain them (only builtins.md, gotchas.md, regulative.md).
  Recorded under peeked/limits in the final report.

## Module plan (flat folder, ASCII names, prefix spr-)

Layer 1 (the law, objectively):
- spr-nouns.l4 : shared nouns (MannerOfNotice, PaymentChoice, DeferralPeriod); declarations only, no test file
- spr-dates.l4 : YMD shim, last day of a period of days or months, tax-year helpers, days between, earlier of
- spr-part1-general.l4 : reg 1, 1A (including the commencement date)
- spr-part2-prisoners.l4 : regs 2, 3
- spr-part3-deferral.l4 : regs 4 to 12A
- spr-part4-qualifying-years.l4 : reg 13
- spr-part5-sharing.l4 : reg 14 and the Schedule (inserted regs 6 and 7 of the 2000 Regulations)
- spr-part6-graduated.l4 : regs 15 to 20
- spr-part7-overseas.l4 : regs 21 to 23
- spr-part8-credits-1.l4 : regs 24 to 28 (Chapters 1 and 2)
- spr-part8-credits-2.l4 : regs 29 to 33
- spr-part8-credits-3.l4 : regs 34 to 39
- tests: spr-tests-<module>.l4, expected values written from the text beside each assertion

Layer 2 (seat): spr-seat.l4, spr-cases-seat.l4.
Seat: a person who is, or will become, entitled to the State Pension, asking what these Regulations mean for when and how their State Pension is claimed, paid and affected by their choices.

## Status (update after every unit)

DONE. Both layers are written and the final checks pass.
Layer 1: spr-nouns, spr-dates, Parts 1/1A, 2, 3, 4, 5, 6, 7, 8 (three modules), each with a test file.
Layer 2: spr-seat.l4 (84 questions) and spr-cases-seat.l4 (420 assertions, at least one per question).
Final check.sh: 25 modules, 0 errors, 1050 assertions satisfied, 0 failed, 0 refused; srcrefs --refs: 423 src lines, 136 runs, 152 locators, 0 problems.
NOTES.md is complete (seat, jural relations, encoded and not, coverage table with every source line in one row, fork register F1 to F37, 24 numbered findings, binary limits, check.sh output, what to do before relying on it).
encoding.json and SOURCE-LICENSE.md are written.
Nothing remains except review by a person.
Tools (session scratchpad, not deposited): spr-tools/ holds the generators for the tests and the seat (gen_tests_part*.py, gen_seat.py, seat_p*.py, seat_findings.py), expand.py (quote markers), gate.sh, mutate.sh and gen_notes.py (NOTES.md).

## Files written

spr-nouns.l4, spr-dates.l4, spr-part1-general.l4, spr-part2-prisoners.l4, spr-part3-deferral.l4, spr-part4-qualifying-years.l4, spr-part5-sharing.l4, spr-part6-graduated.l4, spr-part7-overseas.l4, spr-part8-credits-1.l4, spr-part8-credits-2.l4, spr-part8-credits-3.l4,
spr-seat.l4, spr-cases-seat.l4,
spr-tests-dates.l4, spr-tests-part1.l4 to spr-tests-part7.l4 (Part 1 to Part 7), spr-tests-part8-credits-1.l4, spr-tests-part8-credits-2.l4, spr-tests-part8-credits-3.l4,
check.sh (skill asset plus a `written` column), srcrefs.py (skill asset), BRIEF.md (copy), NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md.

## Fork labels already used in code comments (each needs a NOTES.md entry)

F1 "N days starting with D" inclusive (D is day 1). F2 "N months starting on D": ends the day before the corresponding date; if no corresponding date, last day of the target month.
F3 tax year 6 April to 5 April, named by the starting calendar year. F4 whole days between dates by DATE_SERIAL.
F5 reg 2(2)(c)(ii) "(if any)": no certified release date means the condition is met.
F6 reg 3(1): whether a later described sentence reaches back over the remand period is not said; no recovery rule in the text.
F7 reg 2(4): "relevant benefits" undefined; what replaces reg 13 not said; only the stated effect (reg 13 does not have effect) encoded.
F8 reg 1(3) read literally: a survivor who reaches pensionable age before 6 April 2016 is outside regs 15 to 20, though 16(3), 18(1)(d)(ii) and 20(1)(c)(ii) speak of a person over pensionable age when the spouse died; both readings are visible, the literal one is taken (asserted in the seat cases, NOTES.md finding 1).
F9 reg 1(5) speaks of marriage only; a civil partner who is in a civil partnership with a third person is not addressed.
F10 reg 1A figure is that of the 2026-04-06 edition; no date range in the text.
F11 regs 4(4)(b), 6(2)(e): where no lump sum was paid, nothing to repay, so the repayment limb is met.
F12 reg 6(2)(e)(ii) "within the period mentioned in sub-paragraph (c)": the later end of (c)(i) and (c)(ii) taken.
F13 reg 8(2)(b) "not after 28 days starting with the date": latest permitted day is exercise date + 27 (F1).
F14 ss 17(3), (4) of the 2014 Act not in inputs: weeks = CEILING(counted days / 7); increase = 1/9 % x weeks x reference weekly rate.
F15 reg 12A: change dates given in date order; last modification period ends on the last day of the deferral; periods are day-inclusive.
F16 reg 12A: how the counted weeks are shared among modification periods is not said; weeks for each period are an input.
F17 reg 4(2)/(3): the notice that counts is the latest one issued before the choice; its "date" is the date printed in the notice.
F18 inserted reg 6(7): (a), (b), (c) are alternatives; the earliest that applies is taken; a court period later than three months does not extend time; (c) is for the court only.
F19 reg 18: a manner defect in a choice (reg 5) is treated as no choice, so the default (a lump sum) follows.
F20 regs 16, 18, 20: "under" and "over" pensionable age are strict; on the day the person reaches it they are neither, and the rules return a not-covered result.
F21 reg 17: overlap at R = 0 and S = F between the paragraphs (3)-(4) and (8)-(9); the paragraph with the full-rate percentage is taken first.
F22 reg 18(1): the date the person becomes entitled to make the choice is the later of reaching pensionable age and the spouse's death.
F23 regs 21(4), 21(5): "at the time of that increase" and "immediately before the up-rating increase comes into force" are the same moment.
F24 reg 23(3), (5): what the "increase or decrease" is measured against is not said; taken as the difference regulation 12A makes, supplied as a signed input.
F25 reg 21(2): whether regulations have been made applying regulation 21 to an up-rating increase is a plain input that gates the whole regulation.
F26 reg 21(4)(a): "in respect of the deferral period" is read as an increase that comes into force during it, both end days included.
F27 reg 22: a person who was an overseas resident but in Great Britain or a specified territory is in neither (2) nor (3); no reference rate is given.
F28 reg 25(1): the Chapter 2 / Chapter 3 line is drawn at the tax year starting 6 April 2016, matching regs 28(3) and 33(3); the 2014 Act definitions are not inputs.
F29 regs 28(4)(b), 30(3)(b), 33(4)(b), 37(8): "a woman ... an election made by her" is one input (the person is a woman with an election in force).
F30 regs 30(1)(b), 32(4)(a): the converter text carries a literal "..." where words are missing; the words that remain are encoded and quoted as they stand.
F31 reg 39(b): as written, a regulation 35 application must be received after the end of the year in which the week falls, with no latest date; read literally.
F32 reg 39(a)(i): "before the end of the year following that in which the week falls": receipt on the last day of that year counts as in time.
F33 reg 38: "a period of 12 weeks" is 84 days; the date taken is the date of becoming entitled (for "prior to") or the last day of the week in which entitlement or caring ceases (for "following").
F34 reg 39(a)(ii): "within such further time as ... consider reasonable" is a last day supplied by the person; receipt on or before it is in time; it adds to (i) and never shortens it.
F35 reg 35(4): while the carers have not agreed an election and the Secretary of State has not decided, the text says nothing; the result says so.
F36 reg 37(5), (8): paragraph (5) binds only a credit under (2)(a); a person within (2)(b) needs no application; a woman with an election in force needs none under (2)(a) either.
F37 reg 15(1): the condition that the dead spouse paid graduated contributions is not tested as a separate input (recorded in NOTES.md only; no comment in the code).
