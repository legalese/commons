# NOTES (roc5): Rules of Court 2021 (Singapore), G.N. No. S 914/2021, Orders 20 to 22

This file covers lines 2876 to 3555 of `inputs/SCJA1969-S914-2021.txt`: Order 20 (appeals from tribunals and case stated), Order 21 (costs, with Appendix 1, the fixed costs) and Order 22 (enforcement of judgments and orders).
It is one part's notes for a larger encoding of the Rules, and the lead merges it with the other parts' notes.

**Status, 5 November 2026, and how each claim below was checked.**
Every figure in this file was read from a run on 5 November 2026 and not from memory: `l4 run` on main 1.6.109 for each module (no `DiagnosticSeverity_Error` or `_Warning`), `check.sh` with the second main build 1.6.108 (output in "What check.sh prints"), `srcrefs.py check --refs` and `--strict` (output in the same section), and `work/build.py`, which builds the coverage table from the text and checks that every non-blank line of the range falls in some row.
The expected values in the test files were written from the text before the modules were run, and no expected value was edited to match the code, with one exception that is reported under "Seat": a scenario assertion in `roc5-cases-seat.l4` first expected `NOTHING`, failed, and was changed to `JUST FALSE` because the rule's opening words are "If no notice of objection is filed", an "if" that fails, which this encoding counts as the text's no (marginal reading (a) of the rule of 2026-10-29), and the first expectation had overlooked it; the layer-1 test for the same facts, written from the text first, already said `JUST FALSE`.
In the fix round of 5 November 2026, after an independent review, two expected values changed because the reading of the text changed, and the code changed with them (not the other way round): `o 22 r 12 ...` with an instalment order and no instalment due went from `JUST FALSE` to `NOTHING` (the review's reading of "that is due and unpaid" as a relative clause, fork F10), and `o 21 r 27(5) a person is a Judge in Rules 27 and 28` for `any other person` went from `NOTHING` to `JUST FALSE` (a "means" definition closes the list, fork F9).
The seat's cases for the same facts follow them.
No other expected value was edited in the fix round; every other change was an added assertion: the fix round added 33 assertions to the layer-1 test files (1057 to 1090) and 20 to the seat's cases (642 to 662); the counts are under "What check.sh prints" and "Seat".
Nothing in this encoding is a lawyer's reading: the two readings "for a lawyer" are listed under "Marginal readings for a lawyer (roc5)".

Paths that begin `work/` (the builder, the probes, the generators) are the part agent's scratch files and are not shipped with the row; they are named so that the lead can ask for them.

**The source.**
The text is a plain-text rendering made by a converter script from Singapore Statutes Online; it is not the official text, and nothing here has been verified against the official text.
`inputs/SOURCES.md` records where the file came from and its hashes.

## Files (roc5)

Layer 1, the law, objectively (every rule has a `-- src:` quote and an `@ref` locator, and a test):

| module | covers | tests |
| --- | --- | --- |
| `roc5-o20.l4` | Order 20, rules 1 to 7 | `roc5-tests-o20.l4` |
| `roc5-o21-general.l4` | Order 21, Division 1, rules 1 to 9 and 11 to 16 | `roc5-tests-o21-general.l4` |
| `roc5-o21-assessment.l4` | Order 21, Divisions 2 to 6, rules 17 to 29 | `roc5-tests-o21-assessment.l4` |
| `roc5-o21-appendix.l4` | Order 21, rule 10 and Appendix 1 (the fixed costs) | `roc5-tests-o21-appendix.l4` |
| `roc5-o22-order.l4` | Order 22, rules 1 to 5 | `roc5-tests-o22-order.l4` |
| `roc5-o22-sheriff.l4` | Order 22, rules 6 to 9 | `roc5-tests-o22-sheriff.l4` |
| `roc5-o22-objection.l4` | Order 22, rules 10 to 13 | `roc5-tests-o22-objection.l4` |

Layer 2, the seat: `roc5-seat.l4` and its cases `roc5-cases-seat.l4`.
The keel's `roc-core.l4`, `roc-definitions.l4`, `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` are the lead's and were not edited.

**Where this file departs from `inputs/PLAN.md`.**
PLAN.md (section 2, `inputs/PLAN.md:83`, and section 7 item 10) reads a stated period's outside as `NOTHING`; the brief's ruling of 2026-11-05 (a) makes it `JUST FALSE`, and the brief governs, so every period here answers `JUST FALSE` outside the period.
PLAN.md does not divide the part into modules; this part is seven modules, with Order 22, rules 6 to 13 split into two (`roc5-o22-sheriff.l4`, `roc5-o22-objection.l4`) because of size.

## Coverage (roc5)

One row for each unit of lines 2876 to 3555: an Order heading and title, a rule and its heading, a paragraph, a sub-paragraph, a sub-sub-paragraph, an Appendix 1 heading, part heading and paragraph, a defined term and a table row.
The units were counted by a script that reads the text (`work/units.py`), relabelled by hand in ten places where its labels disagreed with the text (the five Order 21, rule 1 terms, and sub-paragraphs (a), (b) and (b)(i) to (iii) of paragraph 8 of Appendix 1, which are paragraph 8(2) in the text), and extended by 15 rows the script did not see (seven table rows of Appendix 1, five defined terms, three rule headings); `work/units.json` holds the 464 the script gives and `work/units_extra.json` the 15.
**Audit counts: 464 units counted by the script + 15 added by hand = 479 rows in the final table; rows in the table before this work: 0 (the part started from an empty table); 0 units without a row; 0 non-blank lines of the range outside every row or block** (`work/build.py` prints `units counted: 479 rows: 479 ... unassigned: 0 uncovered nonblank lines: 0`).
One discrepancy is not explained: the log written at setup (`PROGRESS.md`) says the script counted 475 units, and the script as it stands today counts 464 (checked on 5 November 2026 by running it to a scratch file and comparing it with `work/units.json`: same count, the ten relabelled units differ in label only).
I did not trace the 11 units that the log's figure and today's differ by, and the count of 475 should not be relied on.
Dispositions: units counted 479; rows 479; encoded 396, fork 13, inert 70.
A row marked `fork F1`, `fork F2` or `fork F3` points at that entry of the fork register and at the rule that encodes the chosen reading (13 rows: Order 21, rules 5(2), 6(2) and 20(6) with their sub-paragraphs, and paragraph 2 of Appendix 1 with its sub-paragraphs).
F4 to F10 are modelling choices or readings added to the register so that a reader sees them, and the rules they affect are marked `encoded`, not `fork` (F7 and F8 add functions to rules that were already covered; F9 and F10 are readings of rules 27(5) and 12, whose rows are `encoded`).
There is no `repealed` or `deferred` row, and no unit of this range is blank or repealed in the text.
Every `inert` row is a heading, with reason 1 (not operative); there is no `inert` row of reason 2 or 3 in this range.
A form named in the text (Forms 39 and 40) is not a unit of its own; the content the rule requires of it is encoded (Order 22, rules 3 and 6).

| unit | line | kind | disposition | L4 name(s) / reason |
| --- | --- | --- | --- | --- |
| O 20 | 2876 | order heading | inert | reason 1: heading, not operative |
| O 20 title | 2877 | order title | inert | reason 1: heading, not operative |
| O 20 r 1 heading | 2878 | rule heading | inert | reason 1: heading, not operative |
| O 20 r 1 | 2879 | rule | encoded | roc5-o20.l4: `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 1(1) | 2879 | paragraph | encoded | roc5-o20.l4: `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 1(1)(a) | 2879 | sub-paragraph | encoded | roc5-o20.l4: `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 1(1)(b) | 2881 | sub-paragraph | encoded | roc5-o20.l4: `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 1(2) | 2884 | paragraph | encoded | roc5-o20.l4: `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 2 heading | 2885 | rule heading | inert | reason 1: heading, not operative |
| O 20 r 2 | 2886 | rule | encoded | roc5-o20.l4: `o 20 r 2 a document is part of the record of proceedings` |
| O 20 r 2 term record of proceedings | 2886 | defined term | encoded | roc5-o20.l4: `o 20 r 2 a document is part of the record of proceedings` |
| O 20 r 2 term tribunal | 2887 | defined term | encoded | roc5-o20.l4: `o 20 r 2 a body is a tribunal` |
| O 20 r 3 heading | 2888 | rule heading | inert | reason 1: heading, not operative |
| O 20 r 3 | 2889 | rule | encoded | roc5-o20.l4: `o 20 r 3(1) the appeal or application is brought in the way the rule requires`; `o 20 r 3(2) the period for filing and serving the originating application and the supporting affidavit` |
| O 20 r 3(1) | 2889 | paragraph | encoded | roc5-o20.l4: `o 20 r 3(1) the appeal or application is brought in the way the rule requires`; `o 20 r 3(2) the period for filing and serving the originating application and the supporting affidavit` |
| O 20 r 3(2) | 2889 | paragraph | encoded | roc5-o20.l4: `o 20 r 3(2) the originating application and affidavit are filed and served in time` |
| O 20 r 3(3) | 2890 | paragraph | encoded | roc5-o20.l4: `o 20 r 3(3) the affidavit states what the rule requires` |
| O 20 r 3(4) | 2891 | paragraph | encoded | roc5-o20.l4: `o 20 r 3(4) the affidavit must include the record of proceedings`; `o 20 r 3(5) the period for the affidavit in reply` |
| O 20 r 3(5) | 2892 | paragraph | encoded | roc5-o20.l4: `o 20 r 3(5) a party served must file and serve an affidavit in reply` |
| O 20 r 4 heading | 2893 | rule heading | inert | reason 1: heading, not operative |
| O 20 r 4 | 2894 | rule | encoded | roc5-o20.l4: `o 20 r 4(1) the parties attend a case conference in time` |
| O 20 r 4(1) | 2894 | paragraph | encoded | roc5-o20.l4: `o 20 r 4(1) the parties attend a case conference in time` |
| O 20 r 4(2) | 2894 | paragraph | encoded | roc5-o20.l4: `o 20 r 4(2) the Court must give the directions that are necessary` |
| O 20 r 5 heading | 2895 | rule heading | inert | reason 1: heading, not operative |
| O 20 r 5 | 2896 | rule | encoded | roc5-o20.l4: `o 20 r 5(1) the written submissions are filed and served in time`; `o 20 r 5(2) the page limit for each party or set of parties` |
| O 20 r 5(1) | 2896 | paragraph | encoded | roc5-o20.l4: `o 20 r 5(1) the written submissions are filed and served in time`; `o 20 r 5(2) the page limit for each party or set of parties` |
| O 20 r 5(2) | 2896 | paragraph | encoded | roc5-o20.l4: `o 20 r 5(2) the written submissions are within the page limit` |
| O 20 r 5(3) | 2897 | paragraph | encoded | roc5-o20.l4: `o 20 r 5(3) the Court may allow the page limit to be exceeded` |
| O 20 r 5(3)(a) | 2897 | sub-paragraph | encoded | roc5-o20.l4: `o 20 r 5(3) the Court may allow the page limit to be exceeded` |
| O 20 r 5(3)(b) | 2899 | sub-paragraph | encoded | roc5-o20.l4: `o 20 r 5(3) the Court may allow the page limit to be exceeded` |
| O 20 r 6 heading | 2901 | rule heading | inert | reason 1: heading, not operative |
| O 20 r 6 | 2902 | rule | encoded | roc5-o20.l4: `o 20 r 6 the appeal or application operates as a stay of enforcement of the tribunal's decision` |
| O 20 r 7 heading | 2903 | rule heading | inert | reason 1: heading, not operative |
| O 20 r 7 | 2904 | rule | encoded | roc5-o20.l4: `o 20 r 7(1) the Court hearing the appeal or application has the power` |
| O 20 r 7(1) | 2904 | paragraph | encoded | roc5-o20.l4: `o 20 r 7(1) the Court hearing the appeal or application has the power` |
| O 20 r 7(2) | 2904 | paragraph | encoded | roc5-o20.l4: `o 20 r 7(2) the Appellate Division or Court of Appeal has the power` |
| O 21 | 2905 | order heading | inert | reason 1: heading, not operative |
| O 21 title | 2906 | order title | inert | reason 1: heading, not operative |
| O 21 div 1 | 2907 | division heading | inert | reason 1: heading, not operative |
| O 21 r 1 heading | 2908 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 1 | 2909 | rule | encoded | roc5-o21-general.l4: `o 21 r 1(2) costs are assessed costs` |
| O 21 r 1(1) | 2909 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 1(1) this Order applies to the costs` |
| O 21 r 1(2) | 2909 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 1(2) costs are assessed costs` |
| O 21 r 1(2) term assessed costs | 2909 | defined term | encoded | roc5-o21-general.l4: `o 21 r 1(2) costs are assessed costs` |
| O 21 r 1(2) term contentious business | 2910 | defined term | encoded | roc5-o21-general.l4: `o 21 r 1(2) the business is contentious business`; `o 21 r 1(2) kind of charge` |
| O 21 r 1(2) term costs | 2911 | defined term | encoded | roc5-o21-general.l4: `o 21 r 1(2) a charge is within costs` |
| O 21 r 1(2) term indemnity basis | 2912 | defined term | encoded | roc5-o21-general.l4: `o 21 r 1(2) the basis is the indemnity basis` |
| O 21 r 1(2) term standard basis | 2913 | defined term | encoded | roc5-o21-general.l4: `o 21 r 1(2) the basis is the standard basis` |
| O 21 r 1(3) | 2914 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 1(3)(a) a reference to a fund includes a reference to the thing` |
| O 21 r 1(3)(a) | 2914 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 1(3)(a) a reference to a fund includes a reference to the thing` |
| O 21 r 1(3)(b) | 2916 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 1(3)(b) a reference to a fund held by a trustee or personal representative includes a reference to the thing` |
| O 21 r 2 heading | 2918 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 2 | 2919 | rule | encoded | roc5-o21-general.l4: `o 21 r 2(1) costs are in the discretion of the Court`; `o 21 r 2(2) circumstance` |
| O 21 r 2(1) | 2919 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(1) costs are in the discretion of the Court`; `o 21 r 2(2) circumstance` |
| O 21 r 2(2) | 2919 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(a) | 2919 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(b) | 2921 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(c) | 2923 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(d) | 2925 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(e) | 2927 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(f) | 2929 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(g) | 2931 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(2)(h) | 2933 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(3) | 2935 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(3) the costs must be fixed by the Court which heard the matter` |
| O 21 r 2(4) | 2936 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(4) the costs are payable from the date of the Court's order` |
| O 21 r 2(5) | 2937 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(5) the Court may order the parties' costs to be set off against one another` |
| O 21 r 2(6) | 2938 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(6) the Court may stay or dismiss the application, action or appeal or make any other order` |
| O 21 r 2(7) | 2939 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(7) the Court hearing the appeal may deal with the costs of the proceedings giving rise to the appeal and of the appeal` |
| O 21 r 2(8) | 2940 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 2(8) the General Division may decide the costs of the whole proceedings or direct the other court to decide the costs before the transfer` |
| O 21 r 3 heading | 2941 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 3 | 2942 | rule | encoded | roc5-o21-general.l4: `o 21 r 3(1) a party is entitled to recover costs from another party` |
| O 21 r 3(1) | 2942 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 3(1) a party is entitled to recover costs from another party` |
| O 21 r 3(2) | 2942 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 3(2) the Court must order the costs in favour of the successful party` |
| O 21 r 3(3) | 2943 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 3(3) the party making the amendment bears the costs of and occasioned by it` |
| O 21 r 3(4) | 2944 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 3(4) the party making the application bears the costs of and occasioned by it`; `o 21 r 3(5) capacity` |
| O 21 r 3(5) | 2945 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 3(5) the person is entitled to the costs out of the fund or the mortgaged property` |
| O 21 r 4 heading | 2946 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 4 | 2947 | rule | encoded | roc5-o21-general.l4: `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` |
| O 21 r 4(a) | 2947 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` |
| O 21 r 4(b) | 2949 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` |
| O 21 r 4(c) | 2951 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` |
| O 21 r 4(d) | 2953 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` |
| O 21 r 5 heading | 2955 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 5 | 2956 | rule | encoded | roc5-o21-general.l4: `o 21 r 5(1) the Court may order costs against the non-party` |
| O 21 r 5(1) | 2956 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 5(1) the Court may order costs against the non-party` |
| O 21 r 5(1)(a) | 2956 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 5(1) the Court may order costs against the non-party` |
| O 21 r 5(1)(b) | 2958 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 5(1) the Court may order costs against the non-party` |
| O 21 r 5(1)(c) | 2960 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 5(1) the Court may order costs against the non-party` |
| O 21 r 5(2) | 2962 | paragraph | fork F1 | roc5-o21-general.l4: `o 21 r 5(2) the Court must give the non-party a reasonable opportunity to be heard` |
| O 21 r 6 heading | 2963 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 6 | 2964 | rule | encoded | roc5-o21-general.l4: `o 21 r 6(1) the Court may make the order against the solicitor` |
| O 21 r 6(1) | 2964 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 6(1) the Court may make the order against the solicitor` |
| O 21 r 6(1)(a) | 2964 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 6(1) the Court may make the order against the solicitor` |
| O 21 r 6(1)(b) | 2966 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 6(1) the Court may make the order against the solicitor` |
| O 21 r 6(1)(c) | 2968 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 6(1) the Court may make the order against the solicitor` |
| O 21 r 6(2) | 2970 | paragraph | fork F1 | roc5-o21-general.l4: `o 21 r 6(2) the Court must give the solicitor a reasonable opportunity to be heard` |
| O 21 r 6(3) | 2971 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 6(3) the Court may direct that notice be given to the solicitor's client` |
| O 21 r 6(4) | 2972 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 6(4) the Court may direct or authorise the Attorney-General to attend and take part` |
| O 21 r 7 heading | 2973 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 7 | 2974 | rule | encoded | roc5-o21-general.l4: `o 21 r 7 the Court may award costs to the successful party not represented by solicitors`; `o 21 r 8 person for whom money is claimed` |
| O 21 r 8 heading | 2975 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 8 | 2976 | rule | encoded | roc5-o21-general.l4: `o 21 r 8 the costs payable by the claimant or the claimant's solicitor must be fixed or approved by the Court or assessed by the Registrar` |
| O 21 r 8(a) | 2976 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 8 the costs payable by the claimant or the claimant's solicitor must be fixed or approved by the Court or assessed by the Registrar` |
| O 21 r 8(b) | 2978 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 8 the costs payable by the claimant or the claimant's solicitor must be fixed or approved by the Court or assessed by the Registrar` |
| O 21 r 8(c) | 2980 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 8 the costs payable by the claimant or the claimant's solicitor must be fixed or approved by the Court or assessed by the Registrar` |
| O 21 r 9 heading | 2983 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 9 | 2984 | rule | encoded | roc5-o21-general.l4: `o 21 r 9(1) the defendant is entitled to the costs incurred to the time of discontinuance` |
| O 21 r 9(1) | 2984 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(1) the defendant is entitled to the costs incurred to the time of discontinuance` |
| O 21 r 9(1)(a) | 2984 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(1) the defendant is entitled to the costs incurred to the time of discontinuance` |
| O 21 r 9(1)(b) | 2986 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(1) the defendant is entitled to the costs incurred to the time of discontinuance` |
| O 21 r 9(2) | 2989 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(2) the claimant is entitled to the costs incurred to the time of receipt of the notice of payment into Court` |
| O 21 r 9(2)(a) | 2989 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(2) the claimant is entitled to the costs incurred to the time of receipt of the notice of payment into Court` |
| O 21 r 9(2)(b) | 2991 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(2) the claimant is entitled to the costs incurred to the time of receipt of the notice of payment into Court` |
| O 21 r 9(3) | 2993 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(3) the claimant may have the costs assessed and sign judgment against that defendant as in paragraph (2)` |
| O 21 r 9(4) | 2994 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(4) the claimant is entitled to have the costs assessed` |
| O 21 r 9(5) | 2995 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(5) the defendant is entitled to the costs of the counterclaim incurred to the time of receipt of the notice of acceptance` |
| O 21 r 9(5)(a) | 2995 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(5) the defendant is entitled to the costs of the counterclaim incurred to the time of receipt of the notice of acceptance` |
| O 21 r 9(5)(b) | 2997 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(5) the defendant is entitled to the costs of the counterclaim incurred to the time of receipt of the notice of acceptance` |
| O 21 r 9(6) | 2999 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 9(6) the defendant is entitled to have the costs of the counterclaim assessed` |
| O 21 r 10 heading | 3000 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 10 | 3001 | rule | encoded | roc5-o21-appendix.l4: `o 21 r 10 the amount of costs allowed is the amount set out in Appendix 1`; `o 21 app 1 court column`; `o 21 app 1 allowance`; `o 21 app 1 the column for the court level` |
| O 21 r 11 heading | 3002 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 11 | 3003 | rule | encoded | roc5-o21-general.l4: `o 21 r 11(1) the Registrar of the Supreme Court has power to assess the costs` |
| O 21 r 11(1) | 3003 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 11(1) the Registrar of the Supreme Court has power to assess the costs` |
| O 21 r 11(1)(a) | 3003 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 11(1) the Registrar of the Supreme Court has power to assess the costs` |
| O 21 r 11(1)(b) | 3005 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 11(1) the Registrar of the Supreme Court has power to assess the costs` |
| O 21 r 11(1)(c) | 3007 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 11(1) the Registrar of the Supreme Court has power to assess the costs` |
| O 21 r 11(2) | 3009 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 11(2) the Registrar of the State Courts has power to assess the costs`; `o 21 r 12 supplementary power` |
| O 21 r 11(2)(a) | 3009 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 11(2) the Registrar of the State Courts has power to assess the costs`; `o 21 r 12 supplementary power` |
| O 21 r 11(2)(b) | 3011 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 11(2) the Registrar of the State Courts has power to assess the costs`; `o 21 r 12 supplementary power` |
| O 21 r 12 heading | 3013 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 12 | 3014 | rule | encoded | roc5-o21-general.l4: `o 21 r 12 the Registrar may do the thing in assessing costs` |
| O 21 r 12(a) | 3014 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 12 the Registrar may do the thing in assessing costs` |
| O 21 r 12(b) | 3016 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 12 the Registrar may do the thing in assessing costs` |
| O 21 r 12(c) | 3018 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 12 the Registrar may do the thing in assessing costs` |
| O 21 r 12(d) | 3020 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 12 the Registrar may do the thing in assessing costs` |
| O 21 r 13 heading | 3022 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 13 | 3023 | rule | encoded | roc5-o21-general.l4: `o 21 r 13(1) the party is entitled to the costs of the assessment proceedings`; `o 21 r 13(2) the period for the offer` |
| O 21 r 13(1) | 3023 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 13(1) the party is entitled to the costs of the assessment proceedings`; `o 21 r 13(2) the period for the offer` |
| O 21 r 13(2) | 3023 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 13(2) the party liable may make the offer` |
| O 21 r 13(3) | 3024 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 13(3) the Registrar may take the offer into account` |
| O 21 r 14 heading | 3025 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 14 | 3026 | rule | encoded | roc5-o21-general.l4: `o 21 r 14(1) the Registrar may issue an interim certificate for the part assessed` |
| O 21 r 14(1) | 3026 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 14(1) the Registrar may issue an interim certificate for the part assessed` |
| O 21 r 14(2) | 3026 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 14(2) the Registrar may issue an interim certificate specifying an amount payable by the solicitor to the client` |
| O 21 r 14(3) | 3027 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 14(3) the Court may order the amount to be paid forthwith to the client or into Court` |
| O 21 r 15 heading | 3028 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 15 | 3029 | rule | encoded | roc5-o21-general.l4: `o 21 r 15 the Registrar may assess the costs the party is liable to pay and set them off, or delay the certificate` |
| O 21 r 15(a) | 3029 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 15 the Registrar may assess the costs the party is liable to pay and set them off, or delay the certificate` |
| O 21 r 15(b) | 3031 | sub-paragraph | encoded | roc5-o21-general.l4: `o 21 r 15 the Registrar may assess the costs the party is liable to pay and set them off, or delay the certificate` |
| O 21 r 16 heading | 3033 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 16 | 3034 | rule | encoded | roc5-o21-general.l4: `o 21 r 16(1) the Court may direct the Registrar to assess the costs, and the Registrar must do so` |
| O 21 r 16(1) | 3034 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 16(1) the Court may direct the Registrar to assess the costs, and the Registrar must do so` |
| O 21 r 16(2) | 3034 | paragraph | encoded | roc5-o21-general.l4: `o 21 r 16(2) the Registrar has the same powers, and the same fees are payable, as if the Court had made an order for assessment` |
| O 21 div 2 | 3035 | division heading | inert | reason 1: heading, not operative |
| O 21 r 17 heading | 3036 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 17 | 3037 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 17 the bill of costs is filed in time` |
| O 21 r 18 heading | 3038 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 18 | 3039 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 18 the Registrar's notice of the assessment is given in time` |
| O 21 r 19 heading | 3040 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 19 | 3041 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 19(1) the copy of the bill of costs is sent in time` |
| O 21 r 19(1) | 3041 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 19(1) the copy of the bill of costs is sent in time` |
| O 21 r 19(2) | 3041 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 19(2) notice need not be given to the party` |
| O 21 r 19(3) | 3042 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 19(3) paragraph (2) applies` |
| O 21 r 20 heading | 3043 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 20 | 3044 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 20(1) the bill of costs has the three separate sections` |
| O 21 r 20(1) | 3044 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(1) the bill of costs has the three separate sections` |
| O 21 r 20(1)(a) | 3044 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(1) the bill of costs has the three separate sections` |
| O 21 r 20(1)(b) | 3046 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(1) the bill of costs has the three separate sections` |
| O 21 r 20(1)(c) | 3048 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(1) the bill of costs has the three separate sections` |
| O 21 r 20(2) | 3050 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(2) the costs are indicated as the rule requires` |
| O 21 r 20(3) | 3051 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(3) the bill of costs sets out the goods and services tax` |
| O 21 r 20(4) | 3052 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(4) the bill of costs is headed as the rule requires` |
| O 21 r 20(5) | 3053 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 20(5) the bill of costs is endorsed as the rule requires` |
| O 21 r 20(6) | 3054 | paragraph | fork F2 | roc5-o21-assessment.l4: `o 21 r 20(6) the bill of costs for contentious business has the content the rule requires` |
| O 21 r 20(6)(a) | 3054 | sub-paragraph | fork F2 | roc5-o21-assessment.l4: `o 21 r 20(6) the bill of costs for contentious business has the content the rule requires` |
| O 21 r 20(6)(b) | 3056 | sub-paragraph | fork F2 | roc5-o21-assessment.l4: `o 21 r 20(6) the bill of costs for contentious business has the content the rule requires` |
| O 21 r 20(6)(c) | 3058 | sub-paragraph | fork F2 | roc5-o21-assessment.l4: `o 21 r 20(6) the bill of costs for contentious business has the content the rule requires` |
| O 21 r 20(6)(d) | 3060 | sub-paragraph | fork F2 | roc5-o21-assessment.l4: `o 21 r 20(6) the bill of costs for contentious business has the content the rule requires` |
| O 21 r 20(6)(e) | 3062 | sub-paragraph | fork F2 | roc5-o21-assessment.l4: `o 21 r 20(6)(e) the bill of costs may contain the lists of authorities cited` |
| O 21 r 20(6)(f) | 3064 | sub-paragraph | fork F2 | roc5-o21-assessment.l4: `o 21 r 20(6)(f) the work is work done in the cause or matter` |
| O 21 r 21 heading | 3066 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 21 | 3067 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 21(1) the Registrar may disallow the costs of the party's attendance` |
| O 21 r 21(1) | 3067 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 21(1) the Registrar may disallow the costs of the party's attendance` |
| O 21 r 21(2) | 3067 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 21(2) the Registrar may adjourn the assessment and direct the solicitor to send a copy of the bill` |
| O 21 r 21(2)(a) | 3067 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 21(2) the Registrar may adjourn the assessment and direct the solicitor to send a copy of the bill` |
| O 21 r 21(2)(b) | 3069 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 21(2) the Registrar may adjourn the assessment and direct the solicitor to send a copy of the bill` |
| O 21 r 21(2)(c) | 3071 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 21(2) the Registrar may adjourn the assessment and direct the solicitor to send a copy of the bill` |
| O 21 div 3 | 3073 | division heading | inert | reason 1: heading, not operative |
| O 21 r 22 heading | 3074 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 22 | 3075 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 22(1) the basis on which the amount of costs is allowed` |
| O 21 r 22(1) | 3075 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(1) the basis on which the amount of costs is allowed` |
| O 21 r 22(1)(a) | 3075 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(1) the basis on which the amount of costs is allowed` |
| O 21 r 22(1)(b) | 3077 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(1) the basis on which the amount of costs is allowed` |
| O 21 r 22(1)(c) | 3079 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(1) the basis on which the amount of costs is allowed` |
| O 21 r 22(2) | 3082 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(2) the basis is the standard basis` |
| O 21 r 22(2) term standard basis | 3082 | defined term | encoded | roc5-o21-assessment.l4: `o 21 r 22(2) the basis is the standard basis` |
| O 21 r 22(3) | 3083 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(3) the basis is the indemnity basis` |
| O 21 r 22(3) term indemnity basis | 3083 | defined term | encoded | roc5-o21-assessment.l4: `o 21 r 22(3) the basis is the indemnity basis` |
| O 21 r 22(4) | 3084 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(4) the basis on which the costs are to be assessed` |
| O 21 r 22(5) | 3085 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 22(5) the claimant is entitled to more costs than in a State Court` |
| O 21 r 23 heading | 3086 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 23 | 3087 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 23(2)(a) the costs are presumed to have been reasonably incurred` |
| O 21 r 23(1) | 3087 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(1) this Rule applies to the assessment` |
| O 21 r 23(2) | 3087 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(2)(a) the costs are presumed to have been reasonably incurred` |
| O 21 r 23(2)(a) | 3087 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(2)(a) the costs are presumed to have been reasonably incurred` |
| O 21 r 23(2)(b) | 3089 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(2)(b) the costs are presumed to have been reasonable in amount` |
| O 21 r 23(2)(c) | 3091 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(2)(c) the costs are presumed to have been unreasonably incurred`; `o 21 r 23(3) kind of client` |
| O 21 r 23(3) | 3093 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(3)(a) the representative acts, where necessary, with the authority of the Court` |
| O 21 r 23(3)(a) | 3093 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(3)(a) the representative acts, where necessary, with the authority of the Court` |
| O 21 r 23(3)(b) | 3095 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(3) references to the client are references to the litigation representative` |
| O 21 r 23(4) | 3097 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(4) delivery of a bill to the client precludes presenting a bill for a larger amount for assessment` |
| O 21 r 23(5) | 3098 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 23(5) the solicitor is entitled to the amount the Registrar allows` |
| O 21 r 24 heading | 3099 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 24 | 3100 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 24(1) this Rule applies to the assessment` |
| O 21 r 24(1) | 3100 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 24(1) this Rule applies to the assessment` |
| O 21 r 24(2) | 3100 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 24(2) the costs are assessed on the indemnity basis` |
| O 21 div 4 | 3101 | division heading | inert | reason 1: heading, not operative |
| O 21 r 25 heading | 3102 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 25 | 3103 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 25 the solicitor must apply for the certificate of the Registrar` |
| O 21 r 26 heading | 3104 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 26 | 3105 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 26 the certificate is conclusive as to the amount of costs allowed` |
| O 21 div 5 | 3106 | division heading | inert | reason 1: heading, not operative |
| O 21 r 27 heading | 3107 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 27 | 3108 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 27(1) the party may apply to a Judge to review the assessment as to the item`; `o 21 r 27(2) the period for applying for review` |
| O 21 r 27(1) | 3108 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 27(1) the party may apply to a Judge to review the assessment as to the item`; `o 21 r 27(2) the period for applying for review` |
| O 21 r 27(2) | 3108 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 27(2) the application for review is made in time` |
| O 21 r 27(3) | 3109 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 27(3) the application is made and heard as the rule requires` |
| O 21 r 27(4) | 3110 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 27(4) the application for review prejudices the Registrar's power to issue an interim certificate for the item`; `o 21 r 27(5) who sits` |
| O 21 r 27(5) | 3111 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 27(5) a person is a Judge in Rules 27 and 28` |
| O 21 r 27(5) term Judge | 3111 | defined term | encoded | roc5-o21-assessment.l4: `o 21 r 27(5) a person is a Judge in Rules 27 and 28` |
| O 21 r 28 heading | 3112 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 28 | 3113 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 28(1) further evidence may be received on the hearing of the review` |
| O 21 r 28(1) | 3113 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 28(1) further evidence may be received on the hearing of the review` |
| O 21 r 28(2) | 3113 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 28(2) the Judge may order the item to be remitted to the Registrar for assessment` |
| O 21 div 6 | 3114 | division heading | inert | reason 1: heading, not operative |
| O 21 r 29 heading | 3115 | rule heading | inert | reason 1: heading, not operative |
| O 21 r 29 | 3116 | rule | encoded | roc5-o21-assessment.l4: `o 21 r 29(1) the date from which the costs carry interest` |
| O 21 r 29(1) | 3116 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 29(1) the date from which the costs carry interest` |
| O 21 r 29(1)(a) | 3120 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 29(1) the date from which the costs carry interest` |
| O 21 r 29(1)(b) | 3123 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 29(1) the date from which the costs carry interest` |
| O 21 r 29(1)(c) | 3126 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 29(1) the date from which the costs carry interest` |
| O 21 r 29(1)(d) | 3129 | sub-paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 29(1) the date from which the costs carry interest` |
| O 21 r 29(2) | 3132 | paragraph | encoded | roc5-o21-assessment.l4: `o 21 r 29 the costs carry interest at the rate of 5.33% per year` |
| O 21 app 1 | 3133 | appendix heading | inert | reason 1: heading, not operative |
| O 21 app 1 heading | 3134 | appendix heading | inert | reason 1: heading, not operative |
| O 21 app 1 heading | 3135 | appendix heading | inert | reason 1: heading, not operative |
| O 21 app 1 part 1 | 3136 | appendix part heading | inert | reason 1: heading, not operative |
| O 21 app 1 para 1 | 3138 | appendix paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(1) | 3138 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(1)(a) | 3138 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(1)(b) | 3140 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(1)(c) | 3142 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(1)(c)(i) | 3143 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(1)(c)(ii) | 3145 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(1)(c)(iii) | 3147 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(2) | 3149 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 1(3) | 3150 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 1(3) the scale of costs and disbursements in both Parts 2 and 3 applies` |
| O 21 app 1 part 2 | 3151 | appendix part heading | inert | reason 1: heading, not operative |
| O 21 app 1 para 2 | 3153 | appendix paragraph | fork F3 | roc5-o21-appendix.l4: `o 21 app 1 para 2 the costs to be allowed excluding disbursements` |
| O 21 app 1 para 2(a) | 3157 | sub-paragraph | fork F3 | roc5-o21-appendix.l4: `o 21 app 1 para 2 the costs to be allowed excluding disbursements` |
| O 21 app 1 para 2(b) | 3162 | sub-paragraph | fork F3 | roc5-o21-appendix.l4: `o 21 app 1 para 2 the costs to be allowed excluding disbursements` |
| O 21 app 1 para 2(c) | 3167 | sub-paragraph | fork F3 | roc5-o21-appendix.l4: `o 21 app 1 para 2 the costs to be allowed excluding disbursements` |
| O 21 app 1 para 3 | 3177 | appendix paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(1) the costs for each additional defendant served` |
| O 21 app 1 para 3(1) | 3177 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(1) the costs for each additional defendant served` |
| O 21 app 1 para 3(1)(a) | 3178 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(1) the costs for each additional defendant served` |
| O 21 app 1 para 3(1)(b) | 3183 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(1) the costs for each additional defendant served` |
| O 21 app 1 para 3(2) | 3188 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(2) the costs for each defendant served by substituted service` |
| O 21 app 1 para 3(3) | 3192 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the costs for service out of Singapore` |
| O 21 app 1 para 3(3)(a) | 3201 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(3)(b) | 3206 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(3)(c) | 3211 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(3)(d) | 3216 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(3)(d)(i) | 3218 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(3)(d)(ii) | 3223 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(3)(e) | 3228 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(3)(f) | 3233 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(3) the disbursement to be allowed` |
| O 21 app 1 para 3(4) | 3238 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(4) the costs for the affidavit of service, including the search fee` |
| O 21 app 1 para 3(5) | 3242 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(5) the costs for the affidavit of service of the summons` |
| O 21 app 1 para 3(6) | 3246 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(6) the costs on an application by summons under Order 51, Rule 4` |
| O 21 app 1 para 3(7) | 3254 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(7) the costs for bankruptcy or winding up searches` |
| O 21 app 1 para 3(8) | 3258 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(8) the goods and services tax allowed` |
| O 21 app 1 para 3(9) | 3262 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 3(9) the costs for any other item approved by the Registrar` |
| O 21 app 1 part 3 | 3266 | appendix part heading | inert | reason 1: heading, not operative |
| O 21 app 1 para 4 | 3268 | appendix paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` |
| O 21 app 1 para 4(a) | 3273 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` |
| O 21 app 1 para 4(b) | 3278 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` |
| O 21 app 1 para 4(c) | 3283 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` |
| O 21 app 1 para 4(d) | 3288 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` |
| O 21 app 1 para 4(e) | 3293 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` |
| O 21 app 1 part 4 | 3298 | appendix part heading | inert | reason 1: heading, not operative |
| O 21 app 1 para 5 | 3300 | appendix paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 5 the costs of judgment` |
| O 21 app 1 para 5 table row costs of judgment | 3305 | table row | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 5 the costs of judgment` |
| O 21 app 1 para 6 | 3309 | appendix paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 para 6(a) | 3309 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 para 6(a)(i) | 3310 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 para 6(a)(ii) | 3312 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 para 6(a)(iii) | 3314 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 para 6(b) | 3316 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 para 6(c) | 3318 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 part 5 | 3320 | appendix part heading | inert | reason 1: heading, not operative |
| O 21 app 1 para 7 | 3322 | appendix paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 7(1) | 3322 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 7(1)(a) | 3322 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 7(1)(b) | 3324 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 7(1)(b)(i) | 3327 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 7(1)(b)(ii) | 3330 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 7(1)(b)(iii) | 3333 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 7(2) | 3336 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(2) the scales apply to the entire proceedings` |
| O 21 app 1 para 7(3) | 3337 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 7(3) the court awards such costs within the scales as it deems appropriate` |
| O 21 app 1 part 6 | 3338 | appendix part heading | inert | reason 1: heading, not operative |
| O 21 app 1 para 8 | 3340 | appendix paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(1) the action is a non-injury motor accident action` |
| O 21 app 1 para 8(1) | 3340 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(1) the action is a non-injury motor accident action` |
| O 21 app 1 para 8(2) | 3340 | appendix sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(2)(a) | 3340 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(1) term non-injury motor accident action | 3340 | defined term | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(1) the action is a non-injury motor accident action` |
| O 21 app 1 para 8(2)(a) table row any stage before defence is served | 3348 | table row | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(2)(a) table row where defence is served | 3352 | table row | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(2)(a) table row where defence to counterclaim is served | 3356 | table row | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(2)(a) table row where affidavits of evidence-in-chief are exchanged | 3360 | table row | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(2)(a) table row the 1st day of trial | 3364 | table row | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(2)(a) table row each subsequent day of trial | 3368 | table row | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(a) the costs for the stage and the sum`; `o 21 app 1 para 8(2)(b) when liability is resolved` |
| O 21 app 1 para 8(2)(b) | 3372 | sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(b) the percentage of the scale` |
| O 21 app 1 para 8(2)(b)(i) | 3373 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(b) the percentage of the scale` |
| O 21 app 1 para 8(2)(b)(ii) | 3375 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(b) the percentage of the scale` |
| O 21 app 1 para 8(2)(b)(iii) | 3377 | sub-sub-paragraph | encoded | roc5-o21-appendix.l4: `o 21 app 1 para 8(2)(b) the percentage of the scale` |
| O 22 | 3379 | order heading | inert | reason 1: heading, not operative |
| O 22 title | 3380 | order title | inert | reason 1: heading, not operative |
| O 22 r 1 heading | 3381 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 1 | 3382 | rule | encoded | roc5-o22-order.l4: `o 22 r 1 the component is within the amount due to the enforcement applicant`; `o 22 r 1 kind of Court order` |
| O 22 r 1 term amount due to the enforcement applicant | 3382 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the component is within the amount due to the enforcement applicant`; `o 22 r 1 kind of Court order` |
| O 22 r 1 term Court order | 3383 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the judgment or order is a Court order` |
| O 22 r 1 term enforcement applicant | 3384 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the person is an enforcement applicant`; `o 22 r 1 kind of enforcement cost` |
| O 22 r 1 term enforcement costs | 3385 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the cost is within the enforcement costs` |
| O 22 r 1 term enforcement order | 3386 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the order is an enforcement order` |
| O 22 r 1 term enforcement respondent | 3387 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the person is an enforcement respondent`; `o 22 r 1 kind of movable property` |
| O 22 r 1 term movable property | 3388 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the thing is movable property` |
| O 22 r 1 term non‑party | 3389 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the person is a non-party`; `o 22 r 1 kind of property` |
| O 22 r 1 term property | 3390 | defined term | encoded | roc5-o22-order.l4: `o 22 r 1 the thing is property` |
| O 22 r 2 heading | 3391 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 2 | 3392 | rule | encoded | roc5-o22-order.l4: `o 22 r 2(1) the person may apply for an enforcement order to enforce the Court orders` |
| O 22 r 2(1) | 3392 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(1) the person may apply for an enforcement order to enforce the Court orders` |
| O 22 r 2(2) | 3392 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(2) the enforcement order authorises the Sheriff to do the thing` |
| O 22 r 2(2)(a) | 3392 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(2) the enforcement order authorises the Sheriff to do the thing` |
| O 22 r 2(2)(b) | 3394 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(2) the enforcement order authorises the Sheriff to do the thing` |
| O 22 r 2(2)(c) | 3396 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(2)(c) the debt may be attached` |
| O 22 r 2(2)(d) | 3398 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(2) the enforcement order authorises the Sheriff to do the thing` |
| O 22 r 2(3) | 3400 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(3) the application is made in the way the rule provides` |
| O 22 r 2(4) | 3401 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(a) | 3401 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(b) | 3403 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(c) | 3405 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(d) | 3407 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(e) | 3409 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(f) | 3411 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(g) | 3413 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(h) | 3415 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(i) | 3417 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(j) | 3419 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(k) | 3421 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(l) | 3423 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(4)(m) | 3425 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4)(m) the affidavit states the undertaking and exhibits it as the rule requires`; `o 22 r 2(5) the period of validity of an enforcement order in the first instance` |
| O 22 r 2(4)(m)(i) | 3426 | sub-sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4)(m) the affidavit states the undertaking and exhibits it as the rule requires`; `o 22 r 2(5) the period of validity of an enforcement order in the first instance` |
| O 22 r 2(4)(m)(ii) | 3428 | sub-sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4)(m) the affidavit states the undertaking and exhibits it as the rule requires`; `o 22 r 2(5) the period of validity of an enforcement order in the first instance` |
| O 22 r 2(4)(m)(iii) | 3430 | sub-sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(4)(m) the affidavit states the undertaking and exhibits it as the rule requires`; `o 22 r 2(5) the period of validity of an enforcement order in the first instance` |
| O 22 r 2(5) | 3433 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(5) the enforcement order is valid in the first instance on the day`; `o 22 r 2(6) the period of each extension` |
| O 22 r 2(6) | 3434 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(6) the Court may extend the validity of the enforcement order` |
| O 22 r 2(7) | 3435 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(7) the date by reference to which the priority is determined` |
| O 22 r 2(8) | 3436 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(8) the enforcement order has ceased to be valid` |
| O 22 r 2(8)(a) | 3436 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(8) the enforcement order has ceased to be valid` |
| O 22 r 2(8)(b) | 3438 | sub-paragraph | encoded | roc5-o22-order.l4: `o 22 r 2(8) the enforcement order has ceased to be valid` |
| O 22 r 3 heading | 3440 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 3 | 3441 | rule | encoded | roc5-o22-order.l4: `o 22 r 3(1) the person may apply to the Court for satisfaction to be recorded` |
| O 22 r 3(1) | 3441 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 3(1) the person may apply to the Court for satisfaction to be recorded` |
| O 22 r 3(2) | 3441 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 3(2) the consent is attested as the rule requires` |
| O 22 r 4 heading | 3442 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 4 | 3443 | rule | encoded | roc5-o22-order.l4: `o 22 r 4 the payment or execution is a valid discharge of the non-party's liability to the enforcement respondent` |
| O 22 r 5 heading | 3444 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 5 | 3445 | rule | encoded | roc5-o22-order.l4: `o 22 r 5(1) the enforcement applicant is entitled to an enforcement order for attachment of debt in respect of the money` |
| O 22 r 5(1) | 3445 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 5(1) the enforcement applicant is entitled to an enforcement order for attachment of debt in respect of the money` |
| O 22 r 5(2) | 3445 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 5(2) the applicant must produce the summons at the office of the Accountant-General and leave a copy there` |
| O 22 r 5(3) | 3446 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 5(3) the applicant must give notice to the Accountant-General`; `o 22 r 5(4) the period before the hearing by which the summons must be served` |
| O 22 r 5(4) | 3447 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 5(4) the summons is served on the enforcement respondent in time` |
| O 22 r 5(5) | 3448 | paragraph | encoded | roc5-o22-order.l4: `o 22 r 5(5) the Court may make such order with respect to the money in Court as it thinks just` |
| O 22 r 6 heading | 3449 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 6 | 3450 | rule | encoded | roc5-o22-sheriff.l4: `o 22 r 6(1) the Sheriff must carry out the terms of the enforcement order in the sequence indicated` |
| O 22 r 6(1) | 3450 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(1) the Sheriff must carry out the terms of the enforcement order in the sequence indicated` |
| O 22 r 6(2) | 3450 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(2) the Sheriff may carry out the terms in any order and sequentially or concurrently` |
| O 22 r 6(3) | 3451 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(3) the enforcement applicant or its solicitor or other authorised representative must accompany the Sheriff`; `o 22 r 6(4) kind of enforcement order`; `o 22 r 6(4) step` |
| O 22 r 6(4) | 3452 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(a) | 3452 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(b) | 3454 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(b)(i) | 3455 | sub-sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(b)(ii) | 3457 | sub-sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(c) | 3459 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(d) | 3461 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(d)(i) | 3462 | sub-sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4)(d)(i) the enforcement order is registered in time` |
| O 22 r 6(4)(d)(ii) | 3464 | sub-sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(e) | 3466 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(f) | 3468 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(4)(g) | 3470 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(5) | 3472 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(5) the notice of seizure or attachment is in the form the rule requires` |
| O 22 r 6(6) | 3473 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(6) the copy of the notice is served on the enforcement respondent in time`; `o 22 r 6(7) method of service` |
| O 22 r 6(7) | 3474 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(7) the copy of the notice may be served on the enforcement respondent by the method`; `o 22 r 6(8) the costs the non-party may claim from the Sheriff`; `o 22 r 6(8) the period for claiming the costs` |
| O 22 r 6(8) | 3475 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(8) the non-party is entitled to claim costs from the Sheriff` |
| O 22 r 6(9) | 3476 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(9)(a) the non-party informs the Sheriff in time`; `o 22 r 6 party`; `o 22 r 6 act` |
| O 22 r 6(9)(a) | 3476 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(9)(a) the non-party informs the Sheriff in time`; `o 22 r 6 party`; `o 22 r 6 act` |
| O 22 r 6(9)(b) | 3478 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(9)(b)(ii) the bar on the non-party dealing with the attached amount`; `o 22 r 6(10) the period for handing or paying over` |
| O 22 r 6(9)(b)(i) | 3479 | sub-sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(9)(b) the non-party cannot yet deal with the attached amount` |
| O 22 r 6(9)(b)(ii) | 3481 | sub-sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(9)(b)(ii) the bar on the non-party dealing with the attached amount`; `o 22 r 6(10) the period for handing or paying over` |
| O 22 r 6(10) | 3483 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(10) the non-party hands or pays over in time` |
| O 22 r 6(10)(a) | 3483 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(10) the non-party hands or pays over in time` |
| O 22 r 6(10)(b) | 3485 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(10) the non-party hands or pays over in time` |
| O 22 r 6(11) | 3488 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 6(11) the Sheriff may engage, or direct the enforcement applicant to engage, the person` |
| O 22 r 7 heading | 3489 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 7 | 3490 | rule | encoded | roc5-o22-sheriff.l4: `o 22 r 7(1) the Sheriff may take steps to sell the seized movable property`; `o 22 r 7(2) the period before which the Sheriff may not take steps to sell` |
| O 22 r 7(1) | 3490 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(1) the Sheriff may take steps to sell the seized movable property`; `o 22 r 7(2) the period before which the Sheriff may not take steps to sell` |
| O 22 r 7(2) | 3490 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(2) the Sheriff may take steps to sell the seized immovable property` |
| O 22 r 7(3) | 3491 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(3) the Sheriff must decide the conditions of sale`; `o 22 r 7(4) the value up to which the Sheriff may conduct the sale` |
| O 22 r 7(4) | 3492 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(4) the sale may be conducted by the Sheriff and may be by private treaty or by public auction` |
| O 22 r 7(5) | 3493 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(5) the sale must be conducted by an auctioneer and by public auction`; `o 22 r 7(6) the period before the sale by which the notice of sale must be given` |
| O 22 r 7(6) | 3494 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(6) the notice of sale of seized property is given as the rule requires` |
| O 22 r 7(6)(a) | 3494 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(6) the notice of sale of seized property is given as the rule requires` |
| O 22 r 7(6)(b) | 3496 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(6) the notice of sale of seized property is given as the rule requires` |
| O 22 r 7(7) | 3499 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(7) the sale of immovable property is conducted as the rule requires`; `o 22 r 7(8) the period before the auction by which the notice must be advertised` |
| O 22 r 7(8) | 3500 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(8) the notice of sale of immovable property is advertised as the rule requires` |
| O 22 r 7(9) | 3501 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 7(9) the Sheriff may sign the documents in place of the enforcement respondent` |
| O 22 r 8 heading | 3502 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 8 | 3503 | rule | encoded | roc5-o22-sheriff.l4: `o 22 r 8(1) the Sheriff must deliver and give possession as soon as is practicable after seizure` |
| O 22 r 8(1) | 3503 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 8(1) the Sheriff must deliver and give possession as soon as is practicable after seizure` |
| O 22 r 8(2) | 3503 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 8(2) the enforcement applicant or its representative must sign the acknowledgment` |
| O 22 r 9 heading | 3504 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 9 | 3505 | rule | encoded | roc5-o22-sheriff.l4: `o 22 r 9(1) the Sheriff must keep proper records of the seized properties, attached debts and money received or expended`; `o 22 r 9(2) what the commission is of`; `o 22 r 9(2) the rate of the Sheriff's commission`; `o 22 r 9(2) the least commission` (+1) |
| O 22 r 9(1) | 3505 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(1) the Sheriff must keep proper records of the seized properties, attached debts and money received or expended`; `o 22 r 9(2) what the commission is of`; `o 22 r 9(2) the rate of the Sheriff's commission`; `o 22 r 9(2) the least commission` (+1) |
| O 22 r 9(2) | 3505 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(2) the Sheriff's commission` |
| O 22 r 9(2)(a) | 3505 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(2) the Sheriff's commission` |
| O 22 r 9(2)(b) | 3507 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(2) the Sheriff's commission` |
| O 22 r 9(2)(c) | 3509 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(2) the Sheriff's commission` |
| O 22 r 9(3) | 3512 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(3) the Sheriff's commission where the property is not sold` |
| O 22 r 9(4) | 3513 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(4) the statement of accounts must show the item` |
| O 22 r 9(4)(a) | 3513 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(4) the statement of accounts must show the item` |
| O 22 r 9(4)(b) | 3515 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(4) the statement of accounts must show the item` |
| O 22 r 9(4)(c) | 3517 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(4)(c) the amount of the landlord's claim to be shown` |
| O 22 r 9(4)(d) | 3519 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(4) the statement of accounts must show the item` |
| O 22 r 9(4)(e) | 3521 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(4) the statement of accounts must show the item` |
| O 22 r 9(4)(f) | 3523 | sub-paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(4) the statement of accounts must show the item` |
| O 22 r 9(5) | 3525 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(5) the position of the item in the order of priority of payments` |
| O 22 r 9(6) | 3526 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(6) the enforcement applicant must pay the amount of the shortfall to the Sheriff` |
| O 22 r 9(7) | 3527 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(7) the enforcement applicant is entitled to add the amount to the amount due as part of the enforcement costs` |
| O 22 r 9(8) | 3528 | paragraph | encoded | roc5-o22-sheriff.l4: `o 22 r 9(8) this Rule applies to the execution or sale` |
| O 22 r 10 heading | 3529 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 10 | 3530 | rule | encoded | roc5-o22-objection.l4: `o 22 r 10(1)(a) the objector gives notice of the objection to the Sheriff in time` |
| O 22 r 10(1) | 3530 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(1)(a) the objector gives notice of the objection to the Sheriff in time` |
| O 22 r 10(1)(a) | 3530 | sub-paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(1)(a) the objector gives notice of the objection to the Sheriff in time` |
| O 22 r 10(1)(b) | 3532 | sub-paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(1)(b) the objector serves a copy of the notice of objection in time and on the persons the rule names`; `o 22 r 10 party`; `o 22 r 10 act` |
| O 22 r 10(2) | 3534 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(2) the notice of objection has the contents the rule requires`; `o 22 r 10(3) the period for the enforcement applicant's notice of consent` |
| O 22 r 10(3) | 3535 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(3) the enforcement applicant must give notice that it consents to the release` |
| O 22 r 10(4) | 3536 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(4) the Sheriff may direct the objector to apply to the Court`; `o 22 r 10(5)(a) the period for applying to the Court` |
| O 22 r 10(5) | 3537 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(5)(a) the objector applies to the Court in time` |
| O 22 r 10(5)(a) | 3537 | sub-paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(5)(a) the objector applies to the Court in time` |
| O 22 r 10(5)(b) | 3539 | sub-paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(5)(b) the objector serves the summons and supporting affidavit in time and on the persons the rule names` |
| O 22 r 10(5)(c) | 3541 | sub-paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(5)(c) the objector gives notice to the Sheriff in time` |
| O 22 r 10(6) | 3543 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(6) the Sheriff may provide the information` |
| O 22 r 10(7) | 3544 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(7) the Sheriff may sell the property` |
| O 22 r 10(8) | 3545 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 10(8) the Sheriff may seek the Court's directions by letter at any time` |
| O 22 r 11 heading | 3546 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 11 | 3547 | rule | encoded | roc5-o22-objection.l4: `o 22 r 11(1) the enforcement applicant may apply for the enforcement respondent to be examined orally in court or to make an affidavit or both on the properties` |
| O 22 r 11(1) | 3547 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 11(1) the enforcement applicant may apply for the enforcement respondent to be examined orally in court or to make an affidavit or both on the properties` |
| O 22 r 11(2) | 3547 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 11(2) the Court may order the enforcement respondent to produce the documents` |
| O 22 r 11(3) | 3548 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 11(3) the order must state the appointment of the officers of the entity who are to be examined` |
| O 22 r 11(4) | 3549 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 11(4) the application is deemed to be enforcement of a Court order` |
| O 22 r 11(5) | 3550 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 11(5) the order is made and served as the rule requires` |
| O 22 r 12 heading | 3551 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 12 | 3552 | rule | encoded | roc5-o22-objection.l4: `o 22 r 12 the enforcement applicant may apply for an enforcement order in respect of the instalments due and unpaid` |
| O 22 r 13 heading | 3553 | rule heading | inert | reason 1: heading, not operative |
| O 22 r 13 | 3554 | rule | encoded | roc5-o22-objection.l4: `o 22 r 13(1) the party may apply for stay of enforcement or stay of the enforcement order`; `o 22 r 13(2) how long the stay lasts` |
| O 22 r 13(1) | 3554 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 13(1) the party may apply for stay of enforcement or stay of the enforcement order`; `o 22 r 13(2) how long the stay lasts` |
| O 22 r 13(2) | 3554 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 13(2) the Court may order a stay of enforcement or of an enforcement order for the duration`; `o 22 r 13(3) direction to the Sheriff` |
| O 22 r 13(3) | 3555 | paragraph | encoded | roc5-o22-objection.l4: `o 22 r 13(3) the order may give the direction to the Sheriff` |


## Judgment calls: the fork register (roc5)

The four rulings that bind this row, word for word as the brief prints them:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**How each was applied here.**
E1: no function gathers a legal effect by name from several sections; where a result is reached by several routes (the amount of costs allowed: Order 21, rules 10 and 22, and Appendix 1) each route is its own function, and I wrote no function that gathers them.
N2: a flat negative ("does not", "is not entitled", "must not") answers `JUST FALSE`; the kind (Hohfeld) is in the "Jural relations" table and is not typed into any answer.
Periods: 36 branches answer `JUST FALSE` outside a period the text fixes in its own words; each carries `[period, ruled 2026-11-05 (a)]`.
Checked in the fix round of 5 November 2026, by reading the code of every function that carries a `[period, ruled 2026-11-05 (a)]` branch and the tests of each: a day outside the stated period answers `JUST FALSE` in all of them, and none answers `NOTHING` merely because the act is outside the period.
The `NOTHING` branches in those functions rest on something else: the input that says the Court has otherwise ordered or directed (Order 20, rule 5(1); Order 21, rule 17; Order 22, rules 5(4) and 6(6)), a seam answer that is not known (Order 20, rule 4(1)), an entitlement that is not known (Order 21, rule 9(1), (2) and (5)), the day of payment not given (Order 21, rule 29(1)), or the scope "a non-party who is served with a notice of attachment" (Order 22, rule 6(8) and (9)(a)).
Order 20, rule 6 states no period and stays `NOTHING` where it did.
"Where": 35 branches answer `JUST FALSE` when a "where" condition fails; each carries `[where, ruled 2026-11-05 (b)]`.
Scope limits with no "only": 5 branches answer `NOTHING` outside the scope; each carries `[scope limit, ruled 2026-11-05 (c)]`.
4 are in `roc5-o21-appendix.l4` and carry the quoted words "In the case of a judgment pursuant to an application for summary judgment under Order 9, Rule 17" (paragraph 3(5)), "In the case of a judgment in default of a notice of intention to contest or not contest, or defence" (paragraph 3(6)), "in cases under paragraph 1(3) in Part 1 of this Appendix" (paragraph 4) and "Costs to be allowed in Magistrates' Courts cases" (paragraph 7(1)).
The 5th is in `roc5-o22-objection.l4`: `o 22 r 12 ...` answers `NOTHING` for an instalment order with no instalment yet due, on the words "in respect of an instalment that is due and unpaid" (fork F10).
"When", "upon" and "on" as "where": 7 branches (2 "when", 3 "upon", 2 "on"), each carrying `[... counts as where: delegated-definitions ruling (c) of 2026-11-05]`.
"Until" bars: 4 branches (Order 21, rule 13(2), in `o 21 r 13(2) the fact of the offer cannot yet be communicated to the Registrar`; Order 22, rule 5(2), in `o 22 r 5(2) the money cannot yet be paid out of Court`; Order 22, rule 6(9)(b), two branches in `o 22 r 6(9)(b) the non-party cannot yet deal with the attached amount`) are each their own yes/no function (`JUST TRUE` before the bar ends, `JUST FALSE` after), and each carries a comment naming the ruling (d) of 2026-11-05 ("until bar").
No function in this range claims that the thing "has happened".
Delegated definitions (ruling (a)) and defences (ruling (b)): this range has neither a definition handed to a list nor a defence "to prove that X", so rulings (a) and (b) were not applied.

**Forks this encoding took**, one entry each: the text, the readings seen, the one taken, and the text that licenses each.
Every entry is "assumed, not ruled"; a lawyer should look at F1 to F4 in particular.
F1 to F3 are readings of the text with different outcomes (the coverage rows say `fork F1` to `fork F3`); F4 to F6 are choices of how to model the text, and are recorded here with their other options for the same reason.
F7 to F10 were added in the fix round of 5 November 2026 after an independent review: F7 and F8 are modelling choices (new yes/no questions), F9 and F10 are readings of the text.

**F1.
"Before the Court makes an order under paragraph (1)" (Order 21, rules 5(2) and 6(2)).**
Reading taken: the duty to give a reasonable opportunity to be heard arises when the Court is about to make the order, so "before" is read as a "where" condition and, when the Court is not about to make the order, the function answers `JUST FALSE` (ruling (b)).
Other reading: "before" is a timing limit on a duty that exists whatever the Court is about to do, and outside it the text is silent (`NOTHING`).
Licence for the reading taken: "Before the Court makes an order under paragraph (1), the Court must give the non-party a reasonable opportunity to be heard" (line 2962).
Where it is in the code: `o 21 r 5(2) the Court must give the non-party a reasonable opportunity to be heard` and `o 21 r 6(2) the Court must give the solicitor a reasonable opportunity to be heard`, each with the tag `[before read as where: assumed, not ruled, recorded as a fork in NOTES.md]`.

**F2.
"For assessment of costs for contentious business" (Order 21, rule 20(6)).**
Reading taken: "for" introduces a "where"-type condition, so a bill of costs that is not for contentious business answers `JUST FALSE` (ruling (b)).
Other reading: it is a scope limit with no "only" (ruling (c)), so outside it the answer is `NOTHING`.
Licence for the reading taken: the paragraph opens "For assessment of costs for contentious business, the bill of costs must ..." (line 3054 to 3065), and the paragraphs before it state their requirements without a limit.
Where it is in the code: `o 21 r 20(6) the bill of costs for contentious business has the content the rule requires`, tagged `[for read as where: assumed, not ruled, recorded as a fork in NOTES.md]`.
The fix round added two functions inside the same opening words, and they take the same reading: `o 21 r 20(6)(e) the bill of costs may contain the lists of authorities cited` (a bill for contentious business: `JUST TRUE`) and `o 21 r 20(6)(f) the work is work done in the cause or matter` (work in connection with the negotiation of a settlement: `JUST TRUE`; other work: `NOTHING`, because "includes" does not close the list).
Outside contentious business both answer `JUST FALSE`, which for a permission and a definition reads oddly; if the other reading of F2 is preferred, those two branches and the one in `o 21 r 20(6) ...` change together.

**F3.
The Appendix 1 "High Court" column and the General Division (Appendix 1, Part 2 onwards).**
Reading taken: when the case is in the General Division, the Appendix's "High Court" column applies; the function `o 21 app 1 the column for the court level` maps `General Division` to the High Court column, `District Court` to the District Court column and `Magistrate's Court` to the Magistrate's Court column, and answers `NOTHING` for any other level.
Other reading: the column named "High Court" is read literally, with no mapping from the General Division, so a case in the General Division would be `NOTHING`.
Licence for the reading taken: the Rules' own definitions (Order 1, rule 3(1), in the keel) define "General Division" as the General Division of the High Court (`inputs/SCJA1969-S914-2021.txt:109`), and Appendix 1 has no column for it.
Where it is in the code: `roc5-o21-appendix.l4` (the comment above `o 21 app 1 the column for the court level`); the coverage rows for paragraph 2 are marked `fork F3` because it is the first place the column is used, and every later paragraph that calls the function takes the same reading.

**F4.
A sum cannot carry the text's no (Appendix 1 and Order 22, rule 9).**
The brief's ruling asks for a yes/no twin where the result is a number, a party or a date (assumed, not ruled).
Reading taken: the value function (for example `o 21 app 1 para 3(1) the costs for each additional defendant served`, or, since the fix round, `o 21 r 29(1) the interest on the costs for one year`) answers `NOTHING` outside its condition and the twin (`o 21 app 1 para 3(1) costs are allowed for the additional defendant`) answers `JUST FALSE`.
Departure from the brief's vocabulary: the `NOTHING-kind (<why>)` comment on those 14 value-function branches says `a sum cannot carry the no` (13) or `a number cannot carry the no` (1), which is not one of the six reasons the brief lists (silent, list not closed, includes, undefined term, points outside the text, limited by its own wording).
None of the six is true of them: the text does say no in its own words, and the result type has nowhere to put it.
Other reading: widen the `o 21 app 1 allowance` type with a constructor meaning "nothing is allowed" so that the value function carries the no itself; this was not done because the type is returned by 18 functions of `roc5-o21-appendix.l4`, whose generated tests would all change.

**F5.
The duties of Order 22 written as regulative rules and as decision functions.**
Rules 6(9)(a), 6(10), 10(1), 10(3) and 10(5) are each written twice: as a regulative rule (`PARTY ... MUST ... WITHIN ... LEST BREACH`), run by `#TRACE`, and as a decision function over the facts.
The 21-day bar of rule 6(9)(b)(ii) is written the same way: a regulative rule (`PARTY ... SHANT ... WITHIN 21 HENCE FULFILLED LEST BREACH`) examined by trace, as Meng's note on ruling (d) hopes, beside the yes/no function that the ruling asks for.
The two differ in one respect: a regulative rule counts a plain number of days from the moment the trace starts, and the decision function counts the period by Order 3, Rule 3 (an input, the last day).
The seat layer uses the decision function.
Reading taken: the regulative rule is a model of the duty and its consequence, not the counting rule.
Other reading: the regulative rule is the encoding and the decision function an aid; the code does not prefer one, and the text does not say.

**F6.
"Subject to any written law" and "subject to this Order" are not threaded as inputs.**
Reading taken: each function answers its own provision.
A phrase such as "unless the Court otherwise orders" or "unless the Court thinks fit to direct an assessment of the costs", which names a specific exception inside the rule, IS an input (11 such inputs in the range, under eight names, for example `the Court has ordered otherwise` and `the Court otherwise orders`).
Other reading: every function takes a `a written law provides otherwise` input, which would add one input to nearly every function of the range and answer nothing about any of them.
Licence: PLAN.md section 5 (seam S-L2) and the keel's `NOTES.md` take the same reading for the other parts, and nothing in the range supplies the written law.

**F7.
The indemnity basis as a yes/no question (Order 21, rules 22(1), 22(4), 23(2) and 24(2)).**
The gap found in review: no function answered "are the costs assessed on the indemnity basis?", so a Court order for that basis, and the two rules that deem it, could not be reached.
Four yes/no functions were added, each named "... the costs are assessed on the indemnity basis" and each answering its own provision (E1: none gathers the others).
`o 21 r 22(1) the costs are assessed on the indemnity basis` takes the Court's order as a fact (`the Court has ordered the costs to be assessed on the indemnity basis`): `JUST TRUE` when it has; `NOTHING` when it only "appears to the Court to be appropriate" (what the Court then does is not in the Rules); `NOTHING` outside (a), (b) and (c), where paragraph (1) says nothing about either basis; and otherwise `JUST FALSE`, because paragraph (1) puts the costs on the standard basis in those cases.
`o 21 r 22(4) the costs are assessed on the indemnity basis`: an order that "indicates the indemnity basis" gives `JUST TRUE`; an order that indicates no basis or another basis gives `JUST FALSE` ("the costs are to be assessed on the standard basis"); an order that indicates the standard basis gives `JUST FALSE` (paragraph (4) names "the standard basis or the indemnity basis" as alternatives).
`o 21 r 23(2) the costs are assessed on the indemnity basis` and `o 21 r 24(2) the costs are assessed on the indemnity basis`: `JUST TRUE` for an assessment to which the rule applies (the text deems the basis); `NOTHING` for any other assessment.
Reading taken (assumed, not ruled): the standard basis and the indemnity basis exclude each other, so a text that puts the costs on one answers `JUST FALSE` to the other; the `JUST FALSE` branches carry the tag `[the standard basis excludes the indemnity basis: assumed, not ruled, fork F7]`, because the text does not say "not" in those words.
Other reading for those branches: `NOTHING`, because paragraph (1) and paragraph (4) speak of the standard basis and do not mention the indemnity basis in the sentence that puts the costs on the standard basis.
A second choice inside F7: "On an assessment to which this Rule applies" in rules 23(2) and 24(2) is read as a scope limit, so another assessment answers `NOTHING`, and not as "on" counting as "where" under the delegated-definitions ruling (c), which would answer `JUST FALSE`; a `JUST FALSE` would say that no costs outside rule 23 are on the indemnity basis, and rule 22(1) says otherwise when the Court orders it.
Noticed, not changed: `o 21 r 23(5) the solicitor is entitled to the amount the Registrar allows` reads "Upon an assessment mentioned in paragraph (4)" the same way (`NOTHING`), so the ruling (c) reading of "upon" would change that one branch to `JUST FALSE`.
The older functions are unchanged: `o 21 r 22(1) the basis on which the amount of costs is allowed` and `o 21 r 22(4) the basis on which the costs are to be assessed` still answer `NOTHING` where the Court orders the indemnity basis, because they have no input for the order; `o 21 r 22(4) the costs are assessed on the standard basis` still answers `NOTHING` for an order that indicates the standard basis, where the new indemnity function answers `JUST FALSE` for the same facts.
`o 21 r 22(3)` needed nothing: `o 21 r 22(3) the basis is the indemnity basis` already answers for a basis it is given.

**F8.
Interest for one year (Order 21, rule 29(1)).**
The review asked for the interest on $10,000 for one year at 5.33%, which is $533; before the fix round only the rate, the commencement date and the running period were encoded.
`o 21 r 29(1) the interest on the costs for one year` gives the amount of the costs times the rate for the four types of costs in the table, and `NOTHING` for Part 4 costs and for other costs (the yes/no twin `o 21 r 29 the costs carry interest at the rate of 5.33% per year` says `JUST FALSE` for Part 4, as F4 describes).
Other reading: a function for any number of days.
None was written: the text says "5.33% per year ... until payment" and does not say whether the interest is simple or compound, how many days make a year, or how a part of a year is counted; the amount for one whole year is the one figure on which every such reading agrees.
A user who needs another period multiplies, or asks the court.

**F9.
"Judge" in Order 21, rules 27 and 28 is a closed definition (Order 21, rule 27(5)).**
Rule 27(5) says that "Judge" "means a Judge sitting in the General Division or a District Judge and includes a judge sitting in the Appellate Division or the Court of Appeal where appropriate".
Reading taken: "means" closes the list, and "includes" attaches only to the appeal judge, so a person who is none of the three is not a Judge for rules 27 and 28.
`o 21 r 27(5) a person is a Judge in Rules 27 and 28` therefore answers `JUST FALSE` for the new constructor `o 21 r 27(5) the Registrar` and for `o 21 r 27(5) any other person`; the second was `NOTHING` before the fix round and is the one other answer that moved with this item, because the Registrar is another person and the two cannot differ.
Each branch carries the tag `[means closes the list: assumed, not ruled, fork F9]`.
The branch for an appeal judge is unchanged: `JUST TRUE` where it is appropriate for that judge to act, `NOTHING` where the input says it is not.
Order 1, rule 3 (line 111 of the text, outside this range) defines "Judge" differently: it adds, "in cases where he or she is empowered to act", a Magistrate or the Registrar.
That definition is not in this range and is not mixed in; the answers here are for rules 27 and 28 only.
Other reading: "any other person" stays `NOTHING` because the word "includes" opens the list; not taken, because the "includes" is attached to the appeal judge alone.

**F10.
"that is due and unpaid" in Order 22, rule 12 is a relative clause, not a "where".**
The rule reads "Where a Court order made under section 43 of the State Courts Act or under any other written law provides for payment by instalments, the enforcement applicant may apply for an enforcement order in respect of an instalment that is due and unpaid or, if there are several instalments due and unpaid, in respect of those instalments".
Reading taken (the review's, agreed): "Where" governs the instalment-order clause only.
A case with no instalment order answers `JUST FALSE` (`[where, ruled 2026-11-05 (b)]`); an instalment order with an instalment due and unpaid answers `JUST TRUE`; an instalment order with no instalment yet due answers `NOTHING`, because "that is due and unpaid" says which instalments the applicant may apply for, has no "only", and so is a scope limit (`[scope limit, ruled 2026-11-05 (c)]`).
Before the fix round the last case answered `JUST FALSE` and cited (b) for the relative clause as well; the citation was wrong, and so was the answer.
Other reading: the whole second clause is a condition of the "where", so an instalment not yet due answers `JUST FALSE`.
Taken because a relative clause identifies the things the permission is about and does not condition it.
The function's inputs are unchanged (the instalment order exists; an instalment is due and unpaid); `an instalment is due and unpaid` is read only when the instalment order exists.

**Checked in the fix round, no change.**
- Order 21, Appendix 1, paragraphs 2(b) and 3(1)(b): no function adds the basic costs to the costs for the additional defendants (a District Court default judgment with two additional defendants: $1,800 plus two times $200 is $2,200).
  Reason: paragraph 2 and paragraph 3(1) are separate scales in separate Parts and each has its function (`o 21 app 1 para 2 the costs to be allowed excluding disbursements`, `o 21 app 1 para 3(1) the costs for each additional defendant served`); a total would be a function that gathers an effect from two provisions, which E1 declines, and it would have to add a sum to a range ("$4,000 to $15,000") and to an "up to" sum, which the text does not say how to do.
  The user multiplies the paragraph 3(1) amount by the number of additional defendants.
- Order 22, rule 2(4)(e): "more than 6 years have passed since the date of the Court order" stays a yes/no input.
  Reason: counting years is Order 3, Rule 3's work (seam S-T1, below), and this range never counts a period.
  The input name already says "more than", so a party at exactly six years answers no; the seat's description of the input now says so ("if exactly 6 years have passed, or fewer, answer no").
- The day of each period is an input (Order 3, Rule 3 counts it): see "Seams" below for the list of functions.

## Jural relations (roc5)

One row for each provision of lines 2876 to 3555 that is a paragraph (or a rule with no paragraphs, or an Appendix 1 paragraph).
The holder has the right (claim), privilege (liberty), power or immunity; the bearer has the correlative duty, no-right, liability or disability.
The kind is the Hohfeld kind of the relation as the text states it; it is recorded here and is not typed into any person-facing answer (ruling N2, 2026-11-04).
A provision that creates no relation (a definition, a counting rule, a rule of reading) is listed once as `none`.
Each relation is encoded once, as one relation between two parties (layer 1), and named neutrally; the seat layer asks it from the position of the party.

| provision | line | holder | bearer | kind | L4 rule(s) |
| --- | --- | --- | --- | --- | --- |
| O 20 r 1(1) | 2879 | none | none | none: scope of the Order | roc5-o20.l4 `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 1(2) | 2884 | none | none | none: scope of the Order (exclusion) | roc5-o20.l4 `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 2 | 2886 | none | none | none: definitions | roc5-o20.l4 `o 20 r 2 a document is part of the record of proceedings` |
| O 20 r 3(1) | 2889 | the Court; every party with an interest | the appellant or applicant | claim / duty (bring it by originating application supported by an affidavit) | roc5-o20.l4 `o 20 r 3(1) the appeal or application is brought in the way the rule requires`; `o 20 r 3(2) the period for filing and serving the originating application and the supporting affidavit` |
| O 20 r 3(2) | 2889 | the Court; every party with an interest in the matter | the appellant or applicant | claim / duty (file and serve within 14 days) | roc5-o20.l4 `o 20 r 3(2) the originating application and affidavit are filed and served in time` |
| O 20 r 3(3) | 2890 | the Court | the appellant or applicant | claim / duty (what the affidavit must state) | roc5-o20.l4 `o 20 r 3(3) the affidavit states what the rule requires` |
| O 20 r 3(4) | 2891 | the Court | the appellant or applicant | claim / duty (include the record of proceedings if available and necessary) | roc5-o20.l4 `o 20 r 3(4) the affidavit must include the record of proceedings`; `o 20 r 3(5) the period for the affidavit in reply` |
| O 20 r 3(5) | 2892 | the Court; the appellant or applicant | each party served | claim / duty (affidavit in reply within 21 days, if necessary) | roc5-o20.l4 `o 20 r 3(5) a party served must file and serve an affidavit in reply` |
| O 20 r 4(1) | 2894 | the Court | the parties | claim / duty (attend a case conference within 6 weeks) | roc5-o20.l4 `o 20 r 4(1) the parties attend a case conference in time` |
| O 20 r 4(2) | 2894 | the parties | the Court | claim / duty (the necessary directions at the case conference) | roc5-o20.l4 `o 20 r 4(2) the Court must give the directions that are necessary` |
| O 20 r 5(1) | 2896 | the Court; the other parties | each party | claim / duty (written submissions at least 14 days before the hearing, subject to Rule 4) | roc5-o20.l4 `o 20 r 5(1) the written submissions are filed and served in time`; `o 20 r 5(2) the page limit for each party or set of parties` |
| O 20 r 5(2) | 2896 | the Court; the other parties | each party or set of parties | claim / duty (35-page limit) | roc5-o20.l4 `o 20 r 5(2) the written submissions are within the page limit` |
| O 20 r 5(3) | 2897 | the Court | the party wishing to exceed the limit | power / liability (special circumstances and payment of fees) | roc5-o20.l4 `o 20 r 5(3) the Court may allow the page limit to be exceeded` |
| O 20 r 6 | 2902 | the party in whose favour the tribunal decided | the appellant or applicant | privilege / no-right (to a stay of enforcement); the Court or a written law may order otherwise: power / liability | roc5-o20.l4 `o 20 r 6 the appeal or application operates as a stay of enforcement of the tribunal's decision` |
| O 20 r 7(1) | 2904 | the Court hearing the appeal or application | the parties | power / liability (the powers of Order 19, Rule 7) | roc5-o20.l4 `o 20 r 7(1) the Court hearing the appeal or application has the power` |
| O 20 r 7(2) | 2904 | the Appellate Division or Court of Appeal | the parties | power / liability (the powers of Order 19, Rule 7) | roc5-o20.l4 `o 20 r 7(2) the Appellate Division or Court of Appeal has the power` |
| O 21 r 1(1) | 2909 | none | none | none: scope of the Order | roc5-o21-general.l4 `o 21 r 1(1) this Order applies to the costs` |
| O 21 r 1(2) | 2909 | none | none | none: definitions | roc5-o21-general.l4 `o 21 r 1(2) costs are assessed costs` |
| O 21 r 1(3) | 2914 | none | none | none: rule of reading ("fund") | roc5-o21-general.l4 `o 21 r 1(3)(a) a reference to a fund includes a reference to the thing` |
| O 21 r 2(1) | 2919 | the Court | the parties | power / liability (costs are in the Court's discretion) | roc5-o21-general.l4 `o 21 r 2(1) costs are in the discretion of the Court`; `o 21 r 2(2) circumstance` |
| O 21 r 2(2) | 2919 | the parties | the Court | claim / duty (have regard to the listed circumstances) | roc5-o21-general.l4 `o 21 r 2(2) the Court must have regard to the circumstance` |
| O 21 r 2(3) | 2935 | the parties | the Court | claim / duty (fix the costs after an oral hearing or written submissions) | roc5-o21-general.l4 `o 21 r 2(3) the costs must be fixed by the Court which heard the matter` |
| O 21 r 2(4) | 2936 | the party entitled to costs | the party ordered to pay | claim / duty (costs payable from the date of the order) | roc5-o21-general.l4 `o 21 r 2(4) the costs are payable from the date of the Court's order` |
| O 21 r 2(5) | 2937 | the Court | the parties | power / liability (set-off of costs) | roc5-o21-general.l4 `o 21 r 2(5) the Court may order the parties' costs to be set off against one another` |
| O 21 r 2(6) | 2938 | the Court | a party who refuses or neglects to pay costs ordered in time | power / liability (stay, dismissal or other order) | roc5-o21-general.l4 `o 21 r 2(6) the Court may stay or dismiss the application, action or appeal or make any other order` |
| O 21 r 2(7) | 2939 | the Court hearing the appeal | the parties | power / liability (costs of the proceedings below and of the appeal) | roc5-o21-general.l4 `o 21 r 2(7) the Court hearing the appeal may deal with the costs of the proceedings giving rise to the appeal and of the appeal` |
| O 21 r 2(8) | 2940 | the General Division | the parties | power / liability (decide the costs of the whole proceedings on transfer) | roc5-o21-general.l4 `o 21 r 2(8) the General Division may decide the costs of the whole proceedings or direct the other court to decide the costs before the transfer` |
| O 21 r 3(1) | 2942 | a party holding an order for costs, or entitled by a later provision | the other party | claim / duty; a party with neither has no-right to costs | roc5-o21-general.l4 `o 21 r 3(1) a party is entitled to recover costs from another party` |
| O 21 r 3(2) | 2942 | the successful party | the Court | claim / duty (costs follow the event, unless some other order should be made) | roc5-o21-general.l4 `o 21 r 3(2) the Court must order the costs in favour of the successful party` |
| O 21 r 3(3) | 2943 | the other parties | the party who amends without permission | claim / duty (bears the costs of and occasioned by the amendment) | roc5-o21-general.l4 `o 21 r 3(3) the party making the amendment bears the costs of and occasioned by it` |
| O 21 r 3(4) | 2944 | the other parties | the party who applies to extend time | claim / duty (bears the costs of and occasioned by the application) | roc5-o21-general.l4 `o 21 r 3(4) the party making the application bears the costs of and occasioned by it`; `o 21 r 3(5) capacity` |
| O 21 r 3(5) | 2945 | a trustee, personal representative or mortgagee who was a party | the fund or the mortgaged property, and the persons interested in it | claim / duty (costs out of the fund, insofar as not recovered elsewhere) | roc5-o21-general.l4 `o 21 r 3(5) the person is entitled to the costs out of the fund or the mortgaged property` |
| O 21 r 4 | 2947 | the Court | the successful party | power / liability (disallow or reduce costs, or order that party to pay) | roc5-o21-general.l4 `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` |
| O 21 r 5(1) | 2956 | the Court | a non-party | power / liability (costs against a non-party) | roc5-o21-general.l4 `o 21 r 5(1) the Court may order costs against the non-party` |
| O 21 r 5(2) | 2962 | the non-party | the Court | claim / duty (a reasonable opportunity to be heard) | roc5-o21-general.l4 `o 21 r 5(2) the Court must give the non-party a reasonable opportunity to be heard` |
| O 21 r 6(1) | 2964 | the Court | a solicitor | power / liability (disallow costs, repay or indemnify) | roc5-o21-general.l4 `o 21 r 6(1) the Court may make the order against the solicitor` |
| O 21 r 6(2) | 2970 | the solicitor | the Court | claim / duty (a reasonable opportunity to be heard) | roc5-o21-general.l4 `o 21 r 6(2) the Court must give the solicitor a reasonable opportunity to be heard` |
| O 21 r 6(3) | 2971 | the Court | the solicitor | power / liability (notice to the solicitor's client) | roc5-o21-general.l4 `o 21 r 6(3) the Court may direct that notice be given to the solicitor's client` |
| O 21 r 6(4) | 2972 | the Court | the Attorney-General | power / liability (attend and take part) | roc5-o21-general.l4 `o 21 r 6(4) the Court may direct or authorise the Attorney-General to attend and take part` |
| O 21 r 7 | 2974 | the Court | the party liable to pay costs to a successful party not represented by solicitors | power / liability | roc5-o21-general.l4 `o 21 r 7 the Court may award costs to the successful party not represented by solicitors`; `o 21 r 8 person for whom money is claimed` |
| O 21 r 8 | 2976 | the person who lacks capacity (a minor, a person lacking capacity, a widow under the Civil Law Act) | the claimant and the claimant's solicitor | claim / duty (costs payable must be fixed or approved by the Court or assessed by the Registrar) | roc5-o21-general.l4 `o 21 r 8 the costs payable by the claimant or the claimant's solicitor must be fixed or approved by the Court or assessed by the Registrar` |
| O 21 r 9(1) | 2984 | the defendant | the claimant | claim / duty (costs to the time of discontinuance); privilege / no-right (sign judgment for the assessed costs) | roc5-o21-general.l4 `o 21 r 9(1) the defendant is entitled to the costs incurred to the time of discontinuance` |
| O 21 r 9(2) | 2989 | the claimant | the defendant | claim / duty (costs to the time of receipt of the notice of payment into Court); privilege / no-right (sign judgment) | roc5-o21-general.l4 `o 21 r 9(2) the claimant is entitled to the costs incurred to the time of receipt of the notice of payment into Court` |
| O 21 r 9(3) | 2993 | the claimant | the defendant sued jointly in libel or slander | power / liability (assess and sign judgment against that defendant) | roc5-o21-general.l4 `o 21 r 9(3) the claimant may have the costs assessed and sign judgment against that defendant as in paragraph (2)` |
| O 21 r 9(4) | 2994 | the claimant | the defendant | claim / duty (to have the costs assessed) | roc5-o21-general.l4 `o 21 r 9(4) the claimant is entitled to have the costs assessed` |
| O 21 r 9(5) | 2995 | the defendant | the claimant | claim / duty (costs of the counterclaim); privilege / no-right (sign judgment) | roc5-o21-general.l4 `o 21 r 9(5) the defendant is entitled to the costs of the counterclaim incurred to the time of receipt of the notice of acceptance` |
| O 21 r 9(6) | 2999 | the defendant | the claimant | claim / duty (to have the costs of the counterclaim assessed) | roc5-o21-general.l4 `o 21 r 9(6) the defendant is entitled to have the costs of the counterclaim assessed` |
| O 21 r 10 | 3001 | the party entitled to costs | the party liable to pay | claim / duty (the amount set out in Appendix 1) | roc5-o21-appendix.l4 `o 21 r 10 the amount of costs allowed is the amount set out in Appendix 1`; `o 21 app 1 court column` (+2) |
| O 21 r 11(1) | 3003 | the Registrar of the Supreme Court | the parties to the assessment | power / liability (assess costs) | roc5-o21-general.l4 `o 21 r 11(1) the Registrar of the Supreme Court has power to assess the costs` |
| O 21 r 11(2) | 3009 | the Registrar of the State Courts | the parties to the assessment | power / liability (assess costs) | roc5-o21-general.l4 `o 21 r 11(2) the Registrar of the State Courts has power to assess the costs`; `o 21 r 12 supplementary power` |
| O 21 r 12 | 3014 | the Registrar | the parties and witnesses | power / liability (take accounts, require parties to be represented separately, examine witnesses, direct production of documents) | roc5-o21-general.l4 `o 21 r 12 the Registrar may do the thing in assessing costs` |
| O 21 r 13(1) | 3023 | the party whose bill is being assessed | the party liable to pay the costs | claim / duty (costs of the assessment proceedings) | roc5-o21-general.l4 `o 21 r 13(1) the party is entitled to the costs of the assessment proceedings`; `o 21 r 13(2) the period for the offer` |
| O 21 r 13(2) | 3023 | the party liable to pay | the other party | privilege / no-right (a written offer to pay a specific sum); the offer must not be communicated to the Registrar until the question of the costs of the assessment falls to be decided: claim / duty | roc5-o21-general.l4 `o 21 r 13(2) the party liable may make the offer` |
| O 21 r 13(3) | 3024 | the Registrar | the parties | power / liability (take the offer into account) | roc5-o21-general.l4 `o 21 r 13(3) the Registrar may take the offer into account` |
| O 21 r 14(1) | 3026 | the Registrar | the parties | power / liability (interim certificate for the part assessed) | roc5-o21-general.l4 `o 21 r 14(1) the Registrar may issue an interim certificate for the part assessed` |
| O 21 r 14(2) | 3026 | the Registrar | the solicitor | power / liability (interim certificate of an amount payable to the client) | roc5-o21-general.l4 `o 21 r 14(2) the Registrar may issue an interim certificate specifying an amount payable by the solicitor to the client` |
| O 21 r 14(3) | 3027 | the Court; the client | the solicitor | power / liability (payment forthwith to the client or into Court) | roc5-o21-general.l4 `o 21 r 14(3) the Court may order the amount to be paid forthwith to the client or into Court` |
| O 21 r 15 | 3029 | the Registrar | a party entitled to be paid costs and also liable to pay costs | power / liability (assess and set off, or delay the certificate) | roc5-o21-general.l4 `o 21 r 15 the Registrar may assess the costs the party is liable to pay and set them off, or delay the certificate` |
| O 21 r 16(1) | 3034 | the Court; the parties | the Registrar | power / liability (direct an assessment); claim / duty (the Registrar must do so) | roc5-o21-general.l4 `o 21 r 16(1) the Court may direct the Registrar to assess the costs, and the Registrar must do so` |
| O 21 r 16(2) | 3034 | the Registrar | the parties | power / liability (same powers and fees as on an order for assessment) | roc5-o21-general.l4 `o 21 r 16(2) the Registrar has the same powers, and the same fees are payable, as if the Court had made an order for assessment` |
| O 21 r 17 | 3037 | the Registrar; the party liable to pay | the party entitled to have costs assessed | claim / duty (file the bill within 12 months unless the Court orders otherwise) | roc5-o21-assessment.l4 `o 21 r 17 the bill of costs is filed in time` |
| O 21 r 18 | 3039 | the parties | the Registrar | claim / duty (notification of the time appointed for assessment) | roc5-o21-assessment.l4 `o 21 r 18 the Registrar's notice of the assessment is given in time` |
| O 21 r 19(1) | 3041 | each party entitled to be heard | the party who filed the bill | claim / duty (send a copy within the time) | roc5-o21-assessment.l4 `o 21 r 19(1) the copy of the bill of costs is sent in time` |
| O 21 r 19(2) | 3041 | the party who filed the bill | the party who would receive the copy | privilege / no-right (notice need not be given) | roc5-o21-assessment.l4 `o 21 r 19(2) notice need not be given to the party` |
| O 21 r 19(3) | 3042 | none | none | none: scope of paragraph (2) | roc5-o21-assessment.l4 `o 21 r 19(3) paragraph (2) applies` |
| O 21 r 20(1) | 3044 | the Registrar | the party presenting the bill | claim / duty (form of the bill of costs) | roc5-o21-assessment.l4 `o 21 r 20(1) the bill of costs has the three separate sections` |
| O 21 r 20(2) | 3050 | the Registrar | the party presenting the bill | claim / duty (form of the bill of costs) | roc5-o21-assessment.l4 `o 21 r 20(2) the costs are indicated as the rule requires` |
| O 21 r 20(3) | 3051 | the Registrar | the party presenting the bill | claim / duty (form of the bill of costs) | roc5-o21-assessment.l4 `o 21 r 20(3) the bill of costs sets out the goods and services tax` |
| O 21 r 20(4) | 3052 | the Registrar | the party presenting the bill | claim / duty (form of the bill of costs) | roc5-o21-assessment.l4 `o 21 r 20(4) the bill of costs is headed as the rule requires` |
| O 21 r 20(5) | 3053 | the Registrar | the party presenting the bill | claim / duty (form of the bill of costs) | roc5-o21-assessment.l4 `o 21 r 20(5) the bill of costs is endorsed as the rule requires` |
| O 21 r 20(6) | 3054 | the Registrar | the party presenting the bill | claim / duty (form of the bill of costs) | roc5-o21-assessment.l4 `o 21 r 20(6) the bill of costs for contentious business has the content the rule requires` |
| O 21 r 21(1) | 3067 | the Registrar | the party whose attendance is in question | power / liability (disallow the costs of attendance) | roc5-o21-assessment.l4 `o 21 r 21(1) the Registrar may disallow the costs of the party's attendance` |
| O 21 r 21(2) | 3067 | the Registrar | the solicitor | power / liability (adjourn and direct a copy of the bill to be sent) | roc5-o21-assessment.l4 `o 21 r 21(2) the Registrar may adjourn the assessment and direct the solicitor to send a copy of the bill` |
| O 21 r 22(1) | 3075 | none | none | none: measure of the amount (the basis on which costs are allowed) | roc5-o21-assessment.l4 `o 21 r 22(1) the basis on which the amount of costs is allowed` |
| O 21 r 22(2) | 3082 | none | none | none: definition (standard basis) | roc5-o21-assessment.l4 `o 21 r 22(2) the basis is the standard basis` |
| O 21 r 22(3) | 3083 | none | none | none: definition (indemnity basis) | roc5-o21-assessment.l4 `o 21 r 22(3) the basis is the indemnity basis` |
| O 21 r 22(4) | 3084 | none | none | none: rule of construction (which basis an order means) | roc5-o21-assessment.l4 `o 21 r 22(4) the basis on which the costs are to be assessed` |
| O 21 r 22(5) | 3085 | the paying party | a claimant who sued in the General Division what a State Court could have heard | immunity / disability (no more than State Court costs) | roc5-o21-assessment.l4 `o 21 r 22(5) the claimant is entitled to more costs than in a State Court` |
| O 21 r 23(1) | 3087 | none | none | none: scope of the Rule | roc5-o21-assessment.l4 `o 21 r 23(1) this Rule applies to the assessment` |
| O 21 r 23(2) | 3087 | none | none | none: rebuttable presumptions (evidence) | roc5-o21-assessment.l4 `o 21 r 23(2)(a) the costs are presumed to have been reasonably incurred` |
| O 21 r 23(3) | 3093 | none | none | none: rule of reading ("client") | roc5-o21-assessment.l4 `o 21 r 23(3)(a) the representative acts, where necessary, with the authority of the Court` |
| O 21 r 23(4) | 3097 | the client | the solicitor | immunity / disability (a bill delivered cannot be followed by a larger bill for assessment) | roc5-o21-assessment.l4 `o 21 r 23(4) delivery of a bill to the client precludes presenting a bill for a larger amount for assessment` |
| O 21 r 23(5) | 3098 | the solicitor | the client | claim / duty (the amount the Registrar allows) | roc5-o21-assessment.l4 `o 21 r 23(5) the solicitor is entitled to the amount the Registrar allows` |
| O 21 r 24(1) | 3100 | none | none | none: scope of the Rule | roc5-o21-assessment.l4 `o 21 r 24(1) this Rule applies to the assessment` |
| O 21 r 24(2) | 3100 | none | none | none: rebuttable presumption (evidence) | roc5-o21-assessment.l4 `o 21 r 24(2) the costs are assessed on the indemnity basis` |
| O 21 r 25 | 3103 | the Registrar | the solicitor | claim / duty (apply for the certificate) | roc5-o21-assessment.l4 `o 21 r 25 the solicitor must apply for the certificate of the Registrar` |
| O 21 r 26 | 3105 | the party entitled to the costs allowed | the party liable to pay | claim / duty (the certificate is conclusive); power / liability (apply for an enforcement order) | roc5-o21-assessment.l4 `o 21 r 26 the certificate is conclusive as to the amount of costs allowed` |
| O 21 r 27(1) | 3108 | a party dissatisfied with the Registrar's decision | the other parties | power / liability (apply to a Judge for review of an item) | roc5-o21-assessment.l4 `o 21 r 27(1) the party may apply to a Judge to review the assessment as to the item`; `o 21 r 27(2) the period for applying for review` |
| O 21 r 27(2) | 3108 | a party dissatisfied with the Registrar's decision | the other parties | power / liability (within 14 days after the decision) | roc5-o21-assessment.l4 `o 21 r 27(2) the application for review is made in time` |
| O 21 r 27(3) | 3109 | the Court | the applicant for review | claim / duty (the way the application is made and heard) | roc5-o21-assessment.l4 `o 21 r 27(3) the application is made and heard as the rule requires` |
| O 21 r 27(4) | 3110 | none | none | none: saving (the Registrar's power to issue an interim certificate is not prejudiced) | roc5-o21-assessment.l4 `o 21 r 27(4) the application for review prejudices the Registrar's power to issue an interim certificate for the item`; `o 21 r 27(5) who sits` |
| O 21 r 27(5) | 3111 | none | none | none: definition ("Judge") | roc5-o21-assessment.l4 `o 21 r 27(5) a person is a Judge in Rules 27 and 28` |
| O 21 r 28(1) | 3113 | the Judge | the parties | power / liability (receive further evidence on the review) | roc5-o21-assessment.l4 `o 21 r 28(1) further evidence may be received on the hearing of the review` |
| O 21 r 28(2) | 3113 | the Judge | the Registrar and the parties | power / liability (remit the item for assessment) | roc5-o21-assessment.l4 `o 21 r 28(2) the Judge may order the item to be remitted to the Registrar for assessment` |
| O 21 r 29(1) | 3116 | the party entitled to the costs | the party liable to pay | claim / duty (interest at 5.33% a year from the stated date until payment) | roc5-o21-assessment.l4 `o 21 r 29(1) the date from which the costs carry interest` |
| O 21 r 29(2) | 3132 | the party liable to pay costs under Part 4 of Appendix 1 | the party entitled to them | immunity / disability (no interest on Part 4 costs) | roc5-o21-assessment.l4 `o 21 r 29 the costs carry interest at the rate of 5.33% per year` |
| O 21 app 1 para 1 | 3138 | none | none | none: which scale applies | roc5-o21-appendix.l4 `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 app 1 para 2 | 3153 | the party entitled to costs | the party liable to pay | claim / duty (costs excluding disbursements by court and case) | roc5-o21-appendix.l4 `o 21 app 1 para 2 the costs to be allowed excluding disbursements` |
| O 21 app 1 para 3 | 3177 | the party entitled to costs | the party liable to pay | claim / duty (costs and disbursements for service, searches, tax and other items) | roc5-o21-appendix.l4 `o 21 app 1 para 3(1) the costs for each additional defendant served` |
| O 21 app 1 para 4 | 3268 | the party entitled to costs | the party liable to pay | claim / duty (disbursements in addition to the Part 2 items) | roc5-o21-appendix.l4 `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` |
| O 21 app 1 para 5 | 3300 | the party entitled to costs | the party liable to pay | claim / duty (costs of judgment) | roc5-o21-appendix.l4 `o 21 app 1 para 5 the costs of judgment` |
| O 21 app 1 para 6 | 3309 | the enforcement applicant | the enforcement respondent | claim / duty (costs allowed to the enforcement applicant) | roc5-o21-appendix.l4 `o 21 app 1 para 6 the costs to be allowed to the enforcement applicant` |
| O 21 app 1 para 7 | 3322 | the party entitled to costs | the party liable to pay | claim / duty (costs within the scales); the Court awards such costs within the scales as it deems appropriate: power / liability | roc5-o21-appendix.l4 `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` |
| O 21 app 1 para 8 | 3340 | the party entitled to costs | the party liable to pay | claim / duty (non-injury motor accident actions: the scale or a percentage of it) | roc5-o21-appendix.l4 `o 21 app 1 para 8(1) the action is a non-injury motor accident action` |
| O 22 r 1 | 3382 | none | none | none: definitions | roc5-o22-order.l4 `o 22 r 1 the component is within the amount due to the enforcement applicant`; `o 22 r 1 kind of Court order` |
| O 22 r 2(1) | 3392 | the enforcement applicant | the enforcement respondent | power / liability (apply for an enforcement order); privilege / no-right (other methods of enforcement remain open) | roc5-o22-order.l4 `o 22 r 2(1) the person may apply for an enforcement order to enforce the Court orders` |
| O 22 r 2(2) | 3392 | the Sheriff | the enforcement respondent and any non-party | power / liability (seize and sell, deliver or give possession, attach a debt, do what the Court order specifies) | roc5-o22-order.l4 `o 22 r 2(2) the enforcement order authorises the Sheriff to do the thing` |
| O 22 r 2(3) | 3400 | the Court | the enforcement applicant | claim / duty (how and when the application is made) | roc5-o22-order.l4 `o 22 r 2(3) the application is made in the way the rule provides` |
| O 22 r 2(4) | 3401 | the Court | the enforcement applicant | claim / duty (what the supporting affidavit must state) | roc5-o22-order.l4 `o 22 r 2(4) the affidavit must state the item` |
| O 22 r 2(5) | 3433 | the enforcement applicant | the enforcement respondent | power / liability (an enforcement order valid for 12 months from the date of issue) | roc5-o22-order.l4 `o 22 r 2(5) the enforcement order is valid in the first instance on the day`; `o 22 r 2(6) the period of each extension` |
| O 22 r 2(6) | 3434 | the Court | the enforcement respondent | power / liability (extend the validity for 12 months at a time, on an application made before expiry) | roc5-o22-order.l4 `o 22 r 2(6) the Court may extend the validity of the enforcement order` |
| O 22 r 2(7) | 3435 | the enforcement applicant | competing claimants | immunity / disability (priority keeps its original date) | roc5-o22-order.l4 `o 22 r 2(7) the date by reference to which the priority is determined` |
| O 22 r 2(8) | 3436 | the enforcement respondent | the enforcement applicant | immunity / disability (the order ceases to be valid) | roc5-o22-order.l4 `o 22 r 2(8) the enforcement order has ceased to be valid` |
| O 22 r 3(1) | 3441 | a person who has satisfied a judgment debt | the judgment creditor and the Court | power / liability (apply, with the creditor's consent, for satisfaction to be recorded) | roc5-o22-order.l4 `o 22 r 3(1) the person may apply to the Court for satisfaction to be recorded` |
| O 22 r 3(2) | 3441 | the Court | the person applying | claim / duty (the consent is attested) | roc5-o22-order.l4 `o 22 r 3(2) the consent is attested as the rule requires` |
| O 22 r 4 | 3443 | the non-party | the enforcement respondent and the enforcement applicant | immunity / disability (payment or execution is a valid discharge) | roc5-o22-order.l4 `o 22 r 4 the payment or execution is a valid discharge of the non-party's liability to the enforcement respondent` |
| O 22 r 5(1) | 3445 | the enforcement applicant | the enforcement respondent | power / liability (apply by summons for money in Court) | roc5-o22-order.l4 `o 22 r 5(1) the enforcement applicant is entitled to an enforcement order for attachment of debt in respect of the money` |
| O 22 r 5(2) | 3445 | the Accountant-General | the enforcement applicant | claim / duty (produce the summons and leave a copy) | roc5-o22-order.l4 `o 22 r 5(2) the applicant must produce the summons at the office of the Accountant-General and leave a copy there` |
| O 22 r 5(3) | 3446 | the Accountant-General | the enforcement applicant | claim / duty (notice if the application is dismissed) | roc5-o22-order.l4 `o 22 r 5(3) the applicant must give notice to the Accountant-General`; `o 22 r 5(4) the period before the hearing by which the summons must be served` |
| O 22 r 5(4) | 3447 | the enforcement respondent | the enforcement applicant | claim / duty (service of the summons in time) | roc5-o22-order.l4 `o 22 r 5(4) the summons is served on the enforcement respondent in time` |
| O 22 r 5(5) | 3448 | the Court | the parties | power / liability (such order about the money in Court as it thinks just) | roc5-o22-order.l4 `o 22 r 5(5) the Court may make such order with respect to the money in Court as it thinks just` |
| O 22 r 6(1) | 3450 | the enforcement applicant; the Court | the Sheriff | claim / duty (carry out the order in the sequence indicated); the Sheriff: power / liability (time, place and manner) | roc5-o22-sheriff.l4 `o 22 r 6(1) the Sheriff must carry out the terms of the enforcement order in the sequence indicated` |
| O 22 r 6(2) | 3450 | the Sheriff | the enforcement applicant | privilege / no-right (any order, sequentially or concurrently, if no sequence is indicated) | roc5-o22-sheriff.l4 `o 22 r 6(2) the Sheriff may carry out the terms in any order and sequentially or concurrently` |
| O 22 r 6(3) | 3451 | the Sheriff | the enforcement applicant | claim / duty (accompany the Sheriff) | roc5-o22-sheriff.l4 `o 22 r 6(3) the enforcement applicant or its solicitor or other authorised representative must accompany the Sheriff`; `o 22 r 6(4) kind of enforcement order` (+1) |
| O 22 r 6(4) | 3452 | the Sheriff | the enforcement respondent and any non-party | power / liability (the steps for each kind of order) | roc5-o22-sheriff.l4 `o 22 r 6(4) the Sheriff carries out the enforcement order by the step`; `o 22 r 6(4)(d)(i) the period for registering the enforcement order` |
| O 22 r 6(5) | 3472 | the Sheriff | the person preparing the notice | claim / duty (the notice is in Form 40) | roc5-o22-sheriff.l4 `o 22 r 6(5) the notice of seizure or attachment is in the form the rule requires` |
| O 22 r 6(6) | 3473 | the enforcement respondent | the Sheriff | claim / duty (a copy of the notice served in time) | roc5-o22-sheriff.l4 `o 22 r 6(6) the copy of the notice is served on the enforcement respondent in time`; `o 22 r 6(7) method of service` |
| O 22 r 6(7) | 3474 | the Sheriff | the enforcement respondent | privilege / no-right (the methods of service in addition to Order 7) | roc5-o22-sheriff.l4 `o 22 r 6(7) the copy of the notice may be served on the enforcement respondent by the method`; `o 22 r 6(8) the costs the non-party may claim from the Sheriff` (+1) |
| O 22 r 6(8) | 3475 | the non-party | the Sheriff | claim / duty (costs of complying); the non-party: privilege / no-right (deduct them from the debt) | roc5-o22-sheriff.l4 `o 22 r 6(8) the non-party is entitled to claim costs from the Sheriff` |
| O 22 r 6(9) | 3476 | the Sheriff | the non-party served with a notice of attachment | claim / duty (inform the Sheriff within 14 days; do not deal with the attached amount until the bar ends) | roc5-o22-sheriff.l4 `o 22 r 6(9)(a) the non-party informs the Sheriff in time`; `o 22 r 6 party` (+1) |
| O 22 r 6(10) | 3483 | the enforcement applicant; the Sheriff | the non-party | claim / duty (hand or pay over the money and the commission within 7 days after the bar ends) | roc5-o22-sheriff.l4 `o 22 r 6(10) the non-party hands or pays over in time` |
| O 22 r 6(11) | 3488 | the Sheriff | the enforcement applicant | power / liability (engage, or direct the engagement of, assisting persons) | roc5-o22-sheriff.l4 `o 22 r 6(11) the Sheriff may engage, or direct the enforcement applicant to engage, the person` |
| O 22 r 7(1) | 3490 | the Sheriff | the enforcement respondent | power / liability (take steps to sell seized movable property) | roc5-o22-sheriff.l4 `o 22 r 7(1) the Sheriff may take steps to sell the seized movable property`; `o 22 r 7(2) the period before which the Sheriff may not take steps to sell` |
| O 22 r 7(2) | 3490 | the Sheriff | the enforcement respondent | power / liability (take steps to sell seized immovable property) | roc5-o22-sheriff.l4 `o 22 r 7(2) the Sheriff may take steps to sell the seized immovable property` |
| O 22 r 7(3) | 3491 | the Sheriff | the enforcement respondent | power / liability (decide the conditions of sale) | roc5-o22-sheriff.l4 `o 22 r 7(3) the Sheriff must decide the conditions of sale`; `o 22 r 7(4) the value up to which the Sheriff may conduct the sale` |
| O 22 r 7(4) | 3492 | the Sheriff | the enforcement respondent | power / liability (conduct the sale, by private treaty or by public auction) | roc5-o22-sheriff.l4 `o 22 r 7(4) the sale may be conducted by the Sheriff and may be by private treaty or by public auction` |
| O 22 r 7(5) | 3493 | the enforcement respondent and the enforcement applicant | the Sheriff | claim / duty (an auctioneer and public auction where the paragraph requires it) | roc5-o22-sheriff.l4 `o 22 r 7(5) the sale must be conducted by an auctioneer and by public auction`; `o 22 r 7(6) the period before the sale by which the notice of sale must be given` |
| O 22 r 7(6) | 3494 | persons who may bid or object | the Sheriff | claim / duty (notice of sale of seized property) | roc5-o22-sheriff.l4 `o 22 r 7(6) the notice of sale of seized property is given as the rule requires` |
| O 22 r 7(7) | 3499 | the enforcement respondent | the Sheriff | claim / duty (conduct of the sale of immovable property) | roc5-o22-sheriff.l4 `o 22 r 7(7) the sale of immovable property is conducted as the rule requires`; `o 22 r 7(8) the period before the auction by which the notice must be advertised` |
| O 22 r 7(8) | 3500 | persons who may bid or object | the Sheriff | claim / duty (advertise the notice of sale of immovable property) | roc5-o22-sheriff.l4 `o 22 r 7(8) the notice of sale of immovable property is advertised as the rule requires` |
| O 22 r 7(9) | 3501 | the Sheriff | the enforcement respondent | power / liability (sign the documents in the respondent's place); the purchaser: immunity / disability (the documents have the same effect) | roc5-o22-sheriff.l4 `o 22 r 7(9) the Sheriff may sign the documents in place of the enforcement respondent` |
| O 22 r 8(1) | 3503 | the enforcement applicant | the Sheriff | claim / duty (deliver and give possession as soon as practicable) | roc5-o22-sheriff.l4 `o 22 r 8(1) the Sheriff must deliver and give possession as soon as is practicable after seizure` |
| O 22 r 8(2) | 3503 | the Sheriff | the enforcement applicant | claim / duty (sign the acknowledgment) | roc5-o22-sheriff.l4 `o 22 r 8(2) the enforcement applicant or its representative must sign the acknowledgment` |
| O 22 r 9(1) | 3505 | the Court; the parties | the Sheriff | claim / duty (keep proper records) | roc5-o22-sheriff.l4 `o 22 r 9(1) the Sheriff must keep proper records of the seized properties, attached debts and money received or expended`; `o 22 r 9(2) what the commission is of` (+2) |
| O 22 r 9(2) | 3505 | the Sheriff | the enforcement applicant | claim / duty (commission of 2% with a floor and a ceiling) | roc5-o22-sheriff.l4 `o 22 r 9(2) the Sheriff's commission` |
| O 22 r 9(3) | 3512 | the Sheriff | the enforcement applicant | claim / duty (commission where the property is not sold) | roc5-o22-sheriff.l4 `o 22 r 9(3) the Sheriff's commission where the property is not sold` |
| O 22 r 9(4) | 3513 | the parties; the persons entitled to payment | the Sheriff | claim / duty (the statement of accounts shows the listed items) | roc5-o22-sheriff.l4 `o 22 r 9(4) the statement of accounts must show the item` |
| O 22 r 9(5) | 3525 | each person entitled to payment | the Sheriff | claim / duty (payment in the order of priority stated) | roc5-o22-sheriff.l4 `o 22 r 9(5) the position of the item in the order of priority of payments` |
| O 22 r 9(6) | 3526 | the Sheriff | the enforcement applicant | claim / duty (pay the shortfall in the enforcement costs) | roc5-o22-sheriff.l4 `o 22 r 9(6) the enforcement applicant must pay the amount of the shortfall to the Sheriff` |
| O 22 r 9(7) | 3527 | the enforcement applicant | the enforcement respondent | privilege / no-right (add the shortfall to the amount due as enforcement costs) | roc5-o22-sheriff.l4 `o 22 r 9(7) the enforcement applicant is entitled to add the amount to the amount due as part of the enforcement costs` |
| O 22 r 9(8) | 3528 | none | none | none: scope of the Rule | roc5-o22-sheriff.l4 `o 22 r 9(8) this Rule applies to the execution or sale` |
| O 22 r 10(1) | 3530 | the Sheriff | the objector | claim / duty (notice of objection within 14 days after service, and service of a copy) | roc5-o22-objection.l4 `o 22 r 10(1)(a) the objector gives notice of the objection to the Sheriff in time` |
| O 22 r 10(2) | 3534 | the Sheriff | the objector | claim / duty (what the notice of objection must contain) | roc5-o22-objection.l4 `o 22 r 10(2) the notice of objection has the contents the rule requires`; `o 22 r 10(3) the period for the enforcement applicant's notice of consent` |
| O 22 r 10(3) | 3535 | the objector | the enforcement applicant | claim / duty (notice of consent within 14 days); the Sheriff: duty to release | roc5-o22-objection.l4 `o 22 r 10(3) the enforcement applicant must give notice that it consents to the release` |
| O 22 r 10(4) | 3536 | the Sheriff | the objector | power / liability (direct the objector to apply to the Court) | roc5-o22-objection.l4 `o 22 r 10(4) the Sheriff may direct the objector to apply to the Court`; `o 22 r 10(5)(a) the period for applying to the Court` |
| O 22 r 10(5) | 3537 | the Court; the Sheriff | the objector | claim / duty (apply, serve and give notice within the times, failing which the objection is deemed withdrawn) | roc5-o22-objection.l4 `o 22 r 10(5)(a) the objector applies to the Court in time` |
| O 22 r 10(6) | 3543 | the Sheriff | the person asking for information | power / liability (provide information) | roc5-o22-objection.l4 `o 22 r 10(6) the Sheriff may provide the information` |
| O 22 r 10(7) | 3544 | the Sheriff | the objector and the parties | power / liability (sell the property) | roc5-o22-objection.l4 `o 22 r 10(7) the Sheriff may sell the property` |
| O 22 r 10(8) | 3545 | the Sheriff | the Court | privilege / no-right (seek directions by letter at any time) | roc5-o22-objection.l4 `o 22 r 10(8) the Sheriff may seek the Court's directions by letter at any time` |
| O 22 r 11(1) | 3547 | the enforcement applicant | the enforcement respondent | power / liability (apply for oral examination or an affidavit on the properties) | roc5-o22-objection.l4 `o 22 r 11(1) the enforcement applicant may apply for the enforcement respondent to be examined orally in court or to make an affidavit or both on the properties` |
| O 22 r 11(2) | 3547 | the Court | the enforcement respondent | power / liability (order production of documents) | roc5-o22-objection.l4 `o 22 r 11(2) the Court may order the enforcement respondent to produce the documents` |
| O 22 r 11(3) | 3548 | the officers of the respondent entity | the Court | claim / duty (the order names the officers to be examined) | roc5-o22-objection.l4 `o 22 r 11(3) the order must state the appointment of the officers of the entity who are to be examined` |
| O 22 r 11(4) | 3549 | none | none | none: deeming (the application is enforcement of a Court order) | roc5-o22-objection.l4 `o 22 r 11(4) the application is deemed to be enforcement of a Court order` |
| O 22 r 11(5) | 3550 | the enforcement respondent | the enforcement applicant | claim / duty (the order is made and served as the paragraph requires) | roc5-o22-objection.l4 `o 22 r 11(5) the order is made and served as the rule requires` |
| O 22 r 12 | 3552 | the enforcement applicant | the enforcement respondent | power / liability (apply in respect of instalments due and unpaid) | roc5-o22-objection.l4 `o 22 r 12 the enforcement applicant may apply for an enforcement order in respect of the instalments due and unpaid` |
| O 22 r 13(1) | 3554 | a party | the other parties | power / liability (apply for a stay of enforcement) | roc5-o22-objection.l4 `o 22 r 13(1) the party may apply for stay of enforcement or stay of the enforcement order`; `o 22 r 13(2) how long the stay lasts` |
| O 22 r 13(2) | 3554 | the Court | the parties | power / liability (stay for a period, until an event or otherwise) | roc5-o22-objection.l4 `o 22 r 13(2) the Court may order a stay of enforcement or of an enforcement order for the duration`; `o 22 r 13(3) direction to the Sheriff` |
| O 22 r 13(3) | 3555 | the Court | the Sheriff | power / liability (direct withdrawal or maintenance of the seizure or attachment) | roc5-o22-objection.l4 `o 22 r 13(3) the order may give the direction to the Sheriff` |

## Marginal readings for a lawyer (roc5)

Two readings are taken as the status quo (the rule of 2026-10-29, assumed, not ruled by a lawyer).
(a) A failed "if", "unless" or "except" counts as the text's no, clause by clause, within the provision that holds it.
The other reading: "if A then B" does not itself say "if not A then not B", so the answer to a case where A fails would be `NOTHING`.
The same section also records the flat negatives ("does not", "is not entitled", "must not"), which the ruling N2 (2026-11-04, option A) counts as the text's no; they are listed with (a) so that a lawyer sees every `JUST FALSE` that rests on an inference or on N2.
(b) A grant or prohibition limited by its own wording ("without", "when", a named complement, a stated period) does not say no outside the limit, so the answer outside the limit is `NOTHING`.
The other reading: the limit is the text's no, so the answer outside the limit would be `JUST FALSE`.
Branches that rest on a ruling of 2026-11-05 (periods, "where", scope limits, delegated definitions, "until" bars) are not listed here: they are ruled, and each carries its ruling in its own comment.

### Reading (a): `JUST FALSE` after a failed "if", "unless" or "except", or a flat negative

| module | L4 name | branches | what the branch rests on | first quoted words | lines |
| --- | --- | --- | --- | --- | --- |
| roc5-o20.l4 | `o 20 r 1 this Order applies to the proceeding` | 2 | failed if/unless/except: counted as the text's no; flat negative counted as the text's no (N2, ruled) | "This Order does not apply to an appeal from a State Court constituted under the State Cour" | 59, 65 |
| roc5-o20.l4 | `o 20 r 3(4) the affidavit must include the record of proceedings` | 1 | failed if/unless/except: counted as the text's no | "if that is available and is necessary for the appeal or the application" | 172 |
| roc5-o20.l4 | `o 20 r 3(5) a party served must file and serve an affidavit in reply` | 1 | failed if/unless/except: counted as the text's no | "The parties who have been served in paragraph (2) must file and serve an affidavit in repl" | 187 |
| roc5-o20.l4 | `o 20 r 6 the appeal or application operates as a stay of enforcement of the tribunal's decision` | 1 | flat negative counted as the text's no (N2, ruled) | "An appeal or application does not operate as a stay of enforcement of the tribunal’s decis" | 313 |
| roc5-o20.l4 | `o 20 r 7(2) the Appellate Division or Court of Appeal has the power` | 1 | failed if/unless/except: counted as the text's no | "If an appeal to the Appellate Division or Court of Appeal is permitted in the written law" | 343 |
| roc5-o21-appendix.l4 | `o 21 r 10 the amount of costs allowed is the amount set out in Appendix 1` | 1 | failed if/unless/except: counted as the text's no | "unless the Court otherwise orders" | 35 |
| roc5-o21-assessment.l4 | `o 21 r 19(3) paragraph (2) applies` | 1 | flat negative counted as the text's no (N2, ruled) | "Paragraph (2) does not apply where an order for the assessment of a solicitor’s bill of co" | 113 |
| roc5-o21-assessment.l4 | `o 21 r 21(1) the Registrar may disallow the costs of the party's attendance` | 1 | flat negative counted as the text's no (N2, ruled) | "may disallow the costs of attendance of any party not entitled to attend by virtue of the " | 268 |
| roc5-o21-assessment.l4 | `o 21 r 21(2) the Registrar may adjourn the assessment and direct the solicitor to send a copy of the bill` | 1 | failed if/unless/except: counted as the text's no | "Where the Court has directed that a solicitor’s bill of costs be assessed for the purpose " | 283 |
| roc5-o21-assessment.l4 | `o 21 r 22(1) the amount of costs is the amount allowed after assessment on the standard basis` | 1 | failed if/unless/except: counted as the text's no | "unless it appears to the Court to be appropriate to order costs to be assessed on the inde" | 352 |
| roc5-o21-assessment.l4 | `o 21 r 22(3) the cost is allowed on the indemnity basis` | 1 | failed if/unless/except: counted as the text's no | "all costs are to be allowed except insofar as they are of an unreasonable amount or have b" | 427 |
| roc5-o21-assessment.l4 | `o 21 r 22(5) the claimant is entitled to more costs than in a State Court` | 1 | failed if/unless/except: counted as the text's no | "the claimant is not entitled to any more costs than the claimant would have been entitled " | 492 |
| roc5-o21-assessment.l4 | `o 21 r 23(2)(a) the costs are presumed to have been reasonably incurred` | 1 | failed if/unless/except: counted as the text's no | "to have been reasonably incurred if they were incurred with the express or implied approva" | 554 |
| roc5-o21-assessment.l4 | `o 21 r 23(2)(b) the costs are presumed to have been reasonable in amount` | 1 | failed if/unless/except: counted as the text's no | "to have been reasonable in amount if their amount was, expressly or impliedly, approved by" | 564 |
| roc5-o21-assessment.l4 | `o 21 r 23(2)(c) the costs are presumed to have been unreasonably incurred` | 2 | failed if/unless/except: counted as the text's no | "to have been unreasonably incurred if, in the circumstances of the case, they are of an un" | 575, 577 |
| roc5-o21-assessment.l4 | `o 21 r 23(4) delivery of a bill to the client precludes presenting a bill for a larger amount for assessment` | 1 | flat negative counted as the text's no (N2, ruled) | "does not preclude the solicitor from presenting a bill for a larger amount or otherwise fo" | 622 |
| roc5-o21-assessment.l4 | `o 21 r 24(2) the costs are presumed to have been unreasonably incurred` | 1 | failed if/unless/except: counted as the text's no | "to have been unreasonably incurred if they were incurred contrary to the duty of the trust" | 665 |
| roc5-o21-assessment.l4 | `o 21 r 26 the certificate is conclusive as to the amount of costs allowed` | 1 | failed if/unless/except: counted as the text's no | "the certificate of the Registrar, unless set aside, is conclusive as to the amount of cost" | 692 |
| roc5-o21-assessment.l4 | `o 21 r 26 the solicitor may apply for an enforcement order for the costs allowed` | 1 | failed if/unless/except: counted as the text's no | "if there is no application for review" | 711 |
| roc5-o21-assessment.l4 | `o 21 r 27(4) the application for review prejudices the Registrar's power to issue an interim certificate for the item` | 1 | flat negative counted as the text's no (N2, ruled) | "does not prejudice the power of the Registrar under Rule 14 to issue an interim certificat" | 767 |
| roc5-o21-assessment.l4 | `o 21 r 28(2) the Judge may order the item to be remitted to the Registrar for assessment` | 1 | failed if/unless/except: counted as the text's no | "(except where the dispute as to the item under review is as to amount only) order the item" | 816 |
| roc5-o21-assessment.l4 | `o 21 r 29 the costs carry interest at the rate of 5.33% per year` | 1 | flat negative counted as the text's no (N2, ruled) | "Costs under Part 4 of Appendix 1 to this Order do not carry any interest." | 897 |
| roc5-o21-general.l4 | `o 21 r 1(1) this Order applies to the costs` | 1 | failed if/unless/except: counted as the text's no | "any other proceedings if any written law provides or if the parties to any proceedings con" | 44 |
| roc5-o21-general.l4 | `o 21 r 2(3) the costs must be fixed by the Court which heard the matter` | 1 | failed if/unless/except: counted as the text's no | "unless the Court thinks fit to direct an assessment of the costs" | 184 |
| roc5-o21-general.l4 | `o 21 r 2(4) the costs are payable from the date of the Court's order` | 1 | failed if/unless/except: counted as the text's no | "unless the parties otherwise agree" | 203 |
| roc5-o21-general.l4 | `o 21 r 2(6) the Court may stay or dismiss the application, action or appeal or make any other order` | 1 | failed if/unless/except: counted as the text's no | "if a party refuses or neglects to pay any costs ordered within the specified time, whether" | 234 |
| roc5-o21-general.l4 | `o 21 r 3(1) a party is entitled to recover costs from another party` | 1 | failed if/unless/except: counted as the text's no | "no party is entitled to recover any costs of or incidental to any proceedings from any oth" | 269 |
| roc5-o21-general.l4 | `o 21 r 3(2) the Court must order the costs in favour of the successful party` | 1 | failed if/unless/except: counted as the text's no | "except when it appears to the Court that in the circumstances of the case some other order" | 281 |
| roc5-o21-general.l4 | `o 21 r 3(3) the party making the amendment bears the costs of and occasioned by it` | 1 | failed if/unless/except: counted as the text's no | "unless the Court otherwise orders" | 295 |
| roc5-o21-general.l4 | `o 21 r 3(4) the party making the application bears the costs of and occasioned by it` | 1 | failed if/unless/except: counted as the text's no | "unless the Court otherwise orders" | 308 |
| roc5-o21-general.l4 | `o 21 r 3(5) the person is entitled to the costs out of the fund or the mortgaged property` | 1 | failed if/unless/except: counted as the text's no | "unless the Court otherwise orders" | 328 |
| roc5-o21-general.l4 | `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` | 1 | failed if/unless/except: counted as the text's no | "if — ( a ) ... ( b ) ... ( c ) ... or ( d )" | 372 |
| roc5-o21-general.l4 | `o 21 r 5(1) the Court may order costs against the non-party` | 1 | failed if/unless/except: counted as the text's no | "Where it is just to do so, the Court may order costs against a non‑party if the non‑party " | 393 |
| roc5-o21-general.l4 | `o 21 r 6(1) the Court may make the order against the solicitor` | 1 | failed if/unless/except: counted as the text's no | "If the solicitor is responsible, either personally or through an employee or agent, for in" | 434 |
| roc5-o21-general.l4 | `o 21 r 6(4) the Court may direct or authorise the Attorney-General to attend and take part` | 1 | failed if/unless/except: counted as the text's no | "if the Court thinks fit, direct or authorise the Attorney‑General to attend and take part " | 477 |
| roc5-o21-general.l4 | `o 21 r 9(1) the defendant is entitled to the costs incurred to the time of discontinuance` | 1 | failed if/unless/except: counted as the text's no | "unless the Court otherwise orders" | 535 |
| roc5-o21-general.l4 | `o 21 r 9(1) the defendant may sign judgment for the assessed costs` | 1 | failed if/unless/except: counted as the text's no | "the defendant is, unless the Court otherwise orders, entitled to the defendant’s costs of " | 555 |
| roc5-o21-general.l4 | `o 21 r 9(2) the claimant is entitled to the costs incurred to the time of receipt of the notice of payment into Court` | 2 | failed if/unless/except: counted as the text's no | "If a claimant accepts money paid into Court in satisfaction of the cause of action, or all" | 572, 574 |
| roc5-o21-general.l4 | `o 21 r 9(2) the claimant may sign judgment for the assessed costs` | 1 | failed if/unless/except: counted as the text's no | "then subject to paragraph (4)" | 592 |
| roc5-o21-general.l4 | `o 21 r 9(3) the claimant may have the costs assessed and sign judgment against that defendant as in paragraph (2)` | 1 | failed if/unless/except: counted as the text's no | "the claimant is not entitled to have the claimant’s costs assessed if the Court otherwise " | 610 |
| roc5-o21-general.l4 | `o 21 r 9(4) the claimant is entitled to have the costs assessed` | 1 | failed if/unless/except: counted as the text's no | "the claimant is not entitled to have the claimant’s costs assessed if the Court otherwise " | 622 |
| roc5-o21-general.l4 | `o 21 r 9(5) the defendant is entitled to the costs of the counterclaim incurred to the time of receipt of the notice of acceptance` | 2 | failed if/unless/except: counted as the text's no | "If a claimant accepts money paid into Court by a defendant who counterclaimed against the " | 641, 643 |
| roc5-o21-general.l4 | `o 21 r 9(5) the defendant may sign judgment for the assessed costs of the counterclaim` | 1 | failed if/unless/except: counted as the text's no | "then, subject to paragraph (6)" | 661 |
| roc5-o21-general.l4 | `o 21 r 9(6) the defendant is entitled to have the costs of the counterclaim assessed` | 1 | failed if/unless/except: counted as the text's no | "Despite paragraph (5), the defendant is not entitled to have the defendant’s costs assesse" | 671 |
| roc5-o21-general.l4 | `o 21 r 12 the Registrar may do the thing in assessing costs` | 1 | failed if/unless/except: counted as the text's no | "if the Court so directs" | 733 |
| roc5-o21-general.l4 | `o 21 r 13(2) the party liable may make the offer` | 1 | failed if/unless/except: counted as the text's no | "make a written offer to pay a specific sum in satisfaction of those costs which is express" | 765 |
| roc5-o21-general.l4 | `o 21 r 14(2) the Registrar may issue an interim certificate specifying an amount payable by the solicitor to the client` | 1 | failed if/unless/except: counted as the text's no | "If, in the course of the assessment of a solicitor’s bill to the solicitor’s own client, i" | 812 |
| roc5-o22-objection.l4 | `o 22 r 10(1)(b) the objector serves a copy of the notice of objection in time and on the persons the rule names` | 1 | failed if/unless/except: counted as the text's no | "serve a copy of the notice of objection on the enforcement applicant, the enforcement resp" | 66 |
| roc5-o22-objection.l4 | `o 22 r 10(3) the enforcement applicant must give notice that it consents to the release` | 1 | failed if/unless/except: counted as the text's no | "If the enforcement applicant accepts the grounds of objection, the enforcement applicant m" | 146 |
| roc5-o22-objection.l4 | `o 22 r 10(4) the Sheriff may direct the objector to apply to the Court` | 1 | failed if/unless/except: counted as the text's no | "If the enforcement applicant, within 14 days after the service of the notice of objection," | 200 |
| roc5-o22-objection.l4 | `o 22 r 10(5)(a) the objection is deemed to have been withdrawn` | 1 | failed if/unless/except: counted as the text's no | "failing which the objection is deemed to have been withdrawn" | 235 |
| roc5-o22-objection.l4 | `o 22 r 10(5)(b) the objector serves the summons and supporting affidavit in time and on the persons the rule names` | 1 | failed if/unless/except: counted as the text's no | "serve the summons and supporting affidavit on the enforcement applicant, the enforcement r" | 257 |
| roc5-o22-objection.l4 | `o 22 r 10(7) the Sheriff may sell the property` | 1 | flat negative counted as the text's no (N2, ruled) | "The Sheriff must not sell any property that is in dispute" | 337 |
| roc5-o22-objection.l4 | `o 22 r 13(1) the party may apply for stay of enforcement or stay of the enforcement order` | 1 | failed if/unless/except: counted as the text's no | "if there is a special case making it inappropriate to enforce the Court order immediately" | 464 |
| roc5-o22-order.l4 | `o 22 r 2(4) the affidavit must state the item` | 5 | failed if/unless/except: counted as the text's no | "if the Court order requires the enforcement respondent to pay money" | 345, 349, 353, 357, 361 |
| roc5-o22-order.l4 | `o 22 r 2(4)(m) the affidavit states the undertaking and exhibits it as the rule requires` | 2 | failed if/unless/except: counted as the text's no | "that the solicitors for the enforcement applicant (if the enforcement applicant is represe" | 387, 389 |
| roc5-o22-order.l4 | `o 22 r 2(5) the enforcement order is valid in the first instance on the day` | 1 | failed if/unless/except: counted as the text's no | "Subject to paragraph (8)" | 415 |
| roc5-o22-order.l4 | `o 22 r 3(2) the consent is attested as the rule requires` | 1 | failed if/unless/except: counted as the text's no | "or if the judgment creditor has no solicitor, by a commissioner for oaths" | 519 |
| roc5-o22-order.l4 | `o 22 r 5(1) the enforcement applicant is entitled to an enforcement order for attachment of debt in respect of the money` | 1 | flat negative counted as the text's no (N2, ruled) | "the enforcement applicant is not entitled to an enforcement order for attachment of debt i" | 557 |
| roc5-o22-order.l4 | `o 22 r 5(3) the applicant must give notice to the Accountant-General` | 1 | failed if/unless/except: counted as the text's no | "If the application is dismissed, the applicant must give notice of that fact to the Accoun" | 610 |
| roc5-o22-sheriff.l4 | `o 22 r 6(2) the Sheriff may carry out the terms in any order and sequentially or concurrently` | 1 | failed if/unless/except: counted as the text's no | "If no sequence of enforcement is indicated in the enforcement order, the Sheriff may carry" | 63 |
| roc5-o22-sheriff.l4 | `o 22 r 6(10) the non-party hands or pays over in time` | 1 | failed if/unless/except: counted as the text's no | "If no notice of objection is filed under Rule 10, the non‑party must hand or pay over" | 412 |
| roc5-o22-sheriff.l4 | `o 22 r 9(6) the enforcement applicant must pay the amount of the shortfall to the Sheriff` | 1 | failed if/unless/except: counted as the text's no | "If the proceeds of sale are not sufficient to pay the enforcement costs, the enforcement a" | 795 |

72 branches in 63 rules rest on reading (a).

### Reading (b): `NOTHING` outside a limit the text states in its own wording

| module | L4 name | branches | lines |
| --- | --- | --- | --- |
| roc5-o20.l4 | `o 20 r 1 this Order applies to the proceeding` | 1 | 61 |
| roc5-o20.l4 | `o 20 r 4(2) the Court must give the directions that are necessary` | 1 | 239 |
| roc5-o20.l4 | `o 20 r 5(3) the Court may allow the page limit to be exceeded` | 1 | 295 |
| roc5-o20.l4 | `o 20 r 7(1) the Court hearing the appeal or application has the power` | 1 | 329 |
| roc5-o21-appendix.l4 | `o 21 r 10 the amount of costs allowed is the amount set out in Appendix 1` | 1 | 33 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 1(3) the scale of costs and disbursements in both Parts 2 and 3 applies` | 1 | 125 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 2 the costs to be allowed excluding disbursements` | 1 | 185 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 3(4) the costs for the affidavit of service, including the search fee` | 1 | 434 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 3(4) costs are allowed for the affidavit of service` | 1 | 451 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 3(9) costs are allowed for any other item` | 1 | 595 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 4 the disbursement to be allowed in addition to the items under Part 2` | 1 | 651 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 7(1) the costs to be allowed excluding disbursements` | 1 | 775 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 7(2) the scales apply to the entire proceedings` | 1 | 805 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 7(3) the court awards such costs within the scales as it deems appropriate` | 1 | 814 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 8(2) the scale of costs in sub-paragraphs (a) and (b), together with paragraph 3 in Part 2, applies` | 1 | 843 |
| roc5-o21-appendix.l4 | `o 21 app 1 para 8(2)(b) the percentage of the scale` | 1 | 946 |
| roc5-o21-assessment.l4 | `o 21 r 19(2) notice need not be given to the party` | 1 | 103 |
| roc5-o21-assessment.l4 | `o 21 r 20(3) the bill of costs sets out the goods and services tax` | 1 | 163 |
| roc5-o21-assessment.l4 | `o 21 r 22(1) the basis on which the amount of costs is allowed` | 1 | 329 |
| roc5-o21-assessment.l4 | `o 21 r 22(2) the amount is allowed on the standard basis` | 1 | 396 |
| roc5-o21-assessment.l4 | `o 21 r 22(5) the claimant is entitled to more costs than in a State Court` | 1 | 489 |
| roc5-o21-assessment.l4 | `o 21 r 22(5) the most costs the claimant may recover` | 1 | 508 |
| roc5-o21-assessment.l4 | `o 21 r 23(1) this Rule applies to the assessment` | 1 | 521 |
| roc5-o21-assessment.l4 | `o 21 r 23(2) the costs are assessed on the indemnity basis` | 1 | 538 |
| roc5-o21-assessment.l4 | `o 21 r 23(4) delivery of a bill to the client precludes presenting a bill for a larger amount for assessment` | 1 | 623 |
| roc5-o21-assessment.l4 | `o 21 r 23(5) the solicitor is entitled to the amount the Registrar allows` | 1 | 633 |
| roc5-o21-assessment.l4 | `o 21 r 24(1) this Rule applies to the assessment` | 1 | 646 |
| roc5-o21-assessment.l4 | `o 21 r 24(2) the costs are assessed on the indemnity basis` | 1 | 656 |
| roc5-o21-assessment.l4 | `o 21 r 27(5) a person is a Judge in Rules 27 and 28` | 1 | 793 |
| roc5-o21-general.l4 | `o 21 r 2(1) costs are in the discretion of the Court` | 1 | 130 |
| roc5-o21-general.l4 | `o 21 r 2(2) the Court must have regard to the circumstance` | 1 | 169 |
| roc5-o21-general.l4 | `o 21 r 2(3) the costs must be fixed by the Court which heard the matter` | 1 | 182 |
| roc5-o21-general.l4 | `o 21 r 2(5) the Court may order the parties' costs to be set off against one another` | 1 | 224 |
| roc5-o21-general.l4 | `o 21 r 2(7) the Court hearing the appeal may deal with the costs of the proceedings giving rise to the appeal and of the appeal` | 1 | 243 |
| roc5-o21-general.l4 | `o 21 r 2(8) the General Division may decide the costs of the whole proceedings or direct the other court to decide the costs before the transfer` | 1 | 252 |
| roc5-o21-general.l4 | `o 21 r 3(2) the Court must order the costs in favour of the successful party` | 1 | 279 |
| roc5-o21-general.l4 | `o 21 r 3(3) the party making the amendment bears the costs of and occasioned by it` | 1 | 293 |
| roc5-o21-general.l4 | `o 21 r 3(4) the party making the application bears the costs of and occasioned by it` | 1 | 306 |
| roc5-o21-general.l4 | `o 21 r 3(5) the person is entitled to the costs out of the fund or the mortgaged property` | 1 | 326 |
| roc5-o21-general.l4 | `o 21 r 6(1) the Court may make the order against the solicitor` | 2 | 436, 438 |
| roc5-o21-general.l4 | `o 21 r 6(3) the Court may direct that notice be given to the solicitor's client` | 1 | 467 |
| roc5-o21-general.l4 | `o 21 r 7 the Court may award costs to the successful party not represented by solicitors` | 1 | 488 |
| roc5-o21-general.l4 | `o 21 r 8 the costs payable by the claimant or the claimant's solicitor must be fixed or approved by the Court or assessed by the Registrar` | 1 | 509 |
| roc5-o21-general.l4 | `o 21 r 13(1) the party is entitled to the costs of the assessment proceedings` | 1 | 744 |
| roc5-o21-general.l4 | `o 21 r 14(1) the Registrar may issue an interim certificate for the part assessed` | 1 | 802 |
| roc5-o21-general.l4 | `o 21 r 16(2) the Registrar has the same powers, and the same fees are payable, as if the Court had made an order for assessment` | 1 | 854 |
| roc5-o22-objection.l4 | `o 22 r 10(3) the Sheriff must release the specified property or debt` | 1 | 165 |
| roc5-o22-objection.l4 | `o 22 r 10(6) the Sheriff may provide the information` | 1 | 329 |
| roc5-o22-objection.l4 | `o 22 r 10(7) the Sheriff may sell the property` | 1 | 338 |
| roc5-o22-objection.l4 | `o 22 r 10(8) the Sheriff may seek the Court's directions by letter at any time` | 1 | 347 |
| roc5-o22-objection.l4 | `o 22 r 11(1) the enforcement applicant may apply for the enforcement respondent to be examined orally in court or to make an affidavit or both on the properties` | 1 | 362 |
| roc5-o22-objection.l4 | `o 22 r 11(2) the Court may order the enforcement respondent to produce the documents` | 1 | 371 |
| roc5-o22-objection.l4 | `o 22 r 11(3) the order states the appointment of the officers as the rule requires` | 1 | 390 |
| roc5-o22-objection.l4 | `o 22 r 11(4) the application is deemed to be enforcement of a Court order` | 1 | 402 |
| roc5-o22-objection.l4 | `o 22 r 11(4) the application is within the terms of any written law or any order staying enforcement of the Court order` | 1 | 411 |
| roc5-o22-objection.l4 | `o 22 r 11(5) the order is made and served as the rule requires` | 1 | 424 |
| roc5-o22-objection.l4 | `o 22 r 13(1) the party may apply for stay of enforcement or stay of the enforcement order` | 1 | 461 |
| roc5-o22-objection.l4 | `o 22 r 13(2) the Court may order a stay of enforcement or of an enforcement order for the duration` | 1 | 479 |
| roc5-o22-objection.l4 | `o 22 r 13(3) the order may give the direction to the Sheriff` | 1 | 496 |
| roc5-o22-order.l4 | `o 22 r 2(1) the person may apply for an enforcement order to enforce the Court orders` | 1 | 160 |
| roc5-o22-order.l4 | `o 22 r 2(1) applying for an enforcement order affects the other method of enforcement` | 1 | 169 |
| roc5-o22-order.l4 | `o 22 r 2(2) the enforcement order authorises the Sheriff to do the thing` | 4 | 204, 208, 212, 216 |
| roc5-o22-order.l4 | `o 22 r 2(2)(c) the debt may be attached` | 1 | 229 |
| roc5-o22-order.l4 | `o 22 r 2(2)(c) the deposit may be attached whether or not it has matured and despite any restriction as to the mode of withdrawal` | 1 | 239 |
| roc5-o22-order.l4 | `o 22 r 2(3) the application is made in the way the rule provides` | 1 | 256 |
| roc5-o22-order.l4 | `o 22 r 2(7) the date by reference to which the priority is determined` | 1 | 455 |
| roc5-o22-order.l4 | `o 22 r 2(7) the priority is determined by reference to the date of original issue` | 1 | 464 |
| roc5-o22-order.l4 | `o 22 r 3(1) the person may apply to the Court for satisfaction to be recorded` | 1 | 492 |
| roc5-o22-order.l4 | `o 22 r 3(1) the Court may order satisfaction to be recorded` | 1 | 503 |
| roc5-o22-order.l4 | `o 22 r 4 the payment or execution is a valid discharge of the non-party's liability to the enforcement respondent` | 1 | 532 |
| roc5-o22-order.l4 | `o 22 r 4 the extent of the discharge` | 1 | 543 |
| roc5-o22-order.l4 | `o 22 r 5(1) the enforcement applicant is entitled to an enforcement order for attachment of debt in respect of the money` | 1 | 558 |
| roc5-o22-order.l4 | `o 22 r 5(1) the enforcement applicant may apply to the Court by summons for payment of the money to the enforcement applicant` | 1 | 567 |
| roc5-o22-order.l4 | `o 22 r 5(1) the most that may be ordered to be paid to the enforcement applicant` | 1 | 581 |
| roc5-o22-order.l4 | `o 22 r 5(5) the Court may make such order with respect to the money in Court as it thinks just` | 1 | 642 |
| roc5-o22-sheriff.l4 | `o 22 r 6(1) the Sheriff must carry out the terms of the enforcement order in the sequence indicated` | 1 | 37 |
| roc5-o22-sheriff.l4 | `o 22 r 6(1) the Sheriff determines the time, place and manner of carrying out the enforcement order` | 1 | 46 |
| roc5-o22-sheriff.l4 | `o 22 r 6(1) the Sheriff may exercise the power relating to forced entry into premises` | 1 | 55 |
| roc5-o22-sheriff.l4 | `o 22 r 6(5) the notice of seizure or attachment may be prepared by that person` | 1 | 195 |
| roc5-o22-sheriff.l4 | `o 22 r 6(8) the non-party is entitled to claim costs from the Sheriff` | 1 | 258 |
| roc5-o22-sheriff.l4 | `o 22 r 6(8) the non-party may deduct the costs from the debt` | 1 | 275 |
| roc5-o22-sheriff.l4 | `o 22 r 6(9)(a) the non-party informs the Sheriff in time` | 1 | 297 |
| roc5-o22-sheriff.l4 | `o 22 r 6(11) the Sheriff may engage, or direct the enforcement applicant to engage, the person` | 1 | 469 |
| roc5-o22-sheriff.l4 | `o 22 r 7(3) the Sheriff must decide the conditions of sale` | 1 | 520 |
| roc5-o22-sheriff.l4 | `o 22 r 7(7) the sale of immovable property is conducted as the rule requires` | 1 | 580 |
| roc5-o22-sheriff.l4 | `o 22 r 7(9) the documents have the same legal effect as if signed by the enforcement respondent` | 1 | 623 |
| roc5-o22-sheriff.l4 | `o 22 r 8(2) the enforcement applicant or its representative must sign the acknowledgment` | 1 | 645 |
| roc5-o22-sheriff.l4 | `o 22 r 9(1) the Sheriff must keep proper records of the seized properties, attached debts and money received or expended` | 1 | 658 |
| roc5-o22-sheriff.l4 | `o 22 r 9(3) the Sheriff's commission where the property is not sold` | 1 | 716 |
| roc5-o22-sheriff.l4 | `o 22 r 9(3) the Sheriff is entitled to a commission where the property is not sold` | 1 | 726 |
| roc5-o22-sheriff.l4 | `o 22 r 9(7) the enforcement applicant is entitled to add the amount to the amount due as part of the enforcement costs` | 1 | 814 |
| roc5-o22-sheriff.l4 | `o 22 r 9(8) this Rule applies to the execution or sale` | 1 | 823 |

96 branches in 92 rules rest on reading (b).


### Reading a result: FALSE and NOTHING (roc5)

This is the rule of 2026-10-29 as refined on 2026-11-04 and 2026-11-05, in the terms of Orders 20 to 22.
Every decision function answers `MAYBE BOOLEAN` unless it computes a number, a date, a basis or an allowance (those answer `MAYBE NUMBER`, `MAYBE DATE`, or `MAYBE` a type of this range).
Where the text can say no to such a function, a yes/no twin beside it answers `JUST FALSE` (for example `o 21 r 29(1) the date from which the costs carry interest` and `o 21 r 29 the costs carry interest at the rate of 5.33% per year`).
Six value functions have no twin: `o 21 r 3(5) the costs not recovered from or paid by any other person` and `o 22 r 9(4)(c) the amount of the landlord's claim to be shown` (both total, they answer a plain number), `o 21 r 22 in whose favour the doubts of the Registrar are resolved`, `o 21 app 1 the column for the court level`, `o 22 r 9(5) the position of the item in the order of priority of payments`, and `o 21 app 1 para 8(2)(b) the percentage of the scale` (its twin is `costs are fixed at a percentage of the scale in the TABLE`, which asks a different question).

**`JUST TRUE`** is the Rules' own yes on the facts.

**`JUST FALSE`** is the Rules' own no, and in this range it comes from exactly these places:
a definition that "means" and the case is not among the members (for example `O 22 r 1` "enforcement respondent", "means a party against whom an enforcement order is sought or made", and `O 21 r 27(5)` "Judge", where the Registrar and any other person are not among the members: fork F9);
a condition the text introduces with "if", "unless", "except", "where", "when", "upon", "on", "failing which" or "until", and it fails (the "if" and "unless" cases are marginal reading (a), below);
a period the text fixes in its own words, and the act falls outside it ("within 14 days after ...", "within 12 months after ...", "at least 14 days before ...");
a flat negative ("does not", "is not entitled", "must not", "do not carry any interest");
a list the text closes with "only" or "nothing but" ("but only if the claim is made within 14 days after service", Order 22, rule 6(8));
two bases that exclude each other, in `o 21 r 22(1) the costs are assessed on the indemnity basis` and `o 21 r 22(4) the costs are assessed on the indemnity basis`: where the text puts the costs on the standard basis, the answer to "is it the indemnity basis" is `JUST FALSE` (4 branches, assumed, not ruled, fork F7; the text does not say "not" in those words).
A `JUST FALSE` never means "the party loses": it means that this provision does not give the thing asked, on these facts.
The sentence the answer is read as is "this provision does not say yes here", and not "the party has no right".
For the defences-style rulings: this range has no "it is a defence to prove that X"; no function says "no defence at all".

**`NOTHING`** is "the Rules do not answer here", and in this range it comes from:
silence (a case outside the cases the paragraph names, for example an Appendix 1 court level that is not a High Court, a District Court or a Magistrate's Court);
a list not closed ("includes", for example `o 21 r 1(2)` "costs includes fees, charges, ...", and the keel's `a person attends`);
an undefined term (a kind of thing the text leaves to a judgment the person states);
a pointer outside the sources (the rate, form or power is in another Order, another Act, a practice direction, or in a written law);
a grant or prohibition limited by its own wording and the case falls outside the limit (96 branches, marginal reading (b), below), and a scope limit with no "only" (5 branches, ruling (c) of 2026-11-05);
a sum, a number or a date that cannot carry the no (14 branches; fork F4): there the twin says `JUST FALSE`.
A caller must never turn `NOTHING` into `FALSE`; the seat layer passes it on as "the Rules do not answer on these facts".

**What a "no" does not mean in this range.**
Where an Order says a party "may" apply, a `JUST FALSE` to "may I apply" means the paragraph, read with the facts given, does not give the power; it does not mean the Court would refuse the application.
Where the text hands a decision to the Court ("as the Court thinks fit", "unless the Court otherwise orders"), the decision is an input and no function guesses it.

**Two things the encoding never does.**
It never counts a period: the last day (or, for a "not earlier than" rule, the first day) is an input taken from Order 3, Rule 3 (seam S-T1).
It never states a conclusion the Rules leave to the Court: the Court's power is encoded as "the Court may ..." and answers whether the paragraph gives the power, not whether it will be used.

**"Subject to any written law".**
It is not threaded as an input in any function of this range (fork F6).
A `JUST TRUE` or `JUST FALSE` is therefore the answer of this provision alone; another written law, or the Court, may change what happens.


## Seams (roc5)

A seam is an input that holds an answer another part's range gives (or a fact outside the sources).
Each line below is: the asking section; the answering section; the input name; its type; and the function that takes it.
Every input name is the label of the answering provision followed by the fact, as PLAN.md section 5 asks; the lead wires them at the merge.

**Seams that PLAN.md section 8 ("You ask") lists for this part.**

| asking | answering | input name | type | taken by |
| --- | --- | --- | --- | --- |
| O 20 r 1 | O 19 r 41 (roc4) | `o 19 r 41 the appeal is one that Order 19, Rule 41 otherwise provides for` | `MAYBE BOOLEAN` | `o 20 r 1 this Order applies to the proceeding` |
| O 20 r 7(1), (2) | O 19 r 7 (roc4) | `o 19 r 7 the Court has the power when hearing an appeal after trial` | `MAYBE BOOLEAN` | `o 20 r 7(1) ...`, `o 20 r 7(2) ...` |
| O 21 r 4 | O 5 (roc1) | `o 5 the party has discharged its duty to consider amicable resolution or to make an offer of amicable resolution` | `MAYBE BOOLEAN` | `o 21 r 4 the Court may disallow or reduce the successful party's costs or order the party to pay costs` |
| O 21 App. 1 para 1(1) | O 52 r 1 (roc10) | `o 52 r 1 the claimant claims relief of the nature specified` | `MAYBE BOOLEAN` | `o 21 app 1 para 1(1) the scale of costs in Part 2 applies to the case` |
| O 21 App. 1 para 3(6) | O 51 r 4 (roc10) | `o 51 r 4 the application is by summons under the rule` | `MAYBE BOOLEAN` | the three `o 21 app 1 para 3(6) ...` functions |
| O 22 r 5(5) | O 33 r 25 (roc7) | `o 33 r 25 the Court's power to make an order with respect to the money in Court is changed` | `MAYBE BOOLEAN` | `o 22 r 5(5) the Court may make such order with respect to the money in Court as it thinks just` |
| O 22 r 6(7) | O 7 r 2 (roc1) | `o 7 r 2 the method is a method of service set out in Order 7, Rules 2 and 3` | `MAYBE BOOLEAN` | `o 22 r 6(7) the copy of the notice may be served on the enforcement respondent by the method` |

**The seam PLAN.md lists that is not a seam input here.**
O 21, Appendix 1, paragraphs 1(1)(c) and 3(4) and (5) cite Order 9, Rule 17 (summary judgment) at five lines (3144 to 3242).
The Appendix asks what happened ("the claimant obtains final judgment under Order 9, Rule 17 unconditionally"; "the Court dismisses an application for summary judgment under Order 9, Rule 17"), which is a fact about the case that the party states; it is a constructor of `o 21 app 1 para 1(1) case` or a plain yes/no input, not an answer that Order 9, Rule 17 computes.
Nothing in this range asks whether Order 9, Rule 17 applies.

**Seams this part took that PLAN.md section 8 does not list.**

| asking | answering | input name | type | taken by |
| --- | --- | --- | --- | --- |
| every period of this range | O 3 r 3 (roc1), S-T1 | `o 3 r 3 the last day for doing the act` | `DATE` | 27 functions (Order 20, rules 3, 4 and 5: 4; Order 21, rules 13, 17, 18, 19 and 27: 5; Order 22, rules 2, 5, 6, 7 and 10: 18) |
| O 22 r 2(3) | O 3 r 3 (roc1), S-T1 | `o 3 r 3 the first day on which the act may be done` | `DATE` | `o 22 r 2(3) the application is made early enough` (the text says "not earlier than") |
| O 20 r 4(1) | O 9 r 1 (roc2), the keel's S-table | `o 9 r 1 the meeting is a case conference as described` | `MAYBE BOOLEAN` | `o 20 r 4(1) the parties attend a case conference in time` |
| O 20 r 5(3) | the Fourth Schedule (roc12) | `sch 4 the fees and additional fees prescribed for the pages in excess of the limit have been paid` | `BOOLEAN` | `o 20 r 5(3) the Court may allow the page limit to be exceeded` |
| O 21 r 1(1), (2) | s 2(1) Legal Profession Act (not among the sources) | `legal profession act s 2(1) the business is contentious business` | `MAYBE BOOLEAN` | `o 21 r 1(1) this Order applies to the costs`, `o 21 r 1(2) the business is contentious business` |

The S-T1 inputs are the count of Order 3, Rule 3, supplied as a date: this part never counts a period, so none of the 27 functions can disagree with Order 3.
The ones that are not in the table (an anchor the person states, such as the date of the tribunal's decision) are plain facts and are not seams.

**Seam S-L2 (Government).**
Order 59, rule 11(1) says "Nothing in Order 22, Order 23 and Order 13, Rule 9 apply in respect of any order against the Government" (PLAN.md section 5.3); nothing in Order 22 here asks whether the Government is a party, and the seat layer does not either.
The merge wires it as a flat statement about the overridden provisions, per PLAN.md section 5.

**The seams other parts ask of this one ("You are asked", PLAN.md section 8).**
These are the functions whose results the other parts can pass; none is edited by this part.

| cited from | cites | the function to pass |
| --- | --- | --- |
| O 19 (roc4) | O 20 whole | `o 20 r 1 this Order applies to the proceeding` |
| O 25, O 33, O 62 (roc6, roc7, roc11) and the Fourth Schedule (roc12) | O 21 whole | `o 21 r 1(1) this Order applies to the costs` |
| O 13, O 42, O 45, O 59 (roc2, roc9, roc11) | O 22 whole, r 2, r 10 | `o 22 r 2(1) the person may apply for an enforcement order to enforce the Court orders`, and the rule 10 functions |
| O 56 (roc10) | O 22 r 2, r 6 | `o 22 r 2(2) the enforcement order authorises the Sheriff to do the thing`, `o 22 r 6(4) the Sheriff carries out the enforcement order by the step` |
| the Fourth Schedule (roc12) | O 20 r 5 | `o 20 r 5(2) the written submissions are within the page limit` and `o 20 r 5(3) the Court may allow the page limit to be exceeded` |

**Which functions take the day as an input, and where the day is counted (fix round, 5 November 2026).**
28 functions of this range compare the day of an act with a period by taking the end of the period (27 functions) or, for one "not earlier than" rule, the start (1 function) as a date input, and comparing the two; none of them counts the period.
Counting is done by Order 3, Rule 3, which is another part's: which day is the last day (the period "begins immediately after" the specified date, Rule 3(3)), how a period of 6 days or less leaves out a non-court day (Rule 3(6)), and how a time that expires on a non-court day carries over to the next court day (Rule 3(7)).
A reader who looks in this range for those rules will not find them, and should not.
The 27 functions that take `o 3 r 3 the last day for doing the act` are these:

- `o 20 r 3(2) the originating application and affidavit are filed and served in time`
- `o 20 r 3(5) the affidavit in reply is filed and served in time`
- `o 20 r 4(1) the parties attend a case conference in time`
- `o 20 r 5(1) the written submissions are filed and served in time`
- `o 21 r 13(2) the party liable may make the offer`
- `o 21 r 17 the bill of costs is filed in time`
- `o 21 r 18 the Registrar's notice of the assessment is given in time`
- `o 21 r 19(1) the copy of the bill of costs is sent in time`
- `o 21 r 27(2) the application for review is made in time`
- `o 22 r 2(5) the enforcement order is valid in the first instance on the day`
- `o 22 r 5(4) the summons is served on the enforcement respondent in time`
- `o 22 r 6(10) the non-party hands or pays over in time`
- `o 22 r 6(4)(d)(i) the enforcement order is registered in time`
- `o 22 r 6(6) the copy of the notice is served on the enforcement respondent in time`
- `o 22 r 6(8) the non-party is entitled to claim costs from the Sheriff`
- `o 22 r 6(9)(a) the non-party informs the Sheriff in time`
- `o 22 r 6(9)(b) the non-party cannot yet deal with the attached amount`
- `o 22 r 7(1) the Sheriff may take steps to sell the seized movable property`
- `o 22 r 7(2) the Sheriff may take steps to sell the seized immovable property`
- `o 22 r 7(6) the notice of sale of seized property is given as the rule requires`
- `o 22 r 7(8) the notice of sale of immovable property is advertised as the rule requires`
- `o 22 r 10(1)(a) the objector gives notice of the objection to the Sheriff in time`
- `o 22 r 10(1)(b) the objector serves a copy of the notice of objection in time and on the persons the rule names`
- `o 22 r 10(3) the enforcement applicant gives notice of consent in time`
- `o 22 r 10(5)(a) the objector applies to the Court in time`
- `o 22 r 10(5)(b) the objector serves the summons and supporting affidavit in time and on the persons the rule names`
- `o 22 r 10(5)(c) the objector gives notice to the Sheriff in time`

The one function that takes `o 3 r 3 the first day on which the act may be done` is `o 22 r 2(3) the application is made early enough`.
Six more functions use a measure of elapsed time that is not a count under Order 3, Rule 3, and are not seam inputs: `o 21 r 9(1)`, `o 21 r 9(2)` and `o 21 r 9(5)` (`the defendant may sign judgment ...`, `the claimant may sign judgment ...`) and `o 21 r 26` take "the hours that have run since the assessment" (48 hours is a count of hours, and Rule 3 counts days and months); `o 21 r 29(1) interest is running on the day` takes the commencement date, the day asked about and the day of payment; `o 22 r 2(6) the Court may extend the validity of the enforcement order` takes the date of the application and the day on which the order would otherwise expire.
`o 22 r 2(4)(e)` takes a yes/no input ("more than 6 years have passed since the date of the Court order"), and the years are the party's count (fork list, "Checked in the fix round").


## Findings: what the text turns out to say (roc5)

Each finding was checked against the line of the text or the file cited, on 5 November 2026.

1. **The keel's `o 1 r 3(1) a person attends` answers `NOTHING` for an ordinary appearance.**
   The definition reads "“attend” includes the appearance by any person using electronic, mechanical or any other means permitted by the Court" (`inputs/SCJA1969-S914-2021.txt:91`), and `roc-definitions.l4` answers `JUST TRUE` only when the person appears by those means and the Court permitted them, and `NOTHING` otherwise (the "includes" rule).
   So the commonest case, a party who simply turns up, is `NOTHING` in the keel.
   Order 20, rule 4(1) ("The parties must attend a case conference") therefore takes the plain fact `the parties attend the meeting` (a `BOOLEAN`) and does not call the keel's function.
   Recorded here and not edited: the keel is read-only, and the lead may want a constructor for an ordinary appearance (see `NEEDS-CORE.md` if present; none was written, because nothing in this range needed a type the core lacks).

2. **Order 22, rule 6(10) is limited to the case where no notice of objection is filed, and Rule 10 does not say when the non-party pays over afterwards.**
   Rule 6(10) opens "If no notice of objection is filed under Rule 10" (line 3483) and gives 7 days after the 21-day bar of rule 6(9)(b)(ii); rule 6(9)(b)(i) bars the non-party from dealing with the attached amount "until after the notice of objection has been determined in the manner set out in that Rule".
   Rule 10(1) to (8) (lines 3530 to 3545) say what the objector, the enforcement applicant and the Sheriff do, and nothing about when the non-party hands over or pays over after a determination.
   The text is silent on that time.
   `o 22 r 6(10) the non-party hands or pays over in time` answers `JUST FALSE` when an objection is filed, because the "if" fails (marginal reading (a)); the silence is the better description, and a lawyer who prefers `NOTHING` for that branch changes one branch of `o 22 r 6(10) the non-party hands or pays over in time` (the one whose quoted words begin "If no notice of objection is filed under Rule 10").

3. **Order 22, rule 10(5) gives a consequence to one of three duties.**
   Only 10(5)(a) says what follows a default: "failing which the objection is deemed to have been withdrawn" (line 3538).
   Paragraphs 10(5)(b) and (c), the service of the summons and the notice to the Sheriff, each within 7 days after making the application, say nothing about a default.
   `o 22 r 10(5)(b) ...` and `(c) ...` answer whether the duty was met on time and nothing more; no consequence is invented.

4. **Order 20, rule 5(1) is "Subject to Rule 4", and Rule 4 does not say in terms that its directions fix the time for submissions.**
   Rule 4(2) says only "the Court must give the directions that are necessary for the appeal or the application" (line 2894), and rule 5(1) gives "at least 14 days before the hearing" (line 2896).
   The implication that the case-conference directions can change the time is taken as an input (`the directions given at the case conference under Rule 4 fix a different time`), and when it is true the function answers `NOTHING` (the directions are not in the Rules).

5. **"Unless the Court otherwise orders" answers `NOTHING` when the Court has ordered otherwise.**
   Where a rule is subject to it, the order's terms are not in the Rules, so the function is `NOTHING` when the input says the Court has ordered otherwise (for example `o 21 r 17 the bill of costs is filed in time`, `roc5-o21-assessment.l4`, the first branch).
   This applies to 11 inputs under eight names in the range (fork F6).

6. **Order 21, rule 29(1) fixes interest to the day of payment, and Part 4 costs carry none.**
   The costs in the first column of the table "carry interest at 5.33% per year from the date mentioned in the second column of the table until payment" (line 3116), and rule 29(2) says that costs under Part 4 of Appendix 1 "do not carry any interest" (line 3132).
   The interest-running function answers `JUST TRUE` on a day from the commencement date to the day of payment, `JUST FALSE` outside, and `NOTHING` when the day of payment is not given, because "until payment" has no end date to test against; the 5.33% is the Rules' own figure and is not an input.

7. **Two rules in the range give a plain sum with a floor and a ceiling.**
   The Sheriff's commission is "2% of" the gross amount or proceeds "subject to a minimum amount of $100 and a maximum amount of $50,000" (Order 22, rule 9(2), line 3511), and the commission where property is not sold is 2% of the lesser of the estimated value and the amount due, subject to the same floor and ceiling (rule 9(3), line 3512).
   Both are `max 100 (min 50000 (2% TIMES x))` over the amount given, with the boundaries tested on both sides.

8. **Order 22, rule 2(5) and (6): twelve months "beginning with the date of issue".**
   An enforcement order "is valid in the first instance for 12 months beginning with the date of issue" (line 3433): the day of issue is day 1, so an order issued on 1 March 2027 is valid through 29 February 2028 (tested: `roc5-cases-seat.l4`, scenario 3).
   An extension is for "a period of 12 months at any time beginning with the day on which the order is made" if the application is made "before the day on which the enforcement order would otherwise expire" (line 3434); the extension's own end is an input from Order 3, Rule 3.

9. **The Appendix 1 "High Court" column** is the Appendix's only name for the court of first instance above the District Court; fork F3.

10. **No `Hohfeld` relation is typed into any answer.**
    The kinds are in the "Jural relations (roc5)" table only (ruling N2).

11. **The indemnity basis is reached through four different provisions, and only one of them lets the Court choose it.**
    Order 21, rule 22(1) puts the costs on the standard basis in three listed cases "unless it appears to the Court to be appropriate to order costs to be assessed on the indemnity basis" (line 3081); rule 22(4) fills a gap when an order gives no basis or another basis (line 3084); rules 23(2) and 24(2) deem the indemnity basis for a solicitor's own client and for a trustee or personal representative paid out of a fund (lines 3087 and 3100).
    Each has its own yes/no function now (fork F7); the Court's order under rule 22(1) is an input, because the Rules do not say when it "appears" appropriate.

12. **"Judge" has two definitions, and they differ on the Registrar.**
    Order 21, rule 27(5) says that "Judge" "means a Judge sitting in the General Division or a District Judge and includes a judge sitting in the Appellate Division or the Court of Appeal where appropriate" for rules 27 and 28 (line 3111), and Order 1, rule 3 (line 111) defines it more widely, adding "in cases where he or she is empowered to act, a Magistrate or the Registrar".
    This range encodes the first only; under it the Registrar is not a Judge, which is the point of rule 27 (a Judge reviews the Registrar's decision).
    Fork F9.


## What your main binary does not accept (roc5)

Measured on 5 November 2026 with `l4-main-109` (1.6.109, main, 4c887e0, 2026-11-04); where a line says "both", the same file was run with `l4-main-108` (1.6.108) and read the same.
The binary governs; where a skill describes a construct that this binary rejects, it is not used here.

1. **`WAIT UNTIL` is not a clause of a regulative rule on either dialect; it is a clock-advance event in a `#TRACE`, and main spells it `WAITUNTIL`.**
   On 1.6.109 and 1.6.108, `#TRACE ... WITH (WAITUNTIL 11)` runs and expires a `WITHIN 10` duty with a `BREACH`, and `(WAITUNTIL 10)` leaves the duty standing with `WITHIN 0` (the deadline is inclusive): probe `work/probe/p9.l4`, same output on both builds.
   Used as a clause between `MUST` and `WITHIN` (probe `work/probe/p7.l4`), either spelling stops at that token with a parse error on main (`parse/unexpected-identifier`) and with an error at the same token on unstable.
   The unstable spelling of the event is ``(`WAIT UNTIL` n)``, which the unstable build 1104 accepts (probe `work/probe/p10.l4`).
   This range uses `(WAITUNTIL n)` in 5 of its 18 traces to show a duty breached by expiry with no act (rules 6(9)(a), 6(10), 10(1), 10(5)) or left standing (rule 10(3)), and 2 more for the bar of rule 6(9)(b)(ii).
2. **`#TRACE` results cannot be asserted.**
   A trace prints `FULFILLED`, `BREACH` or the obligation that is left; no assertion line exists for it, so the counts of `check.sh` cannot see a change of trace outcome.
   The 18 traces of this range (`roc5-o22-sheriff.l4`: 9; `roc5-o22-objection.l4`: 9) were run with both builds and their whole output compared: identical.
   Their outcomes, by rule: 6(9)(a) `FULFILLED` (act on day 14), `BREACH` (act on day 15), `BREACH` (no act, clock at day 15); 6(9)(b)(ii) `FULFILLED` (clock at day 22), `BREACH` (an act of dealing on day 5), `MUST NOT ... WITHIN 0` (clock at day 21: the bar still stands); 6(10) `FULFILLED` (both acts on day 7), `BREACH` (the commission on day 8), `BREACH` (no act, clock at day 8); 10(1) `FULFILLED`, `BREACH` (the copy served on day 15), `BREACH` (no act, clock at day 15); 10(3) `FULFILLED` (consent on day 14) and, for day 15 either by a late act or by the clock, the Sheriff's `MAY` direct; 10(5) `FULFILLED`, `BREACH` (the application on day 8), `BREACH` (no act, clock at day 8).
   Each regulative duty is therefore also written as a decision function, which is asserted (fork F5).
3. **`JUST 80%` is a type error; `JUST (80%)` parses.**
   Probe `work/probe/p4.l4` reports "The argument of '%' is expected to be of type NUMBER" on `JUST 80%`; `work/probe/p6.l4` accepts `JUST (80%)`.
   The percentages of Appendix 1, paragraph 8(2)(b) are written `JUST (80%)`, `JUST (90%)`, `JUST (100%)`.
4. **`NOT a AND NOT b` parses as `NOT (a AND NOT b)`**, as the brief says: probe `work/probe/p5.l4` with `a` false and `b` true gives true, not false.
   Every `NOT` in the range is parenthesised; one test of Order 21, rule 19(2) failed on this before the fix.
5. **Not re-measured here, taken from the brief (guide, section 5):** a continuation line after `#ASSERT` is rejected, and a `•` bullet in a list is a parse error on main.
   Every assertion in the range is on one line, and no list uses a bullet.
6. **`l4 run` exits 0 when an assertion fails.**
   The numbers in "What check.sh prints" are the evidence, not an exit code.


## Seat (roc5)

**The seat is a party to a civil action in the Singapore courts (a claimant, a defendant, a third party or an appellant), asking, on facts they can state, what they must file or serve, by when, how, at what cost, what the Court may order, and what follows if they do not.**
There is no seat for the Court, the Registrar, the Judge, the Sheriff or the Accountant-General.
A rule that addresses only one of them is still asked, because it decides what happens to the party.
The wording is not uniformly party-facing: 105 of the 273 questions (the ones a party asks first) were worded by hand ("did I file my bill of costs in time?", "may I apply to a Judge to review the assessment as to this item?"), and the other 168 state the rule as a question, by a mechanical rule that turns the first auxiliary verb of the rule's own name into the opening word ("must the Sheriff keep proper records of the seized properties ...?", "may the Sheriff seek the Court's directions by letter at any time?").
Their party-facing framing is in the `§§` situational comments (for example "Asked only once an enforcement order has been issued and the Sheriff is acting on it") and in the inputs, which are always facts the party can state.
The individual is the only seat of this part; the enforcement applicant and the objector are positions the same party can be in, and the questions say so in their wording ("as a non-party served with a notice of attachment, ...").

**Files.**
`roc5-seat.l4` has 273 questions, one for each decision function of layer 1 that takes an input; each is an `@export` with its text, and each input has an `@desc` worded as the party would be asked.
`roc5-cases-seat.l4` has 662 assertions: every question has at least one case, 158 of the 273 have a case that answers `NOTHING`, and three scenarios (an appellant from a tribunal, a party who wants costs, a judgment creditor and a non-party served with a notice of attachment) walk the questions in the order a party meets them.
The expected values of the first 628 assertions are those of the layer-1 test files, which were written from the text before the modules were run; the 34 scenario assertions were written from the text on the day (5 of them added in the fix round: a Registrar is not a Judge in rules 27 and 28, the indemnity basis ordered, the interest on $10,000 for one year, and the two cases of Order 22, rule 12), and one of them (the non-party, an objection filed) was changed during the work after it failed: it first expected `NOTHING` and now expects `JUST FALSE`, because the rule's opening words are "If no notice of objection is filed", an "if" that fails, which is counted as the text's no (marginal reading (a) of the rule of 2026-10-29); the first expectation had overlooked the "if", and the layer-1 test for the same facts, written from the text first, already expected `JUST FALSE`; the reason is in the comment above the assertion.

**Names.**
Every question begins "Under Order 20, rule 3(2), ..." (the Rules' own numbering); the Appendix 1 questions begin "Under Order 21, Appendix 1 paragraph 3(1), ...", which follows the brief's "Under schedule N paragraph M," pattern for a schedule; the one question about the column of the scale begins "Under Order 21, Appendix 1, ...".
The helper type and its constructors begin "Under Orders 20 to 22,".
No name in the two files is a bare word, and none can collide with another part's seat.

**Plain inputs.**
Every input is a yes/no, a number, a date or a choice from a list.
A fact that is another part's answer (for example whether a meeting is "a case conference as described" in Order 9, Rule 1, or whether business is "contentious business" under the Legal Profession Act) is asked as "yes, no, or I am not sure"; "I am not sure" becomes `NOTHING`, and a rule that cannot answer without it answers `NOTHING`.
A period is counted by Order 3, Rule 3, which is another part's: the party states the last day of the period (or, for a "not earlier than" rule, the first day) as a date, and the question compares the day of the act with it.
One input is asked as a yes/no that depends on a count of years ("more than 6 years have passed since the date of the Court order", Order 22, rule 2(4)(e)); its description tells the party that exactly 6 years, or fewer, is a no.
A sum fixed by the Rules (the fixed costs of Appendix 1, the Sheriff's commission, the 5.33% interest rate, the $100 costs of a non-party) is read from layer 1 and is never asked.
**If the Rules Committee substitutes a figure** (a new Appendix 1, a new rate, a new commission), the answers change; the figures are in the module's constants and tables, and nothing in the seat layer repeats them.

**Groups.**
The questions are under `§` headings in the order of the text (Order 20, Order 21, Order 22) and `§§` headings by rule (and by paragraph of Appendix 1, after Rule 29 of Order 21, where the text puts it).
Where a group arises only in a situation the party may not be in (an objection to a seizure, a costs order against a non-party, a motor accident action), the heading's comment says so, so that the form can ask "Has this happened to you?" before it shows the group.

**How the layer was made.**
`roc5-seat.l4` is generated by `work/gen_seat.py` from the signatures of the layer-1 functions, so that it calls the rule and never restates it; the wording of each question and each input is in that script's tables (`QUESTION`, `TYPE_NOUN`, `SUBJ`) and the generator is not shipped.
A seat question adds exactly this and nothing else: it turns "yes / no / I am not sure" into a `MAYBE BOOLEAN`, and turns "have I paid / on what date" into a `MAYBE DATE`.

## Dependencies (roc5)

Nothing was copied from `inputs/DEPENDENCIES/` and nothing was needed from it.
The Interpretation Act modules staged there (`sgia-interpretation-time.l4`, `sgia-p1-definitions.l4`) govern periods that an Act sets; the Rules of Court count their own periods (Order 3, Rule 3), so each period of this range takes the last day from Order 3, Rule 3 as an input (seam S-T1), and `inputs/DEPENDENCIES.md` says the Interpretation Act does not govern those.
No other Singapore Act that Commons encodes is cited in a way that needs its answer except the Legal Profession Act (section 2(1), "contentious business"), which is not staged and is taken as the input `legal profession act s 2(1) the business is contentious business`, to be filled later.

## Unstable dialect (roc5)

I looked at time, rule versions and workarounds and found nothing that earns a second encoding.
Time: every period is an input from Order 3, Rule 3, so there is no date arithmetic in this range.
Versions: the one amendment note in the range (Order 20, rule 6, "[S 206/2022 wef 01/04/2022]", line 2902) is already in the current text, so no rule is in force on different dates.
Workarounds: the only difference between the dialects that this range meets is the spelling of the clock-advance event in a trace (`(WAITUNTIL n)` on main, ``(`WAIT UNTIL` n)`` on unstable), which is a spelling and not a shape.
No second, unstable encoding of these provisions was written.

## Caveats (roc5)

- The text is a plain-text rendering made by a converter script, not the official text; nothing here is verified against the official text.
- The two readings "for a lawyer" and the ten forks (F1 to F10) are assumed, not ruled.
- Forms 39 and 40 are named in the text and are not reproduced; what a rule requires of a form is encoded.
- Fees are not in this range (they are in the Fourth Schedule, another part's); the Appendix 1 sums are costs, not fees.
- The seat layer is generated and its wording was read by its author; no lawyer has read it.


## What check.sh prints (roc5)

Run on 5 November 2026 (after the fix round) in the row folder, as `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` (target `main`, the default); exit code 0.
`l4` is 1.6.109 (main, 4c887e0, 2026-11-04); the second build is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Output, exactly:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
roc5-cases-seat.l4                             0       662       0        0         0 |      0       662       0        0  same
roc5-o20.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc5-o21-appendix.l4                           0         0       0        0         0 |      0         0       0        0  same
roc5-o21-assessment.l4                         0         0       0        0         0 |      0         0       0        0  same
roc5-o21-general.l4                            0         0       0        0         0 |      0         0       0        0  same
roc5-o22-objection.l4                          0         0       0        0         0 |      0         0       0        0  same
roc5-o22-order.l4                              0         0       0        0         0 |      0         0       0        0  same
roc5-o22-sheriff.l4                            0         0       0        0         0 |      0         0       0        0  same
roc5-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
roc5-tests-o20.l4                              0        78       0        0         0 |      0        78       0        0  same
roc5-tests-o21-appendix.l4                     0       224       0        0         0 |      0       224       0        0  same
roc5-tests-o21-assessment.l4                   0       183       0        0         0 |      0       183       0        0  same
roc5-tests-o21-general.l4                      0       191       0        0         0 |      0       191       0        0  same
roc5-tests-o22-objection.l4                    0        90       0        0         0 |      0        90       0        0  same
roc5-tests-o22-order.l4                        0       146       0        0         0 |      0       146       0        0  same
roc5-tests-o22-sheriff.l4                      0       178       0        0         0 |      0       178       0        0  same
TOTAL (18 modules)                             0      1752       0        0           |      0      1752       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**Baseline.** No earlier `check.sh` output for this part was supplied.
My own earlier run, taken before the fix round of 5 November 2026 (before the seat wording was last revised and before eight traces were added to `roc5-o22-sheriff.l4` and `roc5-o22-objection.l4`), printed the same 18 modules and 1699 assertions satisfied, against 1752 now (33 more in the layer-1 test files and 20 more in the seat's cases); traces are not counted by `check.sh`, which is why the traces were compared by hand (see "What your main binary does not accept", item 2: 18 traces, identical output on both builds).

**Assertion counts in this part.**
Layer-1 test files: 78 + 191 + 183 + 224 + 146 + 178 + 90 = 1090.
Seat cases: 662.
Total satisfied: 1752; failed 0; refused 0; errors 0.
The keel's own two modules (`roc-core.l4`, `roc-definitions.l4`) have no assertions and no errors.

**srcrefs.py**, run on `roc5-*.l4` in the row folder against `inputs/SCJA1969-S914-2021.txt`:

```
$ python3 -I srcrefs.py check --refs <raw text> roc5-*.l4
srcrefs check: 867 src: lines, 278 runs, 278 locators, 0 problems
$ python3 -I srcrefs.py check --strict <raw text> roc5-*.l4
srcrefs check: 867 src: lines, 278 runs, 278 locators, 0 problems
```

**Stray-comment check.**
`l4 check` over each of the 16 `roc5-*.l4` files, with its output grepped for `is at the end of the file|follows code on its line`: 0 hits in every file, and `Check succeeded.` for every file.

**The quotations in the `FALSE-kind` and `NOTHING-kind` comments** were checked by `work/build.py` against the whole text: 349 quoted passages, 0 not found.