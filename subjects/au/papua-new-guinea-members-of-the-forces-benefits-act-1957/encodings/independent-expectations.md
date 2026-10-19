# Independent expectations: Papua New Guinea (Members of the Forces Benefits) Act 1957

Written from BRIEF.md and the Act only, before reading any .l4 file.

## Baseline facts ("the baseline member")

Male; indigenous inhabitant of Papua New Guinea; served in the Defence Force from 1 March 1942 to 1 June 1944; rate of pay below the minimum prescribed for a male member of the Australian Military Forces; service terminated by discharge.

## Scenarios

| # | Facts (change from baseline) | Expected | Working / words of the Act |
|---|---|---|---|
| 1 | Baseline | member of the Forces = YES | s 3: "male indigenous inhabitant of Papua New Guinea ... who served during the war in the Defence Force at a rate of pay less than the minimum ... and whose service has been terminated by discharge or death" - every limb met |
| 2 | Female | member = NO | s 3 "male" |
| 3 | Pay equal to the minimum AMF rate | member = NO | s 3 "less than the minimum rate" - equal is not less |
| 4 | Still serving, not discharged, not dead | member = NO | s 3 "whose service has been terminated by discharge or death" |
| 5 | Service terminated by death | member = YES | same words, "or death" |
| 6 | Indigenous inhabitant of an island forming part of the territory of a State (e.g. a Torres Strait island, Qld) | member = NO | s 3 "(other than an island forming part of the territory of a State)" |
| 7 | Indigenous inhabitant of a Pacific island not part of a State (e.g. Solomon Islands) | member = YES | s 3 "or of an island in the Pacific Ocean" |
| 8 | Service only from 1 Oct 1945 to 1 Mar 1946 | member = NO | brief: war = 3 Sep 1939 to before 3 Sep 1945 |
| 9 | Service only on 2 Sep 1939 | member = NO | the war "commenced on the third day of September 1939" |
| 10 | Service 3 Sep 1939 (first day) | member = YES | start day inclusive |
| 11 | Baseline; incapacity resulted from an occurrence during war service; no s 5(3) exclusion | Commonwealth liable = YES | s 5(1)(a) |
| 12 | Baseline; no occurrence, but incapacity arose out of / attributable to service | liable = YES | s 5(1)(b) |
| 13 | Baseline; cause existed before service; incapacity aggravated (or materially contributed to) by service conditions; nothing else | liable = YES | s 5(2) deems it attributable, so s 5(1)(b) |
| 14 | Pre-existing cause, NOT aggravated or materially contributed to; no occurrence; not otherwise attributable | liable = NO | none of s 5(1)(a), (b), (2) |
| 15 | As 11 but due to serious default or wilful act | liable = NO | s 5(3)(a) |
| 16 | As 11 but intentionally self-inflicted injury | liable = NO | s 5(3)(b) |
| 17 | As 11 but arose from a serious breach of discipline | liable = NO | s 5(3)(c) |
| 18 | As 11 but the person is not a member (e.g. female) | liable = NO | s 5 applies to "a member of the Forces" |
| 19 | Benefit source: this Act / War Gratuity Act 1945-1947 / any other law (e.g. general repatriation law) | eligible YES / YES / NO | s 4 "(a) by and under this Act; and (b) by and under the War Gratuity Act 1945-1947; and no others". s 6 "prescribed" benefits are "under this Act" |
| 20 | Pension: sale, assignment, charge, execution, bankruptcy | can be taken = NO in every case | s 8 "absolutely inalienable, whether by way or in consequence of sale, assignment, charge, execution, bankruptcy or otherwise" |
| 21 | Death of member from an occurrence in war service | liable (to dependants) = YES | s 5(1) "incapacity or death" |

## Where I read the Act differently from the brief

- **End of "the war".** The brief says the war runs "3 September 1939 to before 3 September 1945". The Act does not give an end date for the war: it says the war "commenced" on 3 Sep 1939 and "includes any other war in which His late Majesty became engaged after that date and before" 3 Sep 1945. The 1945 date limits which *other* wars are included, not when service stops counting. Read strictly, service after 2 Sep 1945 but before the war formally ended (it formally ended, for Australian legal purposes, in 1952) could still be "during the war". I test scenario 8 on the brief's reading (NO) and record this as a reading difference, not a code defect.
- **Liability also needs the member to be a member.** s 5 depends on s 3; I test that (scenario 18).
- s 5(1) liability is "subject to such conditions as are prescribed" - the regulations are not encoded; ignored.

## Added after reading the module (step 3)

| # | Facts | Expected | Working |
|---|---|---|---|
| 22 | Baseline but enlisted 1 Aug 1939 and served on through 1942 | member = YES | s 3 asks whether the man "served during the war", not when he enlisted; service from 3 Sep 1939 onwards is during the war |

This scenario was added once I saw the module records only the date service began. The expected value comes from the Act, not from the code.
