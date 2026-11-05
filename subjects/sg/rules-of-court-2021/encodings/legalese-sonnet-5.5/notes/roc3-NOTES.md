# NOTES (roc3: Rules of Court 2021 (Singapore), lines 1405-2230: Orders 15, 16, 17 and 18)

**Status, 2026-11-05 (second round: after an independent test pass and the rulings of that day).**
Layer 1 (the law) and layer 2 (the seat) are written and run clean on main 1.6.109 and 1.6.108: `check.sh` prints 21 modules, 1522 assertions satisfied, 0 errors, 0 failed and 0 refused, and every module reads the same on both builds (its output is at the end of this file).
`srcrefs.py check --refs` and `--strict` report 0 problems on every `roc3-*.l4` file.
**What the second round changed.**
An independent author wrote 335 scenarios from the text alone and ran them against the first round: 323 assertions satisfied, 10 failed, 0 refused, and 23 gaps (scenarios the encoding had no function for).
(1) `o 15 r 22(1)` now follows `o 15 r 22(3)`: when the commissioner cannot do what paragraph (3) requires, paragraph (1) answers `JUST FALSE` ("Subject to paragraphs (2) and (3)").
(2) Sub-paragraphs (a) and (b) of O 15 r 8(11) are conditions of the submission: a defendant who will give evidence, or who keeps a related counterclaim, answers `JUST FALSE`.
(3) Every "if", "where", "when", "upon", "in such event" and "unless" in the range, and every period fixed in the text's own words, was re-read against the rulings of 2026-11-05: the run made after the source arms were edited and before any expected value was touched failed on 34 layer-1 assertions and 5 seat cases (33 of the layer-1 expectations were `NOTHING` and are now `JUST FALSE`, one was `JUST TRUE` and is now `NOTHING`: O 18 r 3(1)), each on an arm that was edited on purpose, and every one was then updated to the ruled value.
The tests rewritten for the new inputs of O 15 r 22(1) and r 8(11), and the new tests, are not counted in those 34.
A late scan of every "upon", "when" and "whenever" in the range found six more sites, the fee-waiver paragraphs "may upon application waive ..." (fork 15.7 (x)); they now take the fact of an application and answer `JUST FALSE` without one (6 new assertions).
(4) The gaps were filled where the text supports a function (O 15 r 4(16), r 12(1)(b), r 15(4), r 23; the forms of O 15 r 4(1), r 5(1) and O 16 r 2; O 18 r 20(3) and (5), r 22(1), r 30(3) and (5), r 34(1), r 35(7) and (9), r 39(2)); where the text is silent the coverage row says so.
Forks 15.7 to 15.15, 16.2 and 18.6 to 18.9 are new; forks 15.3, 18.1 and 18.5 gained lines.
**What was verified, and how.**
Every expected value in the tests was decided from the text before the run; the numbers above are `check.sh` counts, not exit codes.
The `#TRACE` outcomes of the regulative rules are not asserted (a `DEONTIC` cannot be compared with `EQUALS` on main); they were read by eye on 1.6.109 and compared with 1.6.108 (identical).
**The text is a plain-text rendering made by a converter script from Singapore Statutes Online. It is not the official text, and nothing here is verified against the official text.**
**Where this note and PLAN.md differ, the brief governs (the brief says so).** The differences are listed under "Differences from PLAN.md".

## Files

| file | holds | text lines |
| --- | --- | --- |
| `roc3-order-15-hearings.l4` | Order 15, Division 1, rules 1 to 8: court hearings | 1405-1506 |
| `roc3-order-15-evidence.l4` | Order 15, Division 1, rules 9 to 16: evidence, records, decisions, assessment of damages, trial on affidavits | 1507-1584 |
| `roc3-order-15-affidavits.l4` | Order 15, Division 2, rules 17 to 29: affidavits | 1585-1638 |
| `roc3-order-16.l4` | Order 16: withdrawal and discontinuance | 1639-1667 |
| `roc3-order-17.l4` | Order 17: judgments and orders | 1668-1693 |
| `roc3-order-18-general.l4` | Order 18, Division 1, rules 1 to 14 | 1694-1816 |
| `roc3-order-18-lower.l4` | Order 18, Divisions 2 to 4, rules 15 to 25 | 1817-1985 |
| `roc3-order-18-higher.l4` | Order 18, Division 5, rules 26 to 41 | 1986-2230 |
| `roc3-regulative.l4` | the duties and permissions with a named party, a period and a stated consequence, as regulative rules, run with `#TRACE` | rules of Orders 16, 17, 18 |
| `roc3-tests-*.l4` (8 files) | the tests of the eight modules above | |
| `roc3-seat.l4`, `roc3-cases-seat.l4` | layer 2: the seat, and its cases | |

The rules of one Order are split across several modules only to keep each file small enough to read; the split follows the text's own Divisions and, inside Order 15 Division 1 and Order 18, its rule numbers.
No module imports another roc3 module; they import `roc-core.l4` and `daydate`.
Rules 16, 21, 25 and 33 of Order 18 repeat one another, as do rules 20, 30 and 35 (security) and rules 22 and 34 (payment out).
Each rule has its own functions, named and cited by its own label (option C of ruling E1: each section answers for itself).
Those functions were written by one script from one template (`work/gen18.py`), so the copies cannot drift apart; the script is not shipped, the L4 is.

## Differences from PLAN.md (the brief governs)

- **"Where", "when", "upon" and "until" bars.** PLAN.md predates the rulings of 2026-11-05 on them; this row applies them (the two ruling bullets in the fork register, forks 15.7 and 18.6).
- **File names.** PLAN.md names `roc3-order-15.l4` and `roc3-order-15-tests.l4`; the brief says `roc3-*.l4` and `roc3-tests-*.l4`, and this row splits Orders 15 and 18 into several modules.
- **Seat question names** begin "Under Order N, rule M," as the brief says.
- **Time.** Timeliness is decided against the seam input `o 3 r 3 the last day for doing the act` (S-T1); this part counts no day.
  O 3 r 2(1) (the caveat on the counting rules) is not threaded.

## Coverage (roc3)

One row per unit of lines 1405-2230.
A unit is an order heading, a division heading, a rule heading, a defined term, a rule with a single paragraph, a paragraph or a sub-paragraph.
The rows were produced from the text by a script (`work/units.py`) and mapped to the L4 names by a second (`work/map.py`); neither script is shipped (a name is attached when a `@ref` of the module cites the unit, a part of it, or a paragraph that contains it).
Each row has exactly one disposition: `encoded`, `inert` (with its reason number), `fork` (the row points at the fork register and at the rule that encodes the chosen reading), or `repealed or blank in this text`.
There is no `out-of-scope` row and no `deferred` row.
The tag in square brackets after an L4 name is its module: 15h hearings, 15e evidence, 15a affidavits, 16, 17, 18g general, 18l lower, 18h higher, reg regulative.

**Counts by disposition.**
encoded 508; fork 107; inert 97 (all reason 1: headings and the one marker); repealed or blank in this text 0; total 712.

**Audit.**
The script counted 712 text units: 348 paragraphs, 237 sub-paragraphs, 22 rules with one paragraph, 81 rule headings, 8 defined terms, 8 order headings, 7 division headings and 1 marker.
Rows in the table before the audit: 712; after: 712 (none added or merged).
There are 826 non-blank lines in lines 1405-2230; 0 of them fall outside every row.
The audit found one gap in the first pass: the two sub-paragraphs (a) and (b) of Order 15, rule 8(11) had no locator, because the `@ref` of the function cited only the opening line; the locator was widened to lines 1495-1498 and the tests were rerun (188 assertions satisfied).

| unit | lines | disposition | L4 name(s) and note |
| --- | --- | --- | --- |
| O15 | 1405 | inert (reason 1) | heading or marker: not operative |
| O15 title | 1406 | inert (reason 1) | heading or marker: not operative |
| O15 Division 1 | 1407 | inert (reason 1) | heading or marker: not operative |
| O15 r1 heading | 1408 | inert (reason 1) | heading or marker: not operative |
| O15 r1(1) | 1409 | fork 15.1 | `o 15 r 1(1) the kind of matter is one that must be heard in chambers [15h]`; `o 15 r 1(1) the matter must be heard in chambers [15h]` |
| O15 r1(2) | 1409 | fork 15.11 | `o 15 r 1(2) the matter must be heard in open court [15h]` |
| O15 r1(3) | 1410 | fork 15.1, 18.1 | `o 15 r 1(3) the matter must be heard in open court [15h]` |
| O15 r1(4) | 1411 | fork 15.2 | `o 15 r 1(4) the Court may order the matter to be heard in the other way [15h]` |
| O15 r1(5) | 1412 | fork 15.12 | `o 15 r 1(5) the person may attend the hearing in chambers as of right [15h]` |
| O15 r1(6) | 1413 | encoded | `o 15 r 1(6) the Court may allow the person to attend the hearing in chambers [15h]` |
| O15 r1(7) | 1414 | encoded | `o 15 r 1(7) the Court may hear the matter in court in private with attendance restricted [15h]` |
| O15 r1(8) | 1415 | encoded | `o 15 r 1(8) the person must comply with the practice directions and the Court's directions [15…` |
| O15 r2 heading | 1416 | inert (reason 1) | heading or marker: not operative |
| O15 r2(1) | 1417 | encoded | `o 15 r 2(1) the Registrar of the Supreme Court has the jurisdiction and powers of a Judge sitt…`; `o 15 r 2(1) the Registrar of the Supreme Court may hear the matter in open court [15h]` |
| O15 r2(2) | 1417 | encoded | `o 15 r 2(2) the Registrar of the Supreme Court may refer the matter to a Judge in the General …`; `o 15 r 2(2) the Judge to whom a matter is referred may hear it or send it back to the Registra…`; and 1 more |
| O15 r2(3) | 1418 | encoded | `o 15 r 2(3) the directions that bind the Registrar are given by [15h]`; `o 15 r 2(3) paragraphs (1) and (2) apply to the Registrar of the State Courts [15h]` |
| O15 r3 heading | 1419 | inert (reason 1) | heading or marker: not operative |
| O15 r3(1) | 1420 | encoded | `o 15 r 3(1) the party attends as the Rule requires [15h]` |
| O15 r3(2) | 1420 | encoded | `o 15 r 3(2) the Court may dismiss the party's application, action or appeal or make any other …` |
| O15 r3(3) | 1421 | encoded | `o 15 r 3(3) the Court may dispense with the attendance of the parties or their solicitors and …` |
| O15 r3(3)(a) | 1421-1422 | encoded | `o 15 r 3(3) the Court may dispense with the attendance of the parties or their solicitors and …` |
| O15 r3(3)(b) | 1423-1424 | encoded | `o 15 r 3(3) the Court may dispense with the attendance of the parties or their solicitors and …` |
| O15 r3(4) | 1425 | encoded | `o 15 r 3(4) the Court may direct that the matter be heard in an asynchronous manner [15h]` |
| O15 r4 heading | 1426 | inert (reason 1) | heading or marker: not operative |
| O15 r4(1) | 1427 | encoded | `o 15 r 4(1) the person may request the Registrar to issue an order to attend court or to produ…`; `o 15 r 4(1) the form of the order to attend court or to produce documents [15h]` |
| O15 r4(2) | 1427 | encoded | `o 15 r 4(2) the order is as the Rule requires [15h]` |
| O15 r4(3) | 1428 | encoded | `o 15 r 4(3) the period before the hearing for serving the order [15h]`; `o 15 r 4(3) the order is served in the way and in time the Rule requires [15h]` |
| O15 r4(4) | 1429 | encoded | `o 15 r 4(4) the Registrar may revoke the order [15h]` |
| O15 r4(5) | 1430 | encoded | `o 15 r 4(5) the party may apply to a Judge sitting in the General Division or a District Judge…` |
| O15 r4(6) | 1431 | encoded | `o 15 r 4(6) the period after the Registrar's decision for the application [15h]`; `o 15 r 4(6) the application for review is made as the Rule requires [15h]` |
| O15 r4(7) | 1432 | encoded | `o 15 r 4(7) the order continues to have effect [15h]` |
| O15 r4(8) | 1433 | fork 15.13 | `o 15 r 4(8) the witness need not attend court personally [15h]` |
| O15 r4(9) | 1434 | encoded | `o 15 r 4(9) the witness is entitled to claim reasonable compensation for time and expenses fro…` (note: the text is silent on the amount of the compensation, on the rate and on the procedure for claiming it: no function states any; the entitlement is the function named here) |
| O15 r4(10) | 1435 | encoded | `o 15 r 4(10) the requesting party must include in the letter the name of the prison, the reaso…` |
| O15 r4(11) | 1436-1437 | encoded | `o 15 r 4(11) the order to attend court is to include the words of paragraph (11) [15h]` |
| O15 r4(12) | 1438 | encoded | `o 15 r 4(12) the period before the hearing for serving the order on the Superintendent [15h]`; `o 15 r 4(12) the order to attend court is served on the Superintendent of the prison in time […`; and 1 more |
| O15 r4(13) | 1439 | encoded | `o 15 r 4(13) the witness must remain outside the courtroom [15h]` |
| O15 r4(14) | 1440 | encoded | `o 15 r 4(14) the witness may remain in or leave the courtroom [15h]` |
| O15 r4(15) | 1441 | encoded | `o 15 r 4(15) the requesting party may request the Registrar to produce the document or the Cou…` |
| O15 r4(16) | 1442 | encoded | `o 15 r 4(16) it is sufficient for the Registrar to produce a copy of the document or the recor…` |
| O15 r5 heading | 1443 | inert (reason 1) | heading or marker: not operative |
| O15 r5(1) | 1444 | encoded | `o 15 r 5(1) an application may be made for an order in Form 30 for the issue of a letter of re…`; `o 15 r 5(1) the form of the application for the issue of a letter of request [15h]` |
| O15 r5(1)(a) | 1444-1445 | encoded | `o 15 r 5(1) an application may be made for an order in Form 30 for the issue of a letter of re…` |
| O15 r5(1)(b) | 1446-1448 | encoded | `o 15 r 5(1) an application may be made for an order in Form 30 for the issue of a letter of re…` |
| O15 r5(2) | 1449 | encoded | `o 15 r 5(2) the application may be made in the court [15h]` |
| O15 r5(3) | 1450 | encoded | `o 15 r 5(3) the application is made as the Rule requires [15h]` |
| O15 r5(4) | 1451 | encoded | `o 15 r 5(4) paragraphs (5) to (8) apply [15h]`; `o 15 r 5(5) the form of the letter of request [15h]` |
| O15 r5(5) | 1452 | encoded | `o 15 r 5(5) the letter of request must be in [15h]` |
| O15 r5(5)(a) | 1452-1453 | encoded | `o 15 r 5(5) the letter of request must be in [15h]` |
| O15 r5(5)(b) | 1454-1456 | encoded | `o 15 r 5(5) the letter of request must be in [15h]` |
| O15 r5(6) | 1457 | encoded | `o 15 r 5(6) a translation must accompany the letter of request or a document attached to it [1…` |
| O15 r5(7) | 1458 | encoded | `o 15 r 5(7) the translation is certified as the Rule requires [15h]` |
| O15 r5(8) | 1459 | encoded | `o 15 r 5(8) the party obtaining the order must also file an undertaking in Form 18 [15h]`; `o 15 r 5(8) the undertaking is signed as the Rule requires [15h]`; and 1 more |
| O15 r5(9) | 1460-1463 | encoded | `o 15 r 5(9) the meaning of the term in this Rule [15h]`; `o 15 r 5(9) an instrument is the Hague Evidence Convention [15h]`; and 3 more |
| O15 r5(9) defined term “Hague Evidence Convention” | 1460 | encoded | `o 15 r 5(9) an instrument is the Hague Evidence Convention [15h]` |
| O15 r5(9) defined term “issuing authority” | 1461 | encoded | `o 15 r 5(9) an authority is an issuing authority [15h]` |
| O15 r5(9) defined term “Recommended Model Form” | 1462 | encoded | `o 15 r 5(9) a form is a Recommended Model Form [15h]` |
| O15 r5(9) defined term “transmitting authority” | 1463 | encoded | `o 15 r 5(9) an authority is a transmitting authority [15h]` |
| O15 r6 heading | 1464 | inert (reason 1) | heading or marker: not operative |
| O15 r6(1) | 1465 | encoded | `o 15 r 6(1) the person may attend the hearing [15h]` |
| O15 r6(2) | 1465 | encoded | `o 15 r 6(2) the Court may disallow the person to attend the hearing [15h]` |
| O15 r6(2)(a) | 1465-1466 | encoded | `o 15 r 6(2) the Court may disallow the person to attend the hearing [15h]` |
| O15 r6(2)(b) | 1467-1468 | encoded | `o 15 r 6(2) the Court may disallow the person to attend the hearing [15h]` |
| O15 r6(2)(c) | 1469-1470 | encoded | `o 15 r 6(2) the Court may disallow the person to attend the hearing [15h]` |
| O15 r7 heading | 1471 | inert (reason 1) | heading or marker: not operative |
| O15 r7(1) | 1472 | encoded | `o 15 r 7(1) the originating application must be heard by one Judge [15h]` |
| O15 r7(2) | 1472 | fork 15.8 | `o 15 r 7(2) the Judge may hear the matter with the assistance of assessors [15h]` |
| O15 r7(3) | 1473 | encoded | `o 15 r 7(3) the Court may dismiss the matter [15h]` |
| O15 r7(4) | 1474 | encoded | `o 15 r 7(4) the Court may proceed with the hearing, give judgment against or dismiss the claim…` |
| O15 r7(5) | 1475 | fork 18.1 | `o 15 r 7(5) the originating application or summons must be decided on affidavits and submissio…` |
| O15 r7(6) | 1476 | encoded | `o 15 r 7(6) the Court may order further affidavits, cross-examination of the makers, conversio…` |
| O15 r7(6)(a) | 1476-1477 | encoded | `o 15 r 7(6) the Court may order further affidavits, cross-examination of the makers, conversio…` |
| O15 r7(6)(b) | 1478-1479 | encoded | `o 15 r 7(6) the Court may order further affidavits, cross-examination of the makers, conversio…` |
| O15 r7(6)(c) | 1480-1481 | encoded | `o 15 r 7(6) the Court may order further affidavits, cross-examination of the makers, conversio…` |
| O15 r7(6)(d) | 1482-1483 | encoded | `o 15 r 7(6) the Court may order further affidavits, cross-examination of the makers, conversio…` |
| O15 r7(7) | 1484 | encoded | `o 15 r 7(7) the Court may give its decision immediately after the hearing or at a later date […` |
| O15 r8 heading | 1485 | inert (reason 1) | heading or marker: not operative |
| O15 r8(1) | 1486 | fork 18.1 | `o 15 r 8(1) the trial must be heard by one Judge [15h]` |
| O15 r8(2) | 1486 | fork 15.8, 18.1 | `o 15 r 8(2) the Judge may hear the trial or part of it with the assistance of assessors [15h]` |
| O15 r8(3) | 1487 | encoded | `o 15 r 8(3) the Court may dismiss the claim and any counterclaim [15h]` |
| O15 r8(4) | 1488 | encoded | `o 15 r 8(4) the Court may proceed with the trial, give judgment against or dismiss the claim o…` |
| O15 r8(5) | 1489 | encoded | `o 15 r 8(5) the order of proceedings in paragraphs (6) to (13) applies [15h]` |
| O15 r8(6) | 1490 | encoded | `o 15 r 8(6) the opening statements and affidavits of evidence-in-chief must be read out in Cou…` |
| O15 r8(7) | 1491 | encoded | `o 15 r 8(7) the claimant's evidence is given in the order the Rule requires [15h]` |
| O15 r8(8) | 1492 | encoded | `o 15 r 8(8) the person may cross-examine the claimant and the claimant's witnesses [15h]` |
| O15 r8(9) | 1493 | encoded | `o 15 r 8(9) the defendant's evidence is given in the order the Rule requires [15h]` |
| O15 r8(10) | 1494 | encoded | `o 15 r 8(10) the person may cross-examine the defendant and the defendant's witnesses [15h]` |
| O15 r8(11) | 1495 | fork 15.7 | `o 15 r 8(11) the defendant may make a submission of No case to answer [15h]`; `o 15 r 8(11)(c) the defendant who makes the submission may rely on the evidence of another par…`; and 2 more |
| O15 r8(11)(a) | 1495-1496 | fork 15.7 | `o 15 r 8(11) the defendant may make a submission of No case to answer [15h]` |
| O15 r8(11)(b) | 1497-1498 | fork 15.7 | `o 15 r 8(11) the defendant may make a submission of No case to answer [15h]` |
| O15 r8(11)(c) | 1499-1500 | encoded | `o 15 r 8(11)(c) the defendant who makes the submission may rely on the evidence of another par…` |
| O15 r8(11)(d) | 1501-1502 | encoded | `o 15 r 8(11)(d) the defendant who makes the submission may rely on the evidence of experts [15…` |
| O15 r8(11)(e) | 1503-1504 | encoded | `o 15 r 8(11)(e) the defendant who makes the submission may make submissions on the costs of th…` |
| O15 r8(12) | 1505 | fork 15.7 | `o 15 r 8(12) the Court must hear the submissions of all the parties [15h]` |
| O15 r8(13) | 1506 | encoded | `o 15 r 8(13) the Court may give its decision immediately after the hearing or at a later date …` |
| O15 r9 heading | 1507 | inert (reason 1) | heading or marker: not operative |
| O15 r9 | 1508 | encoded | `o 15 r 9 the person must take an oath or make an affirmation according to the practice of the …` |
| O15 r10 heading | 1509 | inert (reason 1) | heading or marker: not operative |
| O15 r10(1) | 1510 | encoded | `o 15 r 10(1) the Court may ask a witness any questions that the Court considers necessary at a…`; `o 15 r 10(1) the Court must allow the parties to ask the witness further questions arising out…` |
| O15 r10(2) | 1510 | encoded | `o 15 r 10(2) the Court may inspect any object in the courtroom or elsewhere [15e]`; `o 15 r 10(2) the Court may visit the place [15e]` |
| O15 r11 heading | 1511 | inert (reason 1) | heading or marker: not operative |
| O15 r11(1) | 1512 | encoded | `o 15 r 11(1) the Court must maintain a record of the exhibit [15e]` |
| O15 r11(2) | 1512 | encoded | `o 15 r 11(2) the Court may direct that the exhibit be kept in the custody of the party who ten…` |
| O15 r11(3) | 1513 | encoded | `o 15 r 11(3) the exhibits kept with the Court may be returned to the relevant parties [15e]` |
| O15 r11(4) | 1514 | encoded | `o 15 r 11(4) the notice to take back exhibits [15e]`; `o 15 r 11(4) the Court may dispose of the exhibits [15e]`; and 1 more |
| O15 r11(5) | 1515 | encoded | `o 15 r 11(5) the Court must maintain an official record of every hearing [15e]` |
| O15 r11(6) | 1516 | encoded | `o 15 r 11(6) the audio recording is the official record of the hearing [15e]` |
| O15 r11(7) | 1517 | encoded | `o 15 r 11(7) the Court's notes of proceedings are the official record of the hearing [15e]` |
| O15 r11(8) | 1518 | encoded | `o 15 r 11(8) the party may apply for a certified transcript of the official record of the hear…` |
| O15 r11(9) | 1519 | fork 18.1 | `o 15 r 11(9) the costs of producing a certified transcript may be claimed as an item of disbur…` |
| O15 r11(10) | 1520 | encoded | `o 15 r 11(10) the transcript is certified in the manner the Registrar determined [15e]` |
| O15 r11(11) | 1521 | fork 15.9 | `o 15 r 11(11) the time the official record must be kept [15e]`; `o 15 r 11(11) the official record of the hearing must still be kept [15e]` |
| O15 r12 heading | 1522 | inert (reason 1) | heading or marker: not operative |
| O15 r12(1) | 1523 | fork 15.3 | `o 15 r 12(1)(a) the Court may give its decision orally [15e]`; `o 15 r 12(1)(b) the Court may give its decision in writing at the conclusion of the hearing or…` |
| O15 r12(1)(a) | 1523-1524 | fork 15.3 | `o 15 r 12(1)(a) the Court may give its decision orally [15e]` |
| O15 r12(1)(b) | 1525-1526 | fork 15.3 | `o 15 r 12(1)(b) the Court may give its decision in writing at the conclusion of the hearing or…` |
| O15 r12(2) | 1527 | encoded | `o 15 r 12(2) the parties are entitled to a copy of the decision [15e]` |
| O15 r12(3) | 1528 | encoded | `o 15 r 12(3) the Court may dispense with the attendance of the parties and record the judgment…`; `o 15 r 12(3) the Registrar is to inform the parties that the judgment or order is recorded [15…` |
| O15 r12(4) | 1529 | encoded | `o 15 r 12(4) the Court may give such further orders or directions incidental or consequential …` |
| O15 r13 heading | 1530 | inert (reason 1) | heading or marker: not operative |
| O15 r13(1) | 1531 | encoded | `o 15 r 13(1) the Court may give its decision in the matter [15e]` |
| O15 r13(2) | 1531 | encoded | `o 15 r 13(2) the Court may substitute the person as a party and order that the person be bound…` |
| O15 r14 heading | 1532 | inert (reason 1) | heading or marker: not operative |
| O15 r14(1) | 1533 | encoded | `o 15 r 14(1) another Judge or Registrar may take over and give a decision based on the earlier…` |
| O15 r14(2) | 1533 | encoded | `o 15 r 14(2) the Judge or Registrar who takes over may recall any witness and order the partie…` |
| O15 r14(3) | 1534 | encoded | `o 15 r 14(3) the matter must be heard anew by another Judge or Registrar [15e]`; `o 15 r 15(1) kind of proceeding [15e]`; and 1 more |
| O15 r15 heading | 1535 | inert (reason 1) | heading or marker: not operative |
| O15 r15(1) | 1536 | encoded | `o 15 r 15(1) this Rule applies to the proceeding [15e]`; `o 15 r 15(1) the sum is within “damages” in this Rule [15e]` |
| O15 r15(2) | 1536 | encoded | `o 15 r 15(2) the Court must give judgment on liability and on the amount of damages [15e]` |
| O15 r15(1) defined term “damages” | 1536 | encoded | `o 15 r 15(1) the sum is within “damages” in this Rule [15e]` |
| O15 r15(3) | 1537 | encoded | `o 15 r 15(3) the Court may give directions on the assessment of damages and proceed to assess …` |
| O15 r15(4) | 1538 | encoded | `o 15 r 15(4) the period after the judgment for applying for directions [15e]`; `o 15 r 15(4) the damages must be assessed by the Registrar or Judge [15e]`; and 3 more |
| O15 r15(5) | 1539 | fork 15.7 | `o 15 r 15(5) the period after the date of filing for serving the notice of appointment [15e]`; `o 15 r 15(5) the Court may give directions as to the time by which a notice of appointment for…`; and 1 more |
| O15 r15(6) | 1540 | encoded | `o 15 r 15(6) the damages must be assessed until the date of decision in the assessment [15e]` |
| O15 r15(7) | 1541 | encoded | `o 15 r 15(7) the Court may make an award for provisional damages [15e]` |
| O15 r15(8) | 1542 | encoded | `o 15 r 15(8) the claim must be pleaded [15e]` |
| O15 r15(9) | 1543 | encoded | `o 15 r 15(9) the award must specify the contingency and the period for applying for future dam…` |
| O15 r15(10) | 1544 | encoded | `o 15 r 15(10) the Court may specify a different period for each contingency [15e]` |
| O15 r15(11) | 1545 | encoded | `o 15 r 15(11) the Court may extend the period in paragraph (9) or (10) [15e]` |
| O15 r15(12) | 1546 | encoded | `o 15 r 15(12) the claimant may make another application for further damages in respect of the …` |
| O15 r15(13) | 1547 | encoded | `o 15 r 15(13) the application for further damages must be served on the defendant's insurers […`; `o 15 r 15(13) the application for further damages must be served on the defendant [15e]` |
| O15 r15(14) | 1548 | encoded | `o 15 r 15(14) the Court hearing the application for further damages must give the appropriate …` |
| O15 r15(15) | 1549 | encoded | `o 15 r 15(15) the Court may order the damages to be paid in periodic instalments instead of on…` |
| O15 r15(16) | 1550 | encoded | `o 15 r 15(16) the Court may be guided by actuarial tables and other guidelines issued in pract…` (note: the text is silent on which actuarial tables and guides the Court may use: it names none, so no function reads one) |
| O15 r15(17) | 1551 | encoded | `o 15 r 15(17) the Court must give the appropriate directions for the taking of accounts [15e]` |
| O15 r16 heading | 1552 | inert (reason 1) | heading or marker: not operative |
| O15 r16(1) | 1553 | fork 15.4 | `o 15 r 16(1) the trial must be decided on the basis of the affidavits of evidence-in-chief, cr…` |
| O15 r16(2) | 1553 | encoded | `o 15 r 16(2) the Court may allow a witness' evidence-in-chief to be given orally instead of by…` |
| O15 r16(3) | 1554 | fork 15.14 | `o 15 r 16(3) the affidavit of evidence-in-chief may be used [15e]` |
| O15 r16(4) | 1555 | encoded | `o 15 r 16(4) the new fact may be given in oral evidence [15e]` |
| O15 r16(5) | 1556 | encoded | `o 15 r 16(5) the affidavit of evidence-in-chief may contain the evidence [15e]` |
| O15 r16(6) | 1557 | encoded | `o 15 r 16(6) the period before the first date of the hearing for the notice of objection [15e]`; `o 15 r 16(6) the party must give notice of objection to the party relying on the affidavits [1…`; and 1 more |
| O15 r16(7) | 1558 | fork 15.5 | `o 15 r 16(7) the party must give notice by letter to all other parties [15e]`; `o 15 r 16(7) the notice is given at the time the affidavits are served [15e]` |
| O15 r16(8) | 1559 | encoded | `o 15 r 16(8) the notice must state the grounds in section 32 of the Evidence Act that the part…` |
| O15 r16(9) | 1560 | encoded | `o 15 r 16(9) the notice for statements contained in a document contains what the Rule requires…` |
| O15 r16(9)(a) | 1560-1561 | encoded | `o 15 r 16(9) the notice for statements contained in a document contains what the Rule requires…` |
| O15 r16(9)(b) | 1562-1563 | encoded | `o 15 r 16(9) the notice for statements contained in a document contains what the Rule requires…` |
| O15 r16(9)(c) | 1564-1565 | encoded | `o 15 r 16(9) the notice for statements contained in a document contains what the Rule requires…` |
| O15 r16(9)(d) | 1566-1567 | encoded | `o 15 r 16(9) the notice for statements contained in a document contains what the Rule requires…` |
| O15 r16(9)(e) | 1568-1569 | encoded | `o 15 r 16(9) the notice for statements contained in a document contains what the Rule requires…` |
| O15 r16(9)(f) | 1570-1571 | encoded | `o 15 r 16(9) the notice for statements contained in a document contains what the Rule requires…` |
| O15 r16(10) | 1572 | encoded | `o 15 r 16(10) the notice for statements not contained in a document contains what the Rule req…` |
| O15 r16(10)(a) | 1572-1573 | encoded | `o 15 r 16(10) the notice for statements not contained in a document contains what the Rule req…` |
| O15 r16(10)(b) | 1574-1575 | encoded | `o 15 r 16(10) the notice for statements not contained in a document contains what the Rule req…` |
| O15 r16(10)(c) | 1576-1577 | encoded | `o 15 r 16(10) the notice for statements not contained in a document contains what the Rule req…` |
| O15 r16(10)(d) | 1578-1579 | encoded | `o 15 r 16(10) the notice for statements not contained in a document contains what the Rule req…` |
| O15 r16(10)(e) | 1580-1581 | encoded | `o 15 r 16(10) the notice for statements not contained in a document contains what the Rule req…` |
| O15 r16(10)(f) | 1582-1583 | encoded | `o 15 r 16(10) the notice for statements not contained in a document contains what the Rule req…` |
| O15 r16(11) | 1584 | encoded | `o 15 r 16(11) the Court may accept the matter as fact [15e]` |
| O15 Division 2 | 1585 | inert (reason 1) | heading or marker: not operative |
| O15 r17 heading | 1586 | inert (reason 1) | heading or marker: not operative |
| O15 r17 | 1587-1588 | encoded | `o 15 r 17 the act is within “affirm” [15a]`; `o 15 r 17 the person is within “commissioner for oaths” [15a]` |
| O15 r17 defined term “affirm” | 1587 | encoded | `o 15 r 17 the act is within “affirm” [15a]` |
| O15 r17 defined term “commissioner for oaths” | 1588 | encoded | `o 15 r 17 the person is within “commissioner for oaths” [15a]` |
| O15 r18 heading | 1589 | inert (reason 1) | heading or marker: not operative |
| O15 r18 | 1590 | fork 15.6 | `o 15 r 18 the document is an affidavit [15a]` |
| O15 r19 heading | 1591 | inert (reason 1) | heading or marker: not operative |
| O15 r19(1) | 1592 | encoded | `o 15 r 19(1) the affidavit is in the form the Rule requires [15a]` |
| O15 r19(2) | 1592 | fork 15.10 | `o 15 r 19(2) the photograph is as the Rule requires [15a]` |
| O15 r19(2)(a) | 1592-1593 | encoded | `o 15 r 19(2) the photograph is as the Rule requires [15a]` |
| O15 r19(2)(b) | 1594-1595 | encoded | `o 15 r 19(2) the photograph is as the Rule requires [15a]` |
| O15 r19(2)(c) | 1596-1597 | encoded | `o 15 r 19(2) the photograph is as the Rule requires [15a]` |
| O15 r20 heading | 1598 | inert (reason 1) | heading or marker: not operative |
| O15 r20 | 1599 | encoded | `o 15 r 20 the person may make an affidavit [15a]` |
| O15 r21 heading | 1600 | inert (reason 1) | heading or marker: not operative |
| O15 r21 | 1601 | encoded | `o 15 r 21 two or more persons may make a joint affidavit [15a]` |
| O15 r22 heading | 1602 | inert (reason 1) | heading or marker: not operative |
| O15 r22(1) | 1603 | encoded | `o 15 r 22(1) the affidavit may be affirmed and signed, and the attestation completed and signe…` |
| O15 r22(2) | 1603 | encoded | `o 15 r 22(2) the deponent and the commissioner for oaths may sign the affidavit electronically…` |
| O15 r22(3) | 1604 | encoded | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule requires [15a]` |
| O15 r22(3)(a) | 1604-1605 | encoded | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule requires [15a]` |
| O15 r22(3)(b) | 1606-1607 | encoded | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule requires [15a]` |
| O15 r22(3)(c) | 1608-1609 | encoded | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule requires [15a]` |
| O15 r22(3)(d) | 1610-1611 | encoded | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule requires [15a]` |
| O15 r23 heading | 1612 | inert (reason 1) | heading or marker: not operative |
| O15 r23 | 1613 | encoded | `o 15 r 23 an affidavit may be affirmed outside Singapore [15a]` |
| O15 r24 heading | 1614 | inert (reason 1) | heading or marker: not operative |
| O15 r24 | 1615 | encoded | `o 15 r 24 the commissioner for oaths must certify on the affidavit the matters in the Rule [15…`; `o 15 r 24 the certificate is as the Rule requires [15a]` |
| O15 r24(a) | 1615-1616 | encoded | `o 15 r 24 the certificate is as the Rule requires [15a]` |
| O15 r24(b) | 1617-1618 | encoded | `o 15 r 24 the certificate is as the Rule requires [15a]` |
| O15 r24(c) | 1619-1620 | encoded | `o 15 r 24 the certificate is as the Rule requires [15a]` |
| O15 r24(d) | 1621-1622 | encoded | `o 15 r 24 the certificate is as the Rule requires [15a]` |
| O15 r25 heading | 1623 | inert (reason 1) | heading or marker: not operative |
| O15 r25(1) | 1624 | encoded | `o 15 r 25(1) the matter may be put in the affidavit [15a]` |
| O15 r25(2) | 1624 | fork 15.15 | `o 15 r 25(2) the affidavit may contain the matter [15a]` |
| O15 r25(2)(a) | 1624-1625 | fork 15.15 | `o 15 r 25(2) the affidavit may contain the matter [15a]` |
| O15 r25(2)(b) | 1626-1627 | encoded | `o 15 r 25(2) the affidavit may contain the matter [15a]` |
| O15 r26 heading | 1628 | inert (reason 1) | heading or marker: not operative |
| O15 r26(1) | 1629 | fork 15.7 | `o 15 r 26(1) the affidavit may be altered [15a]` |
| O15 r26(2) | 1629 | encoded | `o 15 r 26(2) the maker may correct any mistakes in the affidavit by making another affidavit […` |
| O15 r27 heading | 1630 | inert (reason 1) | heading or marker: not operative |
| O15 r27(1) | 1631 | encoded | `o 15 r 27(1) a copy of the document must be annexed to the affidavit [15a]` |
| O15 r27(2) | 1631 | encoded | `o 15 r 27(2) a copy of the whole document must be annexed [15a]` |
| O15 r27(3) | 1632 | encoded | `o 15 r 27(3) a copy of only those portions of the document need to be annexed [15a]` |
| O15 r27(4) | 1633 | encoded | `o 15 r 27(4) the identification may be done by annexing a picture of the person or object [15a]` |
| O15 r27(5) | 1634 | encoded | `o 15 r 27(5) the annexure must be identified by a certificate of the commissioner for oaths [1…` |
| O15 r28 heading | 1635 | inert (reason 1) | heading or marker: not operative |
| O15 r28 | 1636 | encoded | `o 15 r 28 the seal or signature of the commissioner for oaths must be accepted as valid [15a]` |
| O15 r29 heading | 1637 | inert (reason 1) | heading or marker: not operative |
| O15 r29 | 1638 | encoded | `o 15 r 29 the party must give notice of the intention to use the affidavit and serve it on eve…` |
| O16 | 1639 | inert (reason 1) | heading or marker: not operative |
| O16 title | 1640 | inert (reason 1) | heading or marker: not operative |
| O16 r1 heading | 1641 | inert (reason 1) | heading or marker: not operative |
| O16 r1 | 1642 | fork 16.2 | `o 16 r 1 the party may withdraw the notice of intention to contest or not contest [16]` |
| O16 r2 heading | 1643 | inert (reason 1) | heading or marker: not operative |
| O16 r2(1) | 1644 | fork 16.1 | `o 16 r 2(1) the period after service of the defence [16]`; `o 16 r 2 the form of the notice of discontinuance or withdrawal [16]`; and 4 more |
| O16 r2(2) | 1644 | fork 16.1 | `o 16 r 2(2)(b) the period after service of the defence to counterclaim [16]`; `o 16 r 2(2)(a) the defendant may withdraw the defence or any part of it without the permission…`; and 1 more |
| O16 r2(2)(a) | 1644-1645 | fork 16.1 | `o 16 r 2(2)(a) the defendant may withdraw the defence or any part of it without the permission…` |
| O16 r2(2)(b) | 1646-1648 | fork 16.1 | `o 16 r 2(2)(b) the period after service of the defence to counterclaim [16]`; `o 16 r 2(2)(b) the defendant may discontinue the counterclaim or withdraw a claim in it withou…` |
| O16 r2(3) | 1649 | encoded | `o 16 r 2(3) the date from which the 14 days run for the action [16]` |
| O16 r2(4) | 1650 | encoded | `o 16 r 2(4) the date from which the 14 days run for the counterclaim [16]` |
| O16 r2(5) | 1651 | encoded | `o 16 r 2(5) the action may be withdrawn without the permission of the Court on the consent of …` |
| O16 r2(6) | 1652 | encoded | `o 16 r 2(6) the action is deemed to have been discontinued against the defendant [16]` |
| O16 r2(6)(a) | 1652-1653 | encoded | `o 16 r 2(6) the action is deemed to have been discontinued against the defendant [16]` |
| O16 r2(6)(b) | 1654-1655 | encoded | `o 16 r 2(6) the action is deemed to have been discontinued against the defendant [16]` |
| O16 r2(7) | 1656 | encoded | `o 16 r 2(7) the action, cause or matter is deemed to have been discontinued [16]` |
| O16 r2(8) | 1657 | encoded | `o 16 r 2(8) paragraph (7) applies to the action, cause or matter [16]` |
| O16 r2(9) | 1658 | encoded | `o 16 r 2(9) the Court may extend the time [16]` |
| O16 r2(10) | 1659 | fork 15.7 | `o 16 r 2(10) the Court may reinstate the action, cause or matter and allow it to proceed [16]` |
| O16 r3 heading | 1660 | inert (reason 1) | heading or marker: not operative |
| O16 r3(1) | 1661 | encoded | `o 16 r 3(1) a party may discontinue the action or counterclaim or withdraw a claim without the…`; `o 16 r 3(1) the Court hearing the application may order the discontinuance or striking out on …` |
| O16 r3(2) | 1661 | encoded | `o 16 r 3(2) the application for permission may be made by summons [16]` |
| O16 r4 heading | 1662 | inert (reason 1) | heading or marker: not operative |
| O16 r4 | 1663 | encoded | `o 16 r 4 the discontinuance is a defence to a subsequent action for the same cause of action […` |
| O16 r5 heading | 1664 | inert (reason 1) | heading or marker: not operative |
| O16 r5 | 1665 | encoded | `o 16 r 5 the Court may order the proceedings in the subsequent action to be stayed until the c…` |
| O16 r6 heading | 1666 | inert (reason 1) | heading or marker: not operative |
| O16 r6 | 1667 | encoded | `o 16 r 6 the party may withdraw the summons [16]` |
| O17 | 1668 | inert (reason 1) | heading or marker: not operative |
| O17 title | 1669 | inert (reason 1) | heading or marker: not operative |
| O17 r1 heading | 1670 | inert (reason 1) | heading or marker: not operative |
| O17 r1 | 1671 | fork 17.2 | `o 17 r 1 the thing is an order for the purposes of this Order [17]` |
| O17 r1 defined term “order” | 1671 | fork 17.2 | `o 17 r 1 the thing is an order for the purposes of this Order [17]` |
| O17 r2 heading | 1672 | inert (reason 1) | heading or marker: not operative |
| O17 r2(1) | 1673 | fork 18.1 | `o 17 r 2(1) the order takes effect from the day that it is given [17]` |
| O17 r2(2) | 1673 | fork 18.1 | `o 17 r 2(2) the Court must give that person a reasonable time within which to comply [17]` |
| O17 r2(3) | 1674 | encoded | `o 17 r 2(3) the order is deemed to require immediate compliance [17]` |
| O17 r3 heading | 1675 | inert (reason 1) | heading or marker: not operative |
| O17 r3(1) | 1676 | fork 18.1 | `o 17 r 3(1) the order must be drawn up and filed in Court [17]` |
| O17 r3(2) | 1676 | fork 18.1 | `o 17 r 3(2) the order is in the form that the Rule requires [17]` |
| O17 r3(3) | 1677 | encoded | `o 17 r 3(3) the party must draw up the order [17]` |
| O17 r3(4) | 1678 | encoded | `o 17 r 3(4) the party must draw up only one order for all the applications [17]` |
| O17 r3(5) | 1679 | encoded | `o 17 r 3(5) the period after the order is made for sending the draft [17]`; `o 17 r 3(5) the draft is sent in time [17]`; and 4 more |
| O17 r3(6) | 1680 | fork 18.3 | `o 17 r 3(6) the period for the solicitors to respond to the draft [17]`; `o 17 r 3(6) the solicitors are deemed to consent to the draft [17]`; and 4 more |
| O17 r3(7) | 1681 | encoded | `o 17 r 3(7) the party who drew up the order may write to the Court to resolve the dispute [17]`; `o 17 r 3(7) the letter to the Court is as the Rule requires [17]` |
| O17 r3(8) | 1682 | encoded | `o 17 r 3(8) the Court may decide the dispute without the attendance of the parties or fix an a…` |
| O17 r3(9) | 1683 | encoded | `o 17 r 3(9) the draft of the order is to be submitted to the Registrar [17]` |
| O17 r4 heading | 1684 | inert (reason 1) | heading or marker: not operative |
| O17 r4(1) | 1685 | encoded | `o 17 r 4(1) the Court may redact the order [17]` |
| O17 r4(2) | 1685 | encoded | `o 17 r 4(2) the Court may prohibit the person from inspecting or taking copies of the order [1…` |
| O17 r5 heading | 1686 | inert (reason 1) | heading or marker: not operative |
| O17 r5(1) | 1687 | fork 17.1 | `o 17 r 5(1)(b) the rate of simple interest per year [17]`; `o 17 r 5(1)(a) the money carries interest as agreed between the parties [17]`; and 1 more |
| O17 r5(1)(a) | 1687-1688 | fork 17.1 | `o 17 r 5(1)(a) the money carries interest as agreed between the parties [17]` |
| O17 r5(1)(b) | 1689-1690 | fork 17.1 | `o 17 r 5(1)(b) the rate of simple interest per year [17]`; `o 17 r 5(1)(b) the money carries simple interest at 5.33% per year [17]` |
| O17 r5(2) | 1691 | encoded | `o 17 r 5(2) the simple interest at 5.33% per year from the date the order is made until the da…` |
| O17 r5(3) | 1692 | encoded | `o 17 r 5(3) interest is to be calculated from the date that each instalment is due [17]`; `o 17 r 5(3) the simple interest on an instalment from the date it is due until the date of pay…` |
| O17 r5(4) | 1693 | encoded | `o 17 r 5(4) a part payment must be used to reduce the principal amount due before interest [17]`; `o 17 r 5(4) the principal amount due after the part payment [17]` |
| O18 | 1694 | inert (reason 1) | heading or marker: not operative |
| O18 title | 1695 | inert (reason 1) | heading or marker: not operative |
| O18 amendment marker | 1696 | inert (reason 1) | heading or marker: not operative |
| O18 Division 1 | 1697 | inert (reason 1) | heading or marker: not operative |
| O18 r1 heading | 1698 | inert (reason 1) | heading or marker: not operative |
| O18 r1(1) | 1699 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(a) | 1699 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(a)(i) | 1700-1701 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(a)(ii) | 1702-1703 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(a)(iii) | 1704-1705 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(a)(iv) | 1706-1707 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(a)(iva) | 1708-1709 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(a)(v) | 1710-1711 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(1)(b) | 1712-1713 | encoded | `o 18 r 1(1) this Order applies to the proceeding [18g]`; `o 18 r 1(2) kind of application [18g]` |
| O18 r1(2) | 1714 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r1(2)(a) | 1714 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r1(2)(a)(i) | 1715-1716 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r1(2)(a)(ii) | 1717-1718 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r1(2)(a)(iii) | 1719-1720 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r1(2)(b) | 1721 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r1(2)(b)(i) | 1722-1723 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r1(2)(b)(ii) | 1724-1725 | encoded | `o 18 r 1(2) the application is an application in an action [18g]`; `o 18 r 2 division [18g]`; and 1 more |
| O18 r2 heading | 1726 | inert (reason 1) | heading or marker: not operative |
| O18 r2(1) | 1727 | encoded | `o 18 r 2(1) this Order gives way to a written law on the right to appeal or on permission to a…` |
| O18 r2(2) | 1727 | encoded | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r2(3) | 1728 | encoded | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r2(4) | 1729 | encoded | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r2(5) | 1730 | encoded | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r3 heading | 1731 | inert (reason 1) | heading or marker: not operative |
| O18 r3(1) | 1732 | fork 18.6, 18.1 | `o 18 r 3(1) the time for filing an appeal or an application for permission to appeal starts to…`; `o 18 r 3(1) the time for filing an appeal or an application for permission to appeal is still …` |
| O18 r3(1A) | 1733 | fork 18.5, 15.7 | `o 18 r 3(1A) the period for the lower Court to determine costs [18g]`; `o 18 r 3(1A) the date after which the time starts to run where costs are not determined within…`; and 2 more |
| O18 r3(2) | 1734 | encoded | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined the issue of costs [18g]`; `o 18 r 3(2)(b) the time does not run until all the matters have been heard and determined [18g]`; and 9 more |
| O18 r3(2)(a) | 1734 | encoded | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined the issue of costs [18g]` |
| O18 r3(2)(a)(i) | 1735-1736 | encoded | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined the issue of costs [18g]` |
| O18 r3(2)(a)(ii) | 1737-1738 | encoded | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined the issue of costs [18g]` |
| O18 r3(2)(a)(iii) | 1739-1740 | encoded | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined the issue of costs [18g]` |
| O18 r3(2)(a)(iv) | 1741-1742 | encoded | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined the issue of costs [18g]` |
| O18 r3(2)(b) | 1743-1744 | fork 18.6 | `o 18 r 3(2)(b) the time does not run until all the matters have been heard and determined [18g]`; `o 18 r 3(2)(b) the time is still barred from running because not all the matters have been hea…` |
| O18 r3(2)(c) | 1745 | fork 15.7 | `o 18 r 3(2)(c) paragraph (2)(c) applies to the single application [18g]`; `o 18 r 3(2)(c)(i) the date after which the time runs for the appeal against the decision of th…`; and 3 more |
| O18 r3(2)(c)(i) | 1746-1747 | fork 15.7 | `o 18 r 3(2)(c)(i) the date after which the time runs for the appeal against the decision of th…`; `o 18 r 3(2)(c)(i) the time for the appeal against the decision of the Registrar runs when the …` |
| O18 r3(2)(c)(ii) | 1748-1749 | fork 15.7 | `o 18 r 3(2)(c)(ii) the date after which the time runs for an appeal or an application for perm…`; `o 18 r 3(2)(c)(ii) the time for the appeal or the application for permission against a decisio…` |
| O18 r3(2)(d) | 1750 | fork 15.7, 18.6 | `o 18 r 3(2)(d) the date after which the time runs for the appeal or the application for permis…`; `o 18 r 3(2)(d) the time for the appeal or the application for permission against the decisions…`; and 1 more |
| O18 r3(2)(d)(i) | 1751-1752 | encoded | `o 18 r 3(2)(d) the date after which the time runs for the appeal or the application for permis…`; `o 18 r 3(2)(d) the time for the appeal or the application for permission against the decisions…`; and 1 more |
| O18 r3(2)(d)(ii) | 1753-1754 | encoded | `o 18 r 3(2)(d) the date after which the time runs for the appeal or the application for permis…`; `o 18 r 3(2)(d) the time for the appeal or the application for permission against the decisions…`; and 1 more |
| O18 r4 heading | 1755 | inert (reason 1) | heading or marker: not operative |
| O18 r4(1) | 1756 | fork 18.1 | `o 18 r 4(1) the party may file another appeal for the application [18g]` |
| O18 r4(2) | 1756 | fork 18.1 | `o 18 r 4(2) the party must file a separate notice of appeal for the matters which require perm…` |
| O18 r4(3) | 1757 | encoded | `o 18 r 4(3) each party may file one appeal in respect of all the applications [18g]` |
| O18 r5 heading | 1758 | inert (reason 1) | heading or marker: not operative |
| O18 r5(1) | 1759 | encoded | `o 18 r 5(1) the person may apply to intervene in the appeal [18g]` |
| O18 r5(2) | 1759 | encoded | `o 18 r 5(2) the application for permission to intervene and the supporting affidavit must be f…` |
| O18 r5(3) | 1760 | encoded | `o 18 r 5(3) the supporting affidavit is as the Rule requires [18g]` |
| O18 r5(4) | 1761 | encoded | `o 18 r 5(4) the appellate Court may impose conditions, including ordering the intervening part…` |
| O18 r6 heading | 1762 | inert (reason 1) | heading or marker: not operative |
| O18 r6(1) | 1763 | fork 18.1 | `o 18 r 6(1) the appeal operates as a stay of enforcement or of proceedings under the decision …` |
| O18 r6(2) | 1763 | fork 18.1 | `o 18 r 6(2) an intermediate act or proceeding is invalidated by the appeal [18g]` |
| O18 r6(3) | 1764 | fork 18.1 | `o 18 r 6(3) interest is to be allowed for the time enforcement has been delayed by the appeal …` |
| O18 r7 heading | 1765 | inert (reason 1) | heading or marker: not operative |
| O18 r7 | 1766 | fork 18.4 | `o 18 r 7 the appeal must be heard in chambers [18g]` |
| O18 r8 heading | 1767 | inert (reason 1) | heading or marker: not operative |
| O18 r8(1) | 1768 | encoded | `o 18 r 8(1) the appellate Court may order any party to serve any document on the non-party and…` |
| O18 r8(2) | 1768 | encoded | `o 18 r 8(2) the appellate Court may allow or invite the non-party to give its views and make c…` |
| O18 r8(3) | 1769 | encoded | `o 18 r 8(3) the party may make oral submissions at the hearing of the appeal [18g]` |
| O18 r8(4) | 1770 | encoded | `o 18 r 8(4) the appellate Court may make any order relating to any part of the decision of the…` |
| O18 r8(5) | 1771 | encoded | `o 18 r 8(5) the appellate Court's powers to decide the merits of the appeal are restricted [18…` |
| O18 r8(6) | 1772 | encoded | `o 18 r 8(6) the appellate Court has power to receive further evidence [18g]`; `o 18 r 8(6) the further evidence may be given [18g]` |
| O18 r8(7) | 1773 | encoded | `o 18 r 8(7) the further evidence must be adduced in the manner directed by the appellate Court…` |
| O18 r9 heading | 1774 | inert (reason 1) | heading or marker: not operative |
| O18 r9(1) | 1775 | encoded | `o 18 r 9(1) the appeal may be dismissed [18g]` |
| O18 r9(2) | 1775 | encoded | `o 18 r 9(2) the appeal may proceed in the absence of the respondent [18g]` |
| O18 r9(3) | 1776 | fork 18.3 | `o 18 r 9(3) the period after the dismissal or hearing for the application to restore [18g]`; `o 18 r 9(3) the application to restore the appeal is filed and served in time [18g]`; and 4 more |
| O18 r10 heading | 1777 | inert (reason 1) | heading or marker: not operative |
| O18 r10 | 1778 | encoded | `o 18 r 10 the appellate Court may intervene [18g]` |
| O18 r11 heading | 1779 | inert (reason 1) | heading or marker: not operative |
| O18 r11(1) | 1780 | encoded | `o 18 r 11(1) the lower Court or the appellate Court may order an expedited appeal [18g]` |
| O18 r11(2) | 1780 | encoded | `o 18 r 11(2) the lower Court or the appellate Court may dispense with compliance with any prov…` |
| O18 r12 heading | 1781 | inert (reason 1) | heading or marker: not operative |
| O18 r12(1) | 1782 | encoded | `o 18 r 12(1) the appellant may withdraw the appeal or the applicant may withdraw the applicati…` |
| O18 r12(2) | 1782 | fork 15.7 | `o 18 r 12(2) the appeal or application is deemed withdrawn in relation to the relevant parties…`; `o 18 r 12(2) the security for costs must be paid and the solicitor's undertaking is discharged…` |
| O18 r12(3) | 1783 | encoded | `o 18 r 12(3)(a) the party may request in writing to the appellate Court for directions on the …`; `o 18 r 12(3)(b) oral arguments may be made in the request [18g]`; and 1 more |
| O18 r12(3)(a) | 1783-1784 | encoded | `o 18 r 12(3)(a) the party may request in writing to the appellate Court for directions on the …` |
| O18 r12(3)(b) | 1785-1786 | fork 18.1 | `o 18 r 12(3)(b) oral arguments may be made in the request [18g]` |
| O18 r12(3)(c) | 1787 | encoded | `o 18 r 12(3)(c) the Registrar may remove the appeal or application from the list and give dire…` |
| O18 r12(3)(c)(i) | 1788-1789 | encoded | `o 18 r 12(3)(c) the Registrar may remove the appeal or application from the list and give dire…` |
| O18 r12(3)(c)(ii) | 1790-1791 | encoded | `o 18 r 12(3)(c) the Registrar may remove the appeal or application from the list and give dire…` |
| O18 r12(4) | 1792 | encoded | `o 18 r 12(4) the appeal or application remains on the list [18g]`; `o 18 r 12(4)(b) the appellate Court may at the hearing decide any outstanding issue as to cost…` |
| O18 r12(4)(a) | 1792-1793 | encoded | `o 18 r 12(4) the appeal or application remains on the list [18g]`; `o 18 r 12(4)(b) the appellate Court may at the hearing decide any outstanding issue as to cost…` |
| O18 r12(4)(b) | 1794 | encoded | `o 18 r 12(4) the appeal or application remains on the list [18g]`; `o 18 r 12(4)(b) the appellate Court may at the hearing decide any outstanding issue as to cost…` |
| O18 r12(4)(b)(i) | 1795-1796 | encoded | `o 18 r 12(4) the appeal or application remains on the list [18g]`; `o 18 r 12(4)(b) the appellate Court may at the hearing decide any outstanding issue as to cost…` |
| O18 r12(4)(b)(ii) | 1797-1798 | encoded | `o 18 r 12(4) the appeal or application remains on the list [18g]`; `o 18 r 12(4)(b) the appellate Court may at the hearing decide any outstanding issue as to cost…` |
| O18 r13 heading | 1799 | inert (reason 1) | heading or marker: not operative |
| O18 r13(1) | 1800 | encoded | `o 18 r 13(1) the appellate Court may dispense with the attendance of the parties and record th…`; `o 18 r 13(1) the Registrar is to inform the parties that the judgment or order is recorded [18…` |
| O18 r13(2) | 1800 | encoded | `o 18 r 13(2) the appellate Court may give such further orders or directions incidental or cons…` |
| O18 r14 heading | 1801 | inert (reason 1) | heading or marker: not operative |
| O18 r14(1) | 1802 | encoded | `o 18 r 14(1) the appellate Court may give its decision orally or in writing at the conclusion …` |
| O18 r14(1)(a) | 1802-1803 | encoded | `o 18 r 14(1) the appellate Court may give its decision orally or in writing at the conclusion …` |
| O18 r14(1)(b) | 1804-1805 | encoded | `o 18 r 14(1) the appellate Court may give its decision orally or in writing at the conclusion …` |
| O18 r14(2) | 1806 | encoded | `o 18 r 14(2)(a) the appellate Court may direct the Registrar to inform the parties of its deci…`; `o 18 r 14(2)(b) the parties are to be informed of the Judge or Judges who constituted the appe…` |
| O18 r14(2)(a) | 1806-1807 | encoded | `o 18 r 14(2)(a) the appellate Court may direct the Registrar to inform the parties of its deci…` |
| O18 r14(2)(b) | 1808 | encoded | `o 18 r 14(2)(b) the parties are to be informed of the Judge or Judges who constituted the appe…` |
| O18 r14(2)(b)(i) | 1809-1810 | encoded | `o 18 r 14(2)(b) the parties are to be informed of the Judge or Judges who constituted the appe…` |
| O18 r14(2)(b)(ii) | 1811-1812 | encoded | `o 18 r 14(2)(b) the parties are to be informed of the Judge or Judges who constituted the appe…` |
| O18 r14(2)(b)(iii) | 1813-1814 | encoded | `o 18 r 14(2)(b) the parties are to be informed of the Judge or Judges who constituted the appe…` |
| O18 r14(3) | 1815 | encoded | `o 18 r 14(3) the party is entitled to a copy of the decision [18g]` |
| O18 r14(4) | 1816 | encoded | `o 18 r 14(4) the judgment of the appellate Court may be delivered orally by the Judge [18g]` |
| O18 Division 2 | 1817 | inert (reason 1) | heading or marker: not operative; the text of this Division (rules 15 and 16) has no deemed-withdrawal rule and no security for costs (Divisions 3 to 5 have them): nothing is encoded for either |
| O18 r15 heading | 1818 | inert (reason 1) | heading or marker: not operative |
| O18 r15 | 1819 | encoded | `o 18 r 15 the period after the date of the Registrar's decision for the notice of appeal [18l]`; `o 18 r 15 the notice of appeal in Form 35 is filed and served in time [18l]`; and 3 more |
| O18 r16 heading | 1820 | inert (reason 1) | heading or marker: not operative |
| O18 r16(1) | 1821 | encoded | `o 18 r 16(1) the Registrar may give a summary of the points decided without the need to issue …` |
| O18 r16(2) | 1821 | encoded | `o 18 r 16(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 16(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r16(2)(a) | 1821-1822 | encoded | `o 18 r 16(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 16(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r16(2)(b) | 1823-1824 | encoded | `o 18 r 16(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 16(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r16(2)(c) | 1825-1827 | encoded | `o 18 r 16(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 16(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r16(3) | 1828 | encoded | `o 18 r 16(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 16(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r16(3)(a) | 1828-1829 | encoded | `o 18 r 16(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 16(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r16(3)(b) | 1830 | encoded | `o 18 r 16(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 16(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r16(3)(b)(i) | 1831-1832 | encoded | `o 18 r 16(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 16(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r16(3)(b)(ii) | 1833-1834 | encoded | `o 18 r 16(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 16(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r16(3)(b)(iii) | 1835-1836 | encoded | `o 18 r 16(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 16(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r16(4) | 1837 | encoded | `o 18 r 16(4) the appeal must proceed by way of a rehearing on the documents filed by the parti…`; `o 18 r 16(5) what starts the period for the written submissions [18l]` |
| O18 r16(5) | 1838 | encoded | `o 18 r 16(5) the period for the written submissions [18l]`; `o 18 r 16(5)(a) the period after the notification [18l]`; and 2 more |
| O18 r16(5)(a) | 1838-1839 | encoded | `o 18 r 16(5)(a) the period after the notification [18l]` |
| O18 r16(5)(b) | 1840-1841 | encoded | `o 18 r 16(5) the period for the written submissions [18l]`; `o 18 r 16(5) the written submissions are filed and served in time [18l]` |
| O18 r16(5)(c) | 1842-1843 | encoded | `o 18 r 16(5) the period for the written submissions [18l]`; `o 18 r 16(5) the written submissions are filed and served in time [18l]` |
| O18 r16(5)(d) | 1844-1845 | encoded | `o 18 r 16(5)(d) the period after the filing and service of the notice of appeal [18l]` |
| O18 r16(5)(e) | 1846-1847 | encoded | `o 18 r 16(5) the period for the written submissions [18l]`; `o 18 r 16(5) the written submissions are filed and served in time [18l]` |
| O18 r16(6) | 1848 | fork 18.1 | `o 18 r 16(6) the written submissions include submissions on the appropriate costs orders [18l]`; `o 18 r 16(6) the page limit in pages [18l]`; and 2 more |
| O18 r16(7) | 1849 | fork 18.1 | `o 18 r 16(7) a document other than those set out in the Rule may be filed [18l]` |
| O18 r16(8) | 1850 | encoded | `o 18 r 16(8) the appellate Court may allow the page limit to be exceeded [18l]` |
| O18 r16(8)(a) | 1850-1851 | encoded | `o 18 r 16(8) the appellate Court may allow the page limit to be exceeded [18l]` |
| O18 r16(8)(b) | 1852-1853 | fork 18.1 | `o 18 r 16(8) the appellate Court may allow the page limit to be exceeded [18l]` (note: the text is silent on the amount of the fees for pages in excess of the limit (it says only that they are prescribed): no function computes the fee) |
| O18 r16(9) | 1854 | encoded | `o 18 r 16(9) the appellate Court may upon application waive, refund, defer or apportion the pa…` |
| O18 r16(10) | 1855 | encoded | `o 18 r 16(10) the party may file more than one set of submissions [18l]` |
| O18 Division 3 | 1856 | inert (reason 1) | heading or marker: not operative |
| O18 r17 heading | 1857 | inert (reason 1) | heading or marker: not operative |
| O18 r17(1) | 1858 | fork 18.2 | `o 18 r 17(1) the date after which the 14 days for the notice of appeal run [18l]`; `o 18 r 17(1) the period for the notice of appeal [18l]`; and 1 more |
| O18 r17(1)(a) | 1858-1859 | fork 18.2 | `o 18 r 17(1) the date after which the 14 days for the notice of appeal run [18l]`; `o 18 r 17(1) the period for the notice of appeal [18l]`; and 1 more |
| O18 r17(1)(b) | 1860 | fork 18.2 | `o 18 r 17(1) the date after which the 14 days for the notice of appeal run [18l]`; `o 18 r 17(1) the period for the notice of appeal [18l]`; and 1 more |
| O18 r17(1)(b)(i) | 1861-1862 | fork 18.2 | `o 18 r 17(1) the date after which the 14 days for the notice of appeal run [18l]`; `o 18 r 17(1) the period for the notice of appeal [18l]`; and 1 more |
| O18 r17(1)(b)(ii) | 1863-1864 | fork 18.2 | `o 18 r 17(1) the date after which the 14 days for the notice of appeal run [18l]`; `o 18 r 17(1) the period for the notice of appeal [18l]`; and 1 more |
| O18 r17(2) | 1865 | fork 15.7 | `o 18 r 17(2) the General Division may extend the time for filing and serving the notice of app…`; `o 18 r 17(2) the lower Court may extend the time for filing and serving the notice of appeal […` |
| O18 r18 heading | 1866 | inert (reason 1) | heading or marker: not operative |
| O18 r18(1) | 1867 | encoded | `o 18 r 18(1) the request for further arguments is made as the Rule requires [18l]` |
| O18 r18(2) | 1867 | encoded | `o 18 r 18(2) the request for further arguments is filed in time [18l]` |
| O18 r18(2)(a) | 1867-1868 | encoded | `o 18 r 18(2) the request for further arguments is filed in time [18l]` |
| O18 r18(2)(b) | 1869-1870 | encoded | `o 18 r 18(2) the request for further arguments is filed in time [18l]` |
| O18 r18(3) | 1871 | encoded | `o 18 r 18(3) the request sets out the proposed arguments and a copy of any authority cited [18…` |
| O18 r18(4) | 1872 | encoded | `o 18 r 18(4) the period after receiving the request for informing the requesting party [18l]`; `o 18 r 18(4) the Registrar of the State Courts informs the requesting party in time [18l]` |
| O18 r18(5) | 1873 | encoded | `o 18 r 18(5) it is deemed that the District Judge or Magistrate does not require further argum…` |
| O18 r19 heading | 1874 | inert (reason 1) | heading or marker: not operative |
| O18 r19(1) | 1875 | encoded | `o 18 r 19(1) the period after the date of the decision for applying for permission [18l]`; `o 18 r 19(1) the application for permission to the District Judge or Magistrate is made and se…` |
| O18 r19(2) | 1875 | encoded | `o 18 r 19(2) the application for permission to the General Division is made and served in time…` |
| O18 r19(3) | 1876 | encoded | `o 18 r 19(3) the period after the decision granting permission for the notice of appeal [18l]`; `o 18 r 19(3) the notice of appeal in Form 35 is filed and served in time after permission is g…` |
| O18 r19(4) | 1877 | fork 15.7 | `o 18 r 19(4) the General Division may extend the time for filing and serving an application fo…`; `o 18 r 19(4) the lower Court may extend the time for filing and serving an application for per…` |
| O18 r20 heading | 1878 | inert (reason 1) | heading or marker: not operative |
| O18 r20(1) | 1879 | encoded | `o 18 r 20(1) the appellant has provided security and filed the certificate in Form 36 at the t…`; `o 18 r 20(1) the appellant must provide security and file the certificate [reg]`; and 2 more |
| O18 r20(2) | 1879 | encoded | `o 18 r 20(2) the appellants need to provide only one set of security [18l]` |
| O18 r20(3) | 1880 | fork 18.7 | `o 18 r 20(3) the appellant must provide security for each respondent or each set of respondent…`; `o 18 r 20(3) the security is provided for each set of respondents represented by the same firm…` |
| O18 r20(4) | 1881 | encoded | `o 18 r 20(4) the security is in a form the Rule allows [18l]`; `o 18 r 20(5) kind of action appealed from [18l]` |
| O18 r20(4)(a) | 1881-1882 | encoded | `o 18 r 20(4) the security is in a form the Rule allows [18l]`; `o 18 r 20(5) kind of action appealed from [18l]` |
| O18 r20(4)(b) | 1883-1884 | encoded | `o 18 r 20(4) the security is in a form the Rule allows [18l]`; `o 18 r 20(5) kind of action appealed from [18l]` |
| O18 r20(4)(c) | 1885-1886 | encoded | `o 18 r 20(4) the security is in a form the Rule allows [18l]`; `o 18 r 20(5) kind of action appealed from [18l]` |
| O18 r20(5) | 1887 | encoded | `o 18 r 20(5) the amount of security required [18l]`; `o 18 r 20(5) the security is in the amount required [18l]`; and 1 more |
| O18 r20(5)(a) | 1887-1888 | encoded | `o 18 r 20(5) the amount of security required [18l]`; `o 18 r 20(5) the security is in the amount required [18l]`; and 1 more |
| O18 r20(5)(b) | 1889-1890 | encoded | `o 18 r 20(5) the amount of security required [18l]`; `o 18 r 20(5) the security is in the amount required [18l]`; and 1 more |
| O18 r20(6) | 1891 | encoded | `o 18 r 20(6) any party may apply to the appellate Court to vary or waive the amount of securit…` |
| O18 r20(7) | 1892 | encoded | `o 18 r 20(7) the appellate Court may order further security for costs to be given [18l]` |
| O18 r21 heading | 1893 | inert (reason 1) | heading or marker: not operative |
| O18 r21(1) | 1894 | encoded | `o 18 r 21(1) the District Judge or Magistrate may give a summary of the points decided without…` |
| O18 r21(2) | 1894 | encoded | `o 18 r 21(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 21(2) the District Judge or Magistrate certifies in time [18l]`; and 2 more |
| O18 r21(2)(a) | 1894-1895 | encoded | `o 18 r 21(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 21(2) the District Judge or Magistrate certifies in time [18l]`; and 2 more |
| O18 r21(2)(b) | 1896-1897 | encoded | `o 18 r 21(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 21(2) the District Judge or Magistrate certifies in time [18l]`; and 2 more |
| O18 r21(2)(c) | 1898-1900 | encoded | `o 18 r 21(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 21(2) the District Judge or Magistrate certifies in time [18l]`; and 2 more |
| O18 r21(3) | 1901 | encoded | `o 18 r 21(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 21(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r21(3)(a) | 1901-1902 | encoded | `o 18 r 21(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 21(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r21(3)(b) | 1903 | encoded | `o 18 r 21(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 21(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r21(3)(b)(i) | 1904-1905 | encoded | `o 18 r 21(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 21(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r21(3)(b)(ii) | 1906-1907 | encoded | `o 18 r 21(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 21(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r21(3)(b)(iii) | 1908-1909 | encoded | `o 18 r 21(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 21(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r21(4) | 1910 | encoded | `o 18 r 21(4) the appeal must proceed by way of a rehearing on the documents filed by the parti…`; `o 18 r 21(5) what starts the period for the written submissions [18l]` |
| O18 r21(5) | 1911 | encoded | `o 18 r 21(5) the period for the written submissions [18l]`; `o 18 r 21(5)(a) the period after the notification [18l]`; and 2 more |
| O18 r21(5)(a) | 1911-1912 | encoded | `o 18 r 21(5)(a) the period after the notification [18l]` |
| O18 r21(5)(b) | 1913-1914 | encoded | `o 18 r 21(5) the period for the written submissions [18l]`; `o 18 r 21(5) the written submissions are filed and served in time [18l]` |
| O18 r21(5)(c) | 1915-1916 | encoded | `o 18 r 21(5) the period for the written submissions [18l]`; `o 18 r 21(5) the written submissions are filed and served in time [18l]` |
| O18 r21(5)(d) | 1917-1918 | encoded | `o 18 r 21(5)(d) the period after the filing and service of the notice of appeal [18l]` |
| O18 r21(5)(e) | 1919-1920 | encoded | `o 18 r 21(5) the period for the written submissions [18l]`; `o 18 r 21(5) the written submissions are filed and served in time [18l]` |
| O18 r21(6) | 1921 | fork 18.1 | `o 18 r 21(6) the written submissions include submissions on the appropriate costs orders [18l]`; `o 18 r 21(6) the page limit in pages [18l]`; and 2 more |
| O18 r21(7) | 1922 | encoded | `o 18 r 21(7) the party is required to file separate written submissions [18l]` |
| O18 r21(8) | 1923 | encoded | `o 18 r 21(8) the parties must try to agree on filing a single set of written submissions for e…` |
| O18 r21(9) | 1924 | encoded | `o 18 r 21(9) the parties must request in writing for a case conference before the appellate Co…` |
| O18 r21(10) | 1925 | encoded | `o 18 r 21(10) the parties must inform the Registrar in writing of the timelines agreed and see…` |
| O18 r21(11) | 1926 | fork 18.1 | `o 18 r 21(11) a document other than those set out in the Rule may be filed [18l]` |
| O18 r21(12) | 1927 | fork 18.3, 18.1 | `o 18 r 21(12) the appeal is deemed withdrawn [18l]`; `o 18 r 21(12) the appellant must file and serve the written submissions within the specified t…`; and 2 more |
| O18 r21(13) | 1928 | fork 15.7 | `o 18 r 21(13) the security for costs must be paid and the solicitor's undertaking is discharge…` |
| O18 r21(14) | 1929 | encoded | `o 18 r 21(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 21(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 6 more |
| O18 r21(14)(a) | 1929-1930 | encoded | `o 18 r 21(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 21(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 6 more |
| O18 r21(14)(b) | 1931-1932 | fork 18.1 | `o 18 r 21(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 21(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 6 more |
| O18 r21(14)(c) | 1933-1934 | encoded | `o 18 r 21(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 21(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 6 more |
| O18 r21(15) | 1935 | fork 18.1 | `o 18 r 21(15) the respondent is allowed to make submissions at the hearing of the appeal [18l]`; `o 18 r 21(15) the respondent shall not make submissions at the hearing of the appeal [reg]` |
| O18 r21(16) | 1936 | encoded | `o 18 r 21(16) the appellate Court may allow the page limit to be exceeded [18l]` |
| O18 r21(16)(a) | 1936-1937 | encoded | `o 18 r 21(16) the appellate Court may allow the page limit to be exceeded [18l]` |
| O18 r21(16)(b) | 1938-1939 | fork 18.1 | `o 18 r 21(16) the appellate Court may allow the page limit to be exceeded [18l]` |
| O18 r21(17) | 1940 | encoded | `o 18 r 21(17) the appellate Court may upon application waive, refund, defer or apportion the p…` |
| O18 r21(18) | 1941 | encoded | `o 18 r 21(18) the party may file more than one set of submissions [18l]` |
| O18 r22 heading | 1942 | inert (reason 1) | heading or marker: not operative |
| O18 r22(1) | 1943 | encoded | `o 18 r 22(1) this Rule applies without the need for an order from the Court [18l]`; `o 18 r 22(1) an order from the Court is needed for this Rule to apply [18l]` |
| O18 r22(2) | 1943 | encoded | `o 18 r 22(2) the security for costs must be paid to the respondent towards the costs ordered […`; `o 18 r 22(2) the amount of the security paid to the respondent towards the costs ordered [18l]`; and 1 more |
| O18 r22(3) | 1944 | encoded | `o 18 r 22(3) the security for costs must be paid to the appellant [18l]`; `o 18 r 22(3) the appellant's solicitor is released from any undertaking as to the costs for th…` |
| O18 r23 heading | 1945 | inert (reason 1) | heading or marker: not operative |
| O18 r23 | 1946 | encoded | `o 18 r 23 the step for enforcement is taken as the Rule requires [18l]` |
| O18 Division 4 | 1947 | inert (reason 1) | heading or marker: not operative |
| O18 r24 heading | 1948 | inert (reason 1) | heading or marker: not operative |
| O18 r24 | 1949 | encoded | `o 18 r 24 the period after the date of the Registrar's decision for the notice of appeal [18l]`; `o 18 r 24 the notice of appeal in Form 35 is filed and served in time [18l]` |
| O18 r25 heading | 1950 | inert (reason 1) | heading or marker: not operative |
| O18 r25(1) | 1951 | encoded | `o 18 r 25(1) the Registrar may give a summary of the points decided without the need to issue …` |
| O18 r25(2) | 1951 | encoded | `o 18 r 25(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 25(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r25(2)(a) | 1951-1952 | encoded | `o 18 r 25(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 25(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r25(2)(b) | 1953-1954 | encoded | `o 18 r 25(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 25(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r25(2)(c) | 1955-1957 | encoded | `o 18 r 25(2) the period after the filing of the notice of appeal for the certificate [18l]`; `o 18 r 25(2) the Registrar certifies in time [18l]`; and 2 more |
| O18 r25(3) | 1958 | encoded | `o 18 r 25(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 25(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r25(3)(a) | 1958-1959 | encoded | `o 18 r 25(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 25(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r25(3)(b) | 1960 | encoded | `o 18 r 25(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 25(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r25(3)(b)(i) | 1961-1962 | encoded | `o 18 r 25(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 25(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r25(3)(b)(ii) | 1963-1964 | encoded | `o 18 r 25(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 25(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r25(3)(b)(iii) | 1965-1966 | encoded | `o 18 r 25(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 25(3)(b)(ii) the period of written notice of the intention to strike out [18l]`; and 4 more |
| O18 r25(4) | 1967 | encoded | `o 18 r 25(4) the appeal must proceed by way of a rehearing on the documents filed by the parti…`; `o 18 r 25(5) what starts the period for the written submissions [18l]` |
| O18 r25(5) | 1968 | encoded | `o 18 r 25(5) the period for the written submissions [18l]`; `o 18 r 25(5)(a) the period after the notification [18l]`; and 2 more |
| O18 r25(5)(a) | 1968-1969 | encoded | `o 18 r 25(5)(a) the period after the notification [18l]` |
| O18 r25(5)(b) | 1970-1971 | encoded | `o 18 r 25(5) the period for the written submissions [18l]`; `o 18 r 25(5) the written submissions are filed and served in time [18l]` |
| O18 r25(5)(c) | 1972-1973 | encoded | `o 18 r 25(5) the period for the written submissions [18l]`; `o 18 r 25(5) the written submissions are filed and served in time [18l]` |
| O18 r25(5)(d) | 1974-1975 | encoded | `o 18 r 25(5)(d) the period after the filing and service of the notice of appeal [18l]` |
| O18 r25(5)(e) | 1976-1977 | encoded | `o 18 r 25(5) the period for the written submissions [18l]`; `o 18 r 25(5) the written submissions are filed and served in time [18l]` |
| O18 r25(6) | 1978 | fork 18.1 | `o 18 r 25(6) the written submissions include submissions on the appropriate costs orders [18l]`; `o 18 r 25(6) the page limit in pages [18l]`; and 2 more |
| O18 r25(7) | 1979 | fork 18.1 | `o 18 r 25(7) a document other than those set out in the Rule may be filed [18l]` |
| O18 r25(8) | 1980 | encoded | `o 18 r 25(8) the Judge may allow the page limit to be exceeded [18l]` |
| O18 r25(8)(a) | 1980-1981 | encoded | `o 18 r 25(8) the Judge may allow the page limit to be exceeded [18l]` |
| O18 r25(8)(b) | 1982-1983 | fork 18.1 | `o 18 r 25(8) the Judge may allow the page limit to be exceeded [18l]` |
| O18 r25(9) | 1984 | encoded | `o 18 r 25(9) the Judge may upon application waive, refund, defer or apportion the payment of t…` |
| O18 r25(10) | 1985 | encoded | `o 18 r 25(10) the party may file more than one set of submissions [18l]` |
| O18 Division 5 | 1986 | inert (reason 1) | heading or marker: not operative |
| O18 r26 heading | 1987 | inert (reason 1) | heading or marker: not operative |
| O18 r26 | 1988 | encoded | `o 18 r 26 this Division applies to the appeal or application [18h]` |
| O18 r26(a) | 1988-1989 | encoded | `o 18 r 26 this Division applies to the appeal or application [18h]` |
| O18 r26(b) | 1990-1991 | encoded | `o 18 r 26 this Division applies to the appeal or application [18h]` |
| O18 r26(c) | 1992-1993 | encoded | `o 18 r 26 this Division applies to the appeal or application [18h]` |
| O18 r26(d) | 1994-1995 | encoded | `o 18 r 26 this Division applies to the appeal or application [18h]` |
| O18 r26(e) | 1996-1997 | encoded | `o 18 r 26 this Division applies to the appeal or application [18h]` |
| O18 r27 heading | 1998 | inert (reason 1) | heading or marker: not operative |
| O18 r27(1) | 1999 | fork 18.2 | `o 18 r 27(1) the date after which the 14 days for the notice of appeal run [18h]`; `o 18 r 27(1) the period for the notice of appeal [18h]`; and 1 more |
| O18 r27(1)(a) | 1999-2000 | fork 18.2 | `o 18 r 27(1) the date after which the 14 days for the notice of appeal run [18h]`; `o 18 r 27(1) the period for the notice of appeal [18h]`; and 1 more |
| O18 r27(1)(b) | 2001-2002 | fork 18.2 | `o 18 r 27(1) the date after which the 14 days for the notice of appeal run [18h]`; `o 18 r 27(1) the period for the notice of appeal [18h]`; and 1 more |
| O18 r27(2) | 2003 | fork 15.7 | `o 18 r 27(2) the appellate Court may extend the time for filing and serving the notice of appe…`; `o 18 r 27(2) the lower Court may extend the time for filing and serving the notice of appeal […` |
| O18 r28 heading | 2004 | inert (reason 1) | heading or marker: not operative |
| O18 r28(1) | 2005 | encoded | `o 18 r 28(1) the request for further arguments is made as the Rule requires [18h]` |
| O18 r28(2) | 2006 | encoded | `o 18 r 28(2) the request is made within the time provided in section 29B(2) of the Supreme Cou…` (note: the time limit is set by section 29B of the Supreme Court of Judicature Act, which is outside the sources: compliance with it is taken as an input) |
| O18 r28(3) | 2007 | encoded | `o 18 r 28(3) the request sets out the proposed arguments and a copy of any authority cited [18…` |
| O18 r28(4) | 2008 | encoded | `o 18 r 28(4) the period after receiving the request for informing the requesting party [18h]`; `o 18 r 28(4) the Registrar of the Supreme Court informs the requesting party in time [18h]` |
| O18 r28(5) | 2009 | encoded | `o 18 r 28(5) it is deemed that the Judge does not require further arguments [18h]` |
| O18 r29 heading | 2010 | inert (reason 1) | heading or marker: not operative |
| O18 r29(1) | 2011 | encoded | `o 18 r 29(1) the period after the date of the lower Court's decision for the application for p…`; `o 18 r 29(1) the application for permission to the appellate Court is made in time [18h]` |
| O18 r29(2) | 2011 | encoded | `o 18 r 29(2) the Judge who made the decision may hear further arguments in respect of the deci…`; `o 18 r 29(2)(b) the 15th day after the date on which the decision is made [18h]` |
| O18 r29(2)(a) | 2011-2012 | encoded | `o 18 r 29(2) the Judge who made the decision may hear further arguments in respect of the deci…`; `o 18 r 29(2)(b) the 15th day after the date on which the decision is made [18h]` |
| O18 r29(2)(b) | 2013-2014 | encoded | `o 18 r 29(2) the Judge who made the decision may hear further arguments in respect of the deci…`; `o 18 r 29(2)(b) the 15th day after the date on which the decision is made [18h]` |
| O18 r29(2)(c) | 2015-2016 | encoded | `o 18 r 29(2) the Judge who made the decision may hear further arguments in respect of the deci…`; `o 18 r 29(2)(b) the 15th day after the date on which the decision is made [18h]` |
| O18 r29(3) | 2017 | encoded | `o 18 r 29(3)(a) an application for permission to appeal against the decision may be filed [18h]`; `o 18 r 29(3)(a) an application for permission to appeal against the decision is barred from be…`; and 2 more |
| O18 r29(3)(a) | 2017 | fork 18.6 | `o 18 r 29(3)(a) an application for permission to appeal against the decision may be filed [18h]`; `o 18 r 29(3)(a) an application for permission to appeal against the decision is barred from be…` |
| O18 r29(3)(a)(i) | 2018-2019 | encoded | `o 18 r 29(3)(a) an application for permission to appeal against the decision may be filed [18h]`; `o 18 r 29(3)(a) an application for permission to appeal against the decision is barred from be…` |
| O18 r29(3)(a)(ii) | 2020-2021 | encoded | `o 18 r 29(3)(a) an application for permission to appeal against the decision may be filed [18h]`; `o 18 r 29(3)(a) an application for permission to appeal against the decision is barred from be…` |
| O18 r29(3)(b) | 2022 | encoded | `o 18 r 29(3)(b) the period after the Judge’s further decision for the application for permissi…`; `o 18 r 29(3)(b) the application for permission and the paragraph (7) documents are filed and s…` |
| O18 r29(3)(b)(i) | 2023-2024 | encoded | `o 18 r 29(3)(b) the period after the Judge’s further decision for the application for permissi…`; `o 18 r 29(3)(b) the application for permission and the paragraph (7) documents are filed and s…` |
| O18 r29(3)(b)(ii) | 2025-2026 | encoded | `o 18 r 29(3)(b) the period after the Judge’s further decision for the application for permissi…`; `o 18 r 29(3)(b) the application for permission and the paragraph (7) documents are filed and s…` |
| O18 r29(4) | 2027 | encoded | `o 18 r 29(4) paragraphs (2) and (3) do not affect section 29B of the Supreme Court of Judicatu…`; `o 18 r 29(5)(b) kind of relevant matter [18h]` |
| O18 r29(5) | 2028 | encoded | `o 18 r 29(5) the Court of Appeal may grant permission to appeal against a decision of the Appe…`; `o 18 r 29(5)(b) the matter is one that the Court of Appeal is to have regard to [18h]` |
| O18 r29(5)(a) | 2028-2029 | encoded | `o 18 r 29(5) the Court of Appeal may grant permission to appeal against a decision of the Appe…`; `o 18 r 29(5)(b) the matter is one that the Court of Appeal is to have regard to [18h]` |
| O18 r29(5)(b) | 2030 | encoded | `o 18 r 29(5) the Court of Appeal may grant permission to appeal against a decision of the Appe…`; `o 18 r 29(5)(b) the matter is one that the Court of Appeal is to have regard to [18h]` |
| O18 r29(5)(b)(i) | 2031-2032 | encoded | `o 18 r 29(5) the Court of Appeal may grant permission to appeal against a decision of the Appe…`; `o 18 r 29(5)(b) the matter is one that the Court of Appeal is to have regard to [18h]` |
| O18 r29(5)(b)(ii) | 2033-2034 | encoded | `o 18 r 29(5) the Court of Appeal may grant permission to appeal against a decision of the Appe…`; `o 18 r 29(5)(b) the matter is one that the Court of Appeal is to have regard to [18h]` |
| O18 r29(6) | 2035 | encoded | `o 18 r 29(6) the period after the Registrar’s notification for the application for permission …`; `o 18 r 29(6) the party applies to the relevant appellate Court for permission in time [18h]` |
| O18 r29(6)(a) | 2035-2036 | encoded | `o 18 r 29(6) the period after the Registrar’s notification for the application for permission …`; `o 18 r 29(6) the party applies to the relevant appellate Court for permission in time [18h]` |
| O18 r29(6)(b) | 2037-2039 | encoded | `o 18 r 29(6) the period after the Registrar’s notification for the application for permission …`; `o 18 r 29(6) the party applies to the relevant appellate Court for permission in time [18h]` |
| O18 r29(7) | 2040 | encoded | `o 18 r 29(7)(a) the written submissions and any bundle of authorities are filed at the time of…`; `o 18 r 29(7)(b) the party may file a bundle of documents with the application [18h]`; and 1 more |
| O18 r29(7)(a) | 2040-2041 | encoded | `o 18 r 29(7)(a) the written submissions and any bundle of authorities are filed at the time of…` |
| O18 r29(7)(b) | 2042-2043 | encoded | `o 18 r 29(7)(b) the party may file a bundle of documents with the application [18h]` |
| O18 r29(8) | 2044 | encoded | `o 18 r 29(8) the period after service of the application for the opposing party’s submissions …`; `o 18 r 29(8) the opposing party's written submissions are filed and served in time [18h]` |
| O18 r29(8)(a) | 2044-2045 | encoded | `o 18 r 29(8) the period after service of the application for the opposing party’s submissions …`; `o 18 r 29(8) the opposing party's written submissions are filed and served in time [18h]` |
| O18 r29(8)(b) | 2046-2048 | encoded | `o 18 r 29(8) the period after service of the application for the opposing party’s submissions …`; `o 18 r 29(8) the opposing party's written submissions are filed and served in time [18h]` |
| O18 r29(9) | 2049 | encoded | `o 18 r 29(9) the application, written submissions and bundles are served on all parties who ha…` |
| O18 r29(10) | 2050 | fork 18.1 | `o 18 r 29(10) the written submissions are subject to a page limit of 15 pages [18h]`; `o 18 r 29(10) the number of pages is within the page limit of 15 pages [18h]`; and 1 more |
| O18 r29(11) | 2051 | encoded | `o 18 r 29(11) the number of pages of the bundle of documents is within the page limit of 25 pa…` |
| O18 r29(12) | 2052 | encoded | `o 18 r 29(12) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r29(12)(a) | 2052-2053 | encoded | `o 18 r 29(12) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r29(12)(b) | 2054-2055 | fork 18.1 | `o 18 r 29(12) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r29(13) | 2056 | encoded | `o 18 r 29(13) the appellate Court may upon application waive, refund, defer or apportion the p…` |
| O18 r29(14) | 2057 | fork 18.1 | `o 18 r 29(14) the party may file more than one set of submissions [18h]` |
| O18 r29(15) | 2058 | encoded | `o 18 r 29(15) an affidavit may be filed in the application for permission to appeal [18h]` |
| O18 r29(16) | 2059 | fork 18.1 | `o 18 r 29(16) oral arguments may be made in the application for permission to appeal [18h]` |
| O18 r29(17) | 2060 | encoded | `o 18 r 29(17) the period after the decision granting permission for the notice of appeal [18h]`; `o 18 r 29(17) the notice of appeal in Form 35 is filed and served in time after permission is …` |
| O18 r29(18) | 2061 | encoded | `o 18 r 29(18) the appellate Court may extend the time for filing and serving an application fo…` |
| O18 r30 heading | 2062 | inert (reason 1) | heading or marker: not operative |
| O18 r30(1) | 2063 | encoded | `o 18 r 30(1) the appellant has provided security and filed the certificate in Form 36 at the t…` |
| O18 r30(2) | 2063 | encoded | `o 18 r 30(2) the appellants need to provide only one set of security [18h]` |
| O18 r30(3) | 2064 | fork 18.7 | `o 18 r 30(3) the appellant must provide security for each respondent or each set of respondent…`; `o 18 r 30(3) the security is provided for each set of respondents represented by the same firm…` |
| O18 r30(4) | 2065 | encoded | `o 18 r 30(4) the security is in a form the Rule allows [18h]` |
| O18 r30(4)(a) | 2065-2066 | encoded | `o 18 r 30(4) the security is in a form the Rule allows [18h]` |
| O18 r30(4)(b) | 2067-2068 | encoded | `o 18 r 30(4) the security is in a form the Rule allows [18h]` |
| O18 r30(4)(c) | 2069-2070 | encoded | `o 18 r 30(4) the security is in a form the Rule allows [18h]` |
| O18 r30(5) | 2071 | encoded | `o 18 r 30(5) the amount of security required [18h]`; `o 18 r 30(5) the security is in the amount required [18h]`; and 1 more |
| O18 r30(6) | 2072 | encoded | `o 18 r 30(6) any party may apply to the appellate Court to vary or waive the amount of securit…` |
| O18 r30(7) | 2073 | encoded | `o 18 r 30(7) the appellate Court may order further security for costs to be given [18h]` |
| O18 r31 heading | 2074 | inert (reason 1) | heading or marker: not operative |
| O18 r31(1) | 2075 | encoded | `o 18 r 31(1) the appellate Court may give directions for the filing and service of such joint …` |
| O18 r31(2) | 2075 | encoded | `o 18 r 31(2) the directions in paragraph (1) may be given on the appellate Court’s own motion …` |
| O18 r31(3) | 2076 | encoded | `o 18 r 31(3) the appellate Court may give directions under paragraph (1) even if the related a…` |
| O18 r31(4) | 2077 | encoded | `o 18 r 31(4) the appellate Court may direct any modifications of the rules that are applicable…` |
| O18 r32 heading | 2078 | inert (reason 1) | heading or marker: not operative |
| O18 r32(1) | 2079 | encoded | `o 18 r 32(1) the appellate Court may, if it deems appropriate, order that this Division or any…` |
| O18 r32(1)(a) | 2079-2080 | encoded | `o 18 r 32(1) the appellate Court may, if it deems appropriate, order that this Division or any…` |
| O18 r32(1)(b) | 2081-2082 | encoded | `o 18 r 32(1) the appellate Court may, if it deems appropriate, order that this Division or any…` |
| O18 r32(2) | 2083 | encoded | `o 18 r 32(2) the appellate Court may in any case, if it deems appropriate, order or direct any…` |
| O18 r32(3) | 2084 | encoded | `o 18 r 32(3) the appellate Court may make an order or give a direction pursuant to this Rule o…` |
| O18 r33 heading | 2085 | inert (reason 1) | heading or marker: not operative |
| O18 r33(1) | 2086 | encoded | `o 18 r 33(1) the lower Court may give a summary of the points decided without the need to issu…` |
| O18 r33(2) | 2086 | encoded | `o 18 r 33(2) the period after the filing of the notice of appeal for the certificate [18h]`; `o 18 r 33(2) the lower Court certifies in time [18h]`; and 2 more |
| O18 r33(2)(a) | 2086-2087 | encoded | `o 18 r 33(2) the period after the filing of the notice of appeal for the certificate [18h]`; `o 18 r 33(2) the lower Court certifies in time [18h]`; and 2 more |
| O18 r33(2)(b) | 2088-2089 | encoded | `o 18 r 33(2) the period after the filing of the notice of appeal for the certificate [18h]`; `o 18 r 33(2) the lower Court certifies in time [18h]`; and 2 more |
| O18 r33(2)(c) | 2090-2092 | encoded | `o 18 r 33(2) the period after the filing of the notice of appeal for the certificate [18h]`; `o 18 r 33(2) the lower Court certifies in time [18h]`; and 2 more |
| O18 r33(3) | 2093 | encoded | `o 18 r 33(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 33(3)(b)(ii) the period of written notice of the intention to strike out [18h]`; and 4 more |
| O18 r33(3)(a) | 2093-2094 | encoded | `o 18 r 33(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 33(3)(b)(ii) the period of written notice of the intention to strike out [18h]`; and 4 more |
| O18 r33(3)(b) | 2095 | encoded | `o 18 r 33(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 33(3)(b)(ii) the period of written notice of the intention to strike out [18h]`; and 4 more |
| O18 r33(3)(b)(i) | 2096-2097 | encoded | `o 18 r 33(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 33(3)(b)(ii) the period of written notice of the intention to strike out [18h]`; and 4 more |
| O18 r33(3)(b)(ii) | 2098-2099 | encoded | `o 18 r 33(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 33(3)(b)(ii) the period of written notice of the intention to strike out [18h]`; and 4 more |
| O18 r33(3)(b)(iii) | 2100-2101 | encoded | `o 18 r 33(3)(b) the period after the certification before the appellant must apply to proceed …`; `o 18 r 33(3)(b)(ii) the period of written notice of the intention to strike out [18h]`; and 4 more |
| O18 r33(4) | 2102 | encoded | `o 18 r 33(4) the appeal must proceed by way of a rehearing on the documents filed by the parti…`; `o 18 r 33(5) what starts the period for the written submissions [18h]` |
| O18 r33(5) | 2103 | encoded | `o 18 r 33(5) the period for the written submissions [18h]`; `o 18 r 33(5)(a) the period after the notification [18h]`; and 2 more |
| O18 r33(5)(a) | 2103-2104 | encoded | `o 18 r 33(5)(a) the period after the notification [18h]` |
| O18 r33(5)(b) | 2105-2106 | encoded | `o 18 r 33(5) the period for the written submissions [18h]`; `o 18 r 33(5) the written submissions are filed and served in time [18h]` |
| O18 r33(5)(c) | 2107-2108 | encoded | `o 18 r 33(5) the period for the written submissions [18h]`; `o 18 r 33(5) the written submissions are filed and served in time [18h]` |
| O18 r33(5)(d) | 2109-2110 | encoded | `o 18 r 33(5)(d) the period after the filing and service of the notice of appeal [18h]` |
| O18 r33(5)(e) | 2111-2112 | encoded | `o 18 r 33(5) the period for the written submissions [18h]`; `o 18 r 33(5) the written submissions are filed and served in time [18h]` |
| O18 r33(6) | 2113 | fork 18.1 | `o 18 r 33(6) the written submissions include submissions on the appropriate costs orders [18h]`; `o 18 r 33(6) the page limit in pages [18h]`; and 2 more |
| O18 r33(7) | 2114 | encoded | `o 18 r 33(7) the party is required to file separate written submissions [18h]` |
| O18 r33(8) | 2115 | encoded | `o 18 r 33(8) the parties must try to agree on filing a single set of written submissions for e…` |
| O18 r33(9) | 2116 | encoded | `o 18 r 33(9) the parties must request in writing for a case conference before the appellate Co…` |
| O18 r33(10) | 2117 | encoded | `o 18 r 33(10) the parties must inform the Registrar in writing of the timelines agreed and see…` |
| O18 r33(11) | 2118 | fork 18.1 | `o 18 r 33(11) a document other than those set out in the Rule may be filed [18h]` |
| O18 r33(12) | 2119 | fork 18.3, 18.1 | `o 18 r 33(12) the appeal is deemed withdrawn [18h]`; `o 18 r 33(12) the appellant must file and serve the written submissions within the specified t…`; and 2 more |
| O18 r33(13) | 2120 | fork 15.7 | `o 18 r 33(13) the security for costs must be paid and the solicitor's undertaking is discharge…` |
| O18 r33(14) | 2121 | encoded | `o 18 r 33(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 33(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 3 more |
| O18 r33(14)(a) | 2121-2122 | encoded | `o 18 r 33(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 33(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 3 more |
| O18 r33(14)(b) | 2123-2124 | fork 18.1 | `o 18 r 33(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 33(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 3 more |
| O18 r33(14)(c) | 2125-2126 | encoded | `o 18 r 33(14)(a) the period after the appeal is deemed withdrawn for the request for direction…`; `o 18 r 33(14)(a) the appellant or any party to the appeal may request in writing to the appell…`; and 3 more |
| O18 r33(15) | 2127 | fork 18.1 | `o 18 r 33(15) the respondent is allowed to make submissions at the hearing of the appeal [18h]` |
| O18 r33(16) | 2128 | encoded | `o 18 r 33(16) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r33(16)(a) | 2128-2129 | encoded | `o 18 r 33(16) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r33(16)(b) | 2130-2131 | fork 18.1 | `o 18 r 33(16) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r33(17) | 2132 | encoded | `o 18 r 33(17) the appellate Court may upon application waive, refund, defer or apportion the p…` |
| O18 r33(18) | 2133 | encoded | `o 18 r 33(18) the party may file more than one set of submissions [18h]` |
| O18 r34 heading | 2134 | inert (reason 1) | heading or marker: not operative |
| O18 r34(1) | 2135 | encoded | `o 18 r 34(1) this Rule applies without the need for an order from the Court [18h]`; `o 18 r 34(1) an order from the Court is needed for this Rule to apply [18h]` |
| O18 r34(2) | 2135 | encoded | `o 18 r 34(2) the security for costs must be paid to the respondent towards the costs ordered […`; `o 18 r 34(2) the amount of the security paid to the respondent towards the costs ordered [18h]`; and 1 more |
| O18 r34(3) | 2136 | encoded | `o 18 r 34(3) the security for costs must be paid to the appellant [18h]`; `o 18 r 34(3) the appellant's solicitor is released from any undertaking as to the costs for th…` |
| O18 r34(4) | 2137 | encoded | `o 18 r 34(4) paragraphs (2) and (3) apply to the payment out of security for costs given under…` |
| O18 r35 heading | 2138 | inert (reason 1) | heading or marker: not operative |
| O18 r35(1) | 2139 | encoded | `o 18 r 35(1) the application to the appellate Court is made in the form the Rule requires [18h]` |
| O18 r35(2) | 2139 | fork 18.8 | `o 18 r 35(2) the application may be made in the first instance to the appellate Court [18h]` |
| O18 r35(3) | 2140 | fork 18.1 | `o 18 r 35(3) oral arguments may be made in an application to the appellate Court [18h]` |
| O18 r35(4) | 2141 | encoded | `o 18 r 35(4) the period after service of the application for the affidavit in reply [18h]`; `o 18 r 35(4) the affidavit in reply is filed and served in time [18h]`; and 1 more |
| O18 r35(5) | 2142 | encoded | `o 18 r 35(5) the applicant has provided security and filed the certificate in Form 36 at the t…` |
| O18 r35(6) | 2143 | encoded | `o 18 r 35(6) the applicants need to provide only one set of security [18h]` |
| O18 r35(7) | 2144 | fork 18.7 | `o 18 r 35(7) the applicant must provide security for each opposing party or each set of opposi…`; `o 18 r 35(7) the security is provided for each set of opposing parties represented by the same…` |
| O18 r35(8) | 2145 | encoded | `o 18 r 35(8) the security is in a form the Rule allows [18h]` |
| O18 r35(8)(a) | 2145-2146 | encoded | `o 18 r 35(8) the security is in a form the Rule allows [18h]` |
| O18 r35(8)(b) | 2147-2148 | encoded | `o 18 r 35(8) the security is in a form the Rule allows [18h]` |
| O18 r35(8)(c) | 2149-2150 | encoded | `o 18 r 35(8) the security is in a form the Rule allows [18h]` |
| O18 r35(9) | 2151 | encoded | `o 18 r 35(9) the amount of security required [18h]`; `o 18 r 35(9) the security is in the amount required [18h]`; and 1 more |
| O18 r35(10) | 2152 | encoded | `o 18 r 35(10) any party may apply to the appellate Court to vary or waive the amount of securi…` |
| O18 r35(11) | 2153 | encoded | `o 18 r 35(11) the appellate Court may order further security for costs to be given [18h]` |
| O18 r35(12) | 2154 | encoded | `o 18 r 35(12) the application to strike out a notice of appeal is made as the Rule requires [1…` |
| O18 r35(13) | 2155 | encoded | `o 18 r 35(13) the period after service of the notice of appeal for the summons to strike out […`; `o 18 r 35(13) the summons and the supporting affidavit are filed and served in time [18h]` |
| O18 r35(14) | 2156 | encoded | `o 18 r 35(14) the period after service of the summons to strike out for the affidavit in reply…`; `o 18 r 35(14) the affidavit in reply to the summons to strike out is filed and served in time …` |
| O18 r35(15) | 2157 | encoded | `o 18 r 35(15) a further affidavit may be received in evidence [18h]` |
| O18 r36 heading | 2158 | inert (reason 1) | heading or marker: not operative |
| O18 r36 | 2159 | encoded | `o 18 r 36 the period after the direction or order for the application for permission [18h]`; `o 18 r 36 the application for permission is filed and served in time [18h]` |
| O18 r36(a) | 2159-2160 | encoded | `o 18 r 36 the period after the direction or order for the application for permission [18h]`; `o 18 r 36 the application for permission is filed and served in time [18h]` |
| O18 r36(b) | 2161-2163 | encoded | `o 18 r 36 the period after the direction or order for the application for permission [18h]`; `o 18 r 36 the application for permission is filed and served in time [18h]` |
| O18 r37 heading | 2164 | inert (reason 1) | heading or marker: not operative |
| O18 r37(1) | 2165 | fork 18.1 | `o 18 r 37(1) the period after the date the opposing party’s affidavit in reply is to be filed …`; `o 18 r 37(1) the written submissions and bundles of authorities are filed and served in time […` |
| O18 r37(2) | 2165 | fork 18.1 | `o 18 r 37(2) the written submissions are subject to a page limit of 35 pages [18h]`; `o 18 r 37(2) the number of pages is within the page limit of 35 pages [18h]` |
| O18 r37(3) | 2166 | encoded | `o 18 r 37(3) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r37(3)(a) | 2166-2167 | encoded | `o 18 r 37(3) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r37(3)(b) | 2168-2169 | fork 18.1 | `o 18 r 37(3) the appellate Court may allow the page limit to be exceeded [18h]` |
| O18 r37(4) | 2170 | encoded | `o 18 r 37(4) the appellate Court may upon application waive, refund, defer or apportion the pa…` |
| O18 r37(5) | 2171 | fork 18.1 | `o 18 r 37(5) the party may file more than one set of submissions [18h]` |
| O18 r37(6) | 2172 | encoded | `o 18 r 37(6) the concluding paragraphs of the written submissions are as the Rule requires [18…` |
| O18 r37(6)(a) | 2172-2173 | encoded | `o 18 r 37(6) the concluding paragraphs of the written submissions are as the Rule requires [18…` |
| O18 r37(6)(b) | 2174-2175 | encoded | `o 18 r 37(6) the concluding paragraphs of the written submissions are as the Rule requires [18…` |
| O18 r38 heading | 2176 | inert (reason 1) | heading or marker: not operative |
| O18 r38 | 2177 | fork 15.7, 18.1 | `o 18 r 38 further arguments from the parties are allowed [18h]`; `o 18 r 39(1) kind of direction or order [18h]` |
| O18 r39 heading | 2178 | inert (reason 1) | heading or marker: not operative |
| O18 r39(1) | 2179 | fork 18.9 | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(a) | 2179-2180 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(b) | 2181 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(b)(i) | 2182-2183 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(b)(ii) | 2184-2185 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(b)(iii) | 2186-2187 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(c) | 2188-2189 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(d) | 2190-2191 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(e) | 2192-2193 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(1)(f) | 2194-2195 | encoded | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division and the Court of …` |
| O18 r39(2) | 2196 | encoded | `o 18 r 39(2) the period after the Registrar’s direction or order for the application to vary o…`; `o 18 r 39(2) the application to vary or discharge a direction or order of the Registrar is mad…`; and 1 more |
| O18 r40 heading | 2197 | inert (reason 1) | heading or marker: not operative |
| O18 r40(1) | 2198 | encoded | `o 18 r 40(1) the Court of Appeal may exercise its power under section 29D(1)(a) on an applicat…` |
| O18 r40(2) | 2198 | encoded | `o 18 r 40(2) the Court of Appeal may exercise its power under section 29D(1)(a) on its own mot…` |
| O18 r40(2)(a) | 2198-2199 | encoded | `o 18 r 40(2) the Court of Appeal may exercise its power under section 29D(1)(a) on its own mot…` |
| O18 r40(2)(b) | 2200-2201 | encoded | `o 18 r 40(2) the Court of Appeal may exercise its power under section 29D(1)(a) on its own mot…` |
| O18 r40(2)(c) | 2202-2203 | encoded | `o 18 r 40(2) the Court of Appeal may exercise its power under section 29D(1)(a) on its own mot…` |
| O18 r40(3) | 2204 | encoded | `o 18 r 40(3) the period after service of the notice of appeal for the application under sectio…`; `o 18 r 40(3) the application under section 29D(2)(c)(i) is filed and served in time [18h]` |
| O18 r40(4) | 2205 | encoded | `o 18 r 40(4) the period after the date the written submissions are required for the applicatio…`; `o 18 r 40(4) the application under section 29D(2)(c)(ii) is filed and served in time [18h]`; and 1 more |
| O18 r40(5) | 2206 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r40(5)(a) | 2206-2207 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r40(5)(b) | 2208-2209 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r40(5)(c) | 2210-2211 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r40(5)(d) | 2212-2213 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r40(5)(e) | 2214-2215 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r40(5)(f) | 2216-2217 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r40(5)(g) | 2218-2219 | encoded | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]`; `o 18 r 41(1) matter the Court of Appeal is to have regard to [18h]` |
| O18 r41 heading | 2220 | inert (reason 1) | heading or marker: not operative |
| O18 r41(1) | 2221 | encoded | `o 18 r 41(1) the Court of Appeal is to have regard to the matter [18h]` (note: the text lists the matters the Court of Appeal may have regard to and is silent on how they decide the application: no function states an outcome) |
| O18 r41(1)(a) | 2221-2222 | encoded | `o 18 r 41(1) the Court of Appeal is to have regard to the matter [18h]` |
| O18 r41(1)(b) | 2223-2224 | encoded | `o 18 r 41(1) the Court of Appeal is to have regard to the matter [18h]` |
| O18 r41(1)(c) | 2225-2226 | encoded | `o 18 r 41(1) the Court of Appeal is to have regard to the matter [18h]` |
| O18 r41(2) | 2227 | encoded | `o 18 r 41(2) the period after service of the notice of appeal for the application under sectio…`; `o 18 r 41(2) the application under section 29E(2)(b) is made and served in time [18h]` |
| O18 r41(2)(a) | 2227-2228 | encoded | `o 18 r 41(2) the period after service of the notice of appeal for the application under sectio…`; `o 18 r 41(2) the application under section 29E(2)(b) is made and served in time [18h]` |
| O18 r41(2)(b) | 2229-2230 | encoded | `o 18 r 41(2) the period after service of the notice of appeal for the application under sectio…`; `o 18 r 41(2) the application under section 29E(2)(b) is made and served in time [18h]` |

## Fork register (roc3)

The rulings E1 and N2 below are copied word for word from the brief.
The two rulings of 2026-11-05 are put in this row's own short words, with the times Meng typed them; the lead replaces them with the guide's text at the merge.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**Where option B was used.**
Nowhere by name.
Order 18 repeats four "documents to be filed" rules, three "security for costs" rules and two "payment out" rules; each section answers for itself (option C), and no function gathers the routes to one legal effect.

Each fork below states the readings, the text that licenses each, the one taken, and where it is encoded.

**15.1 (O 15 r 1(1) and (3)): does paragraph (1) reach an appeal to the Appellate Division or the Court of Appeal?**
(A) Paragraph (1) says "every originating application, summons, assessment of damages, taking of accounts and appeal must be heard in chambers", so an appeal to the Appellate Division or the Court of Appeal is caught by (1), and (3) ("must be heard in open court unless ... otherwise orders") contradicts it.
(B) Paragraph (3) is the specific rule for those two courts; (1) governs the other appeals.
**Taken: B.** An application or appeal to the Appellate Division or the Court of Appeal is a kind of its own (`o 15 r 1(3) an application or appeal to the Appellate Division or the Court of Appeal`); (1) answers `NOTHING` for it, and (3) answers.
Encoded in `o 15 r 1(1) the matter must be heard in chambers` and `o 15 r 1(3) the matter must be heard in open court`.

**15.2 (O 15 r 1(4)): "Subject to paragraphs (1) to (3) and any written law".**
(A) Paragraphs (1) to (3) are the starting position and (4) lets the Court switch a matter from chambers to court or the reverse.
(B) Where (1) to (3) say "must", (4) cannot switch.
**Taken: A**, because under B paragraph (4) would never apply to a matter paragraphs (1) to (3) mention.
The "written law" limb is an input and answers `NOTHING` (the written law is outside the sources).

**15.3 (O 15 r 12(1)(a)): "orally at the conclusion of the hearing or on a subsequent date with the parties present".**
(A) "With the parties present" limits only the subsequent date. (B) It limits both.
**Taken: A.** A decision given orally on a later date without the parties present answers `NOTHING` under (a); (b) covers a decision in writing.
Reviewer expected `JUST FALSE` or `JUST TRUE` (the reviewer's value for this row was not given to the encoder); open question.

**15.4 (O 15 r 16(1)): "As a general rule".**
(A) The words state a default that has exceptions (so the rule names no exception and the case outside the three proceedings answers `NOTHING`). (B) They make the rule exceptionless within the three proceedings.
**Taken: A.** The rule is stated as a rule limited by its own wording.

**15.5 (O 15 r 16(7)): "at the time that party serves on the other parties the affidavits".**
(A) The same day. (B) At the same moment.
**Taken: A**, because the Rules count in days and the input is a date; a notice given on another day answers `JUST FALSE` (ruling of 2026-11-05 (a)).

**15.6 (O 15 r 18): "An affidavit is a statement of evidence in the English language, signed and affirmed before a commissioner for oaths."**
(A) A definition: a document lacking any of the four elements is not an affidavit (`JUST FALSE`). (B) A description of the usual affidavit (`NOTHING`).
**Taken: A**, because the rule is headed as the definition of an affidavit in the Division.


**15.7 (many rows): readings the rulings of 2026-11-05 do not decide.**
*Assumed, not ruled, and applied:*
(i) "in such event" (O 18 r 12(2), r 21(13), r 33(13): "must file the document signifying such consent ... and in such event, the security for costs must be paid") counts as "in the event of", so as "where": with the document not filed the answer is `JUST FALSE`.
(ii) "once" and "in the event of" do not occur in lines 1405-2230; "whenever" occurs once (O 18 r 35(2), fork 18.8) and "while" not at all.
(iii) A function that returns a number, a date or a record cannot carry `JUST FALSE`, so a yes/no twin carries the no: `o 18 r 3(1A) the time starts to run after the expiry of the 30-day period`, `o 18 r 3(2)(c)(i) ...` and `o 18 r 3(2)(c)(ii) ...`, `o 18 r 3(2)(d) ... runs from the Court's ruling on further arguments` (each the twin of a date function), and `o 17 r 5(3) interest is to be calculated from the date that each instalment is due` (the twin of the interest figure, written in the first round).
*Left at `NOTHING`, because the ruling names no trigger word or because the trigger starts a prohibition (the other reading is `JUST FALSE`):*
(iv) Occasion phrases: "At the conclusion of the claimant's case" (O 15 r 8(11)), "At the conclusion of the evidence for all the parties" (r 8(12)), "On the hearing of the application for directions" (r 15(5)), "after the appellate Court has heard the appeal and reserved its decision" (O 18 r 38), "on application" and "on the appellant's application made at any time" (O 16 r 2(10); O 18 r 17(2), r 19(4), r 27(2)).
(v) "In special circumstances" and "In a special case" (O 15 r 16(2); O 18 r 16(8), r 21(16), r 25(8), r 29(12), r 33(16), r 37(3)).
(vi) "Subject to" and "Except as provided" (O 15 r 1(6): space, security and the interests of justice; r 8(5); O 18 r 3(1), r 4(1), r 12(4)).
(vii) A "where", "if" or "whenever" that starts a prohibition, when the question asked is the permission: O 15 r 8(11)(c); O 18 r 21(15) and r 33(15) ("Where the respondent ... fails to file ..., the respondent is not allowed ..."); r 29(3)(a) ("If a request ... has been made ... may not be filed ... until the Judge"); r 35(2) ("Whenever ... it must not be made in the first instance to the appellate Court").
A trigger that is not met leaves the prohibition off and says nothing of permission, so the answer is `NOTHING`; where ruling (d) calls for it the bar has its own yes/no question (fork 18.6).
(viii) A window described by a state and not by a period: O 15 r 26(1) "after it has been affirmed but not filed in Court".
(ix) "In the case of ..." with no trigger word as a scope limit: O 15 r 19(2) (fork 15.10) and O 18 r 3(2)(b).
*Applied, found by a scan of every "upon", "when" and "whenever" in the range (the first re-read had missed them):*
(x) "may upon application waive, refund, defer or apportion the payment of the fees" (O 18 r 16(9), r 21(17), r 25(9), r 29(13), r 33(17), r 37(4)) counts as "where an application is made": each takes `an application has been made to waive, refund, defer or apportion the payment of the fees`, and without one the answer is `JUST FALSE`.
Not a condition, because the text gives the other way in the same sentence: O 15 r 4(4) ("upon application by any person or on the Registrar's own motion"), O 18 r 11(1) ("upon any party's application or on its own accord"), r 31(2) ("on its own motion or on the application or request of any party"); nor where "upon" belongs to the content of a thing the Rule describes: O 15 r 4(10) and r 4(11) ("undertakes to pay upon request").
*Period-shaped words that stay `NOTHING` (the other reading is `JUST FALSE`), found by the period audit of 2026-11-05 (see Seams):*
(xi) A period that bounds a prohibition: O 18 r 38 ("no further arguments from the parties after the appellate Court has heard the appeal and reserved its decision").
A period the text does not fix, because another Act sets it: O 18 r 28(2) ("within the time provided in section 29B(2) of the Supreme Court of Judicature Act").
No window at all, because the words are "at any time": the General Division's and the appellate Court's powers to extend time in O 18 r 17(2), r 19(4) and r 27(2) ("on the appellant's application made at any time").
A scope or occasion that only sounds like a time: O 15 r 9 ("before he or she gives evidence in Court"), O 18 r 6(3) ("for such time as enforcement has been delayed by the appeal"), O 18 r 18(1) and r 28(1) (a request made "after" a decision), O 15 r 26(1) (item (viii)).
A target and not a bar, so no function tests a time against it: "as soon as it is practicable" (O 18 r 16(3)(a), r 21(3)(a), r 25(3)(a), r 33(3)(a)) and "a reasonable time" (O 17 r 2(2)).
The "until" bars of ruling (d) are the bar functions of fork 18.6.
Taken: as stated in each item.

**15.8 (O 15 r 7(2) and r 8(2)): "with the assistance of one or 2 assessors".**
(A) A ceiling that "only" does not close: three or more assessors answer `NOTHING`. (B) The words close the number at one or two, so three answers `JUST FALSE`.
**Taken: A** (`o 15 r 7(2) the Judge may hear the matter with the assistance of assessors` and r 8(2) take the number).

**15.9 (O 15 r 11(11)): "kept for 5 years beginning from the last day of the hearing".**
(A) The last day of the hearing is day 1 of the five years. (B) Day 1 is the day after.
**Not decided here.** The function takes "the last day for doing the act, counted under O 3 r 3" as an input, so which day is day 1 is the caller's to count (seam S-T1); the constant `o 15 r 11(11) the time the official record must be kept` says 60 months (NEEDS-CORE.md).

**15.10 (O 15 r 19(2)): "In the case of affidavits filed as evidence-in-chief in an originating claim".**
(A) A scope limit with no "only" (ruling (c)): an affidavit not filed as evidence-in-chief in an originating claim answers `NOTHING`. (B) A "where": `JUST FALSE`.
**Taken: A**, because the words name a class of affidavit and no trigger word is present.

**15.11 (O 15 r 1(2)): "All trials in originating claims must be heard in open court."**
(A) A rule about trials in originating claims; any other matter answers `NOTHING`. (B) Read with paragraph (1), whatever is not such a trial must not be heard in open court.
**Taken: A.** Reviewer expected `JUST FALSE` or `JUST TRUE` (the reviewer's value for this row was not given to the encoder); open question.

**15.12 (O 15 r 1(5), ambiguity A1): "As a general rule, attendance in hearings in chambers is restricted to the parties (if they are not legally represented) or to their solicitors (if they are legally represented)."**
(A) A default with exceptions ("as a general rule"; paragraph (6) lets the Court allow others): a stranger answers `NOTHING`. (B) A flat no for a stranger (`JUST FALSE`).
**Taken: A.** Reviewer expected `JUST FALSE` or `JUST TRUE` (the reviewer's value for this row was not given to the encoder); open question.

**15.13 (O 15 r 4(8)): "A witness served with an order to produce documents only need not attend court personally if ...".**
(A) A scope rule: a witness served with an order to attend court answers `NOTHING`. (B) A flat no for that witness.
**Taken: A.** Reviewer expected `JUST FALSE` or `JUST TRUE`, and concedes it is a scope rule; open question.

**15.14 (O 15 r 16(3)): "An affidavit of evidence-in-chief may not be used if the maker does not attend Court for cross-examination, unless the parties otherwise agree."**
`JUST FALSE` when the maker does not attend and the parties have not agreed; `NOTHING` when the maker attends or the parties agree (an "unless" or an "if" that is not met lifts the bar and does not permit; the same shape as O 15 r 25(2)(a) and O 18 r 35(2)).
**Taken: as stated.** Reviewer expected `JUST FALSE` or `JUST TRUE` (the reviewer's value for this row was not given to the encoder); open question.

**15.15 (O 15 r 25(2)(a)): "vulgar or insulting words unless those words are in issue in the action".**
`JUST FALSE` for vulgar or insulting words that are not in issue; `NOTHING` for such words that are in issue ("unless" lifts the bar; the same shape as POCA s 339ZI(2)(a): "does not apply" lifts a bar, it does not permit).
**Taken: as stated; kept.** Reviewer expected `JUST TRUE`; open question.


**16.1 (O 16 r 2(1), (2)): "at any time not later than 14 days after service of the defence".**
(A) The period has a ceiling and no floor, so a notice served before the defence is served is in time. (B) The notice cannot be served before the defence.
**Taken: A.**
The same edge applies to every "within N days after" rule of this part: timeliness is `the date AT MOST the last day for doing the act`, so an act done before the anchor counts as in time, and the Rules say otherwise nowhere in this range.


**16.2 (O 16 r 1): "may withdraw the notice at any time with the permission of the Court".**
(A) The Court's permission is a condition: without it `JUST FALSE`. (B) The permission is only the manner of withdrawal: the rule grants withdrawal with permission and does not say what follows without it (`NOTHING`).
**Taken: B**, because the paragraph has no "only", no "not" and no "unless".


**17.1 (O 17 r 5(1)(b)): "5.33% per year".**
(A) Simple interest accrues pro rata, so the number of years may be a fraction. (B) Whole years only.
**Taken: A** (`o 17 r 5(2) the simple interest at 5.33% per year from the date the order is made until the date of payment` takes a number of years).

**17.2 (O 17 r 1): "order means an order of the Court and includes a judgment given at any stage of the action".**
(A) "means" closes the list: only an order of the Court or such a judgment is an order for the purposes of the Order (`JUST FALSE` otherwise). (B) "includes" opens it (`NOTHING` otherwise).
**Taken: A**, because the word that begins the definition is "means" (rule of 2026-10-29: a definition that says "means").

**18.1 (all four Orders): the polarity of "unless the Court otherwise orders" and its variants.**
(A) For a requirement or a deeming ("the appeal is deemed withdrawn unless the appellate Court otherwise orders"), an order makes the answer `JUST FALSE` (the requirement does not apply); for a prohibition ("no oral arguments are to be made ... unless the appellate Court otherwise orders"), an order makes the answer `NOTHING` (the prohibition lapses and the paragraph does not say that the thing is then allowed).
(B) Always `NOTHING`. (C) Always `JUST FALSE`.
**Taken: A.** It is stated at the head of each Order 18 module and applied in Orders 15 to 18 wherever the words "otherwise orders" or "otherwise directs" appear (44 rows).
Reviewed again on 2026-11-05 against the rulings of that day: no arm that lifts a bar with "unless", "except where" or "except so far as" was changed to `JUST TRUE` or `JUST FALSE`.
Two functions that carry such an arm also changed, on a different arm: O 18 r 3(1) (the bar and its twin, fork 18.6) and O 18 r 35(4) (its "if the party wishes" arm).
Where an "unless", "except where" or "except so far as" lifts a prohibition or a flat negative, the answer stays `NOTHING` (a lifted bar does not permit): O 15 r 16(3) (fork 15.14), O 15 r 25(2)(a) (fork 15.15), O 18 r 35(2) (fork 18.8), O 15 r 8(1), O 15 r 15(1), O 16 r 3(1), O 18 r 1(2), O 18 r 4(1), O 18 r 6(1), O 18 r 6(2), O 18 r 12(3)(b), O 18 r 12(4), O 18 r 16(7), O 18 r 21(11), O 18 r 21(14)(b), O 18 r 21(15), O 18 r 25(7), O 18 r 29(14), O 18 r 29(16), O 18 r 33(11), O 18 r 33(14)(b), O 18 r 33(15), O 18 r 35(3), O 18 r 35(4), O 18 r 37(1), O 18 r 37(5), O 18 r 38.
Where the bar is itself the question (O 18 r 3(1)), the bar's own yes/no question answers `JUST FALSE` when the "unless" is met (fork 18.6).

**18.2 (O 18 r 17(1) and r 27(1)): limb (a) "within 14 days after the date of the decision; or" limb (b) "in a case where a request for further arguments has been made ... within 14 days after ...".**
(A) The limbs alternate: when a request was made, limb (b) governs. (B) Both are always open to the appellant.
**Taken: A** (`o 18 r 17(1) the date after which the 14 days for the notice of appeal run`, and the same for r 27(1)).
Under B the later date would always win and the rule would never bite.

**18.3 (the regulative rules of O 17 r 3(6), O 18 r 9(3), r 21(12), r 33(12)): what consequence a deeming is in a `#TRACE`.**
(A) The text states the deeming ("failing which they are deemed to consent"; "the appeal is deemed withdrawn") and no other consequence, so the failure to act is written `LEST BREACH BY ... BECAUSE "<the text's words>"`, and the deeming itself is decided by the decision function. (B) A deeming is not a breach, so the duty has no `LEST`.
**Taken: A**, because on main a `MUST` without a `LEST` breaches anyway and the `BECAUSE` words carry the text's own consequence.

**18.4 (O 18 r 7): "Subject to Order 15, Rule 1(3) and any other provision ... appeals must be heard in chambers".**
(A) When the Appellate Division or the Court of Appeal has ordered otherwise under O 15 r 1(3), the matter is no longer one that O 15 r 1(3) sends to open court, so rule 7's chambers rule revives (`JUST TRUE`). (B) The order leaves rule 7 silent (`NOTHING`).
**Taken: A.** This is a marginal reading: it rests on reading an order that the matter need not be heard in open court as an order that it be heard in chambers.

**18.5 (O 18 r 3(1A)): "does not hear and determine the issue of costs within 30 days after".**
(A) A determination on the 30th day is within the period, and time starts to run after the 30-day period (the function returns the day the period expires; the next day is the first day of running). (B) Day 30 is outside.
**Taken: A**, following the text's "within 30 days after" and "after the expiry of the 30-day period".
Open question (the first day the appeal time runs): the date function returns the day the 30-day period expires; whether the first day of running is that day or the next is for the caller who counts under O 3 r 3 (seam S-T1).
The yes/no twin `o 18 r 3(1A) the time starts to run after the expiry of the 30-day period` answers `JUST FALSE` when costs were determined within the 30 days (a "where" that is not met, ruling (b)).


**18.6 (O 18 r 3(1), r 3(2)(b), r 3(2)(d) and r 29(3)(a)): bars "does not start to run until ...", "time does not run until ...", "does not begin to run until that Court ...", "may not be filed ... until the Judge ..." (ruling (d) of 2026-11-05).**
Each bar is its own yes/no question: `o 18 r 3(1) the time for filing an appeal or an application for permission to appeal is still barred from starting to run`, `o 18 r 3(2)(b) the time is still barred from running because not all the matters have been heard and determined`, `o 18 r 3(2)(d) the time ... is still barred from running` and `o 18 r 29(3)(a) an application for permission to appeal against the decision is barred from being filed yet`.
Each answers `JUST TRUE` before the event and `JUST FALSE` after it, and `JUST FALSE` where an "unless" or an "if" that is not met lifts the bar (`NOTHING` where a written law or another paragraph governs).
The thing the bar holds back is never said to have happened on the strength of the bar: after the event `o 18 r 3(1) the time ... starts to run after the lower Court has heard and determined all matters ...` and `o 18 r 29(3)(a) an application for permission to appeal against the decision may be filed` answer `NOTHING` (before the event they answer `JUST FALSE`, a flat negative).
**Taken: as stated.** In the first round `o 18 r 3(1) ... starts to run` answered `JUST TRUE` after the event; that is the change.

**18.7 (O 18 r 20(3) and (5), r 30(3) and (5), r 35(7) and (9)): is the amount in paragraph (5) the amount for each respondent (or each set of respondents represented by one firm), or the total?**
(A) Each respondent or set: two sets of respondents in a District Court action, $5,000 each, is $10,000; two in an appeal under r 30, $15,000 each, is $30,000. (B) The amount is the total whatever the number.
**Assumed, not ruled: A**, because paragraph (3) requires security "for the costs of the appeal for each respondent" (or each set) and paragraph (5) states the amounts in which "the appellant must provide security".
`o 18 r 20(3) and (5) the total security the appellant must provide`, `o 18 r 30(3) and (5) ...` and `o 18 r 35(7) and (9) ...` take the number of sets; `o 18 r 20(3) the security is provided for each set of respondents represented by the same firm of solicitors` (and r 30(3), r 35(7)) takes whether the respondents are represented by one firm.

**18.8 (O 18 r 35(2)): "except where there are special circumstances which make it impossible or impracticable to apply to the lower Court".**
`JUST FALSE` for an application made in the first instance to the appellate Court when the application could have been made to the lower Court and no such circumstance exists; `NOTHING` when the circumstances exist (an "except where" lifts the bar and does not permit; the same shape as O 15 r 25(2)(a)).
**Taken: as stated; kept.** Reviewer expected `JUST TRUE`; open question.

**18.9 (O 18 r 39(1)): "in the following circumstances" (a) to (f).**
(A) The list of the Registrar's powers is not closed: any other direction or order answers `NOTHING`. (B) It is closed (`JUST FALSE`).
**Taken: A**, because the paragraph has no "only"; the three powers that need the parties' consent say so in their own words.


## Jural relations (roc3)

One row per paragraph (or rule with one paragraph, or defined term) of lines 1405-2230.
**How the rows were made.** The kind is read from the modal verb of the paragraph ("must" is a claim of the holder against the bearer; "must not" a claim that the bearer not act; "may" a power when the Court or an official holds it (the correlative is the liability of the parties it affects), otherwise a privilege (the correlative is the no-right of the other parties and the Court); "is entitled" a claim). The bearer is the first actor the paragraph names before the modal verb, and the holder is the party the duty is owed to (the parties for a duty of the Court, the Court and the other parties for a duty of a party). A definition, a deeming, a scope rule or a counting rule creates no relation and is listed once as `none`.
The classification was made by a script and spot-read; it was not reviewed row by row, and a paragraph that holds several modal verbs is classified by its first.
378 rows.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| O15 r1(1) | the parties | the Court | claim / duty | `o 15 r 1(1) the kind of matter is one that must be heard in chambers …` and 1 more |
| O15 r1(2) | the parties | the Court | claim / duty | `o 15 r 1(2) the matter must be heard in open court [15h]` |
| O15 r1(3) | the parties | the Court | claim / duty | `o 15 r 1(3) the matter must be heard in open court [15h]` |
| O15 r1(4) | the Court | the parties affected | power / liability | `o 15 r 1(4) the Court may order the matter to be heard in the other w…` |
| O15 r1(5) | none | none | none (a scope, counting or interpretive rule) | `o 15 r 1(5) the person may attend the hearing in chambers as of right…` |
| O15 r1(6) | the Court | the parties affected | power / liability | `o 15 r 1(6) the Court may allow the person to attend the hearing in c…` |
| O15 r1(7) | the Court | the parties affected | power / liability | `o 15 r 1(7) the Court may hear the matter in court in private with at…` |
| O15 r1(8) | the Court and the other parties | the person | claim / duty | `o 15 r 1(8) the person must comply with the practice directions and t…` |
| O15 r2(1) | the parties | the Registrar | claim / duty | `o 15 r 2(1) the Registrar of the Supreme Court has the jurisdiction a…` and 1 more |
| O15 r2(2) | the Registrar | the parties affected | power / liability | `o 15 r 2(2) the Registrar of the Supreme Court may refer the matter t…` and 2 more |
| O15 r2(3) | the parties | the Registrar | claim / duty | `o 15 r 2(3) the directions that bind the Registrar are given by [15h]` and 1 more |
| O15 r3(1) | the Court and the other parties | a party | claim / duty | `o 15 r 3(1) the party attends as the Rule requires [15h]` |
| O15 r3(2) | a party | the Court and the other parties | privilege / no-right | `o 15 r 3(2) the Court may dismiss the party's application, action or …` |
| O15 r3(3) | the Court | the parties affected | power / liability | `o 15 r 3(3) the Court may dispense with the attendance of the parties…` |
| O15 r3(4) | the Court | the parties affected | power / liability | `o 15 r 3(4) the Court may direct that the matter be heard in an async…` |
| O15 r4(1) | a party | the Court and the other parties | privilege / no-right | `o 15 r 4(1) the person may request the Registrar to issue an order to…` and 1 more |
| O15 r4(2) | the Court and the other parties | the requesting party | claim / duty | `o 15 r 4(2) the order is as the Rule requires [15h]` |
| O15 r4(3) | the Court and the other parties | the requesting party | claim / duty | `o 15 r 4(3) the period before the hearing for serving the order [15h]` and 1 more |
| O15 r4(4) | the Registrar | the parties affected | power / liability | `o 15 r 4(4) the Registrar may revoke the order [15h]` |
| O15 r4(5) | a party | the Court and the other parties | privilege / no-right | `o 15 r 4(5) the party may apply to a Judge sitting in the General Div…` |
| O15 r4(6) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 4(6) the period after the Registrar's decision for the applica…` and 1 more |
| O15 r4(7) | none | none | none (a scope, counting or interpretive rule) | `o 15 r 4(7) the order continues to have effect [15h]` |
| O15 r4(8) | the Court and the other parties | the witness | claim / duty | `o 15 r 4(8) the witness need not attend court personally [15h]` |
| O15 r4(9) | the witness | the party or official who must give it | claim / duty | `o 15 r 4(9) the witness is entitled to claim reasonable compensation …` |
| O15 r4(10) | the Court and the other parties | the witness | claim / duty | `o 15 r 4(10) the requesting party must include in the letter the name…` |
| O15 r4(11) | the Court and the other parties | the person | claim / duty | `o 15 r 4(11) the order to attend court is to include the words of par…` |
| O15 r4(12) | the party concerned | the Court and the other parties | privilege / no-right | `o 15 r 4(12) the period before the hearing for serving the order on t…` and 2 more |
| O15 r4(13) | the Court and the other parties | the witness | claim / duty | `o 15 r 4(13) the witness must remain outside the courtroom [15h]` |
| O15 r4(14) | the witness | the Court and the other parties | privilege / no-right | `o 15 r 4(14) the witness may remain in or leave the courtroom [15h]` |
| O15 r4(15) | the Court | the parties affected | power / liability | `o 15 r 4(15) the requesting party may request the Registrar to produc…` |
| O15 r4(16) | none | none | none (a scope, counting or interpretive rule) | `o 15 r 4(16) it is sufficient for the Registrar to produce a copy of …` |
| O15 r5(1) | none | none | none (a scope, counting or interpretive rule) | `o 15 r 5(1) an application may be made for an order in Form 30 for th…` and 1 more |
| O15 r5(2) | the Judge | the parties affected | power / liability | `o 15 r 5(2) the application may be made in the court [15h]` |
| O15 r5(3) | the Court and the other parties | the applicant | claim / duty | `o 15 r 5(3) the application is made as the Rule requires [15h]` |
| O15 r5(4) | none | none | none (a scope, counting or interpretive rule) | `o 15 r 5(4) paragraphs (5) to (8) apply [15h]` and 1 more |
| O15 r5(5) | the Court and the other parties | a party | claim / duty | `o 15 r 5(5) the letter of request must be in [15h]` |
| O15 r5(6) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 5(6) a translation must accompany the letter of request or a d…` |
| O15 r5(7) | the Court and the other parties | the person | claim / duty | `o 15 r 5(7) the translation is certified as the Rule requires [15h]` |
| O15 r5(8) | the Court and the other parties | a party | claim / duty | `o 15 r 5(8) the party obtaining the order must also file an undertaki…` and 2 more |
| O15 r5(9) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 5(9) the meaning of the term in this Rule [15h]` and 4 more |
| O15 r5(9) defined term “Hague Evidence Convention” | none | none | none (a definition) | `o 15 r 5(9) an instrument is the Hague Evidence Convention [15h]` |
| O15 r5(9) defined term “issuing authority” | none | none | none (a definition) | `o 15 r 5(9) an authority is an issuing authority [15h]` |
| O15 r5(9) defined term “Recommended Model Form” | none | none | none (a definition) | `o 15 r 5(9) a form is a Recommended Model Form [15h]` |
| O15 r5(9) defined term “transmitting authority” | none | none | none (a definition) | `o 15 r 5(9) an authority is a transmitting authority [15h]` |
| O15 r6(1) | the person | the Court and the other parties | privilege / no-right | `o 15 r 6(1) the person may attend the hearing [15h]` |
| O15 r6(2) | the Court | the parties affected | power / liability | `o 15 r 6(2) the Court may disallow the person to attend the hearing […` |
| O15 r7(1) | the parties | the Court | claim / duty | `o 15 r 7(1) the originating application must be heard by one Judge [1…` |
| O15 r7(2) | the Judge | the parties affected | power / liability | `o 15 r 7(2) the Judge may hear the matter with the assistance of asse…` |
| O15 r7(3) | a party | the Court and the other parties | privilege / no-right | `o 15 r 7(3) the Court may dismiss the matter [15h]` |
| O15 r7(4) | a party | the Court and the other parties | privilege / no-right | `o 15 r 7(4) the Court may proceed with the hearing, give judgment aga…` |
| O15 r7(5) | the parties | the Court | claim / duty | `o 15 r 7(5) the originating application or summons must be decided on…` |
| O15 r7(6) | the Court | the parties affected | power / liability | `o 15 r 7(6) the Court may order further affidavits, cross-examination…` |
| O15 r7(7) | the Court | the parties affected | power / liability | `o 15 r 7(7) the Court may give its decision immediately after the hea…` |
| O15 r8(1) | the parties | the Court | claim / duty | `o 15 r 8(1) the trial must be heard by one Judge [15h]` |
| O15 r8(2) | the Judge | the parties affected | power / liability | `o 15 r 8(2) the Judge may hear the trial or part of it with the assis…` |
| O15 r8(3) | a party | the Court and the other parties | privilege / no-right | `o 15 r 8(3) the Court may dismiss the claim and any counterclaim [15h]` |
| O15 r8(4) | a party | the Court and the other parties | privilege / no-right | `o 15 r 8(4) the Court may proceed with the trial, give judgment again…` |
| O15 r8(5) | the parties | the Court | claim / duty | `o 15 r 8(5) the order of proceedings in paragraphs (6) to (13) applie…` |
| O15 r8(6) | the parties | the Court | claim / duty | `o 15 r 8(6) the opening statements and affidavits of evidence-in-chie…` |
| O15 r8(7) | the Court and the other parties | the claimant | claim / duty | `o 15 r 8(7) the claimant's evidence is given in the order the Rule re…` |
| O15 r8(8) | the defendant | the Court and the other parties | privilege / no-right | `o 15 r 8(8) the person may cross-examine the claimant and the claiman…` |
| O15 r8(9) | the Court and the other parties | the claimant | claim / duty | `o 15 r 8(9) the defendant's evidence is given in the order the Rule r…` |
| O15 r8(10) | the claimant | the Court and the other parties | privilege / no-right | `o 15 r 8(10) the person may cross-examine the defendant and the defen…` |
| O15 r8(11) | the claimant | the Court and the other parties | privilege / no-right | `o 15 r 8(11) the defendant may make a submission of No case to answer…` and 3 more |
| O15 r8(12) | the Court and the other parties | a party | claim / duty | `o 15 r 8(12) the Court must hear the submissions of all the parties […` |
| O15 r8(13) | the Court | the parties affected | power / liability | `o 15 r 8(13) the Court may give its decision immediately after the he…` |
| O15 r9 | the Court and the other parties | the person | claim / duty | `o 15 r 9 the person must take an oath or make an affirmation accordin…` |
| O15 r10(1) | the Court | the parties affected | power / liability | `o 15 r 10(1) the Court may ask a witness any questions that the Court…` and 1 more |
| O15 r10(2) | the Court | the parties affected | power / liability | `o 15 r 10(2) the Court may inspect any object in the courtroom or els…` and 1 more |
| O15 r11(1) | the parties | the Court | claim / duty | `o 15 r 11(1) the Court must maintain a record of the exhibit [15e]` |
| O15 r11(2) | the Court | the parties affected | power / liability | `o 15 r 11(2) the Court may direct that the exhibit be kept in the cus…` |
| O15 r11(3) | the Court | the parties affected | power / liability | `o 15 r 11(3) the exhibits kept with the Court may be returned to the …` |
| O15 r11(4) | the Court | the parties affected | power / liability | `o 15 r 11(4) the notice to take back exhibits [15e]` and 2 more |
| O15 r11(5) | the parties | the Court | claim / duty | `o 15 r 11(5) the Court must maintain an official record of every hear…` |
| O15 r11(6) | none | none | none (a scope, counting or interpretive rule) | `o 15 r 11(6) the audio recording is the official record of the hearin…` |
| O15 r11(7) | the Court | the parties affected | power / liability | `o 15 r 11(7) the Court's notes of proceedings are the official record…` |
| O15 r11(8) | a party | the Court and the other parties | privilege / no-right | `o 15 r 11(8) the party may apply for a certified transcript of the of…` |
| O15 r11(9) | the Court | the parties affected | power / liability | `o 15 r 11(9) the costs of producing a certified transcript may be cla…` |
| O15 r11(10) | the parties | the Registrar | claim / duty | `o 15 r 11(10) the transcript is certified in the manner the Registrar…` |
| O15 r11(11) | the parties | the Court | claim / duty | `o 15 r 11(11) the time the official record must be kept [15e]` and 1 more |
| O15 r12(1) | the Court | the parties affected | power / liability | `o 15 r 12(1)(a) the Court may give its decision orally [15e]` and 1 more |
| O15 r12(2) | a party | the party or official who must give it | claim / duty | `o 15 r 12(2) the parties are entitled to a copy of the decision [15e]` |
| O15 r12(3) | a party | the Court and the other parties | privilege / no-right | `o 15 r 12(3) the Court may dispense with the attendance of the partie…` and 1 more |
| O15 r12(4) | the Court | the parties affected | power / liability | `o 15 r 12(4) the Court may give such further orders or directions inc…` |
| O15 r13(1) | the Court | the parties affected | power / liability | `o 15 r 13(1) the Court may give its decision in the matter [15e]` |
| O15 r13(2) | the Court | the parties affected | power / liability | `o 15 r 13(2) the Court may substitute the person as a party and order…` |
| O15 r14(1) | the Judge | the parties affected | power / liability | `o 15 r 14(1) another Judge or Registrar may take over and give a deci…` |
| O15 r14(2) | the Judge | the parties affected | power / liability | `o 15 r 14(2) the Judge or Registrar who takes over may recall any wit…` |
| O15 r14(3) | the Court and the other parties | a party | claim / duty | `o 15 r 14(3) the matter must be heard anew by another Judge or Regist…` and 2 more |
| O15 r15(1) | none | none | none (a scope, counting or interpretive rule) | `o 15 r 15(1) this Rule applies to the proceeding [15e]` and 1 more |
| O15 r15(2) | the parties | the Court | claim / duty | `o 15 r 15(2) the Court must give judgment on liability and on the amo…` |
| O15 r15(1) defined term “damages” | none | none | none (a definition) | `o 15 r 15(1) the sum is within “damages” in this Rule [15e]` |
| O15 r15(3) | the Court | the parties affected | power / liability | `o 15 r 15(3) the Court may give directions on the assessment of damag…` |
| O15 r15(4) | the parties | the Court | claim / duty | `o 15 r 15(4) the period after the judgment for applying for direction…` and 4 more |
| O15 r15(5) | the Court | the parties affected | power / liability | `o 15 r 15(5) the period after the date of filing for serving the noti…` and 2 more |
| O15 r15(6) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 15(6) the damages must be assessed until the date of decision …` |
| O15 r15(7) | the person | the Court and the other parties | privilege / no-right | `o 15 r 15(7) the Court may make an award for provisional damages [15e]` |
| O15 r15(8) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 15(8) the claim must be pleaded [15e]` |
| O15 r15(9) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 15(9) the award must specify the contingency and the period fo…` |
| O15 r15(10) | the Court | the parties affected | power / liability | `o 15 r 15(10) the Court may specify a different period for each conti…` |
| O15 r15(11) | the Court | the parties affected | power / liability | `o 15 r 15(11) the Court may extend the period in paragraph (9) or (10…` |
| O15 r15(12) | the claimant | the Court and the other parties | privilege / no-right | `o 15 r 15(12) the claimant may make another application for further d…` |
| O15 r15(13) | the Court and the other parties | the claimant | claim / duty | `o 15 r 15(13) the application for further damages must be served on t…` and 1 more |
| O15 r15(14) | the parties | the Court | claim / duty | `o 15 r 15(14) the Court hearing the application for further damages m…` |
| O15 r15(15) | the Court | the parties affected | power / liability | `o 15 r 15(15) the Court may order the damages to be paid in periodic …` |
| O15 r15(16) | the Court | the parties affected | power / liability | `o 15 r 15(16) the Court may be guided by actuarial tables and other g…` |
| O15 r15(17) | the parties | the Court | claim / duty | `o 15 r 15(17) the Court must give the appropriate directions for the …` |
| O15 r16(1) | the parties | the Court | claim / duty | `o 15 r 16(1) the trial must be decided on the basis of the affidavits…` |
| O15 r16(2) | the Court | the parties affected | power / liability | `o 15 r 16(2) the Court may allow a witness' evidence-in-chief to be g…` |
| O15 r16(3) | the Court and the other parties | the maker of the affidavit | claim / duty not to | `o 15 r 16(3) the affidavit of evidence-in-chief may be used [15e]` |
| O15 r16(4) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 16(4) the new fact may be given in oral evidence [15e]` |
| O15 r16(5) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 16(5) the affidavit of evidence-in-chief may contain the evide…` |
| O15 r16(6) | the Court and the other parties | a party | claim / duty | `o 15 r 16(6) the period before the first date of the hearing for the …` and 2 more |
| O15 r16(7) | the Court and the other parties | a party | claim / duty | `o 15 r 16(7) the party must give notice by letter to all other partie…` and 1 more |
| O15 r16(8) | the Court and the other parties | a party | claim / duty | `o 15 r 16(8) the notice must state the grounds in section 32 of the E…` |
| O15 r16(9) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 16(9) the notice for statements contained in a document contai…` |
| O15 r16(10) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 16(10) the notice for statements not contained in a document c…` |
| O15 r16(11) | the Court | the parties affected | power / liability | `o 15 r 16(11) the Court may accept the matter as fact [15e]` |
| O15 r17 | none | none | none (a scope, counting or interpretive rule) | `o 15 r 17 the act is within “affirm” [15a]` and 1 more |
| O15 r17 defined term “affirm” | none | none | none (a definition) | `o 15 r 17 the act is within “affirm” [15a]` |
| O15 r17 defined term “commissioner for oaths” | none | none | none (a definition) | `o 15 r 17 the person is within “commissioner for oaths” [15a]` |
| O15 r18 | none | none | none (a scope, counting or interpretive rule) | `o 15 r 18 the document is an affidavit [15a]` |
| O15 r19(1) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 19(1) the affidavit is in the form the Rule requires [15a]` |
| O15 r19(2) | the Court and the other parties | the maker of the affidavit | claim / duty | `o 15 r 19(2) the photograph is as the Rule requires [15a]` |
| O15 r20 | the Court and the other parties | the person | claim / duty | `o 15 r 20 the person may make an affidavit [15a]` |
| O15 r21 | the person | the Court and the other parties | privilege / no-right | `o 15 r 21 two or more persons may make a joint affidavit [15a]` |
| O15 r22(1) | the commissioner for oaths | the Court and the other parties | privilege / no-right | `o 15 r 22(1) the affidavit may be affirmed and signed, and the attest…` |
| O15 r22(2) | the commissioner for oaths | the Court and the other parties | privilege / no-right | `o 15 r 22(2) the deponent and the commissioner for oaths may sign the…` |
| O15 r22(3) | the Court and the other parties | the commissioner for oaths | claim / duty | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule r…` |
| O15 r23 | the party concerned | the Court and the other parties | privilege / no-right | `o 15 r 23 an affidavit may be affirmed outside Singapore [15a]` |
| O15 r24 | the Court and the other parties | the maker of the affidavit | claim / duty | `o 15 r 24 the commissioner for oaths must certify on the affidavit th…` and 1 more |
| O15 r25(1) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 25(1) the matter may be put in the affidavit [15a]` |
| O15 r25(2) | the Court and the other parties | the party concerned | claim / duty not to | `o 15 r 25(2) the affidavit may contain the matter [15a]` |
| O15 r26(1) | the Court | the parties affected | power / liability | `o 15 r 26(1) the affidavit may be altered [15a]` |
| O15 r26(2) | the maker of the affidavit | the Court and the other parties | privilege / no-right | `o 15 r 26(2) the maker may correct any mistakes in the affidavit by m…` |
| O15 r27(1) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 27(1) a copy of the document must be annexed to the affidavit …` |
| O15 r27(2) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 27(2) a copy of the whole document must be annexed [15a]` |
| O15 r27(3) | the Court and the other parties | the party concerned | claim / duty | `o 15 r 27(3) a copy of only those portions of the document need to be…` |
| O15 r27(4) | the person | the Court and the other parties | privilege / no-right | `o 15 r 27(4) the identification may be done by annexing a picture of …` |
| O15 r27(5) | the Court and the other parties | the commissioner for oaths | claim / duty | `o 15 r 27(5) the annexure must be identified by a certificate of the …` |
| O15 r28 | the Court and the other parties | the commissioner for oaths | claim / duty | `o 15 r 28 the seal or signature of the commissioner for oaths must be…` |
| O15 r29 | the Court and the other parties | a party | claim / duty | `o 15 r 29 the party must give notice of the intention to use the affi…` |
| O16 r1 | a party | the Court and the other parties | privilege / no-right | `o 16 r 1 the party may withdraw the notice of intention to contest or…` |
| O16 r2(1) | the claimant | the Court and the other parties | privilege / no-right | `o 16 r 2(1) the period after service of the defence [16]` and 5 more |
| O16 r2(2) | the defendant | the Court and the other parties | privilege / no-right | `o 16 r 2(2)(b) the period after service of the defence to counterclai…` and 2 more |
| O16 r2(3) | none | none | none (a scope, counting or interpretive rule) | `o 16 r 2(3) the date from which the 14 days run for the action [16]` |
| O16 r2(4) | none | none | none (a scope, counting or interpretive rule) | `o 16 r 2(4) the date from which the 14 days run for the counterclaim …` |
| O16 r2(5) | a party | the Court and the other parties | privilege / no-right | `o 16 r 2(5) the action may be withdrawn without the permission of the…` |
| O16 r2(6) | none | none | none (a deeming) | `o 16 r 2(6) the action is deemed to have been discontinued against th…` |
| O16 r2(7) | a party | the Court and the other parties | privilege / no-right | `o 16 r 2(7) the action, cause or matter is deemed to have been discon…` |
| O16 r2(8) | none | none | none (a scope, counting or interpretive rule) | `o 16 r 2(8) paragraph (7) applies to the action, cause or matter [16]` |
| O16 r2(9) | the Court | the parties affected | power / liability | `o 16 r 2(9) the Court may extend the time [16]` |
| O16 r2(10) | the Court | the parties affected | power / liability | `o 16 r 2(10) the Court may reinstate the action, cause or matter and …` |
| O16 r3(1) | the Court and the other parties | a party | claim / duty not to | `o 16 r 3(1) a party may discontinue the action or counterclaim or wit…` and 1 more |
| O16 r3(2) | the party concerned | the Court and the other parties | privilege / no-right | `o 16 r 3(2) the application for permission may be made by summons [16]` |
| O16 r4 | none | none | none (a deeming) | `o 16 r 4 the discontinuance is a defence to a subsequent action for t…` |
| O16 r5 | a party | the Court and the other parties | privilege / no-right | `o 16 r 5 the Court may order the proceedings in the subsequent action…` |
| O16 r6 | the Court and the other parties | a party | claim / duty not to | `o 16 r 6 the party may withdraw the summons [16]` |
| O17 r1 | none | none | none (a scope, counting or interpretive rule) | `o 17 r 1 the thing is an order for the purposes of this Order [17]` |
| O17 r1 defined term “order” | none | none | none (a definition) | `o 17 r 1 the thing is an order for the purposes of this Order [17]` |
| O17 r2(1) | none | none | none (a scope, counting or interpretive rule) | `o 17 r 2(1) the order takes effect from the day that it is given [17]` |
| O17 r2(2) | the Court and the other parties | the person | claim / duty | `o 17 r 2(2) the Court must give that person a reasonable time within …` |
| O17 r2(3) | none | none | none (a deeming) | `o 17 r 2(3) the order is deemed to require immediate compliance [17]` |
| O17 r3(1) | the parties | the Court | claim / duty | `o 17 r 3(1) the order must be drawn up and filed in Court [17]` |
| O17 r3(2) | the Court and the other parties | the party concerned | claim / duty | `o 17 r 3(2) the order is in the form that the Rule requires [17]` |
| O17 r3(3) | the Court and the other parties | a party | claim / duty | `o 17 r 3(3) the party must draw up the order [17]` |
| O17 r3(4) | the Court and the other parties | a party | claim / duty | `o 17 r 3(4) the party must draw up only one order for all the applica…` |
| O17 r3(5) | the Court and the other parties | a party | claim / duty | `o 17 r 3(5) the period after the order is made for sending the draft …` and 5 more |
| O17 r3(6) | the Court and the other parties | the solicitors | claim / duty | `o 17 r 3(6) the period for the solicitors to respond to the draft [17]` and 5 more |
| O17 r3(7) | a party | the Court and the other parties | privilege / no-right | `o 17 r 3(7) the party who drew up the order may write to the Court to…` and 1 more |
| O17 r3(8) | the Court | the parties affected | power / liability | `o 17 r 3(8) the Court may decide the dispute without the attendance o…` |
| O17 r3(9) | the Court and the other parties | a party | claim / duty | `o 17 r 3(9) the draft of the order is to be submitted to the Registra…` |
| O17 r4(1) | the Court | the parties affected | power / liability | `o 17 r 4(1) the Court may redact the order [17]` |
| O17 r4(2) | the Court | the parties affected | power / liability | `o 17 r 4(2) the Court may prohibit the person from inspecting or taki…` |
| O17 r5(1) | none | none | none (a scope, counting or interpretive rule) | `o 17 r 5(1)(b) the rate of simple interest per year [17]` and 2 more |
| O17 r5(2) | the Court and the other parties | the party concerned | claim / duty | `o 17 r 5(2) the simple interest at 5.33% per year from the date the o…` |
| O17 r5(3) | the Court | the parties affected | power / liability | `o 17 r 5(3) interest is to be calculated from the date that each inst…` and 1 more |
| O17 r5(4) | the Court and the other parties | the party concerned | claim / duty | `o 17 r 5(4) a part payment must be used to reduce the principal amoun…` and 1 more |
| O18 r1(1) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 1(1) this Order applies to the proceeding [18g]` and 1 more |
| O18 r1(2) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 1(2) the application is an application in an action [18g]` and 2 more |
| O18 r2(1) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 2(1) this Order gives way to a written law on the right to app…` |
| O18 r2(2) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r2(3) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r2(4) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r2(5) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 2 the Division of this Order that concerns the appeal [18g]` |
| O18 r3(1) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 3(1) the time for filing an appeal or an application for permi…` and 1 more |
| O18 r3(1A) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 3(1A) the period for the lower Court to determine costs [18g]` and 3 more |
| O18 r3(2) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined…` and 10 more |
| O18 r4(1) | a party | the Court and the other parties | privilege / no-right | `o 18 r 4(1) the party may file another appeal for the application [18…` |
| O18 r4(2) | the Court and the other parties | a party | claim / duty | `o 18 r 4(2) the party must file a separate notice of appeal for the m…` |
| O18 r4(3) | a party | the Court and the other parties | privilege / no-right | `o 18 r 4(3) each party may file one appeal in respect of all the appl…` |
| O18 r5(1) | the person | the Court and the other parties | privilege / no-right | `o 18 r 5(1) the person may apply to intervene in the appeal [18g]` |
| O18 r5(2) | the Court and the other parties | a party | claim / duty | `o 18 r 5(2) the application for permission to intervene and the suppo…` |
| O18 r5(3) | the Court and the other parties | the applicant | claim / duty | `o 18 r 5(3) the supporting affidavit is as the Rule requires [18g]` |
| O18 r5(4) | the appellate Court | the parties affected | power / liability | `o 18 r 5(4) the appellate Court may impose conditions, including orde…` |
| O18 r6(1) | the lower Court | the parties affected | power / liability | `o 18 r 6(1) the appeal operates as a stay of enforcement or of procee…` |
| O18 r6(2) | the appellate Court | the parties affected | power / liability | `o 18 r 6(2) an intermediate act or proceeding is invalidated by the a…` |
| O18 r6(3) | the parties | the lower Court | claim / duty | `o 18 r 6(3) interest is to be allowed for the time enforcement has be…` |
| O18 r7 | the parties | the Court | claim / duty | `o 18 r 7 the appeal must be heard in chambers [18g]` |
| O18 r8(1) | the appellate Court | the parties affected | power / liability | `o 18 r 8(1) the appellate Court may order any party to serve any docu…` |
| O18 r8(2) | the appellate Court | the parties affected | power / liability | `o 18 r 8(2) the appellate Court may allow or invite the non-party to …` |
| O18 r8(3) | a party | the Court and the other parties | privilege / no-right | `o 18 r 8(3) the party may make oral submissions at the hearing of the…` |
| O18 r8(4) | the appellate Court | the parties affected | power / liability | `o 18 r 8(4) the appellate Court may make any order relating to any pa…` |
| O18 r8(5) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 8(5) the appellate Court's powers to decide the merits of the …` |
| O18 r8(6) | the appellate Court | the parties affected | power / liability | `o 18 r 8(6) the appellate Court has power to receive further evidence…` and 1 more |
| O18 r8(7) | the parties | the appellate Court | claim / duty | `o 18 r 8(7) the further evidence must be adduced in the manner direct…` |
| O18 r9(1) | the appellant | the Court and the other parties | privilege / no-right | `o 18 r 9(1) the appeal may be dismissed [18g]` |
| O18 r9(2) | the appellant | the Court and the other parties | privilege / no-right | `o 18 r 9(2) the appeal may proceed in the absence of the respondent […` |
| O18 r9(3) | the Court | the parties affected | power / liability | `o 18 r 9(3) the period after the dismissal or hearing for the applica…` and 5 more |
| O18 r10 | the parties | the appellate Court | claim / duty | `o 18 r 10 the appellate Court may intervene [18g]` |
| O18 r11(1) | the lower Court | the parties affected | power / liability | `o 18 r 11(1) the lower Court or the appellate Court may order an expe…` |
| O18 r11(2) | the lower Court | the parties affected | power / liability | `o 18 r 11(2) the lower Court or the appellate Court may dispense with…` |
| O18 r12(1) | the appellant | the Court and the other parties | privilege / no-right | `o 18 r 12(1) the appellant may withdraw the appeal or the applicant m…` |
| O18 r12(2) | a party | the Court and the other parties | privilege / no-right | `o 18 r 12(2) the appeal or application is deemed withdrawn in relatio…` and 1 more |
| O18 r12(3) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 12(3)(a) the party may request in writing to the appellate Cou…` and 2 more |
| O18 r12(4) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 12(4) the appeal or application remains on the list [18g]` and 1 more |
| O18 r13(1) | a party | the Court and the other parties | privilege / no-right | `o 18 r 13(1) the appellate Court may dispense with the attendance of …` and 1 more |
| O18 r13(2) | the appellate Court | the parties affected | power / liability | `o 18 r 13(2) the appellate Court may give such further orders or dire…` |
| O18 r14(1) | the appellate Court | the parties affected | power / liability | `o 18 r 14(1) the appellate Court may give its decision orally or in w…` |
| O18 r14(2) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 14(2)(a) the appellate Court may direct the Registrar to infor…` and 1 more |
| O18 r14(3) | a party | the party or official who must give it | claim / duty | `o 18 r 14(3) the party is entitled to a copy of the decision [18g]` |
| O18 r14(4) | the appellate Court | the parties affected | power / liability | `o 18 r 14(4) the judgment of the appellate Court may be delivered ora…` |
| O18 r15 | the Court and the other parties | a party | claim / duty | `o 18 r 15 the period after the date of the Registrar's decision for t…` and 4 more |
| O18 r16(1) | the Registrar | the parties affected | power / liability | `o 18 r 16(1) the Registrar may give a summary of the points decided w…` |
| O18 r16(2) | the parties | the Registrar | claim / duty | `o 18 r 16(2) the period after the filing of the notice of appeal for …` and 3 more |
| O18 r16(3) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 16(3)(b) the period after the certification before the appella…` and 5 more |
| O18 r16(4) | the parties | the District Judge or Magistrate | claim / duty | `o 18 r 16(4) the appeal must proceed by way of a rehearing on the doc…` and 1 more |
| O18 r16(5) | the Court and the other parties | a party | claim / duty | `o 18 r 16(5) the period for the written submissions [18l]` and 3 more |
| O18 r16(6) | the parties | the appellate Court | claim / duty | `o 18 r 16(6) the written submissions include submissions on the appro…` and 3 more |
| O18 r16(7) | the appellate Court | the parties affected | power / liability | `o 18 r 16(7) a document other than those set out in the Rule may be f…` |
| O18 r16(8) | the appellate Court | the parties affected | power / liability | `o 18 r 16(8) the appellate Court may allow the page limit to be excee…` |
| O18 r16(9) | the appellate Court | the parties affected | power / liability | `o 18 r 16(9) the appellate Court may upon application waive, refund, …` |
| O18 r16(10) | the Court and the other parties | a party | claim / duty not to | `o 18 r 16(10) the party may file more than one set of submissions [18…` |
| O18 r17(1) | the Court and the other parties | a party | claim / duty | `o 18 r 17(1) the date after which the 14 days for the notice of appea…` and 2 more |
| O18 r17(2) | the Judge | the parties affected | power / liability | `o 18 r 17(2) the General Division may extend the time for filing and …` and 1 more |
| O18 r18(1) | the parties | the District Judge or Magistrate | claim / duty | `o 18 r 18(1) the request for further arguments is made as the Rule re…` |
| O18 r18(2) | the Court and the other parties | the party concerned | claim / duty | `o 18 r 18(2) the request for further arguments is filed in time [18l]` |
| O18 r18(3) | the Court and the other parties | the party concerned | claim / duty | `o 18 r 18(3) the request sets out the proposed arguments and a copy o…` |
| O18 r18(4) | the parties | the Registrar | claim / duty | `o 18 r 18(4) the period after receiving the request for informing the…` and 1 more |
| O18 r18(5) | none | none | none (a deeming) | `o 18 r 18(5) it is deemed that the District Judge or Magistrate does …` |
| O18 r19(1) | the Court and the other parties | a party | claim / duty | `o 18 r 19(1) the period after the date of the decision for applying f…` and 1 more |
| O18 r19(2) | the District Judge or Magistrate | the parties affected | power / liability | `o 18 r 19(2) the application for permission to the General Division i…` |
| O18 r19(3) | the Court and the other parties | the applicant | claim / duty | `o 18 r 19(3) the period after the decision granting permission for th…` and 1 more |
| O18 r19(4) | the Judge | the parties affected | power / liability | `o 18 r 19(4) the General Division may extend the time for filing and …` and 1 more |
| O18 r20(1) | the Court and the other parties | the appellant | claim / duty | `o 18 r 20(1) the appellant has provided security and filed the certif…` and 3 more |
| O18 r20(2) | the Court and the other parties | the appellant | claim / duty | `o 18 r 20(2) the appellants need to provide only one set of security …` |
| O18 r20(3) | the Court and the other parties | the respondent | claim / duty | `o 18 r 20(3) the appellant must provide security for each respondent …` and 1 more |
| O18 r20(4) | the Court and the other parties | the party concerned | claim / duty | `o 18 r 20(4) the security is in a form the Rule allows [18l]` and 1 more |
| O18 r20(5) | the Court and the other parties | the appellant | claim / duty | `o 18 r 20(5) the amount of security required [18l]` and 2 more |
| O18 r20(6) | a party | the Court and the other parties | privilege / no-right | `o 18 r 20(6) any party may apply to the appellate Court to vary or wa…` |
| O18 r20(7) | the appellate Court | the parties affected | power / liability | `o 18 r 20(7) the appellate Court may order further security for costs…` |
| O18 r21(1) | the District Judge or Magistrate | the parties affected | power / liability | `o 18 r 21(1) the District Judge or Magistrate may give a summary of t…` |
| O18 r21(2) | the parties | the District Judge or Magistrate | claim / duty | `o 18 r 21(2) the period after the filing of the notice of appeal for …` and 3 more |
| O18 r21(3) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 21(3)(b) the period after the certification before the appella…` and 5 more |
| O18 r21(4) | the parties | the Judge | claim / duty | `o 18 r 21(4) the appeal must proceed by way of a rehearing on the doc…` and 1 more |
| O18 r21(5) | the Court and the other parties | a party | claim / duty | `o 18 r 21(5) the period for the written submissions [18l]` and 3 more |
| O18 r21(6) | the parties | the appellate Court | claim / duty | `o 18 r 21(6) the written submissions include submissions on the appro…` and 3 more |
| O18 r21(7) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 21(7) the party is required to file separate written submissio…` |
| O18 r21(8) | the Court and the other parties | a party | claim / duty | `o 18 r 21(8) the parties must try to agree on filing a single set of …` |
| O18 r21(9) | the Court and the other parties | a party | claim / duty | `o 18 r 21(9) the parties must request in writing for a case conferenc…` |
| O18 r21(10) | the Court and the other parties | a party | claim / duty | `o 18 r 21(10) the parties must inform the Registrar in writing of the…` |
| O18 r21(11) | the appellate Court | the parties affected | power / liability | `o 18 r 21(11) a document other than those set out in the Rule may be …` |
| O18 r21(12) | none | none | none (a deeming) | `o 18 r 21(12) the appeal is deemed withdrawn [18l]` and 3 more |
| O18 r21(13) | a party | the Court and the other parties | privilege / no-right | `o 18 r 21(13) the security for costs must be paid and the solicitor's…` |
| O18 r21(14) | none | none | none (a deeming) | `o 18 r 21(14)(a) the period after the appeal is deemed withdrawn for …` and 7 more |
| O18 r21(15) | the Court and the other parties | the respondent | claim / duty not to | `o 18 r 21(15) the respondent is allowed to make submissions at the he…` and 1 more |
| O18 r21(16) | the appellate Court | the parties affected | power / liability | `o 18 r 21(16) the appellate Court may allow the page limit to be exce…` |
| O18 r21(17) | the appellate Court | the parties affected | power / liability | `o 18 r 21(17) the appellate Court may upon application waive, refund,…` |
| O18 r21(18) | the Court and the other parties | a party | claim / duty not to | `o 18 r 21(18) the party may file more than one set of submissions [18…` |
| O18 r22(1) | the parties | the Court | claim / duty | `o 18 r 22(1) this Rule applies without the need for an order from the…` and 1 more |
| O18 r22(2) | the Court and the other parties | the appellant | claim / duty | `o 18 r 22(2) the security for costs must be paid to the respondent to…` and 2 more |
| O18 r22(3) | the Court and the other parties | the appellant | claim / duty | `o 18 r 22(3) the security for costs must be paid to the appellant [18…` and 1 more |
| O18 r23 | the Court and the other parties | the party concerned | claim / duty | `o 18 r 23 the step for enforcement is taken as the Rule requires [18l]` |
| O18 r24 | the Court and the other parties | a party | claim / duty | `o 18 r 24 the period after the date of the Registrar's decision for t…` and 1 more |
| O18 r25(1) | the Registrar | the parties affected | power / liability | `o 18 r 25(1) the Registrar may give a summary of the points decided w…` |
| O18 r25(2) | the parties | the Registrar | claim / duty | `o 18 r 25(2) the period after the filing of the notice of appeal for …` and 3 more |
| O18 r25(3) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 25(3)(b) the period after the certification before the appella…` and 5 more |
| O18 r25(4) | the parties | the Judge | claim / duty | `o 18 r 25(4) the appeal must proceed by way of a rehearing on the doc…` and 1 more |
| O18 r25(5) | the Court and the other parties | a party | claim / duty | `o 18 r 25(5) the period for the written submissions [18l]` and 3 more |
| O18 r25(6) | the parties | the Judge | claim / duty | `o 18 r 25(6) the written submissions include submissions on the appro…` and 3 more |
| O18 r25(7) | the Judge | the parties affected | power / liability | `o 18 r 25(7) a document other than those set out in the Rule may be f…` |
| O18 r25(8) | the Judge | the parties affected | power / liability | `o 18 r 25(8) the Judge may allow the page limit to be exceeded [18l]` |
| O18 r25(9) | the Judge | the parties affected | power / liability | `o 18 r 25(9) the Judge may upon application waive, refund, defer or a…` |
| O18 r25(10) | the Court and the other parties | a party | claim / duty not to | `o 18 r 25(10) the party may file more than one set of submissions [18…` |
| O18 r26 | none | none | none (a scope, counting or interpretive rule) | `o 18 r 26 this Division applies to the appeal or application [18h]` |
| O18 r27(1) | the Court and the other parties | a party | claim / duty | `o 18 r 27(1) the date after which the 14 days for the notice of appea…` and 2 more |
| O18 r27(2) | the appellate Court | the parties affected | power / liability | `o 18 r 27(2) the appellate Court may extend the time for filing and s…` and 1 more |
| O18 r28(1) | the parties | the Court | claim / duty | `o 18 r 28(1) the request for further arguments is made as the Rule re…` |
| O18 r28(2) | the parties | the Court | claim / duty | `o 18 r 28(2) the request is made within the time provided in section …` |
| O18 r28(3) | the Court and the other parties | the party concerned | claim / duty | `o 18 r 28(3) the request sets out the proposed arguments and a copy o…` |
| O18 r28(4) | the parties | the Registrar | claim / duty | `o 18 r 28(4) the period after receiving the request for informing the…` and 1 more |
| O18 r28(5) | none | none | none (a deeming) | `o 18 r 28(5) it is deemed that the Judge does not require further arg…` |
| O18 r29(1) | the Court and the other parties | a party | claim / duty | `o 18 r 29(1) the period after the date of the lower Court's decision …` and 1 more |
| O18 r29(2) | the Judge | the parties affected | power / liability | `o 18 r 29(2) the Judge who made the decision may hear further argumen…` and 1 more |
| O18 r29(3) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 29(3)(a) an application for permission to appeal against the d…` and 3 more |
| O18 r29(4) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 29(4) paragraphs (2) and (3) do not affect section 29B of the …` and 1 more |
| O18 r29(5) | the Court | the parties affected | power / liability | `o 18 r 29(5) the Court of Appeal may grant permission to appeal again…` and 1 more |
| O18 r29(6) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 29(6) the period after the Registrar’s notification for the ap…` and 1 more |
| O18 r29(7) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 29(7)(a) the written submissions and any bundle of authorities…` and 2 more |
| O18 r29(8) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 29(8) the period after service of the application for the oppo…` and 1 more |
| O18 r29(9) | the Court and the other parties | a party | claim / duty | `o 18 r 29(9) the application, written submissions and bundles are ser…` |
| O18 r29(10) | the parties | the appellate Court | claim / duty | `o 18 r 29(10) the written submissions are subject to a page limit of …` and 2 more |
| O18 r29(11) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 29(11) the number of pages of the bundle of documents is withi…` |
| O18 r29(12) | the appellate Court | the parties affected | power / liability | `o 18 r 29(12) the appellate Court may allow the page limit to be exce…` |
| O18 r29(13) | the appellate Court | the parties affected | power / liability | `o 18 r 29(13) the appellate Court may upon application waive, refund,…` |
| O18 r29(14) | the Court and the other parties | a party | claim / duty not to | `o 18 r 29(14) the party may file more than one set of submissions [18…` |
| O18 r29(15) | the parties | the appellate Court | claim / duty | `o 18 r 29(15) an affidavit may be filed in the application for permis…` |
| O18 r29(16) | the parties | the appellate Court | claim / duty | `o 18 r 29(16) oral arguments may be made in the application for permi…` |
| O18 r29(17) | the Court and the other parties | the applicant | claim / duty | `o 18 r 29(17) the period after the decision granting permission for t…` and 1 more |
| O18 r29(18) | the appellate Court | the parties affected | power / liability | `o 18 r 29(18) the appellate Court may extend the time for filing and …` |
| O18 r30(1) | the Court and the other parties | the appellant | claim / duty | `o 18 r 30(1) the appellant has provided security and filed the certif…` |
| O18 r30(2) | the Court and the other parties | the appellant | claim / duty | `o 18 r 30(2) the appellants need to provide only one set of security …` |
| O18 r30(3) | the Court and the other parties | the respondent | claim / duty | `o 18 r 30(3) the appellant must provide security for each respondent …` and 1 more |
| O18 r30(4) | the Court and the other parties | the party concerned | claim / duty | `o 18 r 30(4) the security is in a form the Rule allows [18h]` |
| O18 r30(5) | the Court and the other parties | the appellant | claim / duty | `o 18 r 30(5) the amount of security required [18h]` and 2 more |
| O18 r30(6) | a party | the Court and the other parties | privilege / no-right | `o 18 r 30(6) any party may apply to the appellate Court to vary or wa…` |
| O18 r30(7) | the appellate Court | the parties affected | power / liability | `o 18 r 30(7) the appellate Court may order further security for costs…` |
| O18 r31(1) | the appellate Court | the parties affected | power / liability | `o 18 r 31(1) the appellate Court may give directions for the filing a…` |
| O18 r31(2) | the Court | the parties affected | power / liability | `o 18 r 31(2) the directions in paragraph (1) may be given on the appe…` |
| O18 r31(3) | the appellate Court | the parties affected | power / liability | `o 18 r 31(3) the appellate Court may give directions under paragraph …` |
| O18 r31(4) | the appellate Court | the parties affected | power / liability | `o 18 r 31(4) the appellate Court may direct any modifications of the …` |
| O18 r32(1) | the appellate Court | the parties affected | power / liability | `o 18 r 32(1) the appellate Court may, if it deems appropriate, order …` |
| O18 r32(2) | the appellate Court | the parties affected | power / liability | `o 18 r 32(2) the appellate Court may in any case, if it deems appropr…` |
| O18 r32(3) | the appellate Court | the parties affected | power / liability | `o 18 r 32(3) the appellate Court may make an order or give a directio…` |
| O18 r33(1) | the lower Court | the parties affected | power / liability | `o 18 r 33(1) the lower Court may give a summary of the points decided…` |
| O18 r33(2) | the parties | the lower Court | claim / duty | `o 18 r 33(2) the period after the filing of the notice of appeal for …` and 3 more |
| O18 r33(3) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 33(3)(b) the period after the certification before the appella…` and 5 more |
| O18 r33(4) | the parties | the appellate Court | claim / duty | `o 18 r 33(4) the appeal must proceed by way of a rehearing on the doc…` and 1 more |
| O18 r33(5) | the Court and the other parties | a party | claim / duty | `o 18 r 33(5) the period for the written submissions [18h]` and 3 more |
| O18 r33(6) | the parties | the appellate Court | claim / duty | `o 18 r 33(6) the written submissions include submissions on the appro…` and 3 more |
| O18 r33(7) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 33(7) the party is required to file separate written submissio…` |
| O18 r33(8) | the Court and the other parties | a party | claim / duty | `o 18 r 33(8) the parties must try to agree on filing a single set of …` |
| O18 r33(9) | the Court and the other parties | a party | claim / duty | `o 18 r 33(9) the parties must request in writing for a case conferenc…` |
| O18 r33(10) | the Court and the other parties | a party | claim / duty | `o 18 r 33(10) the parties must inform the Registrar in writing of the…` |
| O18 r33(11) | the appellate Court | the parties affected | power / liability | `o 18 r 33(11) a document other than those set out in the Rule may be …` |
| O18 r33(12) | none | none | none (a deeming) | `o 18 r 33(12) the appeal is deemed withdrawn [18h]` and 3 more |
| O18 r33(13) | a party | the Court and the other parties | privilege / no-right | `o 18 r 33(13) the security for costs must be paid and the solicitor's…` |
| O18 r33(14) | none | none | none (a deeming) | `o 18 r 33(14)(a) the period after the appeal is deemed withdrawn for …` and 4 more |
| O18 r33(15) | the Court and the other parties | the respondent | claim / duty not to | `o 18 r 33(15) the respondent is allowed to make submissions at the he…` |
| O18 r33(16) | the appellate Court | the parties affected | power / liability | `o 18 r 33(16) the appellate Court may allow the page limit to be exce…` |
| O18 r33(17) | the appellate Court | the parties affected | power / liability | `o 18 r 33(17) the appellate Court may upon application waive, refund,…` |
| O18 r33(18) | the Court and the other parties | a party | claim / duty not to | `o 18 r 33(18) the party may file more than one set of submissions [18…` |
| O18 r34(1) | the parties | the Court | claim / duty | `o 18 r 34(1) this Rule applies without the need for an order from the…` and 1 more |
| O18 r34(2) | the Court and the other parties | the appellant | claim / duty | `o 18 r 34(2) the security for costs must be paid to the respondent to…` and 2 more |
| O18 r34(3) | the Court and the other parties | the appellant | claim / duty | `o 18 r 34(3) the security for costs must be paid to the appellant [18…` and 1 more |
| O18 r34(4) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 34(4) paragraphs (2) and (3) apply to the payment out of secur…` |
| O18 r35(1) | the parties | the appellate Court | claim / duty | `o 18 r 35(1) the application to the appellate Court is made in the fo…` |
| O18 r35(2) | the lower Court | the parties affected | power / liability | `o 18 r 35(2) the application may be made in the first instance to the…` |
| O18 r35(3) | the parties | the appellate Court | claim / duty | `o 18 r 35(3) oral arguments may be made in an application to the appe…` |
| O18 r35(4) | the Court and the other parties | a party | claim / duty | `o 18 r 35(4) the period after service of the application for the affi…` and 2 more |
| O18 r35(5) | the Court and the other parties | a party | claim / duty | `o 18 r 35(5) the applicant has provided security and filed the certif…` |
| O18 r35(6) | the Court and the other parties | the applicant | claim / duty | `o 18 r 35(6) the applicants need to provide only one set of security …` |
| O18 r35(7) | the Court and the other parties | the opposing party | claim / duty | `o 18 r 35(7) the applicant must provide security for each opposing pa…` and 1 more |
| O18 r35(8) | the Court and the other parties | the party concerned | claim / duty | `o 18 r 35(8) the security is in a form the Rule allows [18h]` |
| O18 r35(9) | the Court and the other parties | the applicant | claim / duty | `o 18 r 35(9) the amount of security required [18h]` and 2 more |
| O18 r35(10) | a party | the Court and the other parties | privilege / no-right | `o 18 r 35(10) any party may apply to the appellate Court to vary or w…` |
| O18 r35(11) | the appellate Court | the parties affected | power / liability | `o 18 r 35(11) the appellate Court may order further security for cost…` |
| O18 r35(12) | the parties | the appellate Court | claim / duty | `o 18 r 35(12) the application to strike out a notice of appeal is mad…` |
| O18 r35(13) | the Court and the other parties | the applicant | claim / duty | `o 18 r 35(13) the period after service of the notice of appeal for th…` and 1 more |
| O18 r35(14) | the Court and the other parties | a party | claim / duty | `o 18 r 35(14) the period after service of the summons to strike out f…` and 1 more |
| O18 r35(15) | the appellate Court | the parties affected | power / liability | `o 18 r 35(15) a further affidavit may be received in evidence [18h]` |
| O18 r36 | none | none | none (a scope, counting or interpretive rule) | `o 18 r 36 the period after the direction or order for the application…` and 1 more |
| O18 r37(1) | the parties | the appellate Court | claim / duty | `o 18 r 37(1) the period after the date the opposing party’s affidavit…` and 1 more |
| O18 r37(2) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 37(2) the written submissions are subject to a page limit of 3…` and 1 more |
| O18 r37(3) | the appellate Court | the parties affected | power / liability | `o 18 r 37(3) the appellate Court may allow the page limit to be excee…` |
| O18 r37(4) | the appellate Court | the parties affected | power / liability | `o 18 r 37(4) the appellate Court may upon application waive, refund, …` |
| O18 r37(5) | the Court and the other parties | a party | claim / duty not to | `o 18 r 37(5) the party may file more than one set of submissions [18h]` |
| O18 r37(6) | the Court and the other parties | the party concerned | claim / duty | `o 18 r 37(6) the concluding paragraphs of the written submissions are…` |
| O18 r38 | the parties | the appellate Court | claim / duty | `o 18 r 38 further arguments from the parties are allowed [18h]` and 1 more |
| O18 r39(1) | the Registrar | the parties affected | power / liability | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate D…` |
| O18 r39(2) | the Registrar | the parties affected | power / liability | `o 18 r 39(2) the period after the Registrar’s direction or order for …` and 2 more |
| O18 r40(1) | the Court | the parties affected | power / liability | `o 18 r 40(1) the Court of Appeal may exercise its power under section…` |
| O18 r40(2) | the Court | the parties affected | power / liability | `o 18 r 40(2) the Court of Appeal may exercise its power under section…` |
| O18 r40(3) | the parties | the Court | claim / duty | `o 18 r 40(3) the period after service of the notice of appeal for the…` and 1 more |
| O18 r40(4) | the parties | the Court | claim / duty | `o 18 r 40(4) the period after the date the written submissions are re…` and 2 more |
| O18 r40(5) | the Court | the parties affected | power / liability | `o 18 r 40(5) the Court of Appeal may have regard to the matter [18h]` and 1 more |
| O18 r41(1) | the parties | the Court | claim / duty | `o 18 r 41(1) the Court of Appeal is to have regard to the matter [18h]` |
| O18 r41(2) | none | none | none (a scope, counting or interpretive rule) | `o 18 r 41(2) the period after service of the notice of appeal for the…` and 1 more |

## Marginal readings for a lawyer (roc3)

These are the branches that rest on one of the two readings the rule of 2026-10-29 marks "for a lawyer, not for you to decide": (a) a failed "if" (or "where", or a period that has run out) counts as the text's no, clause by clause; (b) a prohibition or grant limited by its own wording does not.
The status quo is taken in both cases.
Flat negatives ("does not", "may not", "is not entitled") are not marginal: ruling N2 counts them as the text's no.
Part A has 265 branches; part B has 190.

### A. A failed "if", "where" or "unless", a period that has run out, or a requirement not met, read as the text's no (rule of 2026-10-29 (a); rulings of 2026-11-05 (a), (b))

Each branch answers `JUST FALSE` because the condition the text states is not met.
The other reading is `NOTHING`: "if A then B" does not itself say "if not A then not B".

| provision | function | the words the branch rests on | reading taken |
| --- | --- | --- | --- |
| O 15 r 1(3) | `o 15 r 1(3) the matter must be heard in open court` | "unless the Appellate Division or Court of Appeal (as the case may be) otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 15 r 3(1) | `o 15 r 3(1) the party attends as the Rule requires` | "All parties must attend the hearing of any matter in person (if they are not legally repr…" | a requirement not met read as the text's no |
| O 15 r 3(3) | `o 15 r 3(3) the Court may dispense with the attendance of the parties or their …` | "where oral evidence is given at any part of the proceedings (including any part of a tria…" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 15 r 4(2) | `o 15 r 4(2) the order is as the Rule requires` | "must state the requesting party and whether the witness is to give oral evidence or to pr…" | a requirement not met read as the text's no |
| O 15 r 4(3) | `o 15 r 4(3) the order is served in the way and in time the Rule requires` | "at least 28 days before the hearing" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 4(3) | `o 15 r 4(3) the order is served in the way and in time the Rule requires` | "must be served by the requesting party on the witness by personal service in Singapore" | a requirement not met read as the text's no |
| O 15 r 4(6) | `o 15 r 4(6) the application for review is made as the Rule requires` | "within 14 days after that decision" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 4(6) | `o 15 r 4(6) the application for review is made as the Rule requires` | "must be made by summons supported by an affidavit" | a requirement not met read as the text's no |
| O 15 r 4(7) | `o 15 r 4(7) the order continues to have effect` | "until the conclusion of the hearing" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 4(9) | `o 15 r 4(9) the witness is entitled to claim reasonable compensation for time a…` | "upon request" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 15 r 4(12) | `o 15 r 4(12) the order to attend court is served on the Superintendent of the p…` | "must be served at least 14 days before the hearing" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 4(13) | `o 15 r 4(13) the witness must remain outside the courtroom` | "until he or she is called into Court" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 4(15) | `o 15 r 4(15) the requesting party may request the Registrar to produce the docu…` | "Where a document filed in Court or the Court's records are required for the hearing" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 5(1) | `o 15 r 5(1) an application may be made for an order in Form 30 for the issue of…` | "Where — ( a ) an application is made for permission for any person outside Singapore to g…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 5(3) | `o 15 r 5(3) the application is made as the Rule requires` | "must be made by summons and supported by an affidavit setting out the basis for the appli…" | a requirement not met read as the text's no |
| O 15 r 5(4) | `o 15 r 5(4) paragraphs (5) to (8) apply` | "Where an order is made under paragraph (1) for the issue of a letter of request" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 5(6) | `o 15 r 5(6) a translation must accompany the letter of request or a document at…` | "unless that jurisdiction accepts the letter or document in English" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 15 r 5(7) | `o 15 r 5(7) the translation is certified as the Rule requires` | "must be certified by the person making it to be a correct translation; and the certificat…" | a requirement not met read as the text's no |
| O 15 r 5(8) | `o 15 r 5(8) the party obtaining the order must also file an undertaking in Form…` | "when the party files in the Registry the documents mentioned in paragraphs (5), (6) and (…" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 15 r 5(8) | `o 15 r 5(8) the undertaking is signed as the Rule requires` | "signed by the party or the party's solicitor" | a requirement not met read as the text's no |
| O 15 r 6(2) | `o 15 r 6(2) the Court may disallow the person to attend the hearing` | "The Court may disallow any person to attend any hearing if" | a failed "if" read as the text's no |
| O 15 r 7(3) | `o 15 r 7(3) the Court may dismiss the matter` | "If none of the parties attends Court when the hearing begins" | a failed "if" read as the text's no |
| O 15 r 7(4) | `o 15 r 7(4) the Court may proceed with the hearing, give judgment against or di…` | "If one of the parties does not attend Court when the hearing begins" | a failed "if" read as the text's no |
| O 15 r 7(5) | `o 15 r 7(5) the originating application or summons must be decided on affidavit…` | "Unless otherwise provided in any written law or the Court otherwise directs" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 15 r 7(6) | `o 15 r 7(6) the Court may order further affidavits, cross-examination of the ma…` | "Where the Court is of the view that there are disputes of facts in the affidavits" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 8(3) | `o 15 r 8(3) the Court may dismiss the claim and any counterclaim` | "If none of the parties attends Court when the trial begins" | a failed "if" read as the text's no |
| O 15 r 8(4) | `o 15 r 8(4) the Court may proceed with the trial, give judgment against or dism…` | "If one of the parties does not attend Court when the trial begins" | a failed "if" read as the text's no |
| O 15 r 8(7) | `o 15 r 8(7) the claimant's evidence is given in the order the Rule requires` | "The claimant must begin and testify before the claimant's witnesses" | a requirement not met read as the text's no |
| O 15 r 8(9) | `o 15 r 8(9) the defendant's evidence is given in the order the Rule requires` | "When the claimant and the claimant's witnesses have completed giving their evidence" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 15 r 8(9) | `o 15 r 8(9) the defendant's evidence is given in the order the Rule requires` | "the defendant must begin and testify before the defendant's witnesses" | a requirement not met read as the text's no |
| O 15 r 8(11)(d) | `o 15 r 8(11)(d) the defendant who makes the submission may rely on the evidence…` | "if those experts have already given evidence as a panel of experts during the claimant's …" | a failed "if" read as the text's no |
| O 15 r 11(3) | `o 15 r 11(3) the exhibits kept with the Court may be returned to the relevant p…` | "after the time for appealing has expired or after any appeal has been decided" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 11(4) | `o 15 r 11(4) the Court may dispose of the exhibits` | "Where the Court has given the relevant parties at least 14 days’ notice to take back thei…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 11(4) | `o 15 r 11(4) the costs incurred in the disposal must be paid by the relevant pa…` | "Where the Court has given the relevant parties at least 14 days’ notice to take back thei…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 11(6) | `o 15 r 11(6) the audio recording is the official record of the hearing` | "In a hearing where an audio recording system approved by the Registrar is used" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 11(7) | `o 15 r 11(7) the Court's notes of proceedings are the official record of the he…` | "In a hearing where an audio recording system is not used" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 11(8) | `o 15 r 11(8) the party may apply for a certified transcript of the official rec…` | "upon payment of the relevant fees" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 15 r 11(9) | `o 15 r 11(9) the costs of producing a certified transcript may be claimed as an…` | "unless otherwise ordered by the Court" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 15 r 11(10) | `o 15 r 11(10) the transcript is certified in the manner the Registrar determined` | "must be certified in such manner as the Registrar may determine" | a requirement not met read as the text's no |
| O 15 r 11(11) | `o 15 r 11(11) the official record of the hearing must still be kept` | "kept for 5 years beginning from the last day of the hearing" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 12(2) | `o 15 r 12(2) the parties are entitled to a copy of the decision` | "upon payment of the relevant charges" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 15 r 12(3) | `o 15 r 12(3) the Court may dispense with the attendance of the parties and reco…` | "Where the parties in any matter inform the Registrar in writing that they wish to record …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 12(3) | `o 15 r 12(3) the Registrar is to inform the parties that the judgment or order …` | "Where the parties in any matter inform the Registrar in writing that they wish to record …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 14(1) | `o 15 r 14(1) another Judge or Registrar may take over and give a decision based…` | "Where a Judge or a Registrar who has heard a matter has not given his or her decision, or…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 14(1) | `o 15 r 14(1) another Judge or Registrar may take over and give a decision based…` | "if all the parties consent" | a failed "if" read as the text's no |
| O 15 r 14(3) | `o 15 r 14(3) the matter must be heard anew by another Judge or Registrar` | "If the parties do not consent under paragraph (1)" | a failed "if" read as the text's no |
| O 15 r 15(2) | `o 15 r 15(2) the Court must give judgment on liability and on the amount of dam…` | "if the hearing was not ordered to be bifurcated" | a failed "if" read as the text's no |
| O 15 r 15(3) | `o 15 r 15(3) the Court may give directions on the assessment of damages and pro…` | "If the hearing was ordered to be bifurcated, when the Court gives judgment on liability" | a failed "if" read as the text's no |
| O 15 r 15(4) | `o 15 r 15(4) the damages must be assessed by the Registrar or Judge` | "If the hearing was ordered to be bifurcated, and the Court gives judgment on liability an…" | a failed "if" read as the text's no |
| O 15 r 15(4) | `o 15 r 15(4) the application for directions is made in time` | "within one month from the date of the judgment" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 15(4) | `o 15 r 15(4) the party must apply to the Court for directions` | "If the hearing was ordered to be bifurcated, and the Court gives judgment on liability an…" | a failed "if" read as the text's no |
| O 15 r 15(5) | `o 15 r 15(5) the notice of appointment is served in time` | "not later than 14 days after the date of filing" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 15(6) | `o 15 r 15(6) the damages must be assessed until the date of decision in the ass…` | "Where damages are in respect of any continuing cause of action" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 15(7) | `o 15 r 15(7) the Court may make an award for provisional damages` | "Where the damages are for personal injuries" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 15(10) | `o 15 r 15(10) the Court may specify a different period for each contingency` | "If there is more than one contingency" | a failed "if" read as the text's no |
| O 15 r 15(11) | `o 15 r 15(11) the Court may extend the period in paragraph (9) or (10)` | "if the claimant applies for an extension within the period stated" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 15(13) | `o 15 r 15(13) the application for further damages must be served on the defenda…` | "if the claimant knows that the defendant is insured in respect of the claimant's claim" | a failed "if" read as the text's no |
| O 15 r 15(17) | `o 15 r 15(17) the Court must give the appropriate directions for the taking of …` | "Where the damages are for amounts due on taking of accounts" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 16(4) | `o 15 r 16(4) the new fact may be given in oral evidence` | "which may not be departed from or supplemented by new facts in oral evidence unless the n…" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 15 r 16(6) | `o 15 r 16(6) the party must give notice of objection to the party relying on th…` | "If a party intends to object to the contents of affidavits of evidence‑in‑chief" | a failed "if" read as the text's no |
| O 15 r 16(6) | `o 15 r 16(6) the notice of objection is given in time` | "at least 28 days before the first date of the hearing" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 15 r 16(6) | `o 15 r 16(6) the notice of objection is given in time` | "by filing and serving the form specified in the practice directions" | a requirement not met read as the text's no |
| O 15 r 16(7) | `o 15 r 16(7) the party must give notice by letter to all other parties` | "If a party intends to rely on statements in affidavits of evidence‑in‑chief pursuant to s…" | a failed "if" read as the text's no |
| O 15 r 16(9) | `o 15 r 16(9) the notice for statements contained in a document contains what th…` | "the notice in paragraph (7) must contain the following" | a requirement not met read as the text's no |
| O 15 r 16(10) | `o 15 r 16(10) the notice for statements not contained in a document contains wh…` | "the notice in paragraph (7) must contain the following" | a requirement not met read as the text's no |
| O 15 r 18 | `o 15 r 18 the document is an affidavit` | "An affidavit is a statement of evidence in the English language, signed and affirmed befo…" | a closed definition read as no |
| O 15 r 19(1) | `o 15 r 19(1) the affidavit is in the form the Rule requires` | "An affidavit must be in Form 31, with the text set out in consecutively numbered paragrap…" | a requirement not met read as the text's no |
| O 15 r 19(2) | `o 15 r 19(2) the photograph is as the Rule requires` | "measures 35 mm wide and 45 mm high" | a requirement not met read as the text's no |
| O 15 r 20 | `o 15 r 20 the person may make an affidavit` | "must be legally competent to give evidence in court" | a requirement not met read as the text's no |
| O 15 r 21 | `o 15 r 21 two or more persons may make a joint affidavit` | "if all the facts that they are affirming are the same" | a failed "if" read as the text's no |
| O 15 r 22(3) | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule requires` | "Where the affidavit is to be taken, and an oath for the taking of the affidavit is to be …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 22(3) | `o 15 r 22(3) the commissioner for oaths is able to do what the Rule requires` | "the commissioner for oaths must be able to" | a requirement not met read as the text's no |
| O 15 r 24 | `o 15 r 24 the commissioner for oaths must certify on the affidavit the matters …` | "Where the maker of the affidavit is not able to understand English, is illiterate or blind" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 24 | `o 15 r 24 the certificate is as the Rule requires` | "the commissioner for oaths must certify on the affidavit that" | a requirement not met read as the text's no |
| O 15 r 25(2) | `o 15 r 25(2) the affidavit may contain the matter` | "vulgar or insulting words unless those words are in issue in the action" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 15 r 26(1) | `o 15 r 26(1) the affidavit may be altered` | "if the affidavit is re-affirmed before a commissioner for oaths" | a failed "if" read as the text's no |
| O 15 r 27(1) | `o 15 r 27(1) a copy of the document must be annexed to the affidavit` | "Where an affidavit refers to a document" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 27(2) | `o 15 r 27(2) a copy of the whole document must be annexed` | "If it is necessary to refer to the whole document" | a failed "if" read as the text's no |
| O 15 r 27(3) | `o 15 r 27(3) a copy of only those portions of the document need to be annexed` | "If it is necessary to refer to only certain portions of the document" | a failed "if" read as the text's no |
| O 15 r 27(4) | `o 15 r 27(4) the identification may be done by annexing a picture of the person…` | "Where an affidavit refers to a person or object and it is necessary to identify that pers…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 15 r 28 | `o 15 r 28 the seal or signature of the commissioner for oaths must be accepted …` | "unless the contrary is shown" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 16 r 2(1) | `o 16 r 2(1) the claimant may discontinue the action or withdraw a claim without…` | "at any time not later than 14 days after service of the defence" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 16 r 2(2)(b) | `o 16 r 2(2)(b) the defendant may discontinue the counterclaim or withdraw a cla…` | "at any time not later than 14 days after service on the defendant of a defence to counter…" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 16 r 2(5) | `o 16 r 2(5) the action may be withdrawn without the permission of the Court on …` | "at any time before trial" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 16 r 2(7) | `o 16 r 2(7) the action, cause or matter is deemed to have been discontinued` | "for more than one year" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 16 r 2(9) | `o 16 r 2(9) the Court may extend the time` | "on an application by any party made before the one year mentioned in paragraph (7) has el…" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 16 r 3(1) | `o 16 r 3(1) a party may discontinue the action or counterclaim or withdraw a cl…` | "a party may not discontinue an action (whether begun by originating claim or otherwise) o…" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 17 r 1 | `o 17 r 1 the thing is an order for the purposes of this Order` | "“order” means an order of the Court and includes a judgment given at any stage of the act…" | a closed definition read as no |
| O 17 r 2(1) | `o 17 r 2(1) the order takes effect from the day that it is given` | "unless the Court otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 17 r 2(2) | `o 17 r 2(2) the Court must give that person a reasonable time within which to c…` | "Where an order requires a person to pay money, to do or to stop doing an act or to perfor…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 2(2) | `o 17 r 2(2) the Court must give that person a reasonable time within which to c…` | "unless the Court intends that the money must be paid, the act must be done or stopped or …" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 17 r 2(3) | `o 17 r 2(3) the order is deemed to require immediate compliance` | "If no time for compliance is specified under paragraph (2)" | a failed "if" read as the text's no |
| O 17 r 3(1) | `o 17 r 3(1) the order must be drawn up and filed in Court` | "Unless the Court otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 17 r 3(2) | `o 17 r 3(2) the order is in the form that the Rule requires` | "All orders must be in Form 33" | a requirement not met read as the text's no |
| O 17 r 3(4) | `o 17 r 3(4) the party must draw up only one order for all the applications` | "Where a party takes out more than one application and the applications are heard together" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 3(5) | `o 17 r 3(5) the draft is sent in time` | "within 14 days after the order is made" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 17 r 3(5) | `o 17 r 3(5) another party affected by the order may draw it up` | "if that party fails to do so, any other party affected by the order may draw it up" | a failed "if" read as the text's no |
| O 17 r 3(6) | `o 17 r 3(6) the solicitors respond in time` | "within 2 days" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 17 r 3(7) | `o 17 r 3(7) the party who drew up the order may write to the Court to resolve t…` | "Where there is a dispute on the terms of the draft" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 3(7) | `o 17 r 3(7) the letter to the Court is as the Rule requires` | "the letter must set out the areas of dispute" | a requirement not met read as the text's no |
| O 17 r 3(9) | `o 17 r 3(9) the draft of the order is to be submitted to the Registrar` | "Where any of the other parties has no solicitor" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 4(1) | `o 17 r 4(1) the Court may redact the order` | "in the interests of justice or where the order was made in hearings which were conducted …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 4(2) | `o 17 r 4(2) the Court may prohibit the person from inspecting or taking copies …` | "in the interests of justice or where the order was made in hearings which were conducted …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 5(1) | `o 17 r 5(1)(a) the money carries interest as agreed between the parties` | "Where money is payable under an order, it carries" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 5(1)(b) | `o 17 r 5(1)(b) the money carries simple interest at 5.33% per year` | "Where money is payable under an order, it carries" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 5(1)(b) | `o 17 r 5(1)(b) the money carries simple interest at 5.33% per year` | "if there is no agreement on interest, simple interest at 5.33% per year" | a failed "if" read as the text's no |
| O 17 r 5(3) | `o 17 r 5(3) interest is to be calculated from the date that each instalment is …` | "Where instalment payments are allowed by the Court" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 17 r 5(4) | `o 17 r 5(4) a part payment must be used to reduce the principal amount due befo…` | "Where part payments are made on money payable under an order" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 3(1) | `o 18 r 3(1) the time for filing an appeal or an application for permission to a…` | "unless the Court otherwise orders" | a bar that has lifted or been lifted: the bar's own yes/no question answers no (ruling of 2026-11-05, delegated (d); fork 18.6) |
| O 18 r 3(1) | `o 18 r 3(1) the time for filing an appeal or an application for permission to a…` | "until after the lower Court has heard and determined all matters in an application, inclu…" | a bar that has lifted or been lifted: the bar's own yes/no question answers no (ruling of 2026-11-05, delegated (d); fork 18.6) |
| O 18 r 3(1A) | `o 18 r 3(1A) the time starts to run after the expiry of the 30-day period` | "Where the lower Court does not hear and determine the issue of costs within 30 days" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 3(2)(a) | `o 18 r 3(2)(a) the lower Court is deemed to have heard and determined the issue…` | "is deemed to have heard and determined the issue of costs when it has" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 3(2)(b) | `o 18 r 3(2)(b) the time is still barred from running because not all the matter…` | "time does not run until all matters have been heard and determined" | a bar that has lifted or been lifted: the bar's own yes/no question answers no (ruling of 2026-11-05, delegated (d); fork 18.6) |
| O 18 r 3(2)(c) | `o 18 r 3(2)(c) paragraph (2)(c) applies to the single application` | "in the case of a single application pending trial, where one or more matters dealt with i…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 3(2)(c)(i) | `o 18 r 3(2)(c)(i) the time for the appeal against the decision of the Registrar…` | "where one or more matters ... are to be heard before the Registrar and one or more other …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 3(2)(c)(ii) | `o 18 r 3(2)(c)(ii) the time for the appeal or the application for permission ag…` | "where one or more matters ... are to be heard before the Registrar and one or more other …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 3(2)(d) | `o 18 r 3(2)(d) the time for the appeal or the application for permission agains…` | "in the case of a single application pending trial dealing with more than one matter, wher…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 3(2)(d) | `o 18 r 3(2)(d) the time for the appeal or the application for permission agains…` | "in the case of a single application pending trial dealing with more than one matter, wher…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 3(2)(d) | `o 18 r 3(2)(d) the time for the appeal or the application for permission agains…` | "does not begin to run until that Court" | a bar that has lifted or been lifted: the bar's own yes/no question answers no (ruling of 2026-11-05, delegated (d); fork 18.6) |
| O 18 r 4(2) | `o 18 r 4(2) the party must file a separate notice of appeal for the matters whi…` | "In the case of a single application pending trial dealing with more than one matter and w…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 4(3) | `o 18 r 4(3) each party may file one appeal in respect of all the applications` | "Where several applications are heard together" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 5(3) | `o 18 r 5(3) the supporting affidavit is as the Rule requires` | "The supporting affidavit must set out the applicant’s interest in the appeal" | a requirement not met read as the text's no |
| O 18 r 5(4) | `o 18 r 5(4) the appellate Court may impose conditions, including ordering the i…` | "when the appellate Court grants permission to intervene" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 6(3) | `o 18 r 6(3) interest is to be allowed for the time enforcement has been delayed…` | "unless the lower Court or the appellate Court otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 9(1) | `o 18 r 9(1) the appeal may be dismissed` | "If the appellant or the appellant’s solicitor fails to attend at the appeal" | a failed "if" read as the text's no |
| O 18 r 9(2) | `o 18 r 9(2) the appeal may proceed in the absence of the respondent` | "If the appellant or the appellant’s solicitor attends and any respondent or the responden…" | a failed "if" read as the text's no |
| O 18 r 9(3) | `o 18 r 9(3) the application to restore the appeal is filed and served in time` | "within 14 days after the dismissal or hearing of the appeal" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 9(3) | `o 18 r 9(3) the Court may restore the appeal for rehearing` | "upon the application of the absent party" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 9(3) | `o 18 r 9(3) the Court may restore the appeal for rehearing` | "within 14 days after the dismissal or hearing of the appeal" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 9(3) | `o 18 r 9(3) the Court may restore the appeal for rehearing` | "must show good reason for that party’s absence" | a requirement not met read as the text's no |
| O 18 r 10 | `o 18 r 10 the appellate Court may intervene` | "intervene only if substantial injustice will be caused otherwise" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 11(1) | `o 18 r 11(1) the lower Court or the appellate Court may order an expedited appe…` | "If the appeal is urgent or there is a special reason" | a failed "if" read as the text's no |
| O 18 r 12(1) | `o 18 r 12(1) the appellant may withdraw the appeal or the applicant may withdra…` | "at any time before the appeal or application is heard or dealt with" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 12(2) | `o 18 r 12(2) the appeal or application is deemed withdrawn in relation to the r…` | "Upon the filing of Form 34 and if there are no outstanding issues relating to costs or ot…" | a failed "if" read as the text's no |
| O 18 r 12(2) | `o 18 r 12(2) the security for costs must be paid and the solicitor's undertakin…` | "if all the parties to the appeal or application consent to the payment of the security fo…" | a failed "if" read as the text's no |
| O 18 r 12(2) | `o 18 r 12(2) the security for costs must be paid and the solicitor's undertakin…` | "must file the document signifying such consent signed by the parties and in such event" | an "in such event" that is not met, read as "in the event of" and so as "where" (assumed, not ruled: fork 15.7) |
| O 18 r 12(3) | `o 18 r 12(3)(a) the party may request in writing to the appellate Court for dir…` | "If there are any such outstanding issues mentioned in paragraph (2)" | a failed "if" read as the text's no |
| O 18 r 12(3)(c) | `o 18 r 12(3)(c) the Registrar may remove the appeal or application from the lis…` | "upon receiving a request under sub‑paragraph ( a )" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 12(4) | `o 18 r 12(4)(b) the appellate Court may at the hearing decide any outstanding i…` | "if there are any such outstanding issues" | a failed "if" read as the text's no |
| O 18 r 13(1) | `o 18 r 13(1) the appellate Court may dispense with the attendance of the partie…` | "Where the parties in any appeal or application to the appellate Court inform the Registra…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 13(1) | `o 18 r 13(1) the Registrar is to inform the parties that the judgment or order …` | "Where the parties in any appeal or application to the appellate Court inform the Registra…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 14(2)(a) | `o 18 r 14(2)(a) the appellate Court may direct the Registrar to inform the part…` | "Where the appellate Court has decided any matter without hearing oral arguments" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 14(2)(b) | `o 18 r 14(2)(b) the parties are to be informed of the Judge or Judges who const…` | "Where the appellate Court has decided any matter without hearing oral arguments" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 14(3) | `o 18 r 14(3) the party is entitled to a copy of the decision` | "upon payment of the relevant charges" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 15 | `o 18 r 15 the notice of appeal in Form 35 is filed and served in time` | "within 14 days after the date of the Registrar’s decision" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 16(3) | `o 18 r 16(3)(a) the Registrar must endeavour to issue the written grounds of de…` | "certifies under paragraph (2)(b)" | a failed "if" read as the text's no |
| O 18 r 16(3) | `o 18 r 16(3)(b)(i) the appellant must apply in writing to the Registrar to proc…` | "if no written grounds of decision are issued within 12 weeks after the certification" | a failed "if" read as the text's no |
| O 18 r 16(3) | `o 18 r 16(3)(b)(ii) the respondent may apply in writing to the Registrar to pro…` | "if the appellant fails to do so" | a failed "if" read as the text's no |
| O 18 r 16(3) | `o 18 r 16(3)(b)(iii) the respondent may apply to strike out the appeal` | "after the expiry of the 14 days’ notice period" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 16(5) | `o 18 r 16(5) the written submissions are filed and served in time` | "within 14 days after" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 16(6) | `o 18 r 16(6) the written submissions are subject to a page limit of 35 pages` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 16(8) | `o 18 r 16(8) the appellate Court may allow the page limit to be exceeded` | "upon the payment of the fees and additional fees prescribed for the filing of pages in ex…" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 16(9) | `o 18 r 16(9) the appellate Court may upon application waive, refund, defer or a…` | "upon application" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 17(1) | `o 18 r 17(1) the notice of appeal in Form 35 is filed and served in time` | "within 14 days after" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 17(2) | `o 18 r 17(2) the lower Court may extend the time for filing and serving the not…` | "if the appellant applies for such extension before the time expires" | a failed "if" read as the text's no |
| O 18 r 17(2) | `o 18 r 17(2) the lower Court may extend the time for filing and serving the not…` | "before the time expires" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 18(2) | `o 18 r 18(2) the request for further arguments is filed in time` | "must be filed before the earlier of the following" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 18(4) | `o 18 r 18(4) the Registrar of the State Courts informs the requesting party in …` | "within 14 days after receiving the request" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 18(5) | `o 18 r 18(5) it is deemed that the District Judge or Magistrate does not requir…` | "it is deemed that the District Judge or Magistrate does not require further arguments" | a failed "if" read as the text's no |
| O 18 r 19(1) | `o 18 r 19(1) the application for permission to the District Judge or Magistrate…` | "Where permission to appeal is required" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 19(1) | `o 18 r 19(1) the application for permission to the District Judge or Magistrate…` | "within 14 days after the date of the District Judge’s or Magistrate’s decision" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 19(2) | `o 18 r 19(2) the application for permission to the General Division is made and…` | "Where the District Judge or Magistrate does not grant permission to appeal" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 19(2) | `o 18 r 19(2) the application for permission to the General Division is made and…` | "within 14 days after the date of the District Judge’s or Magistrate’s decision not to gra…" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 19(3) | `o 18 r 19(3) the notice of appeal in Form 35 is filed and served in time after …` | "Where permission to appeal is granted" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 19(3) | `o 18 r 19(3) the notice of appeal in Form 35 is filed and served in time after …` | "within 14 days after the date of the Court’s decision granting permission" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 19(4) | `o 18 r 19(4) the lower Court may extend the time for filing and serving an appl…` | "if the application for such extension is made before the time expires" | a failed "if" read as the text's no |
| O 18 r 19(4) | `o 18 r 19(4) the lower Court may extend the time for filing and serving an appl…` | "before the time expires" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 20(2) | `o 18 r 20(2) the appellants need to provide only one set of security` | "need to provide only one set of security" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 20(3) | `o 18 r 20(3) the appellant must provide security for each respondent or each se…` | "Where there is more than one" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 20(3) | `o 18 r 20(3) the security is provided for each set of respondents represented b…` | "Where there is more than one" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 20(3) | `o 18 r 20(3) the security is provided for each set of respondents represented b…` | "represented by the same firm of solicitors" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 21(3) | `o 18 r 21(3)(a) the District Judge or Magistrate must endeavour to issue the wr…` | "certifies under paragraph (2)(b)" | a failed "if" read as the text's no |
| O 18 r 21(3) | `o 18 r 21(3)(b)(i) the appellant must apply in writing to the Registrar to proc…` | "if no written grounds of decision are issued within 12 weeks after the certification" | a failed "if" read as the text's no |
| O 18 r 21(3) | `o 18 r 21(3)(b)(ii) the respondent may apply in writing to the Registrar to pro…` | "if the appellant fails to do so" | a failed "if" read as the text's no |
| O 18 r 21(3) | `o 18 r 21(3)(b)(iii) the respondent may apply to strike out the appeal` | "after the expiry of the 14 days’ notice period" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 21(5) | `o 18 r 21(5) the written submissions are filed and served in time` | "within 14 days after" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 21(6) | `o 18 r 21(6) the written submissions are subject to a page limit of 35 pages` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 21(9) | `o 18 r 21(9) the parties must request in writing for a case conference before t…` | "Where the parties are unable to agree as mentioned in paragraph (8)" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 21(10) | `o 18 r 21(10) the parties must inform the Registrar in writing of the timelines…` | "Where the parties have agreed as mentioned in paragraph (8)" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 21(12) | `o 18 r 21(12) the appeal is deemed withdrawn` | "Where the appellant fails to file and serve the written submissions within the specified …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 21(12) | `o 18 r 21(12) the appeal is deemed withdrawn` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 21(13) | `o 18 r 21(13) the security for costs must be paid and the solicitor's undertaki…` | "if all the parties to the appeal consent to the payment of the security for costs" | a failed "if" read as the text's no |
| O 18 r 21(13) | `o 18 r 21(13) the security for costs must be paid and the solicitor's undertaki…` | "must file the document signifying such consent signed by the parties and in such event" | an "in such event" that is not met, read as "in the event of" and so as "where" (assumed, not ruled: fork 15.7) |
| O 18 r 21(14) | `o 18 r 21(14)(a) the appellant or any party to the appeal may request in writin…` | "Where an appeal is deemed withdrawn pursuant to paragraph (12) and if there are any outst…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 21(14) | `o 18 r 21(14)(a) the request is made in time` | "within 14 days after the date that the appeal is deemed withdrawn" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 21(14) | `o 18 r 21(14)(c) the Registrar may give directions on the making of written sub…` | "upon receiving a request under sub-paragraph (a)" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 21(16) | `o 18 r 21(16) the appellate Court may allow the page limit to be exceeded` | "upon the payment of the fees and additional fees prescribed for the filing of pages in ex…" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 21(17) | `o 18 r 21(17) the appellate Court may upon application waive, refund, defer or …` | "upon application" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 22(2) | `o 18 r 22(2) the security for costs must be paid to the respondent towards the …` | "Where costs are payable by the appellant to the respondent under any order made by the" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 22(3) | `o 18 r 22(3) the security for costs must be paid to the appellant` | "Where no costs are payable by the appellant to the respondent under any order made by the" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 22(3) | `o 18 r 22(3) the appellant's solicitor is released from any undertaking as to t…` | "Where no costs are payable by the appellant to the respondent under any order made by the" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 24 | `o 18 r 24 the notice of appeal in Form 35 is filed and served in time` | "within 14 days after the date of the Registrar’s decision" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 25(3) | `o 18 r 25(3)(a) the Registrar must endeavour to issue the written grounds of de…` | "certifies under paragraph (2)(b)" | a failed "if" read as the text's no |
| O 18 r 25(3) | `o 18 r 25(3)(b)(i) the appellant must apply in writing to the Registrar to proc…` | "if no written grounds of decision are issued within 12 weeks after the certification" | a failed "if" read as the text's no |
| O 18 r 25(3) | `o 18 r 25(3)(b)(ii) the respondent may apply in writing to the Registrar to pro…` | "if the appellant fails to do so" | a failed "if" read as the text's no |
| O 18 r 25(3) | `o 18 r 25(3)(b)(iii) the respondent may apply to strike out the appeal` | "after the expiry of the 14 days’ notice period" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 25(5) | `o 18 r 25(5) the written submissions are filed and served in time` | "within 14 days after" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 25(6) | `o 18 r 25(6) the written submissions are subject to a page limit of 35 pages` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 25(8) | `o 18 r 25(8) the Judge may allow the page limit to be exceeded` | "upon the payment of the fees and additional fees prescribed for the filing of pages in ex…" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 25(9) | `o 18 r 25(9) the Judge may upon application waive, refund, defer or apportion t…` | "upon application" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 27(1) | `o 18 r 27(1) the notice of appeal in Form 35 is filed and served in time` | "within 14 days after" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 27(2) | `o 18 r 27(2) the lower Court may extend the time for filing and serving the not…` | "if the appellant applies for such extension before the time expires" | a failed "if" read as the text's no |
| O 18 r 27(2) | `o 18 r 27(2) the lower Court may extend the time for filing and serving the not…` | "before the time expires" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 28(4) | `o 18 r 28(4) the Registrar of the Supreme Court informs the requesting party in…` | "within 14 days after receiving the request" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 28(5) | `o 18 r 28(5) it is deemed that the Judge does not require further arguments` | "it is deemed that the Judge does not require further arguments" | a failed "if" read as the text's no |
| O 18 r 29(1) | `o 18 r 29(1) the application for permission to the appellate Court is made in t…` | "Where permission to appeal against a decision is required" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 29(1) | `o 18 r 29(1) the application for permission to the appellate Court is made in t…` | "within 14 days after the date of the lower Court’s decision" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 29(2) | `o 18 r 29(2) the Judge who made the decision may hear further arguments in resp…` | "Where permission to appeal against a decision is required" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 29(2) | `o 18 r 29(2) the Judge who made the decision may hear further arguments in resp…` | "if any party to the hearing, or the Judge, requests for further arguments" | a failed "if" read as the text's no |
| O 18 r 29(3)(a) | `o 18 r 29(3)(a) an application for permission to appeal against the decision is…` | "If a request for further arguments in respect of a decision has been made under paragraph…" | a failed "if" read as the text's no |
| O 18 r 29(3)(a) | `o 18 r 29(3)(a) an application for permission to appeal against the decision is…` | "until the Judge" | a bar that has lifted or been lifted: the bar's own yes/no question answers no (ruling of 2026-11-05, delegated (d); fork 18.6) |
| O 18 r 29(3)(b) | `o 18 r 29(3)(b) the application for permission and the paragraph (7) documents …` | "If a request for further arguments in respect of a decision has been made under paragraph…" | a failed "if" read as the text's no |
| O 18 r 29(3)(b) | `o 18 r 29(3)(b) the application for permission and the paragraph (7) documents …` | "within 14 days after the date the Judge" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 29(5) | `o 18 r 29(5) the Court of Appeal may grant permission to appeal against a decis…` | "Where permission to appeal under section 47(1) of the Supreme Court of Judicature Act is …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 29(5) | `o 18 r 29(5) the Court of Appeal may grant permission to appeal against a decis…` | "the Court of Appeal may grant permission to appeal against a decision of the Appellate Di…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 29(6) | `o 18 r 29(6) the party applies to the relevant appellate Court for permission i…` | "within 14 days after the date of the Registrar’s notification" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 29(8) | `o 18 r 29(8) the opposing party's written submissions are filed and served in t…` | "within 14 days after the application, written submissions, any accompanying bundle of aut…" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 29(10) | `o 18 r 29(10) the written submissions are subject to a page limit of 15 pages` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 29(12) | `o 18 r 29(12) the appellate Court may allow the page limit to be exceeded` | "upon the payment of the fees and additional fees prescribed for the filing of pages in ex…" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 29(13) | `o 18 r 29(13) the appellate Court may upon application waive, refund, defer or …` | "upon application" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 29(17) | `o 18 r 29(17) the notice of appeal in Form 35 is filed and served in time after…` | "Where permission to appeal is granted" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 29(17) | `o 18 r 29(17) the notice of appeal in Form 35 is filed and served in time after…` | "within 14 days after the date of the decision granting permission" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 30(2) | `o 18 r 30(2) the appellants need to provide only one set of security` | "need to provide only one set of security" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 30(3) | `o 18 r 30(3) the appellant must provide security for each respondent or each se…` | "Where there is more than one" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 30(3) | `o 18 r 30(3) the security is provided for each set of respondents represented b…` | "Where there is more than one" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 30(3) | `o 18 r 30(3) the security is provided for each set of respondents represented b…` | "represented by the same firm of solicitors" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 31(1) | `o 18 r 31(1) the appellate Court may give directions for the filing and service…` | "Where there are related appeals in the appellate Court" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 31(4) | `o 18 r 31(4) the appellate Court may direct any modifications of the rules that…` | "Where the related appeals comprise" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 33(3) | `o 18 r 33(3)(a) the lower Court must endeavour to issue the written grounds of …` | "certifies under paragraph (2)(b)" | a failed "if" read as the text's no |
| O 18 r 33(3) | `o 18 r 33(3)(b)(i) the appellant must apply in writing to the Registrar to proc…` | "if no written grounds of decision are issued within 12 weeks after the certification" | a failed "if" read as the text's no |
| O 18 r 33(3) | `o 18 r 33(3)(b)(ii) the respondent may apply in writing to the Registrar to pro…` | "if the appellant fails to do so" | a failed "if" read as the text's no |
| O 18 r 33(3) | `o 18 r 33(3)(b)(iii) the respondent may apply to strike out the appeal` | "after the expiry of the 14 days’ notice period" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 33(5) | `o 18 r 33(5) the written submissions are filed and served in time` | "within 14 days after" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 33(6) | `o 18 r 33(6) the written submissions are subject to a page limit of 35 pages` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 33(9) | `o 18 r 33(9) the parties must request in writing for a case conference before t…` | "Where the parties are unable to agree as mentioned in paragraph (8)" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 33(10) | `o 18 r 33(10) the parties must inform the Registrar in writing of the timelines…` | "Where the parties have agreed as mentioned in paragraph (8)" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 33(12) | `o 18 r 33(12) the appeal is deemed withdrawn` | "Where the appellant fails to file and serve the written submissions within the specified …" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 33(12) | `o 18 r 33(12) the appeal is deemed withdrawn` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 33(13) | `o 18 r 33(13) the security for costs must be paid and the solicitor's undertaki…` | "if all the parties to the appeal consent to the payment of the security for costs" | a failed "if" read as the text's no |
| O 18 r 33(13) | `o 18 r 33(13) the security for costs must be paid and the solicitor's undertaki…` | "must file the document signifying such consent signed by the parties and in such event" | an "in such event" that is not met, read as "in the event of" and so as "where" (assumed, not ruled: fork 15.7) |
| O 18 r 33(14) | `o 18 r 33(14)(a) the appellant or any party to the appeal may request in writin…` | "Where an appeal is deemed withdrawn pursuant to paragraph (12) and if there are any outst…" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 33(14) | `o 18 r 33(14)(a) the request is made in time` | "within 14 days after the date that the appeal is deemed withdrawn" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 33(14) | `o 18 r 33(14)(c) the Registrar may give directions on the making of written sub…` | "upon receiving a request under sub-paragraph (a)" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 33(16) | `o 18 r 33(16) the appellate Court may allow the page limit to be exceeded` | "upon the payment of the fees and additional fees prescribed for the filing of pages in ex…" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 33(17) | `o 18 r 33(17) the appellate Court may upon application waive, refund, defer or …` | "upon application" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 34(2) | `o 18 r 34(2) the security for costs must be paid to the respondent towards the …` | "Where costs are payable by the appellant to the respondent under any order made by the" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 34(3) | `o 18 r 34(3) the security for costs must be paid to the appellant` | "Where no costs are payable by the appellant to the respondent under any order made by the" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 34(3) | `o 18 r 34(3) the appellant's solicitor is released from any undertaking as to t…` | "Where no costs are payable by the appellant to the respondent under any order made by the" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 35(4) | `o 18 r 35(4) the affidavit in reply is filed and served in time` | "if the party wishes to file an affidavit in reply to the application" | a failed "if" read as the text's no |
| O 18 r 35(4) | `o 18 r 35(4) the affidavit in reply is filed and served in time` | "within 14 days after the date the application and the affidavit in support of the applica…" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 35(6) | `o 18 r 35(6) the applicants need to provide only one set of security` | "need to provide only one set of security" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 35(7) | `o 18 r 35(7) the applicant must provide security for each opposing party or eac…` | "Where there is more than one" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 35(7) | `o 18 r 35(7) the security is provided for each set of opposing parties represen…` | "Where there is more than one" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 35(7) | `o 18 r 35(7) the security is provided for each set of opposing parties represen…` | "represented by the same firm of solicitors" | a failed "where" read as no (ruling of 2026-11-05 (b)) |
| O 18 r 35(13) | `o 18 r 35(13) the summons and the supporting affidavit are filed and served in …` | "within 14 days after service of the notice of the appeal on the applicant" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 35(14) | `o 18 r 35(14) the affidavit in reply to the summons to strike out is filed and …` | "within 14 days after service of the applicant’s summons and affidavit on that party" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 36 | `o 18 r 36 the application for permission is filed and served in time` | "within 14 days after the date on which that direction or order is made" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 37(1) | `o 18 r 37(1) the written submissions and bundles of authorities are filed and s…` | "within 14 days after the date on which the opposing party’s affidavit in reply is to be f…" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 37(2) | `o 18 r 37(2) the written submissions are subject to a page limit of 35 pages` | "otherwise orders" | "unless ... otherwise" lifting a requirement or a deeming read as no (fork 18.1) |
| O 18 r 37(3) | `o 18 r 37(3) the appellate Court may allow the page limit to be exceeded` | "upon the payment of the fees and additional fees prescribed for the filing of pages in ex…" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 37(4) | `o 18 r 37(4) the appellate Court may upon application waive, refund, defer or a…` | "upon application" | a "when" or "upon" that is not met, read as "where" (ruling of 2026-11-05, delegated (c)) |
| O 18 r 39(2) | `o 18 r 39(2) the application to vary or discharge a direction or order of the R…` | "within 14 days after the date on which that direction or order is made" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 40(3) | `o 18 r 40(3) the application under section 29D(2)(c)(i) is filed and served in …` | "within 14 days after the date of service of the notice of appeal on all parties who have …" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 40(4) | `o 18 r 40(4) the application under section 29D(2)(c)(ii) is filed and served in…` | "no later than 14 days after the date on which the parties’ written submissions are requir…" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |
| O 18 r 41(2) | `o 18 r 41(2) the application under section 29E(2)(b) is made and served in time` | "within 14 days after the date of service of the notice of appeal on all parties who have …" | a period the text fixes in its own words, outside it read as no (ruling of 2026-11-05 (a)) |

### B. A grant or prohibition limited by its own wording, left at `NOTHING` (rule of 2026-10-29 (b))

Each branch answers `NOTHING` because the case falls outside the limit the text writes.
The other reading is `JUST FALSE`: what the text does not grant is not granted.

| provision | function | the words that limit it | NOTHING-kind |
| --- | --- | --- | --- |
| O 15 r 1(1) | `o 15 r 1(1) the matter must be heard in chambers` | "every originating application, summons, assessment of damages, taking of accounts and app…" | limited by its own wording |
| O 15 r 1(1) | `o 15 r 1(1) the matter must be heard in chambers` | "every originating application, summons, assessment of damages, taking of accounts and app…" | limited by its own wording |
| O 15 r 1(2) | `o 15 r 1(2) the matter must be heard in open court` | "All trials in originating claims must be heard in open court" | limited by its own wording |
| O 15 r 1(3) | `o 15 r 1(3) the matter must be heard in open court` | "Applications and appeals to the Appellate Division or Court of Appeal" | limited by its own wording |
| O 15 r 1(4) | `o 15 r 1(4) the Court may order the matter to be heard in the other way` | "any matter which is to be heard in chambers ... any matter which is to be heard in court" | limited by its own wording |
| O 15 r 1(5) | `o 15 r 1(5) the person may attend the hearing in chambers as of right` | "As a general rule, attendance in hearings in chambers is restricted to the parties (if th…" | limited by its own wording |
| O 15 r 1(6) | `o 15 r 1(6) the Court may allow the person to attend the hearing in chambers` | "subject to space, security and the interests of justice" | limited by its own wording |
| O 15 r 1(8) | `o 15 r 1(8) the person must comply with the practice directions and the Court's…` | "All persons in court or in chambers" | limited by its own wording |
| O 15 r 2(2) | `o 15 r 2(2) the Registrar of the Supreme Court may refer the matter to a Judge …` | "The Registrar of the Supreme Court may refer any matter" | limited by its own wording |
| O 15 r 2(2) | `o 15 r 2(2) the Judge to whom a matter is referred may hear it or send it back …` | "who may hear the matter referred to him or her or send it back to the Registrar with dire…" | limited by its own wording |
| O 15 r 2(3) | `o 15 r 2(3) paragraphs (1) and (2) apply to the Registrar of the State Courts` | "This Rule applies in relation to the jurisdiction of the Registrar of the State Courts" | limited by its own wording |
| O 15 r 3(4) | `o 15 r 3(4) the Court may direct that the matter be heard in an asynchronous ma…` | "in any matter that it may decide without hearing oral arguments" | limited by its own wording |
| O 15 r 4(1) | `o 15 r 4(1) the person may request the Registrar to issue an order to attend co…` | "The parties may request the Registrar" | limited by its own wording |
| O 15 r 4(4) | `o 15 r 4(4) the Registrar may revoke the order` | "revoke an order to attend court or an order to produce documents" | limited by its own wording |
| O 15 r 4(5) | `o 15 r 4(5) the party may apply to a Judge sitting in the General Division or a…` | "Any party who is dissatisfied with any decision of the Registrar made under this Rule" | limited by its own wording |
| O 15 r 4(8) | `o 15 r 4(8) the witness need not attend court personally` | "A witness served with an order to produce documents only" | limited by its own wording |
| O 15 r 4(9) | `o 15 r 4(9) the witness is entitled to claim reasonable compensation for time a…` | "A witness who complies with an order to attend court or an order to produce documents" | limited by its own wording |
| O 15 r 4(11) | `o 15 r 4(11) the order to attend court is to include the words of paragraph (11)` | "An order to attend court addressed to a person confined in prison" | limited by its own wording |
| O 15 r 4(12) | `o 15 r 4(12) the order to attend court may be served on the Superintendent of t…` | "The order to attend court in paragraph (11) may be served on the Superintendent of the pr…" | limited by its own wording |
| O 15 r 4(13) | `o 15 r 4(13) the witness must remain outside the courtroom` | "A witness, who is not a party, who has not given his or her evidence" | limited by its own wording |
| O 15 r 4(14) | `o 15 r 4(14) the witness may remain in or leave the courtroom` | "A witness who has given his or her evidence" | limited by its own wording |
| O 15 r 4(16) | `o 15 r 4(16) it is sufficient for the Registrar to produce a copy of the docume…` | "produce a copy of the document or the records requested" | limited by its own wording |
| O 15 r 6(1) | `o 15 r 6(1) the person may attend the hearing` | "Any person may attend a hearing in open court" | limited by its own wording |
| O 15 r 7(2) | `o 15 r 7(2) the Judge may hear the matter with the assistance of assessors` | "with the assistance of one or 2 assessors" | limited by its own wording |
| O 15 r 8(2) | `o 15 r 8(2) the Judge may hear the trial or part of it with the assistance of a…` | "with the assistance of one or 2 assessors" | limited by its own wording |
| O 15 r 8(5) | `o 15 r 8(5) the order of proceedings in paragraphs (6) to (13) applies` | "subject to such directions" | limited by its own wording |
| O 15 r 8(6) | `o 15 r 8(6) the opening statements and affidavits of evidence-in-chief must be …` | "The Court must have control over the order of proceedings and may give the appropriate di…" | limited by its own wording |
| O 15 r 8(8) | `o 15 r 8(8) the person may cross-examine the claimant and the claimant's witnes…` | "The defendant and any other parties may cross-examine the claimant and the claimant's wit…" | limited by its own wording |
| O 15 r 8(10) | `o 15 r 8(10) the person may cross-examine the defendant and the defendant's wit…` | "The claimant and any other parties may cross-examine the defendant and the defendant's wi…" | limited by its own wording |
| O 15 r 8(11) | `o 15 r 8(11) the defendant may make a submission of No case to answer` | "At the conclusion of the claimant's case" | limited by its own wording |
| O 15 r 8(11)(c) | `o 15 r 8(11)(c) the defendant who makes the submission may rely on the evidence…` | "if there is more than one defendant and not all the defendants make the submission of “No…" | limited by its own wording |
| O 15 r 8(11)(e) | `o 15 r 8(11)(e) the defendant who makes the submission may make submissions on …` | "and is unsuccessful may make submissions on the costs of the action" | limited by its own wording |
| O 15 r 8(12) | `o 15 r 8(12) the Court must hear the submissions of all the parties` | "At the conclusion of the evidence for all the parties" | limited by its own wording |
| O 15 r 9 | `o 15 r 9 the person must take an oath or make an affirmation according to the p…` | "before he or she gives evidence in Court" | limited by its own wording |
| O 15 r 10(1) | `o 15 r 10(1) the Court must allow the parties to ask the witness further questi…` | "further questions arising out of the Court's questions" | limited by its own wording |
| O 15 r 10(2) | `o 15 r 10(2) the Court may visit the place` | "visit any place that is relevant to the action" | limited by its own wording |
| O 15 r 11(1) | `o 15 r 11(1) the Court must maintain a record of the exhibit` | "any physical exhibit tendered in evidence and kept with the Court" | limited by its own wording |
| O 15 r 11(2) | `o 15 r 11(2) the Court may direct that the exhibit be kept in the custody of th…` | "any physical exhibit which is bulky, perishable or requires special security or treatment" | limited by its own wording |
| O 15 r 12(1)(a) | `o 15 r 12(1)(a) the Court may give its decision orally` | "orally at the conclusion of the hearing or on a subsequent date with the parties present" | limited by its own wording |
| O 15 r 12(1)(b) | `o 15 r 12(1)(b) the Court may give its decision in writing at the conclusion of…` | "in writing at the conclusion of the hearing or on a subsequent date with or without the p…" | limited by its own wording |
| O 15 r 12(2) | `o 15 r 12(2) the parties are entitled to a copy of the decision` | "a copy of the decision given in writing" | limited by its own wording |
| O 15 r 13(1) | `o 15 r 13(1) the Court may give its decision in the matter` | "any matter which has been heard but not decided yet although a party passes away" | limited by its own wording |
| O 15 r 13(2) | `o 15 r 13(2) the Court may substitute the person as a party and order that the …` | "any person who has taken over the interest or the liability of the deceased party" | limited by its own wording |
| O 15 r 14(2) | `o 15 r 14(2) the Judge or Registrar who takes over may recall any witness and o…` | "The Judge or Registrar who takes over the matter" | limited by its own wording |
| O 15 r 15(1) | `o 15 r 15(1) this Rule applies to the proceeding` | "This Rule applies to the assessment of damages and the taking of accounts" | limited by its own wording |
| O 15 r 15(1) | `o 15 r 15(1) the sum is within “damages” in this Rule` | "unless the context otherwise requires" | limited by its own wording |
| O 15 r 15(4) | `o 15 r 15(4) the provisions of Order 9, Rule 25(12) apply to the application fo…` | "the provisions of Order 9, Rule 25(12) apply to the application for directions" | limited by its own wording |
| O 15 r 15(4) | `o 15 r 15(4) the party must apply to the Court for directions` | "the party entitled to the benefit of the judgment" | limited by its own wording |
| O 15 r 15(5) | `o 15 r 15(5) the Court may give directions as to the time by which a notice of …` | "On the hearing of the application for directions mentioned in paragraph (4)" | limited by its own wording |
| O 15 r 15(8) | `o 15 r 15(8) the claim must be pleaded` | "A claim for provisional damages must be pleaded" | limited by its own wording |
| O 15 r 15(9) | `o 15 r 15(9) the award must specify the contingency and the period for applying…` | "An award for provisional damages" | limited by its own wording |
| O 15 r 15(15) | `o 15 r 15(15) the Court may order the damages to be paid in periodic instalment…` | "damages for personal injuries to be paid in periodic instalments instead of one amount" | limited by its own wording |
| O 15 r 15(16) | `o 15 r 15(16) the Court may be guided by actuarial tables and other guidelines …` | "The Court assessing damages for personal injuries" | limited by its own wording |
| O 15 r 16(1) | `o 15 r 16(1) the trial must be decided on the basis of the affidavits of eviden…` | "the trial in an originating claim, assessment of damages or value, and taking of accounts" | limited by its own wording |
| O 15 r 16(2) | `o 15 r 16(2) the Court may allow a witness' evidence-in-chief to be given orall…` | "In a special case" | limited by its own wording |
| O 15 r 16(3) | `o 15 r 16(3) the affidavit of evidence-in-chief may be used` | "unless the parties otherwise agree" | limited by its own wording |
| O 15 r 16(8) | `o 15 r 16(8) the notice must state the grounds in section 32 of the Evidence Ac…` | "The notice in paragraph (7)" | limited by its own wording |
| O 15 r 16(11) | `o 15 r 16(11) the Court may accept the matter as fact` | "anything that the parties have agreed upon" | limited by its own wording |
| O 15 r 19(2) | `o 15 r 19(2) the photograph is as the Rule requires` | "In the case of affidavits filed as evidence‑in‑chief in an originating claim" | limited by its own wording |
| O 15 r 22(1) | `o 15 r 22(1) the affidavit may be affirmed and signed, and the attestation comp…` | "an affidavit may be affirmed and signed in Singapore before, and the attestation complete…" | limited by its own wording |
| O 15 r 22(1) | `o 15 r 22(1) the affidavit may be affirmed and signed, and the attestation comp…` | "that is created using a remote communication technology that complies with the requiremen…" | limited by its own wording |
| O 15 r 22(2) | `o 15 r 22(2) the deponent and the commissioner for oaths may sign the affidavit…` | "may sign the affidavit electronically in accordance with any requirements laid down in an…" | limited by its own wording |
| O 15 r 23 | `o 15 r 23 an affidavit may be affirmed outside Singapore` | "An affidavit may be affirmed outside Singapore" | limited by its own wording |
| O 15 r 26(1) | `o 15 r 26(1) the affidavit may be altered` | "after it has been affirmed but not filed in Court" | limited by its own wording |
| O 15 r 26(2) | `o 15 r 26(2) the maker may correct any mistakes in the affidavit by making anot…` | "A maker of an affidavit which has been filed in Court" | limited by its own wording |
| O 15 r 27(5) | `o 15 r 27(5) the annexure must be identified by a certificate of the commission…` | "All annexures to an affidavit" | limited by its own wording |
| O 15 r 28 | `o 15 r 28 the seal or signature of the commissioner for oaths must be accepted …` | "The seal or signature of a commissioner for oaths in an affidavit affirmed in or outside …" | limited by its own wording |
| O 15 r 29 | `o 15 r 29 the party must give notice of the intention to use the affidavit and …` | "A party who intends to use in any proceedings any affidavit filed in previous proceedings" | limited by its own wording |
| O 16 r 1 | `o 16 r 1 the party may withdraw the notice of intention to contest or not conte…` | "with the permission of the Court" | limited by its own wording |
| O 16 r 1 | `o 16 r 1 the party may withdraw the notice of intention to contest or not conte…` | "A party who has filed a notice of intention to contest or not contest" | limited by its own wording |
| O 16 r 2(1) | `o 16 r 2(1) the claimant may discontinue the action or withdraw a claim without…` | "by serving a notice in Form 32 to that effect on the defendant concerned" | limited by its own wording |
| O 16 r 2(1) | `o 16 r 2(1) the claimant may discontinue the action or withdraw a claim without…` | "The claimant in an action begun by originating claim" | limited by its own wording |
| O 16 r 2(2)(a) | `o 16 r 2(2)(a) the defendant may withdraw the defence or any part of it without…` | "by serving a notice in Form 32 to that effect on the claimant or other party concerned" | limited by its own wording |
| O 16 r 2(2)(a) | `o 16 r 2(2)(a) the defendant may withdraw the defence or any part of it without…` | "withdraw the defendant's defence or any part of it" | limited by its own wording |
| O 16 r 2(2)(b) | `o 16 r 2(2)(b) the defendant may discontinue the counterclaim or withdraw a cla…` | "by serving a notice in Form 32 to that effect on the claimant or other party concerned" | limited by its own wording |
| O 16 r 2(2)(b) | `o 16 r 2(2)(b) the defendant may discontinue the counterclaim or withdraw a cla…` | "discontinue a counterclaim" | limited by its own wording |
| O 16 r 2(5) | `o 16 r 2(5) the action may be withdrawn without the permission of the Court on …` | "by producing to the Registrar a written consent to the action being withdrawn signed by a…" | limited by its own wording |
| O 16 r 2(6) | `o 16 r 2(6) the action is deemed to have been discontinued against the defendant` | "An action begun by originating claim" | limited by its own wording |
| O 16 r 2(10) | `o 16 r 2(10) the Court may reinstate the action, cause or matter and allow it t…` | "on application" | limited by its own wording |
| O 16 r 3(1) | `o 16 r 3(1) a party may discontinue the action or counterclaim or withdraw a cl…` | "Except as provided by Rule 2" | limited by its own wording |
| O 16 r 3(1) | `o 16 r 3(1) the Court hearing the application may order the discontinuance or s…` | "the Court hearing an application for the grant of such permission may order" | limited by its own wording |
| O 16 r 3(2) | `o 16 r 3(2) the application for permission may be made by summons` | "may be made by summons" | limited by its own wording |
| O 16 r 4 | `o 16 r 4 the discontinuance is a defence to a subsequent action for the same ca…` | "Subject to any terms imposed by the Court in granting permission under Rule 3" | limited by its own wording |
| O 16 r 6 | `o 16 r 6 the party may withdraw the summons` | "may not withdraw it without the permission of the Court" | limited by its own wording |
| O 16 r 6 | `o 16 r 6 the party may withdraw the summons` | "A party who has taken out a summons in a cause or matter" | limited by its own wording |
| O 17 r 3(3) | `o 17 r 3(3) the party must draw up the order` | "The party who takes out an application" | limited by its own wording |
| O 17 r 3(5) | `o 17 r 3(5) another party affected by the order may draw it up` | "any other party affected by the order" | limited by its own wording |
| O 17 r 3(8) | `o 17 r 3(8) the Court may decide the dispute without the attendance of the part…` | "its decision on the dispute on the terms of the draft" | limited by its own wording |
| O 17 r 4(2) | `o 17 r 4(2) the Court may prohibit the person from inspecting or taking copies …` | "any person, other than the parties" | limited by its own wording |
| O 17 r 5(3) | `o 17 r 5(3) the simple interest on an instalment from the date it is due until …` | "Where instalment payments are allowed by the Court" | limited by its own wording |
| O 18 r 1(2) | `o 18 r 1(2) the application is an application in an action` | "(except an application mentioned in paragraph (1)(a)(iv a))" | limited by its own wording |
| O 18 r 3(1) | `o 18 r 3(1) the time for filing an appeal or an application for permission to a…` | "unless the Court otherwise orders" | limited by its own wording |
| O 18 r 3(1) | `o 18 r 3(1) the time for filing an appeal or an application for permission to a…` | "does not start to run until after the lower Court has heard and determined all matters in…" | limited by its own wording |
| O 18 r 3(1A) | `o 18 r 3(1A) the date after which the time starts to run where costs are not de…` | "Where the lower Court does not hear and determine the issue of costs within 30 days" | limited by its own wording |
| O 18 r 3(2)(b) | `o 18 r 3(2)(b) the time does not run until all the matters have been heard and …` | "subject to sub‑paragraph ( c )" | limited by its own wording |
| O 18 r 3(2)(b) | `o 18 r 3(2)(b) the time does not run until all the matters have been heard and …` | "in the case of a single application pending trial dealing with more than one matter" | limited by its own wording |
| O 18 r 3(2)(b) | `o 18 r 3(2)(b) the time is still barred from running because not all the matter…` | "subject to sub‑paragraph ( c )" | limited by its own wording |
| O 18 r 3(2)(b) | `o 18 r 3(2)(b) the time is still barred from running because not all the matter…` | "in the case of a single application pending trial dealing with more than one matter" | limited by its own wording |
| O 18 r 3(2)(c)(i) | `o 18 r 3(2)(c)(i) the date after which the time runs for the appeal against the…` | "where one or more matters ... are to be heard before the Registrar and one or more other …" | limited by its own wording |
| O 18 r 3(2)(c)(ii) | `o 18 r 3(2)(c)(ii) the date after which the time runs for an appeal or an appli…` | "where one or more matters ... are to be heard before the Registrar and one or more other …" | limited by its own wording |
| O 18 r 3(2)(d) | `o 18 r 3(2)(d) the date after which the time runs for the appeal or the applica…` | "in the case of a single application pending trial dealing with more than one matter, wher…" | limited by its own wording |
| O 18 r 4(1) | `o 18 r 4(1) the party may file another appeal for the application` | "Subject to paragraph (2)" | limited by its own wording |
| O 18 r 4(1) | `o 18 r 4(1) the party may file another appeal for the application` | "unless the Court otherwise orders" | limited by its own wording |
| O 18 r 5(1) | `o 18 r 5(1) the person may apply to intervene in the appeal` | "A person who is not a party in the appeal" | limited by its own wording |
| O 18 r 5(2) | `o 18 r 5(2) the application for permission to intervene and the supporting affi…` | "The application for permission to intervene and the supporting affidavit" | limited by its own wording |
| O 18 r 6(1) | `o 18 r 6(1) the appeal operates as a stay of enforcement or of proceedings unde…` | "Except so far as the lower Court or the appellate Court may otherwise direct" | limited by its own wording |
| O 18 r 6(2) | `o 18 r 6(2) an intermediate act or proceeding is invalidated by the appeal` | "Except so far as the appellate Court may otherwise direct" | limited by its own wording |
| O 18 r 6(3) | `o 18 r 6(3) interest is to be allowed for the time enforcement has been delayed…` | "interest for such time as enforcement has been delayed by the appeal" | limited by its own wording |
| O 18 r 7 | `o 18 r 7 the appeal must be heard in chambers` | "Subject to Order 15, Rule 1(3)" | limited by its own wording |
| O 18 r 8(1) | `o 18 r 8(1) the appellate Court may order any party to serve any document on th…` | "any document on a non‑party to the appeal" | limited by its own wording |
| O 18 r 8(2) | `o 18 r 8(2) the appellate Court may allow or invite the non-party to give its v…` | "any non‑party to the appeal" | limited by its own wording |
| O 18 r 8(5) | `o 18 r 8(5) the appellate Court's powers to decide the merits of the appeal are…` | "by reason only that there was no appeal against any previous order" | limited by its own wording |
| O 18 r 8(7) | `o 18 r 8(7) the further evidence must be adduced in the manner directed by the …` | "Such further evidence" | limited by its own wording |
| O 18 r 10 | `o 18 r 10 the appellate Court may intervene` | "In procedural matters" | limited by its own wording |
| O 18 r 11(2) | `o 18 r 11(2) the lower Court or the appellate Court may dispense with complianc…` | "In an expedited appeal" | limited by its own wording |
| O 18 r 12(1) | `o 18 r 12(1) the appellant may withdraw the appeal or the applicant may withdra…` | "by filing and serving a notice of withdrawal of the appeal or application in Form 34 on a…" | limited by its own wording |
| O 18 r 12(3)(b) | `o 18 r 12(3)(b) oral arguments may be made in the request` | "unless the appellate Court otherwise directs" | limited by its own wording |
| O 18 r 12(4) | `o 18 r 12(4) the appeal or application remains on the list` | "Except as provided under paragraph (3)" | limited by its own wording |
| O 18 r 14(3) | `o 18 r 14(3) the party is entitled to a copy of the decision` | "any decision given in writing" | limited by its own wording |
| O 18 r 14(4) | `o 18 r 14(4) the judgment of the appellate Court may be delivered orally by the…` | "any Judge sitting in the appellate Court" | limited by its own wording |
| O 18 r 15 | `o 18 r 15 the notice of appeal in Form 35 is filed and served in time` | "A party who intends to appeal to a District Judge against a decision of the Registrar of …" | limited by its own wording |
| O 18 r 16(7) | `o 18 r 16(7) a document other than those set out in the Rule may be filed` | "otherwise orders" | limited by its own wording |
| O 18 r 16(8) | `o 18 r 16(8) the appellate Court may allow the page limit to be exceeded` | "in special circumstances" | limited by its own wording |
| O 18 r 16(10) | `o 18 r 16(10) the party may file more than one set of submissions` | "for each party or set of parties represented by the same firm of solicitors" | limited by its own wording |
| O 18 r 17(1) | `o 18 r 17(1) the notice of appeal in Form 35 is filed and served in time` | "A party who intends to appeal to the General Division against the decision of a District …" | limited by its own wording |
| O 18 r 17(2) | `o 18 r 17(2) the General Division may extend the time for filing and serving th…` | "on the appellant’s application made at any time" | limited by its own wording |
| O 18 r 18(1) | `o 18 r 18(1) the request for further arguments is made as the Rule requires` | "A request to the District Judge or Magistrate for further arguments from the parties afte…" | limited by its own wording |
| O 18 r 19(4) | `o 18 r 19(4) the General Division may extend the time for filing and serving an…` | "for filing and serving an application for permission to appeal made at any time" | limited by its own wording |
| O 18 r 21(7) | `o 18 r 21(7) the party is required to file separate written submissions` | "A party whose interest in the appeal is passive" | limited by its own wording |
| O 18 r 21(8) | `o 18 r 21(8) the parties must try to agree on filing a single set of written su…` | "All parties to 2 or more related appeals" | limited by its own wording |
| O 18 r 21(11) | `o 18 r 21(11) a document other than those set out in the Rule may be filed` | "otherwise orders" | limited by its own wording |
| O 18 r 21(14) | `o 18 r 21(14)(b) oral arguments may be made in the request` | "unless the appellate Court otherwise directs" | limited by its own wording |
| O 18 r 21(15) | `o 18 r 21(15) the respondent is allowed to make submissions at the hearing of t…` | "Where the respondent to the appeal fails to file and serve the written submissions for th…" | limited by its own wording |
| O 18 r 21(15) | `o 18 r 21(15) the respondent is allowed to make submissions at the hearing of t…` | "unless the appellate Court otherwise orders" | limited by its own wording |
| O 18 r 21(16) | `o 18 r 21(16) the appellate Court may allow the page limit to be exceeded` | "in special circumstances" | limited by its own wording |
| O 18 r 21(18) | `o 18 r 21(18) the party may file more than one set of submissions` | "for each party or set of parties represented by the same firm of solicitors" | limited by its own wording |
| O 18 r 23 | `o 18 r 23 the step for enforcement is taken as the Rule requires` | "a judgment or order which has been the subject matter of an appeal under this Division" | limited by its own wording |
| O 18 r 24 | `o 18 r 24 the notice of appeal in Form 35 is filed and served in time` | "A party who intends to appeal to a Judge in Chambers against a decision of the Registrar …" | limited by its own wording |
| O 18 r 25(7) | `o 18 r 25(7) a document other than those set out in the Rule may be filed` | "otherwise orders" | limited by its own wording |
| O 18 r 25(8) | `o 18 r 25(8) the Judge may allow the page limit to be exceeded` | "in special circumstances" | limited by its own wording |
| O 18 r 25(10) | `o 18 r 25(10) the party may file more than one set of submissions` | "for each party or set of parties represented by the same firm of solicitors" | limited by its own wording |
| O 18 r 27(1) | `o 18 r 27(1) the notice of appeal in Form 35 is filed and served in time` | "A party who intends to appeal to the appellate Court against the decision of the lower Co…" | limited by its own wording |
| O 18 r 27(2) | `o 18 r 27(2) the appellate Court may extend the time for filing and serving the…` | "on the appellant’s application made at any time" | limited by its own wording |
| O 18 r 28(1) | `o 18 r 28(1) the request for further arguments is made as the Rule requires` | "A request under section 29B(2) of the Supreme Court of Judicature Act 1969 to the Judge s…" | limited by its own wording |
| O 18 r 29(3)(a) | `o 18 r 29(3)(a) an application for permission to appeal against the decision ma…` | "If a request for further arguments in respect of a decision has been made under paragraph…" | limited by its own wording |
| O 18 r 29(3)(a) | `o 18 r 29(3)(a) an application for permission to appeal against the decision ma…` | "until the Judge" | limited by its own wording |
| O 18 r 29(7)(a) | `o 18 r 29(7)(a) the written submissions and any bundle of authorities are filed…` | "A party applying for permission under this Rule" | limited by its own wording |
| O 18 r 29(7)(b) | `o 18 r 29(7)(b) the party may file a bundle of documents with the application` | "a bundle of documents that are relevant to the application and that were filed in the pro…" | limited by its own wording |
| O 18 r 29(8) | `o 18 r 29(8) the opposing party's written submissions are filed and served in t…` | "A party who wishes to oppose an application for permission under this Rule" | limited by its own wording |
| O 18 r 29(12) | `o 18 r 29(12) the appellate Court may allow the page limit to be exceeded` | "in special circumstances" | limited by its own wording |
| O 18 r 29(14) | `o 18 r 29(14) the party may file more than one set of submissions` | "unless the appellate Court otherwise orders" | limited by its own wording |
| O 18 r 29(14) | `o 18 r 29(14) the party may file more than one set of submissions` | "for each party or set of parties represented by the same firm of solicitors" | limited by its own wording |
| O 18 r 29(15) | `o 18 r 29(15) an affidavit may be filed in the application for permission to ap…` | "without the permission of the appellate Court" | limited by its own wording |
| O 18 r 29(16) | `o 18 r 29(16) oral arguments may be made in the application for permission to a…` | "unless the appellate Court otherwise orders" | limited by its own wording |
| O 18 r 33(7) | `o 18 r 33(7) the party is required to file separate written submissions` | "A party whose interest in the appeal is passive" | limited by its own wording |
| O 18 r 33(8) | `o 18 r 33(8) the parties must try to agree on filing a single set of written su…` | "All parties to 2 or more related appeals" | limited by its own wording |
| O 18 r 33(11) | `o 18 r 33(11) a document other than those set out in the Rule may be filed` | "otherwise orders" | limited by its own wording |
| O 18 r 33(14) | `o 18 r 33(14)(b) oral arguments may be made in the request` | "unless the appellate Court otherwise directs" | limited by its own wording |
| O 18 r 33(15) | `o 18 r 33(15) the respondent is allowed to make submissions at the hearing of t…` | "Where the respondent to the appeal fails to file and serve the written submissions for th…" | limited by its own wording |
| O 18 r 33(15) | `o 18 r 33(15) the respondent is allowed to make submissions at the hearing of t…` | "unless the appellate Court otherwise orders" | limited by its own wording |
| O 18 r 33(16) | `o 18 r 33(16) the appellate Court may allow the page limit to be exceeded` | "in special circumstances" | limited by its own wording |
| O 18 r 33(18) | `o 18 r 33(18) the party may file more than one set of submissions` | "for each party or set of parties represented by the same firm of solicitors" | limited by its own wording |
| O 18 r 34(4) | `o 18 r 34(4) paragraphs (2) and (3) apply to the payment out of security for co…` | "the payment out of security for costs given under Rule 35(5)" | limited by its own wording |
| O 18 r 35(2) | `o 18 r 35(2) the application may be made in the first instance to the appellate…` | "Whenever under these Rules an application may be made either to the lower Court or to the…" | limited by its own wording |
| O 18 r 35(2) | `o 18 r 35(2) the application may be made in the first instance to the appellate…` | "except where there are special circumstances which make it impossible or impracticable to…" | limited by its own wording |
| O 18 r 35(3) | `o 18 r 35(3) oral arguments may be made in an application to the appellate Court` | "unless the appellate Court otherwise orders" | limited by its own wording |
| O 18 r 35(4) | `o 18 r 35(4) the affidavit in reply is filed and served in time` | "Except where Rule 29(15) provides otherwise" | limited by its own wording |
| O 18 r 35(4) | `o 18 r 35(4) a further affidavit may be filed` | "without permission of the appellate Court" | limited by its own wording |
| O 18 r 35(12) | `o 18 r 35(12) the application to strike out a notice of appeal is made as the R…` | "Any application to the appellate Court to strike out a notice of appeal" | limited by its own wording |
| O 18 r 35(14) | `o 18 r 35(14) the affidavit in reply to the summons to strike out is filed and …` | "A party to the application mentioned in paragraph (12), who wishes to reply to the applic…" | limited by its own wording |
| O 18 r 35(15) | `o 18 r 35(15) a further affidavit may be received in evidence` | "without the permission of the appellate Court" | limited by its own wording |
| O 18 r 36 | `o 18 r 36 the application for permission is filed and served in time` | "An application for the permission of" | limited by its own wording |
| O 18 r 37(1) | `o 18 r 37(1) the written submissions and bundles of authorities are filed and s…` | "Except where otherwise provided by any provision of these Rules or any other written law" | limited by its own wording |
| O 18 r 37(1) | `o 18 r 37(1) the written submissions and bundles of authorities are filed and s…` | "unless the appellate Court otherwise directs" | limited by its own wording |
| O 18 r 37(3) | `o 18 r 37(3) the appellate Court may allow the page limit to be exceeded` | "in special circumstances" | limited by its own wording |
| O 18 r 37(5) | `o 18 r 37(5) the party may file more than one set of submissions` | "unless the appellate Court otherwise orders" | limited by its own wording |
| O 18 r 37(5) | `o 18 r 37(5) the party may file more than one set of submissions` | "for each party or set of parties represented by the same firm of solicitors" | limited by its own wording |
| O 18 r 38 | `o 18 r 38 further arguments from the parties are allowed` | "Unless the appellate Court otherwise directs" | limited by its own wording |
| O 18 r 38 | `o 18 r 38 further arguments from the parties are allowed` | "after the appellate Court has heard the appeal and reserved its decision or after the app…" | limited by its own wording |
| O 18 r 39(1) | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division an…` | "and all of the parties consent to the making of the direction or order" | limited by its own wording |
| O 18 r 39(1) | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division an…` | "and all of the parties consent to the making of the direction or order" | limited by its own wording |
| O 18 r 39(1) | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division an…` | "and all of the parties consent to the making of the direction or order" | limited by its own wording |
| O 18 r 39(1) | `o 18 r 39(1) the Registrar may exercise the powers of the Appellate Division an…` | "in the following circumstances" | limited by its own wording |
| O 18 r 39(2) | `o 18 r 39(2) the application to vary or discharge a direction or order of the R…` | "An application to vary or discharge any direction or order of the Registrar under paragra…" | limited by its own wording |
| O 18 r 39(2) | `o 18 r 39(2) the decision of that Judge is final` | "the decision of that Judge is final" | limited by its own wording |
| O 18 r 40(1) | `o 18 r 40(1) the Court of Appeal may exercise its power under section 29D(1)(a)…` | "on an application to the Court of Appeal to transfer an appeal that has been made to the …" | limited by its own wording |
| O 18 r 40(2) | `o 18 r 40(2) the Court of Appeal may exercise its power under section 29D(1)(a)…` | "on its own motion or on a reference by the Appellate Division" | limited by its own wording |
| O 18 r 40(3) | `o 18 r 40(3) the application under section 29D(2)(c)(i) is filed and served in …` | "An application under section 29D(2)( c )(i) of the Supreme Court of Judicature Act" | limited by its own wording |
| O 18 r 40(4) | `o 18 r 40(4) the application under section 29D(2)(c)(ii) is filed and served in…` | "An application under section 29D(2)( c )(ii) of the Supreme Court of Judicature Act" | limited by its own wording |
| O 18 r 41(2) | `o 18 r 41(2) the application under section 29E(2)(b) is made and served in time` | "An application under section 29E(2)( b ) of the Supreme Court of Judicature Act" | limited by its own wording |

### Reading a result: FALSE and NOTHING (roc3)

A decision function of this row answers `JUST TRUE`, `JUST FALSE` or `NOTHING`.
**`JUST FALSE` is the Rules' own no.**
It is a flat negative ("may not", "is not to", "does not operate as a stay"), a closed definition ("means", "only"), a condition the Rules state and the facts do not meet ("if", "where", "when", "upon", "in such event", "unless"), a period the Rules fix in their own words and the act missed ("within 14 days after"), or a bar's own yes/no question once the event has happened ("is still barred from starting to run").
It does not mean the act is invalid or the party loses; it means the Rules say no to that case in their own words.
**`NOTHING` is "the Rules do not answer on these facts".**
It is returned where the Rules list without closing the list ("includes", "such as", "any other relevant matter"), say nothing about the case, limit a grant in their own wording (a scope such as "a party who intends to appeal", a manner such as "by serving a notice in Form 32", an occasion such as "at the conclusion of the claimant's case"), lift a prohibition with an "unless" or an "except where" (a lifted bar does not permit), or point outside the sources (a written law, a practice direction, the Supreme Court of Judicature Act).
A caller must never read `NOTHING` as no.
In a procedural setting the commonest `NOTHING` is a deadline question asked of a party the Rule does not address (for example a respondent asked about the appellant's deadline), or an act whose manner the Rule leaves to a practice direction.

## Seams (roc3)

Each seam input taken, as PLAN.md names it, and the functions that take it.

| seam | input | taken by |
| --- | --- | --- |
| S-T1 | `o 3 r 3 the last day for doing the act` (`DATE`) | every timeliness function (`... is filed and served in time`, `... is made in time`); the seat asks it as "the last day for doing this, counted under Order 3, rule 3" |
| S-T2, S-F1, S-F2, S-S1, S-S2 | not threaded | the date an act was done is a plain date input; the moment of deemed filing or service (O 28, O 7) is the person's or their solicitor's to state |
| S-L1 | O 9 r 25(12) (roc2): `the application is the application for directions mentioned in paragraph (4)` | `o 15 r 15(4) the provisions of Order 9, Rule 25(12) apply to the application for directions` |
| the reverse seam (PLAN.md 5.2) | O 18 r 29(7) exposed for O 1 r 2(4)(c) | `o 18 r 29(7) the documents mentioned in paragraph (7) are filed with the application` (`MAYBE BOOLEAN`); the lead wires it to the keel's input `o 18 r 29(7) or o 19 r 26(7) the documents mentioned are filed and served with it` together with roc4's O 19 r 26(7) |
| Order 19 | O 18 r 1(2)(b)(ii), r 26(d), r 31(3) and (4), r 32(1)(b) | each speaks of Order 19; an input says whether the matter is within it, and the encoding states only what Order 18 says about it |
| Supreme Court of Judicature Act | ss 29B(2) and (4)(b), 29C, 29D, 29E, 40(4), 47(1), 58(4), the Sixth Schedule | inputs: `a request for further arguments has been made under section 29B(2)`, `the date mentioned in section 29B(4)(b)`, `permission to appeal under section 47(1) is required`, `the request is made within the time provided in section 29B(2)` (answers `NOTHING` when not met: the time is set outside the sources), the grounds of O 18 r 40(2) |
| Evidence Act | s 32 | O 15 r 16(8): `the notice must state the grounds in section 32 of the Evidence Act that the party relies on` takes the fact as an input |
| Prisons Act | the Superintendent's duty to produce the named person in court | O 15 r 4(11): the content of the order is encoded, the Superintendent's duty under the Prisons Act is outside the sources |
| Hague Evidence Convention | defined by O 15 r 5(9) itself; the instrument and its Model Forms are outside | `o 15 r 5(9) an instrument is the Hague Evidence Convention` and the three other defined-term functions |
| practice directions and Forms | Forms 18, 29, 30, 31, 32, 34, 35, 36, 37, 33 and the form specified in practice directions | the Form number is written in the input's name (`the affidavit is in Form 31`); what a Form contains is not encoded (reason 1 for a form that is only a form) |
| Order 1, rule 3(1) | "the Court", "the Registrar", "Appellate Division" and the other defined words | inputs named for the person ("the party attends in person"); the keel's functions are not called from these modules |

**Seam S-T1: this part computes none of its deadlines.**
Every deadline function takes `o 3 r 3 the last day for doing the act` as an input, counted by the caller under O 3 r 3 (roc1), and compares the date of the act with it; nothing in this part adds days, weeks, months or years to a date.
48 functions take it (rule, with the number of functions in brackets): Order 15: r 4 (3), r 11 (1), r 15 (2), r 16 (1); Order 16: r 2 (4); Order 17: r 3 (3); Order 18: r 9 (1), r 15 (1), r 16 (2), r 17 (1), r 18 (1), r 19 (3), r 21 (3), r 24 (1), r 25 (2), r 27 (1), r 28 (1), r 29 (5), r 33 (3), r 35 (3), r 36 (1), r 37 (1), r 39 (1), r 40 (2), r 41 (1).
The lengths the text states are written down as 58 `Period` constants (43 of 14 days after an event, 4 of 12 weeks after an event, 4 of 28 days after an event, 2 of 28 days before a hearing, 1 of 14 days before a hearing, 1 of 60 months after an event, 1 of 1 month after an event, 1 of 2 days after an event, 1 of 30 days after an event), but no function reads them, and the 12 months and the one year of O 16 r 2(6) and (7), the 28 days before a hearing (O 15 r 4(3), r 16(6)), the one calendar month of O 15 r 15(4) and the five years of O 15 r 11(11) are likewise the caller's last day.
The keel designed this seam (S-T1) and nothing was changed; the merge can decide whether to wire the constants to a counting function.

**Note for the merge: where is "the duty does not arise" answered?**
In this part it is answered by the function that states the duty, not by the compliance function and not by a companion.
A `must` function says whether the duty applies: `JUST TRUE` when the Rule's trigger holds and `JUST FALSE` when its "if", "where", "when" or "upon" is not met (for example `o 15 r 27(1) a copy of the document must be annexed to the affidavit`, `o 15 r 5(8) the party obtaining the order must also file an undertaking in Form 18`, `o 18 r 12(2) the security for costs must be paid and the solicitor's undertaking is discharged`).
The compliance function (`... is filed and served in time`) is asked of a party the duty reaches, and answers `NOTHING` for a party it does not reach ("A party who intends to ...").
No function answers `JUST TRUE` for "there was no duty, so nothing to comply with".
7 compliance functions carry a trigger of their own and answer `JUST FALSE` when it is not met; read that as "this Rule requires nothing here", not as late: `o 18 r 19(1) the application for permission to the District Judge or M`; `o 18 r 19(2) the application for permission to the General Division is`; `o 18 r 19(3) the notice of appeal in Form 35 is filed and served in ti`; `o 18 r 29(1) the application for permission to the appellate Court is `; `o 18 r 29(3)(b) the application for permission and the paragraph (7) d`; `o 18 r 29(17) the notice of appeal in Form 35 is filed and served in t`; `o 18 r 35(4) the affidavit in reply is filed and served in time`.
The merge can wire a companion or read `JUST TRUE` for "no duty" through the compliance function; this part does neither.

**Period audit (2026-11-05).**
Checked every function that tests a time against a period, deadline or window the text states in its own words ("within", "not later than", "before", "after", "at least N days before", "until", "for N years"): 88 yes/no functions, 65 that compare a date with `o 3 r 3 the last day for doing the act` or carry the period in their FALSE-kind comment, and 23 that take the period as a yes/no fact ("filed and served in time", "the 14 days' notice period has expired", "made before the one year elapsed").
(a) 87 answer `JUST TRUE` inside the period and `JUST FALSE` outside it, and the tests assert both sides of each: checked, no change.
(b) 0 answered `NOTHING` outside a period the text fixes and were changed.
One of the 88 stays `NOTHING` outside: `o 18 r 28(2)` ("within the time provided in section 29B(2) of the Supreme Court of Judicature Act"), because that Act is not among the sources and the text does not fix the period (fork 15.7 (xi)).
The date-returning functions (for example `o 18 r 27(1) the date after which the 14 days for the notice of appeal run`) are not counted, because a date cannot be a `JUST FALSE`.
The script is `work/period_audit.py`; it is not shipped.

Seams the plan lacks: none found.
One seam the text makes awkward: O 18 r 21(12), (15), r 33(12) say "within the specified time", meaning the time set by paragraph (5) of the same rule; the functions take the fact (`the appellant fails to file and serve the written submissions within the specified time`) and the caller decides it with `o 18 r 21(5) the written submissions are filed and served in time`.

## Dependencies (roc3)

Nothing was copied and nothing is imported from `inputs/DEPENDENCIES/`.
Order 3, rule 3(1) says "The Interpretation Act does not apply to the calculation of time in these Rules", so the staged Interpretation Act module (`sgia-interpretation-time.l4`) does not govern the periods of Orders 15 to 18; they are counted by Order 3, rule 3 (roc1), which this part takes as the input `o 3 r 3 the last day for doing the act`.
No other Act that Commons encodes is cited in these ranges.

## Unstable dialect (roc3)

Looked at time (deadlines counted from events, periods counted backward from a hearing), rule versions and workarounds in lines 1405-2230 and found no shape that earns a second encoding: every deadline is a plain `DATE` comparison against one seam input, and the rules in this range have no versions in force on different dates (the `[S 37/2024 wef 01/02/2024]` amendments are in force for the whole current text).
One workaround is worth knowing: the core `Time unit` has no `Years`, so "5 years" in O 15 r 11(11) is written as 60 months (NEEDS-CORE.md).
A second, unstable encoding of these provisions does not exist.

## Seat (roc3)

`roc3-seat.l4` has 58 questions, each beginning "Under Order N, rule M," with the Rules' own numbering, grouped under `§` headings by Order and `§§` headings by rule in the text's order.
Each takes plain inputs (yes/no, a date, a number, or a choice from a list), one per fact the person can state, with an `@desc` worded as the person would be asked; a fact that may not have happened yet is asked as a yes/no and a date, and reaches the rule as a `MAYBE DATE`.
Each question calls one layer-1 rule and restates nothing.
There is no seat for an official: the Registrar's, District Judge's and Magistrate's duties (certifying grounds of decision, informing a requesting party) are in layer 1 and the person meets them through the questions on their own deadlines.
`roc3-cases-seat.l4` has 149 assertions: up to three cases per question (taken from the hand-written layer-1 tests so that each distinct answer appears), the situations of real people (a claimant discontinuing in time, one day late and without a notice; an appellant one day late and on time; an appellant whose appeal is deemed withdrawn, with and without a Court order; a defendant who will give evidence, one who keeps a related counterclaim and one who may make a submission of No case to answer; an appellant and an applicant providing the right and the wrong security), and a case outside the encoding (a matter of a kind the Rules do not list among those heard in chambers answers `NOTHING`).
**Added in the second round:** the questions of O 15 r 8(11) (no case to answer), O 16 r 2(7) (the action deemed discontinued after a year without a step), O 18 r 20(5) (the amount of security on an appeal to the General Division) and O 18 r 35(9) (the amount of security on an application); the question of O 18 r 3(1) now asks whether the time is "still held back from starting to run", the bar's own question (fork 18.6), because the question "has the time started to run" answers `NOTHING` after the bar lifts.
The security amount of O 18 r 30(5), $15,000, was asked in the first round.

## Findings: what the text turns out to say (roc3)

1. **The four "documents to be filed" rules of Order 18 (rules 16, 21, 25, 33) are one rule in four dresses.**
   Rules 16 and 25 have paragraphs (1) to (10); rules 21 and 33 add (7) to (10) and (12) to (15) (passive parties, related appeals, the deemed withdrawal, the respondent's silence) and renumber the rest.
   The decision-maker differs (the Registrar, the District Judge or Magistrate, the lower Court) and rule 25 says "the Judge" where the others say "the appellate Court".
2. **Time is counted forward and backward, and only forward fits a `WITHIN`.**
   Most periods run "after" an event; three run "before" a hearing (O 15 r 4(3), r 4(12) and r 16(6): the constants `o 15 r 4(3) the period before the hearing for serving the order`, `o 15 r 4(12) the period before the hearing for serving the order on the Superintendent` and `o 15 r 16(6) the period before the first date of the hearing for the notice of objection`).
   The regulative rules cover the forward periods; the backward ones are decided by the decision functions and the seam input.
3. **Several consequences are deemings, not duties.**
   Silence by the other solicitors is deemed consent (O 17 r 3(6)); no certificate within 14 days is presumed to mean no further written grounds (O 18 r 16(2), 21(2), 25(2), 33(2)); no written submissions is a deemed withdrawal (r 21(12), 33(12)); no word from the Registrar of the State Courts or of the Supreme Court within 14 days is a deemed "no further arguments" (r 18(5), 28(5)).
   Each is a decision function whose input is the failure.
4. **The text never says what the Registrar's failure to issue written grounds within 12 weeks costs the Registrar.**
   It says what the appellant, then the respondent, must or may do (r 16(3)(b), 21(3)(b), 25(3)(b), 33(3)(b)); nothing is encoded for the Registrar's side beyond "must endeavour to do so as soon as it is practicable".
5. **Security for costs has amounts only for two kinds of action in rule 20 ($3,000 for a Magistrate's Court action, $5,000 for a District Court action); any other action answers `NOTHING`.**
   Rule 30 fixes $15,000 and rule 35(9) fixes $5,000.
6. **Rule 29(7) is asked by Order 1.**
   Order 1, rule 2(4)(c) points at "the documents mentioned" in O 18 r 29(7) and O 19 r 26(7); only 29(7)(a) (written submissions and any bundle of authorities) is a document that must accompany the application; (b), the bundle of documents, is a "may".
7. **Sub-paragraphs (a) and (b) of Order 15, rule 8(11) are conditions of the opening sentence, not separate rules.**
   The defendant may make the submission only on the basis that (a) the defendant will give no evidence and (b) any counterclaim on substantially the same facts is withdrawn; the first pass of the table caught a locator that stopped at the opening line.
   In the second round a defendant who will give evidence, or who keeps such a counterclaim, answers `JUST FALSE` (the first round answered `NOTHING`).
8. **No expected value was changed to match an output.**
   In the second round 34 expected values were changed because a reading changed by ruling or by the independent pass; the run made before they were touched failed on exactly those assertions, and each sits on an arm that was edited on purpose.
   The failures met on the way in the first round were errors in the encoding or in the test syntax and were corrected there: a call that omitted a second argument (O 15 r 13(1)), a projection applied to a function result without parentheses (the period-selection tests of the certificate rules) and a locator that stopped too early (Order 15, rule 8(11), above).

9. **Pass-throughs: only one lost a no.**
   A search of the eight layer-1 modules for the name of one function inside the body of another finds 20 pairs; in four the callee can answer `JUST FALSE` (it returns a `MAYBE BOOLEAN`): `o 15 r 22(3)` called by `o 15 r 22(1)`, `o 16 r 2(8)` by `o 16 r 2(7)`, `o 18 r 29(7)(a)` by `o 18 r 29(7)`, and `o 15 r 1(3)` by `o 18 r 7`.
   The other 16 call a period constant, a date, a figure, a rate or a plain yes/no test.
   `o 15 r 22(1)` was the one that lost the no: it took paragraph (3)'s result through a plain yes/no input and so turned `JUST FALSE` into `NOTHING`; it now calls paragraph (3) and follows its `JUST FALSE`.
   `o 16 r 2(7)` tests `o 16 r 2(8) ... EQUALS JUST FALSE`, `o 18 r 29(7)` returns the callee's answer as it is, and `o 18 r 7` reads all three answers of `o 15 r 1(3)` (fork 18.4).
   The other sites where a rule says "Subject to" or "Except as provided" a paragraph of its own Order or Rule (`o 15 r 1(4)`, `o 18 r 3(1)`, `r 4(1)`, `r 12(4)`, `r 29(1)`, `o 16 r 3(1)`, `r 4`) take that paragraph's fact as an input of their own (for example `paragraph (2) applies`), so they read no answer of another function; the caller supplies the fact.

## What the main binary does not accept (roc3)

- **A `DEONTIC` value cannot be compared with `EQUALS`.**
  The regulative rules in `roc3-regulative.l4` are therefore run with `#TRACE` and their outcomes read by eye; each duty also has a decision-function twin in the layer-1 modules, and the twin is the one that is asserted (for example `o 18 r 15 the notice of appeal in Form 35 is filed and served in time` for the duty of `o 18 r 15 the appellant must file and serve the notice of appeal`).
  `check.sh` counts only assertions, so it cannot see a changed trace; the 19 traces were compared by running the module on 1.6.109 and on 1.6.108 and reading both outcomes (identical).
- **`WAIT UNTIL` (two words) is an unknown identifier on 1.6.109**; the clock advance is spelled `WAITUNTIL` (as the brief says).
- **`WITHIN` counts forward from the start of the trace.** A period the Rules count backward from a hearing cannot be written in it; no regulative rule is written for O 15 r 4(3), r 4(12) or r 16(6).
- **A function applied to arguments, followed by a projection, must be parenthesised**: `` (`f` x)'s `field` `` (without the brackets the projection binds to the last argument).
- **Not used, because main rejects them:** `REFUSE`, sets, `TYPICALLY` on a record field, `YMD`, a continuation line in an `#ASSERT`.

The 19 traces of `roc3-regulative.l4` and their outcomes on main 1.6.109 (identical on 1.6.108):

| # | trace | outcome |
| --- | --- | --- |
| 1 | ``o 16 r 2(1) the claimant may serve a notice in Form 32 after service of the defence` AT 0 WITH` | FULFILLED |
| 2 | ``o 16 r 2(1) the claimant may serve a notice in Form 32 after service of the defence` AT 0 WITH` | FULFILLED |
| 3 | ``o 17 r 3(5) the party must send a draft of the order to the solicitors of all other parties` AT 0 W` | FULFILLED |
| 4 | ``o 17 r 3(5) the party must send a draft of the order to the solicitors of all other parties` AT 0 W` | PARTY `o 17 r 3(5) any other party affected by the order` MAY `o 17 r 3(5) draw up the order` HENCE FULFILLED |
| 5 | ``o 17 r 3(6) the solicitors must respond to the draft` AT 0 WITH` | FULFILLED |
| 6 | ``o 17 r 3(6) the solicitors must respond to the draft` AT 0 WITH` | DEONTIC BREACHED: BREACH BY `o 17 r 3(6) the solicitors of the other parties` BECAUSE "failing which they are  |
| 7 | ``o 18 r 9(3) the absent party may apply to restore the appeal` AT 0 WITH` | FULFILLED |
| 8 | ``o 18 r 9(3) the absent party may apply to restore the appeal` AT 0 WITH` | FULFILLED |
| 9 | ``o 18 r 15 the appellant must file and serve the notice of appeal` AT 0 WITH` | FULFILLED |
| 10 | ``o 18 r 15 the appellant must file and serve the notice of appeal` AT 0 WITH` | DEONTIC BREACHED: BREACH BY `o 18 r 15 the appellant` BECAUSE "within 14 days after the date of the Registrar’ |
| 11 | ``o 18 r 20(1) the appellant must provide security and file the certificate` AT 0 WITH` | FULFILLED |
| 12 | ``o 18 r 20(1) the appellant must provide security and file the certificate` AT 0 WITH` | DEONTIC BREACHED: BREACH BY `o 18 r 20(1) the appellant` BECAUSE "at the time the appellant files the notice o |
| 13 | ``o 18 r 21(12) the appellant must file and serve the written submissions within the specified time` ` | FULFILLED |
| 14 | ``o 18 r 21(12) the appellant must file and serve the written submissions within the specified time` ` | DEONTIC BREACHED: BREACH BY `o 18 r 21(12) the appellant` BECAUSE "the appeal is deemed withdrawn" |
| 15 | ``o 18 r 33(12) the appellant must file and serve the written submissions within the specified time` ` | FULFILLED |
| 16 | ``o 18 r 33(12) the appellant must file and serve the written submissions within the specified time` ` | DEONTIC BREACHED: BREACH BY `o 18 r 33(12) the appellant` BECAUSE "the appeal is deemed withdrawn" |
| 17 | ``o 18 r 21(14)(a) the party may request directions on the outstanding issues` AT 0 WITH` | FULFILLED |
| 18 | ``o 18 r 21(15) the respondent shall not make submissions at the hearing of the appeal` TRUE FALSE AT` | DEONTIC BREACHED: party `o 18 r 21(15) the respondent` who did action `o 18 r 21(15) make submissions at the h |
| 19 | ``o 18 r 21(15) the respondent shall not make submissions at the hearing of the appeal` FALSE FALSE A` | FULFILLED |

## check.sh output (roc3)

Run as `L4=<main 1.6.109> L4_MAIN=<main 1.6.108> ./check.sh` in the encoding folder.
The print below replaces the first round's; no earlier print is kept in this folder.
The first full run (before the locator of Order 15, rule 8(11) was widened and before the seat's `@desc` wording was rewritten in the second person) and the first round's final run printed 21 modules, 1436 assertions satisfied, 0 errors, 0 failed and 0 refused, with every module `same` on the second main build.
The print below is the second round's: 1522 assertions satisfied (86 more than the first round), after the changes listed under "Status".

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
roc3-cases-seat.l4                             0       149       0        0         0 |      0       149       0        0  same
roc3-order-15-affidavits.l4                    0         0       0        0         0 |      0         0       0        0  same
roc3-order-15-evidence.l4                      0         0       0        0         0 |      0         0       0        0  same
roc3-order-15-hearings.l4                      0         0       0        0         0 |      0         0       0        0  same
roc3-order-16.l4                               0         0       0        0         0 |      0         0       0        0  same
roc3-order-17.l4                               0         0       0        0         0 |      0         0       0        0  same
roc3-order-18-general.l4                       0         0       0        0         0 |      0         0       0        0  same
roc3-order-18-higher.l4                        0         0       0        0         0 |      0         0       0        0  same
roc3-order-18-lower.l4                         0         0       0        0         0 |      0         0       0        0  same
roc3-regulative.l4                             0         0       0        0         0 |      0         0       0        0  same
roc3-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
roc3-tests-order-15-affidavits.l4              0        80       0        0         0 |      0        80       0        0  same
roc3-tests-order-15-evidence.l4                0       156       0        0         0 |      0       156       0        0  same
roc3-tests-order-15-hearings.l4                0       193       0        0         0 |      0       193       0        0  same
roc3-tests-order-16.l4                         0        68       0        0         0 |      0        68       0        0  same
roc3-tests-order-17.l4                         0        68       0        0         0 |      0        68       0        0  same
roc3-tests-order-18-general.l4                 0       171       0        0         0 |      0       171       0        0  same
roc3-tests-order-18-higher.l4                  0       365       0        0         0 |      0       365       0        0  same
roc3-tests-order-18-lower.l4                   0       272       0        0         0 |      0       272       0        0  same
TOTAL (21 modules)                             0      1522       0        0           |      0      1522       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)

```
