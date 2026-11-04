# NOTES (wra4: Welfare Reform Act 2012, Part 5, ss 96 to 134, raw lines 1520-2474)

Status, 4 November 2026: layer 1, the regulative rules, the seat layer and its cases are written and run green on the stable binary 1.6.98 and on the main build 1.6.108 (numbers in the last section).
This part is the benefit cap (ss 96 to 97), claims, payments and appeals (98 to 104), recovery of overpayments (105 to 109), investigation and prosecution (110 to 112), penalties (113 to 116), loss of benefit for benefit offences (117 to 121), tax credit fraud (122 to 126), and information-sharing and disclosure (127 to 134).

**The source is not the official text.**
`ukpga-2012-5.txt` is a plain-text rendering made by a converter script.
Every quotation in the `.l4` files is copied from it by script, and `srcrefs.py check --refs` and `--strict` both report 0 problems over every `wra4-*.l4` file.
Nothing in this folder is "verified against the official text", and no claim here should be read as that.

Read-only inputs used: the brief, `PLAN.md`, `KEEL-NOTES.md`, `ENCODING-GUIDE.md`, `COMMONS-CLAUDE.md`, the example seat layer, the two skills' reference files and the supplied `daydate.l4` and `prelude.l4` libraries.
No other run directory, no file under `~/.claude/`, and no existing encoding of any Act was opened (`peeked`: nothing).

## Files

| file | what it is |
| --- | --- |
| `wra4-ss96-97.l4`, `wra4-ss98-104.l4`, `wra4-s105-recovery.l4`, `wra4-ss106-112.l4`, `wra4-ss113-116.l4`, `wra4-ss117-119.l4`, `wra4-s120-taxcredits.l4`, `wra4-ss121-126.l4`, `wra4-ss127-129.l4`, `wra4-ss130-134.l4` | layer 1: the rules, each with `-- src:` quotation lines and an `@ref`; they IMPORT the keel's `wra-core.l4`; `wra4-s120-taxcredits` also imports `wra4-ss117-119`, and `wra4-ss130-134` imports `wra4-ss96-97` and `wra4-ss127-129` |
| `wra4-tests-<same name>.l4` (ten files) | the tests of each layer-1 module |
| `wra4-regulative.l4`, `wra4-tests-regulative.l4` | the four duties, permissions and prohibitions written as `PARTY ... MUST / MAY / SHANT` rules, and eight `#TRACE`s |
| `wra4-seat.l4`, `wra4-cases-seat.l4` | layer 2: 49 questions for the person in the seat, and 143 cases |
| `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | this file; progress; the one thing the core lacks |
| `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`, `wra-core.l4`, `wra-definitions.l4` | supplied; not edited by this part |

All names in the `.l4` files begin with the label of the provision they implement (`s 105 SSAA 71ZB(3) ...`), including every `DECLARE`d type and constructor, so no name can collide with another part's.
Host Acts are shortened in labels: SSAA (Social Security Administration Act 1992), SSFA (Social Security Fraud Act 2001), SSA1998 (Social Security Act 1998), TCA (Tax Credits Act 2002), LA1980 (Limitation Act 1980), CJA1991 (Criminal Justice Act 1991), SSA(NI)A (Social Security Administration (Northern Ireland) Act 1992), JSA (Jobseekers Act 1995).


## Seat

**The seat is the individual**: a person who claims, receives or is moved to Universal Credit, or who claims Personal Independence Payment, or whose benefits are capped.
There is no seat for the Secretary of State, HM Revenue and Customs, a local authority, a tribunal or a court (ENCODING-GUIDE section 2).
Where a provision addresses only such an official, layer 1 encodes what it decides and the seat asks only what it means to the person (for example, whether the five-year review of the cap sums is overdue, s 96A(1); what may be recovered from them, s 105; who may be told about them, ss 127 to 132).

What the seat layer holds.

- `wra4-seat.l4`: 49 questions under 9 `§` headings in the text's order (ss 96-97; 99-102; 105; 106-112; 113-116; 117-119; 120-121; 127-129; 130-132).
  Each question has `@export <the question as the person asks it>` directly above its `GIVEN` inputs, an `@desc` on every input (worded as that person would be asked, with "Leave out if not known" on every input the regulations supply), and a `GIVETH`.
  Each is named "Under section N, ..." with the Act's own numbering.
- Each question is one call to the layer-1 rule it is named for; it restates nothing.
  Thirty-eight pass the layer-1 inputs straight through.
  Three build or combine: `Under section 97(6)` builds a `Decision` in a `WHERE` (the decision-maker, the benefit and the date are placeholders with a comment: the rule reads the kind of decision only); `Under section 118(5)` builds the eight-field conviction record from eight facts; `Under section 129(1)` calls the four lower rules (129(1), (2), (3), (4)) and hands their answers to the composite rule.
  Eight chain, so that the person is asked for facts they can state and not for a legal conclusion that another rule in this Part computes: `Under section 118(7)` asks the eight conviction facts and chains `Under section 118(5)`; `Under section 119(8), the restriction is to be treated as not imposed` chains `Under section 119(8), SSFA 7(7B) applies`; `Under section 127(2)` and `Under section 127(4)` chain `s 127(1)` and `s 127(3)` (what the information is held for, and who holds it); `Under section 129(5)` chains `Under section 129(1)`; `Under section 130(5)` chains `s 130(1)`, `s 130(2)` and `s 130(6)`; `Under section 131(1)` chains `s 131(11)`; `Under section 132(1)` chains `s 132(2)`.
  A few inputs remain that a lawyer would call a conclusion, because the text leaves them to regulations or to another Act and no rule in this Part computes them: the seam inputs of `Under section 105, SSAA 71ZH(1)` (whether a hardship payment is recoverable, seams 4 to 6), whether the information is "relevant information" (131(12)), and the `MAYBE` inputs marked "Leave out if not known".
- Answers keep their shape.
  A layer-1 rule that returns `MAYBE` answers `MAYBE` here, so `NOTHING` stays `NOTHING` and is never turned into `FALSE`.
  A layer-1 rule that returns a plain `BOOLEAN` is wrapped in `JUST`, so every yes/no question here answers `JUST TRUE`, `JUST FALSE` or `NOTHING`.
  The seat uses `MEANS`, not `DECIDE ... IF` with `GIVETH A BOOLEAN`.
- `wra4-cases-seat.l4`: 143 assertions.
  For each pass-through question (38), the cases are the layer-1 assertions on the rule it calls (one for each distinct result, at most four), asked through the seat with the same answers: 90 assertions.
  For the eleven built, combined or chained questions the cases are written by hand, 53 assertions (97(6) 3; 118(5) 6; 118(7) 4; 119(8) 7B 4; 127(2) 5; 127(4) 5; 129(1) 7; 129(5) 4; 130(5) 5; 131(1) 5; 132(1) 5), each a combination of layer-1 cases through the chain.
  A pass-through case is therefore a layer-1 case seen through the seat, with the expected value wrapped as the seat wraps it.
  The expected values were decided when the layer-1 tests were written, from the text; none was edited to match output.
  The first run of the hand-written cases for `Under section 118(5)` had three assertions fail: I had written the "limb (b)" cases without making the offence a prescribed offence in prescribed circumstances, which paragraph (b) requires ("a prescribed offence which, in the offender's case, is committed in such circumstances as may be prescribed, and which, on conviction ..."). The expected values were wrong, not the rule, and the cases were corrected to the text; a case where the offence is not prescribed (`JUST FALSE`) and one where that is not known (`NOTHING`) were added.
- What the seat does not ask.
  Questions about entitlement to Universal Credit and Personal Independence Payment themselves belong to other parts (the core and wra1/wra3 hold ss 1-95); this layer answers what ss 96-134 say to that person.
  Provisions that only amend another Act, make regulations or fix commencement have no question (they are inert rows in the coverage table).
  The rules that address only an official and say nothing the person can ask (for example `s 96A(3)`, the list in `s 126(13)`) are in layer 1.
- Inputs the regulations supply (a prescribed description, a prescribed date, the relevant amount for the reference period) are inputs with `@desc ... Leave out if not known.`; when left out the answer is `NOTHING`.
  No such number is written from memory.


## Coverage (wra4)

Every provision of lines 1520-2474 has one row with exactly one disposition, and the table is generated from the raw text by a script (`units.py` cuts the text into units; `disp.py` assigns each unit its disposition; `gen.py --table` prints the table below; the scripts are in the run's `work/` directory, outside this folder).
The dispositions are: `encoded` (a layer-1 rule or constant implements it, named in the last column), `fork` (the text can be read two or more ways with different outcomes: the fork register below has the readings, and the last column names the rules that encode the reading taken), `inert` with a reason (1 not operative: a title, heading or lead-in; 2 machinery: an amendment of another Act, a regulation-making power, commencement, procedure; 3 repealed or blank), and `repealed or blank in this text` (the text prints only dots).
No row uses inert reason 3, because the repealed or blank rows have their own disposition.

Audit (`work/audit.py`).

| check | result |
| --- | --- |
| raw lines in 1520-2474 | 955, all non-blank |
| text units counted (headings, sections, subsections, paragraphs, sub-paragraphs, defined terms, list items, host-Act headings and paragraphs) | 931 |
| rows in the table | 931 |
| non-blank raw lines in no unit | 0 |
| raw lines in more than one unit | 0 |
| units outside the range | 0 |
| units without a disposition | 0 |
| every name an `encoded` or `fork` row cites is defined (`work/verify_names.py`) | 257 definitions, 257 cited, 0 missing |
| every defined rule appears in the jural-relations table (`work/verify_jural.py`) | 257 of 257, every section 96 to 134 mentioned |

Rows before and after.
The table is regenerated from the text on every run, so the row count was 931 at the first run and is 931 now; no row was added or deleted by hand.
The audit pass changed one row's disposition (line 1551, the lead-in of s 96(10): `encoded` with no name, now `inert` reason 2) and added helper rules that were missing from the rows that use them.

Counts by disposition.

| disposition | rows |
| --- | --- |
| encoded | 533 |
| fork | 22 |
| inert, reason 1 (not operative) | 63 |
| inert, reason 2 (machinery) | 306 |
| inert, reason 3 | 0 |
| repealed or blank in this text | 7 |
| total | 931 |

(Inert in all: 369.
Of the "repealed or blank" rows, all seven are the dotted subsections s 96(6), (7), (8), (11), s 96A(9), s 97(3) and s 97(5), which the text prints as dots.)


The table (generated by `work/gen.py --table`).

| lines | unit | kind | disposition | L4 name, or why |
| --- | --- | --- | --- | --- |
| 1520 | heading: Part 5 — Social security: general | heading | inert (reason 1: not operative) | title / cross-heading / section heading: not operative |
| 1521 | heading: Benefit cap | heading | inert (reason 1: not operative) | title / cross-heading / section heading: not operative |
| 1522 | s 96 | section | inert (reason 1: not operative) | title / cross-heading / section heading: not operative |
| 1523 | s 96(1) | sub | encoded | `s 96(1) a benefit cap is applied to the person's welfare benefits` |
| 1524 | s 96(2) | sub | encoded | `s 96(2) the total entitlement to welfare benefits`, `s 96(2) the total entitlement exceeds the relevant amount`, `s 96(2) the greatest reduction the cap can require` |
| 1525 | s 96(3) | sub | encoded | `s 96(3) the reference period` |
| 1526 | s 96(4) | sub | inert (reason 2: machinery) | regulation-making power: what regulations may in particular provide (4)(a)-(b); the content is regulations' own, outside the sources |
| 1527 | s 96(4)(a) | para | inert (reason 2: machinery) | regulation-making power: what regulations may in particular provide (4)(a)-(b); the content is regulations' own, outside the sources |
| 1528 | s 96(4)(b) | para | inert (reason 2: machinery) | regulation-making power: what regulations may in particular provide (4)(a)-(b); the content is regulations' own, outside the sources |
| 1529 | s 96(4)(c) | para | encoded | `s 96(1) a benefit cap is applied to the person's welfare benefits` (exceptions input) |
| 1530 | s 96(4)(d) | para | inert (reason 2: machinery) | regulation-making power: what regulations may in particular provide (4)(d)-(g) |
| 1531 | s 96(4)(e) | para | inert (reason 2: machinery) | regulation-making power: what regulations may in particular provide (4)(d)-(g) |
| 1532 | s 96(4)(f) | para | inert (reason 2: machinery) | regulation-making power: what regulations may in particular provide (4)(d)-(g) |
| 1533 | s 96(4)(g) | para | inert (reason 2: machinery) | regulation-making power: what regulations may in particular provide (4)(d)-(g) |
| 1534 | s 96(5) | sub | encoded | `s 96(5B)(c) the annual limit divided into reference periods` (the relevant amount from the annual limit) |
| 1535 | s 96(5A) | sub | encoded | `s 96(5A) the annual limit` |
| 1536 | s 96(5A)(a) | para | encoded | `s 96(5A) the annual limit` |
| 1537 | s 96(5A)(b) | para | encoded | `s 96(5A) the annual limit` |
| 1538 | s 96(5B) | sub | encoded | `s 96(5A) the annual limit` (which figure applies: an input) |
| 1539 | s 96(5B)(a) | para | encoded | `s 96(5A) the annual limit` (which figure applies: an input) |
| 1540 | s 96(5B)(a)(i) | subpara | encoded | `s 96(5A) the annual limit` (which figure applies: an input) |
| 1541 | s 96(5B)(a)(ii) | subpara | encoded | `s 96(5A) the annual limit` (which figure applies: an input) |
| 1542 | s 96(5B)(b) | para | encoded | `s 96(5A) the annual limit` ("resident" as regulations define it: an input) |
| 1543 | s 96(5B)(c) | para | encoded | `s 96(5B)(c) the annual limit divided into reference periods` |
| 1544 | s 96(6) | sub | repealed or blank in this text | a line of dots: repealed or blank in this text |
| 1545 | s 96(7) | sub | repealed or blank in this text | a line of dots: repealed or blank in this text |
| 1546 | s 96(8) | sub | repealed or blank in this text | a line of dots: repealed or blank in this text |
| 1547 | s 96(9) | sub | encoded | `s 96(9) benefit cap regulations may reduce this welfare benefit` |
| 1548 | s 96(9)(a) | para | encoded | `s 96(9) benefit cap regulations may reduce this welfare benefit` |
| 1549 | s 96(9)(b) | para | encoded | `s 96(9) benefit cap regulations may reduce this welfare benefit` |
| 1550 | s 96(9)(c) | para | encoded | `s 96(9) benefit cap regulations may reduce this welfare benefit` |
| 1551 | s 96(10) | sub | inert (reason 2: machinery) | lead-in to the definitions of 96(10): scope only; each definition is encoded where it stands |
| 1552 | s 96(10) “couple” | defterm | encoded | `s 96(10) the two persons are a couple` |
| 1553 | s 96(10) “prescribed” | defterm | encoded | `s 96(10) the matter is prescribed` |
| 1554 | s 96(10) “regulations” | defterm | encoded | `s 96(10) regulations made by this maker are regulations` |
| 1555 | s 96(10) “single person” | defterm | encoded | `s 96(10) the person is a single person` |
| 1556 | s 96(10) “welfare benefit” | defterm | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1557 | s 96(10) "welfare benefit" item 1 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1558 | s 96(10) "welfare benefit" item 2 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1559 | s 96(10) "welfare benefit" item 3 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1560 | s 96(10) "welfare benefit" item 4 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1561 | s 96(10) "welfare benefit" item 5 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1562 | s 96(10) "welfare benefit" item 6 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1563 | s 96(10) "welfare benefit" item 7 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1564 | s 96(10) "welfare benefit" item 8 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1565 | s 96(10) "welfare benefit" item 9 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1566 | s 96(10) "welfare benefit" item 10 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1567 | s 96(10) "welfare benefit" item 11 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1568 | s 96(10) "welfare benefit" item 12 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1569 | s 96(10) "welfare benefit" item 13 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1570 | s 96(10) "welfare benefit" item 14 | listitem | encoded | `s 96(10) the benefit is a welfare benefit` (one test per row) |
| 1571 | s 96(11) | sub | repealed or blank in this text | a line of dots: repealed or blank in this text |
| 1572 | s 96A | section | inert (reason 1: not operative) | section heading: not operative |
| 1573 | s 96A(1) | sub | fork | fork F1 (the latest day for a review "at least once every five years"): `s 96A(1) the latest day for the next review of the sums`, `s 96A(1) the five-year review is overdue`, `s 96A(1) the duty to review the sums` |
| 1574 | s 96A(2) | sub | encoded | `s 96A(2) the Secretary of State may review the sums at this time` |
| 1575 | s 96A(3) | sub | encoded | `s 96A(3) the review met the requirement to take account of the national economic situation` |
| 1576 | s 96A(3)(a) | para | encoded | `s 96A(3) the review met the requirement to take account of the national economic situation` |
| 1577 | s 96A(3)(b) | para | encoded | `s 96A(3) the review met the requirement to take account of the national economic situation` |
| 1578 | s 96A(4) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1579 | s 96A(5) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1580 | s 96A(5)(a) | para | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1581 | s 96A(5)(b) | para | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1582 | s 96A(6) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1583 | s 96A(7) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1584 | s 96A(7)(a) | para | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1585 | s 96A(7)(b) | para | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1586 | s 96A(7)(c) | para | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1587 | s 96A(8) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (96A(4)-(8)): amending s 96(5A) by regulations, coming into force, transitional notices, and disapplying SSAA s 176 consultation |
| 1588 | s 96A(9) | sub | repealed or blank in this text | a line of dots: repealed or blank in this text |
| 1589 | s 97 | section | inert (reason 1: not operative) | section heading: not operative |
| 1590 | s 97(1) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (97(1)-(5)); (3) and (5) are lines of dots (repealed or blank), (4) has a deleted word shown as "..." |
| 1591 | s 97(2) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (97(1)-(5)); (3) and (5) are lines of dots (repealed or blank), (4) has a deleted word shown as "..." |
| 1592 | s 97(3) | sub | repealed or blank in this text | a line of dots: repealed or blank in this text |
| 1593 | s 97(4) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (97(1)-(5)); (3) and (5) are lines of dots (repealed or blank), (4) has a deleted word shown as "..." |
| 1594 | s 97(4A) | sub | inert (reason 2: machinery) | regulation-making power and its procedure (97(1)-(5)); (3) and (5) are lines of dots (repealed or blank), (4) has a deleted word shown as "..." |
| 1595 | s 97(5) | sub | repealed or blank in this text | a line of dots: repealed or blank in this text |
| 1596 | s 97(6) | sub | encoded | `s 97(6) SSA1998 Sch 2 para 8A an appeal lies against the decision` |
| 1597-1598 | s 97(6) SSA1998 Sch 2 para 8A (heading 8A) | host-heading | encoded | `s 97(6) SSA1998 Sch 2 para 8A an appeal lies against the decision` |
| 1599 | heading: Claims and awards | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1600 | s 98 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1601 | s 98(1) | sub | inert (reason 2: machinery) | s 98: amendment of SSAA 5(1) to give regulations a new power: machinery (conditional awards, claims on behalf of another or jointly, notice of change): what regulations may then provide is outside the sources |
| 1602 | s 98(2) | sub | inert (reason 2: machinery) | s 98: amendment of SSAA 5(1) to give regulations a new power: machinery (conditional awards, claims on behalf of another or jointly, notice of change): what regulations may then provide is outside the sources |
| 1603 | s 98(2)(i) | subpara | inert (reason 2: machinery) | s 98: amendment of SSAA 5(1) to give regulations a new power: machinery (conditional awards, claims on behalf of another or jointly, notice of change): what regulations may then provide is outside the sources |
| 1604 | s 98(2)(ii) | subpara | inert (reason 2: machinery) | s 98: amendment of SSAA 5(1) to give regulations a new power: machinery (conditional awards, claims on behalf of another or jointly, notice of change): what regulations may then provide is outside the sources |
| 1605 | s 98(3) | sub | inert (reason 2: machinery) | s 98: amendment of SSAA 5(1) to give regulations a new power: machinery (conditional awards, claims on behalf of another or jointly, notice of change): what regulations may then provide is outside the sources |
| 1606 | s 98(4) | sub | inert (reason 2: machinery) | s 98: amendment of SSAA 5(1) to give regulations a new power: machinery (conditional awards, claims on behalf of another or jointly, notice of change): what regulations may then provide is outside the sources |
| 1607 | s 98(5) | sub | inert (reason 2: machinery) | s 98: amendment of SSAA 5(1) to give regulations a new power: machinery (conditional awards, claims on behalf of another or jointly, notice of change): what regulations may then provide is outside the sources |
| 1608 | s 99 | section | inert (reason 1: not operative) | section heading: not operative |
| 1609 | s 99(1) | sub | inert (reason 2: machinery) | s 99(1)-(3) lead-in: amending words (SSAA 5; the inserted 5(1A) is encoded below) |
| 1610 | s 99(2) | sub | inert (reason 2: machinery) | s 99(1)-(3) lead-in: amending words (SSAA 5; the inserted 5(1A) is encoded below) |
| 1611 | s 99(3) | sub | inert (reason 2: machinery) | s 99(1)-(3) lead-in: amending words (SSAA 5; the inserted 5(1A) is encoded below) |
| 1612 | s 99(3) SSAA 5(1A) | sub | encoded | `s 99(3) SSAA 5(1A) regulations may require the person to supply the information` |
| 1613 | s 99(3) SSAA 5(1A)(a) | para | encoded | `s 99(3) SSAA 5(1A) regulations may require the person to supply the information` |
| 1614 | s 99(3) SSAA 5(1A)(b) | para | encoded | `s 99(3) SSAA 5(1A) regulations may require the person to supply the information` |
| 1615 | s 99(4) | sub | inert (reason 2: machinery) | s 99(4)-(5): repeal of SSAA 5(3A) and a conforming change in SSA1998 s 22 |
| 1616 | s 99(5) | sub | inert (reason 2: machinery) | s 99(4)-(5): repeal of SSAA 5(3A) and a conforming change in SSA1998 s 22 |
| 1617 | heading: Payments | heading | inert (reason 1: not operative) | cross-heading: not operative |
| 1618-1619 | s 100 | section | inert (reason 2: machinery) | s 100: section heading and the amending words (the inserted SSAA 5(3B) is encoded below) |
| 1620 | s 100 SSAA 5(3B) | sub | encoded | `s 100 SSAA 5(3B) the Secretary of State may be given power to direct the payment in this way` |
| 1621 | s 100 SSAA 5(3B)(a) | para | encoded | `s 100 SSAA 5(3B) the Secretary of State may be given power to direct the payment in this way` |
| 1622 | s 100 SSAA 5(3B)(b) | para | encoded | `s 100 SSAA 5(3B) the Secretary of State may be given power to direct the payment in this way` |
| 1623 | s 101 | section | inert (reason 1: not operative) | section heading: not operative |
| 1624 | s 101(1) | sub | inert (reason 2: machinery) | s 101(1): amending words (SSAA 5(1)(r) is encoded below) |
| 1625 | s 101(1) SSAA 5(1)(r) | para | encoded | `s 101(1) SSAA 5(1)(r) regulations may provide for a payment on account in this case` |
| 1626 | s 101(1) SSAA 5(1)(r)(i) | subpara | encoded | `s 101(1) SSAA 5(1)(r) regulations may provide for a payment on account in this case` |
| 1627 | s 101(1) SSAA 5(1)(r)(ii) | subpara | encoded | `s 101(1) SSAA 5(1)(r) regulations may provide for a payment on account in this case` |
| 1628 | s 101(1) SSAA 5(1)(r)(iii) | subpara | encoded | `s 101(1) SSAA 5(1)(r) regulations may provide for a payment on account in this case` |
| 1629 | s 101(2) | sub | inert (reason 2: machinery) | s 101(2): repeal of s 22 of the Welfare Reform Act 2009, which was never brought into force: an amendment of another Act |
| 1630 | heading: Appeals | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1631 | s 102 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1632 | s 102(1) | sub | inert (reason 2: machinery) | s 102(1)-(2): amending words (SSA1998 s 12(2): the words become paragraph (a), then paragraph (b) is inserted) |
| 1633 | s 102(2) | sub | inert (reason 2: machinery) | s 102(1)-(2): amending words (SSA1998 s 12(2): the words become paragraph (a), then paragraph (b) is inserted) |
| 1634 | s 102(2)(a) | para | inert (reason 2: machinery) | s 102(1)-(2): amending words (SSA1998 s 12(2): the words become paragraph (a), then paragraph (b) is inserted) |
| 1635 | s 102(2)(b) | para | inert (reason 2: machinery) | s 102(1)-(2): amending words (SSA1998 s 12(2): the words become paragraph (a), then paragraph (b) is inserted) |
| 1636 | s 102(2) SSA1998 12(2)(b) | para | encoded | `s 102(2) SSA1998 12(2)(b) there is a right of appeal because regulations so provide` |
| 1637 | s 102(3) | sub | inert (reason 2: machinery) | s 102(3) lead-in: amending words |
| 1638 | s 102(3) SSA1998 12(3A) | sub | encoded | `s 102(3) SSA1998 12(3A) there is a right of appeal` (seam 8) |
| 1639 | s 102(3) SSA1998 12(3B) | sub | encoded | `s 102(3) SSA1998 12(3B) the consideration meets the condition the regulations set` |
| 1640 | s 102(3) SSA1998 12(3B)(a) | para | encoded | `s 102(3) SSA1998 12(3B) the consideration meets the condition the regulations set` |
| 1641 | s 102(3) SSA1998 12(3B)(b) | para | encoded | `s 102(3) SSA1998 12(3B) the consideration meets the condition the regulations set` |
| 1642 | s 102(3) SSA1998 12(3B)(c) | para | encoded | `s 102(3) SSA1998 12(3B) the consideration meets the condition the regulations set` |
| 1643 | s 102(3) SSA1998 12(3C) | sub | encoded | `s 102(3) SSA1998 12(3C) the references to the Secretary of State and regulations are read as the other person's` |
| 1644 | s 102(4) | sub | inert (reason 2: machinery) | s 102(4) lead-in: amending words (SSA1998 s 12(7)) |
| 1645 | s 102(4)(a) | para | inert (reason 2: machinery) | s 102(4) lead-in: amending words (SSA1998 s 12(7)) |
| 1646 | s 102(4)(b) | para | inert (reason 2: machinery) | s 102(4) lead-in: amending words (SSA1998 s 12(7)) |
| 1647 | s 102(4)(b) SSA1998 12(7)(b) | para | encoded | `s 102(4) SSA1998 12(7)(b) the purported appeal may be treated as an application for revision` |
| 1648 | s 102(5) | sub | inert (reason 2: machinery) | s 102(5)-(6): a conforming change to SSA1998 s 80(1)(a), and a pointer to Schedule 11 (similar amendments to other Acts; encoded by another part) |
| 1649 | s 102(6) | sub | inert (reason 2: machinery) | s 102(5)-(6): a conforming change to SSA1998 s 80(1)(a), and a pointer to Schedule 11 (similar amendments to other Acts; encoded by another part) |
| 1650 | s 102(7) | sub | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1651 | s 102(8) | sub | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1652 | s 102(9) | sub | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1653 | s 102(9)(a) | para | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1654 | s 102(9)(b) | para | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1655 | s 102(9)(c) | para | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1656 | s 102(9)(d) | para | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1657 | s 102(9)(e) | para | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1658 | s 102(9)(f) | para | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1659 | s 102(9)(g) | para | inert (reason 2: machinery) | s 102(7)-(9): limited-area regulations, by virtue of the power to commence for different areas (s 150(4)(b)): commencement machinery |
| 1660 | s 103 | section | inert (reason 1: not operative) | section heading: not operative |
| 1661 | s 103(1) | sub | inert (reason 2: machinery) | s 103(1): introduces Schedule 12 (amendments reinstating powers); the Schedule is another part's |
| 1662 | s 103(2) | sub | encoded | `s 103(2)(a) the Schedule 12 amendments have effect on the day`, `s 103(2)(b) the regulations have effect on the day` |
| 1663 | s 103(2)(a) | para | encoded | `s 103(2)(a) the Schedule 12 amendments have effect on the day`, `s 103(2)(b) the regulations have effect on the day` |
| 1664 | s 103(2)(b) | para | encoded | `s 103(2)(a) the Schedule 12 amendments have effect on the day`, `s 103(2)(b) the regulations have effect on the day` |
| 1665 | heading: Electronic communications | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1666 | s 104 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1667 | s 104(1) | sub | inert (reason 2: machinery) | s 104(1): amendment of SSAA 189 (the inserted 5A says what regulations' provision on electronic communications includes: a regulation-making power) |
| 1668 | s 104(1) SSAA 189(5A) | sub | inert (reason 2: machinery) | s 104(1): amendment of SSAA 189 (the inserted 5A says what regulations' provision on electronic communications includes: a regulation-making power) |
| 1669 | s 104(1) SSAA 189(5B) | sub | encoded | `s 104(1) SSAA 189(5B) the reference is read as` |
| 1670 | s 104(2) | sub | inert (reason 2: machinery) | s 104(2): amendment of SSA1998 s 79 (the inserted 6A is the same regulation-making provision) |
| 1671 | s 104(2) SSA1998 79(6A) | sub | inert (reason 2: machinery) | s 104(2): amendment of SSA1998 s 79 (the inserted 6A is the same regulation-making provision) |
| 1672 | s 104(2) SSA1998 79(6B) | sub | encoded | `s 104(2) SSA1998 79(6B) the reference is read as` |
| 1673 | heading: Recovery of benefits | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1674 | s 105 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1675 | s 105(1) | sub | inert (reason 2: machinery) | s 105(1) lead-in: amending words (inserts 71ZB to 71ZH into SSAA); the cross-heading it inserts is not operative |
| 1676 | heading: Recovery of benefit payments | heading | inert (reason 2: machinery) | s 105(1) lead-in: amending words (inserts 71ZB to 71ZH into SSAA); the cross-heading it inserts is not operative |
| 1677 | s 105(1) SSAA 71ZB (heading 71ZB) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 71ZB: not operative |
| 1678 | s 105(1) SSAA 71ZB(1) | sub | encoded | `s 105 SSAA 71ZB(1) the amount paid in excess of entitlement`, `s 105 SSAA 71ZB(1) the Secretary of State may recover an overpayment of the benefit`, `s 105 SSAA 71ZB(1) the benefit is named in the list` |
| 1679 | s 105(1) SSAA 71ZB(1)(a) | para | encoded | `s 105 SSAA 71ZB(1)(a) the universal credit paid in excess of entitlement` (seams 2, 3), `s 105 SSAA 71ZB(1) the Secretary of State may recover an overpayment of the benefit` |
| 1680 | s 105(1) SSAA 71ZB(1)(b) | para | encoded | `s 105 SSAA 71ZB(1) the Secretary of State may recover an overpayment of the benefit` (jobseeker's allowance; employment and support allowance; housing credit except in prescribed circumstances) |
| 1681 | s 105(1) SSAA 71ZB(1)(c) | para | encoded | `s 105 SSAA 71ZB(1) the Secretary of State may recover an overpayment of the benefit` (jobseeker's allowance; employment and support allowance; housing credit except in prescribed circumstances) |
| 1682 | s 105(1) SSAA 71ZB(1)(d) | para | encoded | `s 105 SSAA 71ZB(1) the Secretary of State may recover an overpayment of the benefit` (jobseeker's allowance; employment and support allowance; housing credit except in prescribed circumstances) |
| 1683 | s 105(1) SSAA 71ZB(2) | sub | encoded | `s 105 SSAA 71ZB(2) the amount is recoverable from the person` |
| 1684 | s 105(1) SSAA 71ZB(2)(a) | para | encoded | `s 105 SSAA 71ZB(2) the amount is recoverable from the person` |
| 1685 | s 105(1) SSAA 71ZB(2)(b) | para | encoded | `s 105 SSAA 71ZB(2) the amount is recoverable from the person` |
| 1686 | s 105(1) SSAA 71ZB(3) | sub | encoded | `s 105 SSAA 71ZB(3) the determination does not bar recovery` |
| 1687 | s 105(1) SSAA 71ZB(3)(a) | para | encoded | `s 105 SSAA 71ZB(3) the determination does not bar recovery` |
| 1688-1689 | s 105(1) SSAA 71ZB(3)(b) | para | encoded | `s 105 SSAA 71ZB(3) the determination does not bar recovery` |
| 1690 | s 105(1) SSAA 71ZB(4) | sub | inert (reason 2: machinery) | regulation-making power: amounts recoverable calculated or estimated in a prescribed manner |
| 1691 | s 105(1) SSAA 71ZB(5) | sub | encoded | `s 105 SSAA 71ZB(5) the amount is treated as paid in excess of entitlement` |
| 1692 | s 105(1) SSAA 71ZB(6) | sub | encoded | `s 105 SSAA 71ZB(6) the amount paid to one of them may be regarded as paid to the other` |
| 1693 | s 105(1) SSAA 71ZB(7) | sub | encoded | `s 105 SSAA 71ZB(7) an amount recoverable under 71ZB may be recovered in this way` |
| 1694 | s 105(1) SSAA 71ZB(7)(a) | para | encoded | `s 105 SSAA 71ZB(7) an amount recoverable under 71ZB may be recovered in this way` |
| 1695 | s 105(1) SSAA 71ZB(7)(b) | para | encoded | `s 105 SSAA 71ZB(7) an amount recoverable under 71ZB may be recovered in this way` |
| 1696 | s 105(1) SSAA 71ZB(7)(c) | para | encoded | `s 105 SSAA 71ZB(7) an amount recoverable under 71ZB may be recovered in this way` |
| 1697 | s 105(1) SSAA 71ZB(7)(d) | para | encoded | `s 105 SSAA 71ZB(7) an amount recoverable under 71ZB may be recovered in this way` |
| 1698 | s 105(1) SSAA 71ZC (heading 71ZC) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 71ZC: not operative |
| 1699 | s 105(1) SSAA 71ZC(1) | sub | encoded | `s 105 SSAA 71ZC(1) the amount may be recovered by deduction from this payment` |
| 1700 | s 105(1) SSAA 71ZC(2) | sub | encoded | `s 105 SSAA 71ZC(2) the amount paid on behalf of another may be recovered by deduction from this source` |
| 1701 | s 105(1) SSAA 71ZC(2)(a) | para | encoded | `s 105 SSAA 71ZC(2) the amount paid on behalf of another may be recovered by deduction from this source` |
| 1702 | s 105(1) SSAA 71ZC(2)(b) | para | encoded | `s 105 SSAA 71ZC(2) the amount paid on behalf of another may be recovered by deduction from this source` |
| 1703 | s 105(1) SSAA 71ZC(2)(c) | para | encoded | `s 105 SSAA 71ZC(2) the amount paid on behalf of another may be recovered by deduction from this source` |
| 1704 | s 105(1) SSAA 71ZC(3) | sub | encoded | `s 105 SSAA 71ZC(3) the obligation is taken to be discharged by the deduction` |
| 1705 | s 105(1) SSAA 71ZC(4) | sub | encoded | `s 105 SSAA 71ZC(4) the obligation is taken to be discharged by the deduction` |
| 1706 | s 105(1) SSAA 71ZD (heading 71ZD) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 71ZD: not operative |
| 1707 | s 105(1) SSAA 71ZD(1) | sub | encoded | `s 105 SSAA 71ZD(1) the amount may be recovered by deduction from earnings` |
| 1708 | s 105(1) SSAA 71ZD(2) | sub | encoded | `s 105 SSAA 71ZD(2) the payment is earnings` |
| 1709 | s 105(1) SSAA 71ZD(3) | sub | inert (reason 2: machinery) | regulation-making power: what regulations under 71ZD(1) may include |
| 1710 | s 105(1) SSAA 71ZD(3)(a) | para | encoded | `s 105 SSAA 71ZD(3)(a) the person may be required to disclose details of their employer` |
| 1711 | s 105(1) SSAA 71ZD(3)(b) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(b)-(d), the notice to the employer, its contents, how payment is made (the employer is not the seat) |
| 1712 | s 105(1) SSAA 71ZD(3)(c) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(b)-(d), the notice to the employer, its contents, how payment is made (the employer is not the seat) |
| 1713 | s 105(1) SSAA 71ZD(3)(d) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(b)-(d), the notice to the employer, its contents, how payment is made (the employer is not the seat) |
| 1714 | s 105(1) SSAA 71ZD(3)(e) | para | encoded | `s 105 SSAA 71ZD(3)(e) the most that may be deducted from the earnings` |
| 1715 | s 105(1) SSAA 71ZD(3)(f) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1716 | s 105(1) SSAA 71ZD(3)(g) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1717 | s 105(1) SSAA 71ZD(3)(h) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1718 | s 105(1) SSAA 71ZD(3)(i) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1719 | s 105(1) SSAA 71ZD(3)(j) | para | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1720 | s 105(1) SSAA 71ZD(3)(j)(i) | subpara | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1721 | s 105(1) SSAA 71ZD(3)(j)(ii) | subpara | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1722 | s 105(1) SSAA 71ZD(3)(j)(iii) | subpara | inert (reason 2: machinery) | regulation-making power: 71ZD(3)(f)-(j), the employer's administrative costs, records, notification, an offence by regulations, and priority between deductions |
| 1723 | s 105(1) SSAA 71ZE (heading 71ZE) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 71ZE: not operative |
| 1724 | s 105(1) SSAA 71ZE(1) | sub | encoded | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts` |
| 1725 | s 105(1) SSAA 71ZE(1)(a) | para | encoded | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts` |
| 1726 | s 105(1) SSAA 71ZE(1)(b) | para | encoded | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts` |
| 1727 | s 105(1) SSAA 71ZE(2) | sub | encoded | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts` |
| 1728 | s 105(1) SSAA 71ZE(3) | sub | encoded | `s 105 SSAA 71ZE(3) the costs of recovery may be recovered as if recoverable under 71ZB` |
| 1729 | s 105(1) SSAA 71ZE(4) | sub | inert (reason 2: machinery) | transitional provision tied to the commencement of s 62 of another Act: commencement machinery |
| 1730-1731 | s 105(1) SSAA 71ZF (heading 71ZF) | host-heading | inert (reason 2: machinery) | SSAA 71ZF (adjustment of benefit): a regulation-making power; the method itself is listed as a way of recovering in 71ZB(7)(d), encoded there |
| 1732 | s 105(1) SSAA 71ZF(a) | para | inert (reason 2: machinery) | SSAA 71ZF (adjustment of benefit): a regulation-making power; the method itself is listed as a way of recovering in 71ZB(7)(d), encoded there |
| 1733 | s 105(1) SSAA 71ZF(a)(i) | subpara | inert (reason 2: machinery) | SSAA 71ZF (adjustment of benefit): a regulation-making power; the method itself is listed as a way of recovering in 71ZB(7)(d), encoded there |
| 1734-1735 | s 105(1) SSAA 71ZF(a)(ii) | subpara | inert (reason 2: machinery) | SSAA 71ZF (adjustment of benefit): a regulation-making power; the method itself is listed as a way of recovering in 71ZB(7)(d), encoded there |
| 1736 | s 105(1) SSAA 71ZF(b) | para | inert (reason 2: machinery) | SSAA 71ZF (adjustment of benefit): a regulation-making power; the method itself is listed as a way of recovering in 71ZB(7)(d), encoded there |
| 1737 | s 105(1) SSAA 71ZF(b)(i) | subpara | inert (reason 2: machinery) | SSAA 71ZF (adjustment of benefit): a regulation-making power; the method itself is listed as a way of recovering in 71ZB(7)(d), encoded there |
| 1738-1739 | s 105(1) SSAA 71ZF(b)(ii) | subpara | inert (reason 2: machinery) | SSAA 71ZF (adjustment of benefit): a regulation-making power; the method itself is listed as a way of recovering in 71ZB(7)(d), encoded there |
| 1740 | s 105(1) SSAA 71ZG (heading 71ZG) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 71ZG: not operative |
| 1741 | s 105(1) SSAA 71ZG(1) | sub | encoded | `s 105 SSAA 71ZG(1) the Secretary of State may recover the payment` |
| 1742 | s 105(1) SSAA 71ZG(2) | sub | encoded | `s 105 SSAA 71ZG(2) the amount is recoverable from the person` |
| 1743 | s 105(1) SSAA 71ZG(2)(a) | para | encoded | `s 105 SSAA 71ZG(2) the amount is recoverable from the person` |
| 1744 | s 105(1) SSAA 71ZG(2)(b) | para | encoded | `s 105 SSAA 71ZG(2) the amount is recoverable from the person` |
| 1745 | s 105(1) SSAA 71ZG(3) | sub | inert (reason 2: machinery) | regulation-making power: amounts calculated or estimated in a prescribed manner |
| 1746 | s 105(1) SSAA 71ZG(4) | sub | encoded | `s 105 SSAA 71ZG(4) the amount paid to one of them may be regarded as paid to the other` |
| 1747 | s 105(1) SSAA 71ZG(5) | sub | encoded | `s 105 SSAA 71ZG(5) the amount may be recovered in this way` |
| 1748 | s 105(1) SSAA 71ZH (heading 71ZH) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 71ZH: not operative |
| 1749 | s 105(1) SSAA 71ZH(1) | sub | encoded | `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment` (seams 4, 5, 6) |
| 1750 | s 105(1) SSAA 71ZH(1)(a) | para | encoded | `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment` (seams 4, 5, 6) |
| 1751 | s 105(1) SSAA 71ZH(1)(b) | para | encoded | `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment` (seams 4, 5, 6) |
| 1752 | s 105(1) SSAA 71ZH(1)(c) | para | encoded | `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment` (seams 4, 5, 6) |
| 1753 | s 105(1) SSAA 71ZH(1)(d) | para | encoded | `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment` (seams 4, 5, 6) |
| 1754 | s 105(1) SSAA 71ZH(1)(e) | para | encoded | `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment` (seams 4, 5, 6) |
| 1755 | s 105(1) SSAA 71ZH(2) | sub | encoded | `s 105 SSAA 71ZH(2) the amount is recoverable from the person` |
| 1756 | s 105(1) SSAA 71ZH(2)(a) | para | encoded | `s 105 SSAA 71ZH(2) the amount is recoverable from the person` |
| 1757 | s 105(1) SSAA 71ZH(2)(b) | para | encoded | `s 105 SSAA 71ZH(2) the amount is recoverable from the person` |
| 1758 | s 105(1) SSAA 71ZH(3) | sub | inert (reason 2: machinery) | regulation-making power: amounts calculated or estimated in a prescribed manner |
| 1759 | s 105(1) SSAA 71ZH(4) | sub | encoded | `s 105 SSAA 71ZH(4) the amount paid to one claimant may be regarded as paid to the other` |
| 1760 | s 105(1) SSAA 71ZH(5) | sub | encoded | `s 105 SSAA 71ZH(5) the amount may be recovered in this way` |
| 1761 | s 105(2) | sub | inert (reason 2: machinery) | s 105(2)-(4) lead-ins: amendments of SSAA ss 71, 115A and 115B (words inserted, substituted); the substituted 115B(4) and (4A) are encoded below |
| 1762 | s 105(3) | sub | inert (reason 2: machinery) | s 105(2)-(4) lead-ins: amendments of SSAA ss 71, 115A and 115B (words inserted, substituted); the substituted 115B(4) and (4A) are encoded below |
| 1763 | s 105(4) | sub | inert (reason 2: machinery) | s 105(2)-(4) lead-ins: amendments of SSAA ss 71, 115A and 115B (words inserted, substituted); the substituted 115B(4) and (4A) are encoded below |
| 1764 | s 105(4)(a) | para | inert (reason 2: machinery) | s 105(2)-(4) lead-ins: amendments of SSAA ss 71, 115A and 115B (words inserted, substituted); the substituted 115B(4) and (4A) are encoded below |
| 1765 | s 105(4)(a) SSAA 115B(4) | sub | encoded | `s 105(4) SSAA 115B(4)(b) criminal proceedings may be instituted against the recipient for the conduct`, `s 105(4) SSAA 115B(4)(a) the penalty is recoverable from the recipient` |
| 1766 | s 105(4)(a) SSAA 115B(4)(a) | para | encoded | `s 105(4) SSAA 115B(4)(b) criminal proceedings may be instituted against the recipient for the conduct`, `s 105(4) SSAA 115B(4)(a) the penalty is recoverable from the recipient` |
| 1767 | s 105(4)(a) SSAA 115B(4)(b) | para | encoded | `s 105(4) SSAA 115B(4)(b) criminal proceedings may be instituted against the recipient for the conduct`, `s 105(4) SSAA 115B(4)(a) the penalty is recoverable from the recipient` |
| 1768 | s 105(4)(a) SSAA 115B(4A) | sub | encoded | `s 105(4) SSAA 115B(4A) the penalty may be recovered in this way` |
| 1769 | s 105(4)(b) | para | inert (reason 2: machinery) | s 105(4)(b), (5), (6): repeal of a definition, additions to JSA Sch 1 paras 9 and 10 (regulation-making powers on whether a payment is recoverable: they feed seam 6), and an amendment of SSA1998 s 12(4) |
| 1770 | s 105(5) | sub | inert (reason 2: machinery) | s 105(4)(b), (5), (6): repeal of a definition, additions to JSA Sch 1 paras 9 and 10 (regulation-making powers on whether a payment is recoverable: they feed seam 6), and an amendment of SSA1998 s 12(4) |
| 1771 | s 105(5)(a) | para | inert (reason 2: machinery) | s 105(4)(b), (5), (6): repeal of a definition, additions to JSA Sch 1 paras 9 and 10 (regulation-making powers on whether a payment is recoverable: they feed seam 6), and an amendment of SSA1998 s 12(4) |
| 1772 | s 105(5)(a) JSA Sch 1 para 9(c) | para | inert (reason 2: machinery) | s 105(4)(b), (5), (6): repeal of a definition, additions to JSA Sch 1 paras 9 and 10 (regulation-making powers on whether a payment is recoverable: they feed seam 6), and an amendment of SSA1998 s 12(4) |
| 1773 | s 105(5)(b) | para | inert (reason 2: machinery) | s 105(4)(b), (5), (6): repeal of a definition, additions to JSA Sch 1 paras 9 and 10 (regulation-making powers on whether a payment is recoverable: they feed seam 6), and an amendment of SSA1998 s 12(4) |
| 1774 | s 105(5)(b) JSA Sch 1 para 10(5)(a) | para | inert (reason 2: machinery) | s 105(4)(b), (5), (6): repeal of a definition, additions to JSA Sch 1 paras 9 and 10 (regulation-making powers on whether a payment is recoverable: they feed seam 6), and an amendment of SSA1998 s 12(4) |
| 1775 | s 105(6) | sub | inert (reason 2: machinery) | s 105(4)(b), (5), (6): repeal of a definition, additions to JSA Sch 1 paras 9 and 10 (regulation-making powers on whether a payment is recoverable: they feed seam 6), and an amendment of SSA1998 s 12(4) |
| 1776 | s 105(7) | sub | inert (reason 2: machinery) | s 105(7) lead-in: amending words (SSA1998 Sch 3) |
| 1777-1778 | s 105(7) SSA1998 Sch 3 para 6A | host-para | encoded | `s 105(7) SSA1998 Sch 3 para 6A an appeal lies against the decision` |
| 1779-1780 | s 105(7) SSA1998 Sch 3 para 6B | host-para | encoded | `s 105(7) SSA1998 Sch 3 para 6B an appeal lies against the decision` |
| 1781 | s 106 | section | inert (reason 2: machinery) | s 106 section heading and (1) lead-in: amending words (SSAA s 71) |
| 1782 | s 106(1) | sub | inert (reason 2: machinery) | s 106 section heading and (1) lead-in: amending words (SSAA s 71) |
| 1783 | s 106(1) SSAA 71(9A) | sub | encoded | `s 106(1) SSAA 71(9A) the amount may be recovered by deduction from earnings`, `s 106(1) SSAA 71(9B) the payment is earnings` |
| 1784 | s 106(1) SSAA 71(9B) | sub | encoded | `s 106(1) SSAA 71(9A) the amount may be recovered by deduction from earnings`, `s 106(1) SSAA 71(9B) the payment is earnings` |
| 1785 | s 106(1) SSAA 71(9C) | sub | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1786 | s 106(1) SSAA 71(9C)(a) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1787 | s 106(1) SSAA 71(9C)(b) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1788 | s 106(1) SSAA 71(9C)(c) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1789 | s 106(1) SSAA 71(9C)(d) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1790 | s 106(1) SSAA 71(9C)(e) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1791 | s 106(1) SSAA 71(9C)(f) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1792 | s 106(1) SSAA 71(9C)(g) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1793 | s 106(1) SSAA 71(9C)(h) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1794 | s 106(1) SSAA 71(9C)(i) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1795 | s 106(1) SSAA 71(9C)(j) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1796 | s 106(1) SSAA 71(9C)(j)(i) | subpara | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1797 | s 106(1) SSAA 71(9C)(j)(ii) | subpara | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1798 | s 106(1) SSAA 71(9C)(j)(iii) | subpara | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1799 | s 106(2) | sub | inert (reason 2: machinery) | regulation-making power: what regulations under 71(9A) may include (9C)(a)-(j); s 106(2) lead-in |
| 1800 | s 106(2) SSAA 71ZA(2A) | sub | encoded | `s 106(2) SSAA 71ZA(2A) the reference in 71(9A) is read as reaching the amount` |
| 1801 | s 106(3) | sub | inert (reason 2: machinery) | s 106(3) lead-in: amending words (SSAA s 75) |
| 1802 | s 106(3) SSAA 75(8) | sub | encoded | `s 106(3) SSAA 75(8) the amount may be recovered by deduction from earnings` |
| 1803 | s 106(3) SSAA 75(9) | sub | encoded | `s 106(3) SSAA 75(9) the payment is earnings` |
| 1804 | s 106(3) SSAA 75(10) | sub | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1805 | s 106(3) SSAA 75(10)(a) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1806 | s 106(3) SSAA 75(10)(b) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1807 | s 106(3) SSAA 75(10)(c) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1808 | s 106(3) SSAA 75(10)(d) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1809 | s 106(3) SSAA 75(10)(e) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1810 | s 106(3) SSAA 75(10)(f) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1811 | s 106(3) SSAA 75(10)(g) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1812 | s 106(3) SSAA 75(10)(h) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1813 | s 106(3) SSAA 75(10)(i) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1814 | s 106(3) SSAA 75(10)(j) | para | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1815 | s 106(3) SSAA 75(10)(j)(i) | subpara | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1816 | s 106(3) SSAA 75(10)(j)(ii) | subpara | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1817 | s 106(3) SSAA 75(10)(j)(iii) | subpara | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1818 | s 106(4) | sub | inert (reason 2: machinery) | regulation-making power: what regulations under 75(8) may include (10)(a)-(j); s 106(4) lead-in |
| 1819 | s 106(4) SSAA 78(3C) | sub | encoded | `s 106(4) SSAA 78(3C) the amount may be recovered by deduction from earnings` |
| 1820 | s 106(4) SSAA 78(3D) | sub | encoded | `s 106(4) SSAA 78(3D) the payment is earnings` |
| 1821 | s 106(4) SSAA 78(3E) | sub | inert (reason 2: machinery) | regulation-making power: 78(3E) says regulations may include the provision 71(9C) refers to |
| 1822 | s 107 | section | inert (reason 1: not operative) | section heading: not operative |
| 1823 | s 107(1) | sub | encoded | `s 107(1) the exclusion of this benefit from SSAA 71(8) is repealed` |
| 1824 | s 107(2) | sub | encoded | `s 107(2) the exclusion of this benefit from SSA(NI)A 69(8) is repealed` |
| 1825 | s 107(3) | sub | inert (reason 2: machinery) | s 107(3): repeal of paragraphs of Schedule 4 to the Tax Credits Act 2002: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1826 | s 108 | section | inert (reason 1: not operative) | section heading: not operative |
| 1827 | s 108(1) | sub | inert (reason 2: machinery) | s 108(1)-(3) lead-ins: amendment of another Act by words inserted, substituted or repealed: machinery (LA1980 s 38) |
| 1828 | s 108(2) | sub | inert (reason 2: machinery) | s 108(1)-(3) lead-ins: amendment of another Act by words inserted, substituted or repealed: machinery (LA1980 s 38) |
| 1829 | s 108(3) | sub | inert (reason 2: machinery) | s 108(1)-(3) lead-ins: amendment of another Act by words inserted, substituted or repealed: machinery (LA1980 s 38) |
| 1830 | s 108(3) LA1980 38(11) | sub | encoded | `s 108(3) LA1980 38(11) the method of recovery is an “action” for the Limitation Act` |
| 1831 | s 108(3) LA1980 38(11)(a) | para | encoded | `s 108(3) LA1980 38(11) the method of recovery is an “action” for the Limitation Act` |
| 1832 | s 108(3) LA1980 38(11)(b) | para | encoded | `s 108(3) LA1980 38(11) the method of recovery is an “action” for the Limitation Act` |
| 1833-1834 | s 108(3) LA1980 38(11)(c) | para | encoded | `s 108(3) LA1980 38(11) the method of recovery is an “action” for the Limitation Act` |
| 1835 | s 108(4) | sub | encoded | `s 108(4) the amendments apply to the proceedings as if in force from the start` |
| 1836 | heading: Recovery of fines from benefit | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1837 | s 109 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1838 | s 109(1) | sub | inert (reason 2: machinery) | s 109(1) lead-in: amendment of another Act by words inserted, substituted or repealed: machinery (CJA1991 s 24) |
| 1839 | s 109(1)(a) | para | encoded | `s 109 CJA1991 s 24 “income-related” no longer limits the allowance on the day` |
| 1840 | s 109(1)(b) | para | inert (reason 2: machinery) | s 109(1)(b), (2): repeal of a definition and of a paragraph of Schedule 3 to the Welfare Reform Act 2007: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1841 | s 109(2) | sub | inert (reason 2: machinery) | s 109(1)(b), (2): repeal of a definition and of a paragraph of Schedule 3 to the Welfare Reform Act 2007: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1842 | s 109(3) | sub | encoded | `s 109 CJA1991 s 24 “income-related” no longer limits the allowance on the day` (the repeals have effect from 27 October 2008) |
| 1843 | heading: Investigation and prosecution of offences | heading | inert (reason 1: not operative) | cross-heading: not operative |
| 1844-1845 | s 110 | section | inert (reason 2: machinery) | s 110: section heading, lead-in and (a) lead-in: amending words (SSAA 109B(2)) |
| 1846 | s 110(a) | para | inert (reason 2: machinery) | s 110: section heading, lead-in and (a) lead-in: amending words (SSAA 109B(2)) |
| 1847 | s 110(a) SSAA 109B(2)(ia) | para | encoded | `s 110(a) SSAA 109B(2)(ia) the person may be required to supply information for an investigation` |
| 1848 | s 110(b) | para | inert (reason 2: machinery) | s 110(b): a conforming change to paragraph (j): amendment of another Act by words inserted, substituted or repealed: machinery |
| 1849-1850 | s 111 | section | inert (reason 2: machinery) | s 111: time limits for legal proceedings: amendments of SSAA s 116(2) whose text is not among the sources (amendment of another Act by words inserted, substituted or repealed: machinery) |
| 1851 | s 111(a) | para | inert (reason 2: machinery) | s 111: time limits for legal proceedings: amendments of SSAA s 116(2) whose text is not among the sources (amendment of another Act by words inserted, substituted or repealed: machinery) |
| 1852 | s 111(b) | para | inert (reason 2: machinery) | s 111: time limits for legal proceedings: amendments of SSAA s 116(2) whose text is not among the sources (amendment of another Act by words inserted, substituted or repealed: machinery) |
| 1853 | s 112 | section | inert (reason 1: not operative) | section heading: not operative |
| 1854 | s 112(1) | sub | inert (reason 2: machinery) | s 112(1)-(2) lead-ins: amending words (SSAA, after s 116) |
| 1855 | s 112(2) | sub | inert (reason 2: machinery) | s 112(1)-(2) lead-ins: amending words (SSAA, after s 116) |
| 1856 | s 112(2) SSAA 116ZA (heading 116ZA) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 116ZA: not operative |
| 1857 | s 112(2) SSAA 116ZA(1) | sub | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` (the authority administers housing benefit or council tax benefit) |
| 1858 | s 112(2) SSAA 116ZA(2) | sub | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| 1859 | s 112(2) SSAA 116ZA(2)(a) | para | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| 1860 | s 112(2) SSAA 116ZA(2)(b) | para | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| 1861 | s 112(2) SSAA 116ZA(2)(c) | para | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| 1862 | s 112(2) SSAA 116ZA(2)(d) | para | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| 1863 | s 112(2) SSAA 116ZA(2)(e) | para | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| 1864 | s 112(2) SSAA 116ZA(3) | sub | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` (a direction under (3)) |
| 1865 | s 112(2) SSAA 116ZA(4) | sub | encoded | `s 112(2) SSAA 116ZA(4) a direction may relate to the subject` |
| 1866 | s 112(2) SSAA 116ZA(5) | sub | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` (a prescribed condition under (5)) |
| 1867 | s 112(2) SSAA 116ZA(6) | sub | encoded | `s 112(2) SSAA 116ZA(6) the Secretary of State may continue or discontinue the proceedings` |
| 1868 | s 112(2) SSAA 116ZA(6)(a) | para | encoded | `s 112(2) SSAA 116ZA(6) the Secretary of State may continue or discontinue the proceedings` |
| 1869 | s 112(2) SSAA 116ZA(6)(b) | para | encoded | `s 112(2) SSAA 116ZA(6) the Secretary of State may continue or discontinue the proceedings` |
| 1870 | s 112(2) SSAA 116ZA(6)(c) | para | encoded | `s 112(2) SSAA 116ZA(6) the Secretary of State may continue or discontinue the proceedings` |
| 1871 | s 112(2) SSAA 116ZA(6)(d) | para | encoded | `s 112(2) SSAA 116ZA(6) the Secretary of State may continue or discontinue the proceedings` |
| 1872 | s 112(2) SSAA 116ZA(7) | sub | encoded | `s 112(2) SSAA 116ZA(7) the local authority must have regard to the Code for Crown Prosecutors in the decision` |
| 1873 | s 112(2) SSAA 116ZA(7)(a) | para | encoded | `s 112(2) SSAA 116ZA(7) the local authority must have regard to the Code for Crown Prosecutors in the decision` |
| 1874 | s 112(2) SSAA 116ZA(7)(b) | para | encoded | `s 112(2) SSAA 116ZA(7) the local authority must have regard to the Code for Crown Prosecutors in the decision` |
| 1875 | s 112(2) SSAA 116ZA(7)(c) | para | encoded | `s 112(2) SSAA 116ZA(7) the local authority must have regard to the Code for Crown Prosecutors in the decision` |
| 1876 | s 112(2) SSAA 116ZA(7)(d) | para | encoded | `s 112(2) SSAA 116ZA(7) the local authority must have regard to the Code for Crown Prosecutors in the decision` |
| 1877 | s 112(2) SSAA 116ZA(8) | sub | inert (reason 2: machinery) | regulation-making power: regulations shall define "an investigation in respect of a benefit offence" |
| 1878 | s 112(2) SSAA 116ZA(9) | sub | encoded | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` (not in Scotland) |
| 1879 | s 112(3) | sub | inert (reason 2: machinery) | s 112(3)-(6): amendments of SSAA s 116A (words substituted: "unless" to "only if", "must not" to "may", "gives" to "withdraws"): amendment of another Act by words inserted, substituted or repealed: machinery |
| 1880 | s 112(4) | sub | inert (reason 2: machinery) | s 112(3)-(6): amendments of SSAA s 116A (words substituted: "unless" to "only if", "must not" to "may", "gives" to "withdraws"): amendment of another Act by words inserted, substituted or repealed: machinery |
| 1881 | s 112(5) | sub | inert (reason 2: machinery) | s 112(3)-(6): amendments of SSAA s 116A (words substituted: "unless" to "only if", "must not" to "may", "gives" to "withdraws"): amendment of another Act by words inserted, substituted or repealed: machinery |
| 1882 | s 112(5)(a) | para | inert (reason 2: machinery) | s 112(3)-(6): amendments of SSAA s 116A (words substituted: "unless" to "only if", "must not" to "may", "gives" to "withdraws"): amendment of another Act by words inserted, substituted or repealed: machinery |
| 1883 | s 112(5)(b) | para | inert (reason 2: machinery) | s 112(3)-(6): amendments of SSAA s 116A (words substituted: "unless" to "only if", "must not" to "may", "gives" to "withdraws"): amendment of another Act by words inserted, substituted or repealed: machinery |
| 1884 | s 112(6) | sub | inert (reason 2: machinery) | s 112(3)-(6): amendments of SSAA s 116A (words substituted: "unless" to "only if", "must not" to "may", "gives" to "withdraws"): amendment of another Act by words inserted, substituted or repealed: machinery |
| 1885 | heading: Penalties as alternative to prosecution | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1886 | s 113 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1887 | s 113(1) | sub | inert (reason 2: machinery) | s 113(1)-(2) lead-ins: amending words (SSAA s 115A) |
| 1888 | s 113(2) | sub | inert (reason 2: machinery) | s 113(1)-(2) lead-ins: amending words (SSAA s 115A) |
| 1889 | s 113(2) SSAA 115A(1A) | sub | encoded | `s 113(2) SSAA 115A(1A) the penalty provision also applies` |
| 1890 | s 113(2) SSAA 115A(1A)(a) | para | encoded | `s 113(2) SSAA 115A(1A) the penalty provision also applies` |
| 1891 | s 113(2) SSAA 115A(1A)(b) | para | encoded | `s 113(2) SSAA 115A(1A) the penalty provision also applies` |
| 1892 | s 113(3) | sub | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1893 | s 113(4) | sub | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1894 | s 113(4)(a) | para | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1895 | s 113(4)(b) | para | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1896 | s 113(5) | sub | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1897 | s 113(6) | sub | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1898 | s 113(7) | sub | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1899 | s 113(8) | sub | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1900 | s 113(8)(a) | para | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1901 | s 113(8)(b) | para | inert (reason 2: machinery) | s 113(3)-(8): conforming amendments to SSAA 115A and to ss 6B, 6C, 8 and 9 of the Social Security Fraud Act 2001: amendment of another Act by words inserted, substituted or repealed: machinery |
| 1902 | s 114 | section | inert (reason 1: not operative) | s 114 section heading: not operative; the (1) lead-in is amending words |
| 1903 | s 114(1) | sub | inert (reason 1: not operative) | s 114 section heading: not operative; the (1) lead-in is amending words |
| 1904 | s 114(1) SSAA 115A(3) | sub | encoded | `s 114(1) SSAA 115A(3) the amount of the penalty` |
| 1905 | s 114(1) SSAA 115A(3)(a) | para | encoded | `s 114(1) SSAA 115A(3) the amount of the penalty` |
| 1906 | s 114(1) SSAA 115A(3)(b) | para | encoded | `s 114(1) SSAA 115A(3) the amount of the penalty` |
| 1907 | s 114(1) SSAA 115A(3A) | sub | encoded | `s 114(1) SSAA 115A(3A) the amount of the penalty in a case within subsection (1A)` |
| 1908 | s 114(1) SSAA 115A(3B) | sub | inert (reason 2: machinery) | order-making power: the Secretary of State may by order amend the percentage and the figures (115A(3B)); parliamentary control of orders (s 114(2)) |
| 1909 | s 114(1) SSAA 115A(3B)(a) | para | inert (reason 2: machinery) | order-making power: the Secretary of State may by order amend the percentage and the figures (115A(3B)); parliamentary control of orders (s 114(2)) |
| 1910 | s 114(1) SSAA 115A(3B)(b) | para | inert (reason 2: machinery) | order-making power: the Secretary of State may by order amend the percentage and the figures (115A(3B)); parliamentary control of orders (s 114(2)) |
| 1911 | s 114(2) | sub | inert (reason 2: machinery) | order-making power: the Secretary of State may by order amend the percentage and the figures (115A(3B)); parliamentary control of orders (s 114(2)) |
| 1912 | s 114(2) SSAA 190(1)(zza) | para | inert (reason 2: machinery) | order-making power: the Secretary of State may by order amend the percentage and the figures (115A(3B)); parliamentary control of orders (s 114(2)) |
| 1913 | s 115 | section | inert (reason 1: not operative) | s 115 section heading: not operative; the (1) lead-in is amending words |
| 1914 | s 115(1) | sub | inert (reason 1: not operative) | s 115 section heading: not operative; the (1) lead-in is amending words |
| 1915 | s 115(2) | sub | fork | fork F2 (the unit and the first day of the 14): `s 115(2) SSAA 115A(5) the agreement is withdrawn within the cooling-off period`, `s 115(2) the permission to withdraw the agreement` |
| 1916 | s 115(3) | sub | fork | fork F2 (the unit and the first day of the 14): `s 115(3) SSAA 115B(6) the agreement is withdrawn within the cooling-off period` |
| 1917 | heading: Civil penalties | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1918 | s 116 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1919 | s 116(1) | sub | inert (reason 2: machinery) | s 116(1) lead-in: amending words (inserts 115C and 115D into SSAA); the cross-heading and the heading of 115C are not operative |
| 1920 | heading: Civil penalties | heading | inert (reason 2: machinery) | s 116(1) lead-in: amending words (inserts 115C and 115D into SSAA); the cross-heading and the heading of 115C are not operative |
| 1921 | s 116(1) SSAA 115C (heading 115C) | host-heading | inert (reason 2: machinery) | s 116(1) lead-in: amending words (inserts 115C and 115D into SSAA); the cross-heading and the heading of 115C are not operative |
| 1922 | s 116(1) SSAA 115C(1) | sub | encoded | `s 116(1) SSAA 115C(1) the section applies` |
| 1923 | s 116(1) SSAA 115C(1)(a) | para | encoded | `s 116(1) SSAA 115C(1) the section applies` |
| 1924 | s 116(1) SSAA 115C(1)(a)(i) | subpara | encoded | `s 116(1) SSAA 115C(1) the section applies` |
| 1925 | s 116(1) SSAA 115C(1)(a)(ii) | subpara | encoded | `s 116(1) SSAA 115C(1) the section applies` |
| 1926 | s 116(1) SSAA 115C(1)(b) | para | encoded | `s 116(1) SSAA 115C(1) the section applies` |
| 1927 | s 116(1) SSAA 115C(1)(c) | para | encoded | `s 116(1) SSAA 115C(1) the section applies` |
| 1928 | s 116(1) SSAA 115C(1)(d) | para | encoded | `s 116(1) SSAA 115C(1) the section applies` |
| 1929 | s 116(1) SSAA 115C(2) | sub | encoded | `s 116(1) SSAA 115C(2)(a) a penalty may be imposed on the person` |
| 1930 | s 116(1) SSAA 115C(2)(a) | para | encoded | `s 116(1) SSAA 115C(2)(a) a penalty may be imposed on the person` |
| 1931 | s 116(1) SSAA 115C(2)(b) | para | encoded | `s 116(1) SSAA 115C(2)(b) a penalty may be imposed on the other joint claimant instead` |
| 1932 | s 116(1) SSAA 115C(3) | sub | encoded | `s 116(1) SSAA 115C(2)(b) a penalty may be imposed on the other joint claimant instead` |
| 1933 | s 116(1) SSAA 115C(4) | sub | encoded | `s 116(1) SSAA 115C(4) the penalty is recoverable from the person` |
| 1934 | s 116(1) SSAA 115C(5) | sub | encoded | `s 116(1) SSAA 115C(5) the penalty may be recovered in this way` |
| 1935 | s 116(1) SSAA 115C(6) | sub | encoded | `s 116(1) SSAA 115C(6) the body is the appropriate authority` |
| 1936 | s 116(1) SSAA 115C(6) “appropriate authority” | defterm | encoded | `s 116(1) SSAA 115C(6) the body is the appropriate authority` |
| 1937 | s 116(1) SSAA 115C(6) "appropriate authority" item 1 | listitem | encoded | `s 116(1) SSAA 115C(6) the body is the appropriate authority` |
| 1938 | s 116(1) SSAA 115C(6) "appropriate authority" item 2 | listitem | encoded | `s 116(1) SSAA 115C(6) the body is the appropriate authority` |
| 1939 | s 116(1) SSAA 115C(6) “overpayment” | defterm | encoded | `s 116(1) SSAA 115C(6) the payment is an overpayment` |
| 1940 | s 116(1) SSAA 115C(6) “relevant social security benefit” | defterm | encoded | `s 116(1) SSAA 115C(6) the benefit is a relevant social security benefit` |
| 1941 | s 116(1) SSAA 115D (heading 115D) | host-heading | inert (reason 1: not operative) | heading of inserted SSAA 115D: not operative |
| 1942 | s 116(1) SSAA 115D(1) | sub | encoded | `s 116(1) SSAA 115D(1) a penalty may be imposed for failing to provide information` |
| 1943 | s 116(1) SSAA 115D(1)(a) | para | encoded | `s 116(1) SSAA 115D(1) a penalty may be imposed for failing to provide information` |
| 1944 | s 116(1) SSAA 115D(1)(b) | para | encoded | `s 116(1) SSAA 115D(1) a penalty may be imposed for failing to provide information` |
| 1945 | s 116(1) SSAA 115D(1)(c) | para | encoded | `s 116(1) SSAA 115D(1) a penalty may be imposed for failing to provide information` |
| 1946 | s 116(1) SSAA 115D(2) | sub | encoded | `s 116(1) SSAA 115D(2) a penalty may be imposed for failing to notify a change of circumstances` |
| 1947 | s 116(1) SSAA 115D(2)(a) | para | encoded | `s 116(1) SSAA 115D(2) a penalty may be imposed for failing to notify a change of circumstances` |
| 1948 | s 116(1) SSAA 115D(2)(b) | para | encoded | `s 116(1) SSAA 115D(2) a penalty may be imposed for failing to notify a change of circumstances` |
| 1949 | s 116(1) SSAA 115D(2)(c) | para | encoded | `s 116(1) SSAA 115D(2) a penalty may be imposed for failing to notify a change of circumstances` |
| 1950 | s 116(1) SSAA 115D(3) | sub | encoded | `s 116(1) SSAA 115D(3) a further penalty may be imposed for the same overpayment` |
| 1951 | s 116(1) SSAA 115D(4) | sub | encoded | `s 116(1) SSAA 115D(4) the penalty is recoverable from the person` |
| 1952 | s 116(1) SSAA 115D(5) | sub | encoded | `s 116(1) SSAA 115D(5) the penalty may be recovered in this way` |
| 1953 | s 116(1) SSAA 115D(6) | sub | encoded | `s 116(1) SSAA 115D(6) the change is a relevant change of circumstances` |
| 1954 | s 116(2) | sub | inert (reason 2: machinery) | s 116(2): parliamentary control of regulations under 115C(2) and 115D(1)-(2): amendment of SSAA s 190 |
| 1955 | s 116(2) SSAA 190(1)(zzb) | para | inert (reason 2: machinery) | s 116(2): parliamentary control of regulations under 115C(2) and 115D(1)-(2): amendment of SSAA s 190 |
| 1956 | heading: Loss of benefit | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1957 | s 117 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 1958 | s 117(1) | sub | inert (reason 2: machinery) | s 117(1)-(2) lead-ins: amending words (SSFA 6A(1)) |
| 1959 | s 117(2) | sub | inert (reason 2: machinery) | s 117(1)-(2) lead-ins: amending words (SSFA 6A(1)) |
| 1960 | s 117(2) SSFA 6A(1)(f) | para | encoded | `s 117(2) SSFA 6A(1) the benefit is a disqualifying benefit` |
| 1961 | s 117(2) SSFA 6A(1)(g) | para | encoded | `s 117(2) SSFA 6A(1) the benefit is a disqualifying benefit` |
| 1962 | s 117(3) | sub | inert (reason 2: machinery) | s 117(3) lead-in: amending words (SSFA 6A(1)) |
| 1963 | s 117(3) SSFA 6A(1)(fa) | para | encoded | `s 117(3) SSFA 6A(1) the benefit is a sanctionable benefit` |
| 1964 | s 117(3) SSFA 6A(1)(fb) | para | encoded | `s 117(3) SSFA 6A(1) the benefit is a sanctionable benefit` |
| 1965 | s 118 | section | inert (reason 1: not operative) | section heading: not operative |
| 1966 | s 118(1) | sub | inert (reason 2: machinery) | s 118(1)-(4) lead-ins and the substitution in SSFA 6B(11): amending words (its effect is carried by the 6B(11A) function) |
| 1967 | s 118(2) | sub | inert (reason 2: machinery) | s 118(1)-(4) lead-ins and the substitution in SSFA 6B(11): amending words (its effect is carried by the 6B(11A) function) |
| 1968 | s 118(3) | sub | inert (reason 2: machinery) | s 118(1)-(4) lead-ins and the substitution in SSFA 6B(11): amending words (its effect is carried by the 6B(11A) function) |
| 1969 | s 118(4) | sub | inert (reason 2: machinery) | s 118(1)-(4) lead-ins and the substitution in SSFA 6B(11): amending words (its effect is carried by the 6B(11A) function) |
| 1970 | s 118(4) SSFA 6B(11A) | sub | encoded | `s 118(4) SSFA 6B(11A) the relevant period`, `s 118(4) SSFA 6B(11A) the last day of the relevant period` |
| 1971 | s 118(4) SSFA 6B(11A)(a) | para | fork | fork F5 (counting a period of years or weeks, first and last day included): `s 118(4) SSFA 6B(11A) the relevant period`, `s 118(4) SSFA 6B(11A) the last day of the relevant period` |
| 1972 | s 118(4) SSFA 6B(11A)(b) | para | fork | fork F5 (counting a period of years or weeks, first and last day included): `s 118(4) SSFA 6B(11A) the relevant period`, `s 118(4) SSFA 6B(11A) the last day of the relevant period` |
| 1973 | s 118(4) SSFA 6B(11A)(c) | para | fork | fork F5 and F6 (counting a period; a caution that s 121 repeals): `s 118(4) SSFA 6B(11A) the relevant period`, `s 121(1)(c) SSFA 6B(1)(c) a caution is a ground for the loss of benefit` |
| 1974 | s 118(5) | sub | inert (reason 2: machinery) | s 118(5) lead-in: amending words (SSFA 6B) |
| 1975 | s 118(5) SSFA 6B(14) | sub | encoded | `s 118(5) SSFA 6B(14) the offence is a relevant offence` |
| 1976 | s 118(5) SSFA 6B(14)(a) | para | fork | fork F3 ("in England and Wales": where the proceedings are brought, or where the offence was committed): `s 118(5) SSFA 6B(14)(a) the offence is the common law offence of conspiracy to defraud in England and Wales` |
| 1977 | s 118(5) SSFA 6B(14)(b) | para | encoded | `s 118(5) SSFA 6B(14)(b) the offence is a prescribed offence of the kind that is a relevant offence` |
| 1978 | s 118(5) SSFA 6B(14)(b)(i) | subpara | encoded | `s 118(5) SSFA 6B(14)(b)(i) the court found an overpayment of at least 50,000 pounds` |
| 1979 | s 118(5) SSFA 6B(14)(b)(ii) | subpara | encoded | `s 118(5) SSFA 6B(14)(b)(ii) the sentence is a custodial sentence of at least one year` |
| 1980 | s 118(5) SSFA 6B(14)(b)(iii) | subpara | encoded | `s 118(5) SSFA 6B(14)(b)(iii) the court found the offence to have been committed over at least two years` |
| 1981 | s 118(6) | sub | inert (reason 2: machinery) | s 118(6) lead-in and SSFA 6B(15): order-making power (the Secretary of State may amend the periods and amounts) |
| 1982 | s 118(6) SSFA 6B(15) | sub | inert (reason 2: machinery) | s 118(6) lead-in and SSFA 6B(15): order-making power (the Secretary of State may amend the periods and amounts) |
| 1983 | s 118(7) | sub | inert (reason 2: machinery) | s 118(7) lead-in: amending words (SSFA 7) |
| 1984 | s 118(7) SSFA 7(1A) | sub | encoded | `s 118(7) SSFA 7(1A) the restrictions in section 7 do not apply` |
| 1985 | s 118(8) | sub | inert (reason 2: machinery) | s 118(8): amendments of SSFA 11 (the heading, the list of regulations in 11(3)(e), and the words in 11(4)): regulation-making machinery |
| 1986 | s 118(8)(a) | para | inert (reason 2: machinery) | s 118(8): amendments of SSFA 11 (the heading, the list of regulations in 11(3)(e), and the words in 11(4)): regulation-making machinery |
| 1987 | s 118(8)(b) | para | inert (reason 2: machinery) | s 118(8): amendments of SSFA 11 (the heading, the list of regulations in 11(3)(e), and the words in 11(4)): regulation-making machinery |
| 1988 | s 118(8)(b) SSFA 11(3)(e) | para | inert (reason 2: machinery) | s 118(8): amendments of SSFA 11 (the heading, the list of regulations in 11(3)(e), and the words in 11(4)): regulation-making machinery |
| 1989 | s 118(8)(c) | para | inert (reason 2: machinery) | s 118(8): amendments of SSFA 11 (the heading, the list of regulations in 11(3)(e), and the words in 11(4)): regulation-making machinery |
| 1990 | s 119 | section | inert (reason 1: not operative) | section heading: not operative |
| 1991 | s 119(1) | sub | inert (reason 2: machinery) | s 119(1)-(5) lead-ins and the substitutions in SSFA 6B(3) and the heading of section 7: amending words |
| 1992 | s 119(2) | sub | inert (reason 2: machinery) | s 119(1)-(5) lead-ins and the substitutions in SSFA 6B(3) and the heading of section 7: amending words |
| 1993 | s 119(3) | sub | inert (reason 2: machinery) | s 119(1)-(5) lead-ins and the substitutions in SSFA 6B(3) and the heading of section 7: amending words |
| 1994 | s 119(4) | sub | inert (reason 2: machinery) | s 119(1)-(5) lead-ins and the substitutions in SSFA 6B(3) and the heading of section 7: amending words |
| 1995 | s 119(5) | sub | inert (reason 2: machinery) | s 119(1)-(5) lead-ins and the substitutions in SSFA 6B(3) and the heading of section 7: amending words |
| 1996 | s 119(5) SSFA 7(1)(a) | para | encoded | `s 119(5) SSFA 7(1) the conditions in paragraphs (a) to (e) are met`, `s 119(5) SSFA 7(1)(b) the earlier disqualifying event`, `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence`, `s 119(5) SSFA 7(1)(b) the most recent of the dates` |
| 1997 | s 119(5) SSFA 7(1)(b) | para | fork | fork F4 (the five years ending on the offence date: whether the day five years earlier is inside): `s 119(5) SSFA 7(1)(b) the earlier disqualifying event`, `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence` |
| 1998 | s 119(5) SSFA 7(1)(c) | para | encoded | `s 119(5) SSFA 7(1) the conditions in paragraphs (a) to (e) are met`, `s 119(5) SSFA 7(1)(b) the earlier disqualifying event`, `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence`, `s 119(5) SSFA 7(1)(b) the most recent of the dates` |
| 1999 | s 119(5) SSFA 7(1)(d) | para | encoded | `s 119(5) SSFA 7(1) the conditions in paragraphs (a) to (e) are met`, `s 119(5) SSFA 7(1)(b) the earlier disqualifying event`, `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence`, `s 119(5) SSFA 7(1)(b) the most recent of the dates` |
| 2000 | s 119(5) SSFA 7(1)(e) | para | encoded | `s 119(5) SSFA 7(1) the conditions in paragraphs (a) to (e) are met`, `s 119(5) SSFA 7(1)(b) the earlier disqualifying event`, `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence`, `s 119(5) SSFA 7(1)(b) the most recent of the dates` |
| 2001 | s 119(6) | sub | encoded | `s 119(6) SSFA 7(6) the disqualification period` |
| 2002 | s 119(7) | sub | inert (reason 2: machinery) | s 119(7) lead-in: amending words (SSFA 7) |
| 2003 | s 119(7) SSFA 7(6A) | sub | encoded | `s 119(7) SSFA 7(6A) the relevant period`, `s 119(7) SSFA 7(6A) the last day of the relevant period` |
| 2004 | s 119(7) SSFA 7(6A)(a) | para | fork | fork F4 and F5 (the five years ending on the earlier event; a period of three years): `s 119(7) SSFA 7(6A) the relevant period`, `s 119(7) SSFA 7(6A) the last day of the relevant period` |
| 2005 | s 119(7) SSFA 7(6A)(b) | para | fork | fork F5 (counting a period of weeks, first and last day included): `s 119(7) SSFA 7(6A) the relevant period`, `s 119(7) SSFA 7(6A) the last day of the relevant period` |
| 2006 | s 119(8) | sub | inert (reason 2: machinery) | s 119(8) lead-in: amending words (SSFA 7) |
| 2007 | s 119(8) SSFA 7(7A) | sub | encoded | `s 119(8) SSFA 7(7A) subsection (7B) applies` |
| 2008 | s 119(8) SSFA 7(7A)(a) | para | encoded | `s 119(8) SSFA 7(7A) subsection (7B) applies` |
| 2009 | s 119(8) SSFA 7(7A)(b) | para | encoded | `s 119(8) SSFA 7(7A) subsection (7B) applies` |
| 2010 | s 119(8) SSFA 7(7A)(c) | para | encoded | `s 119(8) SSFA 7(7A) subsection (7B) applies` |
| 2011 | s 119(8) SSFA 7(7B) | sub | encoded | `s 119(8) SSFA 7(7B) the restriction is to be treated as not imposed` |
| 2012 | s 119(9) | sub | inert (reason 2: machinery) | s 119(9) lead-in: amending words (SSFA 7(8)) |
| 2013 | s 119(9) SSFA 7(8) “appropriate penalty provision” | defterm | encoded | `s 119(9) SSFA 7(8) the provision is the appropriate penalty provision` |
| 2014 | s 119(9) SSFA 7(8) “disqualifying event” | defterm | encoded | `s 119(9) SSFA 7(8) the event is a disqualifying event` |
| 2015 | s 119(10) | sub | inert (reason 2: machinery) | s 119(10) lead-in: amending words (SSFA 7) |
| 2016 | s 119(10) SSFA 7(8A) | sub | encoded | `s 119(10) SSFA 7(8A) the number of disqualifying events in the set of proceedings`, `s 119(10) SSFA 7(8A)(a) subsection (1)(b) is satisfied`, `s 119(10) SSFA 7(8A)(b) the event is taken into account for the purposes of subsection (1)(d)` |
| 2017 | s 119(10) SSFA 7(8A)(a) | para | fork | fork F4 (the five years ending on the offence date): `s 119(10) SSFA 7(8A)(a) subsection (1)(b) is satisfied` |
| 2018 | s 119(10) SSFA 7(8A)(b) | para | encoded | `s 119(10) SSFA 7(8A) the number of disqualifying events in the set of proceedings`, `s 119(10) SSFA 7(8A)(a) subsection (1)(b) is satisfied`, `s 119(10) SSFA 7(8A)(b) the event is taken into account for the purposes of subsection (1)(d)` |
| 2019 | s 119(10) SSFA 7(8A)(c) | para | encoded | `s 119(7) SSFA 7(6A) the relevant period` (7(8A)(c) and (d) are carried by its two lists of dates) |
| 2020 | s 119(10) SSFA 7(8A)(d) | para | encoded | `s 119(7) SSFA 7(6A) the relevant period` (7(8A)(c) and (d) are carried by its two lists of dates) |
| 2021 | s 119(11) | sub | inert (reason 2: machinery) | s 119(11)-(12): lead-ins, the order-making power in SSFA 7(10A)-(10B), and the amendment of SSFA 11(3)(f): machinery |
| 2022 | s 119(11) SSFA 7(10A) | sub | inert (reason 2: machinery) | s 119(11)-(12): lead-ins, the order-making power in SSFA 7(10A)-(10B), and the amendment of SSFA 11(3)(f): machinery |
| 2023 | s 119(11) SSFA 7(10B) | sub | inert (reason 2: machinery) | s 119(11)-(12): lead-ins, the order-making power in SSFA 7(10A)-(10B), and the amendment of SSFA 11(3)(f): machinery |
| 2024 | s 119(12) | sub | inert (reason 2: machinery) | s 119(11)-(12): lead-ins, the order-making power in SSFA 7(10A)-(10B), and the amendment of SSFA 11(3)(f): machinery |
| 2025 | s 119(12) SSFA 11(3)(f) | para | inert (reason 2: machinery) | s 119(11)-(12): lead-ins, the order-making power in SSFA 7(10A)-(10B), and the amendment of SSFA 11(3)(f): machinery |
| 2026 | s 120 | section | inert (reason 1: not operative) | section heading: not operative |
| 2027 | s 120(1) | sub | inert (reason 2: machinery) | s 120(1)-(2) lead-ins: amending words (TCA after section 36); the cross-heading and the heading of 36A are not operative |
| 2028 | s 120(2) | sub | inert (reason 2: machinery) | s 120(1)-(2) lead-ins: amending words (TCA after section 36); the cross-heading and the heading of 36A are not operative |
| 2029 | heading: Loss of tax credit provisions | heading | inert (reason 2: machinery) | s 120(1)-(2) lead-ins: amending words (TCA after section 36); the cross-heading and the heading of 36A are not operative |
| 2030 | s 120(2) TCA 36A (heading 36A) | host-heading | inert (reason 2: machinery) | s 120(1)-(2) lead-ins: amending words (TCA after section 36); the cross-heading and the heading of 36A are not operative |
| 2031 | s 120(2) TCA 36A(1) | sub | encoded | `s 120(2) TCA 36A(1) subsection (4) applies by virtue of subsection (1)` |
| 2032 | s 120(2) TCA 36A(1)(a) | para | encoded | `s 120(2) TCA 36A(1) subsection (4) applies by virtue of subsection (1)` |
| 2033 | s 120(2) TCA 36A(1)(b) | para | encoded | `s 120(2) TCA 36A(1)(b) the person agreed to pay a penalty as the paragraph describes` |
| 2034 | s 120(2) TCA 36A(1)(c) | para | fork | fork F6 (a caution that s 121(2) repeals): `s 120(2) TCA 36A(1) subsection (4) applies by virtue of subsection (1)`, `s 121(2) TCA 36A(1)(c) a caution is a ground for subsection (4)` |
| 2035 | s 120(2) TCA 36A(2) | sub | encoded | `s 120(2) TCA 36A(2)(a) the provision is the appropriate penalty provision` |
| 2036 | s 120(2) TCA 36A(2)(a) | para | encoded | `s 120(2) TCA 36A(2)(a) the provision is the appropriate penalty provision` |
| 2037 | s 120(2) TCA 36A(2)(b) | para | encoded | `s 120(2) TCA 36A(2)(b) the body is an appropriate authority in relation to the provision` |
| 2038 | s 120(2) TCA 36A(2)(b)(i) | subpara | encoded | `s 120(2) TCA 36A(2)(b) the body is an appropriate authority in relation to the provision` |
| 2039 | s 120(2) TCA 36A(2)(b)(ii) | subpara | encoded | `s 120(2) TCA 36A(2)(b) the body is an appropriate authority in relation to the provision` |
| 2040 | s 120(2) TCA 36A(3) | sub | encoded | `s 120(2) TCA 36A(3) subsection (4) does not apply by virtue of subsection (1)(a)` |
| 2041 | s 120(2) TCA 36A(4) | sub | encoded | `s 120(2) TCA 36A(4) working tax credit is not payable to the person for the day`, `s 120(2) TCA 36A(4)(a) the person is among those to whom working tax credit is not payable` |
| 2042 | s 120(2) TCA 36A(4)(a) | para | encoded | `s 120(2) TCA 36A(4) working tax credit is not payable to the person for the day`, `s 120(2) TCA 36A(4)(a) the person is among those to whom working tax credit is not payable` |
| 2043 | s 120(2) TCA 36A(4)(b) | para | encoded | `s 120(2) TCA 36A(4) working tax credit is not payable to the person for the day`, `s 120(2) TCA 36A(4)(a) the person is among those to whom working tax credit is not payable` |
| 2044 | s 120(2) TCA 36A(5) | sub | inert (reason 2: machinery) | regulation-making power: regulations may reduce the amount payable on a joint claim (36A(5)) |
| 2045 | s 120(2) TCA 36A(6) | sub | encoded | `s 120(2) TCA 36A(6) the disqualification period` |
| 2046 | s 120(2) TCA 36A(7) | sub | encoded | `s 120(2) TCA 36A(7) the relevant period`, `s 120(2) TCA 36A(7) the last day of the relevant period` |
| 2047 | s 120(2) TCA 36A(7)(a) | para | fork | fork F5 (counting a period of years or weeks, first and last day included): `s 120(2) TCA 36A(7) the relevant period`, `s 120(2) TCA 36A(7) the last day of the relevant period` |
| 2048 | s 120(2) TCA 36A(7)(b) | para | fork | fork F5 (counting a period of years or weeks, first and last day included): `s 120(2) TCA 36A(7) the relevant period`, `s 120(2) TCA 36A(7) the last day of the relevant period` |
| 2049 | s 120(2) TCA 36A(7)(c) | para | fork | fork F5 and F6 (counting a period; a caution that s 121(2) repeals): `s 120(2) TCA 36A(7) the relevant period`, `s 121(2) TCA 36A(1)(c) a caution is a ground for subsection (4)` |
| 2050 | s 120(2) TCA 36A(8) | sub | inert (reason 2: machinery) | order-making power (36A(8)); 36A(9) "has effect subject to section 36B" is a precedence pointer, carried by the 36B functions |
| 2051 | s 120(2) TCA 36A(9) | sub | inert (reason 2: machinery) | order-making power (36A(8)); 36A(9) "has effect subject to section 36B" is a precedence pointer, carried by the 36B functions |
| 2052 | s 120(2) TCA 36A(10) | sub | inert (reason 2: machinery) | lead-in to the definitions of 36A(10): scope only; each definition is encoded where it stands |
| 2053 | s 120(2) TCA 36A(10) “benefit offence” | defterm | encoded | `s 120(2) TCA 36A(10) the offence is a benefit offence` |
| 2054 | s 120(2) TCA 36A(10) "benefit offence" item 1 | listitem | encoded | `s 120(2) TCA 36A(10) the offence is a benefit offence` |
| 2055 | s 120(2) TCA 36A(10) "benefit offence" item 2 | listitem | encoded | `s 120(2) TCA 36A(10) the offence is a benefit offence` |
| 2056 | s 120(2) TCA 36A(10) "benefit offence" item 3 | listitem | encoded | `s 120(2) TCA 36A(10) the offence is a benefit offence` |
| 2057 | s 120(2) TCA 36A(10) "benefit offence" item 4 | listitem | encoded | `s 120(2) TCA 36A(10) the offence is a benefit offence` |
| 2058 | s 120(2) TCA 36A(10) “disqualifying benefit” | defterm | encoded | `s 120(2) TCA 36A(10) the benefit is a disqualifying benefit` |
| 2059 | s 120(2) TCA 36A(10) “disqualifying event” | defterm | encoded | `s 120(2) TCA 36A(10) the event is a disqualifying event` |
| 2060 | s 120(2) TCA 36A(10) "disqualifying event" item 1 | listitem | encoded | `s 120(2) TCA 36A(10) the event is a disqualifying event` |
| 2061 | s 120(2) TCA 36A(10) "disqualifying event" item 2 | listitem | encoded | `s 120(2) TCA 36A(10) the event is a disqualifying event` |
| 2062 | s 120(2) TCA 36A(10) "disqualifying event" item 3 | listitem | encoded | `s 120(2) TCA 36A(10) the event is a disqualifying event` |
| 2063 | s 120(2) TCA 36A(10) “relevant offence” | defterm | encoded | `s 120(2) TCA 36A(10) the offence is a relevant offence` |
| 2064 | s 120(2) TCA 36B (heading 36B) | host-heading | inert (reason 1: not operative) | heading of inserted TCA 36B: not operative |
| 2065 | s 120(2) TCA 36B(1) | sub | encoded | `s 120(2) TCA 36B(1) the restriction is to be treated as not imposed` |
| 2066 | s 120(2) TCA 36B(1)(a) | para | encoded | `s 120(2) TCA 36B(1) the restriction is to be treated as not imposed` |
| 2067-2068 | s 120(2) TCA 36B(1)(b) | para | encoded | `s 120(2) TCA 36B(1) the restriction is to be treated as not imposed` |
| 2069 | s 120(2) TCA 36B(2) | sub | encoded | `s 120(2) TCA 36B(2) the restriction is to be treated as not imposed` |
| 2070 | s 120(2) TCA 36B(2)(a) | para | encoded | `s 120(2) TCA 36B(2) the restriction is to be treated as not imposed` |
| 2071-2072 | s 120(2) TCA 36B(2)(b) | para | encoded | `s 120(2) TCA 36B(2) the restriction is to be treated as not imposed` |
| 2073 | s 120(2) TCA 36B(3) | sub | encoded | `s 120(2) TCA 36B(3) section 36A ceases to apply by virtue of the old agreement and subsection (4) applies` |
| 2074 | s 120(2) TCA 36B(3)(a) | para | encoded | `s 120(2) TCA 36B(3) section 36A ceases to apply by virtue of the old agreement and subsection (4) applies` |
| 2075 | s 120(2) TCA 36B(3)(b) | para | encoded | `s 120(2) TCA 36B(3) section 36A ceases to apply by virtue of the old agreement and subsection (4) applies` |
| 2076 | s 120(2) TCA 36B(4) | sub | encoded | `s 120(2) TCA 36B(4) the consequence of the revision`, `s 120(2) TCA 36B(4)(a) the number of days in the reduced disqualification period` |
| 2077 | s 120(2) TCA 36B(4)(a) | para | encoded | `s 120(2) TCA 36B(4) the consequence of the revision`, `s 120(2) TCA 36B(4)(a) the number of days in the reduced disqualification period` |
| 2078 | s 120(2) TCA 36B(4)(a)(i) | subpara | encoded | `s 120(2) TCA 36B(4) the consequence of the revision`, `s 120(2) TCA 36B(4)(a) the number of days in the reduced disqualification period` |
| 2079-2080 | s 120(2) TCA 36B(4)(a)(ii) | subpara | fork | fork F7 (no floor on the reduction of the new disqualification period): `s 120(2) TCA 36B(4)(a) the number of days in the reduced disqualification period` |
| 2081 | s 120(2) TCA 36B(4)(b) | para | encoded | `s 120(2) TCA 36B(4) the consequence of the revision`, `s 120(2) TCA 36B(4)(a) the number of days in the reduced disqualification period` |
| 2082 | s 120(2) TCA 36B(5) | sub | encoded | `s 120(2) TCA 36B(5)(a) the date of the conviction` |
| 2083 | s 120(2) TCA 36B(5)(a) | para | encoded | `s 120(2) TCA 36B(5)(a) the date of the conviction` |
| 2084 | s 120(2) TCA 36B(5)(b) | para | encoded | `s 120(2) TCA 36B(5)(b) the event counts as a conviction for section 36A` |
| 2085 | s 120(2) TCA 36B(5)(b)(i) | subpara | encoded | `s 120(2) TCA 36B(5)(b) the event counts as a conviction for section 36A` |
| 2086 | s 120(2) TCA 36B(5)(b)(ii) | subpara | encoded | `s 120(2) TCA 36B(5)(b) the event counts as a conviction for section 36A` |
| 2087 | s 120(2) TCA 36B(5)(b)(iii) | subpara | encoded | `s 120(2) TCA 36B(5)(b) the event counts as a conviction for section 36A` |
| 2088 | s 120(2) TCA 36B(6) | sub | encoded | `s 120(2) TCA 36B(6) the provision is the appropriate penalty provision` |
| 2089 | s 120(2) TCA 36C (heading 36C) | host-heading | inert (reason 1: not operative) | heading of inserted TCA 36C: not operative |
| 2090 | s 120(2) TCA 36C(1) | sub | encoded | `s 120(2) TCA 36C(1) the restriction in subsection (3) applies` |
| 2091 | s 120(2) TCA 36C(1)(a) | para | encoded | `s 120(2) TCA 36C(1) the restriction in subsection (3) applies` |
| 2092 | s 120(2) TCA 36C(1)(b) | para | fork | fork F4 (the five years ending on the offence date): `s 120(2) TCA 36C(1) the restriction in subsection (3) applies` |
| 2093 | s 120(2) TCA 36C(1)(c) | para | encoded | `s 120(2) TCA 36C(1) the restriction in subsection (3) applies` |
| 2094 | s 120(2) TCA 36C(1)(d) | para | encoded | `s 120(2) TCA 36C(1) the restriction in subsection (3) applies` |
| 2095-2096 | s 120(2) TCA 36C(1)(e) | para | encoded | `s 120(2) TCA 36C(1) the restriction in subsection (3) applies` |
| 2097 | s 120(2) TCA 36C(2) | sub | encoded | `s 120(2) TCA 36C(2) the restriction in subsection (3) does not apply` |
| 2098 | s 120(2) TCA 36C(3) | sub | encoded | `s 120(2) TCA 36C(3) working tax credit is not payable to the person for the day` |
| 2099 | s 120(2) TCA 36C(3)(a) | para | encoded | `s 120(2) TCA 36C(3) working tax credit is not payable to the person for the day` |
| 2100 | s 120(2) TCA 36C(3)(b) | para | encoded | `s 120(2) TCA 36C(3) working tax credit is not payable to the person for the day` |
| 2101 | s 120(2) TCA 36C(4) | sub | inert (reason 2: machinery) | regulation-making power: regulations may reduce the amount payable on a joint claim (36C(4)) |
| 2102 | s 120(2) TCA 36C(5) | sub | encoded | `s 120(2) TCA 36C(5) the disqualification period` |
| 2103 | s 120(2) TCA 36C(6) | sub | encoded | `s 120(2) TCA 36C(6) the relevant period` |
| 2104 | s 120(2) TCA 36C(6)(a) | para | fork | fork F4 and F5 (the five years ending on the earlier event; a period of three years): `s 120(2) TCA 36C(6) the relevant period` |
| 2105 | s 120(2) TCA 36C(6)(b) | para | fork | fork F5 (counting a period of weeks, first and last day included): `s 120(2) TCA 36C(6) the relevant period` |
| 2106 | s 120(2) TCA 36C(7) | sub | inert (reason 2: machinery) | lead-in to the definitions of 36C(7): scope only; each definition is encoded where it stands |
| 2107 | s 120(2) TCA 36C(7) “appropriate penalty provision” | defterm | encoded | `s 120(2) TCA 36C(7) the provision is the appropriate penalty provision` |
| 2108 | s 120(2) TCA 36C(7) “benefit offence” | defterm | encoded | `s 120(2) TCA 36C(7) the offence is a benefit offence` |
| 2109 | s 120(2) TCA 36C(7) "benefit offence" item 1 | listitem | encoded | `s 120(2) TCA 36C(7) the offence is a benefit offence` |
| 2110 | s 120(2) TCA 36C(7) "benefit offence" item 2 | listitem | encoded | `s 120(2) TCA 36C(7) the offence is a benefit offence` |
| 2111 | s 120(2) TCA 36C(7) "benefit offence" item 3 | listitem | encoded | `s 120(2) TCA 36C(7) the offence is a benefit offence` |
| 2112 | s 120(2) TCA 36C(7) "benefit offence" item 4 | listitem | encoded | `s 120(2) TCA 36C(7) the offence is a benefit offence` |
| 2113 | s 120(2) TCA 36C(7) “disqualifying benefit” | defterm | encoded | `s 120(2) TCA 36C(7) the benefit is a disqualifying benefit` |
| 2114 | s 120(2) TCA 36C(7) “disqualifying event” | defterm | encoded | `s 120(2) TCA 36C(7) the event is a disqualifying event` |
| 2115 | s 120(2) TCA 36C(7) “relevant offence” | defterm | encoded | `s 120(2) TCA 36C(7) the offence is a relevant offence` |
| 2116 | s 120(2) TCA 36C(8) | sub | encoded | `s 120(2) TCA 36C(8) the number of disqualifying events in the set of proceedings` |
| 2117 | s 120(2) TCA 36C(8)(a) | para | fork | fork F4 (the five years ending on the offence date): `s 120(2) TCA 36C(8)(a) subsection (1)(b) is satisfied` |
| 2118 | s 120(2) TCA 36C(8)(b) | para | encoded | `s 120(2) TCA 36C(8)(b) the event is taken into account for the purposes of subsection (1)(d)` |
| 2119 | s 120(2) TCA 36C(8)(c) | para | encoded | `s 120(2) TCA 36C(6) the relevant period` (36C(8)(c) and (d) are carried by its two lists of dates) |
| 2120 | s 120(2) TCA 36C(8)(d) | para | encoded | `s 120(2) TCA 36C(6) the relevant period` (36C(8)(c) and (d) are carried by its two lists of dates) |
| 2121 | s 120(2) TCA 36C(9) | sub | inert (reason 2: machinery) | order-making power (36C(9)-(10)); 36C(11) "has effect subject to section 36D" is a precedence pointer, carried by the 36D functions |
| 2122 | s 120(2) TCA 36C(10) | sub | inert (reason 2: machinery) | order-making power (36C(9)-(10)); 36C(11) "has effect subject to section 36D" is a precedence pointer, carried by the 36D functions |
| 2123 | s 120(2) TCA 36C(11) | sub | inert (reason 2: machinery) | order-making power (36C(9)-(10)); 36C(11) "has effect subject to section 36D" is a precedence pointer, carried by the 36D functions |
| 2124 | s 120(2) TCA 36D (heading 36D) | host-heading | inert (reason 1: not operative) | heading of inserted TCA 36D: not operative |
| 2125 | s 120(2) TCA 36D(1) | sub | encoded | `s 120(2) TCA 36D(1) the restriction is to be treated as not imposed` |
| 2126 | s 120(2) TCA 36D(1)(a) | para | encoded | `s 120(2) TCA 36D(1) the restriction is to be treated as not imposed` |
| 2127-2128 | s 120(2) TCA 36D(1)(b) | para | encoded | `s 120(2) TCA 36D(1) the restriction is to be treated as not imposed` |
| 2129 | s 120(2) TCA 36D(2) | sub | encoded | `s 120(2) TCA 36D(2) subsection (3) applies` |
| 2130 | s 120(2) TCA 36D(2)(a) | para | encoded | `s 120(2) TCA 36D(2) subsection (3) applies` |
| 2131 | s 120(2) TCA 36D(2)(b) | para | encoded | `s 120(2) TCA 36D(2) subsection (3) applies` |
| 2132 | s 120(2) TCA 36D(2)(c) | para | encoded | `s 120(2) TCA 36D(2) subsection (3) applies` |
| 2133 | s 120(2) TCA 36D(3) | sub | encoded | `s 120(2) TCA 36D(3) the restriction is to be treated as not imposed` |
| 2134 | s 120(2) TCA 36D(4) | sub | encoded | `s 120(2) TCA 36D(4)(a) the date of the conviction` |
| 2135 | s 120(2) TCA 36D(4)(a) | para | encoded | `s 120(2) TCA 36D(4)(a) the date of the conviction` |
| 2136 | s 120(2) TCA 36D(4)(b) | para | encoded | `s 120(2) TCA 36D(4)(b) the event counts as a conviction for section 36C` |
| 2137 | s 120(2) TCA 36D(4)(b)(i) | subpara | encoded | `s 120(2) TCA 36D(4)(b) the event counts as a conviction for section 36C` |
| 2138 | s 120(2) TCA 36D(4)(b)(ii) | subpara | encoded | `s 120(2) TCA 36D(4)(b) the event counts as a conviction for section 36C` |
| 2139 | s 120(2) TCA 36D(4)(b)(iii) | subpara | encoded | `s 120(2) TCA 36D(4)(b) the event counts as a conviction for section 36C` |
| 2140 | s 120(2) TCA 36D(5) | sub | encoded | `s 120(2) TCA 36D(5) the application counts as a previous application of section 36C` |
| 2141 | s 120(2) TCA 36D(5)(a) | para | encoded | `s 120(2) TCA 36D(5) the application counts as a previous application of section 36C` |
| 2142 | s 120(2) TCA 36D(5)(b) | para | encoded | `s 120(2) TCA 36D(5) the application counts as a previous application of section 36C` |
| 2143 | s 120(3) | sub | inert (reason 2: machinery) | s 120(3) lead-in and (a), (b) lead-in: amending words (TCA 38(1)) |
| 2144 | s 120(3)(a) | para | inert (reason 2: machinery) | s 120(3) lead-in and (a), (b) lead-in: amending words (TCA 38(1)) |
| 2145 | s 120(3)(b) | para | inert (reason 2: machinery) | s 120(3) lead-in and (a), (b) lead-in: amending words (TCA 38(1)) |
| 2146 | s 120(3)(b) TCA 38(1)(ca) | para | encoded | `s 120(3)(b) TCA 38(1)(ca) an appeal lies against the decision` |
| 2147 | s 120(4) | sub | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2148 | s 120(4)(a) | para | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2149 | s 120(4)(a)(i) | subpara | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2150 | s 120(4)(a)(ii) | subpara | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2151 | s 120(4)(b) | para | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2152 | s 120(4)(b) TCA 66(2)(za) | para | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2153 | s 120(4)(b) TCA 66(2)(zb) | para | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2154 | s 120(4)(c) | para | inert (reason 2: machinery) | s 120(4): amendments of TCA 66 (parliamentary control of instruments): machinery |
| 2155 | s 120(5) | sub | inert (reason 2: machinery) | s 120(5) lead-in: amending words (TCA 67) |
| 2156 | s 120(5) TCA 67 “cautioned” | defterm | encoded | `s 120(5) TCA 67 the person is cautioned in relation to the offence` |
| 2157 | s 121 | section | inert (reason 1: not operative) | section heading: not operative |
| 2158 | s 121(1) | sub | inert (reason 2: machinery) | s 121(1) lead-in and (a), (b): amendments of the heading and subsection (1) of SSFA 6B: amending words |
| 2159 | s 121(1)(a) | para | inert (reason 2: machinery) | s 121(1) lead-in and (a), (b): amendments of the heading and subsection (1) of SSFA 6B: amending words |
| 2160 | s 121(1)(b) | para | inert (reason 2: machinery) | s 121(1) lead-in and (a), (b): amendments of the heading and subsection (1) of SSFA 6B: amending words |
| 2161 | s 121(1)(c) | para | fork | fork F6 (a caution that s 121(1)(c) repeals): `s 121(1)(c) SSFA 6B(1)(c) a caution is a ground for the loss of benefit` |
| 2162 | s 121(1)(d) | para | inert (reason 2: machinery) | s 121(1)(d): insertion of "or" in SSFA 6B(13): amending words |
| 2163 | s 121(2) | sub | fork | fork F6 (a caution that s 121(2) repeals): `s 121(2) TCA 36A(1)(c) a caution is a ground for subsection (4)` |
| 2164 | heading: Administration of tax credits | heading | inert (reason 1: not operative) | cross-heading: not operative |
| 2165-2166 | s 122 | section | inert (reason 2: machinery) | s 122 heading and lead-in: amending words (SSAA 109A) |
| 2167 | s 122 SSAA 109A(9) | sub | inert (reason 2: machinery) | SSAA 109A(9) lead-in: the sections apply "as if" (a) and (b), which are encoded below |
| 2168 | s 122 SSAA 109A(9)(a) | para | encoded | `s 122 SSAA 109A(9)(a) the legislation is treated as relevant social security legislation` |
| 2169 | s 122 SSAA 109A(9)(b) | para | encoded | `s 122 SSAA 109A(9)(b) the benefit is treated as a relevant social security benefit for the definition of benefit offence` |
| 2170 | s 123 | section | inert (reason 1: not operative) | section heading: not operative |
| 2171 | s 123(1) | sub | inert (reason 2: machinery) | s 123(1)-(3)(b): amendments of SSAA 122B(2)(a) and (3): amending words |
| 2172 | s 123(2) | sub | inert (reason 2: machinery) | s 123(1)-(3)(b): amendments of SSAA 122B(2)(a) and (3): amending words |
| 2173 | s 123(3) | sub | inert (reason 2: machinery) | s 123(1)-(3)(b): amendments of SSAA 122B(2)(a) and (3): amending words |
| 2174 | s 123(3)(a) | para | inert (reason 2: machinery) | s 123(1)-(3)(b): amendments of SSAA 122B(2)(a) and (3): amending words |
| 2175 | s 123(3)(b) | para | inert (reason 2: machinery) | s 123(1)-(3)(b): amendments of SSAA 122B(2)(a) and (3): amending words |
| 2176-2177 | s 123(3)(c) | para | encoded | `s 123(3)(c) SSAA 122B(3)(d) paragraph (d) is met` |
| 2178 | s 123(3)(c) SSAA 122B(3)(d) | para | encoded | `s 123(3)(c) SSAA 122B(3)(d) paragraph (d) is met` |
| 2179-2180 | s 124 | section | inert (reason 2: machinery) | s 124 heading and lead-in: amending words (TCA 35) |
| 2181 | s 124 TCA 35(2) | sub | encoded | `s 124 TCA 35(2) the mode of trial` |
| 2182 | s 124 TCA 35(3) | sub | encoded | `s 124 TCA 35(3) the greatest punishment on summary conviction for an offence triable summarily only` |
| 2183 | s 124 TCA 35(4) | sub | encoded | `s 124 TCA 35(4) the applicable term` |
| 2184 | s 124 TCA 35(4)(a) | para | encoded | `s 124 TCA 35(4) the applicable term` |
| 2185 | s 124 TCA 35(4)(b) | para | encoded | `s 124 TCA 35(4) the applicable term` |
| 2186 | s 124 TCA 35(5) | sub | encoded | `s 124 TCA 35(2) the mode of trial` |
| 2187 | s 124 TCA 35(6) | sub | encoded | `s 124 TCA 35(6)(a) the greatest punishment on summary conviction for an offence triable either way` |
| 2188 | s 124 TCA 35(6)(a) | para | encoded | `s 124 TCA 35(6)(a) the greatest punishment on summary conviction for an offence triable either way` |
| 2189 | s 124 TCA 35(6)(b) | para | encoded | `s 124 TCA 35(6)(b) the greatest punishment on conviction on indictment` |
| 2190 | s 124 TCA 35(7) | sub | encoded | `s 124 TCA 35(7) the applicable term` |
| 2191 | s 124 TCA 35(7)(a) | para | encoded | `s 124 TCA 35(7) the applicable term` |
| 2192 | s 124 TCA 35(7)(b) | para | encoded | `s 124 TCA 35(7) the applicable term` |
| 2193 | s 124 TCA 35(8) | sub | encoded | `s 124 TCA 35(8) the term as read for an offence committed before commencement` |
| 2194 | s 124 TCA 35(9) | sub | encoded | `s 124 TCA 35(9) the term as read for an offence committed before commencement` |
| 2195 | s 124 TCA 35(10) | sub | inert (reason 2: machinery) | TCA 35(10)-(12): which provisions of SSAA 116 and SSA(NI)A 110 apply to proceedings for the offence: machinery pointing to other Acts |
| 2196 | s 124 TCA 35(10)(a) | para | inert (reason 2: machinery) | TCA 35(10)-(12): which provisions of SSAA 116 and SSA(NI)A 110 apply to proceedings for the offence: machinery pointing to other Acts |
| 2197 | s 124 TCA 35(10)(b) | para | inert (reason 2: machinery) | TCA 35(10)-(12): which provisions of SSAA 116 and SSA(NI)A 110 apply to proceedings for the offence: machinery pointing to other Acts |
| 2198 | s 124 TCA 35(11) | sub | inert (reason 2: machinery) | TCA 35(10)-(12): which provisions of SSAA 116 and SSA(NI)A 110 apply to proceedings for the offence: machinery pointing to other Acts |
| 2199 | s 124 TCA 35(12) | sub | inert (reason 2: machinery) | TCA 35(10)-(12): which provisions of SSAA 116 and SSA(NI)A 110 apply to proceedings for the offence: machinery pointing to other Acts |
| 2200 | s 124 TCA 35(12)(a) | para | inert (reason 2: machinery) | TCA 35(10)-(12): which provisions of SSAA 116 and SSA(NI)A 110 apply to proceedings for the offence: machinery pointing to other Acts |
| 2201 | s 124 TCA 35(12)(b) | para | inert (reason 2: machinery) | TCA 35(10)-(12): which provisions of SSAA 116 and SSA(NI)A 110 apply to proceedings for the offence: machinery pointing to other Acts |
| 2202-2203 | s 125 | section | inert (reason 2: machinery) | s 125 heading and its single sentence: amendment of Part 2 of Schedule 4 to SSAA (adds "the investigation or prosecution of offences relating to tax credits" to paragraph 1): amending words |
| 2204 | s 126 | section | inert (reason 1: not operative) | section heading: not operative |
| 2205 | s 126(1) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2206 | s 126(1)(a) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2207 | s 126(1)(b) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2208 | s 126(2) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2209 | s 126(3) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2210 | s 126(3)(a) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2211 | s 126(3)(b) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2212 | s 126(3)(b)(i) | subpara | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2213 | s 126(3)(b)(ii) | subpara | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2214 | s 126(3)(b)(iii) | subpara | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2215 | s 126(3)(b)(iv) | subpara | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2216 | s 126(4) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2217 | s 126(4)(a) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2218 | s 126(4)(b) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2219 | s 126(5) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2220 | s 126(5)(a) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2221 | s 126(5)(b) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2222 | s 126(6) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2223 | s 126(6)(a) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2224 | s 126(6)(b) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2225 | s 126(7) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2226 | s 126(7)(a) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2227 | s 126(7)(b) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2228 | s 126(7)(c) | para | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2229 | s 126(8) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2230 | s 126(9) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2231 | s 126(10) | sub | inert (reason 2: machinery) | s 126(1)-(10): Order-in-Council powers to transfer tax credit functions and make related provision, their limits (the conditions in (4), the bars in (6)), the consequential provision in (7), the conclusive certificate in (8), the power to amend legislation in (9) and the procedure in (10): regulation-making machinery |
| 2232 | s 126(11) | sub | encoded | `s 126(11) the benefit is a tax credit` |
| 2233 | s 126(12) | sub | inert (reason 2: machinery) | s 126(12): "primary or secondary legislation" means such legislation whenever passed or made: scope of the references in the power, machinery |
| 2234 | s 126(13) | sub | encoded | `s 126(13) the body is the Commissioners` |
| 2235 | s 126(13) “the Commissioners” | defterm | encoded | `s 126(13) the body is the Commissioners` |
| 2236 | s 126(13) “primary legislation” | defterm | encoded | `s 126(13) the legislation is primary legislation` |
| 2237 | s 126(13) “secondary legislation” | defterm | encoded | `s 126(13) the legislation is secondary legislation` |
| 2238 | s 126(13) “tax credit functions” | defterm | encoded | `s 126(13) the function is a tax credit function` |
| 2239 | s 126(14) | sub | inert (reason 2: machinery) | s 126(14): amendment of section 5A(3) of the Ministers of the Crown Act 1975: amending words |
| 2240 | heading: Information-sharing: Secretary of State and HMRC | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2241 | s 127 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2242 | s 127(1) | sub | encoded | `s 127(1) subsection (1) applies to the information` |
| 2243 | s 127(1)(a) | para | encoded | `s 127(1) subsection (1) applies to the information` |
| 2244 | s 127(1)(b) | para | encoded | `s 127(1) subsection (1) applies to the information` |
| 2245 | s 127(2) | sub | encoded | `s 127(2) information held for HMRC functions may be supplied` |
| 2246 | s 127(2)(a) | para | encoded | `s 127(2) information held for HMRC functions may be supplied` |
| 2247-2248 | s 127(2)(b) | para | encoded | `s 127(2) information held for HMRC functions may be supplied` |
| 2249 | s 127(2A) | sub | encoded | `s 127(2A) information held for HMRC functions may be supplied to the Scottish Ministers` |
| 2250 | s 127(3) | sub | encoded | `s 127(3) subsection (3) applies to the information` |
| 2251 | s 127(3)(a) | para | encoded | `s 127(3) subsection (3) applies to the information` |
| 2252 | s 127(3)(b) | para | encoded | `s 127(3) subsection (3) applies to the information` |
| 2253 | s 127(4) | sub | encoded | `s 127(4) information held for departmental functions may be supplied` |
| 2254 | s 127(4)(a) | para | encoded | `s 127(4) information held for departmental functions may be supplied` |
| 2255-2256 | s 127(4)(b) | para | encoded | `s 127(4) information held for departmental functions may be supplied` |
| 2257 | s 127(5) | sub | encoded | `s 127(5) whose authority the recipient needs before supplying the information to another person`, `s 127(5) the recipient may supply the information to another person`, `s 127(5) the prohibition on onward supply` |
| 2258 | s 127(5)(a) | para | encoded | `s 127(5) whose authority the recipient needs before supplying the information to another person`, `s 127(5) the recipient may supply the information to another person`, `s 127(5) the prohibition on onward supply` |
| 2259 | s 127(5)(b) | para | encoded | `s 127(5) whose authority the recipient needs before supplying the information to another person`, `s 127(5) the recipient may supply the information to another person`, `s 127(5) the prohibition on onward supply` |
| 2260 | s 127(5)(c) | para | encoded | `s 127(5) whose authority the recipient needs before supplying the information to another person`, `s 127(5) the recipient may supply the information to another person`, `s 127(5) the prohibition on onward supply` |
| 2261 | s 127(6) | sub | encoded | `s 127(6) it is lawful to use the information for any purposes for which information held for those purposes could be used` |
| 2262 | s 127(7) | sub | inert (reason 2: machinery) | lead-in to the definitions of 127(7): scope only; each definition is encoded where it stands |
| 2263 | s 127(7) “departmental functions” | defterm | encoded | `s 127(7) the function is a departmental function` (the text shows a repealed "or" and omitted words after "employment or training") |
| 2264 | s 127(7) "departmental functions" item 1 | listitem | encoded | `s 127(7) the function is a departmental function` (the text shows a repealed "or" and omitted words after "employment or training") |
| 2265 | s 127(7) "departmental functions" item 2 | listitem | encoded | `s 127(7) the function is a departmental function` (the text shows a repealed "or" and omitted words after "employment or training") |
| 2266 | s 127(7) "departmental functions" item 3 | listitem | encoded | `s 127(7) the function is a departmental function` (the text shows a repealed "or" and omitted words after "employment or training") |
| 2267 | s 127(7) "departmental functions" item 4 | listitem | encoded | `s 127(7) the function is a departmental function` (the text shows a repealed "or" and omitted words after "employment or training") |
| 2268 | s 127(7) “HMRC function” | defterm | encoded | `s 127(7) the function is an HMRC function` (the text shows omitted words after items 1, 2 and 3) |
| 2269 | s 127(7) "HMRC function" item 1 | listitem | encoded | `s 127(7) the function is an HMRC function` (the text shows omitted words after items 1, 2 and 3) |
| 2270 | s 127(7) "HMRC function" item 2 | listitem | encoded | `s 127(7) the function is an HMRC function` (the text shows omitted words after items 1, 2 and 3) |
| 2271 | s 127(7) "HMRC function" item 3 | listitem | encoded | `s 127(7) the function is an HMRC function` (the text shows omitted words after items 1, 2 and 3) |
| 2272 | s 127(7) "HMRC function" item 4 | listitem | encoded | `s 127(7) the function is an HMRC function` (the text shows omitted words after items 1, 2 and 3) |
| 2273 | s 127(7) “Northern Ireland Department” | defterm | encoded | `s 127(7) the department is a Northern Ireland Department` |
| 2274 | s 127(7) "Northern Ireland Department" item 1 | listitem | encoded | `s 127(7) the department is a Northern Ireland Department` |
| 2275 | s 127(7) "Northern Ireland Department" item 2 | listitem | encoded | `s 127(7) the department is a Northern Ireland Department` |
| 2276 | s 127(7) "Northern Ireland Department" item 3 | listitem | encoded | `s 127(7) the department is a Northern Ireland Department` |
| 2277 | s 127(8) | sub | encoded | `s 127(8) the function is treated as relating to social security` |
| 2278 | s 127(8)(a) | para | encoded | `s 127(8) the function is treated as relating to social security` |
| 2279 | s 127(8)(b) | para | encoded | `s 127(8) the function is treated as relating to social security` |
| 2280 | s 127(8)(c) | para | encoded | `s 127(8) the function is treated as relating to social security` |
| 2281 | s 127(8)(d) | para | encoded | `s 127(8) the function is treated as relating to social security` |
| 2282 | s 127(9) | sub | encoded | `s 127(9) this section does not limit the supply` |
| 2283 | s 127(10) | sub | inert (reason 2: machinery) | s 127(10) lead-in: amending words (SSA1998 3(1A)) |
| 2284 | s 127(10) SSA1998 3(1A)(e) | para | encoded | `s 127(10) SSA1998 3(1A)(e) the purpose is within paragraph (e)` |
| 2285 | heading: Information-sharing: Secretary of State and DPP | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2286 | s 128 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2287 | s 128(1) | sub | encoded | `s 128(1) the Secretary of State may supply the information` |
| 2288 | s 128(2) | sub | encoded | `s 128(2) the person is a person specified in subsection (2)` |
| 2289 | s 128(2)(a) | para | encoded | `s 128(2) the person is a person specified in subsection (2)` |
| 2290 | s 128(2)(b) | para | encoded | `s 128(2) the person is a person specified in subsection (2)` |
| 2291 | s 128(3) | sub | encoded | `s 128(3) the purpose is a purpose specified in subsection (3)` |
| 2292 | s 128(3)(a) | para | encoded | `s 128(3) the purpose is a purpose specified in subsection (3)` |
| 2293 | s 128(3)(b) | para | encoded | `s 128(3) the purpose is a purpose specified in subsection (3)` |
| 2294 | s 128(3)(c) | para | encoded | `s 128(3) the purpose is a purpose specified in subsection (3)` |
| 2295 | s 128(3)(d) | para | encoded | `s 128(3) the purpose is a purpose specified in subsection (3)` |
| 2296 | s 128(4) | sub | encoded | `s 128(1) the Secretary of State may supply the information` (a person providing services to the Secretary of State is a supplier) |
| 2297 | s 128(5) | sub | encoded | `s 128(1) the Secretary of State may supply the information` (the answer is NOTHING, never FALSE, where the supply is not within subsections (1) to (3)) |
| 2298 | s 128(6) | sub | inert (reason 2: machinery) | lead-in to the definitions of 128(6): scope only; each definition is encoded where it stands |
| 2299 | s 128(6) “child support information” | defterm | encoded | `s 128(6) the information is child support information` |
| 2300 | s 128(6) “social security information” | defterm | encoded | `s 128(6) the information is social security information` |
| 2301 | s 128(6) “social security matters” | defterm | encoded | `s 128(6) the matter is a social security matter` |
| 2302 | s 128(6) "social security matters" item 1 | listitem | encoded | `s 128(6) the matter is a social security matter` |
| 2303 | s 128(6) "social security matters" item 2 | listitem | encoded | `s 128(6) the matter is a social security matter` |
| 2304 | s 128(6) "social security matters" item 3 | listitem | encoded | `s 128(6) the matter is a social security matter` |
| 2305 | s 129 | section | inert (reason 1: not operative) | section heading: not operative (the unit includes only its heading line) |
| 2306 | s 129(1) | sub | encoded | `s 129(1) subsection (1) bars the disclosure`, `s 129(1) the bar on disclosure applies to the disclosure`, `s 129(1) the prohibition on disclosure` |
| 2307 | s 129(2) | sub | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2308 | s 129(2)(a) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2309 | s 129(2)(b) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2310 | s 129(2)(c) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2311 | s 129(2)(d) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2312 | s 129(2)(e) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2313 | s 129(2)(e)(i) | subpara | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2314 | s 129(2)(e)(ii) | subpara | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2315 | s 129(2)(e)(iii) | subpara | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2316 | s 129(2)(e)(iv) | subpara | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2317 | s 129(2)(f) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2318 | s 129(2)(g) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2319 | s 129(2)(h) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2320 | s 129(2)(i) | para | encoded | `s 129(2) subsection (1) does not apply to the disclosure` |
| 2321 | s 129(3) | sub | encoded | `s 129(3) subsection (1) does not apply to the information` |
| 2322 | s 129(4) | sub | encoded | `s 129(4) subsection (1) stands unaffected by any other enactment` |
| 2323 | s 129(5) | sub | encoded | `s 129(5) the person commits an offence` |
| 2324 | s 129(6) | sub | encoded | `s 129(6) the person has a defence` |
| 2325 | s 129(6)(a) | para | encoded | `s 129(6) the person has a defence` |
| 2326 | s 129(6)(b) | para | encoded | `s 129(6) the person has a defence` |
| 2327 | s 129(7) | sub | encoded | `s 129(7) the greatest punishment for the offence` |
| 2328 | s 129(7)(a) | para | encoded | `s 129(7) the greatest punishment for the offence` |
| 2329 | s 129(7)(b) | para | encoded | `s 129(7) the greatest punishment for the offence` |
| 2330 | s 129(8) | sub | encoded | `s 129(8) a prosecution may be instituted` |
| 2331 | s 129(9) | sub | encoded | `s 129(9) the term as read for an offence committed before 2 May 2022` |
| 2332 | heading: Information-sharing involving local authorities etc | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2333 | s 130 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2334 | s 130(1) | sub | encoded | `s 130(1) this section applies` |
| 2335 | s 130(2) | sub | encoded | `s 130(2) the information falls within subsection (2)` |
| 2336 | s 130(2)(a) | para | encoded | `s 130(2) the information falls within subsection (2)` |
| 2337 | s 130(2)(b) | para | encoded | `s 130(2) the information falls within subsection (2)` |
| 2338 | s 130(2)(c) | para | encoded | `s 130(2) the information falls within subsection (2)` |
| 2339 | s 130(3) | sub | encoded | `s 130(3) the service is a relevant service` |
| 2340 | s 130(3)(a) | para | encoded | `s 130(3) the service is a relevant service` |
| 2341 | s 130(3)(b) | para | encoded | `s 130(3) the service is a relevant service` |
| 2342 | s 130(3)(c) | para | encoded | `s 130(3) the service is a relevant service` |
| 2343 | s 130(4) | sub | encoded | `s 130(4) the accommodation is hospital accommodation` (the text shows omitted words in paragraph (a)) |
| 2344 | s 130(4)(a) | para | encoded | `s 130(4) the accommodation is hospital accommodation` (the text shows omitted words in paragraph (a)) |
| 2345 | s 130(4)(b) | para | encoded | `s 130(4) the accommodation is hospital accommodation` (the text shows omitted words in paragraph (a)) |
| 2346 | s 130(4)(c) | para | encoded | `s 130(4) the accommodation is hospital accommodation` (the text shows omitted words in paragraph (a)) |
| 2347 | s 130(5) | sub | encoded | `s 130(5) the local authority may use or supply the information` |
| 2348 | s 130(5)(a) | para | encoded | `s 130(5) the local authority may use or supply the information` |
| 2349 | s 130(5)(b) | para | encoded | `s 130(5) the local authority may use or supply the information` |
| 2350 | s 130(6) | sub | encoded | `s 130(6) the person is a person specified in subsection (6)` |
| 2351 | s 130(6)(a) | para | encoded | `s 130(6) the person is a person specified in subsection (6)` |
| 2352 | s 130(6)(b) | para | encoded | `s 130(6) the person is a person specified in subsection (6)` |
| 2353 | s 130(6)(c) | para | encoded | `s 130(6) the person is a person specified in subsection (6)` |
| 2354 | s 130(6)(d) | para | encoded | `s 130(6) the person is a person specified in subsection (6)` |
| 2355 | s 130(6)(e) | para | encoded | `s 130(6) the person is a person specified in subsection (6)` |
| 2356 | s 130(7) | sub | encoded | `s 130(7) the benefit is a relevant benefit` |
| 2357 | s 130(7)(a) | para | encoded | `s 130(7) the benefit is a relevant benefit` |
| 2358 | s 130(7)(b) | para | encoded | `s 130(7) the benefit is a relevant benefit` |
| 2359 | s 130(7)(c) | para | encoded | `s 130(7) the benefit is a relevant benefit` |
| 2360 | s 130(7)(d) | para | encoded | `s 130(7) the benefit is a relevant benefit` |
| 2361 | s 130(8) | sub | encoded | `s 130(8) regulations may prescribe the benefit` |
| 2362 | s 131 | section | inert (reason 1: not operative) | section heading: not operative |
| 2363 | s 131(1) | sub | encoded | `s 131(1) the Secretary of State may supply the information to a qualifying person` |
| 2364 | s 131(2) | sub | encoded | `s 131(2) the qualifying person may supply the information to the Secretary of State` |
| 2365 | s 131(2)(a) | para | encoded | `s 131(2) the qualifying person may supply the information to the Secretary of State` |
| 2366-2367 | s 131(2)(b) | para | encoded | `s 131(2) the qualifying person may supply the information to the Secretary of State` |
| 2368 | s 131(3) | sub | encoded | `s 131(3) the qualifying person may use or supply the information` |
| 2369 | s 131(3)(a) | para | encoded | `s 131(3) the qualifying person may use or supply the information` |
| 2370 | s 131(3)(b) | para | encoded | `s 131(3) the qualifying person may use or supply the information` |
| 2371 | s 131(4) | sub | encoded | `s 131(4) the qualifying person may supply the information to a person who provides qualifying welfare services` |
| 2372 | s 131(5) | sub | encoded | `s 131(5) the services are qualifying welfare services` |
| 2373 | s 131(5)(a) | para | encoded | `s 131(5) the services are qualifying welfare services` |
| 2374-2375 | s 131(5)(b) | para | encoded | `s 131(5) the services are qualifying welfare services` |
| 2376 | s 131(6) | sub | encoded | `s 131(6) regulations may prescribe the purpose for information held by a Welsh body` |
| 2377 | s 131(7) | sub | inert (reason 2: machinery) | lead-in to the definitions of 131(7): scope only; each is encoded where it stands |
| 2378 | s 131(7)(a) | para | encoded | `s 131(7)(a) the information held by the Welsh body is excepted information` |
| 2379 | s 131(7)(a)(i) | subpara | encoded | `s 131(7)(a) the information held by the Welsh body is excepted information` |
| 2380 | s 131(7)(a)(ii) | subpara | encoded | `s 131(7)(a) the information held by the Welsh body is excepted information` |
| 2381 | s 131(7)(b) | para | encoded | `s 131(7)(b) the purpose is an excepted purpose in relation to a Welsh body` |
| 2382 | s 131(7)(b)(i) | subpara | encoded | `s 131(7)(b) the purpose is an excepted purpose in relation to a Welsh body` |
| 2383 | s 131(7)(b)(ii) | subpara | encoded | `s 131(7)(b) the purpose is an excepted purpose in relation to a Welsh body` |
| 2384 | s 131(8) | sub | encoded | `s 131(8) regulations may prescribe the purpose for information held by a Scottish body` |
| 2385 | s 131(9) | sub | inert (reason 2: machinery) | lead-in to the definitions of 131(9): scope only; each is encoded where it stands |
| 2386 | s 131(9)(a) | para | encoded | `s 131(9)(a) the information held by the Scottish body is excepted information` |
| 2387 | s 131(9)(a)(i) | subpara | encoded | `s 131(9)(a) the information held by the Scottish body is excepted information` |
| 2388 | s 131(9)(a)(ii) | subpara | encoded | `s 131(9)(a) the information held by the Scottish body is excepted information` |
| 2389 | s 131(9)(b) | para | encoded | `s 131(9)(b) the purpose is an excepted purpose in relation to a Scottish body` |
| 2390 | s 131(10) | sub | encoded | `s 131(10) subsections (1) to (4) do not apply` |
| 2391 | s 131(11) | sub | encoded | `s 131(11) the person is a qualifying person` |
| 2392 | s 131(11)(a) | para | encoded | `s 131(11) the person is a qualifying person` |
| 2393 | s 131(11)(b) | para | encoded | `s 131(11) the person is a qualifying person` |
| 2394 | s 131(11)(c) | para | encoded | `s 131(11) the person is a qualifying person` |
| 2395 | s 131(11)(d) | para | encoded | `s 131(11) the person is a qualifying person` |
| 2396 | s 131(11)(e) | para | encoded | `s 131(11) the person is a qualifying person` |
| 2397 | s 131(11)(f) | para | encoded | `s 131(11) the person is a qualifying person` |
| 2398 | s 131(11)(g) | para | encoded | `s 131(11) the person is a qualifying person` |
| 2399 | s 131(12) | sub | inert (reason 2: machinery) | lead-in to the definitions of 131(12): scope only; each definition is encoded where it stands |
| 2400 | s 131(12) “council tax” | defterm | encoded | `s 131(12) the tax is council tax` |
| 2401 | s 131(12) “person engaged in the administration of housing benefit” | defterm | encoded | `s 131(12) the person is engaged in the administration of housing benefit` |
| 2402 | s 131(12) "person engaged in the administration of housing benefit" item 1 | listitem | encoded | `s 131(12) the person is engaged in the administration of housing benefit` |
| 2403 | s 131(12) "person engaged in the administration of housing benefit" item 2 | listitem | encoded | `s 131(12) the person is engaged in the administration of housing benefit` |
| 2404 | s 131(12) "person engaged in the administration of housing benefit" item 3 | listitem | encoded | `s 131(12) the person is engaged in the administration of housing benefit` |
| 2405 | s 131(12) “relevant information” | defterm | encoded | `s 131(12) the information is relevant information` |
| 2406 | s 131(12) "relevant information" item 1 | listitem | encoded | `s 131(12) the information is relevant information` |
| 2407 | s 131(12) "relevant information" item 2 | listitem | encoded | `s 131(12) the information is relevant information` |
| 2408 | s 131(12) “relevant social security benefit” | defterm | encoded | `s 131(12) it is a relevant social security benefit` |
| 2409 | s 131(12) "relevant social security benefit" item 1 | listitem | encoded | `s 131(12) it is a relevant social security benefit` |
| 2410 | s 131(12) "relevant social security benefit" item 2 | listitem | encoded | `s 131(12) it is a relevant social security benefit` |
| 2411 | s 131(12) “Scottish body” | defterm | encoded | `s 131(12) the person is a Scottish body` |
| 2412 | s 131(12) "Scottish body" item 1 | listitem | encoded | `s 131(12) the person is a Scottish body` |
| 2413 | s 131(12) "Scottish body" item 2 | listitem | encoded | `s 131(12) the person is a Scottish body` |
| 2414 | s 131(12) "Scottish body" item 3 | listitem | encoded | `s 131(12) the person is a Scottish body` |
| 2415 | s 131(12) "Scottish body" item 4 | listitem | encoded | `s 131(12) the person is a Scottish body` |
| 2416 | s 131(12) “welfare services” | defterm | encoded | `s 131(12) the service is welfare services` |
| 2417 | s 131(12) “Welsh body” | defterm | encoded | `s 131(12) the person is a Welsh body` |
| 2418 | s 131(12) "Welsh body" item 1 | listitem | encoded | `s 131(12) the person is a Welsh body` |
| 2419 | s 131(12) "Welsh body" item 2 | listitem | encoded | `s 131(12) the person is a Welsh body` |
| 2420 | s 131(12) "Welsh body" item 3 | listitem | encoded | `s 131(12) the person is a Welsh body` |
| 2421 | s 131(12) "Welsh body" item 4 | listitem | encoded | `s 131(12) the person is a Welsh body` |
| 2422 | s 132 | section | inert (reason 1: not operative) | section heading: not operative |
| 2423 | s 132(1) | sub | encoded | `s 132(1) the person is guilty of an offence` |
| 2424 | s 132(1)(a) | para | encoded | `s 132(1) the person is guilty of an offence` |
| 2425 | s 132(1)(b) | para | encoded | `s 132(1) the person is guilty of an offence` |
| 2426 | s 132(2) | sub | encoded | `s 132(2) subsection (2) applies to the person` |
| 2427 | s 132(2)(a) | para | encoded | `s 132(2) subsection (2) applies to the person` |
| 2428 | s 132(2)(b) | para | encoded | `s 132(2) subsection (2) applies to the person` |
| 2429 | s 132(2)(c) | para | encoded | `s 132(2) subsection (2) applies to the person` |
| 2430 | s 132(2)(d) | para | encoded | `s 132(2) subsection (2) applies to the person` |
| 2431 | s 132(3) | sub | encoded | `s 132(3) the greatest punishment for the offence` |
| 2432 | s 132(3)(a) | para | encoded | `s 132(3) the greatest punishment for the offence` |
| 2433 | s 132(3)(b) | para | encoded | `s 132(3) the greatest punishment for the offence` |
| 2434 | s 132(4) | sub | encoded | `s 132(4) the disclosure is not an offence under this section` |
| 2435 | s 132(4)(a) | para | encoded | `s 132(4) the disclosure is not an offence under this section` |
| 2436 | s 132(4)(b) | para | encoded | `s 132(4) the disclosure is not an offence under this section` |
| 2437 | s 132(5) | sub | encoded | `s 132(5) the person has a defence` |
| 2438 | s 132(5)(a) | para | encoded | `s 132(5) the person has a defence` |
| 2439 | s 132(5)(b) | para | encoded | `s 132(5) the person has a defence` |
| 2440 | s 132(6) | sub | encoded | `s 132(6) the disclosure is made with lawful authority` |
| 2441 | s 132(7) | sub | inert (reason 2: machinery) | saving: "This section does not affect that section" (SSAA 123); it leaves section 123 as it was, so nothing here changes an answer |
| 2442 | s 132(8) | sub | inert (reason 2: machinery) | regulation-making power: regulations under 131(11)(g) may apply section 132 to persons they prescribe (132(8)) |
| 2443 | s 132(8)(a) | para | inert (reason 2: machinery) | regulation-making power: regulations under 131(11)(g) may apply section 132 to persons they prescribe (132(8)) |
| 2444 | s 132(8)(b) | para | inert (reason 2: machinery) | regulation-making power: regulations under 131(11)(g) may apply section 132 to persons they prescribe (132(8)) |
| 2445 | s 132(9) | sub | encoded | `s 132(9) the term as read for an offence committed before 2 May 2022` |
| 2446 | s 133 | section | inert (reason 1: not operative) | section heading: not operative |
| 2447 | s 133(1) | sub | inert (reason 2: machinery) | lead-in to the definitions of 133(1): scope only; each definition is encoded where it stands |
| 2448 | s 133(1) “benefit” | defterm | encoded | `s 133(1) the thing is a benefit` |
| 2449 | s 133(1) “local authority” | defterm | encoded | `s 133(1) the body is a local authority` |
| 2450 | s 133(1) "local authority" item 1 | listitem | encoded | `s 133(1) the body is a local authority` |
| 2451 | s 133(1) "local authority" item 2 | listitem | encoded | `s 133(1) the body is a local authority` |
| 2452 | s 133(1) "local authority" item 3 | listitem | encoded | `s 133(1) the body is a local authority` |
| 2453 | s 133(1) "local authority" item 4 | listitem | encoded | `s 133(1) the body is a local authority` |
| 2454 | s 133(1) "local authority" item 5 | listitem | encoded | `s 133(1) the body is a local authority` |
| 2455 | s 133(1) "local authority" item 6 | listitem | encoded | `s 133(1) the body is a local authority` |
| 2456 | s 133(1) "local authority" item 7 | listitem | encoded | `s 133(1) the body is a local authority` |
| 2457 | s 133(1) “prescribed” | defterm | encoded | `s 133(1) the matter is prescribed` |
| 2458 | s 133(2) | sub | inert (reason 2: machinery) | regulation-making machinery: the content of the power (133(2)), the form (a statutory instrument, 133(3)) and the parliamentary procedure (annulment, 133(4)) |
| 2459 | s 133(2)(a) | para | inert (reason 2: machinery) | regulation-making machinery: the content of the power (133(2)), the form (a statutory instrument, 133(3)) and the parliamentary procedure (annulment, 133(4)) |
| 2460 | s 133(2)(b) | para | inert (reason 2: machinery) | regulation-making machinery: the content of the power (133(2)), the form (a statutory instrument, 133(3)) and the parliamentary procedure (annulment, 133(4)) |
| 2461 | s 133(3) | sub | inert (reason 2: machinery) | regulation-making machinery: the content of the power (133(2)), the form (a statutory instrument, 133(3)) and the parliamentary procedure (annulment, 133(4)) |
| 2462 | s 133(4) | sub | inert (reason 2: machinery) | regulation-making machinery: the content of the power (133(2)), the form (a statutory instrument, 133(3)) and the parliamentary procedure (annulment, 133(4)) |
| 2463 | s 133(5) | sub | encoded | `s 133(5) the Act that gives the meaning of eligible parish council` |
| 2464 | s 133(6) | sub | inert (reason 2: machinery) | s 133(6): repeal of sections 42, 43 and 69(2)(a) of the Welfare Reform Act 2007: amendment of another Act |
| 2465 | s 133(6)(a) | para | inert (reason 2: machinery) | s 133(6): repeal of sections 42, 43 and 69(2)(a) of the Welfare Reform Act 2007: amendment of another Act |
| 2466 | s 133(6)(b) | para | inert (reason 2: machinery) | s 133(6): repeal of sections 42, 43 and 69(2)(a) of the Welfare Reform Act 2007: amendment of another Act |
| 2467 | heading: Information-sharing: miscellaneous | heading | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2468 | s 134 | section | inert (reason 1: not operative) | cross-heading / section heading: not operative |
| 2469 | s 134(1) | sub | inert (reason 2: machinery) | s 134: amendments of section 72 of the Welfare Reform and Pensions Act 1999 and repeals in Schedule 1 to the Education and Skills Act 2008: amendments of other Acts |
| 2470 | s 134(2) | sub | inert (reason 2: machinery) | s 134: amendments of section 72 of the Welfare Reform and Pensions Act 1999 and repeals in Schedule 1 to the Education and Skills Act 2008: amendments of other Acts |
| 2471 | s 134(3) | sub | inert (reason 2: machinery) | s 134: amendments of section 72 of the Welfare Reform and Pensions Act 1999 and repeals in Schedule 1 to the Education and Skills Act 2008: amendments of other Acts |
| 2472 | s 134(3)(a) | para | inert (reason 2: machinery) | s 134: amendments of section 72 of the Welfare Reform and Pensions Act 1999 and repeals in Schedule 1 to the Education and Skills Act 2008: amendments of other Acts |
| 2473 | s 134(3)(b) | para | inert (reason 2: machinery) | s 134: amendments of section 72 of the Welfare Reform and Pensions Act 1999 and repeals in Schedule 1 to the Education and Skills Act 2008: amendments of other Acts |
| 2474 | s 134(4) | sub | inert (reason 2: machinery) | s 134: amendments of section 72 of the Welfare Reform and Pensions Act 1999 and repeals in Schedule 1 to the Education and Skills Act 2008: amendments of other Acts |


## Fork register (wra4)

A fork is a place where the text can be read two or more ways and the outcomes differ.
Each entry gives the rows it covers (the coverage table points back here by number), the text that licenses each reading, the reading taken, and where it is tested.
F1 to F7 have rows with the disposition `fork`; F8 is a recurring ambiguity whose rows are `encoded` (the function answers only the part the text states).

**F1 s 96A(1): the latest day for the five-year review (line 1573).**
Text: "The Secretary of State must at least once every five years review the sums specified in section 96(5A) ..."
Readings: (a) the next review is due by the fifth anniversary of the last, that day included; (b) it is due before the fifth anniversary, so the day before is the last; (c) the five years run from some date the text does not name.
Taken: (a).
The review is overdue only on days after the fifth anniversary.
`add years` clamps 29 February to 28 February.
Rules: `s 96A(1) the latest day for the next review of the sums`, `s 96A(1) the five-year review is overdue`, `s 96A(1) the duty to review the sums` (regulative).
Tested on both sides of the anniversary in `wra4-tests-ss96-97.l4` and with `#TRACE` in `wra4-tests-regulative.l4`.

**F2 s 115(2), (3): the unit and the first day of the 14 (lines 1915-1916).**
Text: "for “28” there is substituted “14”" in the cooling-off subsections SSAA 115A(5) and 115B(6).
The Act prints a number only: neither the unit nor the day the period starts is printed here, and the amended subsections are not among the sources.
Readings: (a) 14 days counted from the agreement, the day of the agreement being day 0, so a withdrawal on day 14 is within; (b) 14 days counting the day of the agreement as day 1, so day 14 of that count is day 13 of (a); (c) another unit (working days, weeks).
Taken: (a).
A withdrawal after day 14 is `NOTHING` (the text does not say what follows a later withdrawal), not `FALSE`.
Rules: `s 115(2) SSAA 115A(5) the agreement is withdrawn within the cooling-off period`, `s 115(3) SSAA 115B(6) the agreement is withdrawn within the cooling-off period`, `s 115(2) the permission to withdraw the agreement` (regulative, `MAY ... WITHIN 14`).

**F3 s 118(5) SSFA 6B(14)(a): "in England and Wales" (line 1976).**
Text: "(a) in England and Wales, the common law offence of conspiracy to defraud".
Readings: (a) where the proceedings are brought; (b) where the offence was committed; (c) both.
Taken: (a): the conviction record carries the place where the proceedings were brought, and the text does not say whether "in England and Wales" qualifies the offence or the proceedings; Greater London, England outside Greater London and Wales are "England and Wales".
Rule: `s 118(5) SSFA 6B(14)(a) the offence is the common law offence of conspiracy to defraud in England and Wales`.

**F4 the five-year window (lines 1997, 2004, 2017, 2092, 2104, 2117).**
Text: SSFA 7(1)(b), 7(6A)(a), 7(8A)(a) and TCA 36C(1)(b), 36C(6)(a), 36C(8)(a): "within the period of five years ending on" a date.
Readings: (a) an event counts if it is on or before that date and after the day exactly five years earlier, so the window is the five years ending on the date, both ends counted; (b) the day exactly five years earlier is inside as well (five years and a day).
Taken: (a); 29 February is clamped.
Rules: `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence`, `s 119(7) SSFA 7(6A) the relevant period`, `s 119(10) SSFA 7(8A)(a) subsection (1)(b) is satisfied`, `s 120(2) TCA 36C(1) the restriction in subsection (3) applies`, `s 120(2) TCA 36C(6) the relevant period`, `s 120(2) TCA 36C(8)(a) subsection (1)(b) is satisfied`.
Tested at the first day inside the window (an event on 2 January 2020 for an offence on 1 January 2025 is inside), at the day exactly five years earlier (1 January 2020: outside), with no event, and across a leap day (an offence on 29 February 2024: an event on 28 February 2019 is outside, 1 March 2019 is inside).

**F5 counting a period of years or weeks (lines 1971-1973, 2004-2005, 2047-2049, 2105).**
Text: "the period of three years", "13 weeks", "four weeks", "26 weeks".
Readings: (a) the period begins on its first day and both the first and the last day count (the keel's `Period`), so 13 weeks ends on the first day plus 90, four weeks on plus 27, 26 weeks on plus 181, and three years on the day before the third anniversary; (b) the last day is the day after the same count (first plus 91, 28, 182, and the third anniversary).
Taken: (a).
Rules: `s 118(4) SSFA 6B(11A) the last day of the relevant period`, `s 119(7) SSFA 7(6A) the last day of the relevant period`, `s 120(2) TCA 36A(7) the last day of the relevant period`.
Asserted by the last day for a given first day (for 1 January 2025: three years ends 31 December 2027, 13 weeks ends 1 April 2025, four weeks ends 28 January 2025, 26 weeks ends 1 July 2025).

**F6 cautions that the Act both inserts and repeals (lines 1973, 2034, 2049, 2161, 2163).**
Text: s 118(4) inserts SSFA 6B(11A)(c) (four weeks "in a case falling within subsection (1)(b) or (c)"), s 120 inserts TCA 36A(1)(c) and 36A(7)(c) (cautions), and s 121(1)(c) and (2) repeal SSFA 6B(1)(c) and TCA 36A(1)(c) ("subsection (1)(c) (cautions) is repealed").
Readings: (a) encode the printed text of ss 118 and 120 and give the repeal its own rules that answer `JUST FALSE` for a caution as a ground; (b) read the printed paragraphs as already amended (no caution case at all); (c) let the repeal win in every function.
Taken: (a).
The case `s 118(4) SSFA 6B(11A) a case within subsection (1)(c)` therefore exists and gives four weeks, and the seat question `Under section 121(1)(c)` says a caution is not a ground.
A caller who asks about a caution through the seat is told no, as s 121 says; a caller who asks the 6B(11A) rule about case (1)(c) gets the printed answer.
Rules: `s 121(1)(c) SSFA 6B(1)(c) a caution is a ground for the loss of benefit`, `s 121(2) TCA 36A(1)(c) a caution is a ground for subsection (4)`, `s 118(4) SSFA 6B(11A) the relevant period`, `s 120(2) TCA 36A(1) subsection (4) applies by virtue of subsection (1)`, `s 120(2) TCA 36A(7) the relevant period`.

**F7 TCA 36B(4)(a): no floor on the reduction (lines 2079-2080).**
Text: "the disqualification period relating to the new disqualifying event shall be reduced by the number of days in so much of the disqualification period relating to the old agreement as had expired".
Readings: (a) the arithmetic as written: the new period less the days expired, which is negative if more days expired than the new period has; (b) floor the result at zero; (c) the paragraph does not apply when the expired days exceed the new period.
Taken: (a); the text states no floor and none was invented, and the test records the negative result.
Rule: `s 120(2) TCA 36B(4)(a) the number of days in the reduced disqualification period`.

**F8 "all such payments and other adjustments shall be made" (lines 2011, 2068, 2072, 2081, 2128, 2133).**
Text: SSFA 7(7B) and TCA 36B(1), (2), (4)(b), 36D(1), (3).
The passive voice names no one who must make the payments, and sets no deadline and no consequence.
Readings: (a) do not invent an actor: the functions answer only whether "the restriction is to be treated as not imposed"; (b) the Secretary of State or HM Revenue and Customs must make them, inferred from who pays the benefit; (c) the person has a claim against whoever paid.
Taken: (a).
No regulative rule is written for these; the jural-relations table records the holder as the person whose restriction is lifted and the bearer as "not named".
Rules: `s 119(8) SSFA 7(7B) the restriction is to be treated as not imposed`, `s 120(2) TCA 36B(1) the restriction is to be treated as not imposed`, `s 120(2) TCA 36B(2) the restriction is to be treated as not imposed`, `s 120(2) TCA 36D(1) the restriction is to be treated as not imposed`, `s 120(2) TCA 36D(3) the restriction is to be treated as not imposed`.

Not forks (looked at and decided without a choice):
the rounding in SSAA 115A(3) ("rounded down to the nearest whole penny") gives the same outcomes on either reading of the arithmetic, so no fork entry; "exceeds" in s 96(2) is strict; the 12(3A) "only if" reading is the lead's shared reading (seam 8), listed under marginal readings.


## Jural relations (wra4)

One row per provision (or run of provisions) that creates a relation, for the whole range.
Hohfeld's correlatives: a claim-right is matched by a duty; a privilege by a no-right; a power by a liability; an immunity by a disability.
Each relation is stated once in layer 1, from one side, and named neutrally; the table gives both parties.
A provision that creates no relation (a definition, a counting rule, an amendment of another Act, commencement) is listed once as `none`.
Where the text names no holder or no bearer, the table says "not named" and does not supply one.

| provision | relation | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | L4 rule |
| --- | --- | --- | --- | --- |
| s 96(1) | power/liability | the Secretary of State (by regulations: to apply a benefit cap) | a single person or couple whose welfare benefits may be capped (liability) | `s 96(1) a benefit cap is applied to the person's welfare benefits` |
| s 96(2) | power/liability | the Secretary of State (to secure that benefits are reduced when the total exceeds the relevant amount) | the single person or couple whose total entitlement exceeds it (liability) | `s 96(2) the total entitlement to welfare benefits`, `s 96(2) the total entitlement exceeds the relevant amount`, `s 96(2) the greatest reduction the cap can require` |
| s 96(3) | none (counting rule: the reference period) | - | - | `s 96(3) the reference period` |
| s 96(4)(a)-(b) | power/liability | the Secretary of State (regulation-making power) | persons subject to the regulations (liability) | not encoded (inert, reason 2) |
| s 96(4)(c), (5) | power/liability | the Secretary of State (regulations: exceptions; the relevant amount) | persons subject to the cap (liability) | `s 96(1) a benefit cap is applied to the person's welfare benefits`, `s 96(2) the greatest reduction the cap can require` |
| s 96(5A), (5B) | power/liability | the Secretary of State (the annual limit; regulations on figures and rounding) | persons resident in Greater London, or elsewhere (liability) | `s 96(5A) the annual limit`, `s 96(5B)(c) the annual limit divided into reference periods` |
| s 96(6)-(8), (11) | none (blank in this text) | - | - | not encoded (repealed or blank) |
| s 96(9) | immunity/disability | a person who receives a welfare benefit provided for by the devolved legislatures or Welsh Ministers | the Secretary of State (disabled from reducing that benefit by cap regulations) | `s 96(9) benefit cap regulations may reduce this welfare benefit` |
| s 96(10) | none (definitions: welfare benefit, couple, single person, regulations, prescribed) | - | - | `s 96(10) the benefit is a welfare benefit`, `s 96(10) the two persons are a couple`, `s 96(10) the person is a single person`, `s 96(10) regulations made by this maker are regulations`, `s 96(10) the matter is prescribed` |
| s 96A(1) | claim-right/duty | persons whose benefits are capped (nominal: the text names no one entitled to enforce the review) | the Secretary of State (must review the sums at least once every five years) | `s 96A(1) the latest day for the next review of the sums`, `s 96A(1) the five-year review is overdue`, `s 96A(1) the duty to review the sums` |
| s 96A(2) | privilege/no-right | the Secretary of State (may review at any other time) | persons whose benefits are capped (no-right to stop a review) | `s 96A(2) the Secretary of State may review the sums at this time` |
| s 96A(3) | claim-right/duty | persons whose benefits are capped (nominal) | the Secretary of State (must take the national economic situation into account in a review) | `s 96A(3) the review met the requirement to take account of the national economic situation` |
| s 96A(4)-(8) | power/liability | the Secretary of State (regulations amending the sums, with transitional provision) | persons whose benefits are capped (liability) | not encoded (inert, reason 2) |
| s 97(1)-(5) | none (machinery: how the regulations are made and controlled) | - | - | not encoded (inert, reason 2) |
| s 97(6) | immunity/disability | the Secretary of State (immune from appeal against a decision to apply the benefit cap) | the person whose benefits are capped (disabled from appealing) | `s 97(6) SSA1998 Sch 2 para 8A an appeal lies against the decision` |
| s 98(1)-(5) | power/liability | the Secretary of State (regulations about claims and awards, SSAA 5(1)) | claimants (liability) | not encoded (inert, reason 2) |
| s 99(3) SSAA 5(1A) | power/liability | the Secretary of State (by regulations: to require information about claims and awards) | a person of a prescribed description (liability to supply it) | `s 99(3) SSAA 5(1A) regulations may require the person to supply the information` |
| s 99(1), (2), (4), (5) | none (amendments of SSAA 5 and SSA 1998 s 22) | - | - | not encoded (inert, reason 2) |
| s 100 SSAA 5(3B) | power/liability | the Secretary of State (by regulations: to direct payment to one of joint claimants in a way) | persons awarded a benefit jointly (liability) | `s 100 SSAA 5(3B) the Secretary of State may be given power to direct the payment in this way` |
| s 101(1) | power/liability | the Secretary of State (by regulations: to pay on account) | a claimant in need whose claim cannot yet be decided (liability to have the payment recovered under 71ZG) | `s 101(1) SSAA 5(1)(r) regulations may provide for a payment on account in this case` |
| s 101(2) | none (a repeal of an unbrought-into-force provision) | - | - | not encoded (inert, reason 2) |
| s 102(3) SSA1998 12(3A) | power/liability | the claimant (power to appeal, where regulations give a right of appeal) | the Secretary of State / First-tier Tribunal (liability to hear it); the right arises only if revision was considered (seam 8) | `s 102(3) SSA1998 12(3A) there is a right of appeal`, `s 102(2) SSA1998 12(2)(b) there is a right of appeal because regulations so provide` |
| s 102(3) SSA1998 12(3B), (3C) | power/liability | the Secretary of State (by regulations: the further condition for the consideration) | claimants (liability) | `s 102(3) SSA1998 12(3B) the consideration meets the condition the regulations set`, `s 102(3) SSA1998 12(3C) the references to the Secretary of State and regulations are read as the other person's` |
| s 102(4) SSA1998 12(7)(b) | power/liability | the Secretary of State (by regulations: to treat a purported appeal as an application for revision) | the person who purports to appeal (liability) | `s 102(4) SSA1998 12(7)(b) the purported appeal may be treated as an application for revision` |
| s 102(1), (5)-(9) | none (amendments; the list of provisions whose regulations may be made so as to have the effect) | - | - | not encoded (inert, reason 2) |
| s 103 | none (supersession amendments in Schedule 12; commencement of two provisions as from 3 November 2008) | - | - | `s 103(2)(a) the Schedule 12 amendments have effect on the day`, `s 103(2)(b) the regulations have effect on the day` |
| s 104 | none (how a reference in the Electronic Communications Act 2000 is read) | - | - | `s 104(1) SSAA 189(5B) the reference is read as`, `s 104(2) SSA1998 79(6B) the reference is read as` |
| s 105 SSAA 71ZB(1) | power/liability | the Secretary of State (to recover an amount paid in excess of entitlement) | the person overpaid (liability) | `s 105 SSAA 71ZB(1) the amount paid in excess of entitlement`, `s 105 SSAA 71ZB(1)(a) the universal credit paid in excess of entitlement`, `s 105 SSAA 71ZB(1) the Secretary of State may recover an overpayment of the benefit`, `s 105 SSAA 71ZB(1) the benefit is named in the list` |
| s 105 SSAA 71ZB(2) | claim-right/duty | the Secretary of State (claim to the amount) | the person to whom it was paid, and any person regulations prescribe (duty to repay) | `s 105 SSAA 71ZB(2) the amount is recoverable from the person` |
| s 105 SSAA 71ZB(3) | immunity/disability | the person paid under a determination that stands (immune from recovery) | the Secretary of State (disabled from recovering unless the determination was reversed, varied, revised or superseded) | `s 105 SSAA 71ZB(3) the determination does not bar recovery` |
| s 105 SSAA 71ZB(4) | power/liability | the Secretary of State (regulations: to calculate or estimate an amount) | persons overpaid (liability) | not encoded (inert, reason 2) |
| s 105 SSAA 71ZB(5), (6) | power/liability | the Secretary of State (to treat late-paid income as an overpayment; to regard a payment to one joint claimant as paid to the other) | the claimant; the other joint claimant (liability) | `s 105 SSAA 71ZB(5) the amount is treated as paid in excess of entitlement`, `s 105 SSAA 71ZB(6) the amount paid to one of them may be regarded as paid to the other` |
| s 105 SSAA 71ZB(7) | power/liability | the Secretary of State (to recover by deduction from benefit, from earnings, through the courts, or by adjustment) | the person from whom the amount is recoverable (liability) | `s 105 SSAA 71ZB(7) an amount recoverable under 71ZB may be recovered in this way` |
| s 105 SSAA 71ZC(1)-(4) | power/liability | the Secretary of State (to deduct from payments of benefit, and from another person's benefit when the amount was paid on behalf of another) | the debtor (liability); the obligation of the other is discharged to the extent recovered | `s 105 SSAA 71ZC(1) the amount may be recovered by deduction from this payment`, `s 105 SSAA 71ZC(2) the amount paid on behalf of another may be recovered by deduction from this source`, `s 105 SSAA 71ZC(3) the obligation is taken to be discharged by the deduction`, `s 105 SSAA 71ZC(4) the obligation is taken to be discharged by the deduction` |
| s 105 SSAA 71ZD | power/liability | the Secretary of State (by regulations: to recover by deduction from earnings; to require the debtor to disclose the employer; to require the employer to deduct) | the debtor (liability); the employer (duty to deduct once served, 71ZD(3)(b)); the debtor's earnings are protected down to a level the regulations set (71ZD(3)(e)) | `s 105 SSAA 71ZD(1) the amount may be recovered by deduction from earnings`, `s 105 SSAA 71ZD(2) the payment is earnings`, `s 105 SSAA 71ZD(3)(a) the person may be required to disclose details of their employer`, `s 105 SSAA 71ZD(3)(e) the most that may be deducted from the earnings` |
| s 105 SSAA 71ZE | power/liability | the Secretary of State (to enforce through the county court or sheriff court; to recover the costs) | the debtor (liability) | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts`, `s 105 SSAA 71ZE(3) the costs of recovery may be recovered as if recoverable under 71ZB` |
| s 105 SSAA 71ZF | power/liability | the Secretary of State (to recover by adjustment of benefit) | the debtor (liability) | not encoded (inert, reason 2) |
| s 105 SSAA 71ZG | power/liability | the Secretary of State (to recover a payment on account) | the person to whom it was paid, or the other joint claimant (liability) | `s 105 SSAA 71ZG(1) the Secretary of State may recover the payment`, `s 105 SSAA 71ZG(2) the amount is recoverable from the person`, `s 105 SSAA 71ZG(4) the amount paid to one of them may be regarded as paid to the other`, `s 105 SSAA 71ZG(5) the amount may be recovered in this way` |
| s 105 SSAA 71ZH | power/liability | the Secretary of State (to recover a hardship payment or other listed payment) | the person paid, or the other joint claimant (liability) | `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment`, `s 105 SSAA 71ZH(2) the amount is recoverable from the person`, `s 105 SSAA 71ZH(4) the amount paid to one claimant may be regarded as paid to the other`, `s 105 SSAA 71ZH(5) the amount may be recovered in this way` |
| s 105(4) SSAA 115B(4), (4A) | immunity/disability | the recipient who has agreed to pay the penalty (immune from prosecution for the conduct) | the authority (disabled from prosecuting; and its claim to the penalty is a claim-right against the recipient) | `s 105(4) SSAA 115B(4)(a) the penalty is recoverable from the recipient`, `s 105(4) SSAA 115B(4)(b) criminal proceedings may be instituted against the recipient for the conduct`, `s 105(4) SSAA 115B(4A) the penalty may be recovered in this way` |
| s 105(7) SSA1998 Sch 3 para 6A, 6B | power/liability | the person subject to the decision (power to appeal) | the decision-maker / First-tier Tribunal (liability to hear it) | `s 105(7) SSA1998 Sch 3 para 6A an appeal lies against the decision`, `s 105(7) SSA1998 Sch 3 para 6B an appeal lies against the decision` |
| s 105(2), (3), (5), (6) | none (amendments of SSAA 71, 115A, JSA Sch 1, SSA 1998 s 12) | - | - | not encoded (inert, reason 2) |
| s 106 | power/liability | the Secretary of State (by regulations: to recover by deduction from earnings in the other cases; to require deductions by the employer) | the debtor (liability); the employer (duty to deduct, SSAA 71(9C)) | `s 106(1) SSAA 71(9A) the amount may be recovered by deduction from earnings`, `s 106(1) SSAA 71(9B) the payment is earnings`, `s 106(2) SSAA 71ZA(2A) the reference in 71(9A) is read as reaching the amount`, `s 106(3) SSAA 75(8) the amount may be recovered by deduction from earnings`, `s 106(3) SSAA 75(9) the payment is earnings`, `s 106(4) SSAA 78(3C) the amount may be recovered by deduction from earnings`, `s 106(4) SSAA 78(3D) the payment is earnings` |
| s 107 | power/liability | the Secretary of State (to recover child benefit and guardian's allowance by deduction from other benefit) | the person overpaid (liability) | `s 107(1) the exclusion of this benefit from SSAA 71(8) is repealed`, `s 107(2) the exclusion of this benefit from SSA(NI)A 69(8) is repealed` |
| s 108 | immunity/disability | the Secretary of State (immune from the Limitation Act 1980 for these methods of recovery) | the debtor (disabled from pleading the limitation period) | `s 108(3) LA1980 38(11) the method of recovery is an “action” for the Limitation Act`, `s 108(4) the amendments apply to the proceedings as if in force from the start` |
| s 109 | none (amendments of CJA 1991 s 24 and WRA 2007; repeals retrospective to 27 October 2008) | - | - | `s 109 CJA1991 s 24 “income-related” no longer limits the allowance on the day` |
| s 110 SSAA 109B(2)(ia) | power/liability | the Secretary of State (authorised officer: to require information in an investigation) | a person of a prescribed description (liability to give it) | `s 110(a) SSAA 109B(2)(ia) the person may be required to supply information for an investigation` |
| s 111 | none (time limits for legal proceedings: amendments of SSAA 116(2)) | - | - | not encoded (inert, reason 2) |
| s 112 SSAA 116ZA(2), (5) | immunity/disability | the person suspected of a benefit offence (immune from prosecution by a local authority except in the listed cases) | the local authority (disabled from bringing proceedings otherwise) | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| s 112 SSAA 116ZA(3), (4), (6) | power/liability | the Secretary of State (to direct that an authority may not bring proceedings; to continue or discontinue proceedings) | the authority (liability) | `s 112(2) SSAA 116ZA(4) a direction may relate to the subject`, `s 112(2) SSAA 116ZA(6) the Secretary of State may continue or discontinue the proceedings` |
| s 112 SSAA 116ZA(7) | claim-right/duty | the person suspected (nominal: the text names no one entitled to enforce it) | the local authority (must have regard to the Code for Crown Prosecutors) | `s 112(2) SSAA 116ZA(7) the local authority must have regard to the Code for Crown Prosecutors in the decision` |
| s 112 SSAA 116ZA(1), (8), (9) | none (scope; definition by regulations; the section does not apply to Scotland) | - | - | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` |
| s 112(1), (3)-(6) | none (amendments of SSAA 116A) | - | - | not encoded (inert, reason 2) |
| s 113 SSAA 115A(1A) | power/liability | the Secretary of State or the authority (to offer a penalty as an alternative to prosecution where no overpayment resulted) | the person who might be prosecuted (liability to be offered the penalty) | `s 113(2) SSAA 115A(1A) the penalty provision also applies` |
| s 113(1), (3)-(8) | none (amendments of SSAA 115A and SSFA) | - | - | not encoded (inert, reason 2) |
| s 114 SSAA 115A(3), (3A) | power/liability | the Secretary of State or the authority (the penalty is fixed at 50% of the overpayment within limits, or 350 pounds) | the person who agrees to pay it (liability) | `s 114(1) SSAA 115A(3) the amount of the penalty`, `s 114(1) SSAA 115A(3A) the amount of the penalty in a case within subsection (1A)` |
| s 114 SSAA 115A(3B), s 114(2) | power/liability | the Secretary of State (order amending the sums) | persons liable to a penalty | not encoded (inert, reason 2) |
| s 115 | power/liability | the person who agreed to pay a penalty (power to withdraw within the cooling-off period) | the authority (liability: the agreement ends) | `s 115(2) SSAA 115A(5) the agreement is withdrawn within the cooling-off period`, `s 115(3) SSAA 115B(6) the agreement is withdrawn within the cooling-off period`, `s 115(2) the permission to withdraw the agreement` |
| s 116 SSAA 115C(1), (2), (3) | power/liability | the appropriate authority (to impose a civil penalty for a negligent incorrect statement, on the person or the other joint claimant) | the person; the other joint claimant unless unaware (liability) | `s 116(1) SSAA 115C(1) the section applies`, `s 116(1) SSAA 115C(2)(a) a penalty may be imposed on the person`, `s 116(1) SSAA 115C(2)(b) a penalty may be imposed on the other joint claimant instead`, `s 116(1) SSAA 115C(6) the body is the appropriate authority`, `s 116(1) SSAA 115C(6) the payment is an overpayment`, `s 116(1) SSAA 115C(6) the benefit is a relevant social security benefit` |
| s 116 SSAA 115C(4), (5) | claim-right/duty | the appropriate authority (claim to the penalty) | the person penalised (duty to pay); recoverable under 71ZC to 71ZE | `s 116(1) SSAA 115C(4) the penalty is recoverable from the person`, `s 116(1) SSAA 115C(5) the penalty may be recovered in this way` |
| s 116 SSAA 115D(1)-(3) | power/liability | the appropriate authority (to impose a civil penalty for failing to provide information or notify a change) | the person (liability); a person with a reasonable excuse is not liable | `s 116(1) SSAA 115D(1) a penalty may be imposed for failing to provide information`, `s 116(1) SSAA 115D(2) a penalty may be imposed for failing to notify a change of circumstances`, `s 116(1) SSAA 115D(3) a further penalty may be imposed for the same overpayment` |
| s 116 SSAA 115D(4)-(6) | claim-right/duty | the appropriate authority (claim to the penalty) | the person penalised (duty to pay) | `s 116(1) SSAA 115D(4) the penalty is recoverable from the person`, `s 116(1) SSAA 115D(5) the penalty may be recovered in this way`, `s 116(1) SSAA 115D(6) the change is a relevant change of circumstances` |
| s 116(2) | none (amendment of SSAA 190) | - | - | not encoded (inert, reason 2) |
| s 117 | none (definitions: disqualifying benefit, sanctionable benefit) | - | - | `s 117(2) SSFA 6A(1) the benefit is a disqualifying benefit`, `s 117(3) SSFA 6A(1) the benefit is a sanctionable benefit` |
| s 118 SSFA 6B(11A) | none (counting rule: the relevant period) | - | - | `s 118(4) SSFA 6B(11A) the relevant period`, `s 118(4) SSFA 6B(11A) the last day of the relevant period` |
| s 118 SSFA 6B(14) | none (definition: relevant offence) | - | - | `s 118(5) SSFA 6B(14) the offence is a relevant offence`, `s 118(5) SSFA 6B(14)(a) the offence is the common law offence of conspiracy to defraud in England and Wales`, `s 118(5) SSFA 6B(14)(b) the offence is a prescribed offence of the kind that is a relevant offence`, `s 118(5) SSFA 6B(14)(b)(i) the court found an overpayment of at least 50,000 pounds`, `s 118(5) SSFA 6B(14)(b)(ii) the sentence is a custodial sentence of at least one year`, `s 118(5) SSFA 6B(14)(b)(iii) the court found the offence to have been committed over at least two years` |
| s 118 SSFA 7(1A) | immunity/disability | a person convicted of a relevant offence (immune from the section 7 restrictions) | the Secretary of State (disabled from applying them) | `s 118(7) SSFA 7(1A) the restrictions in section 7 do not apply` |
| s 118(1)-(3), (6), (8) | none (amendments; order-making power; loss of benefit regulations) | - | - | not encoded (inert, reason 2) |
| s 119 SSFA 7(1), (6), (6A) | power/liability | the Secretary of State (to withhold benefit for a repeated benefit offence) | the offender (liability to the restriction for the disqualification period) | `s 119(5) SSFA 7(1) the conditions in paragraphs (a) to (e) are met`, `s 119(5) SSFA 7(1)(b) the most recent of the dates`, `s 119(5) SSFA 7(1)(b) the earlier disqualifying event`, `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence`, `s 119(6) SSFA 7(6) the disqualification period`, `s 119(7) SSFA 7(6A) the relevant period`, `s 119(7) SSFA 7(6A) the last day of the relevant period` |
| s 119 SSFA 7(7A), (7B) | claim-right/duty | the person whose restriction is treated as not imposed (claim to the payments and adjustments) | not named: the passive "shall be made" names no one (fork register F8) | `s 119(8) SSFA 7(7A) subsection (7B) applies`, `s 119(8) SSFA 7(7B) the restriction is to be treated as not imposed` |
| s 119 SSFA 7(8), (8A), (10A), (10B) | none (definitions; counting rule; order-making power) | - | - | `s 119(9) SSFA 7(8) the provision is the appropriate penalty provision`, `s 119(9) SSFA 7(8) the event is a disqualifying event`, `s 119(10) SSFA 7(8A) the number of disqualifying events in the set of proceedings`, `s 119(10) SSFA 7(8A)(a) subsection (1)(b) is satisfied`, `s 119(10) SSFA 7(8A)(b) the event is taken into account for the purposes of subsection (1)(d)` |
| s 119(1)-(4), (12) | none (amendments) | - | - | not encoded (inert, reason 2) |
| s 120 TCA 36A(1)-(4), (6), (7) | power/liability | HM Revenue and Customs (working tax credit is not payable during the disqualification period) | the offender entitled to working tax credit (liability) | `s 120(2) TCA 36A(1) subsection (4) applies by virtue of subsection (1)`, `s 120(2) TCA 36A(1)(b) the person agreed to pay a penalty as the paragraph describes`, `s 120(2) TCA 36A(3) subsection (4) does not apply by virtue of subsection (1)(a)`, `s 120(2) TCA 36A(4) working tax credit is not payable to the person for the day`, `s 120(2) TCA 36A(4)(a) the person is among those to whom working tax credit is not payable`, `s 120(2) TCA 36A(6) the disqualification period`, `s 120(2) TCA 36A(7) the relevant period`, `s 120(2) TCA 36A(7) the last day of the relevant period` |
| s 120 TCA 36A(2), (10) | none (definitions: appropriate penalty provision, benefit offence, disqualifying event) | - | - | `s 120(2) TCA 36A(2)(a) the provision is the appropriate penalty provision`, `s 120(2) TCA 36A(2)(b) the body is an appropriate authority in relation to the provision`, `s 120(2) TCA 36A(10) the offence is a benefit offence`, `s 120(2) TCA 36A(10) the benefit is a disqualifying benefit`, `s 120(2) TCA 36A(10) the event is a disqualifying event`, `s 120(2) TCA 36A(10) the offence is a relevant offence` |
| s 120 TCA 36A(5), (8), (9) | power/liability | the Treasury / HM Revenue and Customs (regulations; order amending the periods) | offenders (liability) | not encoded (inert, reason 2) |
| s 120 TCA 36B(1)-(4) | claim-right/duty | the person whose restriction is treated as not imposed (claim to the payments and adjustments) | not named: the passive "shall be made" names no one (fork register F8) | `s 120(2) TCA 36B(1) the restriction is to be treated as not imposed`, `s 120(2) TCA 36B(2) the restriction is to be treated as not imposed`, `s 120(2) TCA 36B(3) section 36A ceases to apply by virtue of the old agreement and subsection (4) applies`, `s 120(2) TCA 36B(4) the consequence of the revision`, `s 120(2) TCA 36B(4)(a) the number of days in the reduced disqualification period` |
| s 120 TCA 36B(5), (6) | none (definitions: the date of a conviction; what counts as a conviction) | - | - | `s 120(2) TCA 36B(5)(a) the date of the conviction`, `s 120(2) TCA 36B(5)(b) the event counts as a conviction for section 36A`, `s 120(2) TCA 36B(6) the provision is the appropriate penalty provision` |
| s 120 TCA 36C(1)-(3), (5), (6), (8) | power/liability | HM Revenue and Customs (working tax credit is not payable for a repeated offence) | the offender entitled to working tax credit (liability) | `s 120(2) TCA 36C(1) the restriction in subsection (3) applies`, `s 120(2) TCA 36C(2) the restriction in subsection (3) does not apply`, `s 120(2) TCA 36C(3) working tax credit is not payable to the person for the day`, `s 120(2) TCA 36C(5) the disqualification period`, `s 120(2) TCA 36C(6) the relevant period`, `s 120(2) TCA 36C(8) the number of disqualifying events in the set of proceedings`, `s 120(2) TCA 36C(8)(a) subsection (1)(b) is satisfied`, `s 120(2) TCA 36C(8)(b) the event is taken into account for the purposes of subsection (1)(d)` |
| s 120 TCA 36C(7) | none (definitions) | - | - | `s 120(2) TCA 36C(7) the provision is the appropriate penalty provision`, `s 120(2) TCA 36C(7) the offence is a benefit offence`, `s 120(2) TCA 36C(7) the benefit is a disqualifying benefit`, `s 120(2) TCA 36C(7) the event is a disqualifying event`, `s 120(2) TCA 36C(7) the offence is a relevant offence` |
| s 120 TCA 36C(4), (9)-(11) | power/liability | the Treasury / HM Revenue and Customs (regulations; order amending the periods) | offenders (liability) | not encoded (inert, reason 2) |
| s 120 TCA 36D(1)-(3) | claim-right/duty | the person whose restriction is treated as not imposed (claim to the payments and adjustments) | not named: the passive "shall be made" names no one (fork register F8) | `s 120(2) TCA 36D(1) the restriction is to be treated as not imposed`, `s 120(2) TCA 36D(2) subsection (3) applies`, `s 120(2) TCA 36D(3) the restriction is to be treated as not imposed` |
| s 120 TCA 36D(4), (5) | none (definitions: the date of a conviction; previous application) | - | - | `s 120(2) TCA 36D(4)(a) the date of the conviction`, `s 120(2) TCA 36D(4)(b) the event counts as a conviction for section 36C`, `s 120(2) TCA 36D(5) the application counts as a previous application of section 36C` |
| s 120(3) TCA 38(1)(ca) | power/liability | the person subject to the decision (power to appeal) | HM Revenue and Customs / the tribunal (liability to hear it) | `s 120(3)(b) TCA 38(1)(ca) an appeal lies against the decision` |
| s 120(5) TCA 67 | none (definition: cautioned) | - | - | `s 120(5) TCA 67 the person is cautioned in relation to the offence` |
| s 120(1), (4) | none (amendments; parliamentary control) | - | - | not encoded (inert, reason 2) |
| s 121 | immunity/disability | a person cautioned for a benefit offence (no loss of benefit or working tax credit on the caution) | the Secretary of State / HM Revenue and Customs (disabled: the caution ground is repealed) | `s 121(1)(c) SSFA 6B(1)(c) a caution is a ground for the loss of benefit`, `s 121(2) TCA 36A(1)(c) a caution is a ground for subsection (4)` |
| s 122 SSAA 109A(9) | none (definitions: Tax Credits Act 2002 treated as relevant social security legislation; tax credits as relevant benefits) | - | - | `s 122 SSAA 109A(9)(a) the legislation is treated as relevant social security legislation`, `s 122 SSAA 109A(9)(b) the benefit is treated as a relevant social security benefit for the definition of benefit offence` |
| s 123 | privilege/no-right | authorities (to supply government information for the prevention of tax credit fraud) | the person the information is about (no-right) | `s 123(3)(c) SSAA 122B(3)(d) paragraph (d) is met` |
| s 124 TCA 35 | power/liability | the court (to sentence) | a person convicted of tax credit fraud (liable to the stated punishment, by mode of trial) | `s 124 TCA 35(2) the mode of trial`, `s 124 TCA 35(3) the greatest punishment on summary conviction for an offence triable summarily only`, `s 124 TCA 35(4) the applicable term`, `s 124 TCA 35(6)(a) the greatest punishment on summary conviction for an offence triable either way`, `s 124 TCA 35(6)(b) the greatest punishment on conviction on indictment`, `s 124 TCA 35(7) the applicable term`, `s 124 TCA 35(8) the term as read for an offence committed before commencement`, `s 124 TCA 35(9) the term as read for an offence committed before commencement` |
| s 124 TCA 35(10)-(12) | none (how the maximum terms are read in England and Wales, Scotland and Northern Ireland: amending words) | - | - | not encoded (inert, reason 2) |
| s 125 | none (extends an offence: amendment of another Act) | - | - | not encoded (inert, reason 2) |
| s 126(1)-(10), (12), (14) | power/liability | Her Majesty in Council (Order: to transfer tax credit functions) | HM Revenue and Customs, the Secretary of State and the Treasury (liability) | not encoded (inert, reason 2) |
| s 126(11), (13) | none (definitions: tax credits; the Commissioners; primary and secondary legislation; tax credit functions) | - | - | `s 126(11) the benefit is a tax credit`, `s 126(13) the body is the Commissioners`, `s 126(13) the legislation is primary legislation`, `s 126(13) the legislation is secondary legislation`, `s 126(13) the function is a tax credit function` |
| s 127(2), (2A), (4) | privilege/no-right | the Secretary of State, a Northern Ireland Department, the Commissioners, the Scottish Ministers (to supply or receive information held for HMRC or departmental functions) | the person the information is about (no-right to prevent it) | `s 127(2) information held for HMRC functions may be supplied`, `s 127(2A) information held for HMRC functions may be supplied to the Scottish Ministers`, `s 127(4) information held for departmental functions may be supplied` |
| s 127(5) | claim-right/duty | the authority whose permission is needed (the Commissioners, the Secretary of State, or the Northern Ireland Department) | the recipient of the information (must not supply it onward without that authority) | `s 127(5) whose authority the recipient needs before supplying the information to another person`, `s 127(5) the recipient may supply the information to another person`, `s 127(5) the prohibition on onward supply` |
| s 127(6) | privilege/no-right | the recipient who has used the information for the purpose it was supplied for (to use it for any purposes for which information so held could be used) | the person the information is about (no-right) | `s 127(6) it is lawful to use the information for any purposes for which information held for those purposes could be used` |
| s 127(1), (3), (7)-(10) | none (scope; definitions; savings; amendment of SSA 1998 s 3(1A)) | - | - | `s 127(1) subsection (1) applies to the information`, `s 127(3) subsection (3) applies to the information`, `s 127(7) the function is a departmental function`, `s 127(7) the function is an HMRC function`, `s 127(7) the department is a Northern Ireland Department`, `s 127(8) the function is treated as relating to social security`, `s 127(9) this section does not limit the supply`, `s 127(10) SSA1998 3(1A)(e) the purpose is within paragraph (e)` |
| s 128(1), (4) | privilege/no-right | the Secretary of State and persons providing services to the Secretary of State (to supply social security or child support information to the DPP or a prosecutor) | the person the information is about (no-right) | `s 128(1) the Secretary of State may supply the information` |
| s 128(2), (3), (5), (6) | none (definitions; savings) | - | - | `s 128(2) the person is a person specified in subsection (2)`, `s 128(3) the purpose is a purpose specified in subsection (3)`, `s 128(6) the information is child support information`, `s 128(6) the matter is a social security matter`, `s 128(6) the information is social security information` |
| s 129(1) | claim-right/duty | not named by the text (an offence enforced by the Crown, s 129(8)); in substance the person the information relates to | a person to whom information is supplied under s 128, and their employees and former employees (must not disclose it) | `s 129(1) subsection (1) bars the disclosure`, `s 129(1) the bar on disclosure applies to the disclosure`, `s 129(1) the prohibition on disclosure` |
| s 129(2)-(4) | privilege/no-right | the discloser, in the excepted cases (summaries, DPP functions, ordered or consented disclosures and the rest) | not named (no-right of whoever the bar protects) | `s 129(2) subsection (1) does not apply to the disclosure`, `s 129(3) subsection (1) does not apply to the information`, `s 129(4) subsection (1) stands unaffected by any other enactment` |
| s 129(5), (7), (9) | power/liability | the Crown / the court (to prosecute and punish) | a person who contravenes s 129(1) (liable to the stated punishment) | `s 129(5) the person commits an offence`, `s 129(7) the greatest punishment for the offence`, `s 129(9) the term as read for an offence committed before 2 May 2022` |
| s 129(6) | immunity/disability | a person charged who proves a reasonable belief (immune from conviction) | the prosecution / the court (disabled from convicting) | `s 129(6) the person has a defence` |
| s 129(8) | immunity/disability | a person suspected of the offence (immune from prosecution without the DPP consent) | any prosecutor (disabled); the DPP holds the power to consent (liability: the suspect) | `s 129(8) a prosecution may be instituted` |
| s 130(5) | privilege/no-right | a local authority (to use, or supply to listed persons, information about overnight care or hospital accommodation, for relevant benefit purposes) | the individual receiving the service (no-right) | `s 130(5) the local authority may use or supply the information`, `s 130(1) this section applies`, `s 130(2) the information falls within subsection (2)`, `s 130(6) the person is a person specified in subsection (6)` |
| s 130(3), (4), (7), (8) | none (definitions: relevant service, hospital accommodation, relevant benefit; limit on regulations) | - | - | `s 130(3) the service is a relevant service`, `s 130(4) the accommodation is hospital accommodation`, `s 130(7) the benefit is a relevant benefit`, `s 130(8) regulations may prescribe the benefit` |
| s 131(1)-(4) | privilege/no-right | the Secretary of State, a qualifying person (to supply or use relevant information for welfare services or council tax purposes) | the individual the information is about (no-right) | `s 131(1) the Secretary of State may supply the information to a qualifying person`, `s 131(2) the qualifying person may supply the information to the Secretary of State`, `s 131(3) the qualifying person may use or supply the information`, `s 131(4) the qualifying person may supply the information to a person who provides qualifying welfare services` |
| s 131(6), (8) | immunity/disability | Welsh and Scottish bodies holding excepted information (immune from prescribed purposes that would cover it) | the Secretary of State (disabled from prescribing an excepted purpose) | `s 131(6) regulations may prescribe the purpose for information held by a Welsh body`, `s 131(8) regulations may prescribe the purpose for information held by a Scottish body` |
| s 131(5), (7), (9)-(12) | none (definitions; the saving for s 130) | - | - | `s 131(5) the services are qualifying welfare services`, `s 131(7)(a) the information held by the Welsh body is excepted information`, `s 131(7)(b) the purpose is an excepted purpose in relation to a Welsh body`, `s 131(9)(a) the information held by the Scottish body is excepted information`, `s 131(9)(b) the purpose is an excepted purpose in relation to a Scottish body`, `s 131(10) subsections (1) to (4) do not apply`, `s 131(11) the person is a qualifying person`, `s 131(12) the tax is council tax`, `s 131(12) the person is engaged in the administration of housing benefit`, `s 131(12) the information is relevant information`, `s 131(12) it is a relevant social security benefit`, `s 131(12) the person is a Scottish body`, `s 131(12) the service is welfare services`, `s 131(12) the person is a Welsh body` |
| s 132(1) | claim-right/duty | not named by the text (an offence enforced by the Crown); in substance the person the information relates to | the persons in s 132(2) (must not disclose without lawful authority) | `s 132(1) the person is guilty of an offence`, `s 132(2) subsection (2) applies to the person` |
| s 132(3), (9) | power/liability | the Crown / the court (to prosecute and punish) | a person guilty of the offence (liable to the stated punishment) | `s 132(3) the greatest punishment for the offence`, `s 132(9) the term as read for an offence committed before 2 May 2022` |
| s 132(4)-(6) | privilege/no-right | the discloser (a summary, a prior public disclosure, a reasonable belief, or a disclosure for the purposes of SSAA 123 is not an offence) | not named (no-right of whoever the bar protects) | `s 132(4) the disclosure is not an offence under this section`, `s 132(5) the person has a defence`, `s 132(6) the disclosure is made with lawful authority` |
| s 132(7), (8) | none (saving; regulations may apply the section to prescribed persons) | - | - | not encoded (inert, reason 2) |
| s 133 | none (supplementary: definitions; how regulations are made; interim rule for parish councils; repeals) | - | - | `s 133(1) the thing is a benefit`, `s 133(1) the body is a local authority`, `s 133(1) the matter is prescribed`, `s 133(5) the Act that gives the meaning of eligible parish council` |
| s 134 | none (amendments and repeals of WRPA 1999 s 72 and other Acts) | - | - | not encoded (inert, reason 2) |


### Reading a result: FALSE and NOTHING (wra4)

Every decision function in this part answers one of three things.

- `JUST TRUE` (or `TRUE`): the text says yes for these facts.
- `JUST FALSE` (or `FALSE`): **the text says no, in its own words.**
  In this Part that is a closed list ("welfare benefit means" a list, `s 96(10)`; "appropriate authority means" a list, SSAA 115C(6)), a flat negative ("decisions against which no appeal lies", Schedule 2 para 8A, `s 97(6)`; "no criminal proceedings shall be instituted against the recipient", SSAA 115B(4)(b); "Subsection (1) does not apply to" the disclosures in 129(2), `s 129(1)`), a bar with its exception ("is not recoverable under this section unless the determination has been reversed ...", SSAA 71ZB(3); "The authority may not bring proceedings ... unless", SSAA 116ZA(2); "must not be supplied by the recipient ... without", `s 127(5)`), or a failed "if" (reading (a): see the next section).
- `NOTHING`: **the text does not cover the case.**
  It is never a "no".
  The kinds in this Part, each marked in a comment on the branch as `NOTHING-kind (...)`: *silent* (a decision other than the benefit cap decision, for which Schedule 2 para 8A says nothing); *list not closed* (a benefit other than child tax credit and working tax credit in the lists of "disqualifying benefit" and "sanctionable benefit", because the other part's limb adds Universal Credit); *includes* (a definition that "includes" and so does not list everything); *undefined term* ("such circumstances as may be prescribed", "the relevant amount", "earnings" are for regulations); *points outside the text* (the regulations, SSA 1998 s 12(2), the unprinted text of SSAA 115A(5) and 115B(6)); *limited by own wording* (a "may" that grants a power only where its conditions are met and is silent otherwise, such as `s 127(2)` and `s 128(1)`; "If the recipient ... agrees" in SSAA 115B(4)).

For the person in the seat: a `JUST FALSE` is the Act refusing; a `NOTHING` is these sources not deciding, so the answer depends on regulations, on another Act, or on facts the person has not stated; it must not be read as "no".
A layer-1 rule that returns a plain `BOOLEAN` is total (a test over stated facts, a definition, or a count) and has no `NOTHING`; the seat wraps it in `JUST` so the answer has one shape.


## Marginal readings for a lawyer (wra4)

These are for a lawyer to rule on, not for the encoding to decide (Meng's ruling of 2026-10-22, applied by the brief).
Reading (a), taken as the status quo here: a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no.
Reading (b): a prohibition or a grant limited by its own wording does not count as a "no"; where it does not reach the case the answer is `NOTHING`.
Every branch below answers `JUST FALSE` (or `FALSE`) under (a); under (b) each would answer `NOTHING`.
The list is generated from the `FALSE-kind` comments in the layer-1 modules (`work/marginals.py`): all 139 such branches were read, and those whose wording is a conditional, a bar or an exception are listed; the rest rest on a closed list or a definition ("means ...") and are not marginal.
Line numbers are those of the `.l4` file named.

| # | file:line | rule | the wording the "no" rests on | kind |
| --- | --- | --- | --- | --- |
| M1 | wra4-ss96-97.l4:226 | `s 96(1) a benefit cap is applied to the person's welfare benefits` | "provide for exceptions to the application of the benefit cap" | exception |
| M2 | wra4-ss96-97.l4:243 | `s 96(9) benefit cap regulations may reduce this welfare benefit` | "Regulations under this section may not provide for any reduction to be made from a welfare benefit—" | bar |
| M3 | wra4-ss98-104.l4:104 | `s 102(3) SSA1998 12(3A) there is a right of appeal` | "there is a right of appeal ... only if the Secretary of State has considered whether to revise the decision" | necessary condition ("only if" / "unless") not met |
| M4 | wra4-ss98-104.l4:127 | `s 102(3) SSA1998 12(3B) the consideration meets the condition the regulations set` | "that condition is met only where" (a), (b) or (c) | necessary condition ("only if" / "unless") not met |
| M5 | wra4-s105-recovery.l4:59 | `s 105 SSAA 71ZB(1) the Secretary of State may recover an overpayment of the benefit` | "except in prescribed circumstances, housing credit" (the circumstances apply) | exception |
| M6 | wra4-s105-recovery.l4:132 | `s 105 SSAA 71ZB(3) the determination does not bar recovery` | "is not recoverable under this section unless the determination has been" reversed, varied, revised or superseded | necessary condition ("only if" / "unless") not met |
| M7 | wra4-s105-recovery.l4:286 | `s 105 SSAA 71ZD(3)(e) the most that may be deducted from the earnings` | "earnings must not be reduced" below the level (nothing may be deducted) | bar |
| M8 | wra4-s105-recovery.l4:302 | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts` | "the amount is, if the county court so orders, recoverable" (no order) | failed "if" |
| M9 | wra4-s105-recovery.l4:304 | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts` | "the amount is, if the county court so orders, recoverable" (no order) | failed "if" |
| M10 | wra4-s105-recovery.l4:306 | `s 105 SSAA 71ZE(1) and (2) the amount may be enforced through the courts` | "the amount is, if the county court so orders, recoverable" (no order) | failed "if" |
| M11 | wra4-s105-recovery.l4:457 | `s 105(4) SSAA 115B(4)(b) criminal proceedings may be instituted against the recipient for the conduct` | "no criminal proceedings shall be instituted against the recipient in respect of the conduct to which the notice relates" | bar |
| M12 | wra4-ss106-112.l4:139 | `s 108(4) the amendments apply to the proceedings as if in force from the start` | "except for the purposes of proceedings brought before the coming into force of this section" | exception |
| M13 | wra4-ss106-112.l4:216 | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` | "(9) This section does not apply to Scotland" | flat negative |
| M14 | wra4-ss106-112.l4:220 | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` | "an authority may bring proceedings in accordance with this section only if any such condition is satisfied" | necessary condition ("only if" / "unless") not met |
| M15 | wra4-ss106-112.l4:230 | `s 112(2) SSAA 116ZA(2) the authority may bring proceedings for the benefit offence` | "The authority may not bring proceedings against a person for a benefit offence ... unless" one of (a) to (e) | necessary condition ("only if" / "unless") not met |
| M16 | wra4-ss106-112.l4:265 | `s 112(2) SSAA 116ZA(6) the Secretary of State may continue or discontinue the proceedings` | "The Secretary of State may continue proceedings ... or he may discontinue the proceedings if" (a), (b), (c) or (d); none holds (a failed "if") | failed "if" |
| M17 | wra4-ss113-116.l4:188 | `s 116(1) SSAA 115C(2)(b) a penalty may be imposed on the other joint claimant instead` | "Subsection (2)(b) does not apply if B was not, and could not reasonably be expected to have been, aware" | flat negative |
| M18 | wra4-ss113-116.l4:255 | `s 116(1) SSAA 115D(3) a further penalty may be imposed for the same overpayment` | "only one penalty may be imposed in respect of the same overpayment" | bar |
| M19 | wra4-ss117-119.l4:229 | `s 119(5) SSFA 7(1)(b) a disqualifying event occurred within five years before a benefit offence` | "(b) within the period of five years ending on the date on which the benefit offence was, or any of them were, committed, one or more disqualifying events occurred" (none did) | failed "if" |
| M20 | wra4-ss117-119.l4:253 | `s 119(5) SSFA 7(1) the conditions in paragraphs (a) to (e) are met` | "(a) ..., (b) ..., (c) ..., (d) ..., and (e) ..." (one of the five is not met) | failed "if" |
| M21 | wra4-ss117-119.l4:332 | `s 119(8) SSFA 7(7B) the restriction is to be treated as not imposed` | "as would be necessary if no restriction had been imposed ... that could not have been imposed if P had not agreed to pay the penalty" (this one could have been) | failed "if" |
| M22 | wra4-s120-taxcredits.l4:146 | `s 120(2) TCA 36A(1)(b) the person agreed to pay a penalty as the paragraph describes` | "(b) after being given a notice under subsection (2) of the appropriate penalty provision by an appropriate authority, agrees in the manner specified by the appropriate authority to pay a penalty ...  | failed "if" |
| M23 | wra4-s120-taxcredits.l4:304 | `s 120(2) TCA 36B(1) the restriction is to be treated as not imposed` | "as would be necessary if no restriction had been imposed ... that could not have been imposed if the conviction had not taken place" (this one could have been) | failed "if" |
| M24 | wra4-s120-taxcredits.l4:325 | `s 120(2) TCA 36B(2) the restriction is to be treated as not imposed` | "as would be necessary if no restriction had been imposed ... that could not have been imposed if P had not agreed to pay the penalty" (this one could have been) | failed "if" |
| M25 | wra4-ss127-129.l4:171 | `s 127(5) the recipient may supply the information to another person` | "must not be supplied by the recipient of the information to any other person or body without— (a) ... (b) ... (c)" | bar |
| M26 | wra4-ss127-129.l4:443 | `s 129(1) the bar on disclosure applies to the disclosure` | "Subsection (1) does not apply to" the disclosures in (2) or the information in (3) | flat negative |
| M27 | wra4-ss127-129.l4:597 | `s 129(8) a prosecution may be instituted` | "A prosecution for an offence under this section may be instituted only with the consent of the Director of Public Prosecutions" | necessary condition ("only if" / "unless") not met |
| M28 | wra4-ss130-134.l4:194 | `s 130(8) regulations may prescribe the benefit` | "Regulations under subsection (7)(d) may not prescribe a benefit provision for which is within the legislative competence of the Scottish Parliament" | bar |
| M29 | wra4-ss130-134.l4:311 | `s 131(5) the services are qualifying welfare services` | "services are qualifying welfare services if (a) a local authority, or (b) a person who is a qualifying person by virtue of subsection (11)(g), contributes or will contribute to the expenditure" | failed "if" |
| M30 | wra4-ss130-134.l4:363 | `s 131(6) regulations may prescribe the purpose for information held by a Welsh body` | "The Secretary of State may not exercise the power in subsection (3) to prescribe purposes ... so as to prescribe an excepted purpose in relation to excepted information held by a Welsh body" | bar |
| M31 | wra4-ss130-134.l4:395 | `s 131(8) regulations may prescribe the purpose for information held by a Scottish body` | "The Secretary of State may not exercise the power in subsection (3) to prescribe purposes ... so as to prescribe an excepted purpose in relation to excepted information held by a Scottish body" | bar |

The other reading of every row above is `NOTHING` (not covered).
Rows left out on purpose: the closed lists and definitions that the text states with "means" or "are" (the 96(10) list, the 115C(6) "appropriate authority" list, "excepted information" and "excepted purpose" in 131(7) and (9), the persons in 130(6)); they are the text saying what a thing is, and a thing not on the list is not that thing.
Check that the list is complete: a scan of the ten layer-1 modules for any branch that produces `FALSE` or `JUST FALSE` found none without a `FALSE-kind` comment (the other matches were `WHEN JUST FALSE` pattern arms and one internal test whose failure goes to `NOTHING`).


## Seams (wra4)

The seams PLAN.md section 8 gives this part are rows 2 to 8; rows 1, 9 and 10 belong to other parts.
Each is taken as an input named exactly as the plan names it, except where noted.

| # | the input taken | where | note |
| --- | --- | --- | --- |
| 2 | the amount of each universal credit award (s 8(1)) | the `the amount awarded for the period, in pounds` field of an `Award` whose `the benefit awarded` is `universal credit`, in `s 96(2) the total entitlement to welfare benefits` | not a separate input: the core's `Award` carries the amount, so the caller (the lead, at the merge) supplies the s 8(1) amount in the award record; `universal credit` is one of the constructors `s 96(10) the benefit is a welfare benefit` accepts |
| 3 | `s 3 the claimant is entitled to universal credit for the period` (BOOLEAN) and `s 8(1) the amount of the award of universal credit for the period` (NUMBER) | inputs of `s 105 SSAA 71ZB(1)(a) the universal credit paid in excess of entitlement` | named as the plan names them; the rule is also asked through `Under section 105, SSAA 71ZB(1)(a) ...` |
| 4 | `s 28(2)(f) the hardship payment is recoverable under section 28` (BOOLEAN) | input of `s 105 SSAA 71ZH(1) the Secretary of State may recover the payment` | the regulations' answer, supplied |
| 5 | `s 46 JSA 19C(2)(f) the hardship payment is recoverable under section 19C` (BOOLEAN) | input of the same rule | the regulations' answer, supplied |
| 6 | `s 105 SSAA 71ZH(1)(c) ...`, `(d) ...`, `(e) ...` (BOOLEAN each) | inputs of the same rule | the host Acts (JSA Schedule 1 paragraphs 9 and 10, SSFA 2001) are not among the sources, so each is the caller's answer |
| 7 | the composite for "disqualifying benefit" and "sanctionable benefit" | `s 117(2) SSFA 6A(1) the benefit is a disqualifying benefit`, `s 117(3) SSFA 6A(1) the benefit is a sanctionable benefit` | this part encodes only its own limb: `JUST TRUE` for `child tax credit` and `working tax credit`, `NOTHING` (list not closed) for every other benefit, including `universal credit`; the lead writes the composite at the merge |
| 8 | `the regulations require consideration of revision before an appeal` (MAYBE BOOLEAN) and `the Secretary of State has considered whether to revise` (BOOLEAN) | inputs of `s 102(3) SSA1998 12(3A) there is a right of appeal` | the shared four-row reading, below |

Seam 8, the four rows of `s 102(3) SSA1998 12(3A) there is a right of appeal`:

| regulations require consideration first | the Secretary of State has considered | answer | why |
| --- | --- | --- | --- |
| not known (NOTHING) | any | NOTHING | points outside the text: the regulations are not among the sources |
| JUST FALSE | any | NOTHING | silent: without such regulations the right comes from SSA 1998 s 12(2), which is not among the sources |
| JUST TRUE | no | JUST FALSE | "there is a right of appeal ... only if the Secretary of State has considered whether to revise the decision": a failed "only if" (reading (a); listed under marginal readings) |
| JUST TRUE | yes | NOTHING | "only if" is a necessary condition, and the text does not say what else gives the right |

Seams found that the plan lacks: none.
One thing the core lacks is recorded in `NEEDS-CORE.md` (the Northern Ireland Department, the Northern Ireland Housing Executive and the Treasury are not constructors of `Authority`).


## Findings (what the text turns out to say)

1. **The Act inserts cautions and then repeals them.**
   Section 118(4) inserts SSFA 6B(11A)(c) ("in a case falling within subsection (1)(b) or (c), the period of four weeks") and s 120 inserts TCA 36A(1)(c) and 36A(7)(c); s 121(1)(c) and (2) then repeal SSFA 6B(1)(c) and TCA 36A(1)(c).
   A reader of the printed Act meets both versions.
   Encoded as printed, with the repeal as its own `JUST FALSE` rules (fork F6).
2. **The bar in SSAA 115B(4)(b) and the cooling-off period meet in text that is not printed.**
   Section 105(4) substitutes 115B(4): once the recipient agrees to pay, "no criminal proceedings shall be instituted against the recipient in respect of the conduct to which the notice relates".
   Section 115(3) changes the withdrawal period in 115B(6) from 28 to 14 and prints nothing else of 115B(6).
   The encoded bar is `JUST FALSE` when the recipient has agreed and `NOTHING` otherwise; the text printed here does not say what withdrawing the agreement does to the bar, and the encoding does not say either.
3. **The right of appeal in SSA 1998 12(3A) is a necessary condition, not a source of the right** (seam 8).
   The text says there is a right of appeal where regulations so provide "only if" the Secretary of State has considered revising the decision; where the condition is met the Act does not say what gives the right.
4. **Section 119(5) prints the conditions of SSFA 7(1) without the words that introduce them.**
   It substitutes paragraphs (a) to (e) for the old ones; the lead-in is not in this Act.
   `s 119(5) SSFA 7(1) the conditions in paragraphs (a) to (e) are met` therefore says only whether the five conditions are all met, not what follows.
5. **Seam 7 is half a list.**
   Sections 117(2) and (3) add two limbs (child tax credit and working tax credit) to two lists in SSFA 6A(1); Universal Credit is added by another part's Schedule 2.
   This part answers `NOTHING` for any other benefit; a caller who needs the whole list needs the lead's composite.
6. **Typographical features of the converted text**, noted so that nobody treats them as encoding errors: line 1972 reads "(but not within paragraph (a) above))" with a doubled closing bracket; line 2163 reads "(loss of tax working tax credit in case of conviction, penalty or caution for benefit offence)" in the heading of TCA 36A as quoted by s 121(2); line 2080 reads "when subsection 36A ceased to apply".
   None changes a rule.
7. **The penalty in SSAA 115A(3) is 50% of the overpayment, rounded down to the penny, with a minimum of 350 pounds and a maximum of 2000 pounds** (lines 1904-1906); in the new case of 115A(1A) it is 350 pounds (115A(3A)).
   `s 114(1) SSAA 115A(3) the amount of the penalty` is tested at the floor, the cap and the penny.
8. **The maximum punishments are tables by mode of conviction and by place and date.**
   `s 129(7)`, `s 132(3)` and TCA 35(3) to (9) (in `s 124`) give them; the reading for an offence committed before 2 May 2022 (`s 129(9)`, `s 132(9)`) and before commencement (TCA 35(8), (9)) is a separate rule in each case, tested.
9. **A regulation-making power is not a rule the person can use.**
   128 rows of the coverage table (43 subsections, 67 paragraphs, 17 sub-paragraphs and one host-Act heading) are regulation-making powers or what regulations may in particular provide (96(4), 96A(4) to (8), 71ZB(4), 71ZD(3), 71ZF, 71ZH(3) and the like).
   They are `inert` reason 2 in the coverage table, and where a rule turns on what the regulations provide, that fact is an input with "Leave out if not known" (answer `NOTHING` when left out).


## What the stable binary does not accept

The stable binary 1.6.98 governs; where the skills describe something it rejects, this list is what it did.

- **A list of dates needs commas.**
  `LIST (Date 1 1 2025) (Date 2 1 2020)` is a parse error; `LIST (Date 1 1 2025), (Date 2 1 2020)` is accepted.
- **A bare `NOT` binds loosest and swallows the rest of a conjunction (silent).**
  Measured on the stable binary: `#EVAL TRUE AND NOT FALSE AND FALSE` evaluates to `TRUE`, because `NOT FALSE AND FALSE` is read as `NOT (FALSE AND FALSE)`.
  There was no diagnostic.
  Eleven bare `NOT`s in four modules were found this way and rewritten as `(NOT (x))`, each with a test that discriminates the two readings; every `NOT` in the files is now parenthesised.
- **`ELSE IF ... ELSE (CONSIDER ...)` nested inside a branch fails the layout rule** (loud: a parse error); a `BRANCH` with `IF` and `OTHERWISE` is used instead.
- **`WAIT UNTIL` is not defined** (loud).
  Deadlines are written `WITHIN n`, with the number of days as an input, and the time of each event is the `AT` of the trace.
- **A `DEONTIC` value cannot be the left side of `EQUALS` in an `#ASSERT`.**
  The regulative rules are exercised with `#TRACE` (8 traces in `wra4-tests-regulative.l4`) and each has a boolean twin in a decision module that is asserted.
- **`REFUSE` does not exist**: "not covered" is `NOTHING` or a constructor, asserted.
- **`JL4_LIBRARY_PATH` set to the empty string is not the same as unset** (loud, and misleading): with it empty the binary skips its embedded libraries and reports `Module not found ... prelude`.
  Run with `env -u JL4_LIBRARY_PATH`.
- **`check.sh` does not see a `#TRACE` outcome** (silent).
  The eight traces were run on both binaries and read: FULFILLED, FULFILLED, BREACH, FULFILLED, BREACH, FULFILLED, BREACH, FULFILLED, the same on stable 1.6.98 and main 1.6.108.


## What went wrong

The lead reset this run's sandbox at 07:59:58 on 4 November 2026 (it re-ran the brief builder, which deleted and recreated `runs/iaw-wra4/`).
The run was launched at 08:00 (`LAUNCHED`), and every file of this part's work is dated 08:05 or later, so the reset happened before any of it was written.
Nothing of this part's work was lost and nothing had to be redone; I listed `DEPOSIT` and `work/` after the message arrived, and every file named above was there.
The one trace the reset left in the run itself is that the supplied files (`check.sh`, `srcrefs.py`, `fetch-main-l4.sh`, `wra-core.l4`, `wra-definitions.l4`, `BRIEF.md`, `inputs/`) are dated 07:59.


## What check.sh prints

Command: `env -u JL4_LIBRARY_PATH L4=<stable l4 1.6.98> L4_MAIN=<main l4 1.6.108> bash check.sh` in this folder, target `main` (the default).
Baseline numbers it replaced: the keel's run printed `TOTAL (3 modules)` with 38 assertions satisfied (all in `wra-core-tests.l4`, which is not in this folder); this part's own earlier run, before the regulative module, the seat layer and the added tests, printed `TOTAL (22 modules)` with 960 satisfied.
`wra-core.l4` and `wra-definitions.l4` define things and have no assertions, so they print 0.
The eight `#TRACE`s are not counted by `check.sh` (see above).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
wra-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
wra-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
wra4-cases-seat.l4                             0       143       0        0         0 |      0       143       0        0  same
wra4-regulative.l4                             0         0       0        0         0 |      0         0       0        0  same
wra4-s105-recovery.l4                          0         0       0        0         0 |      0         0       0        0  same
wra4-s120-taxcredits.l4                        0         0       0        0         0 |      0         0       0        0  same
wra4-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra4-ss106-112.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss113-116.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss117-119.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss121-126.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss127-129.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss130-134.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss96-97.l4                                0         0       0        0         0 |      0         0       0        0  same
wra4-ss98-104.l4                               0         0       0        0         0 |      0         0       0        0  same
wra4-tests-regulative.l4                       0         0       0        0         0 |      0         0       0        0  same
wra4-tests-s105-recovery.l4                    0       149       0        0         0 |      0       149       0        0  same
wra4-tests-s120-taxcredits.l4                  0       124       0        0         0 |      0       124       0        0  same
wra4-tests-ss106-112.l4                        0        71       0        0         0 |      0        71       0        0  same
wra4-tests-ss113-116.l4                        0        88       0        0         0 |      0        88       0        0  same
wra4-tests-ss117-119.l4                        0        97       0        0         0 |      0        97       0        0  same
wra4-tests-ss121-126.l4                        0        53       0        0         0 |      0        53       0        0  same
wra4-tests-ss127-129.l4                        0       110       0        0         0 |      0       110       0        0  same
wra4-tests-ss130-134.l4                        0       141       0        0         0 |      0       141       0        0  same
wra4-tests-ss96-97.l4                          0        94       0        0         0 |      0        94       0        0  same
wra4-tests-ss98-104.l4                         0        47       0        0         0 |      0        47       0        0  same
TOTAL (26 modules)                             0      1117       0        0           |      0      1117       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

Every module has 0 errors, 0 failed and 0 refused on the stable binary and the same four counts on the main build; 1117 assertions satisfied, none failing on purpose (no expected failures, so no `expected_failed` entry).
Also run and clean: `python3 -I srcrefs.py check --refs ../../../inputs/ukpga-2012-5.txt wra4-*.l4` and the same with `--strict`: 568 `src:` lines, 243 runs, 253 locators, 0 problems.
