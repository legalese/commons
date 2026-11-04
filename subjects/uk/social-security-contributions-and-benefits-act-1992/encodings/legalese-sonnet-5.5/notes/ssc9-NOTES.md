# NOTES -- ssc9: Schedules 5, 5A, 6, 7, 8, 9, 10, 11, 12, 13 and the Table of Derivations (lines 5067-5744)

Social Security Contributions and Benefits Act 1992 (United Kingdom), 1992 c. 4.
Part agent `ssc9`, run `iaw-ssc9`, encoding `legalese-sonnet-5.5`.

## Status and how each claim here was checked

- **The source is a converter rendering, not the official text.**
  `inputs/ukpga-1992-4.txt` is a plain-text rendering made by a converter script from legislation.gov.uk (point in time 2026-07-08).
  Nothing in this encoding is "verified against the official text".
  The rendering drops paragraph numbers and some limb labels, omits the Act's tables (Schedule 4 among them), and shows repealed text as lines of dots.
- **Verified by running, 2026-11-04.**
  `check.sh` (printout at the end of this file) ran every module on the stable build 1.6.98 and on the main build 1.6.108 and found the same four counts on both for all 25 modules.
  `srcrefs.py check --refs ... --strict` on the 24 `ssc9-*.l4` files reported 0 problems (printout in the section "What check.sh and srcrefs print").
  The coverage table was built by `work/make-coverage.py` from the `@ref` locators in the `.l4` files plus hand-written rows, and the script checked that every one of the 678 lines of 5067-5744 is in some row.
- **Expected values were written by hand from the text** before the code was run, never copied from the code's output.
  Where my own expectation was wrong, the expectation was fixed because the text said otherwise, and no expectation was edited to match the code.
  The slips and corrections are recorded in finding 25.
- **Not verified:** any reading of a provision against the official text; any amount (every figure the Act leaves to Schedule 4, regulations or an order is an input); `#TRACE` outcomes beyond what the six traces print (the stable binary has no assertion for a trace outcome).
- **No lawyer has read this.**
  The two readings that the brief marks "for a lawyer" are listed under "Marginal readings for a lawyer".

## The seat (statement)

**Seat: the individual to whom Schedules 5 to 13 are applied.**
In this range that person is a pensioner who deferred a retirement pension or a shared additional pension (Schedules 5 and 5A), their surviving spouse or civil partner (Schedule 5), a person whose disablement is assessed (Schedule 6), someone claiming an industrial injuries benefit or the widow, widower or child of a person who died of an industrial injury (Schedule 7), a parent or carer claiming Child Benefit (Schedules 9 and 10), and an employee asking about statutory sick pay or statutory maternity pay (Schedules 11 to 13).
No question is asked from the seat of the Secretary of State, the Treasury, an adjudicating authority or an employer's payroll office.
A provision that addresses only an official is encoded in layer 1 for what it decides, and in layer 2 only where it means something to the person (what may be done to them, what they must be given, by when).
The seat layer is two files, `ssc9-seat.l4` (53 questions, each with `@export` and `@desc`, every name beginning "Under schedule N paragraph M,", grouped under `§` headings in the text's order) and `ssc9-cases-seat.l4` (185 assertions, hand-derived).
The seat layer imports the layer-1 modules and calls their rules; it restates no rule.
One question name is a composite over several paragraphs and says so, `Under schedule 10 paragraphs 1 to 5, ...`, because the five priority rules are read together and each decides only when the earlier ones do not; every other question names one paragraph.
A few helper functions in the seat file (the person's choice turned into the module's election) are not questions, carry no `@export`, and begin "Under schedule 5" so that no name clashes.

## Files

| file | holds |
| --- | --- |
| `ssc9-sch5.l4`, `ssc9-tests-sch5.l4` | Schedule 5 paragraphs A1 to 3B: the pensioner's own deferment |
| `ssc9-sch5-w.l4`, `ssc9-tests-sch5-w.l4` | Schedule 5 paragraphs 3C to 9: the surviving spouse or civil partner |
| `ssc9-sch5a.l4`, `ssc9-tests-sch5a.l4` | Schedule 5A: deferred shared additional pension |
| `ssc9-sch6.l4`, `ssc9-tests-sch6.l4` | Schedule 6: assessment of the extent of disablement (answers seam S21) |
| `ssc9-sch7-p1.l4`, `ssc9-tests-sch7-p1.l4` | Schedule 7 Part I: unemployability supplement and its increases |
| `ssc9-sch7-p2.l4`, `ssc9-tests-sch7-p2.l4` | Schedule 7 Parts II and III: disablement gratuity; hospital treatment |
| `ssc9-sch7-p4.l4`, `ssc9-tests-sch7-p4.l4` | Schedule 7 Parts IV and V: reduced earnings allowance; retirement allowance |
| `ssc9-sch7-p6.l4`, `ssc9-tests-sch7-p6.l4` | Schedule 7 Part VI: industrial death benefit |
| `ssc9-sch9-10.l4`, `ssc9-tests-sch9-10.l4` | Schedule 9 (exclusions) and Schedule 10 (priority) for child benefit |
| `ssc9-sch11.l4`, `ssc9-tests-sch11.l4` | Schedule 11: circumstances in which statutory sick pay does not arise |
| `ssc9-sch12-13.l4`, `ssc9-tests-sch12-13.l4` | Schedules 12 and 13: statutory sick pay and statutory maternity pay against other benefits |
| `ssc9-seat.l4`, `ssc9-cases-seat.l4` | the seat layer and its cases |
| `NOTES.md`, `PROGRESS.md` | this file; the progress log |

Schedule 8 has no module: every one of its paragraphs is a line of dots in this text, so its rows are "repealed or blank in this text".
The Table of Derivations has no module: it is a note about where provisions came from, and its rows are not in this text.
`NEEDS-CORE.md` is not written: no core type or constructor was lacking.
The types and constructors this part declares for itself (`sch 5 Election`, `sch 6 Circumstance`, `sch 7 pt IV Extent`, `sch 10 para 1 Place`, `sch 10 para 5 Election` and the like) all begin with their provision label, as the naming rule requires.

## PLAN.md and the brief: where they differ (the brief governs)

1. **The range.**
   The brief and PLAN.md say lines 5067-5745.
   The file has 5744 lines, so the last line of the range is 5744.
2. **Dispositions for blank text.**
   PLAN.md section 1.5 gives each line of dots a row `repealed or blank in this text`; the brief also lists "text shown repealed or blank" as a third reason for `inert`.
   I used the disposition `repealed or blank in this text` for every such row, so no row in the table is "inert, reason 3".
3. **Modules that import each other.**
   PLAN.md section 1.1 says a module starts with the three lines `IMPORT prelude`, `IMPORT daydate`, `IMPORT \`ssc-core\`` "and imports nothing else of the family".
   Four of my modules also import another ssc9 module (`ssc9-sch5-w` and `ssc9-sch5a` import `ssc9-sch5`; `ssc9-sch6` imports `ssc9-sch7-p2`; `ssc9-sch7-p6` imports `ssc9-sch7-p1`) so that one definition is not restated.
   I read "the family" as the other parts; the lead should say if that reading is wrong, because the merged folder then has the same names reachable in two ways.
4. **Test files.**
   PLAN.md names `ssc3-tests.l4` (one test file per part); the brief asks for a case file for the seat and a test for each rule.
   Each module has its own `ssc9-tests-*.l4`, all beginning with the part prefix.
5. **Seam types.**
   Every seam input has the type the plan gives: `BOOLEAN` for S32 and S33, and the `MAYBE` type for the rest.
6. **The keel's F1.**
   The keel's NOTES.md has its own fork F1 (the leap-day case in K2).
   The fork ids in this file are ssc9's; my F1 is a related but different fork (the 12 months of a deferment that began on 29 February).

## Paragraph labels that are inferred

The converter dropped the paragraph numbers, so every label is either one that an in-text citation gives (the citation is named here with its line) or is counted from the nearest cited number and is marked "inferred" in the coverage table.
Where a label could be checked against a citation, it was; the others rest only on the order of the text.

- **Schedule 5.**
  Section 55(2) (src:1687-1693) lists the Schedule's paragraphs as A1; 1 to 3; 3A and 3B; 3C; 4 to 7; 7A and 7B; 7C to 9, which fixes the last paragraph, `Uprating` (src:5291-5292), as paragraph 9 and the "Married couples and civil partners" paragraph (src:5284-5290) as one of 7C to 9.
  A1, 3A, 3B, 3C, 5 to 6A, 7A and 7B are also cited from inside the Schedule (for example "paragraph A1(1)(b)" at src:5101, "paragraph 3B" at src:5110, "paragraphs 5 to 6A" at src:5078, "paragraphs 3B and 7B" at src:5281).
  **Paragraph 2A is inferred.**
  It is cited nowhere in this text; it is the paragraph at src:5098-5103 that sits between paragraph 2 and the power paragraph, and "paragraphs 1 to 3" at src:1688 allows lettered paragraphs between them.
  The power paragraph at src:5104-5105 is labelled 3, from "Subject to paragraph 3 below" at src:5084 and src:5088.
  The unnumbered paragraph at src:5222-5243 that modifies paragraphs 5A to 6A is labelled "unnumbered paragraph following paragraph 7(3)".
  The paragraph 8 sub-paragraphs (1) to (3) at src:5285-5287 and the paragraph 7(1) at src:5215 are lines of dots, labelled by the order of the text.
- **Schedule 5A.**
  Section 55C(2) (src:1744-1746) lists paragraph 1 (election), paragraphs 2 and 3 (increase) and paragraphs 4 and 5 (lump sum).
  The text cites "paragraph 2 (entitlement to increase of pension)" and "paragraph 4 (entitlement to lump sum)" at src:5296-5297, "paragraph 3" at src:5308 and "paragraph 5" at src:5321.
  src:4414 cites "paragraph 5(3) of Schedule 5A", which is the omitted formula.
- **Schedule 6.**
  Paragraph 1(d) or 2 is cited at src:5347 ("Regulations under paragraph 1(d) or 2 above").
  Paragraphs 4 and 6 are cited from Schedule 7 at src:5502 ("paragraph 4 or 6 of Schedule 6").
  Paragraphs 4 and 5 are the two lines of dots under the heading `Severe disablement allowance`, 6 is `Disablement benefit`; 3, 7 and 8 are counted from the order.
  **Paragraph 4 is blank in this text, yet src:5502 cites it** (finding 14).
- **Schedule 7.**
  The text cites Part II at src:5355, "paragraph 11(10) above" at src:5528 and src:5548, "paragraph 15 above" at src:5584, "paragraph 16 below" at src:5578, "paragraph 18 below" at src:5586, "paragraph 19 below" at src:5597 and "paragraph 18 above" at src:5605, and "paragraph 4 above" at src:5423.
  Paragraphs 1 to 3, 5 to 10, 12 to 14, 17, 20 and 21 are counted from those, and are inferred.
  The sub-paragraph numbers inside a paragraph are the text's own.
- **Schedule 8.**
  Paragraphs 1 to 6 and Parts II and III are counted from the headings, and are inferred; the headings cite "paragraph 2" (src:5629) and "paragraph 4" (src:5633, src:5635), which fits the count.
  All are blank.
- **Schedule 9.** Paragraphs 1 to 5 in order, inferred; 2, 4 and 5 are blank.
- **Schedule 10.** Paragraphs 1 to 6 in order; "paragraphs 1 to 5 above" at src:5670 fixes 6(2) as the paragraph after 5.
- **Schedule 11.**
  The text keeps the letters of paragraph 2 ((d), (dd), (f), (g), (h)) but loses the numbers of everything after it.
  The sentence at src:5673 is labelled "paragraph 1, concurrence sentence" because it speaks of "regulations under paragraph 1 above"; the rules after the definition of `relevant date` are labelled by what they qualify ("exception to paragraph 2(d)(i)", "joining rule for paragraph 2(f)", "paragraph 2(g) and its exception").
- **Schedules 12 and 13.**
  Schedule 12 cites "paragraph 4 below" (src:5708) and "paragraph 1 above" (src:5711); paragraphs 2, 5 and 6 are counted from the order.
  Schedule 13 paragraph 3(2) is cited by the core's quotation at src:3369 ("paragraph 3(2) of Schedule 13"); paragraphs 1 and 2 are counted from the order.

## Coverage (ssc9)

Lines 5067-5744 of `ukpga-1992-4.txt`: Schedules 5, 5A, 6, 7, 8, 9, 10, 11, 12 and 13, and the Table of Derivations.
Every row has exactly one disposition: `encoded`, `fork F<n>` (the text can be read two or more ways with different outcomes; the row points at the fork-register entry and at the rule that encodes the reading taken), `inert (reason 1 or 2)`, or `repealed or blank in this text`.
No row is `inert` for reason 3: text shown repealed or blank has its own disposition (section "PLAN.md and the brief", item 2).
A row for an `encoded` or `fork` unit lists the rules that carry its `@ref` (the file is in brackets); the rows were built by `work/make-coverage.py` from those `@ref` locators, so a row cannot cite a line the `.l4` file does not quote.

### Audit counts

- **Text units counted:** 678 non-blank lines in 5067-5744 (the range has 678 lines and none is blank). By kind: 485 numbered or lettered sub-paragraphs and limbs; 81 headings and Schedule titles (tab-indented lines); 78 other (unlabelled paragraphs, lead-ins and continuation lines); 26 lines of dots, or `...`; 8 defined terms.
- **Rows before the hand-written rows:** 216 `@ref` locators in the `.l4` files, which merge into 207 (lines, unit) rows; they left 174 non-blank lines in no row.
- **Rows after:** 313 (185 encoded, 22 fork, 64 inert (reason 1: not operative), 25 inert (reason 2: machinery), 17 repealed or blank in this text). Non-blank lines in no row: 0.
- **Forks:** twelve (F1 to F12), each with at least one row: F1 on 6, F2 on 2, F3 on 2, F4 on 3, F5 on 1, F6 on 2, F7 on 1, F8 on 1, F9 on 1, F10 on 1, F11 on 1, F12 on 1.

```
text lines 5067-5744: 678, non-blank: 678 (of which dots-only or `...`: 26)
encoded locator rows from @ref: 216; merged by (lines, unit): 207
hand-written rows: 106
total rows: 313
per disposition: {'inert (reason 1: not operative)': 64, 'fork': 22, 'encoded': 185, 'inert (reason 2: machinery)': 25, 'repealed or blank in this text': 17}
per fork: {'F1': 6, 'F2': 2, 'F3': 2, 'F4': 3, 'F5': 1, 'F6': 2, 'F7': 1, 'F8': 1, 'F9': 1, 'F10': 1, 'F11': 1, 'F12': 1}
non-blank lines in no row: 0
problems: 0
```

| Lines | Unit | Disposition | L4 name, or what the text shows |
| --- | --- | --- | --- |
| 5067-5068 | sch 5 title and heading of paragraph A1 | inert (reason 1: not operative) | title and heading |
| 5069 | sch 5 para A1(1) | fork F1 | `sch 5 para A1(1) the period of deferment is at least 12 months` (ssc9-sch5.l4) |
| 5069-5071 | sch 5 para A1(1) | fork F1 | `sch 5 para A1(1) the person must elect` (ssc9-sch5.l4) |
| 5069-5072 | sch 5 para A1(1) and (2) | encoded | `sch 5 para A1(1) the election duty` (ssc9-sch5.l4) |
| 5072 | sch 5 para A1(2) | encoded | `sch 5 para A1(2) the election that is treated as made` (ssc9-sch5.l4) |
| 5073-5077 | sch 5 para A1(3) | inert (reason 2: machinery) | power for regulations to let a person change an election and to recover, or credit as paid on account, an amount to avoid duplicated payment; the regulations are not among the sources |
| 5078 | sch 5 para A1(4) | encoded | `sch 5 para A1(4) the weekly rate to which an election applies` (ssc9-sch5.l4) |
| 5079 | heading `Increase of pension where pensioner’s entitlement is deferred` | inert (reason 1: not operative) | heading |
| 5080-5082 | sch 5 para 1(1) | fork F1 | `sch 5 para 1(1) this paragraph applies` (ssc9-sch5.l4) |
| 5080-5083 | sch 5 paras 1 and 2 | encoded | `sch 5 para 1 the amount by which the pension is increased for the deferment` (ssc9-sch5.l4) |
| 5083 | sch 5 para 1(2) | fork F2 | `sch 5 para 1(2) the amount by which the rate of the pension is increased` (ssc9-sch5.l4) |
| 5084 | sch 5 para 2(1) | encoded | `sch 5 para 2(1) the number of increments` (ssc9-sch5.l4) |
| 5084-5088 | sch 5 para 2 | encoded | `sch 5 para 2 the aggregate of the increments` (ssc9-sch5.l4) |
| 5085-5086 | sch 5 para 2(2) | fork F3 | `sch 5 para 2(2) the number of complete incremental periods` (ssc9-sch5.l4) |
| 5088 | sch 5 para 2(3) | encoded | `sch 5 para 2(3) the increment for one incremental period` (ssc9-sch5.l4) |
| 5089-5091 | sch 5 para 2(4) | encoded | `sch 5 para 2(4) the amount calculated under sub-paragraph (3) as rounded` (ssc9-sch5.l4) |
| 5092-5094 | sch 5 para 2(5) | encoded | `sch 5 para 2(5) the weekly rate of pension for sub-paragraph (3)` (ssc9-sch5.l4) |
| 5095 | sch 5 para 2(6) | encoded | `sch 5 para 2(6) the increase under section 47(1) that is counted` (ssc9-sch5.l4) |
| 5096 | sch 5 para 2(7) | encoded | `sch 5 para 2(7) the rate for an incremental period` (ssc9-sch5.l4) |
| 5097 | sch 5 para 2(8) | encoded | `sch 5 para 2(8) the weekly rate used for an increment` (ssc9-sch5.l4) |
| 5098-5101 | sch 5 para 2A(1) | encoded | `sch 5 para 2A(1) this paragraph applies` (ssc9-sch5.l4) |
| 5102 | sch 5 para 2A(2) | encoded | `sch 5 para 2A(2) the amount by which the rate of the pension is increased` (ssc9-sch5.l4) |
| 5103 | sch 5 para 2A(3) | encoded | `sch 5 para 2A(3) the increment for one incremental period` (ssc9-sch5.l4) |
| 5104-5105 | sch 5 para 3(1) and (2) (label inferred from the citation `Subject to paragraph 3 below` at src:5084) | inert (reason 2: machinery) | power for regulations to modify paragraph 2 where the pension rate changes during deferment, and to make consequential changes to paragraph 8(3) |
| 5106 | heading `Lump sum where pensioner’s entitlement is deferred` | inert (reason 1: not operative) | heading |
| 5107-5110 | sch 5 para 3A | encoded | `sch 5 para 3A(2) the person is entitled to a lump sum` (ssc9-sch5.l4) |
| 5111 | heading `Calculation of lump sum` | inert (reason 1: not operative) | heading |
| 5112 | sch 5 para 3B(1) | encoded | `sch 5 para 3B(1) the last accrual period beginning during the period of deferment` (ssc9-sch5.l4); `sch 5 para 3B(1) the lump sum before rounding` (ssc9-sch5.l4) |
| 5113-5114 | sch 5 para 3B(2) accrued amount, para 3B(3) | encoded | `sch 5 para 3B(3) the accrued amount for an accrual period` (ssc9-sch5.l4) |
| 5115 | sch 5 para 3B(2) | encoded | `sch 5 para 3B(2) an accrual period begins on the day` (ssc9-sch5.l4); `sch 5 para 3B(2) the days since the accrual period containing the day began` (ssc9-sch5.l4) |
| 5116-5119 | sch 5 para 3B(2) accrued amount, para 3B(3) | encoded | `sch 5 para 3B(3) the accrued amount for an accrual period` (ssc9-sch5.l4) |
| 5120-5122 | sch 5 para 3B(3) R | fork F4 | `sch 5 para 3B(3) the percentage rate R` (ssc9-sch5.l4) |
| 5123-5125 | sch 5 para 3B(4) | encoded | `sch 5 para 3B(4) the day a change in the base rate is treated as taking effect` (ssc9-sch5.l4) |
| 5126-5132 | sch 5 para 3B(5) and (6) | encoded | `sch 5 para 3B(5) the amount of pension counted for an accrual period` (ssc9-sch5.l4) |
| 5133 | heading `Choice between increase of pension and lump sum where pensioner’s deceased spouse or civil partner has deferred entitlement` | inert (reason 1: not operative) | heading |
| 5134-5138 | sch 5 para 3C(1) | encoded | `sch 5 para 3C(1) this paragraph applies` (ssc9-sch5-w.l4) |
| 5138 | sch 5 para 3C(1)(d) | fork F1 | `sch 5 para 3C(1)(d) S’s entitlement was deferred throughout the 12 months` (ssc9-sch5-w.l4) |
| 5139-5142 | sch 5 para 3C(2) and (3) | encoded | `sch 5 para 3C(2) the election duty` (ssc9-sch5-w.l4) |
| 5142 | sch 5 para 3C(3) | encoded | `sch 5 para 3C(3) the election that is treated as made` (ssc9-sch5-w.l4) |
| 5143-5147 | sch 5 para 3C(4) | inert (reason 2: machinery) | power for regulations to let W change an election and to recover, or credit as paid on account, an amount to avoid duplicated payment; the regulations are not among the sources |
| 5148 | sch 5 para 3C(5) | encoded | `sch 5 para 3C(5) the election affects the application of paragraphs 5 to 6A` (ssc9-sch5-w.l4) |
| 5149 | heading `Increase of pension where pensioner’s deceased spouse or civil partner has deferred entitlement` | inert (reason 1: not operative) | heading |
| 5150-5153 | sch 5 para 4(1) | encoded | `sch 5 para 4(1) this paragraph applies` (ssc9-sch5-w.l4) |
| 5154-5160 | sch 5 para 4(1A) and (3) | encoded | `sch 5 para 4(1A) the amount by which the rate of W’s pension is increased` (ssc9-sch5-w.l4) |
| 5161-5164 | sch 5 para 4(4) | encoded | `sch 5 para 4(4) the amount of the increase to which W is entitled` (ssc9-sch5-w.l4) |
| 5165 | sch 5 para 4(5) | encoded | `sch 5 para 4(5) this paragraph does not apply` (ssc9-sch5-w.l4) |
| 5166-5171 | sch 5 para 5(1) | encoded | `sch 5 para 5(1) this paragraph applies` (ssc9-sch5-w.l4) |
| 5166-5182 | sch 5 para 5 | encoded | `sch 5 para 5 the amount by which the rate of W’s pension is increased` (ssc9-sch5-w.l4) |
| 5172-5182 | sch 5 para 5(2) | encoded | `sch 5 para 5(2) the paragraph that sets out the amounts` (ssc9-sch5-w.l4) |
| 5183-5192 | sch 5 para 5A | encoded | `sch 5 para 5A the sum of the amounts` (ssc9-sch5-w.l4) |
| 5193-5206 | sch 5 para 6 | encoded | `sch 5 para 6 the sum of the amounts` (ssc9-sch5-w.l4) |
| 5207-5214 | sch 5 para 6A | encoded | `sch 5 para 6A the sum of the amounts` (ssc9-sch5-w.l4) |
| 5215 | sch 5 para 7(1) (label inferred) | repealed or blank in this text | a line of dots: shown blank in this text |
| 5216-5218 | sch 5 para 7(2) | encoded | `sch 5 para 7(2) the amount as rounded` (ssc9-sch5-w.l4) |
| 5219-5221 | sch 5 para 7(3) | encoded | `sch 5 para 7(3) the woman falls within this sub-paragraph` (ssc9-sch5-w.l4) |
| 5222-5239 | sch 5 unnumbered paragraph following paragraph 7(3), sub-paragraphs (1) to (4) and (6) | encoded | `sch 5 para after 7(3) the modification of paragraphs 5A to 6A applies` (ssc9-sch5-w.l4) |
| 5240-5242 | sch 5 unnumbered paragraph following paragraph 7(3), sub-paragraph (5) | fork F5 | `sch 5 para after 7(3) the appropriate amount` (ssc9-sch5-w.l4) |
| 5243 | sch 5 unnumbered paragraph following paragraph 7(3), sub-paragraphs (1) to (4) and (6) | encoded | `sch 5 para after 7(3) the modification of paragraphs 5A to 6A applies` (ssc9-sch5-w.l4) |
| 5244 | heading `Entitlement to lump sum where pensioner’s deceased spouse or civil partner has deferred entitlement` | inert (reason 1: not operative) | heading |
| 5245-5246 | sch 5 para 7A | encoded | `sch 5 para 7A(2) W is entitled to a widowed person’s or surviving civil partner’s lump sum` (ssc9-sch5-w.l4) |
| 5247 | heading `Calculation of widowed person’s or surviving civil partner's lump sum` | inert (reason 1: not operative) | heading |
| 5248 | sch 5 para 7B(1) | encoded | `sch 5 para 7B(1) the lump sum before rounding` (ssc9-sch5-w.l4) |
| 5248-5252 | sch 5 para 7B(1) and (2) | encoded | `sch 5 para 7B(1) the last accrual period beginning during the period before S’s death` (ssc9-sch5-w.l4) |
| 5253 | sch 5 para 7B(2) accrued amount, para 7B(3) | encoded | `sch 5 para 7B(3) the accrued amount for an accrual period` (ssc9-sch5-w.l4) |
| 5254 | sch 5 para 7B(1) and (2) | encoded | `sch 5 para 7B(1) the last accrual period beginning during the period before S’s death` (ssc9-sch5-w.l4) |
| 5255 | sch 5 para 7B(2) accrued amount, para 7B(3) | encoded | `sch 5 para 7B(3) the accrued amount for an accrual period` (ssc9-sch5-w.l4) |
| 5256-5261 | sch 5 para 7B(3) P | encoded | `sch 5 para 7B(3) P, the amount of pension for the accrual period` (ssc9-sch5-w.l4) |
| 5262-5264 | sch 5 para 7B(3) R | fork F4 | `sch 5 para 7B(3) the percentage rate R` (ssc9-sch5-w.l4) |
| 5265-5267 | sch 5 para 7B(4) | encoded | `sch 5 para 7B(4) the day a change in the base rate is treated as taking effect` (ssc9-sch5-w.l4) |
| 5268-5273 | sch 5 para 7B(5) | encoded | `sch 5 para 7B(5) the amount of pension counted for an accrual period` (ssc9-sch5-w.l4) |
| 5274 | sch 5 para 7B(6) | encoded | `sch 5 para 7B(6) the increase under section 47(1) that is counted` (ssc9-sch5-w.l4) |
| 5275-5278 | sch 5 para 7B(7) | encoded | `sch 5 para 7B(7) the lump sum after the orders` (ssc9-sch5-w.l4) |
| 5279 | heading `Supplementary` | inert (reason 1: not operative) | heading |
| 5280 | sch 5 para 7C(1) | encoded | `sch 5 para 7C(1) the lump sum as rounded` (ssc9-sch5-w.l4) |
| 5281-5283 | sch 5 para 7C(2) | inert (reason 2: machinery) | duty on the Secretary of State, when prescribing a percentage rate for paragraphs 3B and 7B, to have regard to the national economic situation and other matters; the rate itself is an input |
| 5284 | heading `Married couples and civil partners` | inert (reason 1: not operative) | heading |
| 5285-5287 | sch 5 para 8(1), (2) and (3) (labels inferred) | repealed or blank in this text | three lines of dots: shown blank in this text |
| 5288 | sch 5 para 8(4) | encoded | `sch 5 para 8(4) the conditions in paragraphs 3C(1)(c) and 4(1)(a) are satisfied by S’s pension` (ssc9-sch5-w.l4) |
| 5289 | sch 5 para 8(5) | encoded | `sch 5 para 8(5) the increase or lump sum to which W is entitled under paragraph 4(1A) or 7A(2)` (ssc9-sch5-w.l4) |
| 5290 | sch 5 para 8(6) | encoded | `sch 5 para 8(6) the meaning of the letter` (ssc9-sch5-w.l4) |
| 5291 | heading `Uprating` | inert (reason 1: not operative) | heading |
| 5292 | sch 5 final paragraph `Uprating` (read as paragraph 9) | inert (reason 2: machinery) | the sums are subject to alteration by order of the Secretary of State under section 150 of the Administration Act; the order is not among the sources |
| 5293-5294 | sch 5A title and heading of paragraph 1 | inert (reason 1: not operative) | title and heading |
| 5295-5297 | sch 5A para 1(1) | fork F1 | `sch 5A para 1(1) the person must elect` (ssc9-sch5a.l4) |
| 5295-5298 | sch 5A para 1(1) and (2) | encoded | `sch 5A para 1(1) the election duty` (ssc9-sch5a.l4) |
| 5298 | sch 5A para 1(2) | encoded | `sch 5A para 1(2) the election that is treated as made` (ssc9-sch5a.l4) |
| 5299-5303 | sch 5A para 1(3) | inert (reason 2: machinery) | power for regulations to let a person change an election and to recover, or credit as paid on account, an amount to avoid duplicated payment; the regulations are not among the sources |
| 5304 | heading `Increase of pension where entitlement deferred` | inert (reason 1: not operative) | heading |
| 5305-5307 | sch 5A para 2(1) | fork F1 | `sch 5A para 2(1) this paragraph applies` (ssc9-sch5a.l4) |
| 5305-5308 | sch 5A para 2 | encoded | `sch 5A para 2 the amount by which the shared additional pension is increased for the deferment` (ssc9-sch5a.l4) |
| 5308 | sch 5A para 2(2) | fork F2 | `sch 5A para 2(2) the amount by which the rate of the pension is increased` (ssc9-sch5a.l4) |
| 5309 | heading `Calculation of increment` | inert (reason 1: not operative) | heading |
| 5310 | sch 5A para 3(1) | encoded | `sch 5A para 3(1) the number of increments` (ssc9-sch5a.l4) |
| 5310-5311 | sch 5A para 3 | encoded | `sch 5A para 3 the aggregate of the increments` (ssc9-sch5a.l4) |
| 5311 | sch 5A para 3(2) | encoded | `sch 5A para 3(2) the increment for one incremental period` (ssc9-sch5a.l4) |
| 5312-5313 | sch 5A para 3(3) and (4) | fork F6 | `sch 5A para 3(3) the amount under sub-paragraph (2) as rounded` (ssc9-sch5a.l4) |
| 5314 | sch 5A para 3(5) | fork F3 | `sch 5A para 3(5) the number of complete incremental periods` (ssc9-sch5a.l4) |
| 5315 | sch 5A para 3(6) | encoded | `sch 5A para 3(6) the rate for an incremental period` (ssc9-sch5a.l4) |
| 5316 | sch 5A para 3(7) | inert (reason 2: machinery) | the sums are subject to alteration by order of the Secretary of State under section 150 of the Administration Act; the order is not among the sources |
| 5317 | heading `Lump sum where entitlement to shared additional pension is deferred` | inert (reason 1: not operative) | heading |
| 5318-5321 | sch 5A para 4 | encoded | `sch 5A para 4(2) the person is entitled to a lump sum` (ssc9-sch5a.l4) |
| 5322 | heading `Calculation of lump sum` | inert (reason 1: not operative) | heading |
| 5323 | sch 5A para 5(1) | encoded | `sch 5A para 5(1) the last accrual period beginning during the period of deferment` (ssc9-sch5a.l4); `sch 5A para 5(1) the lump sum before rounding` (ssc9-sch5a.l4) |
| 5324-5325 | sch 5A para 5(2) accrued amount, para 5(3) | encoded | `sch 5A para 5(3) the accrued amount for an accrual period` (ssc9-sch5a.l4) |
| 5326 | sch 5A para 5(2) | encoded | `sch 5A para 5(2) an accrual period begins on the day` (ssc9-sch5a.l4) |
| 5327-5330 | sch 5A para 5(2) accrued amount, para 5(3) | encoded | `sch 5A para 5(3) the accrued amount for an accrual period` (ssc9-sch5a.l4) |
| 5331-5333 | sch 5A para 5(3) R | fork F4 | `sch 5A para 5(3) the percentage rate R` (ssc9-sch5a.l4) |
| 5334-5336 | sch 5A para 5(4) | encoded | `sch 5A para 5(4) the day a change in the base rate is treated as taking effect` (ssc9-sch5a.l4) |
| 5337 | sch 5A para 5(5) | encoded | `sch 5A para 5(5) the amount of shared additional pension counted for an accrual period` (ssc9-sch5a.l4) |
| 5338 | sch 5A para 5(6) | fork F6 | `sch 5A para 5(6) the lump sum as rounded` (ssc9-sch5a.l4) |
| 5339-5340 | sch 6 title and heading of paragraph 1 | inert (reason 1: not operative) | title and heading |
| 5341-5343 | sch 6 para 1(a) and (b) | encoded | `sch 6 para 1(a) the disability is taken into account` (ssc9-sch6.l4) |
| 5344 | sch 6 para 1(c) and para 2 (the handedness limb) | encoded | `sch 6 para 1(c) the assessment may refer to the circumstance` (ssc9-sch6.l4) |
| 5345 | sch 6 para 1(d) | encoded | `sch 6 the extent of the disablement assessed, as a percentage` (ssc9-sch6.l4) |
| 5346 | sch 6 para 1(c) and para 2 (the handedness limb) | encoded | `sch 6 para 1(c) the assessment may refer to the circumstance` (ssc9-sch6.l4) |
| 5347-5350 | sch 6 para 3 | encoded | `sch 6 para 3 the assessment after the adjustment` (ssc9-sch6.l4) |
| 5351 | heading `Severe disablement allowance` | inert (reason 1: not operative) | heading |
| 5352-5353 | sch 6 paras 4 and 5 (labels inferred) | repealed or blank in this text | two lines of dots under the heading `Severe disablement allowance`: shown blank in this text |
| 5354 | heading `Disablement benefit` | inert (reason 1: not operative) | heading |
| 5355 | sch 6 para 6(1) | encoded | `sch 6 para 6(1) the period taken into account by the assessment` (ssc9-sch6.l4) |
| 5356-5358 | sch 6 para 6(2) | encoded | `sch 6 para 6(2) a provisional assessment is made` (ssc9-sch6.l4) |
| 5358 | sch 6 para 6(2)(b) | fork F7 | `sch 6 para 6(2)(b) the day the period taken into account by the next assessment begins` (ssc9-sch6.l4) |
| 5359 | sch 6 para 6(3) | encoded | `sch 6 para 6(3) the period taken into account may end on the day` (ssc9-sch6.l4) |
| 5359-5365 | sch 6 para 6(3), (4) and (5) | encoded | `sch 6 para 6(3) the assessment is a final assessment` (ssc9-sch6.l4) |
| 5366-5369 | sch 6 para 7(a), (b) and (c) | encoded | `sch 6 para 7 what the assessment must state` (ssc9-sch6.l4) |
| 5370 | sch 6 para 7 | encoded | `sch 6 para 7 the percentage and the period may be specified more particularly` (ssc9-sch6.l4) |
| 5371 | heading `Special provision as to entitlement to constant attendance allowance, etc.` | inert (reason 1: not operative) | heading |
| 5372-5375 | sch 6 para 8(1) | inert (reason 2: machinery) | power for regulations to provide how the extent of disablement is determined, for deciding entitlement to a constant attendance allowance increase, by reference to all disabilities; the regulations are not among the sources |
| 5376-5379 | sch 6 para 8(2) | encoded | `sch 6 para 8(2) the payment is one of those payments` (ssc9-sch6.l4) |
| 5380-5382 | sch 7 title, Part I heading, heading `Availability` | inert (reason 1: not operative) | title and headings |
| 5383 | sch 7 pt I para 1 | encoded | `sch 7 pt I para 1 this Part applies to the person` (ssc9-sch7-p1.l4) |
| 5384 | heading `Rate and duration` | inert (reason 1: not operative) | heading |
| 5385 | sch 7 pt I para 2(1) | encoded | `sch 7 pt I para 2(1) the amount of the increase` (ssc9-sch7-p1.l4); `sch 7 pt I para 2(1) the weekly rate is increased` (ssc9-sch7-p1.l4) |
| 5386 | sch 7 pt I para 2(2) | encoded | `sch 7 pt I para 2(2) what an increase of pension under this paragraph is called` (ssc9-sch7-p1.l4) |
| 5387 | sch 7 pt I para 2(3) | encoded | `sch 7 pt I para 2(3) the beneficiary may be treated as incapable of work and likely to remain so permanently` (ssc9-sch7-p1.l4) |
| 5388 | sch 7 pt I para 2(4) | encoded | `sch 7 pt I para 2(4) the supplement is payable on the day` (ssc9-sch7-p1.l4) |
| 5389 | heading `Increase of unemployability supplement` | inert (reason 1: not operative) | heading |
| 5390-5393 | sch 7 pt I para 3(1) | encoded | `sch 7 pt I para 3(1) the beneficiary meets the age condition on the qualifying date` (ssc9-sch7-p1.l4); `sch 7 pt I para 3(1) the increase before the deductions` (ssc9-sch7-p1.l4) |
| 5394 | sch 7 pt I para 3(2) | encoded | `sch 7 pt I para 3(2) the increase after the deduction` (ssc9-sch7-p1.l4) |
| 5395-5396 | sch 7 pt I para 3(3), (3A) and (4) | encoded | `sch 7 pt I para 3(3) the relevant amount` (ssc9-sch7-p1.l4) |
| 5397 | sch 7 pt I para 3(3B) | inert (reason 1: not operative) | a signpost to section 14A that states no rule |
| 5398 | sch 7 pt I para 3(3), (3A) and (4) | encoded | `sch 7 pt I para 3(3) the relevant amount` (ssc9-sch7-p1.l4) |
| 5399-5401 | sch 7 pt I para 3(5), (6) and (7) | encoded | `sch 7 pt I para 3(5) the qualifying date` (ssc9-sch7-p1.l4) |
| 5402-5405 | sch 7 pt I para 3(8) and (9) | encoded | `sch 7 pt I para 3(8) the periods before and after the break are two different periods` (ssc9-sch7-p1.l4) |
| 5406 | sch 7 pt I para 3(10) | encoded | `sch 7 pt I para 3(10) the period is a period of interruption of employment` (ssc9-sch7-p1.l4) |
| 5407 | sch 7 pt I para 3(11) | encoded | `sch 7 pt I para 3(11) the increase subject to section 46(6) and (7)` (ssc9-sch7-p1.l4) |
| 5408 | heading `Increase for beneficiary’s dependent children and qualifying young persons` | inert (reason 1: not operative) | heading |
| 5409-5410 | sch 7 pt I para 4(1) and (2) | encoded | `sch 7 pt I para 4(1) the weekly rate is increased for children` (ssc9-sch7-p1.l4) |
| 5410 | sch 7 pt I para 4(2) | encoded | `sch 7 pt I para 4(2) the amount of the increase` (ssc9-sch7-p1.l4) |
| 5411-5419 | sch 7 pt I para 4(3) and (4) | encoded | `sch 7 pt I para 4(4) the number of children and qualifying young persons for whom no increase is payable` (ssc9-sch7-p1.l4) |
| 5420 | sch 7 pt I para 4(5) | encoded | `sch 7 pt I para 4(5) the amount for the time being specified` (ssc9-sch7-p1.l4) |
| 5421 | sch 7 pt I para 4(6) | encoded | `sch 7 pt I para 4(6) the meaning of week` (ssc9-sch7-p1.l4) |
| 5422 | heading `Additional provisions as to increase under paragraph 4` | inert (reason 1: not operative) | heading |
| 5423-5425 | sch 7 pt I para 5(1) | encoded | `sch 7 pt I para 5(1) the increase for the child may be payable` (ssc9-sch7-p1.l4) |
| 5426-5430 | sch 7 pt I para 5(2) | encoded | `sch 7 pt I para 5(2) the condition in paragraph (b) of sub-paragraph (1) is satisfied` (ssc9-sch7-p1.l4) |
| 5431 | heading `Increase for adult dependants` | inert (reason 1: not operative) | heading |
| 5432-5439 | sch 7 pt I para 6(1) | encoded | `sch 7 pt I para 6(1) the weekly rate is increased for an adult dependant` (ssc9-sch7-p1.l4) |
| 5440 | sch 7 pt I para 6(2) | encoded | `sch 7 pt I para 6(2) the beneficiary is contributing at the requisite rate` (ssc9-sch7-p1.l4) |
| 5441-5444 | sch 7 pt I para 6(3) | inert (reason 2: machinery) | power for regulations to withdraw the increase while the beneficiary contributes to the spouse's or civil partner's maintenance and the spouse's earnings exceed a prescribed amount |
| 5445-5447 | sch 7 pt I para 6(4) | inert (reason 2: machinery) | power for regulations to reduce or withdraw the increase while the beneficiary lives with a spouse or civil partner who has earnings |
| 5448 | sch 7 pt I para 6(5) | inert (reason 2: machinery) | power for regulations to authorise the increase for a person residing with the beneficiary on prescribed conditions |
| 5449 | sch 7 pt I para 6(6) | inert (reason 2: machinery) | power for regulations to prescribe how earnings are calculated or estimated |
| 5450 | sch 7 pt I para 6(7) | encoded | `sch 7 pt I para 6(7) the number of persons in respect of whom the increase is payable` (ssc9-sch7-p1.l4) |
| 5451 | heading `Earnings to include occupational and personal pensions for purposes of disablement pension` | inert (reason 1: not operative) | heading |
| 5452 | sch 7 pt I para 7(1) | encoded | `sch 7 pt I para 7(1) the earnings counted for paragraph 4 or 6` (ssc9-sch7-p1.l4) |
| 5453 | sch 7 pt I para 7(2) | inert (reason 2: machinery) | power for regulations to prescribe how pension payments made otherwise than weekly are apportioned |
| 5454 | heading `Dependency increases: continuation of awards in cases of fluctuating earnings` | inert (reason 1: not operative) | heading |
| 5455-5459 | sch 7 pt I para 8(1) and (2) | encoded | `sch 7 pt I para 8(1) the increase is payable for the week` (ssc9-sch7-p1.l4) |
| 5460 | heading `Part II — Disablement gratuity` | inert (reason 1: not operative) | heading |
| 5461-5464 | sch 7 pt II para 9(1) | encoded | `sch 7 pt II para 9(1) the employed earner is entitled to a disablement gratuity` (ssc9-sch7-p2.l4) |
| 5465-5466 | sch 7 pt II para 9(2)(a) | encoded | `sch 7 pt II para 9(2)(a) the amount of the gratuity` (ssc9-sch7-p2.l4) |
| 5467 | sch 7 pt II para 9(2)(b) | encoded | `sch 7 pt II para 9(2)(b) the gratuity is payable by instalments` (ssc9-sch7-p2.l4) |
| 5468 | sch 7 pt II para 9(3) | encoded | `sch 7 pt II para 9(3) the day after counting` (ssc9-sch7-p2.l4); `sch 7 pt II para 9(3) the first day after the 90 days` (ssc9-sch7-p2.l4); `sch 7 pt II para 9(3) the person may be entitled to a gratuity on the day` (ssc9-sch7-p2.l4) |
| 5469 | heading `Part III — Increase of disablement pension during hospital treatment` | inert (reason 1: not operative) | heading |
| 5470-5472 | sch 7 pt III para 10(1) | encoded | `sch 7 pt III para 10(1) this Part has effect in relation to the period` (ssc9-sch7-p2.l4) |
| 5473-5474 | sch 7 pt III para 10(2) and (3) | encoded | `sch 7 pt III para 10(2) the extent treated as assessed for the part of the period` (ssc9-sch7-p2.l4) |
| 5474 | sch 7 pt III para 10(3) | encoded | `sch 7 pt III para 10(3) the weekly rate of the pension after the reduction` (ssc9-sch7-p2.l4) |
| 5475 | heading `Part IV — Reduced earnings allowance` | inert (reason 1: not operative) | heading |
| 5476-5484 | sch 7 pt IV para 11(1) | encoded | `sch 7 pt IV para 11(1) the employed earner is entitled to reduced earnings allowance` (ssc9-sch7-p4.l4) |
| 5485-5488 | sch 7 pt IV para 11(2) | fork F8 | `sch 7 pt IV para 11(2) the person may again be entitled for the period` (ssc9-sch7-p4.l4) |
| 5489-5490 | sch 7 pt IV para 11(3)(a) | encoded | `sch 7 pt IV para 11(3)(a) the person is treated as entitled on the day` (ssc9-sch7-p4.l4) |
| 5491 | sch 7 pt IV para 11(3)(b) | inert (reason 2: machinery) | power for regulations to prescribe other circumstances in which a person is treated as entitled on a prescribed day |
| 5492 | sch 7 pt IV para 11(4) | inert (reason 2: machinery) | power for regulations to treat employment in which the claimant was engaged at the accident as the regular occupation in prescribed circumstances |
| 5493-5494 | sch 7 pt IV para 11(5)(a) | encoded | `sch 7 pt IV para 11(5)(a) the occupation counts as the regular occupation` (ssc9-sch7-p4.l4) |
| 5495 | sch 7 pt IV para 11(5)(b) | encoded | `sch 7 pt IV para 11(5)(b) the employment may count as employment of an equivalent standard` (ssc9-sch7-p4.l4) |
| 5496 | sch 7 pt IV para 11(5) | encoded | `sch 7 pt IV para 11(5) regard is to be had to the reasonable prospect of advancement` (ssc9-sch7-p4.l4) |
| 5497 | sch 7 pt IV para 11(6) | encoded | `sch 7 pt IV para 11(6) the person is treated as incapable of following the regular occupation` (ssc9-sch7-p4.l4) |
| 5498 | sch 7 pt IV para 11(7) | inert (reason 2: machinery) | power for regulations to provide that a trial, rehabilitation or training period of work does not make a person capable of following an occupation |
| 5499-5501 | sch 7 pt IV para 11(8) | encoded | `sch 7 pt IV para 11(8)(b) the allowance may be awarded for a further period` (ssc9-sch7-p4.l4) |
| 5502 | sch 7 pt IV para 11(9) | fork F12 | `sch 7 pt IV para 11(9) the award may be for the period` (ssc9-sch7-p4.l4) |
| 5503 | sch 7 pt IV para 11(10) | encoded | `sch 7 pt IV para 11(10) the rate of reduced earnings allowance` (ssc9-sch7-p4.l4) |
| 5503-5504 | sch 7 pt IV para 11(10) and (11) | encoded | `sch 7 pt IV para 11(10) the highest rate of reduced earnings allowance` (ssc9-sch7-p4.l4) |
| 5505-5507 | sch 7 pt IV para 11(12) | encoded | `sch 7 pt IV para 11(12) the relevant occupation` (ssc9-sch7-p4.l4) |
| 5508-5510 | sch 7 pt IV para 11(12A) | encoded | `sch 7 pt IV para 11(12A) the person is a person who retired from regular employment` (ssc9-sch7-p4.l4) |
| 5511-5513 | sch 7 pt IV para 11(13) | inert (reason 2: machinery) | on any award except the first the probable standard of remuneration is determined as prescribed, and regulations may refer it to the last award or to scales or indices of earnings; the regulations are not among the sources |
| 5514 | sch 7 pt IV para 11(14) | encoded | `sch 7 pt IV para 11(14) the maximum rate of a disablement pension` (ssc9-sch7-p4.l4) |
| 5515 | heading `Supplementary` | inert (reason 1: not operative) | heading |
| 5516-5520 | sch 7 pt IV para 12(1) | encoded | `sch 7 pt IV para 12(1) the person is entitled to reduced earnings allowance for life` (ssc9-sch7-p4.l4) |
| 5521-5524 | sch 7 pt IV para 12(2) and (3) | encoded | `sch 7 pt IV para 12(2) the weekly rate of the allowance for life` (ssc9-sch7-p4.l4) |
| 5525-5528 | sch 7 pt IV para 12(4) | encoded | `sch 7 pt IV para 12(4) the person is a qualifying beneficiary` (ssc9-sch7-p4.l4) |
| 5529-5530 | sch 7 pt IV para 12(5) and (6) | encoded | `sch 7 pt IV para 12(5) the relevant date` (ssc9-sch7-p4.l4) |
| 5531-5533 | sch 7 pt IV para 12(7) | encoded | `sch 7 pt IV para 12(7) the person is a person who has retired from regular employment` (ssc9-sch7-p4.l4) |
| 5534 | heading `Part V — Retirement allowance` | inert (reason 1: not operative) | heading |
| 5535-5539 | sch 7 pt V para 13(1) | encoded | `sch 7 pt V para 13(1) the day from which the person ceases to be entitled to reduced earnings allowance` (ssc9-sch7-p4.l4) |
| 5540 | sch 7 pt V para 13(2) | encoded | `sch 7 pt V para 13(2) the person is entitled to retirement allowance` (ssc9-sch7-p4.l4); `sch 7 pt V para 13(2) what the benefit is called` (ssc9-sch7-p4.l4) |
| 5541 | sch 7 pt V para 13(3) | encoded | `sch 7 pt V para 13(3) retirement allowance may be payable on the day` (ssc9-sch7-p4.l4) |
| 5542-5545 | sch 7 pt V para 13(4) | encoded | `sch 7 pt V para 13(4) the weekly rate of retirement allowance before rounding` (ssc9-sch7-p4.l4) |
| 5546-5549 | sch 7 pt V para 13(5) | encoded | `sch 7 pt V para 13(5) the weekly rate of reduced earnings allowance taken for sub-paragraph (4)` (ssc9-sch7-p4.l4) |
| 5550-5553 | sch 7 pt V para 13(6) | fork F9 | `sch 7 pt V para 13(6) the weekly rate of retirement allowance after rounding` (ssc9-sch7-p4.l4) |
| 5554 | sch 7 pt V para 13(7) | inert (reason 2: machinery) | the sums are subject to alteration by orders of the Secretary of State under section 150 of the Administration Act; the orders are not among the sources |
| 5555-5557 | sch 7 pt V para 13(8) | inert (reason 2: machinery) | power for regulations to say what `regular employment` means and when a person has given it up |
| 5558-5564 | sch 7 pt V para 13(9) | inert (reason 2: machinery) | power for regulations, under 13(8), to treat a person as having or not having given up regular employment by reference to earnings or hours |
| 5565-5567 | sch 7 pt V para 13(10) | encoded | `sch 7 pt V para 13(10) the day is a day of interruption of employment` (ssc9-sch7-p4.l4) |
| 5568 | sch 7 pt V para 13(11) | encoded | `sch 7 pt V para 13(11) the maximum rate of a disablement pension` (ssc9-sch7-p4.l4) |
| 5569-5570 | sch 7 Part VI title and heading `Introductory` | inert (reason 1: not operative) | headings |
| 5571 | sch 7 pt VI para 14(1) | encoded | `sch 7 pt VI para 14(1) this Part has effect in relation to the death` (ssc9-sch7-p6.l4) |
| 5572 | sch 7 pt VI para 14(1A) | encoded | `sch 7 pt VI para 14(1A) a claim for industrial death benefit may be made` (ssc9-sch7-p6.l4) |
| 5573 | sch 7 pt VI para 14(2) | encoded | `sch 7 pt VI para 14(2) the person is the deceased` (ssc9-sch7-p6.l4) |
| 5574 | heading `Widow’s benefit (entitlement)` | inert (reason 1: not operative) | heading |
| 5575-5577 | sch 7 pt VI para 15(1) and (4) | encoded | `sch 7 pt VI para 15(1) the widow is entitled to death benefit` (ssc9-sch7-p6.l4) |
| 5578 | sch 7 pt VI para 15(2) | fork F11 | `sch 7 pt VI para 15(2) the pension is payable on the day` (ssc9-sch7-p6.l4) |
| 5579 | sch 7 pt VI para 15(3) | encoded | `sch 7 pt VI para 15(3) the pension may be payable for the period` (ssc9-sch7-p6.l4) |
| 5580-5582 | sch 7 pt VI para 15(1) and (4) | encoded | `sch 7 pt VI para 15(1) the widow is entitled to death benefit` (ssc9-sch7-p6.l4) |
| 5583 | heading `Widow’s benefit (rate)` | inert (reason 1: not operative) | heading |
| 5584-5590 | sch 7 pt VI para 16 | fork F10 | `sch 7 pt VI para 16 the weekly rate of the widow's pension on the day` (ssc9-sch7-p6.l4) |
| 5587 | sch 7 pt VI para 16(2)(b) | encoded | `sch 7 pt VI para 16(2)(b) the widow's age brings the higher permanent rate` (ssc9-sch7-p6.l4) |
| 5591 | heading `Widower’s benefit (entitlement and rate)` | inert (reason 1: not operative) | heading |
| 5592-5594 | sch 7 pt VI para 17(1) | encoded | `sch 7 pt VI para 17(1) the widower is entitled to death benefit` (ssc9-sch7-p6.l4) |
| 5595 | sch 7 pt VI para 17(2) | encoded | `sch 7 pt VI para 17(2) the weekly rate of the widower's pension on the day` (ssc9-sch7-p6.l4) |
| 5596 | heading `Deceased's family` | inert (reason 1: not operative) | heading |
| 5597-5602 | sch 7 pt VI para 18(1) | encoded | `sch 7 pt VI para 18(1) the person satisfies the conditions for an allowance for the child` (ssc9-sch7-p6.l4); `sch 7 pt VI para 18(1) the weekly allowance` (ssc9-sch7-p6.l4) |
| 5603 | sch 7 pt VI para 18(2) | encoded | `sch 7 pt VI para 18(2) the allowance for the child may be payable` (ssc9-sch7-p6.l4) |
| 5604 | heading `Limits of entitlement to industrial death benefit in respect of children and qualifying young persons` | inert (reason 1: not operative) | heading |
| 5605-5608 | sch 7 pt VI para 19 | encoded | `sch 7 pt VI para 19 the person is the one entitled to the allowance for the child` (ssc9-sch7-p6.l4) |
| 5609 | heading `Death of person with constant attendance allowance` | inert (reason 1: not operative) | heading |
| 5610-5615 | sch 7 pt VI para 20 | encoded | `sch 7 pt VI para 20 the person is regarded as having died as a result of the injury` (ssc9-sch7-p6.l4) |
| 5616 | heading `Pulmonary disease` | inert (reason 1: not operative) | heading |
| 5617-5622 | sch 7 pt VI para 21 | encoded | `sch 7 pt VI para 21 the death is treated as caused by the disease for which the benefit was payable` (ssc9-sch7-p6.l4) |
| 5623-5624 | sch 8 title and Part I heading | inert (reason 1: not operative) | title and heading |
| 5625-5626 | sch 8 para 1 (label inferred) | repealed or blank in this text | heading `Continuation of workmen's compensation` over a line of dots: blank in this text |
| 5627-5628 | sch 8 para 2 (label inferred) | repealed or blank in this text | heading `Schemes for supplementing workmen's compensation` over a line of dots: blank in this text |
| 5629-5630 | sch 8 para 3 (label inferred) | repealed or blank in this text | heading `Provisions supplementary to paragraph 2` over a line of dots: blank in this text |
| 5631-5632 | sch 8 para 4 (label inferred) | repealed or blank in this text | heading `Industrial diseases benefit schemes` over a line of dots: blank in this text |
| 5633-5634 | sch 8 para 5 (label inferred) | repealed or blank in this text | heading `Restrictions on scope of schemes under paragraph 4` over a line of dots: blank in this text |
| 5635-5636 | sch 8 para 6 (label inferred) | repealed or blank in this text | heading `Nature and amount of benefit under paragraph 4` over a line of dots: blank in this text |
| 5637-5638 | sch 8 Part II | repealed or blank in this text | heading `Part II -- Regulations providing for benefit` over a line of dots: blank in this text |
| 5639-5640 | sch 8 Part III | repealed or blank in this text | heading `Part III -- Interpretation` over a line of dots: blank in this text |
| 5641-5642 | sch 9 title and heading of paragraph 1 | inert (reason 1: not operative) | title and heading |
| 5643-5646 | sch 9 para 1 | encoded | `sch 9 para 1 the person may be entitled to child benefit for the week` (ssc9-sch9-10.l4) |
| 5647-5648 | sch 9 para 2 (label inferred) | repealed or blank in this text | a line reading `...` (editorial omission) and a line of dots: blank in this text |
| 5649 | heading `Married children and qualifying young persons` | inert (reason 1: not operative) | heading |
| 5650 | sch 9 para 3 | encoded | `sch 9 para 3 the person may be entitled to child benefit for the child or qualifying young person` (ssc9-sch9-10.l4) |
| 5651-5652 | sch 9 para 4 (label inferred) | repealed or blank in this text | heading `Persons exempt from tax` over a line of dots: blank in this text |
| 5653-5654 | sch 9 para 5 (label inferred) | repealed or blank in this text | heading `Children entitled to severe disablement allowance` over a line of dots: blank in this text |
| 5655-5656 | sch 10 title and heading of paragraph 1 | inert (reason 1: not operative) | title and heading |
| 5657-5658 | sch 10 para 1(1) and (2) | encoded | `sch 10 para 1 the person is the one entitled` (ssc9-sch9-10.l4) |
| 5659 | heading `Person having child or qualifying young person living with him` | inert (reason 1: not operative) | heading |
| 5660 | sch 10 para 2 | encoded | `sch 10 para 2 the person is the one entitled` (ssc9-sch9-10.l4) |
| 5661 | heading `Opposite-sex spouses or civil partners` | inert (reason 1: not operative) | heading |
| 5662 | sch 10 para 3 | encoded | `sch 10 para 3 the person is the one entitled` (ssc9-sch9-10.l4) |
| 5663 | heading `Parents` | inert (reason 1: not operative) | heading |
| 5664 | sch 10 para 4(1) | encoded | `sch 10 para 4(1) the person is the one entitled` (ssc9-sch9-10.l4) |
| 5665 | sch 10 para 4(2) | encoded | `sch 10 para 4(2) the person is the one entitled` (ssc9-sch9-10.l4) |
| 5666 | heading `Other cases` | inert (reason 1: not operative) | heading |
| 5667 | sch 10 para 5 | encoded | `sch 10 para 5 the person is the one entitled` (ssc9-sch9-10.l4) |
| 5668 | heading `Supplementary` | inert (reason 1: not operative) | heading |
| 5669 | sch 10 para 6(1) | encoded | `sch 10 para 6(1) the election is an election under this Schedule` (ssc9-sch9-10.l4) |
| 5670 | sch 10 para 6(2) | inert (reason 2: machinery) | power for regulations to make exceptions from and modifications of paragraphs 1 to 5 |
| 5671 | sch 11 title | inert (reason 1: not operative) | title |
| 5672 | sch 11 para 1 | encoded | `sch 11 para 1 a period of entitlement may arise` (ssc9-sch11.l4) |
| 5673 | sch 11 para 1, concurrence sentence | inert (reason 2: machinery) | regulations under paragraph 1 need the concurrence of the Treasury |
| 5674 | sch 11 para 2 (d)(i) | encoded | `sch 11 para 2(d)(i) the employee had such a day in the 57 days` (ssc9-sch11.l4) |
| 5675-5677 | sch 11 para 2(a), (b) and (c) | repealed or blank in this text | three limbs shown as dots: blank in this text |
| 5678-5679 | sch 11 para 2 (d)(i) | encoded | `sch 11 para 2(d)(i) the employee had such a day in the 57 days` (ssc9-sch11.l4) |
| 5680-5681 | sch 11 para 2(d)(ii) and (iii) | repealed or blank in this text | two limbs shown as dots: blank in this text |
| 5682 | sch 11 para 2(dd) | encoded | `sch 11 para 2(dd) the circumstance applies` (ssc9-sch11.l4) |
| 5683 | sch 11 para 2(f) | encoded | `sch 11 para 2(f) the circumstance applies` (ssc9-sch11.l4) |
| 5684 | sch 11 para 2(g) and its exception | encoded | `sch 11 para 2(g) the circumstance applies` (ssc9-sch11.l4) |
| 5685 | sch 11 para 2(h) and its exception | encoded | `sch 11 para 2(h) the circumstance applies` (ssc9-sch11.l4) |
| 5686 | sch 11 relevant date | encoded | `sch 11 the relevant date` (ssc9-sch11.l4) |
| 5687-5688 | sch 11, two paragraphs after the definition of `relevant date` (labels not given) | repealed or blank in this text | two lines of dots: blank in this text |
| 5689-5691 | sch 11 exception to para 2(d)(i) | encoded | `sch 11 para 2(d)(i) applies on the day` (ssc9-sch11.l4) |
| 5692 | sch 11 joining rule for para 2(f) | encoded | `sch 11 para 2(f) the employee has done no work for the employer under the contract of service` (ssc9-sch11.l4) |
| 5693 | sch 11 para 2(g) and its exception | encoded | `sch 11 para 2(g) the circumstance applies` (ssc9-sch11.l4) |
| 5694 | sch 11 para 2(h) and its exception | encoded | `sch 11 para 2(h) the circumstance applies` (ssc9-sch11.l4) |
| 5695-5696 | sch 12 title and heading of paragraph 1 | inert (reason 1: not operative) | title and heading |
| 5697-5700 | sch 12 para 1 | encoded | `sch 12 para 1 the day counts as a day of incapacity for work for incapacity benefit` (ssc9-sch12-13.l4) |
| 5701 | heading `Contractual remuneration` | inert (reason 1: not operative) | heading |
| 5702-5705 | sch 12 para 2(1) and (2)(b) | encoded | `sch 12 para 2(2)(b) the contractual remuneration still owed for the day` (ssc9-sch12-13.l4) |
| 5703-5704 | sch 12 para 2(2)(a) | encoded | `sch 12 para 2(2)(a) the statutory sick pay still owed for the day` (ssc9-sch12-13.l4) |
| 5706 | sch 12 para 2(3) | inert (reason 2: machinery) | power for regulations to say which payments are treated as contractual remuneration |
| 5707 | heading `Incapacity benefit` | inert (reason 1: not operative) | heading |
| 5708-5713 | sch 12 para 3(1), (2) and (3) | encoded | `sch 12 para 3(2) the day is or forms part of a period of incapacity for work` (ssc9-sch12-13.l4) |
| 5714-5716 | sch 12 para 4(1) | encoded | `sch 12 para 4(1) section 30A(3) does not apply to the day` (ssc9-sch12-13.l4) |
| 5717 | sch 12 para 4(2) | encoded | `sch 12 para 4(2) section 30A(3) does not apply to the later day` (ssc9-sch12-13.l4) |
| 5718 | heading `Incapacity benefit for widows and widowers` | inert (reason 1: not operative) | heading |
| 5719 | sch 12 para 5 | encoded | `sch 12 para 5 paragraph 1 applies` (ssc9-sch12-13.l4) |
| 5720 | heading `Unemployability supplement` | inert (reason 1: not operative) | heading |
| 5721 | sch 12 para 6 | encoded | `sch 12 para 6 paragraph 1 applies` (ssc9-sch12-13.l4) |
| 5722-5723 | sch 13 title and heading of paragraph 1 | inert (reason 1: not operative) | title and heading |
| 5724 | sch 13 para 1 | encoded | `sch 13 para 1 the day counts as a day of incapacity for work for incapacity benefit` (ssc9-sch12-13.l4) |
| 5725 | heading `Incapacity benefit` | inert (reason 1: not operative) | heading |
| 5726 | sch 13 para 2(1) | inert (reason 2: machinery) | power for regulations to treat a day in the maternity pay period as a day of incapacity for work in prescribed circumstances |
| 5727 | sch 13 para 2(2) | encoded | `sch 13 para 2(2) the weekly rate of the benefit after the deduction` (ssc9-sch12-13.l4) |
| 5728 | heading `Contractual remuneration` | inert (reason 1: not operative) | heading |
| 5729-5732 | sch 13 para 3(1) and (2)(b) | encoded | `sch 13 para 3(2)(b) the contractual remuneration still owed for the week` (ssc9-sch12-13.l4) |
| 5730-5731 | sch 13 para 3(2)(a) | encoded | `sch 13 para 3(2)(a) the statutory maternity pay still owed for the week` (ssc9-sch12-13.l4) |
| 5733 | sch 13 para 3(2A) | encoded | `sch 13 para 3(2A) the meaning of week` (ssc9-sch12-13.l4) |
| 5734 | sch 13 para 3(3) | inert (reason 2: machinery) | power for regulations to say which payments are treated as contractual remuneration |
| 5735-5737 | Table of Derivations, title, `Note:` and note 1 (abbreviations) | inert (reason 1: not operative) | the Table's rows are not in this text; the notes record where provisions came from and create no rule |
| 5738 | Table of Derivations, note 2 | inert (reason 1: not operative) | a note on the Social Security Pensions Act 1975; no rule |
| 5739-5743 | Table of Derivations, note 3 (the three 1991 up-rating orders) | inert (reason 1: not operative) | a note on 1991 statutory instruments that alter sums; no rule of this Act, and not among the sources |
| 5744 | Table of Derivations, note 4 | inert (reason 1: not operative) | a note that the Table does not show transfer of functions orders; no rule |

## Fork register (ssc9)

Twelve forks.
For each: the words, the readings I saw, the reading taken, and the text that licenses it.
The ids F1 to F12 are ssc9's own (the keel's NOTES.md has a different F1).
"Taken" says what the code does; "other reading" says what a lawyer who prefers the other would change.
Where the text itself does not choose, the code answers `NOTHING` on the cases where the readings differ, and answers the same on both readings on the cases where they agree, so no fork is settled by a guess unless this register says so.

| id | rows (lines) | the words | reading taken | other reading |
| --- | --- | --- | --- | --- |
| F1 | A1(1) 12 months (5069); A1(1) must elect (5069-5071); 1(1) applies (5080-5082); 3C(1)(d) (5138); 5A para 1(1) (5295-5297); 5A para 2(1) (5305-5307) | "the period of deferment is at least 12 months" (5069); "S's entitlement was deferred throughout the 12 months" (5138) | Counts the twelve months from the first day to the day before the first anniversary. If the deferment began on 29 February and the next year has no 29 February, the one day on which the readings differ answers `NOTHING`; every other day agrees on both readings | The anniversary of 29 February is 1 March (the way `Date` rolls an impossible date forward), so the twelve months are complete at the end of 28 February, one day later |
| F2 | 1(2) (5083); 5A para 2(2) (5308) | "but only if that amount is enough to increase the rate of the pension by at least 1 per cent" | "the rate of the pension" is the rate being increased, before the increase: the aggregate must be at least 1/100 of that rate | The rate after the increase: the aggregate must be at least 1/99 of the old rate, which is stricter |
| F3 | 2(2) (5085-5086); 5A para 3(5) (5314) | "'incremental period' means any period of six days which are treated by regulations as days of increment" | Six days of increment make one period wherever they fall: the number of periods is the number of days of increment divided by six, rounded down | The six days must be consecutive. The code takes only a count of days, so this reading would need the days themselves as input |
| F4 | 3B(3) R (5120-5122); 7B(3) R (5262-5264); 5A para 5(3) R (5331-5333) | "a percentage rate two per cent. higher than the Bank of England base rate" | Two percentage points above the base rate (base rate 5 gives 7), or the higher rate regulations prescribe | Two per cent of the base rate above it (base rate 5 gives 5.1) |
| F5 | after 7(3), sub-paragraph (5) (5240-5242); 5A, 6 and 6A, which use the term (5183-5214) | "the appropriate amount" is used in 5A(2)(b), 5A(3)(a), 6(2)(b), 6(3)(c), 6(4)(b) and 6A(2)(b) (src:5188, 5191, 5196, 5201, 5205, 5213) and defined only "In paragraphs 5A to 6A as modified by this paragraph" (src:5240) | The definition gives the amount only in the modified cases (W became entitled before 6 April 2012 and S died before 6 April 2012). Outside them the term is undefined in this text, so `sch 5 para after 7(3) the appropriate amount` answers `NOTHING` and 5A, 6 and 6A answer `NOTHING` when they are given no appropriate amount | The definition at src:5240 applies to every use of the term in 5A to 6A, modified or not; the greater-of rule then decides the unmodified cases too |
| F6 | 5A para 3(3) and (4) (5312-5313); 5A para 5(6) (5338) | "taking any 1/2p as nearest to the next whole penny" | A half penny goes up to the next whole penny | The sister provisions say "next whole penny above" (2(4) at 5090, 7(2) at 5217, 7C(1) at 5280); these two say "next whole penny" without "above". Read strictly, they leave open whether the half penny goes up or to the nearest whole penny. The only amounts on which the readings differ are exact half pennies |
| F7 | 6(2)(b) (5358) | "on the next assessment the period to be taken into account shall begin with the end of the period taken into account by the provisional assessment" | The next period begins on the day after the last day of the provisional period, so no day is counted twice | The next period begins on the last day of the provisional period (the "end" read as the last day), so that one day is counted in both |
| F8 | 11(2) (5485-5488) | "who immediately before that date is entitled to reduced earnings allowance..."; "that date" has no antecedent in 11(2) | The date is 1 October 1990 (src:5482, and src:5490 where 11(3)(a) speaks of entitlement "immediately before 1st October 1990") | The date is 10 October 1994, the last date mentioned before 11(2) (src:5483-5484, where "that date" already means 10 October 1994) |
| F9 | 13(6) (5550-5553) | "would exceed the whole number of pence next below it by 1/2p or more... entitled to retirement allowance at a rate equal to the next higher whole number of pence" | Silent on a fraction under 1/2p, so `NOTHING` for that case (limited by its own wording) | A fraction under 1/2p is dropped, as in ordinary rounding to the nearest penny |
| F10 | 16(1)-(3) (5584-5590) | "for the period of 26 weeks next following the deceased's death" | The 26 weeks (182 days) begin on the day of the death, which agrees with 15(2) ("a pension commencing from the death") | The 26 weeks begin the day after the death, which leaves the day of the death with no rate in 16(1) to (3) |
| F11 | 15(2) (5578) | "payable... for life or until she remarries or forms a civil partnership" | "Until" ends the pension on the day of the remarriage or civil partnership: that day and later days answer `FALSE`. ("For life" is a stated period, so a day after her death answers `NOTHING`, not `FALSE`.) | The pension is payable through the day of the remarriage |
| F12 | 11(9) (5502) | "The award may not be for a period longer than the period to be taken into account under paragraph 4 or 6 of Schedule 6" | A limit on the length of the award, in days: a longer award answers `FALSE`, a shorter or equal one answers `NOTHING` (the paragraph is a bar and no grant) | A limit on where the award may end. The two readings agree whenever the award starts with the assessed period |

### What each fork does to the answers

- **F1, F2, F3, F4, F6** change an amount or a yes-or-no only on the cases named in the table; a case on which the readings agree gets the same answer under either.
  The tests carry one case on each side of every boundary, and the leap-day case answers `NOTHING` in each place it arises (`ssc9-tests-sch5.l4`, `ssc9-tests-sch5-w.l4`, `ssc9-tests-sch5a.l4`).
- **F5, F9** return `NOTHING` where the term is undefined or the text is silent, and the tests assert `NOTHING` (for F5, `ssc9-tests-sch5-w.l4` asserts `NOTHING` for an unmodified case and for an absent appropriate amount).
- **F7, F8, F10, F11, F12** take one reading in the code, and the tests assert it with a case on each side of the day on which the readings differ.
  For F8 the alternative reading would also need a different input (entitled immediately before 10 October 1994), which is why it is a fork and not a switch.

### Ambiguities that did not become forks

- **"1/5th per cent"** (2(3) at 5088, 3(2) at 5311) is read as one fifth of one per cent, that is 0.2 per cent.
  I saw no second reading.
- **"Subject to" grants** (for example 2(1) "Subject to paragraph 3 below", 5084) return `NOTHING` when their own conditions hold, because the paragraph that the grant is subject to decides the rest; the seat layer composes them.
- **Week.**
  Schedule 7 Part I paragraph 4(6) (src:5421) says "week" means "such period of 7 days as may be prescribed", which is the core's sixth `Week convention`; Schedule 13 paragraph 3(2A) (src:5733) says "week" means seven days beginning with the day the maternity pay period begins, which is the core's fourth.
  Each rule that counts weeks says which it uses in a comment.

## Jural relations (ssc9)

One row per provision (or group of sub-paragraphs that carry one relation) of lines 5067-5744, in text order.
Hohfeld's pairs: right (claim) and duty; privilege and no-right; power and liability; immunity and disability.

**Conventions.**

- Where the text says a person "is entitled" to a benefit it names no payer.
  The correlative duty is put on **the Secretary of State**, who pays under the Administration Act (not among the sources); this is a reading and is marked "(payer not named)" in the table.
  Where the text says an employer is liable to pay statutory sick pay or statutory maternity pay, the employer is named by the text.
- A rule is cited by the label its name begins with; the label stands for every top-level name of the module that begins with it (`sch 5 para 1(2)` stands for `sch 5 para 1(2) the amount by which the rate of the pension is increased`).
  The full names are in the coverage table.
- Each relation is stated once, from one side, in layer 1; the seat layer asks the same relation from the person's side.
- `none` means the provision creates no relation: a definition, a counting rule, a rounding rule, a heading or a power to make regulations (the person is not the holder of the power).

| lines | provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | L4 rule |
| --- | --- | --- | --- | --- |
| 5069-5072 | Sch 5 para A1(1)-(2): election on a deferred pension | pensioner: power to elect between an increase and a lump sum; Secretary of State: claim that the pensioner elects on claiming or within the prescribed period | Secretary of State: liability to be bound by the election, and by the deemed election of the lump sum under A1(2); pensioner: duty to elect | `sch 5 para A1(1)` (election duty, regulative), `sch 5 para A1(2)` |
| 5073-5077 | Sch 5 para A1(3) | none (regulations may let the election be changed; the pensioner holds no power until they do) | none | (inert, reason 2) |
| 5078 | Sch 5 para A1(4) | none (limits the election: no election applies to an increase under paragraphs 5 to 6A) | none | `sch 5 para A1(4)` |
| 5080-5083 | Sch 5 para 1: increase of pension for the deferment | pensioner: right to the increase (payer not named), if the increase is at least 1 per cent of the rate | Secretary of State: duty to pay the increase; no-right of the pensioner to a smaller increase | `sch 5 para 1(1)`, `sch 5 para 1(2)` |
| 5084-5097 | Sch 5 para 2: increments, incremental periods, rounding | pensioner: right to one increment for each complete incremental period (payer not named) | Secretary of State: duty to pay it; (2), (4)-(8) are calculation rules: none | `sch 5 para 2(1)`, `sch 5 para 2(3)`; the rest `sch 5 para 2(2)`, `2(4)` to `2(8)` |
| 5098-5103 | Sch 5 para 2A: increase where the pension includes an increase under paragraphs 5 to 6A | pensioner: right to the increase (payer not named) | Secretary of State: duty to pay it | `sch 5 para 2A(1)` to `2A(3)` |
| 5104-5105 | Sch 5 para 3: power to modify paragraph 2 | none | none | (inert, reason 2) |
| 5107-5110 | Sch 5 para 3A: lump sum | pensioner: right to the lump sum (payer not named) | Secretary of State: duty to pay it | `sch 5 para 3A(2)` |
| 5112-5132 | Sch 5 para 3B: calculation of the lump sum | none (calculation of the amount of the 3A right) | none | `sch 5 para 3B(1)` to `3B(6)` |
| 5134-5142 | Sch 5 para 3C(1)-(3): W's election | W (the surviving spouse or civil partner): power to elect; Secretary of State: claim to the election | Secretary of State: liability to be bound by it, and by the deemed election under 3C(3); W: duty to elect | `sch 5 para 3C(1)` to `3C(3)` (the election duty is regulative) |
| 5143-5147 | Sch 5 para 3C(4) | none (regulations) | none | (inert, reason 2) |
| 5148 | Sch 5 para 3C(5) | none (the election does not affect paragraphs 5 to 6A) | none | `sch 5 para 3C(5)` |
| 5150-5165 | Sch 5 para 4: W's increase of pension | W: right to the increase (payer not named) | Secretary of State: duty to pay it; no-right of W where 4(5) applies | `sch 5 para 4(1)` to `4(5)` |
| 5166-5221 | Sch 5 paras 5, 5A, 6, 6A, 7: the amounts that make up the increase | none (calculation of the amount of the paragraph 4 right) | none | `sch 5 para 5`, `5A`, `6`, `6A`, `7(2)`, `7(3)` |
| 5222-5243 | Sch 5 unnumbered paragraph after 7(3): modification of 5A to 6A and "appropriate amount" | none (a modification and a definition) | none | `sch 5 para after 7(3)` |
| 5245-5246 | Sch 5 para 7A: W's lump sum | W: right to the lump sum (payer not named) | Secretary of State: duty to pay it | `sch 5 para 7A(2)` |
| 5248-5278 | Sch 5 para 7B: calculation of W's lump sum | none | none | `sch 5 para 7B(1)` to `7B(7)` |
| 5280-5283 | Sch 5 para 7C: rounding; duty of the Secretary of State when prescribing a rate | none (7C(2) is a duty on the Secretary of State to have regard to certain matters, not a right of the person) | none | `sch 5 para 7C(1)`; 7C(2) inert, reason 2 |
| 5284-5290 | Sch 5 para 8: married couples and civil partners | none (counting rules for the conditions in paragraphs 3C and 4) | none | `sch 5 para 8(4)` to `8(6)` |
| 5291-5292 | Sch 5 para 9: uprating | Secretary of State: power to alter the sums by order | pensioner: liability to the alteration | (inert, reason 2) |
| 5295-5298 | Sch 5A para 1: election on a deferred shared additional pension | person: power to elect; Secretary of State: claim to the election | Secretary of State: liability to be bound by it and by the deemed election; person: duty to elect | `sch 5A para 1(1)`, `sch 5A para 1(2)` |
| 5299-5303 | Sch 5A para 1(3) | none (regulations) | none | (inert, reason 2) |
| 5305-5315 | Sch 5A paras 2 and 3: increase and increments | person: right to the increase (payer not named), if at least 1 per cent | Secretary of State: duty to pay it | `sch 5A para 2(1)`, `2(2)`; `sch 5A para 3(1)` to `3(6)` |
| 5316 | Sch 5A para 3(7) | Secretary of State: power to alter the sums by order | person: liability to the alteration | (inert, reason 2) |
| 5318-5338 | Sch 5A paras 4 and 5: lump sum and its calculation | person: right to the lump sum (payer not named) | Secretary of State: duty to pay it; 5 is a calculation: none | `sch 5A para 4(2)`; `sch 5A para 5(1)` to `5(6)` |
| 5341-5346 | Sch 6 para 1(a)-(c): method of assessment | claimant: claim that all the disabilities that result from the loss of faculty are taken into account, and that the assessment refers only to age, sex and physical and mental condition | the authority making the assessment (not named in this text): duty to assess so | `sch 6 para 1(a)`, `sch 6 para 1(c)` |
| 5345 | Sch 6 para 1(d): a prescribed loss of faculty is 100 per cent | claimant: right to be assessed at 100 per cent for a prescribed loss of faculty | the authority making the assessment: duty | `sch 6 the extent of the disablement assessed, as a percentage` |
| 5346-5350 | Sch 6 paras 2 and 3: further principles by regulation; no reduction of an earlier assessment | claimant: immunity from reduction of an assessment by virtue of paragraph 3 | the authority making the assessment: disability (it cannot reduce) | `sch 6 para 3` |
| 5355-5365 | Sch 6 para 6: the period taken into account | claimant: claim to an assessment for the period the paragraph fixes, and to a final assessment under 6(3) when the extent is under 14 per cent | the authority making the assessment: duty | `sch 6 para 6(1)` to `6(3)` |
| 5366-5370 | Sch 6 para 7: what the assessment must state | claimant: claim to be told the percentage and the period | the authority making the assessment: duty | `sch 6 para 7` |
| 5372-5379 | Sch 6 para 8(1)-(2) | none (regulations; a list of payments) | none | `sch 6 para 8(2)`; 8(1) inert, reason 2 |
| 5383 | Sch 7 pt I para 1: application | none (says whom the Part applies to) | none | `sch 7 pt I para 1` |
| 5385-5388 | Sch 7 pt I para 2: increase of a pension where incapable of work | beneficiary: right to the increase (an "unemployability supplement"), payer not named | Secretary of State: duty to pay it; the supplement is payable for a period fixed at the grant and renewable | `sch 7 pt I para 2(1)` to `2(4)` |
| 5390-5407 | Sch 7 pt I para 3: increase of the supplement for age and additional pension | beneficiary: right to the increase, payer not named | Secretary of State: duty to pay it; the deductions, the qualifying date and the 8-week break are calculation rules: none | `sch 7 pt I para 3(1)` to `3(11)` |
| 5409-5421 | Sch 7 pt I para 4: increase for dependent children and qualifying young persons | beneficiary: right to the increase (payer not named), reduced by the partner's earnings | Secretary of State: duty to pay it; privilege to pay less above the earnings threshold | `sch 7 pt I para 4(1)` to `4(6)` |
| 5423-5430 | Sch 7 pt I para 5: conditions of the child increase | none (conditions of the paragraph 4 right) | none | `sch 7 pt I para 5(1)`, `5(2)` |
| 5432-5440 | Sch 7 pt I para 6(1)-(2): increase for adult dependants | beneficiary: right to the increase (payer not named) | Secretary of State: duty to pay it | `sch 7 pt I para 6(1)`, `6(2)` |
| 5441-5449 | Sch 7 pt I para 6(3)-(6) | none (regulations) | none | (inert, reason 2) |
| 5450 | Sch 7 pt I para 6(7): one person only | Secretary of State: privilege not to pay for more than one person | beneficiary: no-right to a second increase for the same period | `sch 7 pt I para 6(7)` |
| 5452-5454 | Sch 7 pt I para 7: earnings include pensions | none (counting rule; 7(2) regulations inert, reason 2) | none | `sch 7 pt I para 7(1)` |
| 5455-5459 | Sch 7 pt I para 8: continuation of increases despite fluctuating earnings | beneficiary: right to the increase for the week | Secretary of State: duty to pay it; no-right where earnings exceed the increase | `sch 7 pt I para 8(1)` |
| 5461-5468 | Sch 7 pt II para 9: disablement gratuity | employed earner: right to the gratuity (payer not named), after the 90 days | Secretary of State: duty to pay it, in instalments if so decided; no-right before the 90 days expire | `sch 7 pt II para 9(1)` to `9(3)` |
| 5470-5474 | Sch 7 pt III para 10: pension during hospital treatment | beneficiary: right to the pension as if assessed at 100 per cent during treatment | Secretary of State: duty to pay it; privilege to pay the reduced rate | `sch 7 pt III para 10(1)` to `10(3)` |
| 5476-5490 | Sch 7 pt IV para 11(1)-(3): entitlement to reduced earnings allowance, no second entitlement | employed earner: right to the allowance (payer not named) | Secretary of State: duty to pay it; no-right of the person who has ceased to be entitled and is not covered by the exception in 11(2) | `sch 7 pt IV para 11(1)`, `11(2)`, `11(3)(a)` |
| 5491-5492 | Sch 7 pt IV para 11(3)(b) and (4) | none (regulations) | none | (inert, reason 2) |
| 5493-5497 | Sch 7 pt IV para 11(5)-(6): regular occupation | claimant: claim that a subsidiary occupation is not the regular occupation, that advancement is regarded, and that deprivation of normal advancement means incapacity | Secretary of State: duty to apply the definitions | `sch 7 pt IV para 11(5)(a)`, `11(5)(b)`, `11(5) regard`, `11(6)` |
| 5498 | Sch 7 pt IV para 11(7) | none (regulations) | none | (inert, reason 2) |
| 5499-5510 | Sch 7 pt IV para 11(8)-(12A): awards, rate, limits | beneficiary: right to an award for the period determined, at the rate the paragraph fixes | Secretary of State: duty to award; no-right to an award longer than the period assessed | `sch 7 pt IV para 11(8)(b)`, `11(9)`, `11(10)`, `11(12)`, `11(12A)` |
| 5511-5513 | Sch 7 pt IV para 11(13) | none (regulations) | none | (inert, reason 2) |
| 5514 | Sch 7 pt IV para 11(14): definition | none | none | `sch 7 pt IV para 11(14)` |
| 5516-5533 | Sch 7 pt IV para 12: allowance for life | qualifying beneficiary: right to the allowance for life at the rate the paragraph fixes | Secretary of State: duty to pay it | `sch 7 pt IV para 12(1)` to `12(7)` |
| 5535-5553 | Sch 7 pt V para 13(1)-(6): retirement allowance | beneficiary who has given up regular employment: right to the allowance (payer not named) | Secretary of State: duty to pay it | `sch 7 pt V para 13(1)` to `13(6)` |
| 5554-5564 | Sch 7 pt V para 13(7)-(9) | none (orders and regulations) | none | (inert, reason 2) |
| 5565-5568 | Sch 7 pt V para 13(10)-(11): definitions | none | none | `sch 7 pt V para 13(10)`, `13(11)` |
| 5571-5572 | Sch 7 pt VI para 14(1)-(1A): the Part's reach; no new claims | Secretary of State: immunity from claims after the commencement of 14(1A); the Part applies only to deaths before 11 April 1988 | claimant: disability (cannot claim) | `sch 7 pt VI para 14(1)`, `14(1A)` |
| 5573 | Sch 7 pt VI para 14(2): "the deceased" | none (definition) | none | `sch 7 pt VI para 14(2)` |
| 5575-5582 | Sch 7 pt VI para 15: widow's death benefit | widow: right to a pension for life or until she remarries (payer not named) | Secretary of State: duty to pay it; no-right while she lives as a married couple with another | `sch 7 pt VI para 15(1)` to `15(3)` |
| 5584-5590 | Sch 7 pt VI para 16: the widow's rate | widow: right to the initial rate for 26 weeks, then the higher or lower permanent rate | Secretary of State: duty to pay at that rate | `sch 7 pt VI para 16` |
| 5592-5595 | Sch 7 pt VI para 17: widower's benefit | widower: right to the pension for life (payer not named) | Secretary of State: duty to pay it | `sch 7 pt VI para 17(1)`, `17(2)` |
| 5597-5608 | Sch 7 pt VI paras 18-19: allowance for the deceased's children; one person only | widow (or a prescribed person): right to the allowance for each child | Secretary of State: duty to pay it; no-right of a second claimant for the same child, and of any claimant other than the widow or widower where one satisfies the conditions | `sch 7 pt VI para 18(1)`, `18(2)`, `19` |
| 5610-5622 | Sch 7 pt VI paras 20-21: deaths treated as industrial | dependants who claim under paragraphs 15 to 18: claim that the death is treated as a result of the injury or disease | Secretary of State: duty to treat the death so | `sch 7 pt VI para 20`, `21` |
| 5643-5646 | Sch 9 para 1: detention, care | Secretary of State: privilege not to pay child benefit for a week the child is in detention, under a supervision order in a residential establishment, or in care | person claiming: no-right to child benefit for that week | `sch 9 para 1` |
| 5647-5648, 5651-5654 | Sch 9 paras 2, 4, 5 | none (blank in this text) | none | (repealed or blank) |
| 5650 | Sch 9 para 3: married children | Secretary of State: privilege not to pay for a child who is married or a civil partner | person claiming: no-right | `sch 9 para 3` |
| 5657-5668 | Sch 10 paras 1-5: priority between claimants | the person who takes priority: right to child benefit for the week; the persons who may elect: power to elect who is entitled | Secretary of State: duty to pay the one who takes priority; the other claimant: no-right; Secretary of State: liability to be bound by the election, or to determine in default of election | `sch 10 para 1` to `sch 10 para 5` |
| 5669-5670 | Sch 10 para 6: election in the prescribed manner; exceptions | none (6(1) states how an election is made; 6(2) is a power to make regulations, inert, reason 2) | none | `sch 10 para 6(1)` |
| 5672-5691 | Sch 11 paras 1-2: circumstances in which no period of entitlement to statutory sick pay arises | employer: privilege not to pay statutory sick pay in the circumstances; the circumstances are the facts that give it | employee: no-right to statutory sick pay | `sch 11 para 1`, `sch 11 para 2(d)(i)` to `2(h)`, `sch 11 the relevant date` and the exceptions |
| 5692-5694 | Sch 11 joining rule and trade dispute rules | employer: privilege not to pay | employee: no-right | `sch 11 para 2(f)`, `2(g)`, `2(h)` and their exceptions |
| 5697-5700 | Sch 12 para 1: days in a period of entitlement | Secretary of State: privilege not to count the day towards a period of incapacity for work for incapacity benefit | employee: no-right to incapacity benefit by counting that day | `sch 12 para 1` |
| 5702-5705 | Sch 12 para 2: contractual remuneration | employer: privilege to set off contractual remuneration paid against statutory sick pay owed, and statutory sick pay paid against contractual remuneration owed | employee: no-right to both for the same day | `sch 12 para 2(1)`, `2(2)(a)`, `2(2)(b)` |
| 5706 | Sch 12 para 2(3) | none (regulations) | none | (inert, reason 2) |
| 5708-5717 | Sch 12 paras 3-4: incapacity benefit after a period of entitlement | employee: right to have the first day after the period of entitlement count as a period of incapacity for work, and to have the waiting days disregarded for 57 days | Secretary of State: duty to do so | `sch 12 para 3(1)` to `3(3)`, `sch 12 para 4(1)`, `4(2)` |
| 5719-5721 | Sch 12 paras 5-6 | employee (for the widow's and widower's conditions, and for Schedule 7 paragraph 3): claim that paragraph 1 does not stop the day from counting | Secretary of State: duty | `sch 12 para 5`, `6` |
| 5724 | Sch 13 para 1: days in the maternity pay period | Secretary of State: privilege not to treat the days as incapacity days | woman: no-right | `sch 13 para 1` |
| 5726-5727 | Sch 13 para 2: incapacity benefit | none for 2(1) (regulations); 2(2): Secretary of State: privilege to deduct statutory maternity pay from benefit | woman: no-right to benefit unless a balance remains | `sch 13 para 2(2)`; 2(1) inert, reason 2 |
| 5729-5733 | Sch 13 para 3: contractual remuneration | employer: privilege to set off, as in Schedule 12 paragraph 2 | woman: no-right to both for the same week | `sch 13 para 3(1)`, `3(2)(a)`, `3(2)(b)`, `3(2A)` |
| 5734 | Sch 13 para 3(3) | none (regulations) | none | (inert, reason 2) |
| 5623-5640 | Sch 8: industrial injuries and diseases (old cases) | none (blank in this text) | none | (repealed or blank) |
| 5735-5744 | Table of Derivations | none (notes on sources; no rule) | none | (inert, reason 1) |
| headings | every heading in the range | none | none | (inert, reason 1) |

## Marginal readings for a lawyer (ssc9)

The rule of 2026-10-29 is in force for every row, and it is "assumed, not ruled by a lawyer".
Two readings in it are for a lawyer to decide, and this encoding takes both as the status quo:

- **(a)** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"); flat negatives count as the text saying no.
- **(b)** a prohibition or grant limited by its own wording does not count as the text's no (so the case outside the limit is `NOTHING`).

Three further readings of mine are marked (c), (d) and (e) below, because they go beyond (a) and (b) and a lawyer may want to take them out.
The tables are generated from the `.l4` files by `work/marginal.py` (each row is a `-- FALSE-kind` or `-- NOTHING-kind (limited by its own wording)` comment, with the rule it sits in), so every branch that rests on one of these readings is listed, and the line numbers are those of the files as they stand.
A `FALSE` branch that is not in the tables is a flat negative or a "means" definition (there are 42 of them; each carries the quoted words in its comment).

**Corrections made late in the run, for the record.**
In a final audit of every `FALSE-kind` branch against the brief, ten branches in eight rules that I had first answered `FALSE` were changed to `NOTHING`, because the words were a "where" (not an "if"), a stated period or start ("for life", "commencing from", "payable for such period as may be determined"), a named complement with no "only" (the widow or a prescribed person), or a duty with no stated consequence ("shall be made in the prescribed manner").
They are `sch 7 pt I para 4(1)` and `6(1)` (the "where the beneficiary is entitled to an unemployability supplement" limb), `sch 7 pt I para 2(4)`, `sch 7 pt V para 13(3)`, `sch 7 pt VI para 15(2)` (before the death and after the widow's death), `sch 7 pt VI para 18(1)` (the "where at his death" limb and a person who is neither the widow nor prescribed), `sch 10 para 5` (an election not made in the prescribed manner) and `sch 10 para 6(1)`.
Their tests and the seat cases were changed with them, by hand, from the text (finding 25).

**Corrections made at the triage after the independent test pass (2026-11-04), for the record.**
Seven rules changed their answers, and each change makes a rule that this encoding already applied elsewhere apply to a rule where it had not been applied (finding 27).
(1) The provisions that deem something and open with "If" or "so long as" (`sch 7 pt VI para 20`, `sch 7 pt VI para 21`, `sch 12 para 3(2)` for the first day, `sch 7 pt IV para 11(6)`) had answered `NOTHING` when their condition failed, while every other "if" in the range answered `FALSE`; they now answer `FALSE` (reading (a)), and so do "does not affect death benefit where the death occurred before ..." in paragraphs 20(3) and 21(3), which is a flat negative.
(2) `sch 5 para 3C(1)(d)` is the predicate for the 12-month limit and now answers `FALSE` short of it, as `sch 5 para A1(1) the period of deferment is at least 12 months` always did; `sch 5 para 3C(1)` still answers `NOTHING` for a short deferment, because it is introduced by "where".
(3) `sch 7 pt I para 1` and `sch 7 pt VI para 14(1)` answer `TRUE` inside the scope that their "only" sentence fixes (reading (e)); they answered `NOTHING` there.
Their tests and the seat cases were changed with them, by hand, from the text.

### Reading (a): a failed condition counted as the text's no (27 branches)

Each branch answers `FALSE` because a condition the text introduces with "if", "only if", "while", "until", "so long as" or "for any period for which/during which" failed.
The other reading: the text says what follows when the condition holds and is silent when it fails, so the answer is `NOTHING`.

| rule | file:line | the words |
| --- | --- | --- |
| `sch 12 para 3(2) the day is or forms part of a period of incapacity for work` | ssc9-sch12-13.l4:83 | "If the first day immediately following the day on which the period of entitlement came to an end— (a) is a day of incapacity for work ..., and (b) is not a day in relat... |
| `sch 5 para 7(3) the woman falls within this sub-paragraph` | ssc9-sch5-w.l4:226 | "a woman falls within this sub-paragraph if" both (a) and (b) |
| `sch 5 para 1(2) the amount by which the rate of the pension is increased` | ssc9-sch5.l4:141 | "but only if that amount is enough to increase the rate of the pension by at least 1 per cent" |
| `sch 5A para 2(2) the amount by which the rate of the pension is increased` | ssc9-sch5a.l4:103 | "but only if that amount is enough to increase the rate of the pension by at least 1 per cent" |
| `sch 6 para 6(2) a provisional assessment is made` | ssc9-sch6.l4:129 | "If on any assessment the condition of the claimant is not such ... as to allow of a final assessment" (a failed "if") |
| `sch 7 pt I para 2(3) the beneficiary may be treated as incapable of work and likely to remain so permanently` | ssc9-sch7-p1.l4:46 | "may be treated ... if it is likely to prevent his earnings in a year exceeding a prescribed amount" (a failed "if") |
| `sch 7 pt I para 2(1) the weekly rate is increased` | ssc9-sch7-p1.l4:62 | "if ... the beneficiary is incapable of work and likely to remain so permanently" (a failed "if") |
| `sch 7 pt I para 4(1) the weekly rate is increased for children` | ssc9-sch7-p1.l4:297 | "shall be increased for any period during which the beneficiary is entitled to child benefit" (a failed "while": marginal reading (a)) |
| `sch 7 pt I para 5(2) the condition in paragraph (b) of sub-paragraph (1) is satisfied` | ssc9-sch7-p1.l4:332 | "if, and only if ... at a weekly rate not less than the amount" |
| `sch 7 pt I para 5(1) the increase for the child may be payable` | ssc9-sch7-p1.l4:353 | "payable only if during that period one or other of the following conditions is satisfied" |
| `sch 7 pt I para 6(1) the weekly rate is increased for an adult dependant` | ssc9-sch7-p1.l4:401 | "shall be increased ... for any period during which" (a) or (b) (a failed "while": marginal reading (a)) |
| `sch 7 pt II para 9(1) the employed earner is entitled to a disablement gratuity` | ssc9-sch7-p2.l4:63 | "shall be entitled to a disablement gratuity, if— (a) he made a claim for disablement benefit before 1st October 1986; (b) ... not less than 1 per cent.; and (c) ... les... |
| `sch 7 pt IV para 11(1) the employed earner is entitled to reduced earnings allowance` | ssc9-sch7-p4.l4:49 | "an employed earner shall be entitled" |
| `sch 7 pt IV para 11(1) the employed earner is entitled to reduced earnings allowance` | ssc9-sch7-p4.l4:51 | "(a) he is entitled to a disablement pension or would be so entitled" |
| `sch 7 pt IV para 11(1) the employed earner is entitled to reduced earnings allowance` | ssc9-sch7-p4.l4:53 | "(b) ... either (i) ... and (ii) ... or is, and has at all times since the end of the period of 90 days ... been, incapable" |
| `sch 7 pt IV para 11(6) the person is treated as incapable of following the regular occupation` | ssc9-sch7-p4.l4:150 | "so long as he is, as a result of the relevant loss of faculty, deprived in whole or in part of those prospects, he is to be treated as incapable" (a failed "so long as") |
| `sch 7 pt IV para 11(8)(b) the allowance may be awarded for a further period` | ssc9-sch7-p4.l4:165 | "if at the end of that period the beneficiary submits a fresh claim for the allowance" (a failed "if") |
| `sch 7 pt V para 13(2) the person is entitled to retirement allowance` | ssc9-sch7-p4.l4:368 | "If the day before ... he is entitled ... at a weekly rate ... of not less than £2.00, he shall be entitled" (a failed "if") |
| `sch 7 pt VI para 15(1) the widow is entitled to death benefit` | ssc9-sch7-p6.l4:80 | "The widow of the deceased shall be entitled to death benefit if at his death either (a) ... or (b) ..." (a failed "if") |
| `sch 7 pt VI para 15(2) the pension is payable on the day` | ssc9-sch7-p6.l4:103 | "payable ... until she remarries or forms a civil partnership"; "until" read as ending the pension on the day of the remarriage (fork F11, NOTES.md) |
| `sch 7 pt VI para 17(1) the widower is entitled to death benefit` | ssc9-sch7-p6.l4:199 | "The widower of the deceased shall be entitled to death benefit if at her death he (a) ... and (b) ..." (a failed "if") |
| `sch 7 pt VI para 18(1) the person satisfies the conditions for an allowance for the child` | ssc9-sch7-p6.l4:250 | "for any period for which ... is entitled to child benefit" (a failed "while": marginal reading (a)) |
| `sch 7 pt VI para 20 the person is regarded as having died as a result of the injury` | ssc9-sch7-p6.l4:342 | "If a person dies at a time when— (a) he is entitled to an increase under section 104 ... or (b) he would have been so entitled but for" (a failed "if"; neither limb is ... |
| `sch 7 pt VI para 20 the person is regarded as having died as a result of the injury` | ssc9-sch7-p6.l4:345 | "If a person dies at a time when— (a) ... the amount of the increase is not less than the amount which at that time is specified" (a failed "if"; limb (b) was not met ei... |
| `sch 7 pt VI para 21 the death is treated as caused by the disease for which the benefit was payable` | ssc9-sch7-p6.l4:374 | "If a person dies as a result of any pulmonary disease and— (a) he was entitled, for a period which includes the date of his death, to disablement pension or gratuity" (... |
| `sch 7 pt VI para 21 the death is treated as caused by the disease for which the benefit was payable` | ssc9-sch7-p6.l4:379 | "(b) the extent of the disablement ... was assessed for such a period at not less than 50 per cent., then" (a failed "if": requirement (b) is not met) |
| `sch 7 pt VI para 21 the death is treated as caused by the disease for which the benefit was payable` | ssc9-sch7-p6.l4:382 | "the requirements of paragraph (b) of sub-paragraph (1) above shall be treated as unsatisfied" (a failed "if": requirement (b) is treated as not met) |

### Reading (c), mine: a priority rule excludes the person who loses (7 branches)

"As between X and Y, the former shall be entitled" names the winner; the branch answers `FALSE` for the loser, because a rule of priority between two claimants is a rule of exclusion.
The other reading: the paragraph says who is entitled and does not in terms say the other is not, so the answer for the loser is `NOTHING`. Converting these is a redesign of the Schedule 10 seat composite, which relies on the loser being `JUST FALSE` to stop its chain of paragraphs, and not a flip of seven branches. Paragraph 19 (a) ("not more than one of those persons shall be entitled") is arguably a flat negative and could move to the flat list.

| rule | file:line | the words |
| --- | --- | --- |
| `sch 7 pt VI para 19 the person is the one entitled to the allowance for the child` | ssc9-sch7-p6.l4:312 | "(a) not more than one of those persons shall be entitled ... in respect of the same child", and (b) names the widow or widower |
| `sch 10 para 1 the person is the one entitled` | ssc9-sch9-10.l4:73 | "the latter shall be entitled" |
| `sch 10 para 2 the person is the one entitled` | ssc9-sch9-10.l4:94 | "the former shall be entitled" |
| `sch 10 para 3 the person is the one entitled` | ssc9-sch9-10.l4:111 | "the woman shall be entitled" |
| `sch 10 para 4(1) the person is the one entitled` | ssc9-sch9-10.l4:129 | "the parent shall be entitled" |
| `sch 10 para 4(2) the person is the one entitled` | ssc9-sch9-10.l4:148 | "the mother shall be entitled" |
| `sch 10 para 5 the person is the one entitled` | ssc9-sch9-10.l4:176 | "such one of them shall be entitled as they may jointly elect" |

### Reading (d), mine: a closed set read from "shall be" or "other than" without "only" (2 branches)

The branch answers `FALSE` for a case outside a set that the text fixes with "shall be all ..." or "without reference to ... other than ...".
The other reading: the set is not closed by "only" or "nothing but", so the answer outside it is `NOTHING`. Converting these touches the Schedule 6 tests and the seat's Schedule 6 questions.

| rule | file:line | the words |
| --- | --- | --- |
| `sch 6 para 1(a) the disability is taken into account` | ssc9-sch6.l4:37 | "the disabilities to be taken into account shall be all disabilities so incurred ... to which the claimant may be expected ... to be subject during the period taken into... |
| `sch 6 para 1(c) the assessment may refer to the circumstance` | ssc9-sch6.l4:62 | "the assessment shall be made without reference to the particular circumstances of the claimant other than age, sex, and physical and mental condition" |

### Reading (e), mine: a scope clause with "only" also states its scope (2 branches)

Each branch answers `TRUE` inside the scope that a sentence with "only" fixes ("applies only in relation to ...", "only has effect in relation to ..."). Outside that scope the answer is `FALSE` (a list closed with "only"), which is not marginal.
The other reading: "only" gives a necessary condition and nothing more, so the answer inside the scope is `NOTHING` and the rest of the Part decides. Taking it out is one line in each of the two functions, and the same line in the test and seat case that pins it. This encoding states the scope of Part III paragraph 10(1) without "only" and answers `TRUE` inside it.

| rule | file:line | the words |
| --- | --- | --- |
| `sch 7 pt I para 1 this Part applies to the person` | ssc9-sch7-p1.l4:28 | "applies only in relation to persons who were beneficiaries in receipt of unemployability supplement" is read as stating the Part's scope, so such a person is inside it |
| `sch 7 pt VI para 14(1) this Part has effect in relation to the death` | ssc9-sch7-p6.l4:27 | "only has effect in relation to deaths before 11th April 1988" is read as stating the Part's scope, so a death before that day is inside it |

### Reading (b): a grant or prohibition limited by its own wording, so the case outside the limit is not a `FALSE` (93 branches)

Each branch answers `NOTHING` because the text's own words (a "where", "subject to", a stated period or start, "to the extent", a named complement) limit the provision and the case falls outside the limit.
The other reading: the case outside the limit is the text's no, so the answer is `FALSE`.

| rule | file:line | the words |
| --- | --- | --- |
| `sch 11 para 1 a period of entitlement may arise` | ssc9-sch11.l4:141 | the Schedule only removes periods of entitlement; section 153 says when one begins |
| `sch 12 para 1 the day counts as a day of incapacity for work for incapacity benefit` | ssc9-sch12-13.l4:30 | the paragraph speaks only of a day within (a) and (b) |
| `sch 12 para 3(2) the day is or forms part of a period of incapacity for work` | ssc9-sch12-13.l4:81 | "the first day" and "each of the first two consecutive days, or the first three" name no other day |
| `sch 12 para 3(2) the day is or forms part of a period of incapacity for work` | ssc9-sch12-13.l4:85 | sub-paragraph (3) is introduced by "Where each of the first two consecutive days, or the first three consecutive days, ... is a day to which paragraphs (a) and (b) ... a... |
| `sch 12 para 4(1) section 30A(3) does not apply to the day` | ssc9-sch12-13.l4:103 | "does not apply in relation to any day which (a) ... and (b) ..." says nothing of other days |
| `sch 12 para 4(2) section 30A(3) does not apply to the later day` | ssc9-sch12-13.l4:113 | "Where sub-paragraph (1) above applies in relation to a day" |
| `sch 12 para 5 paragraph 1 applies` | ssc9-sch12-13.l4:125 | the paragraph says only that paragraph 1 does not apply for that purpose |
| `sch 12 para 6 paragraph 1 applies` | ssc9-sch12-13.l4:136 | the paragraph says only that paragraph 1 does not apply for that purpose |
| `sch 13 para 1 the day counts as a day of incapacity for work for incapacity benefit` | ssc9-sch12-13.l4:152 | the paragraph speaks only of a day within the maternity pay period |
| `sch 5 para 8(4) the conditions in paragraphs 3C(1)(c) and 4(1)(a) are satisfied by S’s pension` | ssc9-sch5-w.l4:38 | the sub-paragraph speaks only of a Category B pension earned by W's contributions |
| `sch 5 para 3C(1) this paragraph applies` | ssc9-sch5-w.l4:60 | "this paragraph applies where" (a), (b) and (c) |
| `sch 5 para 3C(1) this paragraph applies` | ssc9-sch5-w.l4:62 | "Subject to paragraph 8", and condition (c) is not satisfied by such a pension |
| `sch 5 para 3C(1) this paragraph applies` | ssc9-sch5-w.l4:66 | "this paragraph applies where ... (d)" is a "where", not an "if"; paragraph 4(1)(c) speaks of this case |
| `sch 5 para 4(5) this paragraph does not apply` | ssc9-sch5-w.l4:128 | the sub-paragraph names only a death before 6 April 1979 with W of pensionable age before then |
| `sch 5 para 4(1) this paragraph applies` | ssc9-sch5-w.l4:154 | "applies where a widow, widower or surviving civil partner (W) is entitled ... and was married to or was the civil partner of ... (S) when S died" |
| `sch 5 para 4(1) this paragraph applies` | ssc9-sch5-w.l4:158 | none of the conditions (a), (b) or (c) is met |
| `sch 5 para 4(4) the amount of the increase to which W is entitled` | ssc9-sch5-w.l4:210 | "In any case where (a) ... and (b) ..." |
| `sch 5 para 5(1) this paragraph applies` | ssc9-sch5-w.l4:246 | "Where (a) ... and (b) S either (i) ... or (ii) ..." |
| `sch 5 para after 7(3) the modification of paragraphs 5A to 6A applies` | ssc9-sch5-w.l4:309 | "This paragraph modifies paragraphs 5A to 6A in cases where (a) ... and (b) ..." |
| `sch 5 para 5 the amount by which the rate of W’s pension is increased` | ssc9-sch5-w.l4:460 | paragraph 5(1) does not apply |
| `sch 5 para 7A(2) W is entitled to a widowed person’s or surviving civil partner’s lump sum` | ssc9-sch5-w.l4:484 | "This paragraph applies where a person to whom paragraph 3C applies (W) has made (or is treated as having made) an election under paragraph 3C(2)(b)" |
| `sch 5 para 7B(7) the lump sum after the orders` | ssc9-sch5-w.l4:598 | "In any case where (a) ... and (b) ..." |
| `sch 5 para 8(5) the increase or lump sum to which W is entitled under paragraph 4(1A) or 7A(2)` | ssc9-sch5-w.l4:623 | "Where the Category A retirement pension ... includes an increase under section 51A(2) attributable to W’s contributions" |
| `sch 5 para A1(1) the person must elect` | ssc9-sch5.l4:60 | "Where a person’s entitlement to a Category A or Category B retirement pension is deferred" |
| `sch 5 para A1(1) the person must elect` | ssc9-sch5.l4:64 | "and the period of deferment is at least 12 months" |
| `sch 5 para 1(1) this paragraph applies` | ssc9-sch5.l4:121 | "This paragraph applies where a person’s entitlement to a Category A or Category B retirement pension is deferred" |
| `sch 5 para 1(1) this paragraph applies` | ssc9-sch5.l4:128 | neither condition (a) nor (b) is met, and the sub-paragraph says only when it applies |
| `sch 5 para 2(7) the rate for an incremental period` | ssc9-sch5.l4:243 | "Where one or more orders have come into force ... during the period of deferment" |
| `sch 5 para 2(8) the weekly rate used for an increment` | ssc9-sch5.l4:257 | "Where a pensioner’s rights premium is paid ... after the date on which the premium is paid" |
| `sch 5 para 1 the amount by which the pension is increased for the deferment` | ssc9-sch5.l4:274 | paragraph 1(1) never answers FALSE |
| `sch 5 para 1 the amount by which the pension is increased for the deferment` | ssc9-sch5.l4:275 | paragraph 1(1) does not apply on these facts |
| `sch 5 para 2A(1) this paragraph applies` | ssc9-sch5.l4:294 | "This paragraph applies where ..." (a), (b) and (c) |
| `sch 5 para 3A(2) the person is entitled to a lump sum` | ssc9-sch5.l4:334 | "This paragraph applies where ..." (a) and (b) |
| `sch 5 para 3B(3) the percentage rate R` | ssc9-sch5.l4:409 | "such higher rate as may be prescribed" names a rate higher than base rate plus two |
| `sch 5A para 1(1) the person must elect` | ssc9-sch5a.l4:37 | "Where a person’s entitlement to a shared additional pension is deferred" |
| `sch 5A para 1(1) the person must elect` | ssc9-sch5a.l4:41 | "and the period of deferment is at least 12 months" |
| `sch 5A para 2(1) this paragraph applies` | ssc9-sch5a.l4:84 | "This paragraph applies where a person’s entitlement to a shared additional pension is deferred" |
| `sch 5A para 2(1) this paragraph applies` | ssc9-sch5a.l4:91 | neither (a) nor (b) is met |
| `sch 5A para 3(6) the rate for an incremental period` | ssc9-sch5a.l4:164 | "Where one or more orders have come into force under section 150 ... during the period of deferment" |
| `sch 5A para 2 the amount by which the shared additional pension is increased for the deferment` | ssc9-sch5a.l4:183 | paragraph 2(1) never answers FALSE |
| `sch 5A para 2 the amount by which the shared additional pension is increased for the deferment` | ssc9-sch5a.l4:184 | paragraph 2(1) does not apply on these facts |
| `sch 5A para 4(2) the person is entitled to a lump sum` | ssc9-sch5a.l4:201 | "This paragraph applies where (a) ... and (b) ..." |
| `sch 6 para 6(3) the assessment is a final assessment` | ssc9-sch6.l4:167 | "Where the assessed extent ... amounts to less than 14 per cent." says nothing of an extent of 14 per cent or more |
| `sch 6 para 6(3) the period taken into account may end on the day` | ssc9-sch6.l4:179 | "shall not end before" says nothing of an end on or after that date |
| `sch 7 pt I para 2(4) the supplement is payable on the day` | ssc9-sch7-p1.l4:95 | "payable for such period" says when it MAY be payable; whether it is payable then is decided by the rest of the Act |
| `sch 7 pt I para 2(4) the supplement is payable on the day` | ssc9-sch7-p1.l4:96 | "payable for such period as may be determined" is a stated period; the sub-paragraph does not say the supplement is unpayable outside it |
| `sch 7 pt I para 4(1) the weekly rate is increased for children` | ssc9-sch7-p1.l4:294 | "where the beneficiary is entitled to an unemployability supplement" is a "where", not an "if", so the sentence says nothing of a beneficiary without one |
| `sch 7 pt I para 4(1) the weekly rate is increased for children` | ssc9-sch7-p1.l4:296 | "Subject to the provisions of this paragraph and paragraph 5"; the grant is cut back by 4(4) and 5(1) |
| `sch 7 pt I para 5(1) the increase for the child may be payable` | ssc9-sch7-p1.l4:350 | "payable only if" is a necessary condition; paragraph 4 and the other conditions decide |
| `sch 7 pt I para 6(1) the weekly rate is increased for an adult dependant` | ssc9-sch7-p1.l4:392 | "where the beneficiary is entitled to an unemployability supplement" is a "where", not an "if" |
| `sch 7 pt I para 8(1) the increase is payable for the week` | ssc9-sch7-p1.l4:447 | the paragraph speaks only of a beneficiary who "has been awarded" an increase and "ceases to be entitled ... by reason only" of the earnings |
| `sch 7 pt II para 9(3) the person may be entitled to a gratuity on the day` | ssc9-sch7-p2.l4:43 | "until after the expiry": after the 90 days the sub-paragraph says nothing; sub-paragraph (1) decides |
| `sch 7 pt III para 10(1) this Part has effect in relation to the period` | ssc9-sch7-p2.l4:105 | "in relation to a period during which a person is receiving medical treatment as an in-patient" |
| `sch 7 pt III para 10(1) this Part has effect in relation to the period` | ssc9-sch7-p2.l4:108 | neither (a) nor (b) is met |
| `sch 7 pt III para 10(2) the extent treated as assessed for the part of the period` | ssc9-sch7-p2.l4:130 | "Where a person is awarded disablement benefit, but the extent ... at less than 100 per cent": otherwise the assessment stands and sub-paragraph (2) says nothing |
| `sch 7 pt IV para 11(1) the employed earner is entitled to reduced earnings allowance` | ssc9-sch7-p4.l4:61 | "to the extent that" and "only in so far as" leave an entitlement for the part outside the exclusion, and the text does not apportion it |
| `sch 7 pt IV para 11(2) the person may again be entitled for the period` | ssc9-sch7-p4.l4:85 | "this sub-paragraph does not prevent the making ... of a claim for, or an award of" says only that this bar does not apply; sub-paragraph (1) decides |
| `sch 7 pt IV para 11(2) the person may again be entitled for the period` | ssc9-sch7-p4.l4:87 | "A person (a) who ... but (b) who subsequently ceases" |
| `sch 7 pt IV para 11(3)(a) the person is treated as entitled on the day` | ssc9-sch7-p4.l4:100 | "a person who ... shall be treated as entitled ... on any day on which he would have been entitled" says nothing of anyone else |
| `sch 7 pt IV para 11(5)(a) the occupation counts as the regular occupation` | ssc9-sch7-p4.l4:118 | the sub-paragraph only excludes subsidiary occupations; what is a regular occupation is not defined |
| `sch 7 pt IV para 11(5)(b) the employment may count as employment of an equivalent standard` | ssc9-sch7-p4.l4:127 | "equivalent standard" is otherwise undefined and turns on remuneration and prospects (the last clause of 11(5), which directs regard to be had to a reasonable prospect o... |
| `sch 7 pt IV para 11(5) regard is to be had to the reasonable prospect of advancement` | ssc9-sch7-p4.l4:139 | "in assessing the standard of remuneration in any employment": the direction speaks only of that assessment |
| `sch 7 pt IV para 11(9) the award may be for the period` | ssc9-sch7-p4.l4:177 | "may not be longer" is a limit and no grant |
| `sch 7 pt IV para 12(1) the person is entitled to reduced earnings allowance for life` | ssc9-sch7-p4.l4:269 | "A person who on 10th April 1988 or 9th April 1989 satisfies the conditions" says nothing of anyone else |
| `sch 7 pt IV para 12(5) the relevant date` | ssc9-sch7-p4.l4:284 | the relevant date is defined for a beneficiary entitled by virtue of sub-paragraph (1) |
| `sch 7 pt IV para 12(2) the weekly rate of the allowance for life` | ssc9-sch7-p4.l4:321 | the assumption is given for those two dates only |
| `sch 7 pt V para 13(1) the day from which the person ceases to be entitled to reduced earnings allowance` | ssc9-sch7-p4.l4:354 | "a person who ... shall cease to be entitled" says nothing of anyone else |
| `sch 7 pt V para 13(2) the person is entitled to retirement allowance` | ssc9-sch7-p4.l4:369 | sub-paragraph (2) speaks of a person who "ceases under sub-paragraph (1) above" |
| `sch 7 pt V para 13(3) retirement allowance may be payable on the day` | ssc9-sch7-p4.l4:383 | "subject to any enactment contained in Part V or VI of this Act or in the Administration Act and to any regulations made under any such enactment" |
| `sch 7 pt V para 13(3) retirement allowance may be payable on the day` | ssc9-sch7-p4.l4:384 | "payable ... for life" is a stated period; the sub-paragraph does not say the allowance is unpayable after death |
| `sch 7 pt V para 13(6) the weekly rate of retirement allowance after rounding` | ssc9-sch7-p4.l4:431 | "would exceed the whole number of pence next below it by 1/2p or more"; the text does not round a fraction of less than 1/2p |
| `sch 7 pt VI para 14(1A) a claim for industrial death benefit may be made` | ssc9-sch7-p6.l4:43 | a claim not barred by this sub-paragraph is decided by the other paragraphs |
| `sch 7 pt VI para 15(2) the pension is payable on the day` | ssc9-sch7-p6.l4:101 | "a pension commencing from the death of the deceased" is a stated start; the sub-paragraph does not say a pension is unpayable before it |
| `sch 7 pt VI para 15(2) the pension is payable on the day` | ssc9-sch7-p6.l4:105 | "payable ... for life" is a stated period; the sub-paragraph does not say the pension is unpayable after the widow's death |
| `sch 7 pt VI para 15(3) the pension may be payable for the period` | ssc9-sch7-p6.l4:126 | "shall not be payable" is a bar and no grant |
| `sch 7 pt VI para 16 the weekly rate of the widow's pension on the day` | ssc9-sch7-p6.l4:174 | the pension commences from the death |
| `sch 7 pt VI para 18(1) the person satisfies the conditions for an allowance for the child` | ssc9-sch7-p6.l4:248 | "where at his death the deceased was entitled to child benefit" is a "where", not an "if" |
| `sch 7 pt VI para 18(1) the person satisfies the conditions for an allowance for the child` | ssc9-sch7-p6.l4:252 | "Subject to paragraph 19 below"; the allowance is cut back by paragraph 19 and paragraph 5 |
| `sch 7 pt VI para 18(1) the person satisfies the conditions for an allowance for the child` | ssc9-sch7-p6.l4:254 | "the widow or, as the case may be, the person so prescribed shall be entitled" names two persons and does not say "only" |
| `sch 7 pt VI para 18(1) the person satisfies the conditions for an allowance for the child` | ssc9-sch7-p6.l4:257 | "Subject to paragraph 19 below" |
| `sch 7 pt VI para 19 the person is the one entitled to the allowance for the child` | ssc9-sch7-p6.l4:308 | "Where two or more persons satisfy the conditions" |
| `sch 9 para 1 the person may be entitled to child benefit for the week` | ssc9-sch9-10.l4:36 | "no person shall be entitled ... if" is a bar and no grant; section 142 and the rest of Part IX decide |
| `sch 9 para 3 the person may be entitled to child benefit for the child or qualifying young person` | ssc9-sch9-10.l4:49 | a bar and no grant |
| `sch 10 para 1 the person is the one entitled` | ssc9-sch9-10.l4:70 | "shall not confer any priority" says only that this paragraph does not decide; the later paragraphs do |
| `sch 10 para 2 the person is the one entitled` | ssc9-sch9-10.l4:90 | "Subject to paragraph 1 above" |
| `sch 10 para 2 the person is the one entitled` | ssc9-sch9-10.l4:95 | "as between a person entitled ... by virtue of paragraph (a) ... and a person entitled by virtue of paragraph (b)" |
| `sch 10 para 3 the person is the one entitled` | ssc9-sch9-10.l4:108 | "Subject to paragraphs 1 and 2 above, as between a man and woman who are married to, or civil partners of, each other and are residing together" |
| `sch 10 para 4(1) the person is the one entitled` | ssc9-sch9-10.l4:125 | "Subject to paragraphs 1 to 3 above" |
| `sch 10 para 4(1) the person is the one entitled` | ssc9-sch9-10.l4:130 | "as between a person who is and one who is not a parent" |
| `sch 10 para 4(2) the person is the one entitled` | ssc9-sch9-10.l4:144 | "Subject as aforesaid, as between two persons residing together who are parents ... but do not fall within paragraph 3" |
| `sch 10 para 4(2) the person is the one entitled` | ssc9-sch9-10.l4:149 | the sub-paragraph names the mother and no one else |
| `sch 10 para 5 the person is the one entitled` | ssc9-sch9-10.l4:170 | "As between persons not falling within paragraphs 1 to 4 above" |
| `sch 10 para 6(1) the election is an election under this Schedule` | ssc9-sch9-10.l4:189 | "shall be made in the prescribed manner" is a necessary condition, not the whole of validity |

### Reading a result: FALSE and NOTHING (ssc9)

Every decision function in these Schedules answers one of three things, and the reader must not fold the second into the third.

- **`JUST TRUE` and `JUST x`** mean the text, read as the module reads it, gives the person the benefit, the increase, the priority or the amount, on the facts typed in.
- **`JUST FALSE` ("no")** means the text itself says no to this case in its own words, which in these Schedules is one of four things.
  A flat negative: "no person shall be entitled to child benefit in respect of a child ... who is married" (Schedule 9), "shall not be payable for any period during which the beneficiary is living as a married couple with a person whom she is not married to" (Schedule 7 Part VI paragraph 15(3)), "A period of entitlement does not arise" (Schedule 11).
  A definition that says "means" or "shall be taken to be", for example "the deceased" (Schedule 7 Part VI paragraph 14(2)) and the rounding of an amount under 1/2p to zero.
  A condition the text introduces with "if", "only if", "while", "until" or "so long as" that the facts fail ("shall be entitled to a disablement gratuity, if ...", "shall be increased ... for any period during which ...", "payable ... until she remarries", "so long as he is ... deprived ... he is to be treated as incapable").
  A cap or floor in terms ("but not in any case exceeding", "shall not end before").
- **`NOTHING` ("not covered")** means the text, read as the module reads it, does not answer.
  In these Schedules it arises for one of five reasons (the sixth named in the brief, "includes", is not needed here), and each branch's comment says which; the counts in the files are 93 limited by its own wording, 37 points outside the text, 12 silent, 8 undefined term and 1 list not closed.
  *Limited by its own wording*: a provision that "applies where" or "applies in relation to" some case, or is "subject to" another paragraph, or gives something for a stated period or from a stated day, says nothing about a case outside its limit, and says only that the grant is cut back when its own conditions hold (so a grant that holds on the facts is also `NOTHING`, because the paragraph it is "subject to" decides the rest, and the seat layer composes them).
  *Points outside the text*: every rate in Schedule 4, every prescribed amount, period or circumstance, every regulation or order, and every term borrowed from the Pensions Act 1995, the Jobseekers Act 1995 and the Children's Hearings (Scotland) Act 2011.
  *Undefined term*: "the appropriate amount" outside the modified cases; "equivalent standard" in Schedule 7 Part IV.
  *Silent*: an election not made in the prescribed manner; a fraction under 1/2p in paragraph 13(6).
  *List not closed*: where the text lists without "only" (one branch).
  Several of these are answered `NOTHING` on purpose where a caller would be tempted to turn them into `FALSE`: **a caller must never turn `NOTHING` into `FALSE`.**
- **The omitted formula.**
  Schedule 5 paragraphs 3B(3) and 7B(3) and Schedule 5A paragraph 5(3) say that "the accrued amount for an accrual period is" and then go straight to "where--": the converter dropped the formula.
  The functions that would apply it answer `NOTHING` always, and the lump sum is taken from an amount the person states.

For a person: a `FALSE` means "the Act says not in this case"; a `NOTHING` means "the Act, as this text shows it, does not settle this case, and someone (the Secretary of State, a regulation, Schedule 4, a lawyer) has to".

## Seams (ssc9)

One line per seam: asking section, answering section, the name and type of the input.
The inputs are `GIVEN` parameters named with the answering section's label (PLAN.md section 1.3), so the lead can find them by name at the merge.
The ids are those of PLAN.md section 5.

### Seams the plan names, as taken

| id | asking rule (lines) | answering section | input name | type |
| --- | --- | --- | --- | --- |
| S18 | `sch 7 pt I para 5(2) the condition in paragraph (b) of sub-paragraph (1) is satisfied` (5426-5430) | ssc5 s 143(1)(b) | `s 143(1)(b) the contributions are over and above those required for satisfying section 143(1)(b)` | `MAYBE BOOLEAN` |
| S21 | asked by ssc4 s 103(5); answered here by `sch 6 the extent of the disablement assessed, as a percentage` (5345) | ssc9 Schedule 6 | (this part answers; it takes `the percentage the disabilities taken into account amount to`, the assessor's judgment, as a `MAYBE NUMBER`) | the answer is a `MAYBE NUMBER` |
| S32 | `sch 11 para 2(h) the circumstance applies` (5685, 5694) | ssc6 s 153(12) | `s 153(12) the relevant date falls within the disqualifying period` | `BOOLEAN` |
| S32 | `sch 11 para 2(h) the circumstance applies` (5685, 5694) | ssc6 s 171(1) | `s 171(1) the pregnancy terminated otherwise than by confinement` | `BOOLEAN` |
| S33 | `sch 10 para 2 the person is the one entitled` (5660) | ssc5 s 143(1)(a) | `s 143(1)(a) the person is entitled for the week by virtue of paragraph (a)` | `BOOLEAN` |
| S33 | `sch 10 para 2 the person is the one entitled` (5660) | ssc5 s 143(1)(b) | `s 143(1)(b) the person is entitled for the week by virtue of paragraph (b)` | `BOOLEAN` |
| S34 | `sch 7 pt I para 2(1) the amount of the increase` (5385) | ssc8 Schedule 4 Part V paragraph 5 | `sch 4 pt V para 5 the increase of the disablement pension in pounds` | `MAYBE NUMBER` |
| S34 | `sch 7 pt I para 3(1) the increase before the deductions` (5390-5393) | ssc8 Schedule 4 Part V paragraph 6 | `sch 4 pt V para 6 the increase of the unemployability supplement in pounds` | `MAYBE NUMBER` |
| S36 | `sch 7 pt I para 2(1) the weekly rate is increased` (5385) | ssc4 s 94(6) | `s 94(6) the person is incapable of work, "work" meaning work the person can reasonably be expected to do` | `MAYBE BOOLEAN` |
| K2 | `sch 7 pt I para 3(1) the beneficiary meets the age condition on the qualifying date` (5390-5393) | keel s 173(a) | `s 173(a) the person is under 60`; `s 173(a) the person is under 55` | `MAYBE BOOLEAN` each |
| K2 | `sch 7 pt VI para 16(2)(b) the widow's age brings the higher permanent rate` (5587) | keel s 173(a) | `s 173(a) the person was over 50 at the deceased's death`; `s 173(a) the person was over 40 at the end of the period for which she was entitled to such an allowance` | `MAYBE BOOLEAN` each |

The two Part VI K2 names differ from the plan's pattern `s 173(a) the person is over <N>`: the age is asked at a past time (the death, the end of an allowance), so "is" became "was ... at ...".
The lead should wire them to s 173(a) with that time in mind.

**The plan's S34 asks for Schedule 4 Part V paragraphs 5 and 6 only.**
I found eight more paragraphs of the same table that this range needs, listed next.

### Seams I found that the plan lacks

Every one is an input, because Schedule 4 is omitted from this text (PLAN.md section 1.5) and the other sections belong to other parts.

| asking rule (lines) | answering section | input name | type |
| --- | --- | --- | --- |
| `sch 7 pt IV para 11(14)` and `sch 7 pt V para 13(11)` (5514, 5568) | ssc8 Schedule 4 Part V paragraph 1 | `sch 4 pt V para 1 the rate in the first entry in column (2), in pounds` | `MAYBE NUMBER` |
| `sch 7 pt VI para 20` (5610-5615) | ssc8 Schedule 4 Part V paragraph 2(a) | `sch 4 pt V para 2(a) the amount specified for constant attendance` | `MAYBE NUMBER` |
| `sch 7 pt I para 4(2)` (5410) | ssc8 Schedule 4 Part V paragraph 7 | `sch 4 pt V para 7 the increase for each child or qualifying young person in pounds` | `MAYBE NUMBER` |
| `sch 7 pt I para 6(2)` (5440) | ssc8 Schedule 4 Part V paragraph 8 | `sch 4 pt V para 8 the increase for an adult dependant in pounds` | `MAYBE NUMBER` |
| `sch 7 pt II para 9(2)(a)` (5465-5466) | ssc8 Schedule 4 Part V paragraph 9 | `sch 4 pt V para 9 the maximum disablement gratuity in pounds` | `MAYBE NUMBER` |
| `sch 7 pt VI para 16` (5584-5590) | ssc8 Schedule 4 Part V paragraph 10 | `sch 4 pt V para 10 the initial rate in pounds`; `... the higher permanent rate in pounds`; `... the lower permanent rate in pounds` | `MAYBE NUMBER` each |
| `sch 7 pt VI para 17(2)` (5595) | ssc8 Schedule 4 Part V paragraph 11 | `sch 4 pt V para 11 the weekly rate of the widower's pension in pounds` | `MAYBE NUMBER` |
| `sch 7 pt VI para 18(1)` (5597-5602) | ssc8 Schedule 4 Part V paragraph 12 | `sch 4 pt V para 12 the weekly rate of the allowance in pounds` | `MAYBE NUMBER` |
| `sch 11 the relevant date` (5686) | ssc6 s 153 | `s 153 the date on which a period of entitlement would begin if this Schedule did not prevent it arising` | `DATE` |

Facts about the person that belong to another Part, taken as plain inputs and not named in the plan's register (the lead may wire them to the section that decides them, or leave them as the person's own answers):

| asking rule (lines) | belongs to | input |
| --- | --- | --- |
| `sch 7 pt I para 5(1)` (5424), `sch 7 pt VI para 18(2)` (5603) | Part IX (ssc5, "treated as having the child living with him") | `the beneficiary would be treated for the purposes of Part IX as having the child or qualifying young person living with him` (`BOOLEAN`) |
| `sch 7 pt IV para 11(3)(a)` (5489-5490) | s 103(6) (ssc4) | `the person, apart from section 103(6), would have been entitled ...`; `the person would have been entitled on the day, apart from section 103(6)` (`BOOLEAN`) |
| `sch 7 pt IV para 11(1)` (5483-5484) | s 108(2) (ssc4) | `the claim is in relation to a disease prescribed on or after 10 October 1994 under section 108(2)` (`BOOLEAN`); the prescription extended case (`sch 7 pt IV Extent`) |
| `sch 7 pt VI para 20` (5610-5615) | s 104 (ssc4) | `the person was entitled to an increase under section 104 of a disablement pension, being a payment by way of increase ...` (`BOOLEAN`) |
| `sch 11 para 2(d)(i)` (5679) | s 30A(2)(a) (ssc2) | `the days on which the employee was entitled to incapacity benefit, or would have been so entitled had the contribution conditions mentioned in section 30A(2)(a) been satisfied` (`LIST OF DATE`) |
| `sch 7 pt I para 3(11)` (5407) | "section 46(6) and (7)", which this text's s 46 does not have (finding 7) | `section 46(6) or (7) limits the increase` (`MAYBE BOOLEAN`) |

Terms borrowed from an Act that is not among the sources, asked as facts (Guide section 4): the Jobseekers Act 1995 "jobseeking period" and "linked period" (`sch 7 pt I para 3(10)`, `sch 7 pt V para 13(10)`, `MAYBE BOOLEAN`); the Welfare Reform Act 2007 days of entitlement to employment and support allowance (`sch 11 para 2(dd)`, `LIST OF DATE`); the Pensions Act reductions under sections 46 and 109 and the guaranteed minimum pension increases (`sch 5` and `sch 7 pt I para 3(3)`, `NUMBER` and `BOOLEAN`); orders under section 150 or 150A of the Administration Act (`BOOLEAN`); the Children's Hearings (Scotland) Act 2011 supervision order and residential establishment (`sch 9 para 1`, `BOOLEAN`).
"Pensionable age" is the core's `Person` field `date of attaining pensionable age`.

### Seams other parts will ask of this one

S21 is the only one the plan names (ssc4 s 103(5), src:2357, asks `sch 6 the extent of the disablement assessed, as a percentage`).
Schedule 6 paragraph 6(1) in turn takes the "90 days" start from `sch 7 pt II para 9(3) the first day after the 90 days`, which is this part's own function, so that is not a seam.

## What the text turns out to say (findings)

Each finding was checked against the line it cites in `inputs/ukpga-1992-4.txt` when it was written down.
"The text" here is the converter rendering, not the official text.

1. **The converter dropped the paragraph numbers**, so every paragraph label is a citation or a count (section "Paragraph labels that are inferred").
   Section 55(2) (src:1687-1693) and section 55C(2) (src:1744-1746) list the paragraphs of Schedules 5 and 5A, which is the best check there is for those two.
2. **Schedule 4's tables are omitted**, so every rate in this range is an input: ten paragraphs of Schedule 4 Part V (1, 2(a), 5, 6, 7, 8, 9, 10, 11, 12) are asked for (section "Seams").
   Only two of them (5 and 6) are in the plan's seam register.
3. **The accrued-amount formula is omitted in three places**: Schedule 5 paragraph 3B(3) (src:5116-5119), paragraph 7B(3) (src:5255) and Schedule 5A paragraph 5(3) (src:5327-5330).
   Each says "The accrued amount for an accrual period ... is—" and goes at once to "where—".
   The three functions answer `NOTHING` always, and the lump sum in each case is an amount the person states.
4. **A pensioner who does not elect gets the lump sum, not the increase.**
   Paragraph A1(2) (src:5072), paragraph 3C(3) (src:5142) and Schedule 5A paragraph 1(2) (src:5298) each say that if no election is made within the prescribed period the person "is to be treated as having made an election under sub-paragraph (1)(b)" (or (2)(b)), which is the lump sum.
   The duty to elect is therefore discharged by the deeming, and the six `#TRACE` cases of the regulative rules end `FULFILLED` when the period passes with no election.
5. **"The appropriate amount" is used in six places in paragraphs 5A, 6 and 6A (src:5188, 5191, 5196, 5201, 5205, 5213) and defined only for the modified cases** (src:5240).
   This is fork F5.
6. **Schedule 7 Part I paragraph 5(2)(a) refers to "the amount referred to in that sub-paragraph" (src:5427), and paragraph 5(1) refers to no amount** (src:5423-5425 say only "the requisite contributions").
   The amount is taken as an input and the rule answers `NOTHING` while it is missing.
7. **Schedule 7 Part I paragraph 3(11) (src:5407) is "subject to section 46(6) and (7)", and section 46 of this text has only sub-sections (1) to (4)** (src:1424-1442).
   Whether anything limits the increase is taken as an input and the rule answers `NOTHING` when it is unknown or says yes.
8. **Schedule 10 paragraph 3 reaches only "a man and woman who are married to, or civil partners of, each other and are residing together"** (src:5662), and its heading says "Opposite-sex spouses or civil partners" (src:5661).
   Two spouses or civil partners of the same sex are not addressed by paragraph 3; paragraph 5 reaches "persons not falling within paragraphs 1 to 4" (src:5667).
9. **Paragraph 13(6) of Schedule 7 (src:5550-5553) rounds a fraction of 1/2p or more up and says nothing of a smaller fraction** (fork F9).
10. **Schedule 7 Part IV paragraph 11(2) says "that date" with no antecedent in the sub-paragraph** (src:5485-5486), and two dates precede it (fork F8).
11. **Schedule 11 paragraph 2 has no limb (e)** (the limbs run (d), (dd), (f), (g), (h): src:5678, 5682, 5683, 5684, 5685), and limbs (a), (b), (c), (d)(ii) and (d)(iii) are lines of dots (src:5675-5677, 5680-5681).
   The numbers of everything after paragraph 2 are lost.
12. **Schedule 7 Part IV paragraph 12(7) (src:5531-5533) repeats paragraph 11(12A) (src:5508-5510) word for word, except for the sub-paragraph it refers to** (12(1) and 11(11) respectively): both say what "a person who has retired from regular employment" includes.
13. **The rounding words differ between sister provisions**: "the next whole penny above" in paragraphs 2(4)(a), 7(2)(a) and 7C(1) (src:5090, 5217, 5280) and "the next whole penny" in Schedule 5A paragraphs 3(3) and 5(6) (src:5312, 5338) (fork F6).
14. **Schedule 7 Part IV paragraph 11(9) (src:5502) limits an award by "the period to be taken into account under paragraph 4 or 6 of Schedule 6", and paragraph 4 of Schedule 6 is a line of dots in this text** (src:5352).
    Only paragraph 6 (src:5355) gives a period, so the limit is encoded against the period the caller supplies.
15. **The Table of Derivations has notes and no rows** (src:5735-5744): it records where provisions came from, names three 1991 statutory instruments, and creates no rule.
16. **The last clause of Schedule 7 Part IV paragraph 11(5) (src:5496)** directs that "regard is to be had to his reasonable prospect of advancement" in assessing the standard of remuneration.
    It is encoded as a rule with one answer (`JUST TRUE` while the assessment is being made), not left inert.
17. **Schedule 7 Part I paragraph 4(5) lets the Secretary of State "substitute larger amounts"** (src:5420).
    An order that substitutes a smaller amount is outside the power, so the rule answers `NOTHING` for it and not the smaller amount.
18. **Schedule 7 Part VI paragraph 14(1A) (src:5572) bars claims "after the coming into force of this sub-paragraph"**, and the text does not give that day; it is an input.
19. **Twenty-five rows are regulation-making powers or orders** (inert, reason 2), and each of them states something a person could ask: whether an election can be changed (Schedule 5 paragraph A1(3), 3C(4), Schedule 5A paragraph 1(3)); how earnings are apportioned or estimated (Schedule 7 Part I paragraphs 6(3) to (6) and 7(2)); what "regular employment" means (Schedule 7 Part V paragraph 13(8)).
    The text gives no answer to any of them; they are listed under "What the text does not answer" in the final report.
20. **Schedule 13 paragraph 2(2) (src:5727) is itself conditional on regulations** ("Regulations may provide that an amount equal to a woman's statutory maternity pay ... shall be deducted").
    It is encoded as the deduction that applies if the regulations so provide, with the regulations' answer as a plain input.
21. **Two different "week" definitions apply in this range** (fork register, last paragraph): Schedule 7 Part I paragraph 4(6) (src:5421) is the core's sixth convention and Schedule 13 paragraph 3(2A) (src:5733) is its fourth.
22. **The Schedule 6 paragraph 6(2)(b) wording "begin with the end of the period"** (src:5358) can be read as the same day or the next (fork F7).
23. **The 12 months of a deferment that begins on 29 February** have no answer in the text (fork F1); the keel's K2 has a related leap-day case of its own.
24. **Schedule 10 paragraph 5 ends in the Secretary of State's discretion** ("as the Secretary of State may in his discretion determine", src:5667): the determination is an input that `NOTHING` stands in for until it is made, and the seat question asks the person for it.
25. **Where my own expectations were wrong.**
    (i) Early in the run, in the Schedule 7 Part II tests, I mis-counted a Saturday accident date by hand; I fixed the arithmetic, not the code.
    (ii) A hand-written seat expectation for Schedule 5 paragraph A1 for a deferment one day short of 12 months was `JUST FALSE`; the text says "Where ... the period of deferment is at least 12 months", a "where", so it is `NOTHING`.
    (iii) A test of Schedule 7 Part VI paragraph 15(2) for the day she died caught a boundary error in the code (the pension was payable on the day she died but not on the day after); I fixed the code.
    (iv) In a final audit of every `FALSE` branch against the brief, ten branches of eight rules were changed to `NOTHING` (section "Marginal readings for a lawyer"), and the tests and seat cases that expected `FALSE` were changed by hand from the text with them.
    No failing assertion remains, and none was made to pass by editing its expected value to match output.
26. **Schedule 5 paragraph 2A(3) (src:5103) gives no rounding rule.**
    The rounding in paragraph 2(4) (src:5089-5091) is for "an amount ... required to be calculated in accordance with the provisions of sub-paragraph (3) above", that is 2(3), so the increment under 2A(3) is not rounded here and is returned as the exact amount.
27. **Triage of the independent test pass (2026-11-04): what was changed, and what was kept and why.**
    *Changed* (section "Marginal readings for a lawyer", "Corrections made at the triage"): the deeming provisions that open with "If" or "so long as" now answer `FALSE` when the condition fails, the 12-month predicate in `sch 5 para 3C(1)(d)` answers `FALSE` short of the limit, and the two "only" scope sentences (`sch 7 pt I para 1`, `sch 7 pt VI para 14(1)`) answer `TRUE` inside their scope.
    *Kept as `NOTHING`, each on the ground its comment names:*
    (i) `sch 5 para A1(1) the person must elect` and `sch 5A para 1(1) the person must elect` for a deferment under 12 months: the text says "Where", and sub-paragraph (2) of the same paragraph says "If" (src:5072 and 5298), so the drafter used both; paragraphs 1(1)(a) (src:5081) and 2(1)(a) (src:5306) deal with the short deferment.
    (ii) `sch 5 para 4(5) this paragraph does not apply` and `sch 12 para 4(1) section 30A(3) does not apply to the day` outside the case or the 57 days they name: the provisions are prohibitions limited by their own wording (reading (b)), and a `FALSE` would say that paragraph 4, or section 30A(3), applies, which is for paragraph 4(1) and for section 30A(3) to say.
    (iii) `sch 7 pt II para 9(3) the person may be entitled to a gratuity on the day` after the 90 days: the sub-paragraph bars entitlement until then and grants nothing after, which sub-paragraph (1) decides.
    *Not a defect in the encoding:* the increment in `sch 5 para 2(3)` is rounded to the nearest penny by paragraph 2(4)(a) (src:5090), so 1/5th per cent of 184.90 is 0.37, not 0.3698 (a test now pins it).

## What the stable binary does not accept

The binary is the stable build 1.6.98; where it rejected something, I wrote what it accepts.
These were met while writing, each on the stable binary; I did not test each against the main build 1.6.108, but all 25 modules read the same four counts on both.

- **`REFUSE`, `#ASSERT REFUSED` and `BECAUSE`** do not exist; "not covered" is `NOTHING` (a `MAYBE`) and is asserted as `EQUALS NOTHING`.
- **A one-line `CONSIDER` with several `WHEN` arms does not parse inside a `WHERE`.** Each arm goes on its own line.
- **A nested `IF ... THEN ... ELSE` followed by an outer `ELSE` gives a layout error.** `BRANCH` with `IF ... THEN` arms and `OTHERWISE` is used instead.
- **A hyphen in an identifier reads as subtraction** (`max-date` is `max MINUS date`); the name was changed.
- **`NOT a AND b` parses as `NOT (a AND b)`.** Every `NOT` that is meant for one operand is parenthesised; the first draft of `sch 10 para 4(1)`, `4(2)` and the Schedule 11 joining rule had the bug and the tests caught it.
- **`JUST Date d m y` is ambiguous**, and `JUST (Date d m y)` is accepted.
- **`#TRACE` has no assertion form on the stable binary.** The three regulative duties (`sch 5 para A1(1) the election duty`, `sch 5 para 3C(2) the election duty`, `sch 5A para 1(1) the election duty`) are run with six `#TRACE` cases (an election made, and a lapse with a `WAITUNTIL`), all read `FULFILLED` on both builds; `check.sh` compares the four assertion counts and does not see a `#TRACE` outcome, so each duty is also encoded as a decision function (`... the person must elect`, `... the election that is treated as made`) with assertions.
- **A name defined in two imported modules cannot be used at all**, so every top-level name, type and constructor begins with its provision label and the modules share definitions only by import.

## What check.sh and srcrefs print

`check.sh` was run in the deposit folder as `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` (the deposit's own script, unchanged), after the last edit to any `.l4` file.
The sandbox's baseline before this part's work was the one module `ssc-core.l4` with 0 assertions; the keel's 165 assertions in PLAN.md count `ssc-definitions.l4`, which this sandbox does not hold.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc9-cases-seat.l4                             0       185       0        0         0 |      0       185       0        0  same
ssc9-sch11.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc9-sch12-13.l4                               0         0       0        0         0 |      0         0       0        0  same
ssc9-sch5-w.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc9-sch5.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc9-sch5a.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc9-sch6.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p1.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p2.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p4.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p6.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch9-10.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc9-tests-sch11.l4                            0        44       0        0         0 |      0        44       0        0  same
ssc9-tests-sch12-13.l4                         0        44       0        0         0 |      0        44       0        0  same
ssc9-tests-sch5-w.l4                           0       102       0        0         0 |      0       102       0        0  same
ssc9-tests-sch5.l4                             0        92       0        0         0 |      0        92       0        0  same
ssc9-tests-sch5a.l4                            0        47       0        0         0 |      0        47       0        0  same
ssc9-tests-sch6.l4                             0        53       0        0         0 |      0        53       0        0  same
ssc9-tests-sch7-p1.l4                          0       113       0        0         0 |      0       113       0        0  same
ssc9-tests-sch7-p2.l4                          0        32       0        0         0 |      0        32       0        0  same
ssc9-tests-sch7-p4.l4                          0       103       0        0         0 |      0       103       0        0  same
ssc9-tests-sch7-p6.l4                          0        99       0        0         0 |      0        99       0        0  same
ssc9-tests-sch9-10.l4                          0        44       0        0         0 |      0        44       0        0  same
TOTAL (25 modules)                             0       958       0        0           |      0       958       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs ukpga-1992-4.txt ssc9-*.l4` and the same with `--strict`:

```
srcrefs check: 573 src: lines, 205 runs, 216 locators, 0 problems
srcrefs check: 573 src: lines, 205 runs, 216 locators, 0 problems
```
