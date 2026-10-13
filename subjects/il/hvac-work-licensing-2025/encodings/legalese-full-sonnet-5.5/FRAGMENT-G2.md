# FRAGMENT-G2: sections 6 to 9 and the Second Schedule of the Regulation of Engagement in Work on Refrigeration or Air-Conditioning Systems Law 5785-2025

Written by ENCODER G2.
Status: draft; no domain expert has read any of this against the Law.
Every claim below was checked against the files in `deposit/` on the day it was written (the `check.sh` output in section 9 is the one run the numbers come from).
The Hebrew in the modules is copied by script from `inputs/law.wiki` (`srcrefs.py quote`), and `srcrefs.py check --refs` over every module reported 0 problems.
The Wikisource text and the gazette (Sefer HaChukim 3349, pp. 183 to 205) were compared by reading the page images and by bag of words; they agree in ss. 6 to 9 and in the Second Schedule, with the two exceptions in section 6, items C14 and C15.

## 0. Modules and tests

| file | what it holds |
| --- | --- |
| `g2-validity.l4` | s 8 (the validity period; both limbs), the register's last day of validity, `the licence is in force on` a day (IP1, IP19), the s 17(c) extension helper (trap T25) |
| `g2-second-schedule.l4` | the Second Schedule as data (17 items, Parts A to C, columns A, B and C), the readings of the Schedule as data, and the engine that says which items apply to an application (IP6) |
| `g2-conditions.l4` | s 6: (a) the Registrar's duty, (1) to (3), (4) and its three limbs, (b) the Minister's power |
| `g2-exemption.l4` | s 7: the Director's two powers to exempt and the duty to publish |
| `g2-temporary-licence.l4` | s 9: the foreign expert's conditions, the one-year term, the two renewals |
| `g2-renewal.l4` | s 8's second limb (renewal on the conditions of s 6 except (a)(4)) and `the conditions of the licence still hold` (IP18); not in PLAN: it needs g2-conditions and g2-temporary-licence, which g2-validity cannot import |
| `g2-tests-fixtures.l4` | named people, applicants, applications, licences and experts; no assertion |
| `g2-tests-validity.l4`, `g2-tests-second-schedule.l4`, `g2-tests-conditions.l4`, `g2-tests-exemption.l4`, `g2-tests-temporary-licence.l4`, `g2-tests-renewal.l4` | the tests; every expected value was decided from the Hebrew and the readings registered (dates by the Python calendar, `work/g2/oracle.py`), not copied from output; the first suite was written before any module ran, and the tests of FC2, FC7, FS9 and the reading guards were added afterwards, from the stated readings |
| `g2-tests-red.l4` | 44 expectations that are MEANT to fail: each asserts, as if it were the answer, a reading this group did not take (eight of them are old green assertions moved here by the D1 repair, below); check.sh must report exactly 44 failures for it |

Imports.
Every module imports only `prelude`, `daydate`, `il-interpretation-time`, `domain` and modules of this group.
The within-group imports are a departure from the letter of line 17 of the assignment ("imports only prelude, daydate, il-interpretation-time and domain") and are permitted by ruling 1, whose heading is "no cross-group imports".
The order is `g2-validity` <- `g2-second-schedule` <- `g2-conditions` <- `g2-temporary-licence` <- `g2-renewal`; `g2-exemption` imports only prelude, daydate and domain.
No module of another group is imported anywhere.
The tests import the module under test, as they must.

Defects found after delivery, and repaired.
Defect D1 (found 2026-10-13 by the independent test author, an Opus agent that decided its expected values from the source before opening these modules, and checked by the fleet lead against the table; repaired 2026-10-14 by ENCODER G2).
An adult citizen and resident with a clean record, an approved programme and the fee paid, who already holds the Training Division final certificate of the grade sought (a grade 3 certificate, applying for a grade 3 licence), was answered by `training required for the licence sought` with item C6 (up to 200 hours more) and by `the Registrar must grant the licence` with FALSE when the training inputs were FALSE; the same one grade down gave A3 (up to 50 hours) and B5(1) (up to 50 hours).
I had seen it and filed it as contradiction C5 and as the narrow alternative FC7, but TOOK the literal reading; the defect is that the taken reading was the wrong one.
The ruling is that item 1 of each Part ("training of up to 350/480/720 hours conferring a final certificate of grade 1/2/3 from the Training Division") is the way to the licence, so whoever holds the certificate that course confers has completed it and has met item 1, and rows A3, B5(1) and C6 are for the holder of the lesser, ungraded certificate.
Repair: fork FS10 in the engine of `g2-second-schedule.l4` (so that the exported IP6 answer and the duty agree), with the literal reading kept as a callable alternative, and fork FS11 for the certificate of a higher grade (sections 2.2 and 6, C5).
No exported name or signature changed (section 5); the answers for the discriminating applicant did.
Eight old green assertions that stated the literal reading as the answer were moved, unchanged, to `g2-tests-red.l4`; two old red assertions that now hold (the FC2 and FC7 lines) were moved, unchanged, into the green tests; section 9 has the counts.
Defect D2 (same finder and date): `s 17(c) — the last day of validity` ... `extended by` n `months` refused an extension of half a month, which s 17(c) ("not exceeding three months") allows.
Repair: the months form keeps whole months from one to three, because Interpretation Law s 10(b) fixes the last day of a period of months only for whole months, and now says so in its refusal; a part of a month is stated as a day with the new `s 17(c) (to a stated day) — the last day of validity` ... `extended to` ... (section 2.1, FV7).

How the work was checked.
`check.sh` (section 9) reads diagnostics, not exit codes, and counts warnings as red.
A mutation check (`work/g2/mutate.py`, 47 single-edit mutations of the modules, each run against its test module in a scratch copy: the 38 of the first delivery, one of them retargeted at the engine's helper after the repair, and nine added with it for FS10, FS11 and the day form of s 17(c)) caught every one; the harness reports a mutation whose anchor no longer matches as SKIP, not as caught, and one did after the repair (its anchor was fixed and it was run again).
One mutation was deliberately not written because it is equivalent: removing the whole-number test from the months form of s 17(c) changes only the message, since the vendored time module refuses a fractional number of months itself.
Every figure of the encoding was compared with the Hebrew by script (`work/g2/verify_numbers.py`: 118 comparisons, 0 mismatches; the checker's one layout-dependent test of the s 17(c) window was split in two after the repair, and now also compares the day form's three months with the Hebrew), and the wiki against the gazette by bag of words (`work/g2/bagdiff.py`: no word of the wiki's ss. 6 to 9 or Second Schedule is missing from the gazette pages).
One expectation was written wrongly and corrected before the code's answer was looked at: the items of the Schedule with three column A entries are 3, 5, 3, 4 (Part B items 3 and 5, Part C items 3 and 4), and the first draft said 3, 3, 5, 3, 3.
Deontic rules (`MUST`, `MAY`) cannot be compared with `EQUALS`, so they are exercised with `#TRACE`: the traces were read by hand and are described in section 3; what check.sh asserts is the boolean that triggers each of them.

Peeked.
Nothing from `commons/`, `commonswt/`, `canon/`, `il/` or any other encoding, and nothing from `~/.claude/` beyond the two skills.
Two things outside the brief's read list were touched and are disclosed: I listed the directory names (not the contents) of `FLEET_DIR/work/` and `FLEET_DIR/work/surveyor/`, and I listed `jl4-core/libraries/` and grepped `prelude.l4` there for the names of list functions (the standard library, not an encoding of this subject).
My context also carried an index of someone's notes that mentions this subject; I did not follow it.
After a context compaction the harness restored into my context the text of four files that I did not open myself (my own transcript has no Read call for any of them): a README and an `encoding.json` under a `commonswt/` checkout of this subject's other encodings, a brief of the Interpretation Law run under a sibling scratch directory, and a memory note about this subject.
I did not use that text and changed no file in the deposit because of it; the deposit was complete and checked before it arrived, and every change since is the D1/D2 repair, which comes from the lead's message and the Schedule's own rows.
The lead may want to know that the restore exposed cleanroom material.
I also ran a mechanical name-clash check for ruling 5 (`work/g2/clash_check.py`): it read the identifier text at definition positions of the other groups' non-test modules (`g[1345678]-*.l4`) and nothing else, and printed only identifiers that coincide with mine.
It found one real clash, `the licence` (the head of my first spelling of the in-force function, which also occurs in group G3's module), and I resolved it by renaming my export to `the licence is in force on`, the name PLAN proposed.
The other hits were mixfix segments (`and`, `by`, `to`, `, with`) and two names that are `GIVEN` names in my modules (`the Knesset Labour and Welfare Committee approved the order`, `the last day of validity`); I did not open those lines of the other groups' files to see how they use them, and neither is a clash under ruling 5 if they are inputs there too.

## 1. Coverage

44 rows, in the Law's own numbering.
By disposition: 41 `encoded`, 3 `inert`, 0 `refused`, 0 `out-of-scope`, 0 `deferred`.
One disposition differs from `slice-G2.md`: s 6(b) is `encoded` and not `inert`, by ruling 2 (a power is encoded as a `MAY` rule with its procedural precondition, the committee's approval, as a computable condition; the content of an order is not modelled, the Second Schedule as enacted being the only vintage).
The three `inert` rows are the Part headings S2.A, S2.B and S2.C: each is carried as a quotation of its own line of the wiki, and the fact it states (which licence kind the Part leads to) is the field `the part: the licence kind it leads to` of every item of the Part; the heading imposes nothing.
The container rows 6, 7 and 9 have no text of their own beyond their headings; they are the `§` headings of their modules.

| id | provision | disposition | module | rule or datum |
| --- | --- | --- | --- | --- |
| 6 | s 6, conditions for granting a licence | encoded | g2-conditions | the `§ Section 6` heading and the rules below it |
| 6(a) | the Registrar shall grant a licence to an applicant who meets all of (1) to (4) | encoded | g2-conditions | `s 6(a) — the Registrar must grant the licence` (the duty); `s 6(a) — the conditions (1) to (4) all hold`; `the Registrar must grant the licence` (exported boolean) |
| 6(a)(1) | the applicant is an adult | encoded | g2-conditions | `s 6(a)(1) — the applicant is of full age` |
| 6(a)(2) | an Israeli citizen or resident | encoded | g2-conditions | `s 6(a)(2) — the applicant is an Israeli citizen or resident` |
| 6(a)(3) | no conviction or pending indictment that, in the Registrar's opinion, makes the applicant unfit | encoded | g2-conditions | `s 6(a)(3) — no disqualifying conviction or pending indictment` |
| 6(a)(4) | one of three training routes, in accordance with the Second Schedule | encoded | g2-conditions | `s 6(a)(4) — one of the training routes holds, in accordance with the Second Schedule`; `Second Schedule — the requirement for the licence sought is met` |
| 6(a)(4)(a) | holds a final certificate | encoded | g2-conditions | `s 6(a)(4)(a) — the applicant holds a final certificate`; `s 2 — the certificate counts as a final certificate` (stand-in for G1's test) |
| 6(a)(4)(b) | registered in the register of technicians and practical engineers | encoded | g2-conditions | `s 6(a)(4)(b) — the applicant is registered as a technician or practical engineer in refrigeration and air conditioning` |
| 6(a)(4)(c) | completed complementary studies, if column B requires them | encoded | g2-conditions | `s 6(a)(4)(c) — the applicant completed the complementary studies, if required` |
| 6(b) | the Minister, with the Knesset committee's approval, may change the Second Schedule | encoded (was `inert`; ruling 2) | g2-conditions | `s 6(b) — the Minister may change the Second Schedule by order` |
| 7 | s 7, exemption from training | encoded | g2-exemption | the `§ Section 7` heading and the rules below it |
| 7(a) | the Director may exempt a holder of a valid electrician licence from the electricity chapter | encoded | g2-exemption | `s 7(a) — the Director may exempt the applicant from the electricity chapter of the training`; `s 7(a) — the applicant holds a valid electrician licence of a listed kind` |
| 7(b) | the same for a valid working-at-height approval | encoded | g2-exemption | `s 7(b) — the Director may exempt the applicant from the working-at-height chapter of the training`; `s 7(b) — the applicant holds a valid working-at-height approval` |
| 7(c) | the Director must publish the instructions for applying for an exemption | encoded | g2-exemption | `s 7(c) — the Director must publish the instructions for applying for an exemption` |
| 8 | validity (five years or until 31 March of the fifth year, whichever is earlier) and renewal on the conditions of s 6 except (a)(4) | encoded | g2-validity; g2-renewal | `s 8 — the last day of the validity period beginning on`; `s 8 — the last day of validity of the licence`; `the licence is in force on`; and, for the renewal limb, `s 8 — the licence can be renewed for the applicant` |
| 9 | s 9, temporary licence for a foreign expert | encoded | g2-temporary-licence | the `§ Section 9` heading and the rules below it |
| 9(a) | the Registrar may, notwithstanding ss 6 and 8, give a temporary grade 3 licence for up to one year to a foreign expert meeting (1) to (3) | encoded | g2-temporary-licence | `s 9(a) — the Registrar may grant a temporary licence`; `s 9(a) — the applicant is a foreign expert meeting conditions (1) to (3)`; `s 9(a) — the latest last day of a temporary licence granted on`; `the temporary licence may be granted` (exported boolean) |
| 9(a)(1) | invited to Israel to work on a system above 70 kW | encoded | g2-temporary-licence | `s 9(a)(1) — the expert was invited to work on a system above 70 kW` |
| 9(a)(2) | authorised abroad; installed or maintained similar systems in the six preceding years | encoded | g2-temporary-licence | `s 9(a)(2) — the expert is authorised abroad and did similar work in the six preceding years` |
| 9(a)(3) | recognised by the Registrar as of repute and a renowned expert | encoded | g2-temporary-licence | `s 9(a)(3) — the Registrar recognised the expert as of repute and renowned in the field` (an input) |
| 9(b) | the Registrar may renew for two further periods of up to one year each | encoded | g2-temporary-licence | `s 9(b) — the Registrar may renew the temporary licence`; `s 9(b) — the latest last day of a term renewing one that ended on`; `s 9(b) — the number of renewals still open to the temporary licence` |
| S2.A | Part A heading, grade 1 licence | inert | g2-second-schedule | quotation of line 566, carried with item A1 |
| S2.A.1 | item 1: no prior training or experience | encoded | g2-second-schedule | `Second Schedule, Part A, item 1` |
| S2.A.2 | item 2: prior experience | encoded | g2-second-schedule | `Second Schedule, Part A, item 2` |
| S2.A.2/colC | the three-year note | encoded | g2-second-schedule | field `column C: valid for three years from the commencement day` of item A2; `Second Schedule column C — the last day of the three years beginning on`; `Second Schedule column C — the experience items are in force on the day` |
| S2.A.3 | item 3: a Training Division certificate | encoded | g2-second-schedule | `Second Schedule, Part A, item 3` |
| S2.B | Part B heading, grade 2 licence | inert | g2-second-schedule | quotation of line 594, carried with item B1 |
| S2.B.1 | item 1: no prior training or experience | encoded | g2-second-schedule | `Second Schedule, Part B, item 1` |
| S2.B.2 | item 2: registered technician with the programme | encoded | g2-second-schedule | `Second Schedule, Part B, item 2` |
| S2.B.3 | item 3: grade 1 licence, grade 1 certificate or 3 units | encoded | g2-second-schedule | `Second Schedule, Part B, item 3` |
| S2.B.4 | item 4: prior experience | encoded | g2-second-schedule | `Second Schedule, Part B, item 4` |
| S2.B.4/colC | the three-year note | encoded | g2-second-schedule | as S2.A.2/colC, on item B4 |
| S2.B.5 | item 5: a Division certificate, a youth school certificate or 5 units | encoded | g2-second-schedule | `Second Schedule, Part B, item 5` |
| S2.B.6 | item 6: registered technician | encoded | g2-second-schedule | `Second Schedule, Part B, item 6` |
| S2.C | Part C heading, grade 3 licence | inert | g2-second-schedule | quotation of line 641, carried with item C1 |
| S2.C.1 | item 1: no prior training or experience | encoded | g2-second-schedule | `Second Schedule, Part C, item 1` |
| S2.C.2 | item 2: registered practical engineer with the programme | encoded | g2-second-schedule | `Second Schedule, Part C, item 2` |
| S2.C.3 | item 3: grade 1 licence, grade 1 certificate or 3 units | encoded | g2-second-schedule | `Second Schedule, Part C, item 3` |
| S2.C.4 | item 4: grade 2 licence, grade 2 certificate or 5 units (240 hours, column B per the gazette) | encoded | g2-second-schedule | `Second Schedule, Part C, item 4`; the wiki's layout is `Second Schedule, Part C, item 4, as the wiki prints it` |
| S2.C.5 | item 5: prior experience | encoded | g2-second-schedule | `Second Schedule, Part C, item 5` |
| S2.C.5/colC | the three-year note | encoded | g2-second-schedule | as S2.A.2/colC, on item C5 |
| S2.C.6 | item 6: a Division certificate | encoded | g2-second-schedule | `Second Schedule, Part C, item 6` |
| S2.C.7 | item 7: registered practical engineer | encoded | g2-second-schedule | `Second Schedule, Part C, item 7` |
| S2.C.8 | item 8: registered engineer, mechanical branch | encoded | g2-second-schedule | `Second Schedule, Part C, item 8` |

## 2. Forks

Each fork gives the readings, the one taken, the text that licenses each, the callable alternative and the test that exercises it.
"Test" names the test module; every alternative below is asserted TO HOLD in its own module (so it is a working function, not a comment), and each reading not taken is asserted as the answer, and fails, in `g2-tests-red.l4`.
Nothing here is ruled by the owner; every choice is assumed, and each is meant to be reverted alone.

### 2.0 The kinds of period (brief ruling 4)

| kind | where it occurs in this scope | fork |
| --- | --- | --- |
| V, a period of validity | s 8 limb 1 (five years); s 9(a) (the term of a temporary licence); s 9(b) (each renewal); s 17(c)'s extension of up to three months | IL s 10(c) NOT applied, alternative callable: FV2 (s 8), FT2 (s 9(a)), FT3 (s 9(b), counted from the day of renewal), FV7 (s 17(c)) |
| C, a commencement date counted from another date | the three-year note of the Second Schedule (A2, B4, C5), counted from the commencement day of s 63(a)(1) | IL s 10(c) NOT applied, alternative callable: FS8; the commencement day is an input, never hard-coded |
| B, counted backwards | the experience tests of A2, B4, C5 (one year within three, three within seven); s 9(a)(2) (the six preceding years) | outside IL s 10, which speaks of periods from a day or after an event; plain date comparison; FS7, FT4 |
| R, a recurring calendar date | s 8 limb 2, 31 March | not a period; IL s 10(c) has nothing to act on there (FV2's alternative applies (c) to limb 1 only) |
| D, a deadline for doing something | none: ss 6 to 9 and the Second Schedule state no deadline (s 6(a) and s 7(c) state none; no `WITHIN` is invented) | none |
| W, a window for an application or request | none: the time for a renewal application is left to a regulation under s 60(2)(a) (group G7) | none |

### 2.1 Section 8 and the register (g2-validity)

**FV1 (trap T24; kind R and V).**
Readings: the fifth year "from the year in which the licence was granted" is (taken) the year of grant plus five, or (alternative) the year of grant plus four.
Text: s 8, line 100 of `law.wiki` ("until 31 March of the fifth year from the year in which the licence was granted, whichever is earlier"), quoted by script in the module.
Why the one taken: under year plus four the 31 March limb is always earlier than five years (the five-year anniversary falls in year plus five), so "whichever is earlier" would have no work to do and limb 1 would be dead; under year plus five a grant on or before 31 March has limb 1 earlier and a later grant has limb 2 earlier, so both limbs of the Law's own words can govern.
The words "from the year" also point away from the year of grant, which supports counting it as year zero.
Discriminating grants: 1.2.2026 gives 1.2.2031 (taken) or 31.3.2030 (alternative); 1.6.2026 gives 31.3.2031 or 31.3.2030.
Alternative: `s 8 (the year of grant counted as the first year) — the last day of the validity period beginning on`.
Test: `g2-tests-validity.l4`, block "the two limbs".
Changes an answer: on every grant.

**FV2 (kind V).**
Readings: IL s 10(c) is not applied to a validity period (taken); or it is applied to the five-year limb, 31 March being a date and not a period.
Alternative: `s 8 (Interpretation Law s 10(c) applied to the five year limb) — the last day of the validity period beginning on` d `, with` a calendar of rest days.
Test: `g2-tests-validity.l4`: the five-year limb ending Saturday 1.2.2031 moves to Monday 3.2.2031 with Saturday and Sunday rest, to Sunday 2.2.2031 with only Saturday rest, and stays with none.
Changes an answer: whenever limb 1 ends on a rest day.

**FV3 (P3; kind V).**
Readings: for a renewed licence each renewal begins a further validity period counted from the renewal day under the same two limbs (taken); or each further period continues from the day after the previous one ends.
Text: s 8 says "further validity periods" and not from when; "the year in which the licence was granted" is read, for a further period, as the year that period was granted.
Alternative: `s 8 (each further period continues from the end of the previous one) — the last day of validity of the licence`.
Test: `g2-tests-validity.l4`: a licence granted 1.2.2026 and renewed on 15.6.2030 ends 31.3.2035 (taken) or 2.2.2036 (alternative); with a second renewal on 10.4.2035, 31.3.2040 or 3.2.2041.
Also: renewals are taken to be made before the previous period ran out; the latest of the grant and renewal days is taken by comparison, so an out-of-order list does no harm.

**FV4.**
Readings: a licence is valid from the day it was granted, inclusive (taken); or from the day after (the time module's `first day of a period counted from or after an event`).
Alternative: `s 8 (validity begins the day after the grant) — the licence ... is within its period of validity on`.
Test: `g2-tests-validity.l4`: on the grant day the licence is in force (taken) or not.

**FV5.**
Readings: the register's recorded last day (`validity ends on, as recorded`) governs where there is one (taken), which is how an extension under s 17(c) reaches s 8 (integration point IP19); or the Law alone governs and the register is evidence.
Alternative: `s 8 — the last day of validity of the licence, by the Law alone` and `s 8 (the Law alone) — the licence ... is within its period of validity on`.
Test: `g2-tests-validity.l4`: a licence granted 1.2.2026 whose register records 30.4.2031 is in force on 30.4.2031 (taken) and not on the Law alone (the Law gives 1.2.2031).
A temporary licence's term is the Registrar's choice, so for a temporary licence with no recorded last day the answer is a named refusal (`the Law fixes no last day for a temporary licence and the register records none`).

**FV6.**
Readings: a recorded revocation or suspension takes effect on the day recorded (taken), or on the day after.
Text: s 10 (group G1) says nothing of when a decision takes effect; the register carries `revoked on`, `suspended from`, `suspended until`.
Alternative: `the licence is in force on, a revocation or suspension taking effect the day after`.
Test: `g2-tests-validity.l4`: revoked on 1.5.2028, in force on 30.4.2028 and not on 1.5.2028 (taken) or on 1.5.2028 (alternative); a suspension with no last day (until final judgment, s 10(b)) never ends.

**FV7 (trap T25; kind V).**
Readings: an extension "not exceeding three months" under s 17(c) runs on from the last day of validity even where that passes 31 March (taken); or it is capped at the 31 March limb of the period it extends.
Why the one taken: an extension that could not pass the end the Law gave would be no extension where the 31 March limb governs.
Alternative: `s 17(c) (capped at the 31 March limb) — the last day of validity`.
Test: `g2-tests-validity.l4`: three months after 1.2.2031 end on 1.5.2031 (taken) or 31.3.2031 (capped); the licence is in force on 1.4.2031.
s 17(c) itself (who may extend, and when) belongs to group G3; this module owns only how the extension meets s 8.
Part of a month (defect D2, repaired 2026-10-14): the months form takes a whole number of months, one to three, because Interpretation Law s 10(b) fixes the last day of a period of months only for whole months, and it refuses 0, a negative number, a fraction (0.5, 1.5, 2.5) and more than three, with a message that names the day form; a part of a month is stated as a day with `s 17(c) (to a stated day) — the last day of validity` d `extended to` e, which accepts any day after d up to the last day of three months after d and refuses any other.
Test: `g2-tests-validity.l4`: 0.5, 1.5, 2.5, 3.5, 0 and -1 months refused; 15.2.2031 and 2.2.2031 accepted from 1.2.2031; 1.5.2031 accepted, 2.5.2031, 1.2.2031 and 31.1.2031 refused; 30.6.2031 accepted and 1.7.2031 refused from 31.3.2031; a licence extended to 15.2.2031 is in force on that day and not on the next.

### 2.2 The Second Schedule (g2-second-schedule)

The readings of the Schedule are fields of one record, `Reading of the Second Schedule`, and the alternative is the same engine called with another value: `Second Schedule — the items that apply under` reading `to` application `with commencement day` d.
Each named alternative is a constant (`the reading with ... (FSn)`); `g2-tests-second-schedule.l4` asserts that each differs from the reading taken in exactly one field.

**FS1 (trap T1).**
Provisions: B3(2), C3(2), C4(2) name a certificate by grade; B5(1), A3, C6 name "a certificate in refrigeration and air-conditioning studies from the Training Division", with no grade.
Readings: the ungraded entry covers every Training Division certificate that no graded entry of the same Part names (taken: graded over general, so no Division certificate is in two items and each graded item keeps its purpose); or the ungraded entry covers every Division certificate of any grade (the literal text).
Discriminating applicants: a grade 1 certificate seeking grade 2 (B3: up to 100 hours, taken; B3 and B5(1): 100 and 50, alternative); seeking grade 3 (C3: 290; or C3 and C6: 290 and 200); a grade 2 certificate seeking grade 3 (C4: 240; or C4 and C6: 240 and 200).
One exception, since the D1 repair: the Division certificate that item 1 of the Part itself confers is not a column A entry of the ungraded rows on either branch of this fork (FS10 below).
Alternative: `the reading with the ungraded certificate rows reaching every grade (FS1)`.
Test: `g2-tests-second-schedule.l4`, Parts B and C blocks.

**FS2 (trap T2).**
Provisions: item 1 of each Part is headed "no prior training or experience", yet item 1 of Parts A and B has a certificate as its option (2), which is prior training; a 5-unit certificate is item 1(2) of Part B (nothing more required) and item 5(3) of Part B (up to 50 hours).
Readings: item 1 is the default item of its Part, applying to an applicant no other open item of the Part fits (taken); (a) item 1 applies only to an applicant with no prior training or experience at all; (b) item 1 also applies to the holder of a certificate its own column B names.
Why the one taken: the heading of item 1 cannot be literal, because its own option (2) is a certificate; and a Schedule that gave nothing to an applicant with partial experience or an unlisted qualification would leave a gap the Law cannot have meant.
Consequences on the reading taken: A1(2) works (no other item of Part A fits a 3-unit holder); B1(2) is reached by nobody, because B5(3) always fits the 5-unit holder; after the three-year note lapses an experienced applicant falls to item 1.
Alternatives: `the reading with item 1 only for applicants with no prior training or experience at all (FS2a)` (the 3-unit holder seeking grade 1 is then in no item at all, and 364 days of experience also puts an applicant in no item); `the reading with item 1 also open to the holder of a certificate its column B names (FS2b)` (the 5-unit holder seeking grade 2 is in B1 and B5).
Test: `g2-tests-second-schedule.l4`, Parts A and B blocks.

**FS3 (trap T3).**
Provisions: B2 and B6 (C2 and C7) both name registration as a technician (practical engineer); B2 (C2) adds the completed programme including the complement course.
Readings: the registration-alone item reaches the registered applicant who did not complete the programme (taken: the pair partitions on the programme, in line with s 6(a)(4)(b) and (c)); or it reaches every registered applicant (the literal text), so a technician with the programme is in B2 and B6.
Alternative: `the reading with registration alone reaching every registered applicant (FS3)`.
Test: `g2-tests-second-schedule.l4`: Part B and Part C; a technician with the programme, one without, and the programme without the registration.

**FS4 (trap T5).**
Part B heads column B "training or complementary studies required"; Parts A and C head it "requirements for the licence sought".
The encoding reproduces column B as printed in every Part, so the table's answers do not depend on the heading; what the heading changes is what s 6(a)(4)(c)'s "complementary studies, if required in column B" refers to (in Parts A and C there is no column B of complementary studies).
No alternative function is needed or possible: both readings return the same column B.

**FS5 (trap T6).**
Readings: "training of up to N hours" is a ceiling on the course the Training Division runs, and the hours the applicant must complete are not stated (taken); or it is exactly N.
Alternative: `Second Schedule (up to N read as exactly N) — the hours the applicant must complete under`; the function taken is `Second Schedule — the hours the applicant must complete under`, a named refusal for a course and 0 for "no further requirement" and "the certificate itself".
Test: `g2-tests-second-schedule.l4`, block "column B, the hours".

**FS6 (trap T4; wiki against gazette).**
The wiki puts the sentence "training of up to 240 hours" of Part C item 4 in column A, behind a stray opening bracket, and leaves column B empty; the gazette (p. 204, page image) puts it in column B.
Taken: the gazette, which governs.
Alternative: `the Second Schedule with Part C item 4 as the wiki prints it` and `Second Schedule (Part C item 4 as the wiki prints it) — the items that apply to`: column B states nothing, and `Second Schedule — the requirements in column B of` gives a named refusal for it.
Test: `g2-tests-second-schedule.l4`.
Also noted: the wiki's column B of A3 stops one word short of the gazette's (p. 201); no legal effect.

**FS7 (kind B, outside IL s 10).**
(a) "a year of cumulative experience" is a number of days: taken 365, so "three years" are 1095; alternative `the reading with a year of cumulative experience counted in days (FS7a)` n.
(b) The window ends the day before the application ("before the filing of the application"): taken; alternative counts the application day.
(c) Overlapping periods of work are counted once (taken); alternative adds them.
The window starts on the same calendar date N years before the application, rebuilt from its components (a 29 February start rolls to 1 March); no `add years` is used.
Periods are clipped to the window before they are counted.
Discriminating cases (application 1.9.2026): 365 days from 1.9.2025 qualify for A2, 364 do not; a period 31.8.2023 to 29.8.2024 is 365 days but 364 inside the window; a period ending on the application day counts one day less; two overlapping periods give 303 days counted once and 484 added; 1095 days in 2020 to 2022 qualify under (2), 1094 do not.
Test: `g2-tests-second-schedule.l4`, Part A block.

**FS8 (kind C; P9; trap T7).**
The three-year note on A2, B4 and C5: "this provision shall stand for three years from the commencement of this Law, as stated in s 63(a)(1)".
Taken: three years after the commencement day (an input DATE, IP2) by IL s 10(b), the last day inside the period; with a commencement day of 16.7.2025 the last day is 16.7.2028 (a Sunday); the commencement day itself is a day on which the items are in force (the time module's `first day of a period counted from or after an event`, the day after, is NOT used here: it would make the items not in force on the commencement day); IL s 10(c) is not applied; tested on the application day.
Alternatives: IL s 10(c) applied (`Second Schedule column C (Interpretation Law s 10(c) applied) — the last day of the three years beginning on`: with Sunday 16.7.2028 a rest day, 17.7.2028); the note tested on the day of decision (`Second Schedule (the three-year note tested on the day of decision) — the items that apply to`); another anchor, the later commencement of s 63(a)(2) (the same date function called with that date: `Second Schedule column C — the last day of the three years beginning on` 16.1.2027 gives 16.1.2030).
Why the anchor fork: for systems with a refrigerant other than a listed flammable one the licensing duty starts 18 months after the commencement day (s 63(a)(2)), so on the text's anchor the experience route is open for about 18 months after the duty bites for them.
The text names s 63(a)(1), so that is the reading taken; an `Application` carries no system, so the s 63(a)(2) anchor can only be supplied as a date by the caller.
Test: `g2-tests-second-schedule.l4`, block "the three-year note".
A pending application that is decided after the note lapsed is the day-of-decision fork; the Law does not say.

**FS9.**
"A grade 1 licence" in column A of B3(1), C3(1), C4(1): taken, a licence in force on the day of the application (the Schedule does not say that a lapsed, revoked or suspended licence counts); alternative `the reading with a licence named in column A counting although it has lapsed (FS9)`.
Test: `g2-tests-second-schedule.l4`: a licence granted 1.1.2018 ended 1.1.2023.

**FS10 (the Division certificate of the grade sought; defect D1; repaired 2026-10-14).**
Provisions: item 1 of Part A, B, C, column B: "training of up to 350, 480, 720 hours conferring a final certificate of grade 1, 2, 3 from the Training Division"; A3, B5(1), C6, column A: "a certificate in refrigeration and air-conditioning studies from the Training Division", with no grade; s 6(a)(4)(a): a holder of a final certificate.
Readings: the holder of the certificate of the grade sought (grade N for a licence of grade N) has completed the course of item 1 and has met it, so nothing further is asked (taken); or that certificate is only an ordinary column A entry, graded over general puts its holder in the ungraded row, and they are asked for up to 50, 50 or 200 hours more (the literal reading, which this module took before the repair).
Taken, in the engine: the certificate is not a column A entry of the ungraded rows (on both branches of FS1), item 1 applies to its holder whatever other item also fits them, and item 1 is returned with the entry "the certificate itself" added to its column B for the certificate they hold (`Second Schedule — the item as read: ... for the applicant in ...`); every other item, and item 1 for everyone else, is returned exactly as the Schedule prints it.
The added entry is the whole content of the reading: the Schedule prints no such entry.
Discriminating applicants: a grade 3 certificate holder seeking grade 3 (item C1 alone; or C6: up to 200 hours); a grade 2 certificate holder seeking grade 2 (B1 alone; or B5(1): up to 50); a grade 1 certificate holder seeking grade 1 (A1 alone; or A3: up to 50).
Alternative: `the reading with the Division certificate of the grade sought as an ordinary column A entry (FS10)`, and for the duty as a whole `s 6(a) under the reading` called with it.
The three functions named `(the certificate of the grade sought suffices)` in g2-conditions were the alternative while the literal reading was the default; they are kept, with their assertions, and now give the same answers as the default.
Neighbouring cases, checked: a LOWER graded certificate (grade 1 seeking grade 2 or 3, grade 2 seeking grade 3) is unchanged and still governed by the graded item that names it (B3: 100 hours, C3: 290, C4: 240); the Ministry of Education 5-unit certificate is untouched (B1(2) and B5(3) stay the open fork FS2); the youth school certificate is untouched.
Test: `g2-tests-second-schedule.l4`, the last section; `g2-tests-conditions.l4`; the literal reading's assertions are in `g2-tests-red.l4` as the old answers.

**FS11 (a Division certificate of a HIGHER grade than the one sought).**
Provisions: as FS10; the Schedule is silent on whether a grade 3 certificate stands for the course of a lower grade.
Readings: a certificate of a higher grade is not the certificate item 1 confers, so graded over general still puts its holder in the ungraded row (A3 for a grade 2 or grade 3 certificate seeking grade 1; B5(1) for a grade 3 certificate seeking grade 2: up to 50 hours) (taken, the unchanged reading: nothing in the text says a higher certificate stands in for a lower course); or a certificate of the grade sought or of a higher grade meets item 1 and nothing further is asked (a fortiori).
This is a genuine open question for a domain expert (section 7, question 3a), not something the D1 ruling settles: the D1 ruling is about the certificate item 1 itself confers.
Discriminating applicants: a grade 3 certificate holder seeking grade 1 or grade 2 (A3 or B5(1): 50 hours; or item 1 alone); a grade 2 certificate holder seeking grade 1.
Alternative: `the reading with a Division certificate of a higher grade also meeting item 1 (FS11)`; for the duty as a whole `s 6(a) under the reading` called with it.
Test: `g2-tests-second-schedule.l4`, the last section; `g2-tests-conditions.l4`; the alternative's answers are asserted as the default's in `g2-tests-red.l4`.

### 2.3 Section 6 (g2-conditions)

**FC1 (s 6(a) against regulation 4 of the Fees Regulations, group G8).**
s 6(a) says the Registrar SHALL grant; regulation 4 says the Registrar shall NOT give a licence for which a fee was fixed unless it was paid in full.
Taken: payment of the fee is a condition of the duty (the duty arises only where the fee was paid; s 59 empowers fees "for the grant of a licence").
Alternative: `s 6(a) (read without regulation 4) — the Registrar must grant the licence`, under which an applicant who meets every condition and has not paid is under a duty to grant that regulation 4 forbids.
Test: `g2-tests-conditions.l4`, traces.

**FC2 (s 6(a)(4): the three limbs and "in accordance with the Second Schedule").**
Taken: (4) holds when one of (a), (b), (c) holds AND the Schedule's requirement for the licence sought is met.
On that reading limb (c) is the Schedule's requirement itself, so the conjunction collapses to the Schedule; the limbs are encoded as the Law writes them, and the collapse is a finding (section 6, C6).
Alternative: `s 6(a)(4) (the limbs alone) — one of the training routes holds` and `s 6(a) (the limbs of (4) alone) — the conditions (1) to (4) all hold`, under which "in accordance with" asks nothing further of an applicant who meets a limb.
Discriminating applicants: a technician with the programme seeking grade 1 (limb (b) holds; Part A has no item for registrants, so item 1 asks for 350 hours or a 3-unit certificate); a practical engineer seeking grade 2 (Part B has no item for practical engineers).
Test: `g2-tests-conditions.l4`.
The grade 1 certificate holder seeking grade 1 used to be the first discriminating applicant (limb (a) holds, A3 asked up to 50 hours); since the D1 repair (FS10) the default also qualifies them, so the technician is the discriminating applicant and the old red line was replaced by one for the technician.

**FC3 (ss 19(b) and 19(c); integration point IP5).**
Taken: the training or complementary studies the Schedule requires count as completed when the applicant completed them in a programme the Registrar approved (s 19(b)), or when the foreign qualification was recognised as meeting the training requirements (s 19(c)(1)).
Alternative: the programme's approval is not a condition of the applicant's completion (s 19(b) binds the programme, not the applicant): `s 6(a) (the programme's approval not a condition) — the conditions (1) to (4) all hold`.
Test: `g2-tests-conditions.l4`.

**FC4 (s 2 "final certificate"; IP5).**
Taken: every certificate that column A names counts as a final certificate (the Schedule itself names each one as a final certificate), the youth school certificate included (`s 2 — the certificate counts as a final certificate`, a stand-in for group G1's test).
Alternative: the youth school certificate does not count, s 2(1) asking for an examination the Division set that is not stated of it (`s 2 (the youth school certificate not counted) — the certificate counts as a final certificate`).
Test: `g2-tests-conditions.l4`.

**FC5.**
s 6(a)(1) asks that the applicant be an adult and states no age; the word is read as the `of full age` flag of the `Applicant` record (domain.l4), which carries the same note.
There is no number to give an alternative for.

**FC6.**
s 6(b) is a power that exists only with the committee's approval.
Taken: without the approval no power arises and nothing is permitted (the rule is `FULFILLED`).
Alternative: `s 6(b) (an order without the approval is forbidden) — the Minister may change the Second Schedule by order`, under which an order made without approval is a breach.
Test: `g2-tests-conditions.l4`, traces.

**FC7 (the certificate the course confers; repaired 2026-10-14, defect D1).**
The course of an item of Part N confers a final certificate of grade N for a licence of grade N.
Until the repair this module TOOK the literal reading: the holder of that certificate was in the Part's Division-certificate item (A3, B5(1) or C6) and was asked for up to 50, 50 or 200 hours more, so the applicant who completed C1's 720 hours and held the grade 3 certificate it confers was asked for 200 more (section 6, C5).
Now taken: the holder has met item 1 and nothing further is asked.
The decision lives in the engine (fork FS10 above), so that `training required for the licence sought` and the duty agree; this module follows the engine.
Alternative (the literal reading): `s 6(a) under the reading` called with `the reading with the Division certificate of the grade sought as an ordinary column A entry (FS10)`.
The three functions named `(the certificate of the grade sought suffices)` are kept for their assertions and now agree with the default.
Test: `g2-tests-conditions.l4`: grade 1, grade 2 and grade 3 certificate holders seeking the same grade are granted with no course, no approved programme and no recognition; the personal conditions still bind them; a grade 1 certificate seeking grade 2 and an applicant with no certificate are NOT helped by it.

### 2.4 Section 9 (g2-temporary-licence)

**FT1 (s 9(a) "notwithstanding ss 6 and 8").**
Taken: the expert need meet only s 9(a)(1) to (3) and be from a foreign state; s 6(a)(1) (adult), (2) (citizen or resident, which a foreign expert cannot be) and (3) (no disqualifying offence) are not asked.
Alternative: s 6(a)(1) and (3) are still asked: `s 9(a) (also asking s 6(a)(1) and (3)) — the applicant is a foreign expert meeting conditions (1) to (3)`.
Test: `g2-tests-temporary-licence.l4`: a minor, and a convicted expert whose offence the Registrar finds disqualifying.

**FT2 (kind V).**
"a period not exceeding one year": the last day of the term is no later than one year after the day of the grant (IL s 10(b); 1.2.2026 gives 1.2.2027; 29.2.2024 gives 28.2.2025) (taken); alternative: IL s 10(c) applied to that last day (`s 9(a) (Interpretation Law s 10(c) applied) — the latest last day of a temporary licence granted on`).
The Registrar chooses the term; a term past the cap is not an exercise of the power (the `PROVIDED` guard).
Test: `g2-tests-temporary-licence.l4`.

**FT3 (kind V; P5).**
The renewal's one-year cap is counted from the last day of the term it renews (the terms run consecutively) (taken: 31.1.2027 gives 31.1.2028); alternative: from the day of the renewal (`s 9(b) (counted from the day of the renewal) — the latest last day of a term renewed on`).
Test: `g2-tests-temporary-licence.l4`.

**FT4 (kind B).**
"in the six years preceding the filing of the application": from the same calendar date six years before up to the day before the application (taken; application 1.9.2026 gives 1.9.2020; a 29 February application gives 1 March); alternative: the application day counts (`s 9(a)(2) (the application day counts) — ...`).
Test: `g2-tests-temporary-licence.l4`: work on 1.9.2020 counts, on 31.8.2020 does not; on the application day it does not (taken) or does.

**FT5.**
"a system whose cooling capacity is above 70 kW": a single invited system (the text says "a system"), strictly above 70, so a system of exactly 70 kW (a grade 2 system, s 2) does not qualify.
No alternative reading of "above" is offered; the strictness is asserted at 70, 70.5 and 71.

**FT6.**
"similar" systems and "authorised" abroad are facts supplied with the application, not the Registrar's opinion, which the text reserves for (3).

### 2.5 Section 8, second limb (g2-renewal)

**FR1 (trap T26, groups G1 and G2).**
s 6(a) says the Registrar SHALL grant; s 8 says a licence CAN be renewed on the conditions of s 6 except (a)(4) and says nothing of who renews or of a duty; s 10(a) says the Registrar MAY, on six grounds, refuse to renew.
Taken: s 8's second limb states when a licence can be renewed (a boolean test: the passive "can be renewed" is an eligibility test, neither a permission nor a duty), and leaves the Registrar's duty or discretion to ss 5 and 10.
Alternative: s 8 read as a duty like s 6(a), displaced only by a ground under s 10(a): `s 8 (read as a duty) — the Registrar must renew the licence`.
Test: `g2-tests-renewal.l4`, traces.
The fee for a renewal (regulation 2(c), regulation 4) is not asked here.

## 3. Answer table

Dates are those of the tests; "taken" is the reading taken, "alt" a named alternative of section 2.

| scenario | answer | provision |
| --- | --- | --- |
| licence granted 1.2.2026 | last day 1.2.2031 (alt FV1: 31.3.2030) | s 8, limb 1 |
| licence granted 1.6.2026 | last day 31.3.2031 | s 8, limb 2 |
| licence granted 31.3.2026 | the limbs tie: 31.3.2031 | s 8 |
| licence granted 29.2.2024 | last day 28.2.2029 (IL s 10(b): the last day of the month) | s 8, limb 1 |
| licence granted 1.2.2026, renewed 15.6.2030 | last day 31.3.2035 (alt FV3: 2.2.2036) | s 8 |
| licence granted 1.2.2026; Registrar extends three months from 1.2.2031 | last day 1.5.2031 (alt FV7: 31.3.2031) | s 17(c) with s 8 |
| licence granted 1.2.2026 | in force on 1.2.2026 and 1.2.2031, not on 31.1.2026 or 2.2.2031 | s 8 |
| licence revoked on 1.5.2028 | in force on 30.4.2028, not on 1.5.2028 (alt FV6: in force on 1.5.2028) | s 10 as recorded; s 8 |
| temporary licence granted on 1.2.2026 | latest last day 1.2.2027 | s 9(a) |
| temporary licence term ended 31.1.2027, renewed | latest last day of the renewal 31.1.2028; two renewals in all | s 9(b) |
| expert invited for a 70 kW system / a 71 kW system | does not qualify / qualifies | s 9(a)(1) |
| application 1.9.2026: work abroad on 1.9.2020 / 31.8.2020 | counts / does not | s 9(a)(2) |
| applicant with no prior training seeking grade 1 | item A1: up to 350 hours conferring a grade 1 certificate, or a 3-unit certificate | S2.A.1 |
| holder of a 3-unit certificate seeking grade 1 | item A1, option (2): the certificate itself | S2.A.1(2) |
| 365 days of work in the three years before 1.9.2026, seeking grade 1 | item A2: up to 220 hours (364 days: item A1) | S2.A.2 |
| the same, applying on 16.7.2028 / 17.7.2028 (commencement 16.7.2025) | item A2 / item A1 | S2.A.2/colC |
| grade 1 certificate seeking grade 2 | item B3: up to 100 hours (alt FS1: B3 and B5) | S2.B.3(2), S2.B.5(1) |
| 5-unit certificate seeking grade 2 | item B5: up to 50 hours (alt FS2b: B1 and B5) | S2.B.5(3), S2.B.1(2) |
| technician with the programme / without it, seeking grade 2 | item B2: nothing further / item B6: up to 50 hours | S2.B.2, S2.B.6 |
| grade 2 licence in force, seeking grade 3 | item C4: up to 240 hours (gazette) | S2.C.4 |
| registered mechanical engineer seeking grade 3 | item C8: up to 230 hours | S2.C.8 |
| grade 3 certificate seeking grade 3 (and grade 2 for 2, grade 1 for 1) | item C1 alone, nothing further asked (alt FS10: item C6, up to 200 hours; B5(1) and A3: up to 50) | S2.C.1, S2.C.6 |
| grade 1 certificate seeking grade 3 / grade 2 certificate seeking grade 3 | item C3: up to 290 hours / item C4: up to 240 hours | S2.C.3(2), S2.C.4(2) |
| grade 3 certificate seeking grade 1 / grade 2 | item A3 / B5(1): up to 50 hours (alt FS11: item 1 alone) | S2.A.3, S2.B.5(1) |
| s 17(c) extension of half a month from 1.2.2031 | the months form refuses (it takes whole months, IL s 10(b)); the day form `extended to` 15.2.2031 gives 15.2.2031 | s 17(c) |
| adult citizen, clean record, no prior training, course completed in an approved programme, fee paid, seeking grade 1 | the Registrar must grant | s 6(a) |
| the same, fee not paid | no duty (alt FC1: the duty stands) | s 6(a) with regulation 4 |
| the same, course not completed | no duty | s 6(a)(4) |
| holder of a 3-unit certificate seeking grade 1, no course | the Registrar must grant | s 6(a)(4)(a), S2.A.1(2) |
| holder of a valid electrician licence | the Director may exempt from the electricity chapter | s 7(a) |
| applicant with no training at all, adult, citizen, clean | can be renewed (but s 6(a)(4) fails for the same person) | s 8, second limb |

The traces (`#TRACE`) that exercise the regulative rules behaved as follows, read by hand from the output.
s 6(a): the Registrar who grants the licence sought fulfils the rule; with conditions and fee and nothing done the duty stands with no deadline; with the fee unpaid, or a condition failing, no duty arises; FC1's alternative keeps the duty standing with the fee unpaid.
s 6(b): with approval and the Minister acting, `FULFILLED`; with approval and nothing done, the permission stands; without approval, `FULFILLED`; FC6's alternative breaches where the Minister acts without approval.
s 7(a), (b): the Director who exempts fulfils the rule; nothing done leaves the permission standing; a non-holder gives `FULFILLED`.
s 7(c): the Director who publishes fulfils the duty; nothing done leaves it standing and no breach arises (the section states no period).
s 9(a): a grant to the cap fulfils the rule; a grant past the cap is not an exercise of the power (the permission stands); the fee unpaid or a condition failing gives `FULFILLED`.
s 9(b): likewise; two renewals already made, an ordinary licence, or the fee unpaid, give `FULFILLED`.

## 4. Nouns requests for the INTEGRATOR

The shared nouns of domain.l4 were enough for the rules; these are local stand-ins and local nouns, listed so the INTEGRATOR can move any of them.

| noun | where defined | request |
| --- | --- | --- |
| `Foreign expert's application under section 9` and `Work done abroad by a foreign expert under section 9` | g2-temporary-licence | facts a foreign expert's application carries (s 9(a)); move into domain.l4 if other groups need them |
| `Second Schedule column A entry`, `Requirement of the Second Schedule`, `Second Schedule item`, `Reading of the Second Schedule`, `Second Schedule case`, `Second Schedule day span` | g2-second-schedule | G2-private; renamed with "Second Schedule" so that no other group's name can clash |
| `An act under section 6`, `An act under section 7`, `An act under section 9`, `Chapter of the training under section 7` | g2-conditions, g2-exemption, g2-temporary-licence | the acts of the Registrar, the Minister and the Director in these sections |
| `s 2 — the certificate counts as a final certificate` | g2-conditions | a stand-in for group G1's test of s 2 "final certificate" (IP5); replace by G1's rule over `Certificate` when wired |
| the Registrar's opinions | inputs, see section 5 | s 6(a)(3) and s 9(a)(3) |
| exemption given | inputs | `the electricity chapter exemption was given`, `the working-at-height chapter exemption was given` (the Director's exercised discretion) |

Requests of the INTEGRATOR beyond nouns.
1. `Application` carries no system, so the s 63(a)(2) anchor of the three-year note (trap T7) can only be supplied as a date; if group G7 can say which refrigerant regime an application is for, the anchor fork becomes an input.
2. The alternatives of FV2, FT2 and FS8 take a `Calendar of rest days` record and apply `days of rest, recess or holiday listed in`, because the time module's own functions take a `FUNCTION FROM DATE TO BOOLEAN`, which an exported rule cannot take; none of the three is exported, and no exported rule takes a function-typed input.

## 5. Standard inputs consumed and functions exported

Within-group imports are used (section 0).
`the commencement day` is taken as a DATE (IP2: the commencement day of s 63(a)(1), the later of three months after publication and the entry into force of the s 59 regulations, computed by group G7); the BOOLEAN form of IP2 is not consumed.
IP8 (`the licensee breached a licence condition`) is not consumed: FR1 leaves the grounds for refusing to renew to group G1.
No rule of this group is gated on the BOOLEAN form of IP2 (`the Law has commenced for the work on the system`): ss. 6 to 9 state no commencement, and the survey names G2 as a consumer of IP2 only for the three sunset notes; the INTEGRATOR may compose that BOOLEAN with the duty of s 6(a) if it wants the gate.

### Inputs, by exact `GIVEN` name

| input | type | integration point | used by |
| --- | --- | --- | --- |
| `the commencement day` | DATE | IP2 (G7) | the three-year note: `training required for the licence sought`, `the Registrar must grant the licence` |
| `the programme was approved by the Registrar` | BOOLEAN | IP5 (G4, s 19(b)) | s 6(a)(4) |
| `the foreign qualification was recognised` | BOOLEAN | IP5 (G4, s 19(c)) | s 6(a)(4) |
| `the fee was paid in full` | BOOLEAN | IP11 (G8, regulations 2 and 4) | s 6(a), s 9(a), s 9(b) |
| `in the Registrar's opinion an offence the applicant was convicted of or is charged with makes the applicant unfit to be a licensee` | BOOLEAN | IP17 | s 6(a)(3), s 8 renewal |
| `in the Registrar's opinion the expert is of repute and a renowned expert in the field` | BOOLEAN | IP17 | s 9(a)(3) |
| `the training or complementary studies that the Second Schedule requires were completed` | BOOLEAN | G2's own | s 6(a)(4) |
| `the Knesset Labour and Welfare Committee approved the order` | BOOLEAN | s 6(b) | s 6(b) |
| `the electricity chapter exemption was given`, `the working-at-height chapter exemption was given` | BOOLEAN | the Director's discretion, s 7 | `s 7 — the chapters of the training the applicant is exempt from` |
| `a ground for refusing to renew applies under section 10(a)` | BOOLEAN | G1 (s 10(a)); only the alternative FR1 | `s 8 (read as a duty) — the Registrar must renew the licence` |
| `Calendar of rest days` | domain record | IP15 | only the alternatives that apply IL s 10(c) |

The facts about the applicant, the application, the licence and the foreign expert arrive as the records `Applicant`, `Application`, `Licence` of domain.l4 and `Foreign expert's application under section 9`.

### Functions exported (`@export`), copied from the modules by `work/g2/sigs.py`

| module | rule (the identifier is the text between backticks, mixfix segments included; the arguments follow in the order given) | inputs | answer |
| --- | --- | --- | --- |
| g2-conditions.l4 | `the Registrar must grant the licence` application `the commencement day` `in the Registrar's opinion an offence the applicant was convicted of or is charged with makes the applicant unfit to be a licensee` `the training or complementary studies that the Second Schedule requires were completed` `the programme was approved by the Registrar` `the foreign qualification was recognised` `the fee was paid in full` | application : Application; `the commencement day` : DATE; `in the Registrar's opinion an offence the applicant was convicted of or is charged with makes the applicant unfit to be a licensee` : BOOLEAN; `the training or complementary studies that the Second Schedule requires were completed` : BOOLEAN; `the programme was approved by the Registrar` : BOOLEAN; `the foreign qualification was recognised` : BOOLEAN; `the fee was paid in full` : BOOLEAN | A BOOLEAN |
| g2-renewal.l4 | `the conditions of the licence still hold` licence `the conditions of a licence under section 6 still hold` `the conditions of a licence under section 9 still hold` | licence : Licence; `the conditions of a licence under section 6 still hold` : BOOLEAN; `the conditions of a licence under section 9 still hold` : BOOLEAN | A BOOLEAN |
| g2-second-schedule.l4 | `training required for the licence sought` application `the commencement day` | application : Application; `the commencement day` : DATE | A LIST OF `Second Schedule item` |
| g2-temporary-licence.l4 | `s 9(a) — the latest last day of a temporary licence granted on` `the day of the grant` | `the day of the grant` : DATE | A DATE |
| g2-temporary-licence.l4 | `the temporary licence may be granted` expert `in the Registrar's opinion the expert is of repute and a renowned expert in the field` `the fee was paid in full` | expert : `Foreign expert's application under section 9`; `in the Registrar's opinion the expert is of repute and a renowned expert in the field` : BOOLEAN; `the fee was paid in full` : BOOLEAN | A BOOLEAN |
| g2-validity.l4 | `s 8 — the last day of the validity period beginning on` `the day the validity period begins` | `the day the validity period begins` : DATE | A DATE |
| g2-validity.l4 | `s 8 — the last day of validity of the licence` licence | licence : Licence | A DATE |
| g2-validity.l4 | `the licence is in force on` licence day | licence : Licence; day : DATE | A BOOLEAN |
| g2-validity.l4 | `the licence kinds in force on the day` day licences | day : DATE; licences : LIST OF Licence | A LIST OF `Licence kind` |

How to wire.
IP1: the in-force function is named `the licence is in force on` (the name PLAN proposed; an earlier spelling, `the licence` L `is in force on` D, was renamed because its head also occurs in another group's module); consumers call `the licence is in force on` licence day, or take `the licence kinds in force on the day` day licences as the input `licence kinds in force on the day`; the second refuses for the whole list if any licence in it is a temporary licence with no recorded last day (a `filter` forces the refusal), which is deliberate: the register is incomplete, and no kind of the list can be trusted.
IP6: `training required for the licence sought` application `the commencement day` returns the items of the Part sought that apply, each with its column B; on the reading taken item 1 is the default of every Part, so the list is never empty and the named refusal `the Second Schedule gives no item for this applicant` is unreachable there (it is reachable, and tested, through `Second Schedule — the training required for the licence sought under` reading ... with the reading FS2a).
Since the D1 repair (2026-10-14, fork FS10) the item list of an applicant who holds the Division certificate of the grade sought is item 1 of the Part alone, and that item 1 carries one more entry in its column B than the Schedule prints: `column B: the certificate itself` for the certificate held (so for a grade 3 certificate holder seeking grade 3, column B is the 720-hour course or the grade 3 certificate itself; for grade 1 and grade 2, the printed course, the printed Ministry of Education certificate, and the certificate held).
A consumer that displays column B shows that applicant one more way to meet item 1; a consumer that reads only the item numbers sees 1 where it used to see 3, 5 or 6.
For every other applicant the items are returned exactly as the Schedule prints them.
The type `Second Schedule item` and the type of the answer did not change.
IP18: call `the conditions of a licence under section 6 still hold` (application, the opinion) and `the conditions of a licence under section 9 still hold` (expert, the opinion), then pass both to `the conditions of the licence still hold` licence ...; group G1 takes the negation as `a condition for the grant ceased to hold`.
IP19: `s 8 — the last day of validity of the licence` licence is the last day of validity (the register's where recorded); `s 17(c) — the last day of validity` d `extended by` n `months` is the helper for an extension.
Names are mixfix: the identifier is the text between backticks, including the segments between the arguments, exactly as printed above and in the modules.

## 6. Contradictions in the source

A deliberate, separate pass over the finished modules against the Hebrew, after encoding.
Each entry: the provisions, the discriminating case, both readings callable.

**C1.**
S2.B.1(2) and S2.B.5(3) (trap T2): a 5-unit climate-control certificate is, in item 1, enough with nothing more, and in item 5, up to 50 hours.
Discriminating case: an applicant whose only qualification is that certificate, seeking grade 2.
Readings: FS2 (B5 governs) and FS2b (both rows apply).

**C2.**
S2.B.3(2) with S2.B.5(1); S2.C.3(2) and S2.C.4(2) with S2.C.6 (trap T1): the same certificate is covered by a row that names its grade and by a row that names none, with different hours.
Discriminating cases: a grade 1 certificate seeking grade 2 (100 hours or 50), seeking grade 3 (290 or 200); a grade 2 certificate seeking grade 3 (240 or 200).
Readings: FS1.

**C3.**
S2.A.1 and S2.B.1 (trap T2): the item headed "no prior training or experience" has a certificate as its option (2), which is prior training.
Discriminating case: a 3-unit certificate seeking grade 1.
Readings: FS2.

**C4.**
S2.B.2 with S2.B.6; S2.C.2 with S2.C.7 (trap T3): registration alone, and registration with the completed programme, with different requirements.
Discriminating case: a technician who completed the programme (nothing further, or 50 hours).
Readings: FS3.

**C5 (resolved by the reading taken since 2026-10-14, defect D1; kept as a finding).**
S2.A.3, S2.B.5(1), S2.C.6 against s 6(a)(4)(a) and against the Schedule's own courses: s 6(a)(4)(a) says a holder of a final certificate meets (4); read literally, the Schedule asks the holder of a Division certificate for up to 50, 50 or 200 hours more; and the certificate that the course of the item for the licence sought confers (A1(1) and A2: grade 1; B1(1), B3, B4: grade 2; C1, C3, C4, C5, C8: grade 3) is itself a Division certificate of the kind these items reach.
Discriminating case: the applicant who completed C1's 720 hours and holds the grade 3 certificate it confers, applying for a grade 3 licence.
Reading taken since the repair: rows A3, B5(1) and C6 are for the holder of the lesser, ungraded certificate, item 1 is the way to the licence, and this applicant has met it: nothing further (fork FS10).
The literal reading (they are in C6 and are asked for 200 hours more) stays callable.
What remains open: the holder of a certificate of a HIGHER grade than the one sought (fork FS11), where the text does not say that the higher certificate stands for the lower course.
Readings: FS10, FS11 and FC2 (limbs alone).

**C6.**
S2.A, S2.B, S2.C against s 6(a)(4)(b): registration in the register is a route to a licence of any grade, yet Part A has no item for a registered technician, practical engineer or engineer, Part B has none for a practical engineer or an engineer, and Part C has none for a technician; such an applicant falls to item 1 of the Part (350, 480 or 720 hours).
Discriminating cases: a technician with the programme seeking grade 1 (limb (b) holds, Part A asks 350 hours or a 3-unit certificate); a practical engineer seeking grade 2.
Readings: the taken one (the Schedule governs) and FC2's alternative.
Related finding: with "in accordance with the Second Schedule" read as a conjunct, limb (c) ("completed complementary studies, if required") is the Schedule's requirement itself, so (4) collapses to the Schedule and limbs (a) and (b) add nothing.

**C7.**
S2.A.2, S2.B.4, S2.C.5, column C, with s 63(a)(1) and (2) (trap T7): the note runs three years from the commencement day of s 63(a)(1), which is the commencement for listed flammable refrigerants only; for systems of any other refrigerant the licensing duty starts 18 months later (s 63(a)(2)).
Discriminating case: an experienced applicant applying on 1.1.2029 for work on an ordinary-refrigerant system (the route is closed on the text's anchor of 16.7.2025 and open on the s 63(a)(2) anchor of 16.1.2027).
Readings: FS8.

**C8.**
s 8, limb 2 (trap T24): on one reading of "the fifth year from the year in which the licence was granted" (year plus four), "whichever is earlier" has no work to do, because limb 2 is always the earlier.
Discriminating grants: 1.2.2026 and 1.6.2026.
Readings: FV1.

**C9.**
s 8 and s 17(c) (trap T25): an extension of the validity period, and a validity period that ends on a day fixed by s 8.
Discriminating case: a licence granted 1.2.2026 extended by three months from 1.2.2031 and in force on 1.4.2031.
Readings: FV7.

**C10.**
s 6(a), s 8 and s 10(a) (trap T26): a duty to grant, a possibility of renewal, and a power to refuse to renew.
Discriminating case: an applicant who meets s 6(a)(1) to (3) and against whom a ground of s 10(a) applies.
Readings: FR1.

**C11.**
s 6(a) and regulation 4 of the Fees Regulations (group G8): the Registrar SHALL grant, and SHALL NOT give a licence for which a fee was fixed unless it was paid.
Discriminating case: an applicant who meets s 6(a)(1) to (4) and has not paid.
Readings: FC1.

**C12.**
s 9(a), "notwithstanding ss 6 and 8", with s 6(a)(1) to (3): the expert's three conditions replace all of s 6, so a foreign expert need not be an adult or free of a disqualifying offence, and cannot be a citizen or resident.
Discriminating case: a minor expert, or one whose offence the Registrar finds disqualifying.
Readings: FT1.

**C13.**
S2.B column B heading against the headings of Parts A and C (trap T5), and s 6(a)(4)(c)'s "complementary studies, if required in column B": only Part B's column B speaks of complementary studies.
No discriminating applicant: both readings return the same column B (FS4).

**C14.**
S2.C.4 (trap T4): the wiki's layout against the gazette's (section FS6).
A defect of the unofficial text; the gazette governs.

**C15.**
S2.A.3, column B: the wiki line stops one word short of the gazette's line (p. 201).
A defect of the unofficial text with no legal effect.

**C16.**
s 6(b) with s 60(1)(a) (group G7): the Minister may change the Second Schedule by order with the Knesset committee's approval, and may make regulations on training requirements for a licence, "different kinds of training for different kinds of licence, for those with prior experience or prior training", also with the committee's approval.
Two powers over the same subject; the Law does not say which instrument prevails if they differ.
No callable reading: it is a question about which instrument governs, not a computation.

**C17.**
No 5-unit route to grade 3: items 1 of Parts A and B offer a certificate as an alternative to the course (3 units for grade 1, 5 units for grade 2); Part C has no certificate option, and the 5-unit certificate leads, in C4(3), to up to 240 hours.
Not a contradiction but an asymmetry the text does not explain.

## 7. Open questions for a domain expert

1. Is item 1 of each Part the default item (FS2), or does it apply only to an applicant with no prior training or experience at all?
2. Is the 5-unit certificate in B1(2) a direct route to a grade 2 licence, or is it B5(3)'s up to 50 hours (C1)?
3. Is the reading taken since 2026-10-14 right, that a Division certificate of the grade sought (grade 1 for grade 1, and so on) is the certificate item 1 confers and satisfies the Schedule with nothing further (FS10, FC7, C5)? If not, why must the holder of the certificate a course confers take up to 50, 50 or 200 hours more?
3a. Does a Division certificate of a HIGHER grade than the one sought (grade 3 seeking grade 1 or 2) stand for the course of the lower grade, or is its holder in the ungraded row (A3, B5(1): up to 50 hours) (FS11)?
4. Does "in accordance with the Second Schedule" in s 6(a)(4) add a condition to limbs (a) and (b), or is it the content of limb (c) (FC2, C6)?
5. How is "a year of cumulative experience" counted: 365 days, twelve months, or the days the applicant worked (FS7)? Do overlapping periods count once? Does work on the day of the application count?
6. Does the three-year note on the experience items run from the commencement day for every refrigerant, or from the later commencement day that applies to the system (FS8, C7)? Is it tested on the day of application or the day of decision?
7. Which year is "the fifth year from the year in which the licence was granted" (FV1)? Does a renewal count a further validity period from the renewal day or from the end of the previous one (FV3)? Can a renewal be made after a licence has lapsed?
8. Can an extension under s 17(c) pass 31 March (FV7)? Is an extension of a part of a month stated by the day it ends on, as the day form does (D2)?
9. Does s 9(a)'s "notwithstanding ss 6 and 8" displace s 6(a)(1) and (3) for a foreign expert (FT1)?
10. Is the fee a condition of the Registrar's duty under s 6(a) (FC1), and is s 8's renewal a duty or an eligibility test (FR1)?
11. Does a youth vocational school certificate satisfy s 2's "final certificate" (FC4)?
12. Does a licence that has lapsed, been revoked or been suspended still count as "a grade 1 licence" in column A of items B3(1), C3(1) and C4(1) (FS9)? When does a decision under s 10 take effect (FV6)?
13. Which prevails where an order under s 6(b) and regulations under s 60(1)(a) both set training requirements (C16)?
14. Does an exemption under s 7 change the hours of the training, and can it be given to an applicant whose requirement involves no training?

## 8. What the sources do not answer

Each is an input or a named refusal in the encoding; none gets a default.
The age of majority (s 6(a)(1)); the flag `of full age` is an input.
The content of an order under s 6(b) (none is in the sources): the Second Schedule as enacted is the only vintage.
How many hours an applicant must complete within "up to N hours" (trap T6), and how many hours a chapter takes, so what an exemption under s 7 saves.
The list of licences in regulation 7(1) to (7) of the Electricity (Licences) Regulations and the approval of regulations 5 and 6 of the Work at Height Regulations; each arrives as a flag on the applicant.
What makes a system "similar" to the systems a foreign expert was invited for (s 9(a)(2)), and what "authorised" abroad means.
Whether a renewal can be made after a licence lapsed, the time within which a renewal must be applied for (a regulation under s 60(2)(a), group G7), and from when a renewed licence is valid (FV3).
When a decision under s 10 takes effect (FV6).
Whether a temporary licence may be renewed beyond two renewals, or after its term ended.
Whether s 7's exemption is available where the Schedule asks for no training.
Whether a Division certificate of a higher grade than the one sought stands for the course of the lower grade (FS11); the text says nothing, and the encoding takes the unchanged reading with the other callable.
Whether the extension under s 17(c) may be a part of a month, and by what rule its last day is fixed: s 10(b) of the Interpretation Law fixes the end of a period only of whole months, so the day form states the day (D2).
What happens to an application made before the three-year note lapsed and decided after it (FS8).
What the programme with the complement course consists of (B2, C2): it is a flag on the applicant.
The identity of the Registrar and the Director of the Training Division, the Registrar's opinions, and the calendar of days of rest, recess and holiday for any year: all inputs.
The text of the Law as amended after the Wikisource revision (rev 2947808, 2025-07-10).
A consequence for the exported `the licence kinds in force on the day` and for `the licence is in force on`: for a temporary licence with no recorded last day the answer is a named refusal, and the list function refuses for the whole list.

## 9. What check.sh printed

`work/g2/check.sh` is the skill's `assets/check.sh` adapted to this group (the glob `g2-*.l4`, a warnings column, `g2-tests-red.l4` expected to fail 44 times, and the extra checks).
The INTEGRATOR's `check.sh` needs `g2-tests-red.l4) echo 44 ;;` in its `expected_failed` table, and `encoding.json` needs `g2-tests-red.l4` in `expected_red`.

```text
module                                errors satisfied  failed  refused  warnings  expected
g2-conditions.l4                           0         0       0        0         0         0
g2-exemption.l4                            0         0       0        0         0         0
g2-renewal.l4                              0         0       0        0         0         0
g2-second-schedule.l4                      0         0       0        0         0         0
g2-temporary-licence.l4                    0         0       0        0         0         0
g2-tests-conditions.l4                     0       110       0        0         0         0
g2-tests-exemption.l4                      0        10       0        0         0         0
g2-tests-fixtures.l4                       0         0       0        0         0         0
g2-tests-red.l4                           44         0      44        0         0        44
g2-tests-renewal.l4                        0        16       0        0         0         0
g2-tests-second-schedule.l4                0       210       0        0         0         0
g2-tests-temporary-licence.l4              0        41       0        0         0         0
g2-tests-validity.l4                       0        93       0        0         0         0
g2-validity.l4                             0         0       0        0         0         0
TOTAL (14 modules)                        44       480      44        0         0
(a failed assertion is also an error; any other error, any refused assertion, any warning makes the run red)

extra checks
  all modules start with '@lang en' and have ASCII filenames
  imports are only prelude, daydate, il-interpretation-time, domain and g2- modules
  il-interpretation-time.l4 matches the pinned sha256
  l4 check: no stray @ref warnings
  srcrefs: srcrefs check: 162 src: lines, 56 runs, 74 locators, 0 problems
  order problems: 0
(check.sh exit status 0)
```
