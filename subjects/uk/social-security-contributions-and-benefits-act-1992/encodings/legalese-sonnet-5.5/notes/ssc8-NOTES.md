# NOTES -- ssc8: Schedules 1, 2, 3, 4, 4A and 4B of the Social Security Contributions and Benefits Act 1992 (United Kingdom), 1992 c. 4

This file covers lines 4454-5066 of `ukpga-1992-4.txt` only (part agent `ssc8`; the other parts and the keel's core are not described here).
It is built from fragments by `work/build_notes.py`; the coverage table is generated from `work/cov_rows.py`, which checks that every non-blank line of the range is in exactly one row.

## What this is

- **The text is a plain-text rendering made by a converter script from legislation.gov.uk (point in time 2026-07-08). It is not the official text.**
  Nothing in this encoding is "verified against the official text".
  Quotes in the `.l4` files are copied mechanically from that rendering and checked by `srcrefs.py`.
- **Two layers.**
  Layer 1 is the law, objectively: `ssc8-sch1a.l4` (Schedule 1, paragraphs 1 to 3B), `ssc8-sch1b.l4` (paragraphs 6 to 11), `ssc8-sch2.l4`, `ssc8-sch3.l4`, `ssc8-sch4.l4`, `ssc8-sch4a.l4`, `ssc8-sch4b.l4`, each with `ssc8-tests-<name>.l4`.
  Layer 2 is the seat: `ssc8-seat.l4` and `ssc8-cases-seat.l4`.
- **Where PLAN.md and the brief differ, the brief governs.**
  The differences I found: (1) PLAN.md section 4 gives the coverage rows for Schedule 4 and the three tables of Schedule 4A as `repealed or blank in this text` with a note that the table is absent; that is one of the brief's four dispositions, so I used it for the five Schedule 4 Part headings that stand over an omitted table or dots (one row each).  The three sentences of Schedule 4A that introduce its tables ("The appropriate table for ... is as follows—") are `encoded`, not blank: each states which persons the table is for, which is a rule (`sch 4A para 2(3) which table applies`), and the bands and percentages are inputs.
  (2) PLAN.md section 5 types seam S31 (`s 44 the relevant year`, `s 44 the final relevant year`) as `Tax year` each; Schedule 4A paragraph 1 needs only how many relevant years there are (the divisor), so `sch 4A para 1 the amount referred to in section 45(2)(c)` takes `the number of relevant years` as a `NUMBER` (see Seams).
  (3) PLAN.md names the S1 answers `sch 3 pt I para <N> the contribution conditions for <the benefit> are satisfied`; the four functions are named for the paragraph and, where the paragraph is for one benefit, that benefit (see Seams).
  (4) The brief says "PLAN.md section 8" names the seams; in the PLAN I was given the seam register is section 5 (S1 at line 295, S31 at line 325), and section 4 is "The parts".
- **Paragraph labels marked with a dagger (†) are counted from position, not read from the text**, because the rendering drops every Schedule paragraph number and keeps only the headings.
  A label with no dagger is anchored by a citation in the text, which I checked line by line:
  Schedule 1 paragraphs 3, 3A and 3B ("paragraphs 3 to 3B of Schedule 1", src:256; "paragraph 3B above", src:4708), 6 (src:4605, 4609, 4683, 4685), 7 (src:4587, 4641, 4642), 7B (src:4686, 4688) and 8 ("paragraph 8(1)(m)", src:1881);
  Schedule 2 paragraph 3, because "paragraph 3(5) of this Schedule" (src:4798) lands in the third heading, "Reliefs";
  Schedule 3 Part I paragraphs 2 (src:870, 1299, 1353), 5 (src:1073, 1087, 1794 and many more), 5A (src:1251-1252, 1485, 1817) and 6 ("Schedule 3, Part I, paragraph 6", src:1754);
  Schedule 4B paragraph 1 (src:5009, 5025), paragraphs 8, 9 and 10 ("paragraphs 8 to 10", src:5026) and paragraph 13 (src:5058).
  The labels with a dagger are: Schedule 1 paragraphs 1, 2, 4, 5, 5A, 7A, 7C, 7D, 7E, 9, 10, 11; Schedule 2 paragraphs 1, 2, 4, 5, 6, 7, 8 (6 is the heading "Other provisions", src:4795; 7 and 8 are the two unheaded paragraphs at src:4798 and 4799); Schedule 3 paragraphs 1, 3, 4, 7, 8 (section 21(5A) names "4(2)(a)" and "7(4)(a)", src:759, so paragraphs 4 and 7 exist, but which lines of this text they are is counted); Schedule 4A paragraphs 1 to 9 (counted from its Parts and sub-headings; the text never cites them); Schedule 4B paragraphs 2 to 7, 11 and 12 (counted between the cited ones: counting forward from 1 reaches 8, 9 and 10 at the three headings "Amount A", "Amount A" and "Amount B", which agrees with the citation at src:5026).
  If a label with a dagger is wrong, the L4 names that carry it are wrong too; the quoted text and the line numbers are not.

## Coverage (ssc8)

Lines 4454-5066 of `ukpga-1992-4.txt`: Schedule 1 (4454), Schedule 2 (4747), Schedule 3 (4804), Schedule 4 (4901), Schedule 4A (4908), Schedule 4B (4996).
The table is generated from `work/cov_rows.py` by `work/build_notes.py`, which also checks that every non-blank line of the range is in exactly one row (it exits non-zero otherwise).
Dispositions: `encoded` (a rule, definition or table in layer-1 L4 with a test and an `@ref`), `inert (1)` not operative, `inert (2)` machinery, `inert (3)` text shown repealed or blank, `fork` (the text can be read two or more ways; the Note column names the fork-register entry), `repealed or blank in this text` (what the text shows is stated).  A † after a paragraph number marks a label counted from position (see the head).
There is no `out-of-scope` or `deferred` row.  `inert (3)` is not used: lines the text shows as dots are `repealed or blank in this text`.

### Summary

| disposition | rows |
| --- | --- |
| encoded | 133 |
| fork | 28 |
| inert (1) | 52 |
| inert (2) | 37 |
| inert (3) | 0 |
| repealed or blank in this text | 37 |
| total | 287 |

| Schedule | lines | rows | encoded | fork | inert (1) | inert (2) | repealed or blank |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Schedule 1 (4454-4746) | 293 | 122 | 51 | 10 | 15 | 32 | 14 |
| Schedule 2 (4747-4803) | 57 | 35 | 15 | 3 | 7 | 0 | 10 |
| Schedule 3 (4804-4900) | 97 | 42 | 19 | 8 | 8 | 3 | 4 |
| Schedule 4 (4901-4907) | 7 | 6 | 0 | 0 | 1 | 0 | 5 |
| Schedule 4A (4908-4995) | 88 | 49 | 31 | 4 | 10 | 2 | 2 |
| Schedule 4B (4996-5066) | 71 | 33 | 17 | 3 | 11 | 0 | 2 |

### Audit

- Non-blank lines in 4454-5066: 613 (the range has no blank lines: 613 lines in all).
- Text units counted independently by `count_units` in `work/build_notes.py`: 313 = 62 headings + 186 numbered sub-paragraphs + 46 unnumbered paragraphs + 10 defined terms + 9 lines of dots (lettered limbs are counted with their parent).
- Rows in the table: 287; rows grouping two or more units are expected (for example a sub-paragraph and its limbs share a row), so the row count is not the unit count; what is checked is that no line is outside a row and no line is in two.
- Rows before and after the audit pass: 281 and 287.  The audit pass found no uncovered line and no line in two rows (an earlier ad hoc check of the first 281 rows had found the same).  It did find one row that hid four repealed limbs, shown as dots, inside a longer inert (2) row: the row for Schedule 1 paragraph 8(1)(a)-(q) was split into seven so that lines 4717, 4719-4720 and 4729 are `repealed or blank in this text` rows of their own.

### Table

| Lines | Unit | Disposition | L4 name or reason | Note |
| --- | --- | --- | --- | --- |
| 4454 | Sch 1 title | inert (1) | title of the Schedule |  |
| 4455 | Sch 1 para 1† heading | inert (1) | heading |  |
| 4456-4459 | Sch 1 para 1† (1) | encoded | `sch 1 para 1(1)(a) the single payment of earnings in respect of employments under the same employer`, `sch 1 para 1(1)(b) ...paid by different persons...` | the closing power to substitute a prescribed period for a week is taken as the input `regulations provide otherwise` / `the circumstances are prescribed` |
| 4460-4464 | Sch 1 para 1† (2)-(6) | repealed or blank in this text | five lines of dots (4460, 4461, 4462, 4463, 4464) | text shown repealed or blank |
| 4465 | Sch 1 para 1† (7) | fork | `sch 1 para 1(7) the separate payments of earnings by the employers` | F-S1-1 |
| 4466 | Sch 1 para 1† (8) | fork | `sch 1 para 1(8) the secondary contributors' shares of the liability` | F-S1-1 |
| 4467 | Sch 1 para 1† (8A) | inert (2) | regulation-making authority (the Inland Revenue) |  |
| 4468-4470 | Sch 1 para 1† (9)-(11) | repealed or blank in this text | three lines of dots (4468, 4469, 4470) | text shown repealed or blank |
| 4471 | Sch 1 para 2† heading | inert (1) | heading |  |
| 4472 | Sch 1 para 2† | inert (2) | power to make regulations on the intervals at which payments of earnings are treated as made |  |
| 4473 | Sch 1 para 3 heading | inert (1) | heading |  |
| 4474 | Sch 1 para 3(1) | fork | `sch 1 para 3(1) the primary contribution that the secondary contributor is liable in the first instance to pay`, `... the earner is liable in the first instance ...`, `... the contributions are taken to be paid by the earner`, regulative twin `sch 1 para 3(1) the secondary contributor's duty to pay the earner's primary contribution` | F-S1-6 |
| 4475 | Sch 1 para 3(2) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4476 | Sch 1 para 3(3) | encoded | `sch 1 para 3(3) the amount the secondary contributor is entitled to recover from the earner`, `sch 1 para 3(3) the recovery is by deduction from the earner's earnings` |  |
| 4477-4478 | Sch 1 para 3(3A), (3B) | encoded | `sch 1 para 3(3B) the amount the employer may recover from the employee` |  |
| 4479-4481 | Sch 1 para 3(4) | encoded | `sch 1 para 3(4) sub-paragraph (5) applies` |  |
| 4482-4483 | Sch 1 para 3(5), (5)(a) | encoded | `sch 1 para 3(5) the amount the employer may recover from the employee` |  |
| 4484 | Sch 1 para 3(5)(b) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4485 | Sch 1 para 3(6) | inert (2) | regulation-making authority (the Inland Revenue) |  |
| 4486 | Sch 1 para 3A heading | inert (1) | heading |  |
| 4487-4490 | Sch 1 para 3A(1) | encoded | `sch 1 para 3A(1) the person liable is prohibited from the act`; regulative twins `sch 1 para 3A(1) the prohibition on deducting` / `...otherwise recovering` / `...agreeing` |  |
| 4491-4494 | Sch 1 para 3A(2) | fork | `sch 1 para 3A(2) the amount of the secondary Class 1 contribution that may be recovered under the agreement` | F-S1-9 |
| 4495-4497 | Sch 1 para 3A(2A) | encoded | same function (input `the part of the amount that relates to matters within sub-paragraph (2A)`) |  |
| 4498-4501 | Sch 1 para 3A(2B) | encoded | `sch 1 para 3A(2B) the amount is relevant employment income` |  |
| 4502-4504 | Sch 1 para 3A(3) | encoded | same function as (2): the two dates |  |
| 4505-4506 | Sch 1 para 3A(4) "agreement" | encoded | `sch 1 para 3A(4) the thing is an agreement` |  |
| 4507 | Sch 1 para 3A(4) "relevant earner" | encoded | `sch 1 para 3A(4) the earner is a relevant earner` |  |
| 4508 | Sch 1 para 3B heading | inert (1) | heading |  |
| 4509-4516 | Sch 1 para 3B(1) | encoded | `sch 1 para 3B(1) this paragraph applies to the election` |  |
| 4517-4521 | Sch 1 para 3B(1A) | encoded | `sch 1 para 3B(1A) the amount is relevant employment income` |  |
| 4522-4525 | Sch 1 para 3B(2) | encoded | `sch 1 para 3B(2) the liability is treated as falling on the earner` |  |
| 4526-4529 | Sch 1 para 3B(3) | fork | `sch 1 para 3B(3) the election is in force on the day` | F-S1-3 |
| 4530-4532 | Sch 1 para 3B(4) | encoded | `sch 1 para 3B(4) the approval covers the election` |  |
| 4533-4535 | Sch 1 para 3B(5) | encoded | `sch 1 para 3B(5) the Inland Revenue is entitled to refuse the approval` |  |
| 4536-4539 | Sch 1 para 3B(6) | encoded | `sch 1 para 3B(6) the Inland Revenue may withdraw the approval by notice` | marginal reading (a) |
| 4540-4544 | Sch 1 para 3B(7) | encoded | `sch 1 para 3B(7) the election has no effect on the contributions on the income` | marginal reading (a) |
| 4545-4547 | Sch 1 para 3B(7A) | fork | `sch 1 para 3B(7A) the withdrawal date` | F-S1-4 |
| 4548-4550 | Sch 1 para 3B(7B) | encoded | `sch 1 para 3B(7B) the part of the transferred liability for which the election is void` |  |
| 4551 | Sch 1 para 3B(8) | encoded | `sch 1 para 3B(8) the person may appeal against the Inland Revenue's decision` |  |
| 4552-4555 | Sch 1 para 3B(9) | encoded | `sch 1 para 3B(9) the tribunal may take the course` |  |
| 4556 | Sch 1 para 3B(10) | encoded | `sch 1 para 3B(10) the election applies to the contributions in respect of the income` |  |
| 4557-4560 | Sch 1 para 3B(11) | inert (2) | power of the Inland Revenue to make regulations on elections and approvals |  |
| 4561-4564 | Sch 1 para 3B(12) | fork | `sch 1 para 3B(12) the liabilities are deemed to have fallen on the earner`, `... the reimbursement the secondary contributor is entitled to from the earner` | F-S1-8 |
| 4565 | Sch 1 para 3B(13) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4566 | Sch 1 para 3B(14) | encoded | `sch 1 para 3B(14) the tribunal is` |  |
| 4567 | Sch 1 para 4† heading | inert (1) | heading |  |
| 4568-4572 | Sch 1 para 4† | inert (2) | power of the Inland Revenue to make regulations on Class 1 contributions (a) to (d) |  |
| 4573 | Sch 1 para 5† heading | inert (1) | heading |  |
| 4574-4576 | Sch 1 para 5† | inert (2) | power of the Inland Revenue to make regulations on Class 1A contributions |  |
| 4577 | Sch 1 para 5A† heading | inert (1) | heading |  |
| 4578 | Sch 1 para 5A† | inert (2) | power of the Inland Revenue to make regulations on Class 1B contributions |  |
| 4579 | Sch 1 para 6 heading | inert (1) | heading |  |
| 4580-4583 | Sch 1 para 6(1) | inert (2) | power of the Inland Revenue to make regulations combining collection with tax |  |
| 4584-4587 | Sch 1 para 6(2)(a)-(c) | inert (2) | what the regulations may in particular provide |  |
| 4588 | Sch 1 para 6(2), closing words | encoded | `sch 1 para 6(2) the reference in sub-paragraph (1)(b) or (c) includes the thing` |  |
| 4589 | Sch 1 para 6(3) | encoded | `sch 1 para 6(3) the rate of interest` | the rate is an input |
| 4590-4593 | Sch 1 para 6(4) | encoded | `sch 1 para 6(4) regulations under sub-paragraph (1) may require the interest to be paid` |  |
| 4594 | Sch 1 para 6(4A) | encoded | `sch 1 para 6(4A) regulations under sub-paragraph (1) may require interest on the Class 1B sum to be paid` |  |
| 4595 | Sch 1 para 6(4B) | encoded | `sch 1 para 6(4B) a deduction of income tax is made from the interest`, `... the interest is taken into account in computing income, profits or losses for tax purposes` |  |
| 4596 | Sch 1 para 6(4C) | encoded | `sch 1 para 6(4C) the interest is taken into account in computing income, profits or losses for tax purposes` |  |
| 4597 | Sch 1 para 6(5) | inert (2) | power of the Secretary of State to make regulations |  |
| 4598-4601 | Sch 1 para 6(6) | inert (2) | what regulations under (5) may require |  |
| 4602 | Sch 1 para 6(7) | inert (2) | application of section 98 of the Taxes Management Act 1970 to regulations |  |
| 4603 | Sch 1 para 6(8) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4604 | Sch 1 para 7 heading | inert (1) | heading |  |
| 4605-4608 | Sch 1 para 7(1) | encoded | `sch 1 para 7(1) this paragraph applies` |  |
| 4609-4611 | Sch 1 para 7(2) | encoded | `sch 1 para 7(2) section 98A of the Taxes Management Act 1970 applies to the contributions return as to the tax return` |  |
| 4612 | Sch 1 para 7(3) | encoded | `sch 1 para 7(3) the person may also be required to pay a penalty under paragraph (a) for the associated contributions return` |  |
| 4613-4616 | Sch 1 para 7(4) | encoded | `sch 1 para 7(4) the single penalty that may be imposed` |  |
| 4617-4619 | Sch 1 para 7(5) | encoded | `sch 1 para 7(5) the limit of the single penalty` |  |
| 4620-4622 | Sch 1 para 7(6), T and C | encoded | `sch 1 para 7(6) the part apportioned to income tax`, `... to contributions` |  |
| 4623 | Sch 1 para 7(7) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4624 | Sch 1 para 7(8) | encoded | `sch 1 para 7(8) sub-paragraph (6) has effect` |  |
| 4625 | Sch 1 para 7(9) | encoded | `sch 1 para 7(9) the tax year corresponding to the year of assessment` |  |
| 4626-4628 | Sch 1 para 7(10) | encoded | `sch 1 para 7(10) what is omitted in applying the subsection` |  |
| 4629-4632 | Sch 1 para 7(11) | encoded | `sch 1 para 7(11)(a) ...`, `(b) ...`, `(c) ...` |  |
| 4633-4635 | Sch 1 para 7(12) | encoded | `sch 1 para 7(12) a penalty under section 98A may be imposed` |  |
| 4636-4640 | Sch 1 para 7(13) | encoded | `sch 1 para 7(13) the contributions return and the tax return are associated` | (13)(a) is the pointer to (1) |
| 4641 | Sch 1 para 7A† (1) | encoded | `sch 1 para 7A(1) this paragraph applies` |  |
| 4642-4644 | Sch 1 para 7A† (2) | inert (2) | power of the Treasury to make regulations on penalties for fraud or negligence |  |
| 4645 | Sch 1 para 7A† (3), lead-in | encoded | quoted with (b): `sch 1 para 7A(3)(b) the penalty may be imposed by the Inland Revenue on the day` |  |
| 4646 | Sch 1 para 7A† (3)(a) | inert (2) | what the regulations must prescribe (the rates) |  |
| 4647 | Sch 1 para 7A† (3)(b) | fork | `sch 1 para 7A(3)(b) the penalty may be imposed by the Inland Revenue on the day` | F-S1-7 |
| 4648-4650 | Sch 1 para 7A† (3)(c)-(e) | inert (2) | what the regulations must provide (the date a penalty is incurred, enforcement, mitigation) |  |
| 4651 | Sch 1 para 7B heading | inert (1) | heading |  |
| 4652 | Sch 1 para 7B(1) | inert (2) | power of the Treasury to make regulations on payment otherwise than through PAYE |  |
| 4653-4666 | Sch 1 para 7B(2)(a)-(i) | inert (2) | what the regulations may in particular provide |  |
| 4667-4670 | Sch 1 para 7B(3) | encoded | `sch 1 para 7B(3) regulations under sub-paragraph (2)(e) may require the interest to be paid` |  |
| 4671 | Sch 1 para 7B(4) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4672 | Sch 1 para 7B(5), lead-in | encoded | quoted with (b): `sch 1 para 7B(5)(b) the penalty may be imposed by the Inland Revenue on the day` |  |
| 4673 | Sch 1 para 7B(5)(a) | inert (2) | what the regulations must prescribe (the rates) |  |
| 4674-4676 | Sch 1 para 7B(5)(b) | fork | `sch 1 para 7B(5)(b) the penalty may be imposed by the Inland Revenue on the day` | F-S1-7 |
| 4677-4679 | Sch 1 para 7B(5)(c)-(e) | inert (2) | what the regulations must provide (the date a penalty is incurred, enforcement, mitigation) |  |
| 4680 | Sch 1 para 7B(5A) | inert (2) | power to apply Part X of the Taxes Management Act 1970 |  |
| 4681-4682 | Sch 1 para 7B(6), (7) | repealed or blank in this text | two lines of dots (4681, 4682) | text shown repealed or blank |
| 4683 | Sch 1 para 7B(8) | encoded | `sch 1 para 7B(8) the interest or penalties that may be charged for the earlier period` |  |
| 4684 | Sch 1 para 7B(9) | encoded | `sch 1 para 7B(9) the reference to contributions in sub-paragraph (1) includes the thing` |  |
| 4685 | Sch 1 para 7B(10) | encoded | `sch 1 para 7B(10) the rate of interest` | the rate is an input |
| 4686-4687 | Sch 1 para 7C† (1), (2) | inert (2) | power of the Inland Revenue to make regulations on recovery |  |
| 4688 | Sch 1 para 7C† (3) | encoded | `sch 1 para 7C(3) the reference to contributions in this paragraph includes the thing` |  |
| 4689 | Sch 1 para 7D† | inert (2) | power of the Inland Revenue to make regulations on set-off |  |
| 4690-4692 | Sch 1 para 7E† (1) | inert (2) | power to make regulations on payment of Class 2 contributions for maternity allowance |  |
| 4693-4695 | Sch 1 para 7E† (2), (a), (b) | inert (2) | what the regulations may provide |  |
| 4696 | Sch 1 para 7E† (2)(b)(i) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4697-4698 | Sch 1 para 7E† (2)(b)(ii), (3) | inert (2) | what the regulations may provide; the authority that makes them |  |
| 4699 | Sch 1 para 8 heading | inert (1) | heading |  |
| 4700-4716 | Sch 1 para 8(1)(a)-(h) | inert (2) | general powers to make regulations (records, treating payments, repayment) |  |
| 4717 | Sch 1 para 8(1)(i) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4718 | Sch 1 para 8(1)(ia) | inert (2) | general power to make regulations (repayment of Class 1A or 1B) |  |
| 4719-4720 | Sch 1 para 8(1)(j), (k) | repealed or blank in this text | two lines of dots | text shown repealed or blank |
| 4721-4728 | Sch 1 para 8(1)(l)-(o) | inert (2) | general powers to make regulations (treating payments as other classes, return of contributions paid in error, treating persons as employed earners) |  |
| 4729 | Sch 1 para 8(1)(p) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4730 | Sch 1 para 8(1)(q) | inert (2) | general power to make regulations (incidental matters) |  |
| 4731-4734 | Sch 1 para 8(1A) | inert (2) | who the appropriate authority is for the regulations |  |
| 4735-4736 | Sch 1 para 8(2), (3) | repealed or blank in this text | two lines of dots (4735, 4736) | text shown repealed or blank |
| 4737-4740 | Sch 1 para 9† | inert (2) | power of the Treasury to make regulations on the age a person is treated as having attained in a week |  |
| 4741 | Sch 1 para 10† heading | inert (1) | heading |  |
| 4742 | Sch 1 para 10† (1) | fork | `sch 1 para 10(1) the Secretary of State may pay the contributions and deduct the amount from the pension or allowance`, `... the pension or allowance left after the deduction`, regulative twin `sch 1 para 10(1) the Secretary of State's permission to pay and deduct` | F-S1-5 |
| 4743 | Sch 1 para 10† (2) | encoded | `sch 1 para 10(2) sub-paragraph (1) has effect despite the instrument` |  |
| 4744 | Sch 1 para 11† heading | inert (1) | heading |  |
| 4745 | Sch 1 para 11† (1) | inert (2) | power of the Treasury to make regulations on sickness payments |  |
| 4746 | Sch 1 para 11† (2) | encoded | `sch 1 para 11(2) the amendments may be made notwithstanding the society's rules` |  |
| 4747 | Sch 2 title | inert (1) | title of the Schedule |  |
| 4748 | Sch 2 para 1† heading | inert (1) | heading |  |
| 4749-4752 | Sch 2 para 1†, lead-in and (a), (ab), (ac) | encoded | `sch 2 para 1 the meaning of the term` |  |
| 4753 | Sch 2 para 1† (b) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4754 | Sch 2 para 1† (c) "year" | encoded | `sch 2 para 1 the meaning of the term` |  |
| 4755 | Sch 2 para 2† heading | inert (1) | heading |  |
| 4756-4758 | Sch 2 para 2† | encoded | `sch 2 para 2 the profit is one in respect of which Class 4 contributions are payable`, `sch 2 para 2 the full amount of the profits ...` |  |
| 4759 | Sch 2 para 3 heading | inert (1) | heading |  |
| 4760-4761 | Sch 2 para 3(1), (a) | encoded | `sch 2 para 3(1) relief is available under the provision` |  |
| 4762 | Sch 2 para 3(1)(b) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4763-4764 | Sch 2 para 3(1)(c), (d) | encoded | `sch 2 para 3(1) relief is available under the provision` |  |
| 4765-4767 | Sch 2 para 3(2), (a), (b) | encoded | `sch 2 para 3(2) the relief provision does not apply` |  |
| 4768 | Sch 2 para 3(2)(c) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4769 | Sch 2 para 3(2)(d) | encoded | `sch 2 para 3(2) the relief provision does not apply` |  |
| 4770 | Sch 2 para 3(2)(e) | repealed or blank in this text | line of dots followed by an editorial omission | text shown repealed or blank |
| 4771-4772 | Sch 2 para 3(2)(f), (g) | encoded | `sch 2 para 3(2) the relief provision does not apply` |  |
| 4773 | Sch 2 para 3(3) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4774-4776 | Sch 2 para 3(4) | fork | `sch 2 para 3(4) the profits for each year after the loss is deducted`, `sch 2 para 3(4) the excess still to be deducted after the last year given` | F-S2-1 |
| 4777 | Sch 2 para 3(5), lead-in | fork | `sch 2 para 3(5) the amount of the payment for which relief is allowed` | F-S2-1 |
| 4778 | Sch 2 para 3(5)(a) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4779-4786 | Sch 2 para 3(5)(b)-(e) and the closing words | fork | `sch 2 para 3(5) the amount of the payment for which relief is allowed`, `... the profits for each year after the payments are deducted`, `... the payments still to be deducted after the last year given` | F-S2-1 |
| 4787 | Sch 2 para 4† heading | inert (1) | heading |  |
| 4788 | Sch 2 para 4† (1) | encoded | `sch 2 para 4(1) the profits in respect of which the partner's liability arises` |  |
| 4789 | Sch 2 para 4† (2) | encoded | `sch 2 para 4(2) the contributions are charged on the partner separately` |  |
| 4790 | Sch 2 para 5† heading | inert (1) | heading |  |
| 4791 | Sch 2 para 5†, lead-in | encoded | `sch 2 para 5 Class 4 contributions are payable on the profits received as trustee` |  |
| 4792 | Sch 2 para 5† (a) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4793-4794 | Sch 2 para 5† (b) and the closing words | encoded | `sch 2 para 5 Class 4 contributions are payable on the profits received as trustee` |  |
| 4795 | Sch 2 para 6† heading | inert (1) | heading |  |
| 4796 | Sch 2 para 6† (1) | encoded | `sch 2 para 6(1) section 101 of the Finance Act 2009 applies to the sum`, `... section 102 ...` |  |
| 4797 | Sch 2 para 6† (2) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4798 | Sch 2 para 7† | encoded | `sch 2 para 7 the assessment is final and conclusive for computing Class 4 liability`, `sch 2 para 7 the allowance or adjustment may be taken into account in computing the profits` |  |
| 4799-4801 | Sch 2 para 8† | encoded | `sch 2 para 8 Part V of the Taxes Management Act 1970 applies to the matter` |  |
| 4802 | Sch 2, editorial omission after para 8† | repealed or blank in this text | a line reading `...` (an editorial omission) | text shown repealed or blank |
| 4803 | Sch 2, paragraph after 8† | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4804 | Sch 3 title | inert (1) | title of the Schedule |  |
| 4805 | Sch 3 Part I heading | inert (1) | heading |  |
| 4806 | Sch 3 Part I para 1† heading (Unemployment benefit) | inert (1) | heading |  |
| 4807 | Sch 3 Part I para 1† | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4808 | Sch 3 Part I para 2 heading | inert (1) | heading |  |
| 4809 | Sch 3 Part I para 2(1) | encoded | `sch 3 pt I para 2 the contribution conditions for short-term incapacity benefit are satisfied` (the seam S1 answer) |  |
| 4810-4812 | Sch 3 Part I para 2(2) | fork | `sch 3 pt I para 2(2) the first condition is satisfied` | F-S3-1, F-S3-2 |
| 4813-4815 | Sch 3 Part I para 2(3) | fork | `sch 3 pt I para 2(3) the second condition is satisfied` | F-S3-2 |
| 4816-4820 | Sch 3 Part I para 2(4) | fork | `sch 3 pt I para 2(4) the earnings factor for the first condition` | F-S3-5 |
| 4821-4825 | Sch 3 Part I para 2(5) | fork | `sch 3 pt I para 2(5) the earnings factor for the second condition` | F-S3-5 |
| 4826-4827 | Sch 3 Part I para 2(6), (a) | encoded | `sch 3 pt I para 2(6)(a) the relevant time` |  |
| 4828 | Sch 3 Part I para 2(6)(b) | fork | `sch 3 pt I para 2(6)(b) the calendar year in which the relevant benefit year begins` | F-S3-4 |
| 4829 | Sch 3 Part I para 2(7) | encoded | `sch 3 pt I para 2(7) the previous claim is disregarded` | marginal reading (b) |
| 4830-4832 | Sch 3 Part I para 2(8) | inert (2) | power to make regulations (the effect is the input `regulations ... first condition` of para 2(2)) |  |
| 4833-4836 | Sch 3 Part I para 2(9) "benefit" | encoded | `sch 3 pt I para 2(9) the thing is a benefit for sub-paragraph (8)` |  |
| 4837 | Sch 3 Part I para 2(9) "modifications" | encoded | `sch 3 pt I para 2(9) the change is a modification` |  |
| 4838 | Sch 3 Part I para 3† heading (Maternity allowance) | inert (1) | heading |  |
| 4839-4841 | Sch 3 Part I paras 3†, 4† | repealed or blank in this text | two lines of dots (4839, 4841) either side of a line reading `...` (4840) | text shown repealed or blank |
| 4842 | Sch 3 Part I para 5 heading | inert (1) | heading |  |
| 4843-4846 | Sch 3 Part I para 5(1) | encoded | `sch 3 pt I para 5(1) this paragraph sets out the contribution conditions for the benefit` |  |
| 4847-4848 | Sch 3 Part I para 5(2), (a) | encoded | `sch 3 pt I para 5(2) contributions of a relevant class were actually paid and the earnings factor reaches the qualifying earnings factor` |  |
| 4849-4852 | Sch 3 Part I para 5(2)(b) | fork | `sch 3 pt I para 5(2)(b) the earnings factor for the first condition` | F-S3-5 |
| 4853-4855 | Sch 3 Part I para 5(3) | encoded | `sch 3 pt I para 5(3) the second condition is satisfied` |  |
| 4856-4860 | Sch 3 Part I para 5(4) | fork | `sch 3 pt I para 5(4) the earnings factor for the second condition` | F-S3-5 |
| 4861 | Sch 3 Part I para 5(5) | encoded | `sch 3 pt I para 5(5) the year is a relevant year` | the table of requisite numbers of years is omitted from the text: an input |
| 4862-4864 | Sch 3 Part I para 5(6) | encoded | `sch 3 pt I para 5(6) the first condition is taken to be satisfied` |  |
| 4865-4867 | Sch 3 Part I para 5(6A) | encoded | `sch 3 pt I para 5(6A) the first condition is taken to be satisfied` |  |
| 4868 | Sch 3 Part I para 5(6B) | encoded | `sch 3 pt I para 5(6B) the allowance is main phase employment and support allowance` |  |
| 4869-4872 | Sch 3 Part I para 5(7) | fork | `sch 3 pt I para 5(7) the second condition is taken to be satisfied` | F-S3-3 |
| 4873 | Sch 3 Part I para 5(7A) | inert (2) | power to make regulations (the effect is the input `precluded from regular employment` of para 5(7)) |  |
| 4874-4876 | Sch 3 Part I para 5(8) | encoded | `sch 3 pt I para 5(8) the year is in the contributor's working life` |  |
| 4877-4879 | Sch 3 Part I para 5A(1) | encoded | `sch 3 pt I para 5A(1) this paragraph applies to the benefit` | marginal reading (a) |
| 4880-4882 | Sch 3 Part I para 5A(2) | encoded | `sch 3 pt I para 5A(2) the contribution condition is satisfied` |  |
| 4883-4887 | Sch 3 Part I para 5A(3) | encoded | `sch 3 pt I para 5A(3) the earnings factor` |  |
| 4888-4891 | Sch 3 Part I para 5A(4) | inert (2) | power to make regulations (the effect is an input of para 5A(2)) |  |
| 4892 | Sch 3 Part I para 6 heading | inert (1) | heading |  |
| 4893-4895 | Sch 3 Part I para 6(1) | encoded | `sch 3 pt I para 6 the contribution conditions for a child's special allowance are satisfied` |  |
| 4896 | Sch 3 Part I para 6(2) | encoded | `sch 3 pt I para 6(2) the year is a relevant year` |  |
| 4897 | Sch 3 Part II heading | inert (1) | heading |  |
| 4898 | Sch 3 Part II paras 7† | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4899 | Sch 3 Part II para 8† | encoded | `sch 3 pt II para 8 the first contribution condition is taken to be satisfied` |  |
| 4900 | Sch 3 Part II after para 8† | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4901 | Sch 4 title | inert (1) | title of the Schedule |  |
| 4902 | Sch 4 Part I heading | repealed or blank in this text | the table of rates is absent from this text; heading only | the rates are inputs; the seam S2 answers are `sch 4 pt I para 2 the lower rate of short-term incapacity benefit in pounds` and `... the higher rate ...` (in ssc8-sch4.l4) |
| 4903-4904 | Sch 4 Part II | repealed or blank in this text | heading, then a line of dots | text shown repealed or blank |
| 4905 | Sch 4 Part III heading | repealed or blank in this text | the table of rates is absent from this text; heading only | the rates are inputs |
| 4906 | Sch 4 Part IV heading | repealed or blank in this text | the table of rates is absent from this text; heading only | the rates are inputs |
| 4907 | Sch 4 Part V heading | repealed or blank in this text | the table of rates is absent from this text; heading only | the rates are inputs; the seam S34 answers are `sch 4 pt V para 5 the increase of the disablement pension in pounds` and `sch 4 pt V para 6 the increase of the unemployability supplement in pounds` (in ssc8-sch4.l4) |
| 4908 | Sch 4A title | inert (1) | title of the Schedule |  |
| 4909 | Sch 4A Part I heading | inert (1) | heading |  |
| 4910-4914 | Sch 4A para 1† (1) | encoded | `sch 4A para 1 the amount referred to in section 45(2)(c)` |  |
| 4915 | Sch 4A para 1† (2) | encoded | `sch 4A para 1(2) the divisor for the amount` |  |
| 4916 | Sch 4A para 1† (3) | encoded | `sch 4A para 1(3) the first alternative number` |  |
| 4917-4919 | Sch 4A para 1† (4) | encoded | `sch 4A para 1(4) the second alternative number` |  |
| 4920 | Sch 4A para 1† (5) | encoded | `sch 4A para 1(5) the divisor for the amount` |  |
| 4921 | Sch 4A para 1† (6) | encoded | `sch 4A para 1(6) the first alternative number` |  |
| 4922-4924 | Sch 4A para 1† (7) | encoded | `sch 4A para 1(7) the second alternative number` |  |
| 4925 | Sch 4A para 1† (8) | encoded | the number of relevant years is an input of `sch 4A para 1 the amount referred to in section 45(2)(c)` (section 44's answer) |  |
| 4926 | Sch 4A Part II heading | inert (1) | heading |  |
| 4927 | Sch 4A para 2† (1) | encoded | `sch 4A para 2(1) Part II applies to the tax year` | marginal reading (a) |
| 4928-4932 | Sch 4A para 2† (2) | fork | `sch 4A para 2(2)(a) the part of the surplus in the band`, `sch 4A para 2(2) the amount for the year found band by band`, `sch 4A para 2 the amount for the year` | F-S4B-1 |
| 4933-4935 | Sch 4A para 2† (3), (4), (4A) (the three tables are omitted) | encoded | `sch 4A para 2(3) which table applies`; the bands and percentages are inputs | the tables are omitted from this text |
| 4936 | Sch 4A para 2† (5) | inert (2) | power to make regulations |  |
| 4937-4938 | Sch 4A para 2† (6), (a) | encoded | `sch 4A para 2(6)(a) the value of N` |  |
| 4939 | Sch 4A para 2† (6)(b) | encoded | `sch 4A para 2(6)(b) LET` |  |
| 4940 | Sch 4A para 2† (6)(c) | encoded | `sch 4A para 2(6)(c) QEF` |  |
| 4941 | Sch 4A para 2† (6)(d) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4942 | Sch 4A para 2† (7) | encoded | `sch 4A para 2(7) 2QEF` |  |
| 4943 | Sch 4A para 2† (8) | encoded | `sch 4A para 2(8) the final relevant year` |  |
| 4944-4945 | Sch 4A Part III heading and "Introduction" heading | inert (1) | headings |  |
| 4946 | Sch 4A para 3† (1) | encoded | `sch 4A para 3(1) Part III applies to the tax year` | marginal reading (a) |
| 4947 | Sch 4A para 3† (2) | encoded | the condition is the input of `sch 4A para 3(1) Part III applies to the tax year` (the weeks in which it is satisfied) |  |
| 4948 | Sch 4A para 3† (3) | encoded | `sch 4A para 3(3) Part II does not apply because of the condition` | JUST TRUE when the condition holds in one or more weeks; JUST FALSE in none (marginal reading (a)) |
| 4949 | Sch 4A para 4† heading (The amount) | inert (1) | heading |  |
| 4950-4952 | Sch 4A para 4† | encoded | `sch 4A para 4 amount C`, `sch 4A para 4 the difference` |  |
| 4953 | Sch 4A para 5† heading (Amount A) | inert (1) | heading |  |
| 4954 | Sch 4A para 5† (1) | encoded | `sch 4A para 5 amount A` |  |
| 4955-4959 | Sch 4A para 5† (2) | fork | `sch 4A para 5 amount A` | F-S4B-1 |
| 4960-4962 | Sch 4A para 5† (3), (4), (4A) (the three tables are omitted) | encoded | `sch 4A para 2(3) which table applies` (the same test); bands and percentages are inputs | the tables are omitted from this text |
| 4963 | Sch 4A para 6† heading (Amount B, first case) | inert (1) | heading |  |
| 4964 | Sch 4A para 6† (1) | encoded | `sch 4A kind of contracted-out employment` and `sch 4A para 4 amount C` |  |
| 4965-4967 | Sch 4A para 6† (2) | fork | `sch 4A para 6 amount B in the first case` | F-S4B-1 |
| 4968-4970 | Sch 4A para 6† (3) | encoded | `sch 4A para 6 amount B in the first case` (20 + N before 6 April 2009; 20 on or after) |  |
| 4971 | Sch 4A para 7† heading (Amount B, second case) | inert (1) | heading |  |
| 4972 | Sch 4A para 7† (1) | encoded | `sch 4A kind of contracted-out employment` and `sch 4A para 4 amount C` |  |
| 4973-4977 | Sch 4A para 7† (2) | fork | `sch 4A para 7 amount B in the second case` | F-S4B-1 |
| 4978-4980 | Sch 4A para 7† (3), (4), (4A) (the three tables are omitted) | encoded | `sch 4A para 2(3) which table applies` (the same test); bands and percentages are inputs | the tables are omitted from this text |
| 4981 | Sch 4A para 8† heading (Interpretation) | inert (1) | heading |  |
| 4982 | Sch 4A para 8† (1) | encoded | `sch 4A kind of contracted-out employment` (the three schemes are the Pension Schemes Act 1993's: a fact asked of the person) |  |
| 4983 | Sch 4A para 8† (2) | encoded | `sch 4A para 8(2) there is an assumed surplus in the pensioner's earnings factor for the year` |  |
| 4984 | Sch 4A para 8† (3) | encoded | `sch 4A para 8(3) section 44A is ignored in applying section 44(6)` |  |
| 4985-4988 | Sch 4A para 8† (4), (a), (b), (c) | encoded | `sch 4A para 2(6)(a) the value of N`, `(b) LET`, `(c) QEF` (the same functions) |  |
| 4989 | Sch 4A para 8† (4)(d) | repealed or blank in this text | line of dots | text shown repealed or blank |
| 4990 | Sch 4A para 8† (5) | encoded | `sch 4A para 2(7) 2QEF` (the same function) |  |
| 4991 | Sch 4A para 8† (6) | encoded | `sch 4A para 2(8) the final relevant year` (the same function) |  |
| 4992 | Sch 4A Part IV heading | inert (1) | heading |  |
| 4993-4995 | Sch 4A para 9† (Part IV) | inert (2) | power of the Secretary of State to make regulations |  |
| 4996 | Sch 4B title | inert (1) | title of the Schedule |  |
| 4997 | Sch 4B Part 1 heading | inert (1) | heading |  |
| 4998-5001 | Sch 4B para 1(1) | encoded | `sch 4B para 1 the amount referred to in section 45(2)(d)` |  |
| 5002 | Sch 4B para 1(2) | encoded | `sch 4B para 1 the amount referred to in section 45(2)(d)` (nil when the total is negative) |  |
| 5003-5004 | Sch 4B Part 2 heading and "Application" heading | inert (1) | headings |  |
| 5005-5007 | Sch 4B para 2† | encoded | `sch 4B para 2 Part 2 applies to the relevant year` | marginal reading (a) |
| 5008 | Sch 4B para 3† heading | inert (1) | heading |  |
| 5009-5011 | Sch 4B para 3† | encoded | `sch 4B para 3 the appropriate amount for the year under Part 2` |  |
| 5012-5013 | Sch 4B para 4† | encoded | `sch 4B para 4 the flat rate amount` |  |
| 5014-5018 | Sch 4B para 5† | fork | `sch 4B para 5 the earnings-related amount` | F-S4B-1 |
| 5019-5020 | Sch 4B Part 3 heading and "Application" heading | inert (1) | headings |  |
| 5021-5023 | Sch 4B para 6† | encoded | `sch 4B para 6 Part 3 applies to the relevant year` | marginal reading (a) |
| 5024 | Sch 4B para 7† heading | inert (1) | heading |  |
| 5025-5027 | Sch 4B para 7† | encoded | `sch 4B para 7 the appropriate amount for the year under Part 3` |  |
| 5028 | Sch 4B para 8 heading | inert (1) | heading |  |
| 5029-5032 | Sch 4B para 8 | encoded | `sch 4B para 8 amount A where the assumed earnings factor does not exceed the LET` |  |
| 5033 | Sch 4B para 9 heading | inert (1) | heading |  |
| 5034-5042 | Sch 4B para 9 | fork | `sch 4B para 9 amount A where the assumed earnings factor exceeds the LET` | F-S4B-1 |
| 5043 | Sch 4B para 10 heading | inert (1) | heading |  |
| 5044-5048 | Sch 4B para 10(1) | fork | `sch 4B para 10 amount B` | F-S4B-1 |
| 5049 | Sch 4B para 10(2) | encoded | `sch 4B para 10(2) section 44B is ignored in applying section 44(6)` |  |
| 5050 | Sch 4B Part 4 heading | inert (1) | heading |  |
| 5051-5053 | Sch 4B para 11† | encoded | `sch 4B para 11 which Part governs the year` and `sch 4B para 3 the appropriate amount for the year` | the regulation-making power is machinery: the case it leaves to regulations answers NOTHING |
| 5054-5055 | Sch 4B Part 5 heading and lead-in | inert (1) | heading and introductory words |  |
| 5056 | Sch 4B para 12†, first definition | repealed or blank in this text | line of dots | text shown repealed or blank |
| 5057 | Sch 4B para 12† "the contracted-out condition" | encoded | `sch 4B para 12 the contracted-out condition is satisfied for the tax week` |  |
| 5058 | Sch 4B para 12† "the FRAA" | encoded | `sch 4B para 13 the flat rate accrual amount` |  |
| 5059 | Sch 4B para 12† "the LET" | encoded | `sch 4B para 12 the LET for the year` |  |
| 5060 | Sch 4B para 12† "the QEF" | encoded | `sch 4B para 12 the QEF for the year` |  |
| 5061 | Sch 4B para 12† "the pensioner's assumed earnings factor" | encoded | `sch 4B para 12 the pensioner's assumed earnings factor for the year` |  |
| 5062 | Sch 4B para 12† "relevant year" and "final relevant year" | encoded | `sch 4B para 12 the number of relevant years in the pensioner's working life`, `sch 4B para 12 the final relevant year` |  |
| 5063 | Sch 4B para 12†, last definition | repealed or blank in this text | line of dots | text shown repealed or blank |
| 5064-5066 | Sch 4B para 13 | encoded | `sch 4B para 13 the flat rate accrual amount` |  |

## Fork register (ssc8)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives every reading, the text that licenses each, the one taken, and the rule that encodes it.
Every reading taken is "assumed, not ruled by a lawyer".

| id | where | readings | taken | text that licenses | rule |
| --- | --- | --- | --- | --- | --- |
| F-S1-1 | Sch 1 para 1(7), (8) | (A) an apportionment divides the whole: the parts add up to the payment or liability; (B) any parts the regulations prescribe are separate payments, whether or not they add up | A: parts that do not add up answer NOTHING | "apportioning the payment" (src:4465); "apportioned, in such manner as may be prescribed, between the secondary contributors" (src:4466) | `sch 1 para 1(7) the separate payments of earnings by the employers`, `sch 1 para 1(8) the secondary contributors' shares of the liability` |
| F-S1-3 | Sch 1 para 3B(3) | (A) the election is no longer in force on the day of the first of the three ending events; (B) it is in force through that day | A | "shall continue in force from the time when it is made until whichever of the following first occurs" (src:4526) | `sch 1 para 3B(3) the election is in force on the day` |
| F-S1-4 | Sch 1 para 3B(7A) | (A) the withdrawal date is the later date the notice specifies, if it is later than the day notice is given, otherwise the day notice is given; (B) the text gives two meanings joined by "or" and does not say which governs when both exist | A | "(a) the date on which notice of the withdrawal of the approval is given, or (b) such later date as the Inland Revenue may specify in that notice" (src:4546-4547) | `sch 1 para 3B(7A) the withdrawal date` |
| F-S1-5 | Sch 1 para 10(1) | (A) "Class 1" means primary and secondary Class 1 only, so Class 1A and Class 1B contributions are not excluded; (B) it covers every class whose name begins "Class 1" | A | "(other than Class 1 or Class 4 contributions)" (src:4742); the Schedule lists "Class 1, Class 1A and Class 1B" as three things at src:4630 and "secondary Class 1 or any Class 1A or Class 1B" at src:4487 | `sch 1 para 10(1) the Secretary of State may pay the contributions and deduct the amount from the pension or allowance` |
| F-S1-6 | Sch 1 para 3(1) | (A) the secondary contributor first pays the whole of the earner's primary contribution unless regulations prescribe a part, in which case the part; (B) the text offers the whole and the part as alternatives and does not say which applies when regulations are silent | A | "the earner's primary contribution or a prescribed part of the earner's primary contribution" (src:4474) | `sch 1 para 3(1) the primary contribution that the secondary contributor is liable in the first instance to pay` |
| F-S1-7 | Sch 1 paras 7A(3)(b), 7B(5)(b) | (A) a penalty may be imposed after the day it is incurred and up to and including the sixth (or third) anniversary; (B) up to the day before the anniversary. A 29 February has no anniversary in a year that is not a leap year, and the text does not say which day stands in | A; a 29 February with no anniversary answers NOTHING | "within six years after the date on which the penalty is incurred" (src:4647, 4675); "within three years after the final determination" (src:4676) | `sch 1 para 7A(3)(b) the penalty may be imposed by the Inland Revenue on the day`, `sch 1 para 7B(5)(b) ...`, `sch 1 paras 7A and 7B the anniversary of the day` |
| F-S1-8 | Sch 1 para 3B(12) | (A) an election was made "before the end of the period of three months beginning with the date of the passing" if it was made before the day three months on (where that month is too short, before the first of the next month), including an election made before the passing; (B) only an election made on or after the passing | A | "an election is made under this paragraph before the end of the period of three months beginning with the date of the passing of the Child Support, Pensions and Social Security Act 2000" (src:4562); the date of passing is not in the text and is an input | `sch 1 para 3B(12) the liabilities are deemed to have fallen on the earner`, `sch 1 para 3B(12) the day three months on` |
| F-S1-9 | Sch 1 para 3A(2), (2A), (3) | (A) the amount recoverable under the agreement is the smaller of what it allows and the secondary Class 1 contribution payable on relevant employment income, less the part (2A) disregards, and nil where (3) applies; (B) the sub-paragraphs say only "to the extent that" and give no arithmetic | A | "does not apply to the extent that an agreement ... allows the secondary contributor to recover ... the whole or any part" (src:4491-4494); "to be disregarded ... to the extent that it relates to" (src:4495); "does not authorise any recovery" (src:4502) | `sch 1 para 3A(2) the amount of the secondary Class 1 contribution that may be recovered under the agreement` |
| F-S2-1 | Sch 2 para 3(4), (5) | (A) a deduction (or relieved payment) is taken from the profits of each year as far as those profits go, a year with no profits absorbs nothing, a year's loss stays as it is, and what is left carries to the next year; (B) a year with a loss increases the amount carried | A | "as far as may be" (src:4775); "deducted as far as may be from those of the immediately following year, whether or not the person claims or is entitled to claim relief under this paragraph for that year, and, so far as it cannot be so deducted, then from those of the next year, and so on" (src:4776, 4786) | `sch 2 para 3(4) the profits for each year after the loss is deducted`, `sch 2 para 3(5) the profits for each year after the payments are deducted` |
| F-S3-1 | Sch 3 Pt I para 2(2) | (A) "that year's lower earnings limit" in (b) is the lower earnings limit of the year in (a), so one year must satisfy (a) and (b) together; (B) (a) and (b) may be satisfied in different years | A | "(a) ... in respect of one of the last three complete years ... (b) ... not less than that year's lower earnings limit multiplied by 25" (src:4811-4812) | `sch 3 pt I para 2(2) the first condition is satisfied` |
| F-S3-2 | Sch 3 Pt I para 2(2), (3) | (A) a "complete" year is a tax year that ended before the benefit year began; so for a benefit year beginning in calendar year B the last complete year began in B-2; (B) another count | A | "the last three complete years before the beginning of the relevant benefit year" (src:4811, 4814); the text does not define "complete"; "benefit year" is s 21(6) (src:761-764), re-encoded here as the first Sunday in January | `sch 3 pt I para 2(2)(a) the record is for the complete year that many years before the benefit year` |
| F-S3-3 | Sch 3 Pt I para 5(7) | (A) "the other years" are the rest of the requisite number; the second condition is deemed met if the qualifying years are at least half the requisite number and qualifying years plus precluded years reach it; (B) the precluded years need not make up the whole | A | "(a) those paragraphs are complied with as respects at least half that number of years ...; and (b) in each of the other years the contributor concerned was, within the meaning of regulations, precluded from regular employment by responsibilities at home" (src:4870-4871) | `sch 3 pt I para 5(7) the second condition is taken to be satisfied` |
| F-S3-4 | Sch 3 Pt I para 2(6)(b) | (A) "benefit year" is the s 21(6) period beginning on the first Sunday in January; (B) regulations "for any prescribed purposes" may give it another meaning, which would change the year | A | "the benefit year in which there falls the beginning of the period of incapacity for work" (src:4828); s 21(6) (src:761-764) | `sch 3 pt I para 2(6)(b) the calendar year in which the relevant benefit year begins` |
| F-S3-5 | Sch 3 Pt I paras 2(4), 2(5), 5(2)(b) | (A) the earnings factor adds the factor from Class 1 earnings (and credited earnings where the sub-paragraph says so) to that from Class 2 (and Class 3) contributions; (B) paragraph 2(4)(a)(i) and (ii) are alternatives joined by "or" and only one counts | A | "(i) ... or (ii) from Class 2 contributions" (src:4818-4819); s 21(5)(c)(i): "the aggregate of his earnings factors derived from so much of his earnings ... and from his Class 2 and Class 3 contributions" (src:753) | `sch 3 pt I para 2(4) the earnings factor for the first condition` and the four like it |
| F-S4B-1 | Sch 4A paras 2(2), 5(2), 6(2), 7(2); Sch 4B paras 4, 5, 8, 9, 10 | (A) to "multiply ... in accordance with the last order under section 148 of the Administration Act" is to scale by (100 + p) / 100, p being the percentage by which that order directs the amount to be increased; (B) another operation | A; p is an input | "multiply the amount of each such part in accordance with the last order under section 148 of the Administration Act" (src:4930); Schedule 4B paragraphs 4 and 8 also increase the FRAA "by the percentage by which earnings factors for 2015-16 are directed to be increased by the last order under section 148" (src:5013, 5032) or multiply it under section 148AA (src:5012, 5031); the orders are not in this text | `sch 4A para 2(2) the amount for the year found band by band` and the other amount functions |

Not forks, but the same kind of decision, with the choice recorded where it is taken:
- the readings (a) and (b) of the FALSE and NOTHING rule are listed under "Marginal readings for a lawyer";
- an input a table would give (every Schedule 4 rate, the bands and percentages of Schedule 4A, the requisite number of years in Schedule 3 paragraph 5(5)) is an input, never a forked reading.

## Jural relations (ssc8)

Hohfeld's pairs: a claim (right) is matched by a duty; a privilege (liberty) by a no-right; a power by a liability; an immunity by a disability.
One row per provision that creates a relation, stated once, from the holder's side.
A provision that creates none (a definition, a counting rule, a heading, a repealed line, or a condition of entitlement whose right is created in another part of the Act) is listed as `none`, with the reason.
The regulation-making powers are rows too: each is a power of the authority and a liability of the persons the regulations may bind.
They are `inert` reason 2 in the coverage table, so they have no L4 rule.
The text does not always name the party on the other side; where it does not, the cell says "not named" and no party is invented.

| Provision (lines) | Holder (right, privilege, power, immunity) | Bearer (duty, no-right, liability, disability) | Relation | L4 rule |
| --- | --- | --- | --- | --- |
| Sch 1 para 1† (1)(a), (b), (1)(closing words) (4456-4459) | none | none | a counting rule: which earnings are one payment of earnings for liability; the closing power to prescribe a different period is a power of the regulation-maker, input only | `sch 1 para 1(1)(a) ...`, `sch 1 para 1(1)(b) ...` |
| Sch 1 para 1† (7), (8) (4465-4466) | none | none | an apportionment rule: it divides a liability that ss 6 to 7 create, and creates none itself (F-S1-1) | `sch 1 para 1(7) ...`, `sch 1 para 1(8) ...` |
| Sch 1 para 1† (8A), para 2†, para 3(6), paras 4†, 5†, 5A† (4467, 4471-4472, 4485, 4567-4578) | the Inland Revenue: power to make regulations on the points listed | the persons whose Class 1, 1A or 1B contributions the regulations govern: liability | power and liability | none (inert 2) |
| Sch 1 para 3(1) (4474) | a payee the sentence does not name: claim to the earner's primary contribution (or a prescribed part) from the secondary contributor; the earner: privilege not to pay it in the first instance ("to the exclusion of the earner") | the secondary contributor: duty to pay it in the first instance; the payee: no-right against the earner in the first instance | duty, with the earner's liberty; what the secondary contributor pays is taken as paid by the earner | `sch 1 para 3(1) the secondary contributor's duty to pay the earner's primary contribution` and the three decision functions of the paragraph |
| Sch 1 para 3(3) (4476) | the secondary contributor: claim to recover from the earner what it paid for them, "subject to and in accordance with regulations" | the earner: duty to reimburse, and only by deduction from earnings (regulations "shall provide ... for it not to be made in any other way") | claim and duty | `sch 1 para 3(3) the amount the secondary contributor is entitled to recover from the earner`, `... the recovery is by deduction from the earner's earnings` |
| Sch 1 para 3(3A), (3B), (4), (5) (4477-4483) | the employer: claim to recover from the employee the primary Class 1 contributions paid on the employee's non-cash earnings, "If and to the extent that regulations so provide" | the employee: duty to reimburse in the prescribed manner | claim and duty, conditional on regulations that the text does not contain (the amount is an input) | `sch 1 para 3(3B) ...`, `sch 1 para 3(4) ...`, `sch 1 para 3(5) ...` |
| Sch 1 para 3A(1) (4487-4490) | the relevant earner: claim that the person liable not deduct, recover or agree to recover the employer's contributions | the person who is or has been liable to pay secondary Class 1, 1A or 1B contributions: duty ("shall not") | claim and duty | `sch 1 para 3A(1) the person liable is prohibited from the act`; `sch 1 para 3A(1) the prohibition on deducting`, `... otherwise recovering`, `... agreeing` |
| Sch 1 para 3A(2), (2A), (3) (4491-4504) | the secondary contributor: privilege to recover secondary Class 1 contribution on relevant employment income under an agreement | the earner: no-right; and, where (2A) or (3) applies, the secondary contributor has no authority to recover (a disability) | privilege, cut back by two disabilities | `sch 1 para 3A(2) the amount of the secondary Class 1 contribution that may be recovered under the agreement` (F-S1-9) |
| Sch 1 para 3A(2B), 3A(4) (4498-4507) | none | none | definitions of "relevant employment income", "agreement", "relevant earner" | `sch 1 para 3A(2B) ...`, `sch 1 para 3A(4) ...` |
| Sch 1 para 3B(1), (1A), (2) (4509-4525) | the secondary contributor and the earner, acting jointly: power to transfer the secondary contributor's liability on relevant employment income to the earner, once the Inland Revenue has approved | the earner: liability to have that liability fall on them; the secondary contributor: liability to be relieved of it; the Inland Revenue is bound to treat the liability as the earner's | power and liability | `sch 1 para 3B(1) this paragraph applies to the election`, `sch 1 para 3B(2) the liability is treated as falling on the earner` |
| Sch 1 para 3B(3) (4526-4529) | either party: power to end the election (jointly revoke; the secondary contributor alone by notice to the earner) | the other party: liability to have the election ended | power and liability | `sch 1 para 3B(3) the election is in force on the day`, `... the ending event has occurred by the day` |
| Sch 1 para 3B(4), (5) (4530-4535) | the Inland Revenue: power to give an approval of one election or of a class; privilege to refuse it, including on the two grounds listed | the secondary contributor: liability to the grant or refusal; no-right to the approval | power and liability; privilege and no-right | `sch 1 para 3B(4) the approval covers the election`, `sch 1 para 3B(5) the Inland Revenue is entitled to refuse the approval` |
| Sch 1 para 3B(6), (7), (7A), (7B) (4536-4550) | the Inland Revenue: power to withdraw an approval by notice; the withdrawal takes effect from the withdrawal date (F-S1-4) | the secondary contributor: liability to the withdrawal; the parties to an affected or void election: disability (the election has no effect on the contributions described, or is void to that extent) | power and liability; disability | `sch 1 para 3B(6) ...`, `sch 1 para 3B(7A) the withdrawal date`, `sch 1 para 3B(7) ...`, `sch 1 para 3B(7B) ...` |
| Sch 1 para 3B(8), (9) (4551-4555) | the person who applied for the approval or to whom it was given: power to appeal against refusal or withdrawal; the tribunal: power to dismiss, remit with a direction or quash | the Inland Revenue: liability to the appeal and to the tribunal's course | power and liability | `sch 1 para 3B(8) ...`, `sch 1 para 3B(9) the tribunal may take the course` |
| Sch 1 para 3B(10) (4556) | the earner: immunity (the election does not apply to contributions on income that was employment income before the election) | the secondary contributor and the Inland Revenue: disability | immunity and disability | `sch 1 para 3B(10) the election applies to the contributions in respect of the income` |
| Sch 1 para 3B(11) (4557-4560) | the Inland Revenue: power to make regulations on elections and approvals | persons making or applying for them: liability | power and liability | none (inert 2) |
| Sch 1 para 3B(12) (4561-4564) | the secondary contributor: claim to reimbursement from the earner for payments toward the liabilities deemed to have fallen on the earner | the earner: duty to reimburse | claim and duty (F-S1-8) | `sch 1 para 3B(12) the liabilities are deemed to have fallen on the earner`, `... the reimbursement the secondary contributor is entitled to from the earner` |
| Sch 1 para 3B(14) (4566) | none | none | a definition of "tribunal" | `sch 1 para 3B(14) the tribunal is` |
| Sch 1 para 6(1), (5)-(7) (4580-4583, 4597-4602) | the Inland Revenue (and, for (5), the Secretary of State with the concurrence of the Inland Revenue): power to make regulations | persons liable to contributions: liability | power and liability | none (inert 2) |
| Sch 1 para 6(2), (3) (4584-4589) | none | none | a statement of what the power includes and the rate of interest (an input) | `sch 1 para 6(2) ...`, `sch 1 para 6(3) the rate of interest` |
| Sch 1 para 6(4), (4A) (4590-4594) | the person liable to the contributions: immunity from interest being required until the decision is made, or while a relevant tax appeal is pending | the Inland Revenue: disability (regulations "shall not require" it) | immunity and disability | `sch 1 para 6(4) ...`, `sch 1 para 6(4A) ...` |
| Sch 1 para 6(4B), (4C) (4595-4596) | the recipient of the interest: immunity from deduction of income tax and from the interest counting in computing income, profits or losses | the payer and the Inland Revenue: disability | immunity and disability | `sch 1 para 6(4B) ...` (two), `sch 1 para 6(4C) ...` |
| Sch 1 para 7(1), (2) (4605-4611) | the Inland Revenue (by regulations under para 6(1)): power to apply TMA s 98A penalties to late contributions returns | the person required to make the return: liability | power and liability | `sch 1 para 7(1) this paragraph applies`, `sch 1 para 7(2) ...` |
| Sch 1 para 7(3) (4612) | the person already penalised under s 98A(2)(a): immunity from a second penalty for the associated contributions return | the Inland Revenue: disability | immunity and disability | `sch 1 para 7(3) ...` |
| Sch 1 para 7(4), (5) (4613-4619) | the Inland Revenue (an authorised officer): power to impose a single penalty on both returns, up to the limit | the person liable on both returns: liability; the limit is a disability of the Inland Revenue | power and liability | `sch 1 para 7(4) the single penalty that may be imposed`, `sch 1 para 7(5) the limit of the single penalty` |
| Sch 1 para 7(6), (8) (4620-4624) | the National Insurance Fund: claim to the contributions part of a recovered single penalty, "for the purposes of making any payment into the National Insurance Fund"; the Inland Revenue: privilege to deduct its administrative costs of recovery first | the Inland Revenue: duty to apportion what it recovers between income tax and contributions in the ratio T:C (sub-paragraph (8): despite any provision treating the penalty as tax) | claim and duty; privilege | `sch 1 para 7(6) the part apportioned to income tax`, `... to contributions`, `sch 1 para 7(8) ...` |
| Sch 1 para 7(9)-(11), (13) (4625-4640) | none | none | construction rules for applying TMA ss 98A, 100D, 103 and the word "associated" | `sch 1 para 7(9) the tax year corresponding to the year of assessment`, `sch 1 para 7(10) what is omitted in applying the subsection`, `sch 1 para 7(11)(a) the reference to tax in section 103(1) includes the contributions`, `sch 1 para 7(11)(b) the penalty is regarded as a penalty in respect of the tax return`, `sch 1 para 7(13) the contributions return and the tax return are associated` |
| Sch 1 para 7(11)(c), (12) (4632-4635) | the person: immunity from the extended time limit on death; from a penalty while a decision that affects it is pending | the Inland Revenue: disability | immunity and disability | `sch 1 para 7(11)(c) ...`, `sch 1 para 7(12) ...` |
| Sch 1 para 7A(1)-(3) (4641-4650) | the Treasury: power to make regulations on penalties for incorrect or missing information; the Inland Revenue: power to impose the penalty within six years; privilege to mitigate, remit, stay or compound | the person who fails or errs: liability; after six years the person has an immunity, the Inland Revenue a disability | power and liability; immunity and disability | `sch 1 para 7A(1) ...`, `sch 1 para 7A(3)(b) the penalty may be imposed by the Inland Revenue on the day` |
| Sch 1 para 7B(1), (2), (5A) (4652-4680) | the Treasury: power to make regulations on payment and penalties outside PAYE | the persons paying or failing to return: liability | power and liability | none (inert 2) |
| Sch 1 para 7B(3), (5)(b), (8)-(10) (4667-4685) | the person liable: immunity from interest until a decision is made; from a penalty after six years or three years from the final determination | the Inland Revenue: disability | immunity and disability | `sch 1 para 7B(3) regulations under sub-paragraph (2)(e) may require the interest to be paid`, `sch 1 para 7B(5)(b) the penalty may be imposed by the Inland Revenue on the day`, `sch 1 para 7B(8) the interest or penalties that may be charged for the earlier period`, `sch 1 para 7B(9) the reference to contributions in sub-paragraph (1) includes the thing`, `sch 1 para 7B(10) the rate of interest` |
| Sch 1 para 7C†, 7D†, 7E†, para 8, para 9† (4686-4698, 4699-4740) | the Inland Revenue, the Treasury, the Secretary of State: powers to make regulations (recovery as income tax, set-off, early Class 2 payment, records, treating payments, repayment, and the like) | the persons the regulations bind: liability | power and liability | `sch 1 para 7C(3) the reference to contributions in this paragraph includes the thing`, otherwise none (inert 2) |
| Sch 1 para 10(1) (4742) | the Secretary of State: privilege to pay the person's contributions (other than Class 1 or Class 4) and deduct the amount from a pension or allowance, with the person's consent; the person: power to give or withhold consent | the person: no-right to the full pension once consent is given; the Secretary of State: liability to the consent | privilege and no-right; power and liability (F-S1-5) | `sch 1 para 10(1) the Secretary of State may pay the contributions and deduct the amount from the pension or allowance`, `... the pension or allowance left after the deduction`, `sch 1 para 10(1) the Secretary of State's permission to pay and deduct` |
| Sch 1 para 10(2) (4743) | none | none | a precedence rule: sub-paragraph (1) prevails over any Act, warrant, order or scheme | `sch 1 para 10(2) sub-paragraph (1) has effect despite the instrument` |
| Sch 1 para 11(1) (4745) | the Treasury: power to make regulations on how sickness payments counting as remuneration are made | the persons through whom they are made: liability | power and liability | none (inert 2) |
| Sch 1 para 11(2) (4746) | a registered friendly society: power to amend its rules by the prescribed procedure despite its rules | the society's rules: disability | power and disability | `sch 1 para 11(2) the amendments may be made notwithstanding the society's rules` |
| Sch 2 para 1† (4748-4754) | none | none | definitions of the Schedule's terms | `sch 2 para 1 the meaning of the term` |
| Sch 2 para 2† (4755-4758) | the Inland Revenue: claim to Class 4 contributions on the full amount of the profits described | the person with those profits: duty to pay | claim and duty (the charge itself is in another part of the Act; this paragraph fixes the base) | `sch 2 para 2 the profit is one in respect of which Class 4 contributions are payable`, `sch 2 para 2 the full amount of the profits in respect of which Class 4 contributions are payable` |
| Sch 2 para 3(1), (2) (4759-4772) | the person: claim to the listed reliefs (3(1)); the Inland Revenue: privilege to refuse the personal reliefs and others listed in (2) | the Inland Revenue: duty to allow (3(1)); the person: no-right to those in (2) | claim and duty; privilege and no-right | `sch 2 para 3(1) relief is available under the provision`, `sch 2 para 3(2) the relief provision does not apply` |
| Sch 2 para 3(4), (5) (4774-4786) | the person: claim to have the loss deduction and the listed payments reduce profits, year after year | the Inland Revenue: duty to deduct "as far as may be" (F-S2-1) | claim and duty | `sch 2 para 3(4) the profits for each year after the loss is deducted`, `sch 2 para 3(5) the amount of the payment for which relief is allowed` and the helpers |
| Sch 2 para 4†(1), (2) (4788-4789) | the Inland Revenue: claim to each partner's contributions on their share | each partner: duty on their own share; each partner has an immunity from the others' share | claim and duty; immunity | `sch 2 para 4(1) the profits in respect of which the partner's liability arises`, `sch 2 para 4(2) the contributions are charged on the partner separately` |
| Sch 2 para 5† (4791-4794) | the trustee, or any other person: immunity from Class 4 contributions on profits received as trustee | the Inland Revenue: disability | immunity and disability | `sch 2 para 5 Class 4 contributions are payable on the profits received as trustee` |
| Sch 2 para 6† (1) (4796) | the Inland Revenue: claim to late payment interest on amounts due for Class 4 (FA 2009 s 101); the person: claim to interest on sums HMRC owes (s 102) | the person: duty to pay interest; HMRC: duty to pay interest | two claims and duties | `sch 2 para 6(1) section 101 of the Finance Act 2009 applies to the sum`, `... section 102 ...` |
| Sch 2 para 7† (4798) | the person and the Inland Revenue, each: immunity from having an income-tax assessment that is final and conclusive re-opened for Class 4; the Inland Revenue: immunity from any allowance or adjustment on the ground of diminution of income or loss, unless made on a special application before or allowed under paragraph 3(5) | the other of them: disability; the person: disability to claim the allowance or adjustment | immunity and disability | `sch 2 para 7 the assessment is final and conclusive for computing Class 4 liability`, `sch 2 para 7 the allowance or adjustment may be taken into account in computing the profits` |
| Sch 2 para 8† (4799-4801) | the person: power to appeal as under TMA Part V, with the Schedule's reservation | the Inland Revenue: liability to the appeal | power and liability | `sch 2 para 8 Part V of the Taxes Management Act 1970 applies to the matter` |
| Sch 3 Part I para 1†, 3†, 4† and Part II para 7† (4806-4807, 4838-4841, 4898) | none | none | repealed or blank lines | none (repealed or blank) |
| Sch 3 Part I para 2 (4808-4837) | none (the claim to short-term incapacity benefit is created by s 30A in another part) | none | the contribution conditions the claimant must meet; this Schedule creates no claim | `sch 3 pt I para 2 the contribution conditions for short-term incapacity benefit are satisfied` (seam S1) and its parts |
| Sch 3 Part I para 5 (4842-4876) | none (the claims arise in the sections that cite paragraph 5: ss 37 and 38 at src:1073 and 1087, s 44 at src:1251, ss 48A to 51ZA at src:1485-1548, s 51 at src:1616, elsewhere) | none | the contribution conditions; deeming rules in (6), (6A), (7) | `sch 3 pt I para 5 the contribution conditions for the benefit are satisfied` (S1) and its parts |
| Sch 3 Part I para 5A (4877-4891) | none (the claims arise in the sections that cite paragraph 5A: s 44 at src:1252, ss 48A to 51ZA at src:1485-1548, s 51 at src:1617, elsewhere) | none | the contribution condition for persons reaching pensionable age on or after 6 April 2010 | `sch 3 pt I para 5A the contribution conditions for the benefit are satisfied` (S1) and its parts |
| Sch 3 Part I para 6, Part II para 8† (4892-4899) | none (the claim to child's special allowance arises in the section that cites paragraph 6, src:1754, elsewhere) | none | the contribution condition; a deeming rule for a repeat claim | `sch 3 pt I para 6 the contribution conditions for a child's special allowance are satisfied` (S1), `sch 3 pt II para 8 the first contribution condition is taken to be satisfied` |
| Sch 4 and its Parts I to V (4901-4907) | none | none | headings over tables the text omits; four rates cross as inputs | `sch 4 pt I para 2 the lower rate of short-term incapacity benefit in pounds`, `... the higher rate ...`, `sch 4 pt V para 5 ...`, `sch 4 pt V para 6 ...` (seams S2, S34) |
| Sch 4A Parts I to IV (4908-4995) | none (the pensioner's claim to the additional pension arises in ss 44 to 45B, elsewhere) | none | computation of an amount of additional pension payable under s 45(2)(c); the Secretary of State may make regulations in Part IV (inert 2) | `sch 4A para 1 the amount referred to in section 45(2)(c)` and the functions for paragraphs 2 to 8 |
| Sch 4B Parts 1 to 5 (4996-5066) | none (the claim arises in ss 44 to 45B) | none | computation of an amount payable under s 45(2)(d) | `sch 4B para 1 the amount referred to in section 45(2)(d)` and the functions for paragraphs 2 to 13 |
| Every line the text shows as dots (44 lines, each in a `repealed or blank in this text` row of the coverage table; some are also named in the rows above): Schedule 1: 4460-4464, 4468-4470, 4475, 4484, 4565, 4603, 4623, 4671, 4681-4682, 4696, 4717, 4719-4720, 4729, 4735-4736; Schedule 2: 4753, 4762, 4768, 4770, 4773, 4778, 4792, 4797, 4802-4803; Schedule 3: 4807, 4839-4841, 4898, 4900; Schedule 4: 4904; Schedule 4A: 4941, 4989; Schedule 4B: 5056, 5063 | none | none | repealed or blank: no provision, so no relation | none (repealed or blank) |

## Marginal readings for a lawyer (ssc8)

Two readings of the rule of 2026-10-29 are for a lawyer to decide, not for me.
I took both as the status quo and list every branch that rests on one.

- **Reading (a): a failed "if" is the text's no, clause by clause; a flat negative is the text saying no.**
  It is an inference: "if A then B" does not itself say "if not A then not B".
  Every FALSE-kind branch of this range rests on it, so the first table lists all of them (the generator reads them from the `-- FALSE-kind` comments in the `.l4` files, so the table cannot drift from the code).
  The other reading, for every row of that table: the sentence says what follows when its condition is met (or what is barred in the case it names) and is silent on every other case, so the function would answer `NOTHING` (not covered) there instead of `JUST FALSE`.
  The column "Rests on" says which kind of sentence the "no" comes from: a flat negative ("shall not", "does not", "no ... shall"), an exclusion in the text's own words ("to the exclusion of", "other than", "nothing in this sub-paragraph applies"), a definition ("means", or "are associated if"), or a failed condition ("if", "until", "is that", "in a case where", "only").
- **Reading (b): a prohibition or grant limited by its own wording does not say no outside the limit.**
  Every NOTHING-kind branch marked "limited by its own wording" rests on it; the second table lists all of them.
  The other reading, for every row of that table: outside its limit the sentence is a no, so the function would answer `JUST FALSE`.
  For the "Where ..." and "In any case where ..." sentences this is the same question as reading (a) puts for "if", and a lawyer may well prefer one answer for both.
  In general I applied (b) to sentences that begin "Where ..." or "In any case where ..." and grant or apply something, and (a) to sentences built on "if", "until", "is that" or "only" and to flat negatives.
  Three sentences mix the two and are the places a lawyer is most likely to choose differently: Schedule 1 paragraph 7(12) ("shall not be imposed where", read as a flat negative under (a)), Schedule 2 paragraph 3(1)(a) ("but only where loss arises from ...", read as "only" under (a)), and Schedule 3 paragraph 5A(1)(a) ("in a case where ... attains pensionable age on or after 6th April 2010", read under (a); see below).

### Branches that answer `JUST FALSE`, resting on reading (a)

| Module | Rule | Rests on | The words the no rests on |
| --- | --- | --- | --- |
| `ssc8-sch1a.l4` | `sch 1 para 3(1) the earner is liable in the first instance for that primary contribution` | (a) exclusion in the text's own words | "on behalf of and to the exclusion of the earner" |
| `ssc8-sch1a.l4` | `sch 1 para 3(3) the recovery is by deduction from the earner's earnings` | (a) flat negative | "and for it not to be made in any other way" |
| `ssc8-sch1a.l4` | `sch 1 para 3A(2) the amount of the secondary Class 1 contribution that may be recovered under the agreement` | (a) flat negative | "Sub-paragraph (2) above does not authorise any recovery" |
| `ssc8-sch1a.l4` | `sch 1 para 3A(2B) the amount is relevant employment income` | (a) definition | "“relevant employment income”, in relation to the earner, means" (a), (b) or (c) |
| `ssc8-sch1a.l4` | `sch 1 para 3A(4) the earner is a relevant earner` | (a) definition | "“relevant earner” ... means an earner in respect of whom he is or has been so liable" |
| `ssc8-sch1a.l4` | `sch 1 para 3B(1A) the amount is relevant employment income` | (a) definition | "“relevant employment income”, in relation to the earner, means" (a), (b) or (c) |
| `ssc8-sch1a.l4` | `sch 1 para 3B(3) the election is in force on the day` | (a) failed condition | "shall continue in force ... until whichever of the following first occurs" |
| `ssc8-sch1a.l4` | `sch 1 para 3B(6) the Inland Revenue may withdraw the approval by notice` | (a) failed condition | "If, at any time after they have given an approval ..., it appears to the Inland Revenue" (a) or (b) (reading (a): a failed "If" is the text's no) |
| `ssc8-sch1a.l4` | `sch 1 para 3B(7) the election has no effect on the contributions on the income` | (a) failed condition | "shall have the effect that the election ... has no effect on contributions on relevant employment income if" (i) or (ii) (reading (a): a failed "if" is the text's no) |
| `ssc8-sch1a.l4` | `sch 1 para 3B(10) the election applies to the contributions in respect of the income` | (a) flat negative | "an election under sub-paragraph (1) above shall not apply to any contributions in respect of income which, before the election was made, counted as employment income" |
| `ssc8-sch1b.l4` | `sch 1 para 6(4) regulations under sub-paragraph (1) may require the interest to be paid` | (a) flat negative | "regulations under sub-paragraph (1) above shall not require any such interest to be paid until the decision has been made" |
| `ssc8-sch1b.l4` | `sch 1 para 6(4A) regulations under sub-paragraph (1) may require interest on the Class 1B sum to be paid` | (a) flat negative | "shall not require the payment of interest on a sum due in respect of a Class 1B contribution if a relevant tax appeal has been brought but not finally determined" |
| `ssc8-sch1b.l4` | `sch 1 para 6(4B) a deduction of income tax is made from the interest` | (a) flat negative | "shall be paid without any deduction of income tax" |
| `ssc8-sch1b.l4` | `sch 1 para 6(4B) the interest is taken into account in computing income, profits or losses for tax purposes` | (a) flat negative | "shall not be taken into account in computing any income, profits or losses for any tax purposes" |
| `ssc8-sch1b.l4` | `sch 1 para 6(4C) the interest is taken into account in computing income, profits or losses for tax purposes` | (a) flat negative | "is not to be taken into account in computing any income, profits or losses for any tax purposes" |
| `ssc8-sch1b.l4` | `sch 1 para 7(3) the person may also be required to pay a penalty under paragraph (a) for the associated contributions return` | (a) flat negative | "he shall not also be required to pay a penalty under that paragraph in respect of any failure in respect of the associated contributions return" |
| `ssc8-sch1b.l4` | `sch 1 para 7(11)(c) section 103(1)(b) applies to the penalty in respect of the associated contributions return` | (a) flat negative | "it shall also not apply in relation to a penalty so imposed in respect of the associated contributions return" |
| `ssc8-sch1b.l4` | `sch 1 para 7(12) a penalty under section 98A may be imposed` | (a) flat negative | "A penalty under section 98A of that Act as it applies by virtue of this paragraph shall not be imposed where" |
| `ssc8-sch1b.l4` | `sch 1 para 7(13) the contributions return and the tax return are associated` | (a) definition | "a contributions return and a tax return are “associated” if" (i) or (ii) (a definition by "if") |
| `ssc8-sch1b.l4` | `sch 1 para 7B(3) regulations under sub-paragraph (2)(e) may require the interest to be paid` | (a) flat negative | "regulations under sub-paragraph (2)(e) above shall not require any such interest to be paid until the decision has been made" |
| `ssc8-sch1b.l4` | `sch 1 para 7B(8) the interest or penalties that may be charged for the earlier period` | (a) "only" | "but only to the extent that interest or penalties would have been chargeable" |
| `ssc8-sch2.l4` | `sch 2 para 3(1) relief is available under the provision` | (a) "only" | "but only where loss arises from activities the profits ... of which would be brought into computation for the purposes of Class 4 contributions" |
| `ssc8-sch2.l4` | `sch 2 para 5 Class 4 contributions are payable on the profits received as trustee` | (a) flat negative | "such contributions shall not be payable either by him or by any other person" |
| `ssc8-sch2.l4` | `sch 2 para 7 the allowance or adjustment may be taken into account in computing the profits` | (a) flat negative | "no allowance or adjustment of liability, on the ground of diminution of income or loss, shall be taken into account ... unless" |
| `ssc8-sch3.l4` | `sch 3 pt I para 2(2) the first condition is satisfied` | (a) failed condition | "The first condition is that" (reading (a): a failed limb is the text's no) |
| `ssc8-sch3.l4` | `sch 3 pt I para 2(3) the second condition is satisfied` | (a) failed condition | "The second condition is that" (reading (a): a failed limb is the text's no) |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(1) this paragraph sets out the contribution conditions for the benefit` | (a) exclusion in the text's own words | "(other than one in relation to which paragraph 5A applies)" |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(6) the first condition is taken to be satisfied` | (a) failed condition | "The first condition shall be taken to be satisfied if" (reading (a): this sub-paragraph does not deem it) |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(6B) the allowance is main phase employment and support allowance` | (a) definition | "is to an employment and support allowance in the case of which the calculation of the amount payable in respect of the claimant includes an addition" |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(6A) the first condition is taken to be satisfied` | (a) failed condition | "The first condition shall be taken to be satisfied if" (reading (a): this sub-paragraph does not deem it) |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(2) the first condition is satisfied` | (a) failed condition | "The first condition is that" (reading (a): a failed limb is the text's no) |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(3) the second condition is satisfied` | (a) failed condition | "The second condition is that" (reading (a): a failed limb is the text's no) |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(7) the second condition is taken to be satisfied` | (a) exclusion in the text's own words | "But nothing in this sub-paragraph applies in relation to any benefit to which section 23A above applies" |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(7) the second condition is taken to be satisfied` | (a) failed condition | "shall be taken to be satisfied notwithstanding ... if" (reading (a): this sub-paragraph does not deem it) |
| `ssc8-sch3.l4` | `sch 3 pt I para 5A(1) this paragraph applies to the benefit` | (a) failed condition | "in a case where the contributor concerned attains pensionable age on or after 6th April 2010" |
| `ssc8-sch3.l4` | `sch 3 pt I para 5A(2) the contribution condition is satisfied` | (a) failed condition | "The contribution condition ... is that" (reading (a): a failed limb is the text's no) |
| `ssc8-sch3.l4` | `sch 3 pt I para 6 the contribution conditions for a child's special allowance are satisfied` | (a) failed condition | "The contribution condition for a child’s special allowance is that" |
| `ssc8-sch3.l4` | `sch 3 pt II para 8 the first contribution condition is taken to be satisfied` | (a) failed condition | "he shall be taken to satisfy the first contribution condition for the benefit if" (reading (a): this paragraph does not deem it) |
| `ssc8-sch4a.l4` | `sch 4A para 2(1) Part II applies to the tax year` | (a) flat negative | "Part II of this Schedule does not apply in relation to the year" |
| `ssc8-sch4a.l4` | `sch 4A para 2(1) Part II applies to the tax year` | (a) failed condition | "This Part of this Schedule applies if" (reading (a): a failed condition is the text's no) |
| `ssc8-sch4a.l4` | `sch 4A para 3(1) Part III applies to the tax year` | (a) failed condition | "This Part of this Schedule applies if the following condition is satisfied in relation to each tax week" (reading (a)) |
| `ssc8-sch4a.l4` | `sch 4A para 3(3) Part II does not apply because of the condition` | (a) failed condition | "If the condition is satisfied in relation to one or more tax weeks" (reading (a): a failed "If" is the text's no) |
| `ssc8-sch4b.l4` | `sch 4B para 2 Part 2 applies to the relevant year` | (a) failed condition | "This Part applies to a relevant year if" (reading (a): a failed limb is the text's no) |
| `ssc8-sch4b.l4` | `sch 4B para 6 Part 3 applies to the relevant year` | (a) failed condition | "This Part applies to a relevant year if" (reading (a): a failed limb is the text's no) |

44 branches.

The least certain branch is Schedule 3 paragraph 5A(1)(a): "a Category A retirement pension in a case where the contributor concerned attains pensionable age on or after 6th April 2010".
I took the failed "in a case where" as the text's no, so a contributor who attains pensionable age earlier gets `JUST FALSE` for "paragraph 5A applies".
My reason is that paragraph 5(1)(b) says "(other than one in relation to which paragraph 5A applies)", which presupposes that the two paragraphs divide the Category A pensions between them.
The other reading is `NOTHING`, because "in a case where" is a limit of the grant (reading (b)) and the text does not say in so many words that 5A applies to no other case.
For the Category B limb of the same sentence, "in the cases provided for by any of sections 48A to 51ZA", I took reading (b) (`NOTHING` outside), the same as paragraph 5(1)(c), which has the same words; both limbs answer alike in both paragraphs.
The S1 answer for paragraph 5A is `NOTHING` whenever "paragraph 5A applies" is not `JUST TRUE` (`sch 3 pt I para 5A the contribution conditions for the benefit are satisfied`, last branch), so the choice for either limb changes only the intermediate answer of `sch 3 pt I para 5A(1) this paragraph applies to the benefit`.

Two sentences carry an "(other than ...)" parenthetical and are answered differently on purpose, which a lawyer may want to unify.
Schedule 1 paragraph 10(1) is a grant ("the Secretary of State may with the consent of that person pay any contributions (other than Class 1 or Class 4 contributions)"), and its function is named for the permission (`the Secretary of State may pay ...`): outside the limit (a Class 1 or Class 4 contribution, or no consent) it answers `NOTHING`, reading (b), the "named complement" and "with the consent" being limits of the grant.
Schedule 3 paragraph 5(1)(b) says for which benefits a paragraph sets out the conditions ("a Category A retirement pension (other than one in relation to which paragraph 5A applies)"), and its function is a predicate named for that scope (`this paragraph sets out the contribution conditions for the benefit`): past the limit it answers `JUST FALSE`, reading (a).
The other reading of the first would be `JUST FALSE` for Class 1 and Class 4; of the second, `NOTHING` for a Category A pension to which paragraph 5A applies.

Two functions named for a permission that is limited by a stated period or a named complement answer `NOTHING` past the limit, by reading (b): `sch 1 para 7A(3)(b) the penalty may be imposed by the Inland Revenue on the day` (past six years, and the sentence binds the regulation-maker: "Regulations ... shall ... provide for the penalty to be imposed ... within six years") and `sch 2 para 2 the profit is one in respect of which Class 4 contributions are payable` (a profit of a trade carried on wholly outside the United Kingdom, and "Subject to the following paragraphs").
The other reading of both is `JUST FALSE`.

### Branches that answer `NOTHING`, resting on reading (b)

| Module | Rule | The limit the answer rests on |
| --- | --- | --- |
| `ssc8-sch1a.l4` | `sch 1 para 1(1)(b) the single payment of earnings paid by different persons in respect of different employments` | "in prescribed circumstances"; outside them the sub-paragraph says nothing |
| `ssc8-sch1a.l4` | `sch 1 para 3(1) the primary contribution that the secondary contributor is liable in the first instance to pay` | "Where earnings are paid to an employed earner and in respect of that payment liability arises for primary and secondary Class 1 contributions" |
| `ssc8-sch1a.l4` | `sch 1 para 3(1) the contributions are taken to be paid by the earner` | "contributions paid by the secondary contributor on behalf of the earner" |
| `ssc8-sch1a.l4` | `sch 1 para 3(3) the recovery is by deduction from the earner's earnings` | "subject to sub-paragraphs (3A) to (5) below": those sub-paragraphs make their own provision |
| `ssc8-sch1a.l4` | `sch 1 para 3(3B) the amount the employer may recover from the employee` | "Sub-paragraph (3B) applies where" the employee receives earnings other than in money from the employer in a tax year |
| `ssc8-sch1a.l4` | `sch 1 para 3(4) sub-paragraph (5) applies` | "Sub-paragraph (5) below applies in a case where" (a) and (b) |
| `ssc8-sch1a.l4` | `sch 1 para 3(5) the amount the employer may recover from the employee` | the sub-paragraph is for the case sub-paragraph (4) describes |
| `ssc8-sch1a.l4` | `sch 1 para 3B(1) this paragraph applies to the election` | "This paragraph applies where" the election is made jointly and approved |
| `ssc8-sch1a.l4` | `sch 1 para 3B(3) the election is in force on the day` | "from the time when it is made": before it is made the sub-paragraph says nothing |
| `ssc8-sch1a.l4` | `sch 1 para 3B(4) the approval covers the election` | "for an election to be made by the secondary contributor and a particular person" |
| `ssc8-sch1a.l4` | `sch 1 para 3B(4) the approval covers the election` | "for all elections to be made, or to be made in particular circumstances, by the secondary contributor and particular persons or ... of a particular description" |
| `ssc8-sch1a.l4` | `sch 1 para 3B(8) the person may appeal against the Inland Revenue's decision` | "the person who applied for it or, as the case may be, to whom it was given" |
| `ssc8-sch1a.l4` | `sch 1 para 3B(9) the tribunal may take the course` | "in the case of a decision to withdraw an approval" |
| `ssc8-sch1a.l4` | `sch 1 para 3B(9) the tribunal may take the course` | "On an appeal under sub-paragraph (8) above that is notified to the tribunal" |
| `ssc8-sch1a.l4` | `sch 1 para 3B(10) the election applies to the contributions in respect of the income` | "Subject to sub-paragraph (12) below": that sub-paragraph makes its own provision |
| `ssc8-sch1a.l4` | `sch 1 para 3B(12) the liabilities are deemed to have fallen on the earner` | "Where" (a) the election is made within three months of the passing and (b) it is expressed to relate to the earlier liabilities |
| `ssc8-sch1a.l4` | `sch 1 para 3B(12) the reimbursement the secondary contributor is entitled to from the earner` | the entitlement is "accordingly", that is, in the case sub-paragraph (12) describes |
| `ssc8-sch1b.l4` | `sch 1 para 6(4) regulations under sub-paragraph (1) may require the interest to be paid` | the bar lasts "until the decision has been made" and covers only the cases described; the sub-paragraph grants nothing |
| `ssc8-sch1b.l4` | `sch 1 para 6(4A) regulations under sub-paragraph (1) may require interest on the Class 1B sum to be paid` | the bar is for a "relevant tax appeal" "brought but not finally determined"; otherwise the sub-paragraph says nothing |
| `ssc8-sch1b.l4` | `sch 1 para 6(4B) a deduction of income tax is made from the interest` | "Interest required to be paid, by virtue of sub-paragraph (2)(a) or (b) above, by regulations under sub-paragraph (1) above" |
| `ssc8-sch1b.l4` | `sch 1 para 6(4B) the interest is taken into account in computing income, profits or losses for tax purposes` | "Interest required to be paid, by virtue of sub-paragraph (2)(a) or (b) above, by regulations under sub-paragraph (1) above" |
| `ssc8-sch1b.l4` | `sch 1 para 6(4C) the interest is taken into account in computing income, profits or losses for tax purposes` | the sub-paragraph is about interest under section 101 on sums due in respect of Class 1 contributions |
| `ssc8-sch1b.l4` | `sch 1 para 7(1) this paragraph applies` | "This paragraph applies where" regulations make a provision of the two kinds |
| `ssc8-sch1b.l4` | `sch 1 para 7(2) section 98A of the Taxes Management Act 1970 applies to the contributions return as to the tax return` | "Where this paragraph applies, regulations ... may provide ...; and where they so provide" |
| `ssc8-sch1b.l4` | `sch 1 para 7(3) the person may also be required to pay a penalty under paragraph (a) for the associated contributions return` | "Where a person has been required to pay a penalty under paragraph (a) of subsection (2) of section 98A of that Act" |
| `ssc8-sch1b.l4` | `sch 1 para 7(4) the single penalty that may be imposed` | "In any case where" the person is liable in respect of both returns and an officer has so determined |
| `ssc8-sch1b.l4` | `sch 1 para 7(11)(b) the penalty is regarded as a penalty in respect of the tax return` | "any penalty by virtue of sub-paragraph (4) above" |
| `ssc8-sch1b.l4` | `sch 1 para 7(11)(c) section 103(1)(b) applies to the penalty in respect of the associated contributions return` | "where, by virtue of subsection (2) (death), subsection (1)(b) does not apply" |
| `ssc8-sch1b.l4` | `sch 1 para 7(12) a penalty under section 98A may be imposed` | the bar is for the case (a) and (b) describe |
| `ssc8-sch1b.l4` | `sch 1 para 7A(1) this paragraph applies` | "This paragraph applies where paragraph 7 above applies" |
| `ssc8-sch1b.l4` | `sch 1 para 7A(3)(b) the penalty may be imposed by the Inland Revenue on the day` | "within six years after the date on which the penalty is incurred"; outside that period the sub-paragraph grants nothing |
| `ssc8-sch1b.l4` | `sch 1 para 7B(3) regulations under sub-paragraph (2)(e) may require the interest to be paid` | the bar lasts "until the decision has been made" and covers only the cases described; the sub-paragraph grants nothing |
| `ssc8-sch1b.l4` | `sch 1 para 7B(5)(b) the penalty may be imposed by the Inland Revenue on the day` | "within three years after the final determination of the amount of those contributions" |
| `ssc8-sch1b.l4` | `sch 1 para 7B(5)(b) the penalty may be imposed by the Inland Revenue on the day` | "within six years after the date on which the penalty is incurred"; limb (ii) is for a penalty whose amount is ascertained by reference to contributions |
| `ssc8-sch1b.l4` | `sch 1 para 10(1) the Secretary of State may pay the contributions and deduct the amount from the pension or allowance` | "with the consent of that person" and "(other than Class 1 or Class 4 contributions)"; outside those limits the sub-paragraph grants nothing |
| `ssc8-sch1b.l4` | `sch 1 para 10(1) the pension or allowance left after the deduction` | no deduction is provided for unless the Secretary of State may pay under the sub-paragraph |
| `ssc8-sch1b.l4` | `sch 1 para 11(2) the amendments may be made notwithstanding the society's rules` | "In any case where regulations ... have the effect of requiring ..., the amendments may ... be made in accordance with the procedure prescribed" |
| `ssc8-sch2.l4` | `sch 2 para 2 the profit is one in respect of which Class 4 contributions are payable` | the paragraph says what is payable on profits (a) and (b) and nothing of any other profit |
| `ssc8-sch2.l4` | `sch 2 para 3(4) the profits for each year after the loss is deducted` | sub-paragraph (4) is for "the year 1990-1991 or any subsequent year of assessment for which a person claims and is allowed relief" |
| `ssc8-sch2.l4` | `sch 2 para 3(5) the amount of the payment for which relief is allowed` | "being payments for which relief from income tax is or can be given" |
| `ssc8-sch2.l4` | `sch 2 para 3(5) the amount of the payment for which relief is allowed` | "so far as the payment is incurred wholly or exclusively for the purposes of any relevant trade, profession or vocation" |
| `ssc8-sch2.l4` | `sch 2 para 4(1) the profits in respect of which the partner's liability arises` | "Where a trade or profession is carried on by two or more persons jointly" |
| `ssc8-sch2.l4` | `sch 2 para 4(2) the contributions are charged on the partner separately` | "Where sub-paragraph (1) above applies" |
| `ssc8-sch2.l4` | `sch 2 para 5 Class 4 contributions are payable on the profits received as trustee` | "In any circumstances in which apart from this paragraph a person would ... be assessed and charged ... in the capacity of trustee" |
| `ssc8-sch2.l4` | `sch 2 para 6(1) section 101 of the Finance Act 2009 applies to the sum` | the first limb is "any amount due in respect of Class 4 contributions" |
| `ssc8-sch2.l4` | `sch 2 para 6(1) section 102 of the Finance Act 2009 applies to the sum` | the second limb is "sums to be paid by HMRC" in relation to Class 4 contributions |
| `ssc8-sch2.l4` | `sch 2 para 7 the assessment is final and conclusive for computing Class 4 liability` | "Where an assessment has become final and conclusive for the purposes of income tax" |
| `ssc8-sch2.l4` | `sch 2 para 7 the allowance or adjustment may be taken into account in computing the profits` | the exception ends the bar; the sentence does not itself grant the allowance |
| `ssc8-sch2.l4` | `sch 2 para 8 Part V of the Taxes Management Act 1970 applies to the matter` | "nothing in this Schedule affects the extent to which the Income Tax Acts apply with respect to any decision falling to be made" under these provisions |
| `ssc8-sch3.l4` | `sch 3 pt I para 2(2) the first condition is satisfied` | "one of the last three complete years before the beginning of the relevant benefit year" |
| `ssc8-sch3.l4` | `sch 3 pt I para 2(3) the second condition is satisfied` | "the last two complete years before the beginning of the relevant benefit year" |
| `ssc8-sch3.l4` | `sch 3 pt I para 2(7) the previous claim is disregarded` | "Where a person makes a claim ... the previous claim shall be disregarded" |
| `ssc8-sch3.l4` | `sch 3 pt I para 2(9) the thing is a benefit for sub-paragraph (8)` | "credits under regulations under section 22(5) above" only if there were such credits |
| `ssc8-sch3.l4` | `sch 3 pt I para 5(1) this paragraph sets out the contribution conditions for the benefit` | "in the cases provided for by any of sections 48A to 51ZA" |
| `ssc8-sch3.l4` | `sch 3 pt I para 5 the contribution conditions for the benefit are satisfied` | this paragraph sets out the conditions only for the benefits it lists in sub-paragraph (1) |
| `ssc8-sch3.l4` | `sch 3 pt I para 5A(1) this paragraph applies to the benefit` | "in the cases provided for by any of sections 48A to 51ZA", read as in paragraph 5(1)(c), which has the same words |
| `ssc8-sch3.l4` | `sch 3 pt I para 5A the contribution conditions for the benefit are satisfied` | "This paragraph applies to" the two pensions it lists |
| `ssc8-sch4a.l4` | `sch 4A para 8(3) section 44A is ignored in applying section 44(6)` | "for the purpose of calculating amount B" |
| `ssc8-sch4b.l4` | `sch 4B para 10(2) section 44B is ignored in applying section 44(6)` | "for the purposes of this paragraph" |

59 branches.

### Other `NOTHING` answers (not marginal)

The remaining `NOTHING-kind` comments say "silent", "list not closed", "includes", "undefined term" or "points outside the text".
They are not readings for a lawyer to choose between: the text gives no answer, or sends the question to a table, a regulation, an order or another Act that is not in these sources.
Counts, from the same generator: silent: 13; list not closed: 7; includes: 8; undefined term: 8; points outside the text: 18.

### Reading a result: FALSE and NOTHING (ssc8)

Every decision function of this range that is a yes-or-no question answers one of three things: `JUST TRUE`, `JUST FALSE`, or `NOTHING`.
A caller must never turn `NOTHING` into `FALSE`.

- **`JUST FALSE` is the text saying no in its own words.**
  In Schedule 1 it is a prohibition or bar the sentence states ("shall not also be required to pay a penalty", "does not authorise any recovery", "shall not require ... interest ... until the decision has been made"), an exclusion ("to the exclusion of the earner"), or a failed condition the sentence sets ("until whichever of the following first occurs").
  In Schedule 2 it is the text's own flat negatives ("such contributions shall not be payable either by him or by any other person", "no allowance or adjustment ... shall be taken into account") and the "but only where" of the loss relief.
  In Schedule 3 it is a failed limb of a condition the paragraph states ("The first condition is that ...", "The contribution condition ... is that ...", "shall be taken to be satisfied if ..."): the claimant does not meet that condition on the facts given.
  It is not "the claimant gets no benefit": the right to a benefit arises in another part of the Act, and a `JUST FALSE` here means only that this Schedule's condition is not met.
  In Schedules 4A and 4B it is "Part II of this Schedule does not apply in relation to the year" (`sch 4A para 2(1) Part II applies to the tax year`), or a Part that applies "if" its condition holds and the condition fails.
  The function `sch 4A para 3(3) Part II does not apply because of the condition` is named for the proposition the sentence asserts, so it answers `JUST TRUE` when the condition holds in one or more tax weeks (the same weeks make `Part II applies` `JUST FALSE`) and `JUST FALSE` when it holds in none (reading (a)).
  Whether a failed "if" is really the text's no is reading (a), for a lawyer (see above).
- **`NOTHING`, shown to a person as "not covered", is the text giving no answer.**
  Either the text is silent, or its list is not closed, or it says "includes", or it leaves a term undefined, or it sends the question to something outside these sources, or the case falls outside the limit of a grant or prohibition the text words narrowly.
  In this range the commonest reasons are:
  a rate, band or percentage that sits in a table this text omits (all of Schedule 4, the three tables of Schedule 4A, the requisite-years table of Schedule 3 paragraph 5(5)); a rate or an amount that regulations, an order under section 148 of the Administration Act or a Treasury or Inland Revenue power fixes; a term defined in another Act (ITEPA 2003, TMA 1970, ITA 2007, Finance Act 2009, the Pension Schemes Act 1993); a date the Act refers to and does not state (the day of the passing of the Child Support, Pensions and Social Security Act 2000); and a "Where ..." or "In any case where ..." sentence that does not fit the case.
  `NOTHING` does not mean "no entitlement" and does not mean "yes": it means this text cannot say.
- **Where a person's answer is `NOTHING`, the seat shows it as not covered, and no caller (including the seat layer) turns it into a yes or a no.**
  For example, a Category A retirement pension for a person who reached pensionable age on or after 6 April 2010 asks paragraph 5A, and the 30-year condition answers `JUST TRUE` or `JUST FALSE`; a person who reached it earlier is outside paragraph 5A, so that question is `NOTHING` (not covered) and the person is directed to paragraph 5 by the section that cites it.
  The tests assert the `NOTHING` answers as well as the others, so a change that turns one into a `FALSE` fails the suite.

## Seams (ssc8)

Names are as PLAN.md section 5 gives them (the brief says section 8; see the head).
A seam input is a `GIVEN` parameter named for the answering section; the lead wires it when the parts are merged.

| seam | direction | the L4 name or input in this range | type | note |
| --- | --- | --- | --- | --- |
| S1 | ssc8 answers (asked by ss 21(3), 30A(2)(a), 37(1), 38(1), 39A(2), 44, 51) | `sch 3 pt I para 2 the contribution conditions for short-term incapacity benefit are satisfied`, `sch 3 pt I para 5 the contribution conditions for the benefit are satisfied`, `sch 3 pt I para 5A the contribution conditions for the benefit are satisfied`, `sch 3 pt I para 6 the contribution conditions for a child's special allowance are satisfied` | `MAYBE BOOLEAN` | The PLAN names the paragraph the asking sentence cites (2, 5 or 5A); paragraph 6 is the child's special allowance (src:1754), which the PLAN's row does not list. Paragraphs 5 and 5A serve several benefits, so their names say "the benefit". |
| S2 | ssc8 answers (asked by s 30B(2)) | `sch 4 pt I para 2 the lower rate of short-term incapacity benefit in pounds`, `sch 4 pt I para 2 the higher rate of short-term incapacity benefit in pounds` | `MAYBE NUMBER` | the table is omitted from this text, so each takes the rate "that the omitted table of Part I of Schedule 4 specifies" as a `MAYBE NUMBER` input and passes it through; unstated stays `NOTHING` |
| S34 | ssc8 answers (asked by Schedule 7) | `sch 4 pt V para 5 the increase of the disablement pension in pounds`, `sch 4 pt V para 6 the increase of the unemployability supplement in pounds` | `MAYBE NUMBER` each | same: a pass-through of an omitted table |
| S11 | ssc8 asks | `s 22(5) the person was credited with contributions or earnings by regulations` | `BOOLEAN` | used by `sch 3 pt I para 2(9) the thing is a benefit for sub-paragraph (8)` |
| S31 | ssc8 asks | `s 44 the final relevant year` (a `Tax year`); and, for the count of relevant years, `the number of relevant years` as a `NUMBER` input of `sch 4A para 1 ...` | `Tax year` and `NUMBER` | the PLAN types both `s 44 the relevant year` and `s 44 the final relevant year` as `Tax year`; Schedule 4A paragraph 1 needs only the count (it is the divisor), so I take a number |

Seams I found that the PLAN lacks:

- `s 44A the low earnings threshold for the year`, a `NUMBER` input of `sch 4A para 2(6)(b) LET`.
  Schedule 4A paragraph 2(6)(b) says "LET" means the low earnings threshold "as specified in section 44A above" (src:4939).
  The threshold is an amount in a section of ssc3, so it is a seam; Schedule 4B paragraph 12 (src:5059) says the same, and there it is a field of the `sch 4B a relevant year` record (`the low earnings threshold for the year`).
- `s 122(1) the qualifying earnings factor for the year`, a `NUMBER` input of `sch 4A para 2(6)(c) QEF` (src:4940: "QEF" means the qualifying earnings factor for the tax year concerned), and likewise a field of `sch 4B a relevant year` for Schedule 4B paragraph 12 (src:5060).
  Section 122(1) is in ssc5 and defines the term; the figure for a year is an input there too.
- The numbers that Schedule 4B paragraph 12 hands back to section 44 ("relevant year" and "final relevant year" have the meanings in section 44, src:5062) are fields of the `sch 4B a relevant year` and `sch 4B the final relevant year` records, not new functions.
- The percentage by which the last order under section 148 of the Administration Act directs earnings factors to be increased: a `NUMBER` input of Schedule 4A paragraphs 2(2), 5(2), 6(2) and 7(2) (`the percentage by which the last order under section 148 directs the year's earnings factors to be increased`), and a field of `sch 4B a relevant year` for Schedule 4B paragraphs 5, 9 and 10.
  Schedule 4B paragraphs 4 and 8 add two more: the section 148AA percentage for the flat rate accrual amount and the section 148 percentage for 2015-16, both fields of `sch 4B the final relevant year` (F-S4B-1).
  Sections 148 and 148AA are not among the sources.
- The count of relevant years, the surplus, the pensioner's earnings factor, the number of tax weeks in the year and the number of those in which the contracted-out condition is satisfied are inputs in the same way (Schedule 4A: `GIVEN` parameters; Schedule 4B: fields of `sch 4B a relevant year`).
  They are other sections' answers (ss 44, 44A, 45) and the Schedules say so ("relevant year" and "final relevant year" have the meanings in section 44, src:4925, 4943, 5062).

Types of my own that resemble a core type, and why (nothing is missing from the core, so there is no `NEEDS-CORE.md`):

- `sch 1 para 3A kind of contribution` has three members for the three kinds of contribution that paragraph 3A(1) names ("secondary Class 1 or any Class 1A or Class 1B", src:4487) and a fourth, `some other contributions`, for which the function answers `NOTHING`.
  The core's `Class of contribution` has eight members, including Class 1 primary, 2, 3, 3A and 4, which paragraph 3A does not speak of, and no "other" member; a seat question over it would offer choices the paragraph cannot answer.
  The core type is used where a class is a fact about a payment (`ssc8-sch1b.l4`, paragraphs 6(2) and 7C(3)).
- The other small enums (`sch 1 para 3A kind of act`, `sch 2 para 3 relief provision`, `sch 4A which table` and the like) name members of a list that one sentence of the text gives, with an "other" member where the text does not close the list; the core has no counterpart for any of them.

## Seat (ssc8)

**The seat** is a person who works, is self-employed, or claims a benefit, statutory pay or Child Benefit in Great Britain, asking what this range of the Act means for them: whether and how much they must pay in contributions, whether they meet a benefit's contribution conditions, how much additional pension a year's figures give, and what the Revenue may and may not take back from them.
The employer, the partner, the trustee and the Inland Revenue have no seat questions of their own: what the Schedules mean for them is asked from the person's side ("my employer", "my pension").

- **Files.** `ssc8-seat.l4` (27 questions, each an `@export` whose description is the question and whose inputs carry an inline `@desc`) and `ssc8-cases-seat.l4` (64 `#ASSERT`s through the questions).
  Every question name begins "Under schedule N paragraph M," so that no two parts' questions can share a name.
- **Order.** The questions sit under `§` and `§§` headings in the order of the text: Schedule 1 paragraphs 1, 3, 3A, 3B, 6 to 7B, 10; Schedule 2 paragraphs 2 and 3, 4, 5; Schedule 3 paragraphs 2, 5, 5A, 6; Schedule 4A paragraphs 1 and 2; Schedule 4B paragraph 1.
  Headings for provisions that apply only to some people say so ("an election to move my employer's liability on to me (only if I have made such an election)"), so that a form can ask "has this happened to you?" first.
- **No rule is restated.**
  Each question builds the records the long modules expect from plain answers (a number, a date, a yes or no) and calls the same function; the long modules are imported, not copied.
  The inputs are plain values, because an input of a record type cannot be filled by a form.
- **Inputs a table or a regulation would give are asked of the person.**
  The Schedule 4 rates, the bands and percentages of Schedule 4A, the requisite number of years of Schedule 3 paragraph 5(5), the percentage by which an order under section 148 increases earnings factors, and the amount that regulations allow an employer to recover are each a number the person states, with a `@desc` that says where it comes from.
  A placeholder is never typed in from memory.
- **Limits of the seat, so a reader does not take a question for more than it is.**
  The Schedule 4A paragraph 2 question takes two bands, because the table of bands is not in this text; a table with more bands needs the long function (`sch 4A para 2(2) the amount for the year found band by band`) directly.
  The Schedule 4A paragraph 1 and Schedule 4B paragraph 1 questions take the totals the later paragraphs produce as inputs, so Schedule 4A paragraphs 3 to 8 and Schedule 4B paragraphs 2 to 13 have no question of their own.
  Schedule 4 has no question: it only passes through rates the person would have to state (seams S2 and S34).
  The regulative twins (Schedule 1 paragraphs 3(1), 3A(1), 10(1)) have no seat question; the decision functions that carry the same duties are asked instead.
- **Cases.** The 64 assertions were generated by `work/gen_cases.py` from the question names, with expected values worked by hand from the text and stated in the comment above each assertion (for example Schedule 4A paragraph 2: surplus 8,000; first band to 5,000 at 20%, second band at 10%; order increase 10%; 5,000 x 1.10 x 20% + 3,000 x 1.10 x 10% = 1,430).
  A case whose answer is `NOTHING` says so beside the assertion, with the text that leaves it open.

## What the text turns out to say

Numbered so they can be cited; each is something I read in the text (line numbers are the converter rendering's, not the official text's) and not an opinion.

1. **The rendering drops every paragraph number in the Schedules and keeps only the headings.**
   Schedule 4 (src:4901-4907) is its title, five Part headings and one line of dots: no rate survives, so each Schedule 4 Part heading is `repealed or blank in this text`, and the four Schedule 4 functions (for seams S2 and S34) are pass-throughs of rates the person states.
   Paragraph labels marked † in this file are counted from position (see the head).
2. **No table survives in Schedule 4A.**
   Part II (paragraph 2), amount A and amount B in its second case (Part III) each say "The appropriate table for ... is as follows—" three times (src:4933-4935, 4960-4962, 4978-4980), and no table follows any of them.
   The three sentences cover persons attaining pensionable age after the end of the first appointed year, and none covers persons attaining it before the end of that year.
   Amount B in its first case gives a percentage ("20 + N", "20") only for the same two ranges (src:4969-4970).
   So for a person who attained pensionable age before the end of the first appointed year, `sch 4A para 2(3) which table applies` answers `sch 4A no table is given`, and the amounts answer `NOTHING`: the text names no table or percentage for them.
   The first appointed year is appointed by order (section 122(1)), so it is an input.
3. **Schedule 3 paragraph 2's two conditions are tied to the year's own lower earnings limit, by different multiples.**
   The first condition needs an earnings factor "not less than that year's lower earnings limit multiplied by 25" (src:4812), the second "multiplied by 50" in each of the last two complete years (src:4815); paragraph 6(1)(b) says 50 as well (src:4895).
   These multiples are the Act's own and are typed into the long module; the limits themselves are inputs.
4. **Schedule 3 paragraph 2(4)(a) joins its two sources of earnings factor with "or", while section 21(5)(c)(i) defines the earnings factor as the aggregate of the earnings and the Class 2 and 3 contributions** (src:4818-4819, 753).
   I read paragraph 2(4)(a) as the aggregate (F-S3-5).
   A lawyer may read it as one source or the other.
5. **Schedule 2 names section 383 of ITA 2007 twice for opposite purposes.**
   Paragraph 3(2)(b) lists it among the reliefs that "shall not apply" (src:4767); paragraph 3(5)(b) allows relief for "payments under section 383 ..., being payments for which relief from income tax is or can be given" "so far as the payment is incurred wholly or exclusively for the purposes of any relevant trade, profession or vocation" (src:4779, 4786).
   The two sub-paragraphs are encoded as separate functions that do not call each other; the text does not say which prevails in a case that satisfies both.
6. **Paragraphs 6(4) and 7B(3) of Schedule 1 are the same bar on interest, resting on different statutes.**
   Paragraph 6(4) bars interest until a decision under "section 8, 10 or 11 of the Social Security Contributions (Transfer of Functions, etc.) Act 1999" has been made (src:4591); paragraph 7B(3) bars it for a decision under "section 8, 9, 10, 12, 14 or 15 of the Social Security Act 1998" (src:4668); paragraph 7(12) uses the 1999 Act's list again for penalties (src:4634).
   They are separate functions (the 1999 Act's list in 6(4) and 7(12), the 1998 Act's list in 7B(3)), each taking as its first input that its own list of sections applies, so a decision under the other Act's sections does not trigger the bar.
7. **Paragraph 7(11)(a) of Schedule 1 names "Class 1, Class 1A and Class 1B" as three things** (src:4630), and paragraph 3A(1) says "secondary Class 1 or any Class 1A or Class 1B" (src:4487).
   That is why paragraph 10(1)'s "(other than Class 1 or Class 4 contributions)" is read as excluding only the Class 1 contributions of an employed earner and Class 4, not Class 1A or 1B (F-S1-5).
8. **Two dates the Act refers to are not in the text.**
   "the day of the passing of the Child Support, Pensions and Social Security Act 2000" appears in paragraphs 3A(3)(b) and 3B(12) (src:4504, 4562) and is an input; "19th May 2000" is stated (src:4503, 4563) and is typed in.
9. **A penalty period measured in years has no end on a 29 February.**
   Paragraphs 7A(3)(b) and 7B(5)(b) allow imposition "within six years after the date on which the penalty is incurred" and "within three years after the final determination" (src:4647, 4675-4676); the text does not say what the sixth or third anniversary of 29 February is in a year that is not a leap year.
   `sch 1 paras 7A and 7B the anniversary of the day` answers `NOTHING` then, and the tests assert it for 29 February 2008 (third and sixth anniversaries) and `JUST (Date 29 2 2012)` for the fourth.
10. **The Act itself states two sums of money in this range and a few fixed numbers; everything else is left to a table, a regulation or an order.**
    The sums are the flat rate accrual amount, £72.80 where the final relevant year is 2015-16 or earlier and £93.60 otherwise (src:5065-5066, "but subject to section 148AA of the Administration Act").
    The fixed numbers are 25 and 50 times the lower earnings limit (src:4812, 4815, 4895), not less than 30 years of a working life (src:4881), N = 0.5 for each tax year before 2009-10 (src:4985), 20 for amount B (src:4970), and in Schedule 4B 10%, 44 and 20% (src:5017-5018, 5038-5039, 5047).
    These are typed into the long modules; limits, rates, thresholds, percentages and the requisite number of years are inputs.
11. **Schedule 1 paragraph 3(1) does not say who is paid.**
    "be liable in the first instance to pay also the earner's primary contribution or a prescribed part of the earner's primary contribution, on behalf of and to the exclusion of the earner" (src:4474) names no payee, so the Jural relations table gives the claim's holder as "not named" and the regulative twin has only the secondary contributor as a party.
    The whole-or-a-part alternative is F-S1-6.

## What the stable binary does not accept

The brief says the stable binary (1.6.98) governs where a skill describes a construct it rejects.
Sorted by how each failure shows up.

**Loud (an error, so it teaches):**
- A function applied to a field access must have the access in parentheses: `f (election's \`x\`) day`, `JUST (payment's \`x\`)`.
  Without them, `f election's \`x\` day` and `JUST payment's \`x\`` parse as `(f election)'s x` and `(JUST payment)'s x` and fail to type-check.
- A lambda whose body joins two tests with `AND` needs the body in parentheses: `GIVEN y YIELD (a AND b)`.
- There is no `length`; the list-size function is `count`.
- A `DEONTIC` result cannot be the subject of an `#ASSERT` on this binary.
  The regulative twins (Schedule 1 paragraphs 3(1), 3A(1), 10(1)) are therefore run with `#TRACE` (six traces, in `ssc8-tests-sch1a.l4` and `ssc8-tests-sch1b.l4`), and the same duties are also decision functions, which carry the asserted answers.
  The trace outcomes, read from the output: paragraph 3(1) with the payment made is `FULFILLED`; each of the three prohibitions of 3A(1), when the act is done, is `BREACH` by the person with the reason given; with nothing done by time 5 the prohibition stays open (no breach, no fulfilment).

**Silent (a wrong answer with exit code 0):**
- **`Date d m y` with a day that the month does not have rolls forward.**
  Measured here on 1.6.98: `Date 30 2 2023` is 2 March 2023 and `Date 31 11 2023` is 1 December 2023, with no warning.
  Any rule that builds a date by adding months to a day-of-month would give a date that is too late.
  Schedule 1 paragraph 3B(12)'s three-month period is therefore built by a helper that clamps to the first day of the following month (`sch 1 para 3B(12) the day three months on`, with the helpers `the same day three months on` and `the day of the month three months on is in that month`).
- **`check.sh` is blind to trace outcomes.**
  It counts assertions, and its own footer says it does not see a different TRACE outcome.
  I compared the trace output of the two binaries by hand (byte-identical for `ssc8-tests-sch1a.l4` and `ssc8-tests-sch1b.l4`), but a future change that flips a trace would not turn the run red.

## What `check.sh` prints

Run as `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108, 2ae7c9b> ./check.sh` from this folder; exit status 0.  The output of the last run, unedited:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc8-cases-seat.l4                             0        64       0        0         0 |      0        64       0        0  same
ssc8-sch1a.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-sch1b.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-sch2.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-sch3.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-sch4.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-sch4a.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-sch4b.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-tests-sch1a.l4                            0       149       0        0         0 |      0       149       0        0  same
ssc8-tests-sch1b.l4                            0       132       0        0         0 |      0       132       0        0  same
ssc8-tests-sch2.l4                             0        73       0        0         0 |      0        73       0        0  same
ssc8-tests-sch3.l4                             0       172       0        0         0 |      0       172       0        0  same
ssc8-tests-sch4.l4                             0         8       0        0         0 |      0         8       0        0  same
ssc8-tests-sch4a.l4                            0        94       0        0         0 |      0        94       0        0  same
ssc8-tests-sch4b.l4                            0        53       0        0         0 |      0        53       0        0  same
TOTAL (17 modules)                             0       745       0        0           |      0       745       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Gates on the references: `python3 -I srcrefs.py check --refs <raw text> ssc8-*.l4` and the same with `--strict` both report 0 problems (numbers in PROGRESS.md).

Per-file runs were also grepped for `DiagnosticSeverity_Warning`, `is at the end of the file` and `follows code on its line`: none.
