# Notes: the Old Age Security Act and the Old Age Security Regulations (the keel)

These are the shared notes of the keel agent `oas-g0`.
The three pieces that follow (oa1, oa2, oa3) take their facts about the whole text from this file, so read it before you import anything.

**Status (2026-10-22).**
This folder holds six modules and five test files, all written by the keel and all running on the stable build `1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.
Verified by running, not by reading: `check.sh` prints 0 errors, 229 assertions satisfied, 0 failed and 0 refused over the eleven files (the exact print is under "What check.sh prints").
`srcrefs.py check --refs` against the Act file reports 0 problems over all eleven files.
`l4 check` on each file shows no error and no warning, and no "is at the end of the file" or "follows code on its line" diagnostic.
Each module was imported by a three-line throwaway file and its assertion was satisfied, and so was one file importing all six at once; the throwaway files are deleted.
The keel wrote no seat layer, no `@export` and no `@desc`; everything outside lines 13-91 of the Act is for the pieces.
Nothing here has been run on `unstable`, because the brief gave the keel only the stable binary; the local `YMD` shim in `oas-core.l4` is expected to collide with `unstable`'s own prelude `YMD`, which was not measured.

**The text.**
`R.S.C.-1985-c.-O-9.txt` and `C.R.C.-c.-1246.txt` are unofficial plain-text renderings made by a converter script (`jl_xml2txt.py`) from the Justice Canada XML repository; each is a consolidation current to 2026-09-30.
They are not the official text, they drop the historical notes, footnotes and French items, and nothing in this encoding has been verified against the official text.
The `-- src:N |` lines in the modules are copied from the rendering by `srcrefs.py quote`, so they show what the rendering says and nothing more.
Only the English version is deposited, and the two language versions have equal authority.

**Licence.**
`STUB-SOURCE-LICENSE.md` says the Reproduction of Federal Law Order covers reproduction and does not expressly grant a right to adapt, and that whether an encoding that quotes this text may rely on the Open Government Licence - Canada is a human decision to be recorded before an encoding quotes it.
Every keel rule quotes the text, so the keel's modules depend on that decision; the keel has not made it and has written no `SOURCE-LICENSE.md`.
The attribution the licence asks for is "Contains information licensed under the Open Government Licence - Canada."
The deposit must also say that the quoted text is not an official version.

**Which instrument each rule comes from.**
Every rule the keel encodes comes from the Act, R.S.C., 1985, c. O-9, section 2 or 2.1, and its `@ref` says so.
The keel encodes nothing from the Regulations; oa3 encodes them.
The rounding helpers in `oas-core-measures.l4` are arithmetic and not provisions: they do what the dropped-digit rule of Regulations 7, 8(2), 8(3) and 9(2) describes, and the keel does not encode those sections.
For the same reason none of the helpers carries an `@ref`: no provision licenses them, and the file's header says so; every rule in the other five modules carries one.

**Dates are data.**
Lines 13-91 of the Act hold no date of enactment, assent, making or coming into force, and no commencement rule, so the keel carries no enactment or commencement value and none is owed by this range.
The title block and section 1 (the short title) are oa1's.
Section 2 does hold dated thresholds, and they are rule data.
These are written as dates inside the rule the section's words govern, each with its `@ref` and each tested on both sides of the edge: July 2008 and July 2020 in "income" (a)(i) and (b.1), July 2022 in "income" (c.1), April 1996 in "special qualifying factor", and April 1998, June 30, 1999 and July 1, 1999 in "payment period".
March 1996, January 2001 and March 7, 1996 in "specially qualified individual" appear only in the names of inputs, because the person states whether they held.

**Files.**

| file | what it holds | assertions satisfied |
| --- | --- | --- |
| `oas-core.l4` | the core: `YMD` shim, `Benefit`, `Kind of pension`, `Kind of allowance`, `Party`, `Calendar span`, `Unit of time`, `Time limit`, `Sentence of imprisonment` | none (declarations only) |
| `oas-core-measures.l4` | shared arithmetic, no provision: months, ages, time limits, rounding | none |
| `oas-core-periods.l4` | s 2 "payment period", "payment quarter", "first adjustment quarter", "second adjustment quarter", "Consumer Price Index" | none |
| `oas-core-terms.l4` | s 2 "applicant", "beneficiary", "pensioner", "survivor", "common-law partner", "cheque", "release", and the Part under which each benefit is authorized | none |
| `oas-core-pension.l4` | s 2 "specially qualified individual" and "special qualifying factor"; s 2.1(1) and (2) | none |
| `oas-core-income.l4` | s 2 "income" | none |
| `oas-core-tests-measures.l4` | tests of the helpers | 60 |
| `oas-core-tests-periods.l4` | tests of the four quarters, the payment period and the Consumer Price Index | 59 |
| `oas-core-tests-terms.l4` | tests of the person and thing definitions | 37 |
| `oas-core-tests-pension.l4` | tests of the special qualifying factor and s 2.1 | 31 |
| `oas-core-tests-income.l4` | tests of "income", paragraph by paragraph and as a whole | 42 |

Every expected value in the tests is worked out by hand from the words of the text, with the arithmetic in the comment beside it.
No keel module holds an `#ASSERT`, so importing one runs no assertion.

## Vocabulary

Every type and every enumeration constructor the keel declares.
The first block is the core, `oas-core.l4`; the last three types sit with the rules that use them, in the module named.
"Licensed by" names the provision that makes the thing necessary; "convention" means no provision licenses it and the encoding chose it, for the reason in the row.
Record fields are not listed; the field names are in the files and are the Act's own words.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `Benefit` | enumeration | the three things the Act pays: a pension, a supplement or an allowance | s 2 "benefit", line 20 |
| `Pension` | constructor of `Benefit` | a monthly pension authorized to be paid under Part I | s 2 "pension", line 63 |
| `Supplement` | constructor of `Benefit` | a monthly guaranteed income supplement authorized to be paid under Part II | s 2 "supplement", line 83 |
| `Allowance` | constructor of `Benefit` | the allowance authorized to be paid under Part III | s 2 "allowance", line 16 |
| `Kind of pension` | enumeration | the two sizes of pension | s 3(1), line 96, and s 3(2), line 107 |
| `Full monthly pension` | constructor of `Kind of pension` | the pension payable to a person who meets s 3(1) | s 3(1), line 96 |
| `Partial monthly pension` | constructor of `Kind of pension` | the pension payable under s 3(2) to a person not eligible for a full one | s 3(2), line 107 |
| `Kind of allowance` | enumeration | the two allowances | s 19(1), line 515, and s 21(1), line 573 |
| `Allowance under section 19` | constructor of `Kind of allowance` | the allowance to the spouse, common-law partner or former common-law partner of a pensioner | s 19(1), line 515 |
| `Allowance under section 21` | constructor of `Kind of allowance` | the allowance to a survivor | s 21(1), line 573 |
| `Party` | enumeration | the persons and bodies the Act and the Regulations name as acting or being acted on; the PARTY type of a regulative rule | s 2 "Minister", line 57, and the sections named in the file beside each constructor |
| `Minister` | constructor of `Party` | the Minister of Employment and Social Development | s 2 "Minister", line 57 |
| `Governor in Council` | constructor of `Party` | makes the regulations | ss 34 and 34.2 |
| `Applicant` | constructor of `Party` | a person who has applied, or is deemed to have applied, for a benefit | s 2 "applicant", line 17 |
| `Beneficiary` | constructor of `Party` | a person to whom payment of a benefit has been approved | s 2 "beneficiary", line 19 |
| `Pensioner` | constructor of `Party` | a person whose application for a pension has been approved | s 2 "pensioner", line 64 |
| `Survivor` | constructor of `Party` | a person whose spouse or common-law partner has died and who has not become the partner of another | s 2 "survivor", line 84 |
| `Spouse or common-law partner` | constructor of `Party` | the spouse or common-law partner of an applicant, pensioner or beneficiary | s 2 "common-law partner", line 22; ss 19(1), 28(2) |
| `Former common-law partner` | constructor of `Party` | a former common-law partner of a pensioner | s 19(1) |
| `Sponsor` | constructor of `Party` | the sponsor whose undertaking is in effect under the Immigration and Refugee Protection Act | ss 11(7)(e), 19(6)(d), 21(9)(c); Regs 22.1(1) |
| `Representative` | constructor of `Party` | a responsible person or agency acting for a person, or appointed to receive a benefit for a beneficiary | Regs 4(1), 24(1) |
| `Estate` | constructor of `Party` | the estate or succession of a deceased person | ss 29(1), 29(2), 37(2.1); Regs 24(5) |
| `Social Security Tribunal` | constructor of `Party` | the Tribunal to which a decision of the Minister is appealed | s 28(1); Regs 38 |
| `Tax Court of Canada` | constructor of `Party` | the Court to which a ground of appeal about income is referred | s 28(2); Regs 2(1) "Court" |
| `Registrar of the Tax Court of Canada` | constructor of `Party` | the Registrar who acts in a reference | Regs 38.1(2), 39(1), 40(1) |
| `Federal Court` | constructor of `Party` | the court in which a debt to Her Majesty is recoverable | ss 37(2), 37(2.01), 37(2.02); s 44.2(1) "judge" |
| `Provincial or municipal authority` | constructor of `Party` | a provincial or municipal authority that pays assistance and may be reimbursed | s 36(2); Regs 4(2), 28.1 |
| `Statistics Canada` | constructor of `Party` | publishes the Consumer Price Index and supplies age information | ss 2 "Consumer Price Index", 6, 27 |
| `Minister of National Revenue` | constructor of `Party` | supplies reports and tax returns to the Minister | s 33.1; Regs 17 |
| `Other person` | constructor of `Party` | anyone else the Act addresses ("a person who has received ...", "every person who ...") | ss 37(1), 44(1) |
| `Calendar span` | record | a stretch of days with its `first day` and `last day`, both included | s 2 "payment period", line 58, and "payment quarter", line 62; also the base calendar year of ss 10 and 22 |
| `Unit of time` | enumeration | the unit of a time limit | convention: the text states limits in days, months and years (ss 27.1(1), 11(7)(a), 29(1)) and a piece needs one way to write them |
| `Days` | constructor of `Unit of time` | a limit counted in days | convention, as `Unit of time` |
| `Months` | constructor of `Unit of time` | a limit counted in calendar months | convention, as `Unit of time` |
| `Years` | constructor of `Unit of time` | a limit counted in calendar years | convention, as `Unit of time` |
| `Time limit` | record | a `number of units` and a `unit`; turn it into a date with `the day that is _ after _` or `the day that is _ before _` | convention, as `Unit of time` |
| `Sentence of imprisonment` | record | the four facts that make a sentence count for the incarceration rules: served in a penitentiary, length in days, served in a prison as defined in the Prisons and Reformatories Act, and the province's agreement under s 41 of the Department of Employment and Social Development Act | ss 5(3), lines 131-133; 19(6)(f), lines 549-551; 21(9)(d), lines 607-609 |
| `Manner of release` (`oas-core-terms.l4`) | enumeration | how a person left custody | s 2 "release", line 66 |
| `Release on earned remission`, `Release at the expiry of a sentence`, `Release on parole`, `Release on statutory release`, `Any other release from custody` | constructors of `Manner of release` | how a person left custody: the four ways s 2 names (earned remission, expiry of a sentence, parole, statutory release) and a last one for anything else, which is not a release | s 2 "release", line 66 |
| `Special qualification facts` (`oas-core-pension.l4`) | record | the four facts the specially qualified individual test reads: years of residence after eighteen, as of the last day of the preceding month; pension or allowance payable for March 1996 or earlier; payable for January 2001 or earlier; residing in Canada before March 7, 1996 as a citizen or permanent resident | s 2 "specially qualified individual", lines 78-80 |
| `Income facts` (`oas-core-income.l4`) | record | the sixteen figures a person reads off their tax return and records that s 2 "income" starts from or adjusts | s 2 "income", lines 29-56 |

## Naming conventions

- **Rule.** A backticked English phrase in the Act's own words that reads as a clause (`the person is a pensioner`) or a noun phrase (`the payment quarter containing the month containing _`), with the inputs after it or between its keywords; the keel's rule names carry no section label.
- **Names a piece declares.** Every rule, constant, type and enumeration constructor a piece declares begins with the label of the provision it encodes, as `s 12(2): the supplement for a month`, so that no two pieces declare the same name; a label such as `s 12(2): ` works in a type, a constructor and a rule name on 1.6.98 (measured).
- **Input.** A backticked phrase in the Act's words that states the fact (`the person's application for a pension has been approved`); a record input is named for what it holds and its fields are the Act's own phrases; one input holds one fact.
- **Question.** A yes or no a person can answer is a BOOLEAN rule or input named as a clause that is true or false (`the person is a survivor`), never as a question; the seat layer turns it into an `@export` with a `@desc`.
- **Enumeration constructor.** A capitalised phrase naming the case (`Release on parole`, `Allowance under section 19`); the keel's carry no label, a piece's carry theirs.
- **Money.** A NUMBER of Canadian dollars, exact, with cents as a fraction (273.80); it is rounded only where the text says so, and then with the helpers in `oas-core-measures.l4`.
- **Percentage.** A NUMBER that is a fraction of one, written with the postfix `%`: `0.6%` is the number 0.006 (section 7.1(1) adds 0.6% for each month).
- **Fraction of a whole.** A NUMBER between 0 and 1 (0.3 for three tenths, as in the special qualifying factor), never a percentage.
- **Days, months, years, ages.** A NUMBER with the unit in the name of the thing (`length in days`); an age is a NUMBER of complete years; a time limit is a `Time limit`, never a bare number.
- **Date.** A DATE built with `Date d m y`, day first, or with `YMD y m d` from the keel; bracket a `YMD` in a comparison, `d AT LEAST (YMD 2008 7 1)`.
- **Month.** The DATE of its first day; every keel rule that takes a month accepts any date in it and normalises with `the first day of the month containing _`; two months are the same month when the normalised dates are equal.
- **A fact about something outside the piece.** An input, never a stub rule, named in the words of the provision that defines it; the names two pieces must share are in the register under "Instructions to the pieces".
- **A figure the Act leaves to the Regulations ("prescribed").** An input of the type the Act's phrase implies (a `Time limit` for "prescribed time", a NUMBER for an amount), named `the prescribed ...`; the figure itself exists only in oa3's encoding of the Regulation that fixes it.
- **A fact that depends on a time.** The Act's own time phrase goes in the input's name (`... on the day preceding the day on which the person's application is approved`), so two readings at two times are two inputs.
- **Record fields.** Backticked phrases that do not begin with `is ` or `has `; the same field name in two records, even across imports, is accepted (measured).
- **A case the text does not answer.** A `MAYBE` with `NOTHING`, asserted by a test, never `FALSE` or `0`; the keel has one such case, "income" (a)(i) after June 2020 (fork F3).

## Defined terms

Every term the text defines, in the keel's range or elsewhere.
"By reference" means the keel does not encode it: the named piece does, and a piece that needs it takes it as an input named in the Act's words.
Line numbers are lines of the file named in the first column group; the Act is `R.S.C.-1985-c.-O-9.txt` and the Regulations are `C.R.C.-c.-1246.txt`.

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| allowance | Act s 2, line 16 | `oas-core.l4`: `Benefit` constructor `Allowance`, `Kind of allowance`; `oas-core-terms.l4`: `the Part of the Act under which the benefit is authorized _` | what Part III pays is oa2's |
| applicant | Act s 2, line 17 | `oas-core-terms.l4`: `the person is an applicant _ _ _` | the three limbs are inputs; the provisions that deem an application or waive it (for example ss 5(2), 11(3) and 11(3.1), which Regs 3(2) and 10.1 cite) are oa1's and oa2's |
| application | Act s 2, line 18 | `oas-core-terms.l4`: carried by the inputs of `the person is an applicant _ _ _`; no separate rule | a pure alias for "an application for a benefit" |
| beneficiary | Act s 2, line 19 | `oas-core-terms.l4`: `the person is a beneficiary _` | |
| benefit | Act s 2, line 20 | `oas-core.l4`: `Benefit` | |
| cheque | Act s 2, line 21 | `oas-core-terms.l4`: `the instrument is a cheque _` | |
| common-law partner | Act s 2, line 22 | `oas-core-terms.l4`: `the person is a common-law partner of the individual _ _ _ _` | fork F6 |
| Consumer Price Index | Act s 2, line 23 | `oas-core-periods.l4`: `the Consumer Price Index for an adjustment quarter _ _ _` | unrounded mean of the three monthly figures; Regs 9 rounding is oa3's (fork F10) |
| first adjustment quarter | Act s 2, lines 24-28 | `oas-core-periods.l4`: `the first adjustment quarter in relation to the payment quarter containing _` | |
| income | Act s 2, lines 29-56 | `oas-core-income.l4`: `the income of a person for a calendar year _ _` and one rule per paragraph | the starting figure and the adjustments are inputs in `Income facts`; the Income Tax Act is not in the text |
| Minister | Act s 2, line 57 | `oas-core.l4`: `Party` constructor `Minister` | |
| payment period | Act s 2, lines 58-61 | `oas-core-periods.l4`: `the payment period in relation to the month containing _` | fork F2 |
| payment quarter | Act s 2, line 62 | `oas-core-periods.l4`: `the payment quarter containing the month containing _` | |
| pension | Act s 2, line 63 | `oas-core.l4`: `Benefit` constructor `Pension`, `Kind of pension`; `oas-core-terms.l4`: `the Part of the Act under which the benefit is authorized _` | what Part I pays is oa1's |
| pensioner | Act s 2, line 64 | `oas-core-terms.l4`: `the person is a pensioner _` | |
| prescribed | Act s 2, line 65 | not encoded | the convention is under "Naming conventions": an input named `the prescribed ...`, the figure being in the Regulation oa3 encodes |
| release | Act s 2, line 66 | `oas-core-terms.l4`: `leaving custody in this way is a release _ _`, `Manner of release` | fork F7 |
| Review Tribunal | Act s 2, line 67 | repealed, 2012, c. 19, s. 235 | nothing to encode |
| second adjustment quarter | Act s 2, lines 68-72 | `oas-core-periods.l4`: `the second adjustment quarter in relation to the payment quarter containing _` | |
| special qualifying factor | Act s 2, lines 73-77 | `oas-core-pension.l4`: `the special qualifying factor of a person for the month containing _ _` | |
| specially qualified individual | Act s 2, lines 78-80 | `oas-core-pension.l4`: `the person is a specially qualified individual _` | fork F4 |
| spouse | Act s 2, line 81 | repealed, 2000, c. 12, s. 192 | the word is still used throughout; with no definition it is a plain fact (fork F9) |
| spouse's allowance | Act s 2, line 82 | repealed, 2000, c. 12, s. 192 | nothing to encode |
| supplement | Act s 2, line 83 | `oas-core.l4`: `Benefit` constructor `Supplement`; `oas-core-terms.l4`: `the Part of the Act under which the benefit is authorized _` | what Part II pays is oa2's |
| survivor | Act s 2, line 84 | `oas-core-terms.l4`: `the person is a survivor _ _` | |
| widow | Act s 2, line 85 | repealed, 2000, c. 12, s. 192 | nothing to encode |
| the amount of a full monthly pension | Act s 2.1(1), line 87 | `oas-core-pension.l4`: `the amount of a full monthly pension _ _` | selects the amount before any 7.1 increase (fork F8) |
| pensioner's monthly pension in ss 12(5) and 22(2) | Act s 2.1(2), line 89 | `oas-core-pension.l4`: `the pensioner's monthly pension in subsections 12(5) and 22(2) _ _` | |
| pension in s 12(5.1) | Act s 2.1(2), line 89 | `oas-core-pension.l4`: `the pension in subsection 12(5.1) _ _` | |
| base calendar year | Act s 10, line 232 (and s 22(1), line 644, "same meaning") | by reference: encoded by piece oa2, section 10, taken there as an input | the last calendar year ending before the current payment period |
| current payment period | Act s 10, line 233 (a second definition, for an allowance, at s 22(1), line 646) | by reference: encoded by piece oa2, sections 10 and 22(1) | the two definitions differ by benefit |
| previous payment period | Act s 10, line 234 | by reference: encoded by piece oa2, section 10 | |
| monthly base income | Act s 12(6), line 315 | by reference: encoded by piece oa2, section 12 | uses the keel's "income" and the amount of a full monthly pension "calculated without regard to subsection 7(5)" |
| first or second degree murder | Act s 21.1(6), line 635 | by reference: encoded by piece oa2, section 21.1 | |
| manslaughter | Act s 21.1(7), line 637 | by reference: encoded by piece oa2, section 21.1 | |
| current fiscal year | Act s 22(1), line 645 | repealed, 1998, c. 21, s. 116 | nothing to encode; oa2 records it in its coverage table |
| income, before July 1, 1999 | Act s 22(1), line 647, pointing to s 13, line 363 | by reference: encoded by piece oa2, sections 13 and 22(1) | a different definition of income for months before July 1, 1999; the keel's "income" is the current s 2 definition |
| monthly income of a survivor | Act s 22(1), line 648 | by reference: encoded by piece oa2, section 22 | |
| monthly joint income | Act s 22(1), line 649 | by reference: encoded by piece oa2, section 22 | |
| pension equivalent | Act s 22(1), line 652 | by reference: encoded by piece oa2, section 22 | the amount of the full monthly pension "that has not been increased under subsection 7(5)" (the V1 amount below) |
| residual income of the survivor | Act s 22(1), line 653 | by reference: encoded by piece oa2, section 22 | |
| residual joint income | Act s 22(1), line 660 | by reference: encoded by piece oa2, section 22 | |
| rounded pension equivalent | Act s 22(1), line 667 | by reference: encoded by piece oa2, section 22 | use the keel's `_ rounded to the next higher multiple of _` |
| rounded supplement equivalent | Act s 22(1), line 668 | by reference: encoded by piece oa2, section 22 | use the keel's `_ rounded to the next higher multiple of _` |
| supplement equivalent | Act s 22(1), line 669 | by reference: encoded by piece oa2, section 22 | |
| supplement equivalent for the survivor | Act s 22(1), line 670 | by reference: encoded by piece oa2, section 22 | |
| an incarcerated person described in subsection 5(3) | Act s 5(3), lines 131-133 (a described category, not a labelled definition) | by reference: encoded by piece oa1, section 5, taken there as an input; oa2 uses it at ss 19(1.1) and 22(1) | the keel's `Sentence of imprisonment` holds the sentence facts |
| administration | Act s 33(1), line 897 | by reference: encoded by piece oa1, section 33 | |
| federal institution | Act s 33(1), line 898 | by reference: encoded by piece oa1, section 33 | |
| public officer | Act s 33(1), line 899 | by reference: encoded by piece oa1, section 33 (and Regs 2(3), by oa3) | |
| document | Act s 44.2(1), line 1096 | by reference: encoded by piece oa1, section 44.2 | |
| dwelling-house | Act s 44.2(1), line 1097 | by reference: encoded by piece oa1, section 44.2 | |
| judge | Act s 44.2(1), line 1100 | by reference: encoded by piece oa1, section 44.2 | |
| Act | Regs 2(1), line 15 | by reference: encoded by piece oa3, section 2 | means the Old Age Security Act |
| appeal | Regs 2(1), line 16 | by reference: encoded by piece oa3, section 2 | |
| appellant | Regs 2(1), line 17 | by reference: encoded by piece oa3, section 2 | |
| application form | Regs 2(1), line 19 | by reference: encoded by piece oa3, section 2 | |
| beneficiary includes | Regs 2(1), line 20 | by reference: encoded by piece oa3, section 2 | widens the Act's "beneficiary" to a person on whose behalf a benefit has become payable |
| Court | Regs 2(1), line 22 | by reference: encoded by piece oa3, section 2 | the Tax Court of Canada; the keel's `Party` constructor `Tax Court of Canada` |
| reference | Regs 2(1), line 24 | by reference: encoded by piece oa3, section 2 | |
| request for reconsideration | Regs 2(1), line 26 | by reference: encoded by piece oa3, section 2 | |
| applicant, Board, Minister, Regional Director, Review Committee, Review Tribunal, secretary | Regs 2(1), lines 18, 21, 23, 25, 27, 28, 29 | repealed in the Regulations | oa3 records them; the Act's "applicant" and "Minister" are the keel's |
| residence and presence in Newfoundland | Regs 2(2), line 31 | by reference: encoded by piece oa3, section 2 | deems residence and presence in Newfoundland before union to be in Canada |
| prescribed individual | Regs 2(3), line 32 | by reference: encoded by piece oa3, section 2 | for the Act's "public officer" in s 33(1) |
| average of the Consumer Price Index for a period of months | Regs 9(1) and (2), lines 83-88 | by reference: encoded by piece oa3, section 9, on top of the keel's `the Consumer Price Index for an adjustment quarter _ _ _` | fork F10 |
| pension income | Regs 14, line 113 | by reference: encoded by piece oa3, section 14, taken by oa2 (s 14 of the Act) as an input | |
| resides in Canada, is present in Canada | Regs 21(1), lines 154-157 | by reference: encoded by piece oa3, section 21, taken by oa1 and oa2 as inputs | register entry below |
| legal residence | Regs 22(1), lines 231-236 | by reference: encoded by piece oa3, section 22, taken by oa1 (s 4(1)) and oa2 (ss 19(2), 21(2)) as an input | register entry below |
| events in relation to a sponsor | Regs 22.1(1), lines 247-251 | by reference: encoded by piece oa3, section 22.1, taken by oa2 (ss 11(8), 19(6.2), 21(9.1)) as an input | |
| average bank rate, bank rate, debt, demand for payment, due date | Regs 48(1), lines 344-350 | by reference: encoded by piece oa3, section 48 | |

Counted by kind, the table holds 81 defined terms: 24 encoded by the keel as a rule or a type, 1 not encoded by design (the convention for the word prescribed, explained in its row), 12 repealed in the text, and 44 by reference to another piece (7 to oa1, 16 to oa2, 21 to oa3).

## Instructions to the pieces

1. **What to import.** `IMPORT` of a hyphenated module needs backticks: ``IMPORT `oas-core` ``.
   Imports are transitive: a file that imports `oas-core-periods` alone already sees everything in `oas-core` and `oas-core-measures` (measured, with `YMD` and `Pension`).
   Import `oas-core` always and the others as you need them; a name defined in two imported modules, or defined again in the importer, is an error at the first use ("There are multiple definitions for the identifier").
2. **Do not define `YMD`.**
   Every stable-binary instruction tells a writer to add a local `YMD` shim, and this is the one place that does not apply: `oas-core.l4` already defines it, and a second definition in your piece fails with "There are multiple definitions for the identifier YMD" (measured).
   The same goes for every name in the list at the end of this section.
3. **Label every name you declare** with the section of the provision it encodes (`s 12(2): ...`), for rules, constants, types and constructors alike, so that the pieces compose without a clash; the keel's names carry no label, so no label ever clashes with a keel name.
4. **Tests go in their own files.**
   Keep `#ASSERT` out of every module another piece or a seat layer will import, and do not import any `oas-core-tests-*` file.
5. **Months.**
   Pass a month to a keel rule as any date in it; the rule normalises.
   The month for which a benefit is payable is the one that decides which dated paragraph of "income" applies, so `the income of a person for a calendar year _ _` takes that month first and the person's `Income facts` second.
   Call it once for the applicant and once for the spouse or common-law partner, each with their own `Income facts`.
6. **Income is not rounded and not limited to zero**, because the definition says neither (fork F11); where a provision of the Act rounds or floors an income, that provision's piece does it, with the helpers.
7. **Rounding.**
   Use `_ rounded to the next higher multiple of _`, `_ rounded to the next lower multiple of _` and `_ rounded half up to the number of decimal places _` and do not write your own; a rounding the text does not state is not applied.
8. **Time limits.**
   Write a limit as a `Time limit` (`a limit in days _`, `a limit in months _`, `a limit in years _`) and a deadline as `the day that is _ after _` or `the day that is _ before _`; a regulative rule's `WITHIN` counts days, and `the number of days from _ to _` gives that number.
9. **Ages.**
   `the day on which a person born on _ attains the age of _`, `the month in which a person born on _ attains the age of _` and `the age in complete years on _ of a person born on _`; the text gives no rule for the day an age is attained, so the anniversary of the birth is taken (fork F5).
10. **Where the Act says "the amount of a full monthly pension" or "pension" in a rule about the supplement or the allowance, there are three different amounts, and the Act says which one each place means.**
    oa1 works them out in Part I (ss 3(3), 7, 7.1) and oa2 takes them as inputs, under these exact names; the keel's rules in `oas-core-pension.l4` select among them.

    | amount | what it is | exact input name | where the Act uses it |
    | --- | --- | --- | --- |
    | V1 | the full monthly pension "calculated without regard to subsection 7(5)", that is, without the 10% increase at 75 | `the amount of the full monthly pension calculated without regard to subsection 7(5)` | s 12(6)(b)(i), line 322; "pension equivalent" in s 22(1), line 652 |
    | V2 | the full monthly pension "as it is calculated in accordance with section 7" (the 7(5) increase is in section 7, so it is in), not increased under subsection 7.1(1) or (2) | `the amount calculated in accordance with section 7, before any increase under subsection 7.1(1) or (2)` | s 2.1(1), line 87: the keel's `the amount of a full monthly pension _ _` |
    | V3 | the amount after any increase under subsection 7.1(1) or (2) (deferral of the application) | `the amount after any increase under subsection 7.1(1) or (2)` | what is actually payable; oa1's concern |

    For s 2.1(2) the keel's `the pensioner's monthly pension in subsections 12(5) and 22(2) _ _` and `the pension in subsection 12(5.1) _ _` take the pension before and after an increase under 7.1(1) or (2), under the input names in their `GIVEN` lines, and answer with the one before.
    Each of the three rules ignores its "after" argument by design: passing it is how the call site shows which amount the Act means, and a test shows the answer does not move when the "after" amount does.
11. **Inputs two pieces must name alike (the register).**
    The names are fixed so that a later composition can wire one piece's answer to another's input; where the Act's provision is time-indexed, the stem is fixed and the piece adds the Act's own time phrase.

    | input | type | what it stands for | answered by |
    | --- | --- | --- | --- |
    | `the Consumer Price Index for the first adjustment quarter that relates to the payment quarter` | NUMBER | the figure Regs 9 gives for the first adjustment quarter: the mean of the three monthly figures, rounded as Regs 9(2) says | oa3 Regs 9, on top of the keel's `the Consumer Price Index for an adjustment quarter _ _ _`; used by the ratio provisions Regs 8(1) lists: ss 7(2), 12(2), 12.1(3), 22(4.2), 22.1(4) |
    | `the Consumer Price Index for the second adjustment quarter that relates to the payment quarter` | NUMBER | the same, for the second adjustment quarter | the same |
    | `the person resides in Canada` | BOOLEAN | stem: Regs 21(1)(a), "makes his home and ordinarily lives in any part of Canada" | oa3 Regs 21 |
    | `the person is present in Canada` | BOOLEAN | stem: Regs 21(1)(b), "physically present in any part of Canada" | oa3 Regs 21 |
    | `the person is legally resident in Canada` | BOOLEAN | stem: ss 4(1), 19(2), 21(2), which Regs 22(1) explains; add the day as the Act words it | oa3 Regs 22 |
    | `the person is an incarcerated person described in subsection 5(3)` | BOOLEAN | the s 5(3) category, used by oa2 at ss 19(1.1) and 22(1) | oa1 s 5(3) |
    | `the prescribed time within which a request for cancellation may be made` | `Time limit` | ss 9.3(1) and 18.2(1) leave it to the regulations; Regs 26.1(1) says six months after payment commenced | oa3 Regs 26.1 |

    A fact you need from another piece that is not in the register: name it in the Act's words, and list it in your own NOTES.md so the composition can wire it.
12. **A party the core lacks.**
    A piece that needs a party `Party` does not name declares its own enumeration under its own label; `Other person` is there for the Act's "any person".
13. **Spouse.**
    The Act no longer defines "spouse" (fork F9); take "spouse or common-law partner" as a fact the person states, and call `the person is a common-law partner of the individual _ _ _ _` where the Act's test for a common-law partner is the question.
14. **Names the keel owns** (generated from the files when this file was written; do not declare any of them; an underscore stands for an argument):

**`oas-core.l4`**

- types: `Benefit`, `Kind of pension`, `Kind of allowance`, `Party`, `Calendar span`, `Unit of time`, `Time limit`, `Sentence of imprisonment`
- constructors: `Pension`, `Supplement`, `Allowance`, `Full monthly pension`, `Partial monthly pension`, `Allowance under section 19`, `Allowance under section 21`, `Minister`, `Governor in Council`, `Applicant`, `Beneficiary`, `Pensioner`, `Survivor`, `Spouse or common-law partner`, `Former common-law partner`, `Sponsor`, `Representative`, `Estate`, `Social Security Tribunal`, `Tax Court of Canada`, `Registrar of the Tax Court of Canada`, `Federal Court`, `Provincial or municipal authority`, `Statistics Canada`, `Minister of National Revenue`, `Other person`, `Days`, `Months`, `Years`
- rules and constants (an underscore stands for an argument):
  - `YMD _ _ _`

**`oas-core-measures.l4`**

- rules and constants (an underscore stands for an argument):
  - `the first day of the month containing _`
  - `the last day of the month containing _`
  - `the number of the month containing _`
  - `the first day of the month that is _ months after the month containing _`
  - `the number of months from the month containing _ to the month containing _`
  - `the day on which a person born on _ attains the age of _`
  - `the month in which a person born on _ attains the age of _`
  - `the age in complete years on _ of a person born on _`
  - `a limit in days _`
  - `a limit in months _`
  - `a limit in years _`
  - `the day that is _ after _`
  - `the day that is _ before _`
  - `the number of days from _ to _`
  - `_ rounded to the next higher multiple of _`
  - `_ rounded to the next lower multiple of _`
  - `_ rounded half up to the number of decimal places _`
  - `rounded to the nearest cent _`

**`oas-core-periods.l4`**

- rules and constants (an underscore stands for an argument):
  - `the month in which a fiscal year begins`
  - `the payment period in relation to the month containing _`
  - `the payment quarter containing the month containing _`
  - `the first adjustment quarter in relation to the payment quarter containing _`
  - `the second adjustment quarter in relation to the payment quarter containing _`
  - `the Consumer Price Index for an adjustment quarter _ _ _`

**`oas-core-terms.l4`**

- types: `Manner of release`
- constructors: `Release on earned remission`, `Release at the expiry of a sentence`, `Release on parole`, `Release on statutory release`, `Any other release from custody`
- rules and constants (an underscore stands for an argument):
  - `the person is an applicant _ _ _`
  - `the person is a beneficiary _`
  - `the person is a pensioner _`
  - `the person is a survivor _ _`
  - `the person is a common-law partner of the individual _ _ _ _`
  - `the instrument is a cheque _`
  - `leaving custody in this way is a release _ _`
  - `the Part of the Act under which the benefit is authorized _`

**`oas-core-pension.l4`**

- types: `Special qualification facts`
- rules and constants (an underscore stands for an argument):
  - `the person is a specially qualified individual _`
  - `the special qualifying factor of a person for the month containing _ _`
  - `the amount of a full monthly pension _ _`
  - `the pensioner's monthly pension in subsections 12(5) and 22(2) _ _`
  - `the pension in subsection 12(5.1) _ _`

**`oas-core-income.l4`**

- types: `Income facts`
- rules and constants (an underscore stands for an argument):
  - `the single amount deducted under subparagraph (a)(i) of the definition of income _ _`
  - `the deduction from income from office or employment under paragraph (a) of the definition of income _ _`
  - `the deduction from self-employment earnings under paragraph (b) of the definition of income _`
  - `the combined amount under paragraph (b.1) of the definition of income _ _`
  - `the deduction under paragraph (b.1) of the definition of income _ _`
  - `the deduction under paragraph (c) of the definition of income _`
  - `the deduction under paragraph (c.1) of the definition of income _ _`
  - `the deduction under paragraph (d) of the definition of income _`
  - `the net deduction under paragraph (e) of the definition of income _`
  - `the income of a person for a calendar year _ _`


## Coverage table

One row per heading, section, subsection, definition and paragraph of lines 13-91 of the Act.
The three sections in the range are 2, 2.1 and 2.2; the four headings are lines 13, 14, 86 and 88.
`encoded` means a rule or type carries it; `fork` means it is encoded on a reading the fork register explains; `inert` means no rule is possible or owed, with the reason; `repealed or blank in this text` means the text marks it repealed.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| "Interpretation" (heading) | 13 | inert | | A heading above s 2; it only names what follows (the definitions of s 2 and the two rules of s 2.1), and no rule is licensed by it, so it is carried by the section labels in the `@ref` lines and by nothing else. |
| "Definitions" (marginal note) | 14 | inert | | A marginal note labelling s 2; it adds nothing the definitions below it do not say. |
| s 2, introductory words "In this Act," | 15 | inert | | It says the definitions apply in the Act and states no rule; the encoding does not model the scope of a definition, so every keel rule is available to every piece. |
| allowance | 16 | encoded | `oas-core.l4` `Benefit`, `Kind of allowance`; `oas-core-terms.l4` `the Part of the Act under which the benefit is authorized _` | The Part that authorizes it (III); what it pays is oa2's. |
| applicant | 17 | encoded | `oas-core-terms.l4` `the person is an applicant _ _ _` | Applied, or deemed to have applied, or the requirement waived. |
| application | 18 | encoded | `oas-core-terms.l4`, carried by the inputs of `the person is an applicant _ _ _` | "Application means an application for a benefit": an alias with nothing to compute, so there is no separate rule; the Act's own phrase is used in the input names of the applicant rule (`the person has applied for a benefit`). |
| beneficiary | 19 | encoded | `oas-core-terms.l4` `the person is a beneficiary _` | |
| benefit | 20 | encoded | `oas-core.l4` `Benefit` | A pension, supplement or allowance. |
| cheque | 21 | encoded | `oas-core-terms.l4` `the instrument is a cheque _` | Any instrument issued in payment of a benefit. |
| common-law partner | 22 | fork | `oas-core-terms.l4` `the person is a common-law partner of the individual _ _ _ _` | F6: the relevant time of a living individual, and whether the anniversary day completes the year. |
| Consumer Price Index | 23 | encoded | `oas-core-periods.l4` `the Consumer Price Index for an adjustment quarter _ _ _` | The mean of three monthly figures; F10 records that the Regs 9 rounding is oa3's. |
| first adjustment quarter, (a)-(d) | 24-28 | encoded | `oas-core-periods.l4` `the first adjustment quarter in relation to the payment quarter containing _` | Four cases on the month the payment quarter begins; every payment quarter falls in one. |
| income, "except that" | 29 | encoded | `oas-core-income.l4` `the income of a person for a calendar year _ _` | Not rounded and not limited to zero (F11). |
| income (a)(i) | 30-33 | fork | `oas-core-income.l4` `the single amount deducted under subparagraph (a)(i) of the definition of income _ _` | F3: (a)(i) gives no amount for a month after June 2020, and the rule says NOTHING there. |
| income (a)(ii) and (iii) | 34-35 | encoded | `oas-core-income.l4` `the deduction from income from office or employment under paragraph (a) of the definition of income _ _` | Employment insurance premiums and Canada Pension Plan contributions, deducted for every month. |
| income (b) | 36-38 | encoded | `oas-core-income.l4` `the deduction from self-employment earnings under paragraph (b) of the definition of income _` | |
| income (b.1) | 39-41 | fork | `oas-core-income.l4` `the combined amount under paragraph (b.1) of the definition of income _ _`, `the deduction under paragraph (b.1) of the definition of income _ _` | F1: the condition "if those reduced self-employment earnings are greater than zero". |
| income (c) | 42-46 | encoded | `oas-core-income.l4` `the deduction under paragraph (c) of the definition of income _` | Four payments, each "to the extent that those amounts have been included in computing that income": the input is the amount included. |
| income (c.1) | 47-51 | encoded | `oas-core-income.l4` `the deduction under paragraph (c.1) of the definition of income _ _` | Months after June 2022 only. |
| income (d) | 52-55 | encoded | `oas-core-income.l4` `the deduction under paragraph (d) of the definition of income _` | Three times the excess, if any. |
| income (e) | 56 | encoded | `oas-core-income.l4` `the net deduction under paragraph (e) of the definition of income _` | Deduct the paragraph 56(1)(q.1) and subsection 56(6) amounts, add the paragraph 60(y) and (z) amounts. |
| Minister | 57 | encoded | `oas-core.l4` `Party` constructor `Minister` | |
| payment period, lead-in and (a) | 58-59 | fork | `oas-core-periods.l4` `the payment period in relation to the month containing _` | F2: the Act does not say when a fiscal year begins. |
| payment period (b) and (c) | 60-61 | encoded | `oas-core-periods.l4` `the payment period in relation to the month containing _` | April 1, 1998 to June 30, 1999, then July 1 to June 30. |
| payment quarter | 62 | encoded | `oas-core-periods.l4` `the payment quarter containing the month containing _` | The calendar quarter; every quarter lies inside one payment period (checked, no fork). |
| pension | 63 | encoded | `oas-core.l4` `Benefit`, `Kind of pension`; `oas-core-terms.l4` `the Part of the Act under which the benefit is authorized _` | The Part that authorizes it (I); what it pays is oa1's. |
| pensioner | 64 | encoded | `oas-core-terms.l4` `the person is a pensioner _` | |
| prescribed | 65 | inert | | "Prescribed means prescribed by the regulations": an interpretive pointer with nothing to compute; the convention for a prescribed figure (an input named `the prescribed ...`, the figure being in oa3's encoding of the Regulation) is under "Naming conventions". |
| release | 66 | fork | `oas-core-terms.l4` `leaving custody in this way is a release _ _`, `Manner of release` | F7: what "that has not been terminated or revoked" qualifies. |
| Review Tribunal | 67 | repealed or blank in this text | | "[Repealed, 2012, c. 19, s. 235]". |
| second adjustment quarter, (a)-(d) | 68-72 | encoded | `oas-core-periods.l4` `the second adjustment quarter in relation to the payment quarter containing _` | |
| special qualifying factor, (a), (b)(i), (ii) | 73-77 | encoded | `oas-core-pension.l4` `the special qualifying factor of a person for the month containing _ _` | One before April 1996 and for anyone not specially qualified; otherwise the whole years of residence over ten. |
| specially qualified individual, (a), (b) | 78-80 | fork | `oas-core-pension.l4` `the person is a specially qualified individual _` | F4: the day the ten years are counted to, and what the "where" clause of (b) qualifies. |
| spouse | 81 | repealed or blank in this text | | "[Repealed, 2000, c. 12, s. 192]"; the word is still used, see F9. |
| spouse's allowance | 82 | repealed or blank in this text | | "[Repealed, 2000, c. 12, s. 192]". |
| supplement | 83 | encoded | `oas-core.l4` `Benefit`; `oas-core-terms.l4` `the Part of the Act under which the benefit is authorized _` | The Part that authorizes it (II); what it pays is oa2's. |
| survivor | 84 | encoded | `oas-core-terms.l4` `the person is a survivor _ _` | |
| widow | 85 | repealed or blank in this text | | "[Repealed, 2000, c. 12, s. 192]". |
| "Amount of full monthly pension" (marginal note) | 86 | inert | | A marginal note above s 2.1(1). |
| s 2.1(1) | 87 | fork | `oas-core-pension.l4` `the amount of a full monthly pension _ _` | F8: whether the 7(5) increase and the 7.1(5) and (6) increases are in or out. |
| "Monthly pension" (marginal note) | 88 | inert | | A marginal note above s 2.1(2). |
| s 2.1(2) | 89 | fork | `oas-core-pension.l4` `the pensioner's monthly pension in subsections 12(5) and 22(2) _ _`, `the pension in subsection 12(5.1) _ _` | F8, same reading. |
| s 2.2 | 90 | repealed or blank in this text | | "[Repealed, 2016, c. 7, s. 188]". |

Counts: 43 rows for the 3 sections (2, 2.1, 2.2) and 4 headings of the range, of which 24 encoded, 8 fork, 6 inert and 5 repealed or blank in this text.

## Fork register

Every ambiguity the keel met, the readings it saw, the one it took, and why.
A fork the courts or the regulator has settled would say who settled it; none of these is, to the keel's knowledge, settled, and the keel has no access to case law or administrative guidance, so none is settled here by authority.

| id | provision | readings seen | taken, and why | where |
| --- | --- | --- | --- | --- |
| F1 | s 2 "income" (b.1), line 39: "the aggregate of [employment income as reduced] and [self-employment earnings as reduced], if those reduced self-employment earnings are greater than zero" | (1) the self-employment component joins the aggregate only when it is greater than zero; (2) the whole combined amount exists only when the reduced self-employment earnings are greater than zero | (1). Reading (2) gives a person with employment income and no self-employment income no deduction at all from July 2020, in the very paragraph that replaces the (a)(i) deduction; the keel judged that unlikely and took the reading that keeps it. Not checked against any official guidance. | `oas-core-income.l4`; test: reduced self-employment earnings of -200 leave a combined amount of 8000, not 7800 |
| F2 | s 2 "payment period" (a), line 59: "the fiscal year that includes the month, where the month is before April, 1998" | the Act does not say when a fiscal year begins: April 1 to March 31, or the calendar year | April 1 to March 31, because paragraph (b) starts the next period on April 1, 1998, straight after a fiscal year that would then end on March 31, 1998. An inference, held in one named constant, `the month in which a fiscal year begins`. | `oas-core-periods.l4`; tests for months in 1995 to 1998 |
| F3 | s 2 "income" (a)(i), lines 31-33: a single amount for a month before July 2008 (A) and for a month after June 2008 but before July 2020 (B) | for a month after June 2020 the subparagraph gives no amount: read as no deduction under (i) (but (ii) and (iii) remain), or as the (B) amount continuing | no amount under (i), which the rule says as NOTHING; paragraph (a) then adds only (ii) and (iii), and (b.1) deals with the combined amount from July 2020. | `oas-core-income.l4`; tests assert NOTHING |
| F4 | s 2 "specially qualified individual", lines 78-80 | (i) the day at which "an aggregate period of ten or more years" is counted: the definition names none; (ii) whether the "where, before March 7, 1996, the person was residing in Canada ..." clause limits (b) only, or (a) as well | (i) the last day of the immediately preceding month, the day the definition just above, "special qualifying factor", names for the same aggregate; (ii) (b) only, because the clause sits inside (b) after its own comma and (a) ends with "or". | `oas-core-pension.l4`; tests `the facts of 3 TRUE FALSE FALSE` and `3 FALSE TRUE FALSE` |
| F5 | the day a person attains an age (used by ss 7(5), 7.1(5) and (6), and the age tests) | the anniversary of the birth, or the day before | the anniversary of the birth: the inputs hold no rule that says otherwise. For a person born on 29 February in a year that follows a non-leap year, `add years` gives 28 February. | `oas-core-measures.l4`; tests for 15 March and 29 February births |
| F6 | s 2 "common-law partner", line 22: "cohabiting ... at the relevant time, having so cohabited ... for a continuous period of at least one year" | (i) the relevant time of an individual who has not died: the day of the application, of the approval, of the month in question, or the day the question is asked; (ii) whether a period that began exactly one year before the relevant time is "at least one year" | (i) the day the question is asked, passed in as an input, so the calling provision says which day it means; the text fixes the relevant time only for a death; (ii) yes: the period is at least a year on its anniversary. | `oas-core-terms.l4`; tests on 14 and 15 March and on 29 February 2024 |
| F7 | s 2 "release", line 66: "on parole or statutory release that has not been terminated or revoked" | the qualifier belongs to statutory release only, or to parole and statutory release | both: a parole that has been revoked is not a release. | `oas-core-terms.l4`; tests for parole and statutory release with `TRUE` |
| F8 | s 2.1, lines 87 and 89: "has not been increased under subsection 7.1(1) or (2)" | whether (i) the 10% increase at 75 in s 7(5) is excluded too; (ii) the increases in 7.1(5) and (6), which apply to an amount "as it is increased under subsection (1)" or "(2)", are excluded | (i) s 7(5) is included: s 2.1(1) says "as it is calculated in accordance with section 7", which contains 7(5), and where the Act wants 7(5) left out it says so (s 12(6)(b)(i), s 22(1) "pension equivalent"); (ii) excluded, because they are increases of the amount 7.1(1) and (2) have already increased. | `oas-core-pension.l4`; register in "Instructions to the pieces", item 10 |
| F9 | "spouse", line 81, repealed in 2000 and still used in "survivor", "common-law partner", ss 12, 19, 21 and elsewhere | the text defines no legal test for a spouse | a plain fact the person states; the keel invents no test. | `oas-core-terms.l4` input `the person's spouse or common-law partner has died`, and the `Party` constructor |
| F10 | s 2 "Consumer Price Index", line 23: "the average", and Regs 9(1) and (2) | whether the Act's "average" is the exact mean, or the mean expressed as Regs 9(2) says (to one decimal place) | the keel gives the exact mean and nothing else; Regs 9 is oa3's, and the ratio provisions of the Act take the Regs 9 figure (register, item 11). This is a boundary between pieces and not a doubt about the text. | `oas-core-periods.l4`; test with 158.4, 159.0, 160.2 |
| F11 | s 2 "income" as a whole | a negative result (deductions larger than the starting figure): floored at zero, or left negative | left negative, because the definition does not floor it; a provision that needs a floor says so. | `oas-core-income.l4`; test: 1000 less 3500 is -2500 |

**Where the keel looked and found no fork.**
The four paragraphs of "first adjustment quarter" and of "second adjustment quarter" cover every payment quarter, because a quarter begins on April 1, July 1, October 1 or January 1, and the payment quarter rule cannot return any other start.
Every payment quarter lies inside one payment period, because each of the three periods starts on April 1 or July 1 and ends on March 31 or June 30 (the one in paragraph (b) is fifteen months, five quarters).
Section 2.2 and the four repealed definitions are marked repealed in the text and nothing further depends on them.
The Act's `RELATED PROVISIONS` and `AMENDMENTS NOT IN FORCE` (from line 1146) were read for anything touching sections 2, 2.1 and 2.2, and none amends them.
Two related provisions refer to them: 2012, c. 19, s. 262 keeps the repealed provisions, and with them the "Review Tribunal", in force for appeals already begun, and 2021, c. 23, s. 275 pays pensioners "as defined in section 2", which "income" (c)(i.1) cites by name; both belong to oa1.
The amendments not in force replace subsections 19(4) and 21(4) and section 24(1) and add provisions after section 26; none touches the interpretation provisions.

## What the stable binary does not accept

The target is `main`, build `1.6.98 (main, 7689b0d, 2026-10-19)`.
The first list is what `references/dialects.md` of the writing skill says for this build, read and not re-measured by the keel; the second is what the keel itself met while writing.

From `dialects.md`, each with what to write instead:

- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (except `LEST BREACH ... BECAUSE`): return a `MAYBE` with `NOTHING` for a case not covered, and assert it.
- A section `GIVEN` (the next rule only, with seven different messages): a `GIVEN` on every rule.
- `TYPICALLY` on a field or a `GIVEN`: leave it out and put the presumed value in the `@desc`.
- `YMD`: absent from the prelude; the keel's shim is in `oas-core.l4`, and a `YMD` compared without brackets fails with a `__GEQ__` message, so write `d AT LEAST (YMD 2008 7 1)` or `d AT LEAST (Date 1 7 2008)`.
- `@lang`, `@infixl`, `@infixr`, `@infix`, `@nonassertable`, `@nonexhaustive` and any unknown `@word`: leave out; `@export`, `@desc`, `@nlg`, `@ref`, `@ref-map` and `@ref-src` are fine.
- Sets (`SET OF`, `setFromList`, `UNION`, `setSize`, `is in`): a `LIST OF` and `elem`.
- `DECLARE Applicant` with no body (an opaque type): give the type one field.
- An infix `EXPONENT` in a module with an `IMPORT` is an error on `unstable` and fine on `main`; the keel uses the prefix `EXPONENT 10 n`, which both read.
- `NOT a AND b` with no brackets is read as `NOT (a AND b)` on `main` without a word: bracket every `NOT`.
- An input named in an action (`MUST Pay Borrower creditor 10`) matches any payload on `main`: use `PROVIDED payee EQUALS creditor`.
- A rule applied inside `MUST (...)`, a field read in an action's argument, `MUST DO`, `` `IS INTEGER` `` (spelled `ISINTEGER` on main), `` `WAIT UNTIL` `` (spelled `WAITUNTIL`), the ledger (`RECORD`, `COMMIT`, `ATTEST`, `RECALL`), `EVERY`, `WITHIN 5 OF THE DEADLINE` and the temporal built-ins: see the file; none is used in the keel.

Met by the keel, measured on 1.6.98:

- There is no record update: `base WITH a IS 10`, where `base` is a value, fails with "You are trying to apply"; construct the record in full, or write a helper that takes the varying fields (the income tests do the second).
- A mixfix name with a keyword after its last argument (`x `rounded half up to` n `decimal places``) was not found at the call site (error: could not find a definition for `decimal places`), even with the argument in brackets; end a pattern on an argument, as `_ rounded half up to the number of decimal places _` does.
- A name defined in two imported modules, or in an imported module and again in the importer, is an error at the first use ("There are multiple definitions for the identifier"); the same field name in two records is accepted, even across imports.
- A `§` heading does not hide a name from an importer.
- Diamond imports (two modules that both import `oas-core`, imported together) work.
- `add months` and `add years` accept a negative count and clamp to the end of a shorter month; `Days in month`, `DATE_YEAR`, `DATE_MONTH`, `FLOOR`, `CEILING`, `min` and `max` all work; a DATE minus a NUMBER is a number of days.
- The brief's rule that every `#ASSERT` sits on one line was kept; no assertion was written across lines.

## What check.sh prints

Run from this folder with `L4` set to the stable binary and `L4_TARGET=unstable`, exactly as the brief says:

```
L4=<L4_BIN> L4_TARGET=unstable ./check.sh
```

The binary is itself a `main` build, so every module was already read by `main`; the target `unstable` only skips the second run of the same binary, and the first line says so.
The exit status was 0.
The print was:

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
oas-core-income.l4                             0         0       0        0         0
oas-core-measures.l4                           0         0       0        0         0
oas-core-pension.l4                            0         0       0        0         0
oas-core-periods.l4                            0         0       0        0         0
oas-core-terms.l4                              0         0       0        0         0
oas-core-tests-income.l4                       0        42       0        0         0
oas-core-tests-measures.l4                     0        60       0        0         0
oas-core-tests-pension.l4                      0        31       0        0         0
oas-core-tests-periods.l4                      0        59       0        0         0
oas-core-tests-terms.l4                        0        37       0        0         0
oas-core.l4                                    0         0       0        0         0
TOTAL (11 modules)                             0       229       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

How to read it: `errors` counts error diagnostics (a failed assertion is one), `satisfied` the assertions that held, `failed` those that did not, `refused` those that refused, and `expected` the failures the module declares it expects (none here).
A green run needs 0 in `errors`, `failed` and `refused`; the exit status alone is not enough, because `l4 run` exits 0 when an assertion refuses.
The script runs every `.l4` in its folder, so a piece's folder holds the piece's modules and tests and nothing from another piece.
