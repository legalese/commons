# NOTES (coa28): Companies Act 2006 (United Kingdom), lines 18349-19081

Status (as of the check.sh run recorded at the foot of this file): layer 1 and layer 2 are written, every module checks with 0 errors and every assertion in the tests and the seat cases is satisfied on the stable builds 1.6.110 and 1.6.109.
Everything below was checked by script against the files in this folder on the day it was written; where a statement rests on a reading and not on a measurement, it says so.

**The text is a converter rendering, not the official text.**
`inputs/ukpga-2006-46.txt` is a plain-text rendering of the Act made by a converter script from legislation.gov.uk (see `inputs/SOURCES.md` and the meta file for its version and hashes).
Nothing in this folder is "verified against the official text", and no claim here should be read as one.
Every quotation in the modules is copied by script from that rendering (`-- src:N | ...` lines), and `srcrefs.py check --refs` and `--strict` report 0 problems for the files (recorded at the foot).

## What is in this folder (coa28)

Layer 1, the law, in isomorphic modules with tests:

| module | provisions | tests |
|---|---|---|
| `coa28-part44.l4` | ss 1274 to 1283 (actuaries and the 2004 Act, institutional investors, Enterprise Act 2002 s 241A, expenses of winding up, commonhold) | `coa28-tests-part44.l4` |
| `coa28-part45.l4` | ss 1284 to 1287 (Northern Ireland) | `coa28-tests-part45-47.l4` |
| `coa28-part46.l4` | ss 1288 to 1297 (regulations and orders, enactment, continuity of the law) | `coa28-tests-part46.l4` |
| `coa28-part47.l4` | s 1299 (extent) | `coa28-tests-part45-47.l4` |
| `coa28-sch1.l4` | Schedule 1 (interests in shares or debentures) | `coa28-tests-sch1.l4` |
| `coa28-sch1a.l4` | Schedule 1A (people with significant control) | `coa28-tests-sch1a.l4` |
| `coa28-sch1b.l4` | Schedule 1B (restrictions notices, offences) | `coa28-tests-sch1b.l4` |
| `coa28-sch1c.l4` | Schedule 1C (Takeover Panel rules) | `coa28-tests-sch1c.l4` |

Layer 2, the seat: `coa28-seat.l4` (74 questions, each `@export` with `@desc`) and `coa28-cases-seat.l4` (232 assertions).
The seat is an individual who is, or may become, a director, company secretary or member of a company, or who deals with one; its questions are grouped under `§` headings in the order of the text, with a comment on each group that arises only in a situation (a takeover bid, a restrictions notice, a winding up).
`coa28-seat.l4` and `coa28-cases-seat.l4` import every layer-1 module at once; a probe that imports all eight layer-1 modules together with `coa-core.l4` and `coa-definitions.l4` loads with 0 errors (the diamond through `coa28-part46` and `coa-core` resolves).

The keel files `coa-core.l4` and `coa-definitions.l4` are the keel's, read-only, and were not changed.
`NEEDS-CORE.md` lists the constructors I wanted from the core.
`PROGRESS.md` is the resume file.

## Coverage (coa28)

The table below was built by script (`work/cov/gen.py`, not shipped) from the raw text, a row specification, and the `@ref` locators in the layer-1 modules.
It has one row per text unit, a unit being one line of the rendering: a heading, a section or paragraph opening, a subsection, a lettered or numbered item, a defined term, or a continuation line (closing words).
Every non-blank line of 18349-19081 falls in a row (733 lines, 0 blank, 0 uncovered; the script asserts the union and stops if a line is missing).
Line 18785 is in two rows because it holds two limbs of one sentence (sch 1A para 24(9): the power to revise guidance is machinery, the clause saying that "guidance" includes revised guidance is encoded).

Each row has exactly one disposition: `encoded` (a rule, definition or table in layer 1, cited with `@ref`, with at least one test), `inert 1`, `inert 2`, `inert 3` (the three reasons of the brief), or `fork` (the text reads two ways; the row names the fork).
The `L4 name` column lists every layer-1 name whose `@ref` locator covers the line; `〃` means the same as the row above; the `Tests` column counts the `#ASSERT` and `#TRACE` lines in `coa28-tests-*.l4` that mention one of those names or, for a type, one of its constructors.
The script also checks that no encoded or fork row lacks a name and that none has 0 tests (0 rows fail either check).

**Why the substance of s 1274(3), 241A and 176ZA is `encoded` while s 1274(2)(l) to (t) is `inert 2`.**
All of these are amendments of other Acts, and the brief allows `inert 2` for "amendments of other Acts".
I encoded what decides something about a person (who is a member of a professional actuarial body, who may disclose information and to whom, what the individual may not do with it, how the expenses of winding up rank against a floating charge) and left inert what is a grant power or an instruction to amend (the purposes for which a body may be given a grant, the words to be inserted, the commencement).
That is a line I drew, not one the text draws; a reviewer who reads "amendments of other Acts" as covering the inserted text may move those rows to `inert 2`.

**Signposts and purpose clauses.**
Reason 1 lists "a purpose or objects clause that creates no rule".
Two rows are filed under reason 1 on the wider ground that they create no rule: sch 1B para 1(5) ("The effect of a restrictions notice is set out in paragraph 3", a signpost) and sch 1B para 4(2) ("The direction is given for the purpose of protecting those third party rights", a purpose clause), and the two introductions sch 1A para 7 and para 10 ("This Part of this Schedule specifies ...", "This Part sets out rules for the interpretation of this Schedule").
A reviewer who reads reason 1 strictly (titles, headings, long title, enacting words, a purpose or objects clause) may want sch 1B para 1(5) encoded; it would have one answer and no test beyond that.

**Machinery rows (inert 2) are regulation-making and rule-making powers, the Act's own commencement and short title, amendments of other Acts, and the repeals of s 1295.**
The brief lists "short title and extent" as machinery; s 1299 (extent) is nevertheless encoded, because it answers a question an individual can ask (does this provision extend to the whole of the United Kingdom?).
Sch 1C paras 8(3), 9(4), 11(2), 13(2) and 14 are rules the Panel "may" make, or powers it "may" be given; they are filed as rule-making powers.

**Repealed or blank (inert 3).**
Only s 1278(1)(f) is a row of dots in the text, and it is the only row filed under reason 3.
The text also shows `...` after s 1286(1)(c); the text does not say what it stands for, and items (a) to (e) are encoded as printed.

**Coverage summary (script output).**

| measure | count |
|---|---|
| lines in 18349-19081 | 733 (0 blank) |
| text units counted by script: lines that open a heading, section, paragraph, subsection, item or defined term | 700 |
| continuation lines (closing words and the like) | 33 |
| provision-level rows in the first draft of the table, before the audit below | 486 |
| provision-level rows after the audit | 481 |
| line-level rows in the table below (one per text line; line 18785 in two rows) | 734 |
| provision-level rows by disposition | encoded 251, fork 12, inert 1 111, inert 2 106, inert 3 1 |
| line-level rows by disposition | encoded 494, fork 18, inert 1 113, inert 2 108, inert 3 1 |
| lines in no row | 0 |
| encoded or fork rows with no L4 name / with 0 tests | 0 / 0 |

The audit compared every encoded row with the `@ref` locators in the layer-1 modules and found five places where a row and the locators disagreed: three lead-in lines (18404, 18481, 18493) and sch 1C para 20(1)'s lead-in (19061) were filed as separate `inert 1` rows although they are part of an encoded sentence, and line 18876 (sch 1B para 8(1)) was in no locator.
The quotes were widened to cite the lead-ins and para 8(1), the five rows were merged into the rows that follow them, and the first-draft count of 486 became 481.


| Line | Unit (provision; for a multi-line row, the line quoted) | Disposition | L4 name (layer 1) | Tests | Note |
|---|---|---|---|---|---|
| 18349 | Part 44 title | inert 1 |  |  | Part title |
| 18350 | Part 44 group heading: Regulation of actuaries etc | inert 1 |  |  | cross-heading |
| 18351 | s 1274 heading | inert 1 |  |  | section heading |
| 18352 | s 1274(1) | inert 2 |  |  | amends s 16 of the Companies (Audit, Investigations and Community Enterprise) Act 2004: amendment of another Act |
| 18353 | s 1274(2) lead | inert 2 |  |  | amends s 16(2) of the 2004 Act: amendment of another Act |
| 18354 | s 1274(2) new para (l) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18355 | s 1274(2) new para (m) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18356 | s 1274(2) new para (n) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18357 | s 1274(2) new para (o) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18358 | s 1274(2) new para (p) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18359 | s 1274(2) new para (q) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18360 | s 1274(2) new para (r) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18361 | s 1274(2) new para (s) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18362 | s 1274(2) new para (t) | inert 2 |  |  | inserted purpose of grants to bodies: amendment of another Act (a grant power) |
| 18363 | s 1274(3) lead | inert 2 |  |  | amends s 16(5) of the 2004 Act (the instruction; the inserted definitions below are encoded) |
| 18364 | s 1274(3) definition of professional actuarial body -- "“professional actuarial body” means—" | encoded | `s 1274(3) the body is a professional actuarial body` | 3 |  |
| 18365 | s 1274(3) definition of professional actuarial body -- "(a) the Institute of Actuaries, or" | encoded | 〃 | 〃 |  |
| 18366 | s 1274(3) definition of professional actuarial body -- "(b) the Faculty of Actuaries in Scot..." | encoded | 〃 | 〃 |  |
| 18367 | s 1274(3) definition of members of a professional actuarial body | encoded | `s 1274(3) the person is a member of a professional actuarial body`; `s 1274(3) function` | 7 |  |
| 18368 | s 1274(3) definition of regulatory functions -- "“regulatory functions”, in relation ..." | encoded | `s 1274(3) the function is a regulatory function in relation to professional actuarial bodies` | 4 |  |
| 18369 | s 1274(3) definition of regulatory functions -- "(a) investigatory or disciplinary fu..." | encoded | 〃 | 〃 |  |
| 18370 | s 1274(3) definition of regulatory functions -- "(b) the setting by such bodies of st..." | encoded | 〃 | 〃 |  |
| 18371 | s 1274(3) definition of regulatory functions -- "(c) the determining by such bodies o..." | encoded | 〃 | 〃 |  |
| 18372 | s 1275 heading | inert 1 |  |  | section heading |
| 18373 | s 1275(1) | inert 2 |  |  | amends s 17 of the 2004 Act: amendment of another Act |
| 18374 | s 1275(2) | inert 2 |  |  | amends s 17(3)(a) of the 2004 Act: amendment of another Act |
| 18375 | s 1275(3) lead | inert 2 |  |  | inserts s 17(3A) in the 2004 Act (the instruction; the inserted subsection is encoded) |
| 18376 | s 1275(3) inserted s 17(3A) and (a), (b) -- "(3A) The following persons are withi..." | encoded | `s 1275(3) the person is within subsection (3A) of section 17 of the 2004 Act` | 3 |  |
| 18377 | s 1275(3) inserted s 17(3A) and (a), (b) -- "(a) the administrators of a public s..." | encoded | 〃 | 〃 |  |
| 18378 | s 1275(3) inserted s 17(3A) and (a), (b) -- "(b) the trustees or managers of an o..." | encoded | 〃 | 〃 |  |
| 18379 | s 1275(4) lead | inert 2 |  |  | amends s 17(4) of the 2004 Act: amendment of another Act |
| 18380 | s 1275(4) inserted s 17(4)(c) | inert 2 |  |  | inserted regulation-making power (different provision for different cases) |
| 18381 | s 1275(5) lead | inert 2 |  |  | amends s 17 of the 2004 Act (the instruction; the inserted subsection (13) is encoded) |
| 18382 | s 1275(5) inserted s 17(13) | encoded | `s 1275(5) the draft is to proceed in that House as if it were not a hybrid instrument` | 3 |  |
| 18383 | s 1275(6) | encoded | `s 1275(6) the amendments have effect in relation to the exercise of the power` | 2 |  |
| 18384 | s 1275(7) lead | inert 2 |  |  | amends Schedule 3 to the Pensions Act 2004: amendment of another Act |
| 18385 | s 1275(7) inserted entry (ga) | inert 2 |  |  | amends a disclosure gateway of the Pensions Regulator (an official's power): amendment of another Act |
| 18386 | s 1276 heading | inert 1 |  |  | section heading |
| 18387 | s 1276(1) | inert 2 |  |  | amends s 16 of the 2004 Act: amendment of another Act |
| 18388 | s 1276(2) lead | inert 2 |  |  | substitutes s 16(6) of the 2004 Act (the instruction; the substituted subsection is encoded) |
| 18389 | s 1276(2) substituted s 16(6) | encoded | `s 1276(2) the matter is one to which subsection (2)(a) to (t) of section 16 of the 2004 Act is read as referring in Scotland` | 2 |  |
| 18390 | s 1276(3) | inert 2 |  |  | amends s 16(2)(c) of the 2004 Act: amendment of another Act |
| 18391 | s 1276(4) lead | inert 2 |  |  | amends s 16(5) of the 2004 Act: amendment of another Act |
| 18392 | s 1276(4)(a) | inert 2 |  |  | amends a definition in s 16(5) of the 2004 Act: amendment of another Act |
| 18393 | s 1276(4)(b) | inert 2 |  |  | amends a definition in s 16(5) of the 2004 Act: amendment of another Act |
| 18394 | s 1276(4)(c) inserted definition of the 1986 Order -- "(c) after that definition insert—" | encoded | `s 1276(4)(c) the instrument is the 1986 Order` | 2 |  |
| 18395 | s 1276(4)(c) inserted definition of the 1986 Order -- "“the 1986 Order” means the Companies..." | encoded | 〃 | 〃 |  |
| 18396 | s 1276(5) | inert 2 |  |  | amends s 66 (extent) of the 2004 Act: amendment of another Act |
| 18397 | Part 44 group heading: institutional investors | inert 1 |  |  | cross-heading |
| 18398 | s 1277 heading | inert 1 |  |  | section heading |
| 18399 | s 1277(1) | inert 2 |  |  | regulation-making power (Treasury or Secretary of State) |
| 18400 | s 1277(2) lead | inert 2 |  |  | says the power is exercisable in accordance with ss 1278 to 1280 |
| 18401 | s 1277(2) first bullet (s 1278) | inert 2 |  |  | pointer within the power |
| 18402 | s 1277(2) second bullet (s 1279) | inert 2 |  |  | pointer within the power |
| 18403 | s 1277(2) third bullet (s 1280) | inert 2 |  |  | pointer within the power |
| 18404 | s 1277(3) lead-in and (a) persons acting on behalf of an institution -- "(3) In this section and the sections..." | encoded | `s 1277(3)(a) the person is a person acting on behalf of the institution` | 3 |  |
| 18405 | s 1277(3) lead-in and (a) persons acting on behalf of an institution -- "(a) references to a person acting on..." | encoded | 〃 | 〃 |  |
| 18406 | s 1277(3) lead-in and (a) persons acting on behalf of an institution -- "(i) any person to whom authority has..." | encoded | 〃 | 〃 |  |
| 18407 | s 1277(3) lead-in and (a) persons acting on behalf of an institution -- "(ii) such other persons as may be sp..." | encoded | 〃 | 〃 |  |
| 18408 | s 1277(3)(b) specified | encoded | `s 1277(3)(b) the matter is specified for the purposes of sections 1277 to 1280` | 2 |  |
| 18409 | s 1277(4) enforcement by civil proceedings -- "(4) The obligation imposed by regula..." | encoded | `s 1277(4) the person may bring civil proceedings to enforce the obligation` | 4 |  |
| 18410 | s 1277(4) enforcement by civil proceedings -- "(a) any person to whom the informati..." | encoded | 〃 | 〃 |  |
| 18411 | s 1277(4) enforcement by civil proceedings -- "(b) a specified regulatory authority..." | encoded | 〃 | 〃 |  |
| 18412 | s 1277(5) | inert 2 |  |  | regulation-making power (different provision for different cases) |
| 18413 | s 1277(6) | encoded | `s 1277(6) the procedure for regulations under section 1277` | 1 |  |
| 18414 | s 1278 heading | inert 1 |  |  | section heading |
| 18415 | s 1278(1) institutions (lead, (a) to (e)) -- "(1) The institutions to which sectio..." | encoded | `s 1278(1) the institution is one to which section 1277 applies` | 6 |  |
| 18416 | s 1278(1) institutions (lead, (a) to (e)) -- "(a) unit trust schemes within the me..." | encoded | 〃 | 〃 |  |
| 18417 | s 1278(1) institutions (lead, (a) to (e)) -- "(b) open-ended investment companies ..." | encoded | 〃 | 〃 |  |
| 18418 | s 1278(1) institutions (lead, (a) to (e)) -- "(c) companies approved for the purpo..." | encoded | 〃 | 〃 |  |
| 18419 | s 1278(1) institutions (lead, (a) to (e)) -- "(d) pension schemes as defined in se..." | encoded | 〃 | 〃 |  |
| 18420 | s 1278(1) institutions (lead, (a) to (e)) -- "(e) undertakings authorised under th..." | encoded | 〃 | 〃 |  |
| 18421 | s 1278(1)(f) | inert 3 |  |  | the text shows only a row of dots: an item repealed or blank in this text |
| 18422 | s 1278(2) lead | inert 2 |  |  | regulation-making power |
| 18423 | s 1278(2)(a) | inert 2 |  |  | regulation-making power (other descriptions of institution) |
| 18424 | s 1278(2)(b) | inert 2 |  |  | regulation-making power (disapplication) |
| 18425 | s 1278(3) | encoded | `s 1278(3) the regulations meet the requirement to specify by whom the duty is to be fulfilled` | 2 |  |
| 18426 | s 1279 heading | inert 1 |  |  | section heading |
| 18427 | s 1279(1) shares (lead, (a), (b)) -- "(1) The shares to which section 1277..." | encoded | `s 1279(1) the shares are shares to which section 1277 applies` | 4 |  |
| 18428 | s 1279(1) shares (lead, (a), (b)) -- "(a) of a description traded on a spe..." | encoded | 〃 | 〃 |  |
| 18429 | s 1279(1) shares (lead, (a), (b)) -- "(b) in which the institution has, or..." | encoded | 〃 | 〃 |  |
| 18430 | s 1279(1) closing sentence | inert 2 |  |  | regulation-making power (a description of shares may be excluded) |
| 18431 | s 1279(2) interest in shares | encoded | `s 1279(2) the institution has an interest in the shares` | 2 |  |
| 18432 | s 1279(2) depositary certificate (lead, (a), (b)) -- "A “depositary certificate” means an ..." | encoded | `s 1279(2) the instrument is a depositary certificate` | 4 |  |
| 18433 | s 1279(2) depositary certificate (lead, (a), (b)) -- "(a) in respect of shares held by ano..." | encoded | 〃 | 〃 |  |
| 18434 | s 1279(2) depositary certificate (lead, (a), (b)) -- "(b) the transfer of which may be eff..." | encoded | 〃 | 〃 |  |
| 18435 | s 1279(3) interest through a scheme or vehicle -- "(3) Where an institution has an inte..." | encoded | `s 1279(3) the institution is taken to have an interest in the shares` | 4 |  |
| 18436 | s 1279(3) interest through a scheme or vehicle -- "(a) in a specified description of co..." | encoded | 〃 | 〃 |  |
| 18437 | s 1279(3) interest through a scheme or vehicle -- "(b) in any other specified descripti..." | encoded | 〃 | 〃 |  |
| 18438 | s 1279(3) interest through a scheme or vehicle -- "it is taken to have an interest in a..." | encoded | 〃 | 〃 |  |
| 18439 | s 1279(4) | encoded | `s 1279(4) the scheme or vehicle is taken to have an interest in the shares` | 2 |  |
| 18440 | s 1280 heading | inert 1 |  |  | section heading |
| 18441 | s 1280(1) lead | inert 2 |  |  | regulation-making power (specified information) |
| 18442 | s 1280(1)(a) | inert 2 |  |  | regulation-making power |
| 18443 | s 1280(1)(b) | inert 2 |  |  | regulation-making power |
| 18444 | s 1280(1)(c) | inert 2 |  |  | regulation-making power |
| 18445 | s 1280(2) | inert 2 |  |  | regulation-making power |
| 18446 | s 1280(3) | inert 2 |  |  | regulation-making power |
| 18447 | s 1280(4) lead | inert 2 |  |  | regulation-making power |
| 18448 | s 1280(4)(a) | inert 2 |  |  | regulation-making power |
| 18449 | s 1280(4)(b) | inert 2 |  |  | regulation-making power |
| 18450 | s 1280(5) lead | inert 2 |  |  | regulation-making power |
| 18451 | s 1280(5)(a) | inert 2 |  |  | regulation-making power |
| 18452 | s 1280(5)(b) aggregated form ((b), (i) to (iii)) -- "(b) that in such a case it is suffic..." | encoded | `s 1280(5)(b) the information is information given in aggregated form` | 4 | the definition of aggregated form is encoded; the power it sits in is not |
| 18453 | s 1280(5)(b) aggregated form ((b), (i) to (iii)) -- "(i) relating to the exercise or non-..." | encoded | 〃 | 〃 | 〃 |
| 18454 | s 1280(5)(b) aggregated form ((b), (i) to (iii)) -- "(ii) relating to the instructions gi..." | encoded | 〃 | 〃 | 〃 |
| 18455 | s 1280(5)(b) aggregated form ((b), (i) to (iii)) -- "(iii) relating to the delegation by ..." | encoded | 〃 | 〃 | 〃 |
| 18456 | s 1280(6) instructions | encoded | `s 1280(6) the reference to instructions in section 1280 covers the instruction`; `s 1281 241A(2) kind of information` | 7 |  |
| 18457 | Part 44 group heading: Enterprise Act 2002 | inert 1 |  |  | cross-heading |
| 18458 | s 1281 heading | inert 1 |  |  | section heading |
| 18459 | s 1281 instruction | inert 2 |  |  | amends Part 9 of the Enterprise Act 2002 (the instruction; the inserted s 241A is encoded) |
| 18460 | inserted s 241A heading | inert 1 |  |  | heading of the inserted section |
| 18461 | s 1281 241A(1) disclosure by a public authority -- "(1) A public authority which holds p..." | encoded | `s 1281 241A(1) the public authority may disclose the information to any person` | 6 |  |
| 18462 | s 1281 241A(1) disclosure by a public authority -- "(a) for the purposes of, or in conne..." | encoded | 〃 | 〃 |  |
| 18463 | s 1281 241A(1) disclosure by a public authority -- "(b) for the purposes of obtaining le..." | encoded | 〃 | 〃 |  |
| 18464 | s 1281 241A(1) disclosure by a public authority -- "(c) otherwise for the purposes of es..." | encoded | 〃 | 〃 |  |
| 18465 | s 1281 241A(2) exclusions -- "(2) Subsection (1) does not apply to..." | encoded | `s 1281 241A(2) subsection (1) does not apply to the information` | 5 |  |
| 18466 | s 1281 241A(2) exclusions -- "(a) information which comes to a pub..." | encoded | 〃 | 〃 |  |
| 18467 | s 1281 241A(2) exclusions -- "(b) competition information within t..." | encoded | 〃 | 〃 |  |
| 18468 | s 1281 241A(2) exclusions -- "(c) information which comes to a pub..." | encoded | 〃 | 〃 |  |
| 18469 | s 1281 241A(2) exclusions -- "(d) information which comes to a pub..." | encoded | 〃 | 〃 |  |
| 18470 | s 1281 241A(3) prescribed | encoded | `s 1281 241A(3) the information or proceedings are prescribed`; `s 1281 241A(1) purpose` | 8 |  |
| 18471 | s 1281 241A(4) lead | inert 2 |  |  | order-making power |
| 18472 | s 1281 241A(4)(a) | inert 2 |  |  | order-making power |
| 18473 | s 1281 241A(4)(b) | inert 2 |  |  | order-making power |
| 18474 | s 1281 241A(4)(c) procedure | encoded | `s 1281 241A(4)(c) the procedure for an order under section 241A` | 1 |  |
| 18475 | s 1281 241A(5) use of information disclosed | encoded | `s 1281 241A(5) the person is barred from using the information for the purpose`; `s 1281 241A(5) party`; `s 1281 241A(5) action`; `s 1281 241A(5) the recipient's prohibition on use` | 6 |  |
| 18476 | Part 44 group heading: Expenses of winding up | inert 1 |  |  | cross-heading |
| 18477 | s 1282 heading | inert 1 |  |  | section heading |
| 18478 | s 1282(1) instruction | inert 2 |  |  | inserts s 176ZA in the Insolvency Act 1986 (the instruction; the inserted section is encoded) |
| 18479 | inserted s 176ZA heading | inert 1 |  |  | heading of the inserted section |
| 18480 | s 1282(1) 176ZA(1) | encoded | `s 1282(1) 176ZA(1) the expenses of winding up have priority over claims to property comprised in or subject to a floating charge`; `s 1282(1) 176ZA(1) the amount of the expenses that has priority over floating charge claims`; `s 1282 claimant` | 11 |  |
| 18481 | s 1282(1) 176ZA(2) lead and (a) -- "(2) In subsection (1)—" | encoded | `s 1282(1) 176ZA(2)(a) the assets of the company available for payment of general creditors` | 2 |  |
| 18482 | s 1282(1) 176ZA(2) lead and (a) -- "(a) the reference to assets of the c..." | encoded | 〃 | 〃 |  |
| 18483 | s 1282(1) 176ZA(2)(b) lead, (i), (ii) -- "(b) the reference to claims to prope..." | encoded | `s 1282(1) 176ZA(2)(b) the claim is a claim to property comprised in or subject to a floating charge` | 3 |  |
| 18484 | s 1282(1) 176ZA(2)(b) lead, (i), (ii) -- "(i) the holders of debentures secure..." | encoded | 〃 | 〃 |  |
| 18485 | s 1282(1) 176ZA(2)(b) lead, (i), (ii) -- "(ii) any preferential creditors enti..." | encoded | 〃 | 〃 |  |
| 18486 | s 1282(1) 176ZA(3) lead | inert 2 |  |  | rule-making power (restricting the application of subsection (1)) |
| 18487 | s 1282(1) 176ZA(3)(a) | inert 2 |  |  | rule-making power |
| 18488 | s 1282(1) 176ZA(3)(b) | inert 2 |  |  | rule-making power |
| 18489 | s 1282(1) 176ZA(4) | encoded | `s 1282(1) 176ZA(4) the expense is an expense of the winding up` | 2 |  |
| 18490 | s 1282(2) instruction | inert 2 |  |  | inserts Article 150ZA in the Insolvency (Northern Ireland) Order 1989 (the instruction; the inserted Article is encoded) |
| 18491 | inserted Article 150ZA heading | inert 1 |  |  | heading of the inserted Article |
| 18492 | s 1282(2) 150ZA(1) | encoded | `s 1282(2) 150ZA(1) the expenses of winding up have priority over claims to property comprised in or subject to a floating charge`; `s 1282(2) 150ZA(1) the amount of the expenses that has priority over floating charge claims` | 3 |  |
| 18493 | s 1282(2) 150ZA(2) lead and (a) -- "(2) In paragraph (1)—" | encoded | `s 1282(2) 150ZA(2)(a) the assets of the company available for payment of general creditors` | 1 |  |
| 18494 | s 1282(2) 150ZA(2) lead and (a) -- "(a) the reference to assets of the c..." | encoded | 〃 | 〃 |  |
| 18495 | s 1282(2) 150ZA(2)(b) lead, (i), (ii) -- "(b) the reference to claims to prope..." | encoded | `s 1282(2) 150ZA(2)(b) the claim is a claim to property comprised in or subject to a floating charge` | 2 |  |
| 18496 | s 1282(2) 150ZA(2)(b) lead, (i), (ii) -- "(i) the holders of debentures secure..." | encoded | 〃 | 〃 |  |
| 18497 | s 1282(2) 150ZA(2)(b) lead, (i), (ii) -- "(ii) any preferential creditors enti..." | encoded | 〃 | 〃 |  |
| 18498 | s 1282(2) 150ZA(3) lead | inert 2 |  |  | rule-making power |
| 18499 | s 1282(2) 150ZA(3)(a) | inert 2 |  |  | rule-making power |
| 18500 | s 1282(2) 150ZA(3)(b) | inert 2 |  |  | rule-making power |
| 18501 | s 1282(2) 150ZA(4) | encoded | `s 1282(2) 150ZA(4) the expense is an expense of the winding up` | 2 |  |
| 18502 | Part 44 group heading: Commonhold associations | inert 1 |  |  | cross-heading |
| 18503 | s 1283 heading | inert 1 |  |  | section heading |
| 18504 | s 1283 | encoded | `s 1283 paragraph 3(1) of Schedule 3 to the Commonhold and Leasehold Reform Act 2002 applies to the alteration` | 3 | the instruction and the substituted words are one sentence; the substituted words are encoded |
| 18505 | Part 45 title | inert 1 |  |  | Part title |
| 18506 | s 1284 heading | inert 1 |  |  | section heading |
| 18507 | s 1284(1) | encoded | `s 1284(1) the provision extends to Northern Ireland`; `s 1284(2) instrument` | 10 |  |
| 18508 | s 1284(2) | encoded | `s 1284(2) the instrument ceases to have effect` | 4 |  |
| 18509 | s 1285 heading | inert 1 |  |  | section heading |
| 18510 | s 1285(1) | encoded | `s 1285(1) the enactment extends to Northern Ireland`; `s 1285(2) enactment` | 6 |  |
| 18511 | s 1285(2) lead, (a), (b) -- "(2) The following enactments shall c..." | encoded | `s 1285(2) the enactment ceases to have effect` | 3 |  |
| 18512 | s 1285(2) lead, (a), (b) -- "(a) the European Public Limited-Liab..." | encoded | 〃 | 〃 |  |
| 18513 | s 1285(2) lead, (a), (b) -- "(b) the European Public Limited-Liab..." | encoded | 〃 | 〃 |  |
| 18514 | s 1285(3) | encoded | `s 1285(3) the entity is a UK Societas`; `s 1286(1) form of business organisation` | 9 |  |
| 18515 | s 1286 heading | inert 1 |  |  | section heading |
| 18516 | s 1286(1) lead, (a) to (e), closing words -- "(1) The enactments in force in Great..." | encoded | `s 1286(1) the enactments in force in Great Britain relating to the form extend to Northern Ireland`; `s 1286(2) enactment` | 11 | the text shows '...' after item (c) and does not say what it stands for; items (a) to (e) are encoded as printed |
| 18517 | s 1286(1) lead, (a) to (e), closing words -- "(a) limited liability partnerships," | encoded | 〃 | 〃 | 〃 |
| 18518 | s 1286(1) lead, (a) to (e), closing words -- "(b) limited partnerships," | encoded | 〃 | 〃 | 〃 |
| 18519 | s 1286(1) lead, (a) to (e), closing words -- "(c) open-ended investment companies,..." | encoded | 〃 | 〃 | 〃 |
| 18520 | s 1286(1) lead, (a) to (e), closing words -- "(d) European Economic Interest Group..." | encoded | 〃 | 〃 | 〃 |
| 18521 | s 1286(1) lead, (a) to (e), closing words -- "(e) UK Economic Interest Groupings," | encoded | 〃 | 〃 | 〃 |
| 18522 | s 1286(1) lead, (a) to (e), closing words -- "extend to Northern Ireland." | encoded | 〃 | 〃 | 〃 |
| 18523 | s 1286(2) lead, (a) to (d) -- "(2) The following enactments shall c..." | encoded | `s 1286(2) the enactment ceases to have effect` | 5 |  |
| 18524 | s 1286(2) lead, (a) to (d) -- "(a) the Limited Liability Partnershi..." | encoded | 〃 | 〃 |  |
| 18525 | s 1286(2) lead, (a) to (d) -- "(b) the Limited Partnerships Act 190..." | encoded | 〃 | 〃 |  |
| 18526 | s 1286(2) lead, (a) to (d) -- "(c) the Open-Ended Investment Compan..." | encoded | 〃 | 〃 |  |
| 18527 | s 1286(2) lead, (a) to (d) -- "(d) the European Economic Interest G..." | encoded | 〃 | 〃 |  |
| 18528 | s 1287 heading | inert 1 |  |  | section heading |
| 18529 | s 1287(1) | encoded | `s 1287(1) the provision extends to Northern Ireland`; `s 1287(2) instrument` | 4 |  |
| 18530 | s 1287(2) | encoded | `s 1287(2) the instrument ceases to have effect` | 2 |  |
| 18531 | Part 46 title | inert 1 |  |  | Part title |
| 18532 | Part 46 group heading: Regulations and orders | inert 1 |  |  | cross-heading |
| 18533 | s 1288 heading | inert 1 |  |  | section heading |
| 18534 | s 1288 | encoded | `s 1288 the regulations or order under this Act must be made by statutory instrument` | 2 |  |
| 18535 | s 1289 heading | inert 1 |  |  | section heading |
| 18536 | s 1289 | encoded | `s 1289 the statutory instrument is subject to annulment in pursuance of a resolution of either House of Parliament` | 4 |  |
| 18537 | s 1290 heading | inert 1 |  |  | section heading |
| 18538 | s 1290 | encoded | `s 1290 the regulations or order are barred from being made`; `s 1291(2) kind of interval`; `s 1291(2) interval` | 7 |  |
| 18539 | s 1291 heading | inert 1 |  |  | section heading |
| 18540 | s 1291(1) lead and (a) -- "(1) Regulations or orders under this..." | encoded | `s 1291(1)(a) the requirement to lay the regulations or order before Parliament after being made has been met` | 2 |  |
| 18541 | s 1291(1) lead and (a) -- "(a) must be laid before Parliament a..." | encoded | 〃 | 〃 |  |
| 18542 | s 1291(1)(b) | fork (F2) | `s 1291(1)(b) the last day of the 28 days beginning with the day on which they were made`; `s 1291(1)(b) the regulations or order have ceased to have effect`; `s 1291(3) thing` | 18 | fork F2 |
| 18543 | s 1291(2) | fork (F1) | `s 1291(2) no account is taken of the time in the interval`; `s 1291(2) the day falls in a time that is not taken into account`; `s 1291(2) the day on which the last of the days to count falls` | 13 | fork F1 |
| 18544 | s 1291(3) lead, (a), (b) -- "(3) The regulations or order ceasing..." | encoded | `s 1291(3) the regulations or order ceasing to have effect affects the thing` | 3 |  |
| 18545 | s 1291(3) lead, (a), (b) -- "(a) anything previously done under t..." | encoded | 〃 | 〃 |  |
| 18546 | s 1291(3) lead, (a), (b) -- "(b) the making of new regulations or..." | encoded | 〃 | 〃 |  |
| 18547 | s 1292 heading | inert 1 |  |  | section heading |
| 18548 | s 1292(1) lead | inert 2 |  |  | regulation- and order-making power |
| 18549 | s 1292(1)(a) | inert 2 |  |  | regulation- and order-making power |
| 18550 | s 1292(1)(b) | inert 2 |  |  | regulation- and order-making power |
| 18551 | s 1292(1)(c) | inert 2 |  |  | regulation- and order-making power |
| 18552 | s 1292(2) | encoded | `s 1292(2) the provision may be made by order`; `s 1292(2) the provision may be made by regulations` | 4 |  |
| 18553 | s 1292(3) | encoded | `s 1292(3) the provision may be made subject to the procedure` | 5 |  |
| 18554 | s 1292(4) | encoded | `s 1292(4) the provision may be made subject to affirmative resolution procedure` | 2 |  |
| 18555 | Part 46 group heading: Bank of England | inert 1 |  |  | cross-heading |
| 18556 | s 1292A heading | inert 1 |  |  | section heading |
| 18557 | s 1292A | encoded | `s 1292A the reference to the Bank of England includes the Bank acting as the Prudential Regulation Authority`; `s 1293 kind of provision` | 10 |  |
| 18558 | Part 46 group heading: Meaning of enactment | inert 1 |  |  | cross-heading |
| 18559 | s 1293 heading | inert 1 |  |  | section heading |
| 18560 | s 1293 lead, (a), (aa), (b), (c) -- "In this Act, unless the context othe..." | encoded | `s 1293 the provision is an enactment` | 6 |  |
| 18561 | s 1293 lead, (a), (aa), (b), (c) -- "(a) an enactment contained in subord..." | encoded | 〃 | 〃 |  |
| 18562 | s 1293 lead, (a), (aa), (b), (c) -- "(aa) an enactment contained in, or i..." | encoded | 〃 | 〃 |  |
| 18563 | s 1293 lead, (a), (aa), (b), (c) -- "(b) an enactment contained in, or in..." | encoded | 〃 | 〃 |  |
| 18564 | s 1293 lead, (a), (aa), (b), (c) -- "(c) an enactment contained in, or in..." | encoded | 〃 | 〃 |  |
| 18565 | Part 46 group heading: Consequential and transitional provisions | inert 1 |  |  | cross-heading |
| 18566 | s 1294 heading | inert 1 |  |  | section heading |
| 18567 | s 1294(1) | inert 2 |  |  | order-making power (consequential amendments) |
| 18568 | s 1294(2) lead | inert 2 |  |  | order-making power |
| 18569 | s 1294(2)(a) | inert 2 |  |  | order-making power |
| 18570 | s 1294(2)(b) | inert 2 |  |  | order-making power |
| 18571 | s 1294(2)(c) | inert 2 |  |  | order-making power |
| 18572 | s 1294(3) lead | inert 2 |  |  | order-making power |
| 18573 | s 1294(3)(a) | inert 2 |  |  | order-making power |
| 18574 | s 1294(3)(b) | inert 2 |  |  | order-making power |
| 18575 | s 1294(3) closing words | inert 2 |  |  | order-making power |
| 18576 | s 1294(4) | inert 2 |  |  | order-making power |
| 18577 | s 1294(5) | inert 2 |  |  | order-making power (additional to other amendments and repeals) |
| 18578 | s 1294(6) | encoded | `s 1294(6) the procedure for an order under section 1294` | 1 |  |
| 18579 | s 1295 heading | inert 1 |  |  | section heading |
| 18580 | s 1295 | inert 2 |  |  | repeals of other enactments (Schedule 16 is another part's range) |
| 18581 | s 1296 heading | inert 1 |  |  | section heading |
| 18582 | s 1296(1) | inert 2 |  |  | order-making power (transitional provision and savings) |
| 18583 | s 1296(2) | inert 2 |  |  | order-making power |
| 18584 | s 1296(3) | inert 2 |  |  | order-making power |
| 18585 | s 1296(4) | encoded | `s 1296(4) the procedure for an order under section 1296` | 1 |  |
| 18586 | s 1297 heading | inert 1 |  |  | section heading |
| 18587 | s 1297(1) | encoded | `s 1297(1) section 1297 applies` | 2 |  |
| 18588 | s 1297(2) | encoded | `s 1297(2) the repeal and re-enactment affects the continuity of the law` | 3 |  |
| 18589 | s 1297(3) | encoded | `s 1297(3) the thing has effect thereafter as if done under or for the purposes of the corresponding provision of this Act` | 6 |  |
| 18590 | s 1297(4) | encoded | `s 1297(4) the reference to the provision of this Act is construed as including a reference to the corresponding repealed provision` | 6 |  |
| 18591 | s 1297(5) | encoded | `s 1297(5) the reference to the repealed provision is construed as being or including a reference to the corresponding provision of this Act` | 4 |  |
| 18592 | s 1297(6) | encoded | `s 1297(6) section 1297 yields to a specific transitional provision or saving` | 2 |  |
| 18593 | s 1297(7) | encoded | `s 1297(7) the reference to this Act includes the instrument` | 3 |  |
| 18594 | s 1297(8) | encoded | `s 1297(8) the instrument is subordinate legislation for section 1297` | 3 |  |
| 18595 | Part 47 title | inert 1 |  |  | Part title |
| 18596 | s 1298 heading | inert 1 |  |  | section heading |
| 18597 | s 1298 | inert 2 |  |  | short title of the Act |
| 18598 | s 1299 heading | inert 1 |  |  | section heading |
| 18599 | s 1299 | encoded | `s 1299 the provision extends to the whole of the United Kingdom` | 3 |  |
| 18600 | s 1300 heading | inert 1 |  |  | section heading |
| 18601 | s 1300(1) lead | inert 2 |  |  | the Act's own commencement |
| 18602 | s 1300(1)(a) | inert 2 |  |  | the Act's own commencement |
| 18603 | s 1300(1)(b) lead | inert 2 |  |  | the Act's own commencement |
| 18604 | s 1300(1)(b) first bullet (s 1274) | inert 2 |  |  | the Act's own commencement |
| 18605 | s 1300(1)(b) second bullet (s 1276) | inert 2 |  |  | the Act's own commencement |
| 18606 | s 1300(1)(c) | inert 2 |  |  | the Act's own commencement |
| 18607 | s 1300(1)(d) | inert 2 |  |  | the Act's own commencement |
| 18608 | s 1300(2) | inert 2 |  |  | the Act's own commencement (commencement by order) |
| 18609 | SCHEDULES divider | inert 1 |  |  | divider |
| 18610 | Schedule 1 title | inert 1 |  |  | Schedule title |
| 18611 | Schedule 1 reference line (Sections 254 and 255) | inert 1 |  |  | reference line |
| 18612 | Schedule 1 group heading: Introduction | inert 1 |  |  | cross-heading |
| 18613 | sch 1 para 1(1) | encoded | `sch 1 para 1(1) the provisions of this Schedule govern the reference`; `sch 1 para 1(2) kind of security` | 5 |  |
| 18614 | sch 1 para 1(2) | encoded | `sch 1 para 1(2) the provisions of this Schedule apply to the security` | 3 |  |
| 18615 | Schedule 1 group heading: General provisions | inert 1 |  |  | cross-heading |
| 18616 | sch 1 para 2(1) | encoded | `sch 1 para 2(1) the person has an interest in the shares` | 2 |  |
| 18617 | sch 1 para 2(2) | encoded | `sch 1 para 2(2) the restraint or restriction is disregarded` | 2 |  |
| 18618 | sch 1 para 2(3) | encoded | `sch 1 para 2(3) the lack of identifiability of the shares matters to the interest` | 2 |  |
| 18619 | sch 1 para 2(4) | encoded | `sch 1 para 2(4) the person is deemed to have the interest` | 2 |  |
| 18620 | Schedule 1 group heading: Rights to acquire shares | inert 1 |  |  | cross-heading |
| 18621 | sch 1 para 3(1) | encoded | `sch 1 para 3(1) the person is taken to have an interest in the shares by entering into a contract to acquire them` | 2 |  |
| 18622 | sch 1 para 3(2) lead, (a), (b), closing words -- "(2) A person is taken to have an int..." | encoded | `sch 1 para 3(2) the person is taken to have an interest in the shares by a right to call for delivery or a right or obligation to acquire an interest` | 5 |  |
| 18623 | sch 1 para 3(2) lead, (a), (b), closing words -- "(a) he has a right to call for deliv..." | encoded | 〃 | 〃 |  |
| 18624 | sch 1 para 3(2) lead, (a), (b), closing words -- "(b) he has a right to acquire an int..." | encoded | 〃 | 〃 |  |
| 18625 | sch 1 para 3(2) lead, (a), (b), closing words -- "whether the right or obligation is c..." | encoded | 〃 | 〃 |  |
| 18626 | sch 1 para 3(3) | encoded | `sch 1 para 3(3) the right or obligation is to be taken to be a right to acquire, or an obligation to take, an interest in shares for sub-paragraph (2)` | 2 |  |
| 18627 | sch 1 para 3(4) lead, (a), (i), (ii), (b), (c) -- "(4) A person ceases to have an inter..." | encoded | `sch 1 para 3(4) the person ceases to have an interest in the shares by virtue of paragraph 3` | 5 |  |
| 18628 | sch 1 para 3(4) lead, (a), (i), (ii), (b), (c) -- "(a) on the shares being delivered to..." | encoded | 〃 | 〃 |  |
| 18629 | sch 1 para 3(4) lead, (a), (i), (ii), (b), (c) -- "(i) in fulfilment of a contract for ..." | encoded | 〃 | 〃 |  |
| 18630 | sch 1 para 3(4) lead, (a), (i), (ii), (b), (c) -- "(ii) in satisfaction of a right of h..." | encoded | 〃 | 〃 |  |
| 18631 | sch 1 para 3(4) lead, (a), (i), (ii), (b), (c) -- "(b) on a failure to deliver the shar..." | encoded | 〃 | 〃 |  |
| 18632 | sch 1 para 3(4) lead, (a), (i), (ii), (b), (c) -- "(c) on the lapse of his right to cal..." | encoded | 〃 | 〃 |  |
| 18633 | Schedule 1 group heading: Right to exercise or control exercise of rights | inert 1 |  |  | cross-heading |
| 18634 | sch 1 para 4(1) lead, (a), (b) -- "4 (1) A person is taken to have an i..." | encoded | `sch 1 para 4(1) the person is taken to have an interest in the shares by an entitlement to exercise or control the exercise of a right` | 5 |  |
| 18635 | sch 1 para 4(1) lead, (a), (b) -- "(a) to exercise any right conferred ..." | encoded | 〃 | 〃 |  |
| 18636 | sch 1 para 4(1) lead, (a), (b) -- "(b) to control the exercise of any s..." | encoded | 〃 | 〃 |  |
| 18637 | sch 1 para 4(2) lead, (a), (b) -- "(2) For this purpose a person is tak..." | encoded | `sch 1 para 4(2) the person is taken to be entitled to exercise or control the exercise of a right conferred by the holding of shares` | 3 |  |
| 18638 | sch 1 para 4(2) lead, (a), (b) -- "(a) has a right (whether subject to ..." | encoded | 〃 | 〃 |  |
| 18639 | sch 1 para 4(2) lead, (a), (b) -- "(b) is under an obligation (whether ..." | encoded | 〃 | 〃 |  |
| 18640 | sch 1 para 4(3) lead, (a), (b) -- "(3) A person is not by virtue of thi..." | encoded | `sch 1 para 4(3) the person is taken by virtue of paragraph 4 to be interested in the shares by reason only of the appointment` | 4 |  |
| 18641 | sch 1 para 4(3) lead, (a), (b) -- "(a) he has been appointed a proxy to..." | encoded | 〃 | 〃 |  |
| 18642 | sch 1 para 4(3) lead, (a), (b) -- "(b) he has been appointed by a body ..." | encoded | 〃 | 〃 |  |
| 18643 | Schedule 1 group heading: Bodies corporate | inert 1 |  |  | cross-heading |
| 18644 | sch 1 para 5(1) lead, (a), (b) -- "5 (1) A person is taken to be intere..." | encoded | `sch 1 para 5(1)(b) the person is entitled to exercise or control the exercise of more than one-half of the voting power at general meetings of the body corporate`; `sch 1 para 5(1) the person is taken to be interested in the shares because a body corporate is interested in them` | 9 |  |
| 18645 | sch 1 para 5(1) lead, (a), (b) -- "(a) the body corporate or its direct..." | encoded | 〃 | 〃 |  |
| 18646 | sch 1 para 5(1) lead, (a), (b) -- "(b) he is entitled to exercise or co..." | encoded | 〃 | 〃 |  |
| 18647 | sch 1 para 5(2) lead, (a), (b), closing words -- "(2) For the purposes of sub-paragrap..." | encoded | `sch 1 para 5(2) the voting power of the other body corporate is taken to be exercisable by the person` | 3 |  |
| 18648 | sch 1 para 5(2) lead, (a), (b), closing words -- "(a) a person is entitled to exercise..." | encoded | 〃 | 〃 |  |
| 18649 | sch 1 para 5(2) lead, (a), (b), closing words -- "(b) that body corporate is entitled ..." | encoded | 〃 | 〃 |  |
| 18650 | sch 1 para 5(2) lead, (a), (b), closing words -- "the voting power mentioned in paragr..." | encoded | 〃 | 〃 |  |
| 18651 | Schedule 1 group heading: Trusts | inert 1 |  |  | cross-heading |
| 18652 | sch 1 para 6(1) | encoded | `sch 1 para 6(1) the beneficiary is taken to have an interest in the shares` | 3 |  |
| 18653 | sch 1 para 6(2) | encoded | `sch 1 para 6(2) the interest in reversion, remainder or fee is disregarded` | 3 |  |
| 18654 | sch 1 para 6(3) lead, (a), (b) -- "(3) A person is treated as not inter..." | encoded | `sch 1 para 6(3) the person is treated as not interested in the shares`; `sch 1 para 6(4) basis of the interest` | 7 |  |
| 18655 | sch 1 para 6(3) lead, (a), (b) -- "(a) under the law in force in any pa..." | encoded | 〃 | 〃 |  |
| 18656 | sch 1 para 6(3) lead, (a), (b) -- "(b) under the law in force in Scotla..." | encoded | 〃 | 〃 |  |
| 18657 | sch 1 para 6(4) lead, (a), (b), (c) -- "(4) There shall be disregarded any i..." | encoded | `sch 1 para 6(4) the interest is disregarded`; `sch 1 para 6(5) interest` | 7 |  |
| 18658 | sch 1 para 6(4) lead, (a), (b), (c) -- "(a) an authorised unit trust scheme ..." | encoded | 〃 | 〃 |  |
| 18659 | sch 1 para 6(4) lead, (a), (b), (c) -- "(b) a scheme made under section 22 o..." | encoded | 〃 | 〃 |  |
| 18660 | sch 1 para 6(4) lead, (a), (b), (c) -- "(c) the scheme set out in the Schedu..." | encoded | 〃 | 〃 |  |
| 18661 | sch 1 para 6(5) lead, (a), (b) -- "(5) There shall be disregarded any i..." | encoded | `sch 1 para 6(5) the interest is disregarded`; `sch 1 para 6(5) body` | 6 |  |
| 18662 | sch 1 para 6(5) lead, (a), (b) -- "(a) of the Church of Scotland Genera..." | encoded | 〃 | 〃 |  |
| 18663 | sch 1 para 6(5) lead, (a), (b) -- "(b) of any other person in shares he..." | encoded | 〃 | 〃 |  |
| 18664 | sch 1 para 6(5) definitions of the Church of Scotland bodies | encoded | `sch 1 para 6(5) the body is the Church of Scotland General Trustees or the Church of Scotland Trust`; `sch 1 para 3 the person has an interest in the shares by virtue of paragraph 3`; `sch 1 para 4 the person has an interest in the shares by virtue of paragraph 4`; `sch 1 para 6 the beneficiary has an interest in the shares by virtue of paragraph 6`; `sch 1 paras 2 to 6 the person has an interest in the shares or debentures for sections 254 and 255` | 22 |  |
| 18665 | Schedule 1A title | inert 1 |  |  | Schedule title |
| 18666 | Schedule 1A reference line (Section 790C) | inert 1 |  |  | reference line |
| 18667 | Schedule 1A Part 1 title | inert 1 |  |  | Part title |
| 18668 | Schedule 1A group heading: Introduction | inert 1 |  |  | cross-heading |
| 18669 | sch 1A para 1 | encoded | `sch 1A para 1 at least one of the specified conditions is met by X in relation to company Y` | 4 |  |
| 18670 | Schedule 1A group heading: Ownership of shares | inert 1 |  |  | cross-heading |
| 18671 | sch 1A para 2 | fork (F4) | `sch 1A para 2 the first condition is met` | 8 | fork F4 (what 'holds directly' means: the Schedule does not say) |
| 18672 | Schedule 1A group heading: Ownership of voting rights | inert 1 |  |  | cross-heading |
| 18673 | sch 1A para 3 | encoded | `sch 1A para 3 the second condition is met` | 5 |  |
| 18674 | Schedule 1A group heading: Ownership of right to appoint or remove directors | inert 1 |  |  | cross-heading |
| 18675 | sch 1A para 4 | encoded | `sch 1A para 4 the third condition is met` | 3 |  |
| 18676 | Schedule 1A group heading: Significant influence or control | inert 1 |  |  | cross-heading |
| 18677 | sch 1A para 5 | encoded | `sch 1A para 5 the fourth condition is met` | 3 |  |
| 18678 | Schedule 1A group heading: Trusts, partnerships etc | inert 1 |  |  | cross-heading |
| 18679 | sch 1A para 6 lead, (a), (b) -- "6 The fifth condition is that—" | encoded | `sch 1A para 6 the fifth condition is met` | 5 |  |
| 18680 | sch 1A para 6 lead, (a), (b) -- "(a) the trustees of a trust or the m..." | encoded | 〃 | 〃 |  |
| 18681 | sch 1A para 6 lead, (a), (b) -- "(b) X has the right to exercise, or ..." | encoded | 〃 | 〃 |  |
| 18682 | Schedule 1A Part 2 title | inert 1 |  |  | Part title |
| 18683 | Schedule 1A group heading: Introduction (Part 2) | inert 1 |  |  | cross-heading |
| 18684 | sch 1A para 7 lead, (a), (b) -- "7 This Part of this Schedule specifi..." | inert 1 |  |  | says what Part 2 is for (the circumstances in which an interest is held, or held through a legal entity); the rules are in paras 8 and 9: a purpose statement that creates no rule |
| 18685 | sch 1A para 7 lead, (a), (b) -- "(a) a person (“V”) is to be regarded..." | inert 1 |  |  | 〃 |
| 18686 | sch 1A para 7 lead, (a), (b) -- "(b) an interest held by V in company..." | inert 1 |  |  | 〃 |
| 18687 | Schedule 1A group heading: Holding an interest | inert 1 |  |  | cross-heading |
| 18688 | sch 1A para 8(1) lead, (a) to (e) -- "8 (1) V holds an interest in company..." | encoded | `sch 1A para 8(1) V holds an interest in company W` | 7 |  |
| 18689 | sch 1A para 8(1) lead, (a) to (e) -- "(a) V holds shares in company W, dir..." | encoded | 〃 | 〃 |  |
| 18690 | sch 1A para 8(1) lead, (a) to (e) -- "(b) V holds, directly or indirectly,..." | encoded | 〃 | 〃 |  |
| 18691 | sch 1A para 8(1) lead, (a) to (e) -- "(c) V holds, directly or indirectly,..." | encoded | 〃 | 〃 |  |
| 18692 | sch 1A para 8(1) lead, (a) to (e) -- "(d) V has the right to exercise, or ..." | encoded | 〃 | 〃 |  |
| 18693 | sch 1A para 8(1) lead, (a) to (e) -- "(e) sub-paragraph (2) is satisfied." | encoded | 〃 | 〃 |  |
| 18694 | sch 1A para 8(2) lead, (a), (b) -- "(2) This sub-paragraph is satisfied ..." | encoded | `sch 1A para 8(2) this sub-paragraph is satisfied` | 3 |  |
| 18695 | sch 1A para 8(2) lead, (a), (b) -- "(a) the trustees of a trust or the m..." | encoded | 〃 | 〃 |  |
| 18696 | sch 1A para 8(2) lead, (a), (b) -- "(b) V has the right to exercise, or ..." | encoded | 〃 | 〃 |  |
| 18697 | Schedule 1A group heading: Interests held through a legal entity | inert 1 |  |  | cross-heading |
| 18698 | sch 1A para 9(1) lead, (a), (b), (i), (ii) -- "9 (1) This paragraph applies where V..." | encoded | `sch 1A para 9(1) paragraph 9 applies`; `sch 1A para 9(2) legal entity` | 8 |  |
| 18699 | sch 1A para 9(1) lead, (a), (b), (i), (ii) -- "(a) holds an interest in company W b..." | encoded | 〃 | 〃 |  |
| 18700 | sch 1A para 9(1) lead, (a), (b), (i), (ii) -- "(b) does so by virtue of having a ma..." | encoded | 〃 | 〃 |  |
| 18701 | sch 1A para 9(1) lead, (a), (b), (i), (ii) -- "(i) a legal entity (“L”) which holds..." | encoded | 〃 | 〃 |  |
| 18702 | sch 1A para 9(1) lead, (a), (b), (i), (ii) -- "(ii) a legal entity that is part of ..." | encoded | 〃 | 〃 |  |
| 18703 | sch 1A para 9(2) lead, (a), (b) -- "(2) Where this paragraph applies, V ..." | encoded | `sch 1A para 9(2) V holds the interest in company W through the legal entity` | 5 |  |
| 18704 | sch 1A para 9(2) lead, (a), (b) -- "(a) through L, and" | encoded | 〃 | 〃 |  |
| 18705 | sch 1A para 9(2) lead, (a), (b) -- "(b) through each other legal entity ..." | encoded | 〃 | 〃 |  |
| 18706 | Schedule 1A Part 3 title | inert 1 |  |  | Part title |
| 18707 | Schedule 1A group heading: Introduction (Part 3) | inert 1 |  |  | cross-heading |
| 18708 | sch 1A para 10 | inert 1 |  |  | says what Part 3 is for (rules of interpretation); the rules are in paras 11 to 25: a purpose statement that creates no rule |
| 18709 | Schedule 1A group heading: Joint interests | inert 1 |  |  | cross-heading |
| 18710 | sch 1A para 11 | encoded | `sch 1A para 11 the person is treated as holding the share or right` | 2 |  |
| 18711 | Schedule 1A group heading: Joint arrangements | inert 1 |  |  | cross-heading |
| 18712 | sch 1A para 12(1) | encoded | `sch 1A para 12(1) the person is treated as holding the combined shares or rights of both` | 2 |  |
| 18713 | sch 1A para 12(2) | encoded | `sch 1A para 12(2) the arrangement is a joint arrangement` | 4 |  |
| 18714 | sch 1A para 12(3) | encoded | `sch 1A para 12(3) the thing is an arrangement as paragraph 21 gives the meaning` | 2 |  |
| 18715 | Schedule 1A group heading: Calculating shareholdings | inert 1 |  |  | cross-heading |
| 18716 | sch 1A para 13(1) | encoded | `sch 1A para 13(1) the person holds more than 25% of the shares in the legal entity that has a share capital` | 5 |  |
| 18717 | sch 1A para 13(2) lead and (a) -- "(2) In relation to a legal entity th..." | encoded | `sch 1A para 13(2)(a) the right is a holding of shares in the legal entity that does not have a share capital`; `sch 1A para 13(2)(b) the person holds more than 25% of the shares in the legal entity that does not have a share capital` | 7 |  |
| 18718 | sch 1A para 13(2) lead and (a) -- "(a) a reference to holding shares in..." | encoded | 〃 | 〃 |  |
| 18719 | sch 1A para 13(2)(b) | encoded | `sch 1A para 13(2)(b) the person holds more than 25% of the shares in the legal entity that does not have a share capital` | 4 |  |
| 18720 | Schedule 1A group heading: Voting rights | inert 1 |  |  | cross-heading |
| 18721 | sch 1A para 14(1) | encoded | `sch 1A para 14(1) the right is a voting right in the legal entity` | 2 |  |
| 18722 | sch 1A para 14(2) lead and (a) -- "(2) In relation to a legal entity th..." | encoded | `sch 1A para 14(2)(a) the right is a right of exercising voting rights in the entity`; `sch 1A para 14(2)(b) the person exercises more than 25% of the voting rights in the entity` | 6 |  |
| 18723 | sch 1A para 14(2) lead and (a) -- "(a) a reference to exercising voting..." | encoded | 〃 | 〃 |  |
| 18724 | sch 1A para 14(2)(b) | encoded | `sch 1A para 14(2)(b) the person exercises more than 25% of the voting rights in the entity` | 3 |  |
| 18725 | sch 1A para 15 | encoded | `sch 1A para 15 the voting rights in the legal entity, reduced by the rights held by the entity itself` | 1 |  |
| 18726 | Schedule 1A group heading: Rights to appoint or remove members of the board | inert 1 |  |  | cross-heading |
| 18727 | sch 1A para 16 | encoded | `sch 1A para 16 the person has the right to appoint or remove a majority of the board of directors` | 3 |  |
| 18728 | sch 1A para 17 | encoded | `sch 1A para 17 the reference to a board of directors is read as a reference to the equivalent management body` | 2 |  |
| 18729 | Schedule 1A group heading: Shares or rights held indirectly | inert 1 |  |  | cross-heading |
| 18730 | sch 1A para 18(1) lead, (a), (b), (i), (ii) -- "18 (1) A person holds a share “indir..." | encoded | `sch 1A para 18(1) the person holds the share indirectly` | 5 |  |
| 18731 | sch 1A para 18(1) lead, (a), (b), (i), (ii) -- "(a) holds the share in question, or" | encoded | 〃 | 〃 |  |
| 18732 | sch 1A para 18(1) lead, (a), (b), (i), (ii) -- "(b) is part of a chain of legal enti..." | encoded | 〃 | 〃 |  |
| 18733 | sch 1A para 18(1) lead, (a), (b), (i), (ii) -- "(i) each of which (other than the la..." | encoded | 〃 | 〃 |  |
| 18734 | sch 1A para 18(1) lead, (a), (b), (i), (ii) -- "(ii) the last of which holds the sha..." | encoded | 〃 | 〃 |  |
| 18735 | sch 1A para 18(2) lead, (a), (b), (i), (ii) -- "(2) A person holds a right “indirect..." | encoded | `sch 1A para 18(2) the person holds the right indirectly` | 5 |  |
| 18736 | sch 1A para 18(2) lead, (a), (b), (i), (ii) -- "(a) holds that right, or" | encoded | 〃 | 〃 |  |
| 18737 | sch 1A para 18(2) lead, (a), (b), (i), (ii) -- "(b) is part of a chain of legal enti..." | encoded | 〃 | 〃 |  |
| 18738 | sch 1A para 18(2) lead, (a), (b), (i), (ii) -- "(i) each of which (other than the la..." | encoded | 〃 | 〃 |  |
| 18739 | sch 1A para 18(2) lead, (a), (b), (i), (ii) -- "(ii) the last of which holds that ri..." | encoded | 〃 | 〃 |  |
| 18740 | sch 1A para 18(3) lead, (a) to (d) -- "(3) For these purposes, A has a “maj..." | encoded | `sch 1A para 18(3) A has a majority stake in B`; `sch 1A para 18(3)(a) A holds a majority of the voting rights in B` | 7 |  |
| 18741 | sch 1A para 18(3) lead, (a) to (d) -- "(a) A holds a majority of the voting..." | encoded | 〃 | 〃 |  |
| 18742 | sch 1A para 18(3) lead, (a) to (d) -- "(b) A is a member of B and has the r..." | encoded | 〃 | 〃 |  |
| 18743 | sch 1A para 18(3) lead, (a) to (d) -- "(c) A is a member of B and controls ..." | encoded | 〃 | 〃 |  |
| 18744 | sch 1A para 18(3) lead, (a) to (d) -- "(d) A has the right to exercise, or ..." | encoded | 〃 | 〃 |  |
| 18745 | sch 1A para 18(4) lead, (a), (b) -- "(4) In the application of this parag..." | encoded | `sch 1A para 18(4) the legal entity is treated as having the right to appoint the director` | 3 |  |
| 18746 | sch 1A para 18(4) lead, (a), (b) -- "(a) a person's appointment as direct..." | encoded | 〃 | 〃 |  |
| 18747 | sch 1A para 18(4) lead, (a), (b) -- "(b) the directorship is held by the ..." | encoded | 〃 | 〃 |  |
| 18748 | Schedule 1A group heading: Shares held by nominees | inert 1 |  |  | cross-heading |
| 18749 | sch 1A para 19 | encoded | `sch 1A para 19 the share is treated as held by the person` | 3 |  |
| 18750 | Schedule 1A group heading: Rights treated as held by person who controls their exercise | inert 1 |  |  | cross-heading |
| 18751 | sch 1A para 20(1) | encoded | `sch 1A para 20(1) the right is treated as held by the person` | 5 |  |
| 18752 | sch 1A para 20(2) lead, (a), (b), (c) -- "(2) A person “controls” a right if, ..." | encoded | `sch 1A para 20(2) the person controls the right` | 4 |  |
| 18753 | sch 1A para 20(2) lead, (a), (b), (c) -- "(a) by that person," | encoded | 〃 | 〃 |  |
| 18754 | sch 1A para 20(2) lead, (a), (b), (c) -- "(b) in accordance with that person's..." | encoded | 〃 | 〃 |  |
| 18755 | sch 1A para 20(2) lead, (a), (b), (c) -- "(c) with that person's consent or co..." | encoded | 〃 | 〃 |  |
| 18756 | sch 1A para 21(1) lead, (a), (b) -- "21 (1) “Arrangement” includes—" | encoded | `sch 1A para 21(1) the thing is an arrangement` | 3 |  |
| 18757 | sch 1A para 21(1) lead, (a), (b) -- "(a) any scheme, agreement or underst..." | encoded | 〃 | 〃 |  |
| 18758 | sch 1A para 21(1) lead, (a), (b) -- "(b) any convention, custom or practi..." | encoded | 〃 | 〃 |  |
| 18759 | sch 1A para 21(2) | encoded | `sch 1A para 21(2) the thing counts as an arrangement`; `sch 1A para 21 the thing is an arrangement for this Schedule` | 5 |  |
| 18760 | Schedule 1A group heading: Rights exercisable only in certain circumstances etc | inert 1 |  |  | cross-heading |
| 18761 | sch 1A para 22(1) lead, (a), (b) -- "22 (1) Rights that are exercisable o..." | encoded | `sch 1A para 22(1) the rights are taken into account` | 4 |  |
| 18762 | sch 1A para 22(1) lead, (a), (b) -- "(a) when the circumstances have aris..." | encoded | 〃 | 〃 |  |
| 18763 | sch 1A para 22(1) lead, (a), (b) -- "(b) when the circumstances are withi..." | encoded | 〃 | 〃 |  |
| 18764 | sch 1A para 22(2) | encoded | `sch 1A para 22(2) the rights are taken into account even while the entity is in those proceedings` | 3 |  |
| 18765 | sch 1A para 22(3) lead, (a), (b), (c) -- "(3) “Relevant insolvency proceedings..." | encoded | `sch 1A para 22(3) the proceedings are relevant insolvency proceedings` | 4 |  |
| 18766 | sch 1A para 22(3) lead, (a), (b), (c) -- "(a) administration within the meanin..." | encoded | 〃 | 〃 |  |
| 18767 | sch 1A para 22(3) lead, (a), (b), (c) -- "(b) administration within the meanin..." | encoded | 〃 | 〃 |  |
| 18768 | sch 1A para 22(3) lead, (a), (b), (c) -- "(c) proceedings under the insolvency..." | encoded | 〃 | 〃 |  |
| 18769 | sch 1A para 22(4) | encoded | `sch 1A para 22(4) the rights continue to be taken into account` | 2 |  |
| 18770 | Schedule 1A group heading: Rights attached to shares held by way of security | inert 1 |  |  | cross-heading |
| 18771 | sch 1A para 23 lead, (a), (b) -- "23 Rights attached to shares held by..." | fork (F5) | `sch 1A para 23 the rights are treated as held by the person who provided the security`; `sch 1A paras 11 to 23 the block is treated as held by X`; `sch 1A paras 11 to 23 the amount counted as held by X`; `sch 1A paras 11 to 23 the further amount that might be counted as held by X` | 22 | fork F5 ((a) and (b) joined by 'and') |
| 18772 | sch 1A para 23 lead, (a), (b) -- "(a) where apart from the right to ex..." | fork (F5) | 〃 | 〃 | 〃 |
| 18773 | sch 1A para 23 lead, (a), (b) -- "(b) where the shares are held in con..." | fork (F5) | 〃 | 〃 | 〃 |
| 18774 | Schedule 1A group heading: Significant influence or control (para 24) | inert 1 |  |  | cross-heading |
| 18775 | sch 1A para 24(1) | encoded | `sch 1A para 24(1) the Secretary of State has issued the guidance` | 2 |  |
| 18776 | sch 1A para 24(2) | encoded | `sch 1A para 24(2) regard must be had to the guidance` | 3 |  |
| 18777 | sch 1A para 24(3) | encoded | `sch 1A para 24(3) the Secretary of State has laid a draft of the guidance before Parliament before issuing it` | 2 |  |
| 18778 | sch 1A para 24(4) | encoded | `sch 1A para 24(4) the Secretary of State must take no further steps in relation to the draft` | 5 |  |
| 18779 | sch 1A para 24(5) | encoded | `sch 1A para 24(5) the Secretary of State must issue and publish the guidance in the form of the draft` | 4 |  |
| 18780 | sch 1A para 24(6) | encoded | `sch 1A para 24(6) sub-paragraph (4) prevents a new draft of proposed guidance from being laid before Parliament` | 2 |  |
| 18781 | sch 1A para 24(7) | encoded | `sch 1A para 24(7) the day on which the 40-day period begins` | 3 |  |
| 18782 | sch 1A para 24(8) lead, (a), (b) -- "(8) In calculating the 40-day period..." | encoded | `sch 1A para 24(8) the last day of the 40-day period` | 2 |  |
| 18783 | sch 1A para 24(8) lead, (a), (b) -- "(a) Parliament is dissolved or proro..." | encoded | 〃 | 〃 |  |
| 18784 | sch 1A para 24(8) lead, (a), (b) -- "(b) both Houses are adjourned for mo..." | encoded | 〃 | 〃 |  |
| 18785 | sch 1A para 24(9) first limb (power to revise guidance) | inert 2 | `sch 1A para 24(9) the reference in paragraph 24 to guidance covers the guidance` | 2 | a power of the Secretary of State |
| 18785 | sch 1A para 24(9) second limb (guidance includes revised guidance) | encoded | 〃 | 〃 |  |
| 18786 | Schedule 1A group heading: Limited partnerships | inert 1 |  |  | cross-heading |
| 18787 | sch 1A para 25(1) | encoded | `sch 1A para 25(1) the individual meets the specified condition by virtue only of being a limited partner` | 2 |  |
| 18788 | sch 1A para 25(2) lead, (a), (b), closing words -- "(2) An individual does not meet the ..." | encoded | `sch 1A para 25(2) the individual meets the specified condition by virtue only of holding shares or a right in or in relation to a limited partner` | 2 |  |
| 18789 | sch 1A para 25(2) lead, (a), (b), closing words -- "(a) holding shares, or" | encoded | 〃 | 〃 |  |
| 18790 | sch 1A para 25(2) lead, (a), (b), closing words -- "(b) holding a right," | encoded | 〃 | 〃 |  |
| 18791 | sch 1A para 25(2) lead, (a), (b), closing words -- "in or in relation to a limited partn..." | encoded | 〃 | 〃 |  |
| 18792 | sch 1A para 25(3) | encoded | `sch 1A para 25(3) sub-paragraphs (1) and (2) apply`; `sch 1A para 25(4) kind of partner` | 6 |  |
| 18793 | sch 1A para 25(4) lead, (a), (b) -- "(4) In this paragraph “ limited part..." | encoded | `sch 1A para 25(4) the individual is a limited partner for this paragraph` | 4 |  |
| 18794 | sch 1A para 25(4) lead, (a), (b) -- "(a) a limited partner in a limited p..." | encoded | 〃 | 〃 |  |
| 18795 | sch 1A para 25(4) lead, (a), (b) -- "(b) a foreign limited partner." | encoded | 〃 | 〃 |  |
| 18796 | sch 1A para 25(5) lead, (a), (b) -- "(5) In this paragraph “ foreign limi..." | encoded | `sch 1A para 25(5) the individual is a foreign limited partner` | 4 |  |
| 18797 | sch 1A para 25(5) lead, (a), (b) -- "(a) participates in arrangements est..." | encoded | 〃 | 〃 |  |
| 18798 | sch 1A para 25(5) lead, (a), (b) -- "(b) has the characteristics prescrib..." | encoded | 〃 | 〃 |  |
| 18799 | sch 1A para 25(6) lead, (a), (b) -- "(6) Regulations under this paragraph..." | inert 2 |  |  | regulation-making power (prescribing characteristics) |
| 18800 | sch 1A para 25(6) lead, (a), (b) -- "(a) the nature of arrangements;" | inert 2 |  |  | 〃 |
| 18801 | sch 1A para 25(6) lead, (a), (b) -- "(b) the nature of an individual's pa..." | inert 2 |  |  | 〃 |
| 18802 | sch 1A para 25(7) | encoded | `sch 1A para 25(7) the procedure for regulations under paragraph 25` | 1 |  |
| 18803 | Schedule 1A Part 4 title | inert 1 |  |  | Part title |
| 18804 | sch 1A para 26(1) | inert 2 |  |  | regulation-making power (amending the Schedule) |
| 18805 | sch 1A para 26(2) lead | inert 2 |  |  | regulation-making power |
| 18806 | sch 1A para 26(2)(a) | inert 2 |  |  | regulation-making power |
| 18807 | sch 1A para 26(2)(b) | inert 2 |  |  | regulation-making power |
| 18808 | sch 1A para 26(2)(c) | inert 2 |  |  | regulation-making power |
| 18809 | sch 1A para 26(3) | encoded | `sch 1A para 26(3) the procedure for regulations under paragraph 26`; `sch 1A paras 2 to 4 and 25 the individual meets the specified condition` | 5 |  |
| 18810 | Schedule 1B title | inert 1 |  |  | Schedule title |
| 18811 | Schedule 1B reference line (Section 790I) | inert 1 |  |  | reference line |
| 18812 | Schedule 1B group heading: Right to issue restrictions notice | inert 1 |  |  | cross-heading |
| 18813 | sch 1B para 1(1) lead, (a), (b) -- "1 (1) This paragraph applies if—" | encoded | `sch 1B para 1(1) paragraph 1 applies` | 3 |  |
| 18814 | sch 1B para 1(1) lead, (a), (b) -- "(a) a notice under section 790D , 79..." | encoded | 〃 | 〃 |  |
| 18815 | sch 1B para 1(1) lead, (a), (b) -- "(b) the person fails to comply with ..." | encoded | 〃 | 〃 |  |
| 18816 | sch 1B para 1(2) | fork (F11) | `sch 1B para 1(2) the company may give the person a warning notice` | 3 | fork F11 (a "may" function whose "if" gate failed: NOTHING, not "may not") |
| 18817 | sch 1B para 1(3) lead, (a), (b) -- "(3) The company may issue the restri..." | fork (F6) | `sch 1B para 1(3) the last day of the period of one month beginning with the date on which the warning notice was given`; `sch 1B para 1(3) the company may issue the restrictions notice` | 13 | fork F6 ('the period of one month beginning with the date') |
| 18818 | sch 1B para 1(3) lead, (a), (b) -- "(a) the person has not complied with..." | fork (F6) | 〃 | 〃 | 〃 |
| 18819 | sch 1B para 1(3) lead, (a), (b) -- "(b) the company has not been provide..." | fork (F6) | 〃 | 〃 | 〃 |
| 18820 | sch 1B para 1(4) | encoded | `sch 1B para 1(4) the restrictions notice is issued on the person` | 2 |  |
| 18821 | sch 1B para 1(5) | inert 1 |  |  | a signpost to paragraph 3; it creates no rule (reason 1 is read as 'not operative'; see Marginal readings) |
| 18822 | sch 1B para 1(6) | encoded | `sch 1B para 1(6) the company has had regard to the effect of the notice on the rights of third parties`; `sch 1B para 1(6) action`; `sch 1B para 1(6) the company's duty to have regard to the rights of third parties` | 4 |  |
| 18823 | Schedule 1B group heading: Relevant interests | inert 1 |  |  | cross-heading |
| 18824 | sch 1B para 2(1) lead, (a), (b), (c) -- "2 (1) For the purposes of this Sched..." | encoded | `sch 1B para 2(1) the person has a relevant interest in the company` | 4 |  |
| 18825 | sch 1B para 2(1) lead, (a), (b), (c) -- "(a) holds any shares in the company," | encoded | 〃 | 〃 |  |
| 18826 | sch 1B para 2(1) lead, (a), (b), (c) -- "(b) holds any voting rights in the c..." | encoded | 〃 | 〃 |  |
| 18827 | sch 1B para 2(1) lead, (a), (b), (c) -- "(c) holds the right to appoint or re..." | encoded | 〃 | 〃 |  |
| 18828 | sch 1B para 2(2) | encoded | `sch 1B para 2(2) the thing is the relevant interest` | 2 |  |
| 18829 | sch 1B para 2(3) | encoded | `sch 1B para 2(3) the person is regarded as having the relevant interest` | 3 |  |
| 18830 | Schedule 1B group heading: Effect of restrictions notice | inert 1 |  |  | cross-heading |
| 18831 | sch 1B para 3(1) lead, (a) to (d) -- "3 (1) The effect of a restrictions n..." | encoded | `sch 1B para 3(1) the effect of the restrictions notice applies to the act` | 9 |  |
| 18832 | sch 1B para 3(1) lead, (a) to (d) -- "(a) any transfer of the interest is ..." | encoded | 〃 | 〃 |  |
| 18833 | sch 1B para 3(1) lead, (a) to (d) -- "(b) no rights are exercisable in res..." | encoded | 〃 | 〃 |  |
| 18834 | sch 1B para 3(1) lead, (a) to (d) -- "(c) no shares may be issued in right..." | encoded | 〃 | 〃 |  |
| 18835 | sch 1B para 3(1) lead, (a) to (d) -- "(d) except in a liquidation, no paym..." | encoded | 〃 | 〃 |  |
| 18836 | sch 1B para 3(2) | encoded | `sch 1B para 3(2) the agreement to transfer the interest is void` | 3 |  |
| 18837 | sch 1B para 3(3) | encoded | `sch 1B para 3(3) sub-paragraph (2) applies to the agreement` | 2 |  |
| 18838 | sch 1B para 3(4) | encoded | `sch 1B para 3(4) the agreement to transfer the associated right is void` | 4 |  |
| 18839 | sch 1B para 3(5) | encoded | `sch 1B para 3(5) sub-paragraph (4) applies to the agreement` | 2 |  |
| 18840 | sch 1B para 3(6) lead, (a), (b) -- "(6) An “ associated right ”, in rela..." | encoded | `sch 1B para 3(6) the right is an associated right in relation to the relevant interest` | 3 |  |
| 18841 | sch 1B para 3(6) lead, (a), (b) -- "(a) a right to be issued with any sh..." | encoded | 〃 | 〃 |  |
| 18842 | sch 1B para 3(6) lead, (a), (b) -- "(b) a right to receive payment of an..." | encoded | 〃 | 〃 |  |
| 18843 | sch 1B para 3(7) | fork (F7) | `sch 1B para 3(7) the provisions of paragraph 3 are subject to the direction`; `sch 1B para 3(1) act` | 11 | fork F7 ('subject to any directions': a covered act answers NOTHING, not FALSE) |
| 18844 | Schedule 1B group heading: Protection of third party rights | inert 1 |  |  | cross-heading |
| 18845 | sch 1B para 4(1) | fork (F12) | `sch 1B para 4(1) the court may give a direction` | 3 | fork F12 (a "may" function whose "if" gate failed: NOTHING, not "may not") |
| 18846 | sch 1B para 4(2) | inert 1 |  |  | states the purpose of a direction (protecting third party rights); it creates no rule beyond 4(1) and 4(3) |
| 18847 | sch 1B para 4(3) | encoded | `sch 1B para 4(3) the act does not constitute a breach of the restrictions placed on the relevant interest` | 2 |  |
| 18848 | sch 1B para 4(4) lead and (a) -- "(4) An order containing a direction ..." | encoded | `sch 1B para 4(4)(a) the order containing the direction meets the requirement to specify the acts`; `sch 1B para 4(4)(b) the order may confine the direction to cases where the acts are done by persons or for purposes described in the order` | 4 |  |
| 18849 | sch 1B para 4(4) lead and (a) -- "(a) must specify the acts that will ..." | encoded | 〃 | 〃 |  |
| 18850 | sch 1B para 4(4)(b) | encoded | `sch 1B para 4(4)(b) the order may confine the direction to cases where the acts are done by persons or for purposes described in the order` | 2 |  |
| 18851 | sch 1B para 4(5) | encoded | `sch 1B para 4(5) the direction may be given subject to the terms` | 2 |  |
| 18852 | Schedule 1B group heading: Breach of restrictions | inert 1 |  |  | cross-heading |
| 18853 | sch 1B para 5(1) | encoded | `sch 1B para 5(1) the person commits an offence` | 6 |  |
| 18854 | sch 1B para 5(2) lead, (a), (b), (c) -- "(2) The things are—" | encoded | 〃 | 〃 |  |
| 18855 | sch 1B para 5(2) lead, (a), (b), (c) -- "(a) exercising or purporting to exer..." | encoded | 〃 | 〃 |  |
| 18856 | sch 1B para 5(2) lead, (a), (b), (c) -- "(b) exercising or purporting to exer..." | encoded | 〃 | 〃 |  |
| 18857 | sch 1B para 5(2) lead, (a), (b), (c) -- "(c) voting in respect of a relevant ..." | encoded | 〃 | 〃 |  |
| 18858 | sch 1B para 5(3) lead, (a), (b), (c) -- "(3) A person who has a relevant inte..." | encoded | `sch 1B para 5(3) the person commits an offence` | 6 |  |
| 18859 | sch 1B para 5(3) lead, (a), (b), (c) -- "(a) knows a person to be entitled (a..." | encoded | 〃 | 〃 |  |
| 18860 | sch 1B para 5(3) lead, (a), (b), (c) -- "(b) does not know the person to be a..." | encoded | 〃 | 〃 |  |
| 18861 | sch 1B para 5(3) lead, (a), (b), (c) -- "(c) fails to notify the person of th..." | encoded | 〃 | 〃 |  |
| 18862 | sch 1B para 5(4) lead, (a), (b) -- "(4) A person commits an offence if t..." | encoded | `sch 1B para 5(4) the person commits an offence` | 4 |  |
| 18863 | sch 1B para 5(4) lead, (a), (b) -- "(a) either has a relevant interest t..." | encoded | 〃 | 〃 |  |
| 18864 | sch 1B para 5(4) lead, (a), (b) -- "(b) enters in that capacity into an ..." | encoded | 〃 | 〃 |  |
| 18865 | sch 1B para 5(5) | encoded | `sch 1B para 5(5) the interest is subject to restrictions` | 2 |  |
| 18866 | sch 1B para 6 lead and (a) -- "6 If shares in a company are issued ..." | encoded | `sch 1B para 6(a) the company commits an offence`; `sch 1B para 6(b) the officer of the company commits an offence` | 8 |  |
| 18867 | sch 1B para 6 lead and (a) -- "(a) the company, and" | encoded | 〃 | 〃 |  |
| 18868 | sch 1B para 6(b) | encoded | `sch 1B para 6(b) the officer of the company commits an offence` | 5 |  |
| 18869 | sch 1B para 7(1) lead, (a), (b), (i), (ii) -- "7 (1) A person guilty of an offence ..." | encoded | `sch 1B para 7(1) the penalty for an offence under paragraph 5 or 6` | 5 |  |
| 18870 | sch 1B para 7(1) lead, (a), (b), (i), (ii) -- "(a) on conviction on indictment, to ..." | encoded | 〃 | 〃 |  |
| 18871 | sch 1B para 7(1) lead, (a), (b), (i), (ii) -- "(b) on summary conviction—" | encoded | 〃 | 〃 |  |
| 18872 | sch 1B para 7(1) lead, (a), (b), (i), (ii) -- "(i) in England and Wales, to a fine," | encoded | 〃 | 〃 |  |
| 18873 | sch 1B para 7(1) lead, (a), (b), (i), (ii) -- "(ii) in Scotland or Northern Ireland..." | encoded | 〃 | 〃 |  |
| 18874 | sch 1B para 7(2) | fork (F7) | `sch 1B para 7(2) the provisions of paragraphs 5 and 6 are subject to the direction`; `sch 1B para 5(2) thing` | 8 | fork F7 ('subject to any direction') |
| 18875 | Schedule 1B group heading: Relaxation of restrictions | inert 1 |  |  | cross-heading |
| 18876 | sch 1B para 8(1) and (2) -- "8 (1) An application may be made to ..." | encoded | `sch 1B para 8(2) the person may apply for an order under paragraph 8` | 3 | 8(1) says an application may be made; 8(2) says by whom; one function |
| 18877 | sch 1B para 8(1) and (2) -- "(2) An application for an order unde..." | encoded | 〃 | 〃 | 〃 |
| 18878 | sch 1B para 8(3) lead, (a), (b) -- "(3) The court must not make an order..." | encoded | `sch 1B para 8(3) the court is barred from making an order under paragraph 8` | 5 |  |
| 18879 | sch 1B para 8(3) lead, (a), (b) -- "(a) it is satisfied that the informa..." | encoded | 〃 | 〃 |  |
| 18880 | sch 1B para 8(3) lead, (a), (b) -- "(b) the relevant interest is to be t..." | encoded | 〃 | 〃 |  |
| 18881 | sch 1B para 8(4) | encoded | `sch 1B para 8(4) the order may continue the restriction` | 4 |  |
| 18882 | sch 1B para 8(5) lead and (a) -- "(5) Where any restrictions continue ..." | encoded | `sch 1B para 8(5)(a) an application may be made for an order directing that the relevant interest cease to be subject to those restrictions`; `sch 1B para 8(5)(b) sub-paragraph (3) applies to the making of the order` | 4 |  |
| 18883 | sch 1B para 8(5) lead and (a) -- "(a) an application may be made under..." | encoded | 〃 | 〃 |  |
| 18884 | sch 1B para 8(5)(b) | encoded | `sch 1B para 8(5)(b) sub-paragraph (3) applies to the making of the order` | 2 |  |
| 18885 | Schedule 1B group heading: Orders for sale | inert 1 |  |  | cross-heading |
| 18886 | sch 1B para 9(1) | encoded | `sch 1B para 9(1) the court may order that the relevant interest be sold subject to the court's approval as to the sale` | 2 |  |
| 18887 | sch 1B para 9(2) | encoded | `sch 1B para 9(2) the person may apply for an order under sub-paragraph (1)` | 2 |  |
| 18888 | sch 1B para 9(3) | encoded | `sch 1B para 9(3) the court may make such further order relating to the sale or transfer of the interest as it thinks fit` | 2 |  |
| 18889 | sch 1B para 9(4) lead, (a), (b), (c) -- "(4) An application for an order unde..." | encoded | `sch 1B para 9(4) the person may apply for an order under sub-paragraph (3)` | 4 |  |
| 18890 | sch 1B para 9(4) lead, (a), (b), (c) -- "(a) by the company in question," | encoded | 〃 | 〃 |  |
| 18891 | sch 1B para 9(4) lead, (a), (b), (c) -- "(b) by the person appointed by or in..." | encoded | 〃 | 〃 |  |
| 18892 | sch 1B para 9(4) lead, (a), (b), (c) -- "(c) by any person with an interest i..." | encoded | 〃 | 〃 |  |
| 18893 | sch 1B para 9(5) | encoded | `sch 1B para 9(5) the court may order that the applicant's costs be paid out of the proceeds of sale` | 2 |  |
| 18894 | sch 1B para 10(1) | encoded | `sch 1B para 10(1) the amount that must be paid into court` | 1 |  |
| 18895 | sch 1B para 10(2) | encoded | `sch 1B para 10(2) the person may apply to the court for the whole or part of the proceeds to be paid to the person` | 2 |  |
| 18896 | sch 1B para 10(3) lead, (a), (b) -- "(3) On such an application, the cour..." | encoded | `sch 1B para 10(3) the amount the court must order to be paid to the applicant` | 2 |  |
| 18897 | sch 1B para 10(3) lead, (a), (b) -- "(a) the whole of the proceeds of sal..." | encoded | 〃 | 〃 |  |
| 18898 | sch 1B para 10(3) lead, (a), (b) -- "(b) if another person was also benef..." | encoded | 〃 | 〃 |  |
| 18899 | sch 1B para 10(4) | encoded | `sch 1B para 10(4) the applicant is entitled to payment of those costs out of the proceeds before any person receives any part of the proceeds under paragraph 10` | 2 |  |
| 18900 | Schedule 1B group heading: Company's power to withdraw restrictions notice | inert 1 |  |  | cross-heading |
| 18901 | sch 1B para 11 lead, (a), (b), (c) -- "11 A company that issues a person wi..." | encoded | `sch 1B para 11 the company must by notice withdraw the restrictions notice`; `sch 1B para 11 action`; `sch 1B para 11 the company's duty to withdraw the restrictions notice` | 6 |  |
| 18902 | sch 1B para 11 lead, (a), (b), (c) -- "(a) it is satisfied that there is a ..." | encoded | 〃 | 〃 |  |
| 18903 | sch 1B para 11 lead, (a), (b), (c) -- "(b) the notice served under section ..." | encoded | 〃 | 〃 |  |
| 18904 | sch 1B para 11 lead, (a), (b), (c) -- "(c) it discovers that the rights of ..." | encoded | 〃 | 〃 |  |
| 18905 | Schedule 1B group heading: Supplementary provision | inert 1 |  |  | cross-heading |
| 18906 | sch 1B para 12(1) | inert 2 |  |  | regulation-making power (procedure for notices) |
| 18907 | sch 1B para 12(2) lead | inert 2 |  |  | regulation-making power |
| 18908 | sch 1B para 12(2)(a) | inert 2 |  |  | regulation-making power |
| 18909 | sch 1B para 12(2)(b) | inert 2 |  |  | regulation-making power |
| 18910 | sch 1B para 12(2)(c) | inert 2 |  |  | regulation-making power |
| 18911 | sch 1B para 12(3) | encoded | `sch 1B para 12(3) the procedure for regulations under paragraph 12` | 1 |  |
| 18912 | Schedule 1B group heading: Offence of failing to comply with notices | inert 1 |  |  | cross-heading |
| 18913 | sch 1B para 13(1) | encoded | `sch 1B para 13(1) the person commits an offence by failing to comply with the notice` | 4 |  |
| 18914 | sch 1B para 13(2) | encoded | `sch 1B para 13(2) the officer of the entity commits an offence` | 6 |  |
| 18915 | sch 1B para 13(3) lead, (a), (b), (i), (ii), (iii) -- "(3) A person guilty of an offence un..." | encoded | `sch 1B para 13(3) the penalty for an offence under paragraph 13` | 6 |  |
| 18916 | sch 1B para 13(3) lead, (a), (b), (i), (ii), (iii) -- "(a) on conviction on indictment, to ..." | encoded | 〃 | 〃 |  |
| 18917 | sch 1B para 13(3) lead, (a), (b), (i), (ii), (iii) -- "(b) on summary conviction—" | encoded | 〃 | 〃 |  |
| 18918 | sch 1B para 13(3) lead, (a), (b), (i), (ii), (iii) -- "(i) in England and Wales, to impriso..." | encoded | 〃 | 〃 |  |
| 18919 | sch 1B para 13(3) lead, (a), (b), (i), (ii), (iii) -- "(ii) in Scotland, to imprisonment fo..." | encoded | 〃 | 〃 |  |
| 18920 | sch 1B para 13(3) lead, (a), (b), (i), (ii), (iii) -- "(iii) in Northern Ireland, to impris..." | encoded | 〃 | 〃 |  |
| 18921 | Schedule 1B group heading: Offence of failing to provide information | inert 1 |  |  | cross-heading |
| 18922 | sch 1B para 14(1) | encoded | `sch 1B para 14(1) the person commits an offence by failing to comply with the duty` | 3 |  |
| 18923 | sch 1B para 14(2) | encoded | `sch 1B para 14(2) the officer of the entity commits an offence` | 3 |  |
| 18924 | sch 1B para 14(3) lead, (a), (b), (i), (ii), (iii) -- "(3) A person guilty of an offence un..." | encoded | `sch 1B para 14(3) the penalty for an offence under paragraph 14` | 5 |  |
| 18925 | sch 1B para 14(3) lead, (a), (b), (i), (ii), (iii) -- "(a) on conviction on indictment, to ..." | encoded | 〃 | 〃 |  |
| 18926 | sch 1B para 14(3) lead, (a), (b), (i), (ii), (iii) -- "(b) on summary conviction—" | encoded | 〃 | 〃 |  |
| 18927 | sch 1B para 14(3) lead, (a), (b), (i), (ii), (iii) -- "(i) in England and Wales, to impriso..." | encoded | 〃 | 〃 |  |
| 18928 | sch 1B para 14(3) lead, (a), (b), (i), (ii), (iii) -- "(ii) in Scotland, to imprisonment fo..." | encoded | 〃 | 〃 |  |
| 18929 | sch 1B para 14(3) lead, (a), (b), (i), (ii), (iii) -- "(iii) in Northern Ireland, to impris..." | encoded | 〃 | 〃 |  |
| 18930 | Schedule 1B group heading: False statements: basic offence | inert 1 |  |  | cross-heading |
| 18931 | sch 1B para 14A(1) | encoded | `sch 1B para 14A(1) the person commits the basic offence of making a false statement` | 3 |  |
| 18932 | sch 1B para 14A(2) | encoded | `sch 1B para 14A(2) the officer of the entity commits an offence` | 3 |  |
| 18933 | sch 1B para 14A(3) lead, (a), (b), (c) -- "(3) A person guilty of an offence un..." | encoded | `sch 1B para 14A(3) the penalty for an offence under paragraph 14A` | 5 |  |
| 18934 | sch 1B para 14A(3) lead, (a), (b), (c) -- "(a) in England and Wales, to a fine;" | encoded | 〃 | 〃 |  |
| 18935 | sch 1B para 14A(3) lead, (a), (b), (c) -- "(b) in Scotland, to a fine not excee..." | encoded | 〃 | 〃 |  |
| 18936 | sch 1B para 14A(3) lead, (a), (b), (c) -- "(c) in Northern Ireland, to a fine n..." | encoded | 〃 | 〃 |  |
| 18937 | Schedule 1B group heading: False statements: aggravated offence | inert 1 |  |  | cross-heading |
| 18938 | sch 1B para 14B(1) | encoded | `sch 1B para 14B(1) the person commits the aggravated offence of making a false statement` | 2 |  |
| 18939 | sch 1B para 14B(2) | encoded | `sch 1B para 14B(2) the officer of the entity commits an offence` | 3 |  |
| 18940 | sch 1B para 14B(3) lead, (a), (b), (i), (ii), (iii) -- "(3) A person guilty of an offence un..." | encoded | `sch 1B para 14B(3) the penalty for an offence under paragraph 14B` | 5 |  |
| 18941 | sch 1B para 14B(3) lead, (a), (b), (i), (ii), (iii) -- "(a) on conviction on indictment, to ..." | encoded | 〃 | 〃 |  |
| 18942 | sch 1B para 14B(3) lead, (a), (b), (i), (ii), (iii) -- "(b) on summary conviction—" | encoded | 〃 | 〃 |  |
| 18943 | sch 1B para 14B(3) lead, (a), (b), (i), (ii), (iii) -- "(i) in England and Wales, to impriso..." | encoded | 〃 | 〃 |  |
| 18944 | sch 1B para 14B(3) lead, (a), (b), (i), (ii), (iii) -- "(ii) in Scotland, to imprisonment fo..." | encoded | 〃 | 〃 |  |
| 18945 | sch 1B para 14B(3) lead, (a), (b), (i), (ii), (iii) -- "(iii) in Northern Ireland, to impris..." | encoded | 〃 | 〃 |  |
| 18946 | Schedule 1C title | inert 1 |  |  | Schedule title |
| 18947 | Schedule 1C reference line (Section 943) | inert 1 |  |  | reference line |
| 18948 | Schedule 1C Part 1 title | inert 1 |  |  | Part title |
| 18949 | sch 1C para 1(1) | encoded | `sch 1C para 1(1) the rules must afford the holders equivalent treatment` | 4 |  |
| 18950 | sch 1C para 1(2) | encoded | `sch 1C para 1(2) the rules must protect the other holders of securities` | 2 |  |
| 18951 | sch 1C para 2(1) | encoded | `sch 1C para 2(1) the holders must have sufficient time and information to reach a properly informed decision on the takeover bid`; `sch 1C para 2(2) effect` | 7 |  |
| 18952 | sch 1C para 2(2) lead, (a), (b), (c) -- "(2) Where it advises the holders of ..." | encoded | `sch 1C para 2(2) the board of the offeree company must give its views on the effect of implementation of the takeover bid` | 5 |  |
| 18953 | sch 1C para 2(2) lead, (a), (b), (c) -- "(a) employment," | encoded | 〃 | 〃 |  |
| 18954 | sch 1C para 2(2) lead, (a), (b), (c) -- "(b) conditions of employment, and" | encoded | 〃 | 〃 |  |
| 18955 | sch 1C para 2(2) lead, (a), (b), (c) -- "(c) the locations of the company’s p..." | encoded | 〃 | 〃 |  |
| 18956 | sch 1C para 3 | encoded | `sch 1C para 3 the board of the offeree company complies with the principle`; `sch 1C para 4 company concerned` | 10 |  |
| 18957 | sch 1C para 4 lead, (a), (b), (c), closing words -- "4 False markets must not be created ..." | encoded | `sch 1C para 4 the creation of a false market in the securities of the company is barred` | 6 |  |
| 18958 | sch 1C para 4 lead, (a), (b), (c), closing words -- "(a) the offeree company," | encoded | 〃 | 〃 |  |
| 18959 | sch 1C para 4 lead, (a), (b), (c), closing words -- "(b) if the offeror is a company, tha..." | encoded | 〃 | 〃 |  |
| 18960 | sch 1C para 4 lead, (a), (b), (c), closing words -- "(c) any other company concerned by t..." | encoded | 〃 | 〃 |  |
| 18961 | sch 1C para 4 lead, (a), (b), (c), closing words -- "in such a way that the rise or fall ..." | encoded | 〃 | 〃 |  |
| 18962 | sch 1C para 5 lead, (a), (b) -- "5 An offeror must announce a takeove..." | encoded | `sch 1C para 5 the offeror is barred from announcing the takeover bid yet` | 7 |  |
| 18963 | sch 1C para 5 lead, (a), (b) -- "(a) ensuring that the offeror can fu..." | encoded | 〃 | 〃 |  |
| 18964 | sch 1C para 5 lead, (a), (b) -- "(b) taking all reasonable measures t..." | encoded | 〃 | 〃 |  |
| 18965 | sch 1C para 6 | encoded | `sch 1C para 6 the hindrance of the offeree company is barred` | 3 |  |
| 18966 | Schedule 1C Part 2 title | inert 1 |  |  | Part title (the rendering writes it PART2) |
| 18967 | Schedule 1C group heading: Protection of minority shareholders, the mandatory takeover bid and the equitable price | inert 1 |  |  | cross-heading |
| 18968 | sch 1C para 7(1) lead, (a), (b) -- "7 (1) Rules must ensure that a perso..." | encoded | `sch 1C para 7(1) the rules must require P to make a mandatory takeover bid` | 5 |  |
| 18969 | sch 1C para 7(1) lead, (a), (b) -- "(a) P, or any person acting in conce..." | encoded | 〃 | 〃 |  |
| 18970 | sch 1C para 7(1) lead, (a), (b) -- "(b) the acquired securities, when ad..." | encoded | 〃 | 〃 |  |
| 18971 | sch 1C para 7(2) | encoded | `sch 1C para 7(2) the mandatory takeover bid meets the requirement the rules must ensure`; `sch 1C para 8(1) purchase`; `sch 1C para 8 the highest of the prices` | 6 |  |
| 18972 | sch 1C para 7(3) | encoded | `sch 1C para 7(3) the obligation to make a mandatory takeover bid no longer applies` | 2 |  |
| 18973 | sch 1C para 8(1) | fork (F10) | `sch 1C para 8(1) the equitable price` | 6 | fork F10 (month arithmetic and 'before the bid is announced') |
| 18974 | sch 1C para 8(2) | encoded | `sch 1C para 8(2) the offer consideration must not be less than` | 3 |  |
| 18975 | sch 1C para 8(3) | inert 2 |  |  | rule-making power (the Panel may adjust the equitable price) |
| 18976 | sch 1C para 8(4) | encoded | `sch 1C para 8(4) the Panel's decision to adjust the equitable price meets the requirement`; `sch 1C para 9(1) consideration` | 7 |  |
| 18977 | sch 1C para 9(1) lead, (a), (b), (c) -- "9 (1) Rules must ensure that the off..." | encoded | `sch 1C para 9(1) the rules must ensure that the offeror may offer the consideration for the securities` | 4 |  |
| 18978 | sch 1C para 9(1) lead, (a), (b), (c) -- "(a) securities," | encoded | 〃 | 〃 |  |
| 18979 | sch 1C para 9(1) lead, (a), (b), (c) -- "(b) cash, or" | encoded | 〃 | 〃 |  |
| 18980 | sch 1C para 9(1) lead, (a), (b), (c) -- "(c) a combination of both." | encoded | 〃 | 〃 |  |
| 18981 | sch 1C para 9(2) lead, (a), (b) -- "(2) Rules must ensure that cash must..." | encoded | `sch 1C para 9(2) the rules must ensure that cash is offered as an alternative` | 4 |  |
| 18982 | sch 1C para 9(2) lead, (a), (b) -- "(a) as an alternative where the cons..." | encoded | 〃 | 〃 |  |
| 18983 | sch 1C para 9(2) lead, (a), (b) -- "(b) at least as an alternative where..." | encoded | 〃 | 〃 |  |
| 18984 | sch 1C para 9(3) lead, (a), (b) -- "(3) “A relevant period” is a period—" | encoded | `sch 1C para 9(3) the day is within the relevant period` | 4 |  |
| 18985 | sch 1C para 9(3) lead, (a), (b) -- "(a) beginning at the same time as th..." | encoded | 〃 | 〃 |  |
| 18986 | sch 1C para 9(3) lead, (a), (b) -- "(b) ending when the offer closes for..." | encoded | 〃 | 〃 |  |
| 18987 | sch 1C para 9(4) | inert 2 |  |  | rule-making power (rules may require cash in all cases) |
| 18988 | sch 1C para 10 | encoded | `sch 1C para 10 the rule is barred` | 3 |  |
| 18989 | Schedule 1C group heading: Information concerning takeover bids | inert 1 |  |  | cross-heading |
| 18990 | sch 1C para 11(1) | encoded | `sch 1C para 11(1) the decision to make a takeover bid has been made public and the Panel informed as the rules must ensure` | 3 |  |
| 18991 | sch 1C para 11(2) | inert 2 |  |  | rule-making power (rules may require the Panel to be informed first) |
| 18992 | sch 1C para 11(3) lead, (a), (b) -- "(3) Rules must ensure that, as soon ..." | encoded | `sch 1C para 11(3) the boards of the offeree company and of the offeror must inform` | 3 |  |
| 18993 | sch 1C para 11(3) lead, (a), (b) -- "(a) the representatives of their res..." | encoded | 〃 | 〃 |  |
| 18994 | sch 1C para 11(3) lead, (a), (b) -- "(b) where there are no such represen..." | encoded | 〃 | 〃 |  |
| 18995 | sch 1C para 12(1) | encoded | `sch 1C para 12(1) the offeror has met the requirement to draw up and make public an offer document` | 2 |  |
| 18996 | sch 1C para 12(2) | encoded | `sch 1C para 12(2) the offeror has met the requirement to provide a copy to the Panel before the offer document is made public` | 2 |  |
| 18997 | sch 1C para 12(3) lead, (a), (b) -- "(3) Rules must ensure that, when the..." | encoded | `sch 1C para 12(3) the boards of the offeree company and of the offeror must communicate the offer document to`; `sch 1C para 12(4) item` | 7 |  |
| 18998 | sch 1C para 12(3) lead, (a), (b) -- "(a) to the representatives of their ..." | encoded | 〃 | 〃 |  |
| 18999 | sch 1C para 12(3) lead, (a), (b) -- "(b) where there are no such represen..." | encoded | 〃 | 〃 |  |
| 19000 | sch 1C para 12(4) lead | encoded | `sch 1C para 12(4) the offer document states at least the information the rules must require` | 5 |  |
| 19001 | sch 1C para 12(4)(a) | encoded | 〃 | 〃 |  |
| 19002 | sch 1C para 12(4)(b) | encoded | 〃 | 〃 |  |
| 19003 | sch 1C para 12(4)(c) | encoded | 〃 | 〃 |  |
| 19004 | sch 1C para 12(4)(d) | encoded | 〃 | 〃 |  |
| 19005 | sch 1C para 12(4)(e) | encoded | 〃 | 〃 |  |
| 19006 | sch 1C para 12(4)(f) | encoded | 〃 | 〃 |  |
| 19007 | sch 1C para 12(4)(g) | encoded | 〃 | 〃 |  |
| 19008 | sch 1C para 12(4)(h) | encoded | 〃 | 〃 |  |
| 19009 | sch 1C para 12(4)(i) | encoded | 〃 | 〃 |  |
| 19010 | sch 1C para 12(4)(j) | encoded | 〃 | 〃 |  |
| 19011 | sch 1C para 12(4)(k) | encoded | 〃 | 〃 |  |
| 19012 | sch 1C para 12(4)(l) lead, (i), (ii), (iii) -- "(l) if the offeror is a company and ..." | encoded | 〃 | 〃 |  |
| 19013 | sch 1C para 12(4)(l) lead, (i), (ii), (iii) -- "(i) the offeror’s intentions with re..." | encoded | 〃 | 〃 |  |
| 19014 | sch 1C para 12(4)(l) lead, (i), (ii), (iii) -- "(ii) the offeror’s intentions with r..." | encoded | 〃 | 〃 |  |
| 19015 | sch 1C para 12(4)(l) lead, (i), (ii), (iii) -- "(iii) the offeror’s strategic plans ..." | encoded | 〃 | 〃 |  |
| 19016 | sch 1C para 12(4)(m) | encoded | 〃 | 〃 |  |
| 19017 | sch 1C para 12(4)(n) | encoded | 〃 | 〃 |  |
| 19018 | sch 1C para 12(4)(o) | encoded | 〃 | 〃 |  |
| 19019 | sch 1C para 12(4)(p) | encoded | 〃 | 〃 |  |
| 19020 | sch 1C para 12(4)(q) | encoded | 〃 | 〃 |  |
| 19021 | Schedule 1C group heading: Time allowed for acceptance | inert 1 |  |  | cross-heading |
| 19022 | sch 1C para 13(1) | fork (F8) | `sch 1C para 13(1) the time allowed for acceptance is within the limits the rules must ensure`; `sch 1C para 15 company` | 10 | fork F8 (counting 'two weeks' and '10 weeks beginning with the day after') |
| 19023 | sch 1C para 13(2) | inert 2 |  |  | rule-making power (rules may extend the maximum period) |
| 19024 | sch 1C para 14(1) | inert 2 |  |  | rule-making power (rules may change the time allowed) |
| 19025 | sch 1C para 14(2) | inert 2 |  |  | rule-making power (the Panel may grant a derogation) |
| 19026 | Schedule 1C group heading: Disclosure | inert 1 |  |  | cross-heading |
| 19027 | sch 1C para 15 lead, (a), (b), (c), closing words -- "15 Rules must ensure that a takeover..." | encoded | `sch 1C para 15 the rules must ensure that the takeover bid is made public so as to ensure market transparency and integrity for the securities of the company`; `sch 1C para 16 recipient` | 9 |  |
| 19028 | sch 1C para 15 lead, (a), (b), (c), closing words -- "(a) the offeree company," | encoded | 〃 | 〃 |  |
| 19029 | sch 1C para 15 lead, (a), (b), (c), closing words -- "(b) if the offeror is a company, tha..." | encoded | 〃 | 〃 |  |
| 19030 | sch 1C para 15 lead, (a), (b), (c), closing words -- "(c) any other company affected by th..." | encoded | 〃 | 〃 |  |
| 19031 | sch 1C para 15 lead, (a), (b), (c), closing words -- "in particular in order to prevent th..." | encoded | 〃 | 〃 |  |
| 19032 | sch 1C para 16 lead, (a), (b) -- "16 Rules must ensure that all inform..." | encoded | `sch 1C para 16 the rules must ensure that the information and documents are readily and promptly available to the recipient` | 4 |  |
| 19033 | sch 1C para 16 lead, (a), (b) -- "(a) to the holders of securities adm..." | encoded | 〃 | 〃 |  |
| 19034 | sch 1C para 16 lead, (a), (b) -- "(b) to the representatives of the em..." | encoded | 〃 | 〃 |  |
| 19035 | Schedule 1C group heading: Obligations of the board of directors of the offeree company | inert 1 |  |  | cross-heading |
| 19036 | sch 1C para 17(1) lead, (a), (b) -- "17 (1) Rules must ensure that, durin..." | fork (F9) | `sch 1C para 17(1) the rules must require the board to obtain the prior authorisation of a general meeting` | 6 | fork F9 ('during the relevant period' and 'other than seeking alternative takeover bids') |
| 19037 | sch 1C para 17(1) lead, (a), (b) -- "(a) before taking any action, other ..." | fork (F9) | 〃 | 〃 | 〃 |
| 19038 | sch 1C para 17(1) lead, (a), (b) -- "(b) in particular, before issuing an..." | fork (F9) | 〃 | 〃 | 〃 |
| 19039 | sch 1C para 17(2) lead, (a), (b) -- "(2) “The relevant period”—" | encoded | `sch 1C para 17(2) the day is within the relevant period` | 8 |  |
| 19040 | sch 1C para 17(2) lead, (a), (b) -- "(a) begins when the board of directo..." | encoded | 〃 | 〃 |  |
| 19041 | sch 1C para 17(2) lead, (a), (b) -- "(b) ends when the result of the bid ..." | encoded | 〃 | 〃 |  |
| 19042 | sch 1C para 17(3) lead, (a), (b) -- "(3) Rules must ensure that, with reg..." | encoded | `sch 1C para 17(3) the rules must require a general meeting to approve or confirm the decision`; `sch 1C para 17(4) body` | 9 |  |
| 19043 | sch 1C para 17(3) lead, (a), (b) -- "(a) which does not form part of the ..." | encoded | 〃 | 〃 |  |
| 19044 | sch 1C para 17(3) lead, (a), (b) -- "(b) the implementation of which may ..." | encoded | 〃 | 〃 |  |
| 19045 | sch 1C para 17(4) | encoded | `sch 1C para 17(4) the body is the board of directors for paragraph 17` | 4 |  |
| 19046 | sch 1C para 18(1) lead, (a), (b) -- "18 (1) Rules must ensure that the bo..." | encoded | `sch 1C para 18(1) the board has met the requirement to draw up and make public its opinion` | 4 |  |
| 19047 | sch 1C para 18(1) lead, (a), (b) -- "(a) the effects of implementation of..." | encoded | 〃 | 〃 |  |
| 19048 | sch 1C para 18(1) lead, (a), (b) -- "(b) the offeror’s strategic plans fo..." | encoded | 〃 | 〃 |  |
| 19049 | sch 1C para 18(2) lead, (a), (b) -- "(2) Rules must ensure that the board..." | encoded | `sch 1C para 18(2) the board must at the same time communicate its opinion to` | 3 |  |
| 19050 | sch 1C para 18(2) lead, (a), (b) -- "(a) to the representatives of its em..." | encoded | 〃 | 〃 |  |
| 19051 | sch 1C para 18(2) lead, (a), (b) -- "(b) where there are no such represen..." | encoded | 〃 | 〃 |  |
| 19052 | sch 1C para 18(3) | encoded | `sch 1C para 18(3) the employees' representatives' opinion must be appended to the document`; `sch 1C para 19 topic` | 8 |  |
| 19053 | Schedule 1C group heading: Other rules applicable to the conduct of takeover bids | inert 1 |  |  | cross-heading |
| 19054 | sch 1C para 19 lead, (a) to (e) -- "19 Rules must make provision governi..." | encoded | `sch 1C para 19 the rules must make provision on the topic` | 6 |  |
| 19055 | sch 1C para 19 lead, (a) to (e) -- "(a) the lapsing of takeover bids," | encoded | 〃 | 〃 |  |
| 19056 | sch 1C para 19 lead, (a) to (e) -- "(b) the revision of takeover bids," | encoded | 〃 | 〃 |  |
| 19057 | sch 1C para 19 lead, (a) to (e) -- "(c) competing takeover bids," | encoded | 〃 | 〃 |  |
| 19058 | sch 1C para 19 lead, (a) to (e) -- "(d) the disclosure of the results of..." | encoded | 〃 | 〃 |  |
| 19059 | sch 1C para 19 lead, (a) to (e) -- "(e) the irrevocability of takeover b..." | encoded | 〃 | 〃 |  |
| 19060 | Schedule 1C group heading: Interpretation | inert 1 |  |  | cross-heading |
| 19061 | sch 1C para 20(1) lead and definition of offer document -- "20 (1) In this Schedule—" | encoded | `sch 1C para 20(1) the document is an offer document`; `sch 1C para 20(1) the company is an offeree company`; `sch 1C para 20(1) the person is the offeror in relation to the takeover bid`; `sch 1C para 20(1) the rules are rules for this Schedule`; `sch 1C para 20(1) the instruments are securities`; `sch 1C para 20(1) the offer is a takeover bid`; `sch 1C para 20(1) the rights are voting rights for this Schedule` | 19 | the lead-in is quoted with each of the seven definitions |
| 19062 | sch 1C para 20(1) lead and definition of offer document -- "“offer document” means a document re..." | encoded | 〃 | 〃 | 〃 |
| 19063 | sch 1C para 20(1) definition of offeree company | encoded | `sch 1C para 20(1) the company is an offeree company` | 2 |  |
| 19064 | sch 1C para 20(1) definition of offeror | encoded | `sch 1C para 20(1) the person is the offeror in relation to the takeover bid` | 2 |  |
| 19065 | sch 1C para 20(1) definition of rules | encoded | `sch 1C para 20(1) the rules are rules for this Schedule` | 2 |  |
| 19066 | sch 1C para 20(1) definition of securities | encoded | `sch 1C para 20(1) the instruments are securities` | 4 |  |
| 19067 | sch 1C para 20(1) definition of takeover bid | encoded | `sch 1C para 20(1) the offer is a takeover bid` | 5 |  |
| 19068 | sch 1C para 20(1) definition of voting rights | encoded | `sch 1C para 20(1) the rights are voting rights for this Schedule` | 2 |  |
| 19069 | sch 1C para 20(2) | encoded | `sch 1C para 20(2) the securities are of one class` | 2 |  |
| 19070 | sch 1C para 20(3) lead, (a), (b) -- "(3) In this Schedule, “persons actin..." | encoded | `sch 1C para 20(3) the person is a person acting in concert`; `sch 1C para 20(4) pair` | 11 |  |
| 19071 | sch 1C para 20(3) lead, (a), (b) -- "(a) acquiring control of the offeree..." | encoded | 〃 | 〃 |  |
| 19072 | sch 1C para 20(3) lead, (a), (b) -- "(b) frustrating the successful outco..." | encoded | 〃 | 〃 |  |
| 19073 | sch 1C para 20(4) lead, (a), (b) -- "(4) For the purposes of this Schedul..." | encoded | `sch 1C para 20(4) the two are deemed to be acting in concert`; `sch 1C para 21(2) provision` | 11 |  |
| 19074 | sch 1C para 20(4) lead, (a), (b) -- "(a) A is deemed to be acting in conc..." | encoded | 〃 | 〃 |  |
| 19075 | sch 1C para 20(4) lead, (a), (b) -- "(b) B and those subsidiary undertaki..." | encoded | 〃 | 〃 |  |
| 19076 | sch 1C para 21(1) | encoded | `sch 1C para 21(1) the body is a company for this Schedule` | 4 |  |
| 19077 | sch 1C para 21(2) lead and the three listed provisions -- "(2) The listed provisions are—" | encoded | `sch 1C para 21(2) the provision is one of the listed provisions` | 4 |  |
| 19078 | sch 1C para 21(2) lead and the three listed provisions -- "paragraph 4(b) and (c);" | encoded | 〃 | 〃 |  |
| 19079 | sch 1C para 21(2) lead and the three listed provisions -- "paragraph 12(4)(b), (l) and (p);" | encoded | 〃 | 〃 |  |
| 19080 | sch 1C para 21(2) lead and the three listed provisions -- "paragraph 15(b) and (c)." | encoded | 〃 | 〃 |  |
| 19081 | sch 1C para 21(3) | encoded | `sch 1C para 21(3) section 1 applies for the purposes of the provision` | 3 |  |

## Fork register (coa28)

A fork is a place where the text reads two or more ways with different outcomes.
Part A copies, word for word, the five rulings that govern the branches of this encoding (E1, N2, periods and "where", delegated definitions and "until" bars, and the case-by-case decision).
Part B lists the forks numbered F1 to F12, with the readings seen, the reading taken, and the text that licenses it.
Part C gives one line per site for the six questions the case-by-case decision leaves to the encoder: an "unless" or "except" once met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; and a missing event in the state ledger (no site in this range; there is no ledger).
Each line names the provision, the function, the answer taken and the other reading, for the human reviewer to overrule.

### Part A: the rulings, verbatim from `BRIEF.md`

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

How these bear on this encoding: E1 option B applies to the gathering functions `sch 1 paras 2 to 6 the person has an interest in the shares or debentures for sections 254 and 255` and `sch 1A paras 2 to 4 and 25 the individual meets the specified condition`, both written by hand over routes the module itself defines; option C (per-section answers) applies to everything else.
N2 is followed: a flat negative answers `JUST FALSE`, and the one prohibition whose bearer the text names (s 241A(5)) is also written as a `SHANT` rule.
The periods ruling (a) and (b) is followed for the 28-day and 40-day periods, sch 1B para 1(3), and sch 1C paras 13(1), 17(1); scope limits with no "only" answer `NOTHING` (ruling (c)).
The delegated-definitions ruling applies to sch 1C para 21(2) (a definition handed to a list of provisions) and to the bars (d): s 1290, sch 1B para 8(3) and sch 1C para 5 are bar functions (`JUST TRUE` while the bar holds, `JUST FALSE` once the "unless" or "only after" is met).

### Part B: the numbered forks

| id | provision (lines) | function | readings seen | reading taken | text that licenses it |
|---|---|---|---|---|---|
| F1 | s 1291(2) (18543) | `s 1291(2) the day falls in a time that is not taken into account` | (i) "more than four days" counted inclusively, the first and last day both counting, and a time that is longer has every one of its days left out; (ii) counted exclusively (a difference of more than four days); (iii) only the days beyond the fourth are left out | (i): an adjournment of 10 to 13 January (four days) is not left out, one of 10 to 14 January (five days) is left out whole; a dissolution or prorogation is left out whatever its length; the per-time function `s 1291(2) no account is taken of the time in the interval` answers `NOTHING` for an adjournment of four days or fewer, and the day-counting helper treats that as a time that counts (a helper that returns a plain `BOOLEAN`, so this is the one place a `NOTHING` is read as "the days count") | "no account shall be taken of any time during which Parliament is dissolved or prorogued or during which both Houses are adjourned for more than four days": "any time during which" points at the whole time |
| F2 | s 1291(1)(b) (18542) | `s 1291(1)(b) the last day of the 28 days beginning with the day on which they were made` | (i) the day of making is day 1 and the last day is the 28th; (ii) the day after the making is day 1 | (i): the last day is the day of making plus 27 days (plus the days left out) | "28 days beginning with the day on which they were made" |
| F3 | see Part C (b) | the compliance functions of the bare "must" sites | (i) a bare "must" not yet done answers `JUST FALSE` of the compliance function; (ii) it answers `NOTHING`, because the text says what must be done and not what follows from not doing it | (i): the function is named for what the text requires ("has met the requirement ..."), so `JUST FALSE` says only that the requirement is not met | the case-by-case ruling (a bare "must" not done) |
| F4 | sch 1A para 2 (18671) | `sch 1A para 2 the first condition is met` | "holds, directly or indirectly": (i) shares X holds in X's own name are held directly, the Schedule's para 18 giving "indirectly"; (ii) the Schedule leaves "directly" undefined, so the count is `NOTHING` | (i), by the ordinary meaning of the word: a block marked as held directly by X counts | para 18 defines only "indirectly" (18730-18747); the word "directly" appears in paras 2, 3, 4 and 8(1) without a definition |
| F5 | sch 1A para 23 (18771-18773) | `sch 1A para 23 the rights are treated as held by the person who provided the security` | (i) limbs (a) and (b) are cumulative; (ii) either suffices | (i): both must hold | limb (a) ends "..., and", and (b) follows |
| F6 | sch 1B para 1(3) (18817) | `sch 1B para 1(3) the last day of the period of one month beginning with the date on which the warning notice was given` | (i) a month beginning on the 10th ends on the 9th of the next month (the last day of the next month if that month is shorter), and the company may issue from the following day; (ii) a month beginning on the 10th ends on the 10th of the next month | (i): given on 10 January, the company may issue the restrictions notice on 10 February, not on 9 February | "by the end of the period of one month beginning with the date on which the warning notice was given" |
| F7 | sch 1B para 3(7), 7(2) (18843, 18874) | `sch 1B para 3(1) the effect of the restrictions notice applies to the act`, `sch 1B para 5(1)`, `5(3)`, `5(4)`, `6(a)`, `6(b)` | "subject to any direction": (i) an act a direction covers is `NOTHING` (the direction's content is outside the question); (ii) it is `JUST FALSE` (not restricted, no offence) | (i), by ruling (c) (a limit of the grant in its own wording, with no "only") | "The provisions of this section are subject to any directions given under paragraph 4"; "The provisions of those paragraphs are subject to any direction given under paragraph 4 or 8" |
| F8 | sch 1C para 13(1) (19022) | `sch 1C para 13(1) the time allowed for acceptance is within the limits the rules must ensure` | "the period of two weeks nor more than the period of 10 weeks beginning with the day after the date of publication": (i) both periods begin with the day after publication, so the earliest last day is publication plus 14 days and the latest is plus 70 days; (ii) "beginning with the day after" qualifies only the ten weeks, and the two weeks begin on the date of publication (the earliest last day is publication plus 13) | (i) | the single phrase "beginning with the day after the date of publication" at the end of the sentence |
| F9 | sch 1C para 17(1) (19036-19038) | `sch 1C para 17(1) the rules must require the board to obtain the prior authorisation of a general meeting` | (i) a day outside "the relevant period" answers `JUST FALSE` (ruling (a)); an action that is "seeking alternative takeover bids" answers `JUST FALSE` (the "other than" is met); (ii) both answer `NOTHING` | (i) | para 17(2) fixes the relevant period; "other than seeking alternative takeover bids" |
| F10 | sch 1C para 8(1) (18973) | `sch 1C para 8(1) the equitable price` | "over a period, determined by rules, of not less than 6 and not more than 12 months before the mandatory takeover bid is announced": (i) a purchase counts if it is before the announcement day and its date plus the period in months is not before the announcement day; a period outside 6 to 12 months answers `NOTHING`; (ii) purchases on the announcement day count; (iii) a period outside 6 to 12 is used as given | (i) | the period is "determined by rules", an input; the text bounds it |
| F11 | sch 1B para 1(2) (18816) | `sch 1B para 1(2) the company may give the person a warning notice` | when paragraph 1 does not apply ("(1) This paragraph applies if ..."): (i) the text is silent whether the company may give a warning notice, so `NOTHING`; (ii) the failed "if" is the text's own no, so `JUST FALSE` ("may not") | (i): a function named for a power does not turn a failed "if" gate into "may not"; the "if" is not "only if" (name-test sweep of 2026-11-12, Part E; was `JUST FALSE`) | "(2) The company may give the person a notice under this paragraph" after "(1) This paragraph applies if" |
| F12 | sch 1B para 4(1) (18845) | `sch 1B para 4(1) the court may give a direction` | when the application is not by a person aggrieved, or the court is not satisfied that the notice unfairly affects third parties' rights: (i) the text is silent whether the court may give a direction, so `NOTHING`; (ii) the failed "if" is the text's own no, so `JUST FALSE` ("may not") | (i), as F11 (was `JUST FALSE`) | "The court may give a direction under this paragraph if, on application by any person aggrieved, the court is satisfied that ...", not "only if" |

### Part C: the six questions the case-by-case decision leaves to the encoder

**(a) An "unless" or "except" once it is met** (including the "only after" and "must not ... unless" bars).

| Provision | Function | Site | Answer taken | Other reading |
|---|---|---|---|---|
| s 1288 | `s 1288 the regulations or order under this Act must be made by statutory instrument` | "Except as otherwise provided" is met | `JUST FALSE` | `NOTHING`: another provision decides, outside the sources |
| s 1290 | `s 1290 the regulations or order are barred from being made` | "unless a draft ... has been laid ... and approved" is met | `JUST FALSE` (not barred) | `NOTHING` |
| s 1291(1)(b) | `s 1291(1)(b) the regulations or order have ceased to have effect` | "unless during that period they are approved by resolution of each House" is met | `JUST FALSE` | `NOTHING` |
| s 1292A | `s 1292A the reference to the Bank of England includes the Bank acting as the Prudential Regulation Authority` | "except in section 796" is met (the reference is in s 796) | `NOTHING` | `JUST TRUE`: the exception displaces the rule, so the reference includes the Bank there |
| s 1293 | `s 1293 the provision is an enactment` | "unless the context otherwise requires" is met | `NOTHING` | `JUST FALSE` |
| s 1299 | `s 1299 the provision extends to the whole of the United Kingdom` | "Except as otherwise provided (or the context otherwise requires)" is met | `JUST FALSE` | `NOTHING`: what extent it has then is outside the text |
| sch 1A para 20(1) | `sch 1A para 20(1) the right is treated as held by the person` | "(and not by the person who in fact holds the right, unless that person also controls it)": the holder in fact also controls it | `JUST TRUE` for the holder (it controls it); `JUST FALSE` for a holder who does not control it while another person does | `NOTHING` for the holder who does not control it |
| sch 1A para 21(2) | `sch 1A para 21(2) the thing counts as an arrangement` | "does not count as an arrangement unless there is at least some degree of stability" is met (there is stability) | `NOTHING`: the sub-paragraph says what does not count, not what does | `JUST TRUE` |
| sch 1B para 3(1)(d), 3(4) | `sch 1B para 3(1) the effect of the restrictions notice applies to the act`; `sch 1B para 3(4) the agreement to transfer the associated right is void` | "except in a liquidation" / "(otherwise than in a liquidation)" is met | `JUST FALSE` for the payment restriction and the associated-right transfer in a liquidation | `NOTHING` |
| sch 1B para 8(3) | `sch 1B para 8(3) the court is barred from making an order under paragraph 8` | "must not make an order ... unless" (a) or (b) is met | `JUST FALSE` (not barred) | `NOTHING` |
| sch 1C para 5 | `sch 1C para 5 the offeror is barred from announcing the takeover bid yet` | "must announce a takeover bid only after" (a) and (b) is met | `JUST FALSE` | `NOTHING` |
| sch 1C para 17(1) | `sch 1C para 17(1) the rules must require the board to obtain the prior authorisation of a general meeting` | "other than seeking alternative takeover bids": the action is seeking alternative bids | `JUST FALSE` | `NOTHING` |

**(b) A bare "must" not done** (fork F3; the answer is the compliance function, not the consequence).

| Provision (function) | Site | Words | Answer taken | Other reading |
|---|---|---|---|---|
| `s 1278(3) the regulations meet the requirement to specify by whom the duty is to be fulfilled` | coa28-part44.l4:203 | "The regulations must specify by whom, in the case of any description of institution, the duty imposed by the r..." | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `s 1291(1)(a) the requirement to lay the regulations or order before Parliament after being made h...` | coa28-part46.l4:83 | "must be laid before Parliament after being made" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1A para 24(1) the Secretary of State has issued the guidance` | coa28-sch1a.l4:497 | "The Secretary of State must issue guidance" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1A para 24(3) the Secretary of State has laid a draft of the guidance before Parliament befor...` | coa28-sch1a.l4:519 | "Before issuing guidance under this paragraph the Secretary of State must lay a draft of it before Parliament" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1B para 1(6) the company has had regard to the effect of the notice on the rights of third pa...` | coa28-sch1b.l4:89 | "the company must have regard to the effect of the notice on the rights of third parties" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1B para 4(4)(a) the order containing the direction meets the requirement to specify the acts` | coa28-sch1b.l4:271 | "An order containing a direction under this paragraph— (a) must specify the acts that will not constitute a bre..." | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 3 the board of the offeree company complies with the principle` | coa28-sch1c.l4:96 | "must act in the interests of the company as a whole and must not deny the holders of securities the opportunit..." | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 7(2) the mandatory takeover bid meets the requirement the rules must ensure` | coa28-sch1c.l4:194 | "the mandatory takeover bid must be addressed at the earliest opportunity to all of the holders of those securi..." | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 8(4) the Panel's decision to adjust the equitable price meets the requirement` | coa28-sch1c.l4:251 | "any decision by the Panel to adjust the equitable price must be substantiated and made public" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 11(1) the decision to make a takeover bid has been made public and the Panel informed...` | coa28-sch1c.l4:321 | "a decision to make a takeover bid must be made public without delay and the Panel must be informed of the bid" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 12(1) the offeror has met the requirement to draw up and make public an offer document` | coa28-sch1c.l4:345 | "an offeror must draw up and make public in good time an offer document containing the information necessary" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 12(2) the offeror has met the requirement to provide a copy to the Panel before the o...` | coa28-sch1c.l4:354 | "before the offer document is made public, the offeror must provide a copy to the Panel" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 12(4) the offer document states at least the information the rules must require` | coa28-sch1c.l4:419 | "the offer document must state at least— (a) ... (q)" | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 17(3) the rules must require a general meeting to approve or confirm the decision` | coa28-sch1c.l4:548 | "with regard to decisions taken before the beginning of the relevant period and not yet partly or fully impleme..." | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |
| `sch 1C para 18(1) the board has met the requirement to draw up and make public its opinion` | coa28-sch1c.l4:581 | "the board of directors of the offeree company must draw up and make public a document setting out its opinion ..." | `JUST FALSE` (the requirement is not met) | `NOTHING` (the text says what must be done, not what follows) |

**(c) "Listed in Schedule N" (and a list the text hands a definition or an offence to).**

| Provision | Function | Site | Answer taken | Other reading |
|---|---|---|---|---|
| sch 1C para 21(2) | `sch 1C para 21(2) the provision is one of the listed provisions` | "The listed provisions are— paragraph 4(b) and (c); paragraph 12(4)(b), (l) and (p); paragraph 15(b) and (c)": a provision not among them | `JUST FALSE` (a definition handed to a list: delegated-definitions ruling (a)) | `NOTHING` |
| sch 1B para 5(1), 5(2) | `sch 1B para 5(1) the person commits an offence` | "does anything listed in sub-paragraph (2)": a thing that is not on the list | `NOTHING` (the list names the things that are offences; the text does not say another thing is not) | `JUST FALSE` (an offence handed to a list) |

**(d) A duty whose "if" or "where" is unmet.** The duty-bearing functions among the failed-condition branches are below; every failed "if" or "where" in the range, duty or not, is in the marginal readings section (M1), with the same answer and the same other reading.

| Provision (function) | Site | Words | Answer taken | Other reading |
|---|---|---|---|---|
| `s 1283 paragraph 3(1) of Schedule 3 to the Commonhold and Leasehold Reform Act 2002 applies to th...` | coa28-part44.l4:499 | "Where a commonhold association alters its memorandum or articles at a time when the land specified in its memo..." | `JUST FALSE` | `NOTHING` |
| `s 1290 the regulations or order are barred from being made` | coa28-part46.l4:60 | "Where regulations or orders under this Act are subject to “affirmative resolution procedure”" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 24(4) the Secretary of State must take no further steps in relation to the draft` | coa28-sch1a.l4:554 | "If, within the 40-day period, either House of Parliament resolves not to approve the draft guidance" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 24(4) the Secretary of State must take no further steps in relation to the draft` | coa28-sch1a.l4:555 | "If, within the 40-day period, either House of Parliament resolves not to approve the draft guidance" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 24(5) the Secretary of State must issue and publish the guidance in the form of the d...` | coa28-sch1a.l4:567 | "If no such resolution is made within that period, the Secretary of State must issue and publish the guidance i..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 9(1) paragraph 9 applies` | coa28-sch1a.l4:822 | "This paragraph applies where V— (a) ... and (b) ..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 1(1) paragraph 1 applies` | coa28-sch1b.l4:30 | "This paragraph applies if" | `JUST FALSE` | `NOTHING` |
| `sch 1B para 1(3) the company may issue the restrictions notice` | coa28-sch1b.l4:71 | "if, by the end of the period of one month ..., (a) the person has not complied ..., and (b) the company has no..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 5(1) the person commits an offence` | coa28-sch1b.l4:329 | "A person commits an offence if the person does anything listed in sub-paragraph (2) knowing that the interest ..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 5(3) the person commits an offence` | coa28-sch1b.l4:351 | "A person who has a relevant interest that the person knows to be subject to restrictions commits an offence if..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 5(4) the person commits an offence` | coa28-sch1b.l4:367 | "A person commits an offence if the person— (a) either has a relevant interest that the person knows to be subj..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 6(a) the company commits an offence` | coa28-sch1b.l4:390 | "If shares in a company are issued in contravention of a restriction imposed by virtue of a restrictions notice..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 6(b) the officer of the company commits an offence` | coa28-sch1b.l4:404 | "If shares in a company are issued in contravention of a restriction imposed by virtue of a restrictions notice..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 11 the company must by notice withdraw the restrictions notice` | coa28-sch1b.l4:602 | "A company that issues a person with a restrictions notice under paragraph 1 must by notice withdraw the restri..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 13(1) the person commits an offence by failing to comply with the notice` | coa28-sch1b.l4:636 | "A person to whom a notice under section 790D, 790DA, 790E or 790EA is addressed commits an offence if the pers..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 13(2) the officer of the entity commits an offence` | coa28-sch1b.l4:647 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14(1) the person commits an offence by failing to comply with the duty` | coa28-sch1b.l4:680 | "A person commits an offence if the person fails, without reasonable excuse, to comply with a duty under sectio..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14(2) the officer of the entity commits an offence` | coa28-sch1b.l4:691 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14A(1) the person commits the basic offence of making a false statement` | coa28-sch1b.l4:724 | "A person commits an offence if, in purported compliance with a notice ... and without reasonable excuse, the p..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14A(2) the officer of the entity commits an offence` | coa28-sch1b.l4:735 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14B(1) the person commits the aggravated offence of making a false statement` | coa28-sch1b.l4:764 | "A person commits an offence if, in purported compliance with a notice ..., the person makes a statement that t..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14B(2) the officer of the entity commits an offence` | coa28-sch1b.l4:775 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 1(2) the rules must protect the other holders of securities` | coa28-sch1c.l4:51 | "If a person acquires control of a company, the other holders of securities must be protected" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 2(2) the board of the offeree company must give its views on the effect of implementa...` | coa28-sch1c.l4:79 | "Where it advises the holders of securities" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 4 the creation of a false market in the securities of the company is barred` | coa28-sch1c.l4:119 | "(b) if the offeror is a company, that company" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 7(3) the obligation to make a mandatory takeover bid no longer applies` | coa28-sch1c.l4:163 | "where control has been acquired following a voluntary takeover bid to all the holders of securities for all th..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 7(1) the rules must require P to make a mandatory takeover bid` | coa28-sch1c.l4:179 | "Rules must ensure that a person (“P”) is required to make a takeover bid (“a mandatory takeover bid”) where— (..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 9(2) the rules must ensure that cash is offered as an alternative` | coa28-sch1c.l4:296 | "Rules must ensure that cash must be offered— (a) as an alternative where the consideration offered does not co..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 15 the rules must ensure that the takeover bid is made public so as to ensure market ...` | coa28-sch1c.l4:459 | "(b) if the offeror is a company, that company" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 18(3) the employees' representatives' opinion must be appended to the document` | coa28-sch1c.l4:605 | "where the board of directors of the offeree company receives in good time a separate opinion from the represen..." | `JUST FALSE` | `NOTHING` |

**(e) "(other than X)".**

| Provision | Function | Site | Answer taken | Other reading |
|---|---|---|---|---|
| s 1279(2) | `s 1279(2) the instrument is a depositary certificate` | "(other than options)": an instrument that confers only options | `JUST FALSE` (a "means" definition) | `NOTHING` |
| s 1281 241A(5) | `s 1281 241A(5) the person is barred from using the information for the purpose` | "any purpose other than those specified in subsection (1)": a purpose that is specified in (1) | `NOTHING`: the sentence bars other purposes and says nothing of these | `JUST FALSE` (not barred) |
| sch 1A para 18(1)(b)(i), 18(2)(b)(i) | `sch 1A para 18(1) the person holds the share indirectly`; `sch 1A para 18(2) ...` | "each of which (other than the last) has a majority stake in the entity immediately below it" | the chain is one plain input (`... each of which (other than the last) has a majority stake ... and the last of which holds the share`); the function does not test each link | test each link, with the last link tested for holding the share instead |
| sch 1A para 25(4)(a) | `sch 1A para 25(4) the individual is a limited partner for this paragraph` | "(other than one who takes part in the management of the partnership business)" | `JUST FALSE` for a limited partner who takes part in the management | `NOTHING` |
| sch 1C para 17(1)(a) | `sch 1C para 17(1) ...` | "other than seeking alternative takeover bids" | see (a) above | see (a) above |
| sch 1C para 21(1) | `sch 1C para 21(1) the body is a company for this Schedule` | "other than in the listed provisions": the provision is a listed one | `NOTHING`: there s 1 does not apply (21(3)) and the Schedule gives no other meaning | `JUST TRUE`: any company is a company there |

**(f) A missing event in the state ledger.** No site: this range has no state ledger and no function reads an event log.

### Part D: a question raised after the first report (2026-11-12)

The lead's consistency check read sch 1A para 23 against the periods, "where" and scope ruling and asked why its "where" limbs answered `NOTHING` when the "where" limits of s 1283, sch 1C paras 7(3), 9(2), 17(3) and 18(3) answer `JUST FALSE`.
Re-reading the paragraph (lines 18771-18773) shows two different limits, and I had filed both as `NOTHING`.
Its subject, "Rights attached to shares held by way of security provided by a person", is a scope limit with no "only", so ruling (c) applies and the answer outside it is `NOTHING`.
Its limbs, "(a) where ... and (b) where ...", are "where" conditions, so ruling (b) applies and the answer when one fails is `JUST FALSE`.
I took option (1): the "where" arm now answers `JUST FALSE`, and the subject arm stays `NOTHING` (the person asked about did not provide the security).
The other reading, the one first filed, is that the limbs limit the grant itself and answer `NOTHING` when they fail.

- Function changed: `sch 1A para 23 the rights are treated as held by the person who provided the security` (the `OTHERWISE` arm, was `NOTHING`, now `JUST FALSE`, with a `-- FALSE-kind` comment quoting the "where" words and a `RECONCILED 2026-11-12` note).
- Caller changed: `sch 1A paras 11 to 23 the block is treated as held by X` has a new constructor, `sch 1A para 23 rights attached to shares held by another by way of security provided by X, not meeting paragraph 23(a) and (b)`, which answers `JUST FALSE`.
  The older constructor `sch 1A para 23 rights attached to shares held by way of security, not meeting paragraph 23(a) and (b)` stays `NOTHING`, because it does not say whether X provided the security or holds it, and para 23 answers `JUST FALSE` only for the provider.
- Assertions restated in place, each with `-- RECONCILED 2026-11-12: was NOTHING; ...`: four.
  Three are in `coa28-tests-sch1a.l4`: `sch 1A para 23 the rights are treated as held by the person who provided the security` with the inputs `TRUE FALSE TRUE TRUE`, `TRUE TRUE FALSE TRUE` and `TRUE TRUE TRUE FALSE`, each now `EQUALS JUST FALSE`.
  One is in `coa28-cases-seat.l4`: `Under schedule 1A paragraph 23, are the rights treated as held by the person who provided the security` with `TRUE TRUE FALSE TRUE`, now `EQUALS JUST FALSE`.
- Assertions added: one block-level test for the new constructor (`JUST FALSE`), and one seat case where the security was not provided by the person asked about (`FALSE TRUE TRUE TRUE EQUALS NOTHING`, the scope limit).

### Part E: Name-test sweep of 2026-11-12

The lead asked for every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" to be tested for a grant or power turned into a bar: a function named for a grant that answers `JUST FALSE` because an "if" gate failed reads as "may not", and the Guide (section 5, "In short") gives `NOTHING` where the text limits a grant in its own wording and the case falls outside the limit.
Twenty-six functions matched the name test.
Seventeen of them already answer only `JUST TRUE` or `NOTHING` (for example `sch 1B para 8(2)`, `9(1)`, `9(3)`, `9(4)`, `9(5)`, `10(2)` and `s 1292(2)` to `(4)`), and two are not grants or powers (`s 1275(6)` says when amendments have effect in relation to the exercise of a power, and `sch 1 para 5(2)` is about "voting power").
The other seven are in the table; the first column is flipped, the others are kept or listed.

| flipped to `NOTHING` | kept `JUST FALSE` (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 2 | 2 | 1 | 2 |

**Flipped to `NOTHING`** (one fork line each, F11 and F12 in Part B, and in the marginal readings; the other reading is `JUST FALSE`, a failed "if" read as the text's own no):

- `sch 1B para 1(2) the company may give the person a warning notice` (F11).
- `sch 1B para 4(1) the court may give a direction` (F12).

**Kept `JUST FALSE`:**

- `sch 1B para 9(2) the person may apply for an order under sub-paragraph (1)`: the text says "may only be made by the company in question".
- `s 1281 241A(1) the public authority may disclose the information to any person`: its `JUST FALSE` arm is the flat negative of s 241A(2), "Subsection (1) does not apply to ...", and every other arm already answers `NOTHING` or `JUST TRUE`.

**Listed, not flipped: "may" with a "where", "when" or "upon" gate** (assumed, not ruled, that these equivalents go with the listed group; ruling (b) of the periods and "where" ruling says `JUST FALSE`, and the Guide's line on grants points the other way, which is a question for the maintainer or a lawyer):

- `sch 1B para 1(3) the company may issue the restrictions notice`: the gate is "if, by the end of the period of one month beginning with the date on which the warning notice was given, (a) ... and (b) ...", a condition of the "after" kind; the function answers `JUST FALSE` while the month has not ended and when (a) or (b) fails.
  The other reading is `NOTHING` on both arms.

**Listed, not flipped: "entitled"** (an entitlement is a claim, not a power, and the Guide does not settle it):

- `sch 1 para 4(2) the person is taken to be entitled to exercise or control the exercise of a right conferred by the holding of shares`.
- `sch 1 para 5(1)(b) the person is entitled to exercise or control the exercise of more than one-half of the voting power at general meetings of the body corporate`.
- Both answer `JUST FALSE` when their "if" fails, and both are counting rules about who controls a right, not claims to anything; they are listed because the name test matches them.
  The one "entitled" function that is a claim, `sch 1B para 10(4)` (the applicant's costs), already answers `NOTHING` outside its gate.

## Jural relations (coa28)

One row per provision (or run of provisions) that creates a relation, giving the holder of the right, privilege, power or immunity, the bearer of the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it.
A provision that creates no relation (a definition, a counting rule, a scope rule, a procedure) is listed once as `none`.
A relation is stated once, neutrally, never from both sides.
Where the text names only one party, the other is marked "not named in the text" or "by inference"; I have not invented a holder.
The kinds are Hohfeld's: claim/duty, privilege/no-right, power/liability, immunity/disability.
Most of this range is machinery or counting rules, so most rows are `none`; the relations are in the enforcement paragraphs of Schedule 1B (company against holder, court against applicant, State against offender), in s 241A, in s 1277(4) and s 1297(3), and in the second-order "rules must ensure" paragraphs of Schedule 1C, where the Takeover Panel is the bearer of a duty to make rules and the offeror and the board bear the first-order duties through those rules.
Every row of the coverage table that is not inert is mapped to exactly one row here (the script checks that no encoded or fork row is left out).
The regulation-, order- and rule-making powers (inert 2) are Hohfeldian powers with a correlative liability, and one summary row lists them; the other inert rows (headings, signposts, amendments of other Acts, commencement, short title, the repeal in s 1295) create no relation of their own and are not listed again.

| Provision | Holder (right, privilege, power, immunity) | Kind | Bearer (duty, no-right, liability, disability) | L4 rule | Note |
|---|---|---|---|---|---|
| s 1274(3) | none | none | none | `s 1274(3) the body is a professional actuarial body`; `s 1274(3) the person is a member of a professional actuarial body`; `s 1274(3) function` (and 1 more) | definitions (professional actuarial body, members, regulatory functions) |
| s 1275(3) (inserted s 17(3A)) | the body that may require the levy (as the 2004 Act's s 17 gives it the power) | power / liability | administrators of a public service pension scheme; trustees or managers of an occupational or personal pension scheme | `s 1275(3) the person is within subsection (3A) of section 17 of the 2004 Act` | this paragraph says who is within the class that may be required to pay; the power itself is in s 17 of the 2004 Act, outside the sources |
| s 1275(5) (inserted s 17(13)), s 1275(6) | none | none | none | `s 1275(5) the draft is to proceed in that House as if it were not a hybrid instrument`; `s 1275(6) the amendments have effect in relation to the exercise of the power` | parliamentary procedure for a hybrid instrument; application in time |
| s 1276(2), (4)(c) | none | none | none | `s 1276(2) the matter is one to which subsection (2)(a) to (t) of section 16 of the 2004 Act is read as referring in Scotland`; `s 1276(4)(c) the instrument is the 1986 Order` | scope of the amended 2004 Act in Scotland; a definition |
| s 1277(3) | none | none | none | `s 1277(3)(a) the person is a person acting on behalf of the institution`; `s 1277(3)(b) the matter is specified for the purposes of sections 1277 to 1280` | definitions |
| s 1277(4) | any person to whom the information should have been provided; a specified regulatory authority | power (to sue) / liability | the institution (or person acting for it) that was to give the information | `s 1277(4) the person may bring civil proceedings to enforce the obligation` | 'enforceable by civil proceedings by' names the holders of the power |
| s 1277(6) | none | none | none | `s 1277(6) the procedure for regulations under section 1277` | procedure for the regulations |
| s 1278(1), s 1279, s 1280(5)(b), (6) | none | none | none | `s 1278(1) the institution is one to which section 1277 applies`; `s 1279(1) the shares are shares to which section 1277 applies`; `s 1279(2) the institution has an interest in the shares` (and 6 more) | scope and definitions: which institutions and shares the information regulations apply to; what 'aggregated form' and 'instructions' mean |
| s 1278(3) | institutions (the persons whose duty the regulations assign) | claim / duty | the Treasury or the Secretary of State (the maker of the regulations), who must specify by whom the duty is fulfilled | `s 1278(3) the regulations meet the requirement to specify by whom the duty is to be fulfilled` | the text puts the duty on the regulation-maker; it names no holder of the claim, so the institutions are the natural one (an inference) |
| s 1281 (241A(1)) | a public authority holding prescribed information | privilege / no-right | the person the information concerns (the text does not name the person) | `s 1281 241A(1) the public authority may disclose the information to any person` | the authority 'may disclose'; the text does not say who loses a right |
| s 1281 (241A(2)) | none | none | none | `s 1281 241A(2) subsection (1) does not apply to the information` | exclusions that take the information outside the privilege of 241A(1) |
| s 1281 (241A(3), (4)(c)) | none | none | none | `s 1281 241A(3) the information or proceedings are prescribed`; `s 1281 241A(1) purpose`; `s 1281 241A(4)(c) the procedure for an order under section 241A` | definition of 'prescribed'; procedure for orders |
| s 1281 (241A(5)) | not named in the text | claim / duty (SHANT: `s 1281 241A(5) the recipient's prohibition on use`) | the person to whom information is disclosed under s 241A | `s 1281 241A(5) the person is barred from using the information for the purpose`; `s 1281 241A(5) party`; `s 1281 241A(5) action` (and 1 more) | the text puts the duty on the recipient and names no holder |
| s 1282 (176ZA(1)); (150ZA(1)) | those owed the expenses of the winding up (the text does not name them) | claim / duty (a priority) | the holders of the floating charge and any preferential creditors, whose claims rank behind to the extent the assets of the company available for general creditors are insufficient | `s 1282(1) 176ZA(1) the expenses of winding up have priority over claims to property comprised in or subject to a floating charge`; `s 1282(1) 176ZA(1) the amount of the expenses that has priority over floating charge claims`; `s 1282 claimant` (and 2 more) | the priority is stated as a rank; the correlatives are stated here as claim and duty (a lawyer may prefer power and liability) |
| s 1282 (176ZA(2), (4); 150ZA(2), (4)) | none | none | none | `s 1282(1) 176ZA(2)(a) the assets of the company available for payment of general creditors`; `s 1282(1) 176ZA(2)(b) the claim is a claim to property comprised in or subject to a floating charge`; `s 1282(1) 176ZA(4) the expense is an expense of the winding up` (and 3 more) | definitions |
| s 1283 | none | none | none | `s 1283 paragraph 3(1) of Schedule 3 to the Commonhold and Leasehold Reform Act 2002 applies to the alteration` | substituted words in the Commonhold and Leasehold Reform Act 2002; the effect is in that Act, outside the sources |
| ss 1284 to 1287 | none | none | none | `s 1284(1) the provision extends to Northern Ireland`; `s 1284(2) instrument`; `s 1284(2) the instrument ceases to have effect` (and 11 more) | extent to Northern Ireland and the ceasing of earlier Northern Ireland enactments: provisions of extent between legislatures, no relation between persons |
| s 1288 | not named in the text | claim / duty | whoever makes regulations or orders under the Act | `s 1288 the regulations or order under this Act must be made by statutory instrument` | 'shall be made by statutory instrument': a duty with no named holder |
| s 1289 | each House of Parliament | power / liability | the regulations or order (annulled by a resolution of either House) | `s 1289 the statutory instrument is subject to annulment in pursuance of a resolution of either House of Parliament` | the relation is between a House and the instrument; no person is named as liable |
| s 1290 | each House of Parliament (its approval) | power / disability | the maker of the regulations or order, who must not make them unless the draft was laid and approved by each House | `s 1290 the regulations or order are barred from being made`; `s 1291(2) kind of interval`; `s 1291(2) interval` |  |
| s 1291(1) | each House of Parliament (approval in the 28 days) | power / liability | the regulations or order, which cease to have effect unless approved; the maker, who must lay them | `s 1291(1)(a) the requirement to lay the regulations or order before Parliament after being made has been met`; `s 1291(1)(b) the last day of the 28 days beginning with the day on which they were made`; `s 1291(1)(b) the regulations or order have ceased to have effect` (and 4 more) | (2) is a counting rule: none for it |
| s 1291(3) | anyone who did something under the regulations or order | immunity / disability | anyone who might say the thing is undone by the ceasing; the maker keeps the power to make new regulations | `s 1291(3) the regulations or order ceasing to have effect affects the thing` |  |
| s 1292(2), (3), (4) | the maker of regulations or orders | power / liability | those subject to the regulations or order | `s 1292(2) the provision may be made by order`; `s 1292(2) the provision may be made by regulations`; `s 1292(3) the provision may be made subject to the procedure` (and 1 more) | extends which instrument may carry a provision and which procedure applies |
| s 1292A, s 1293 | none | none | none | `s 1292A the reference to the Bank of England includes the Bank acting as the Prudential Regulation Authority`; `s 1293 kind of provision`; `s 1293 the provision is an enactment` | interpretation |
| s 1294(6), s 1296(4) | none | none | none | `s 1294(6) the procedure for an order under section 1294`; `s 1296(4) the procedure for an order under section 1296` | procedure for orders (each stated only in the sentence that gives the procedure) |
| s 1297(1), (2) | none | none | none | `s 1297(1) section 1297 applies`; `s 1297(2) the repeal and re-enactment affects the continuity of the law` | when the section applies; continuity |
| s 1297(3) | a person who did something under the repealed provision | immunity / disability | anyone who might say the thing lapsed with the repeal | `s 1297(3) the thing has effect thereafter as if done under or for the purposes of the corresponding provision of this Act` | 'has effect thereafter as if done under' the corresponding provision |
| s 1297(4), (5), (6), (7), (8) | none | none | none | `s 1297(4) the reference to the provision of this Act is construed as including a reference to the corresponding repealed provision`; `s 1297(5) the reference to the repealed provision is construed as being or including a reference to the corresponding provision of this Act`; `s 1297(6) section 1297 yields to a specific transitional provision or saving` (and 2 more) | rules of reading; saving; interpretation |
| s 1299 | none | none | none | `s 1299 the provision extends to the whole of the United Kingdom` | extent |
| the regulation-, order- and rule-making powers (ss 1277(1), (2), (5), 1278(2), 1279(1) closing sentence, 1280(1) to (5)(a), 241A(4)(a) and (b), 176ZA(3), 150ZA(3), 1292(1), 1294(1) to (5), 1296(1) to (3); sch 1A paras 25(6), 26(1) and (2); sch 1B para 12(1) and (2); sch 1C paras 8(3), 9(4), 11(2), 13(2), 14) | the Secretary of State and the Treasury (the regulations and orders); the maker of the rules (s 176ZA(3), Article 150ZA(3): the text names none); the Takeover Panel (sch 1C: the rules may confer powers on it or require things) | power / liability | those the regulations, orders or rules bind | none (inert 2) | filed inert 2 (reason: regulation-making and rule-making powers): each is a power with its correlative liability, and none is encoded |
| Schedule 1, paras 1 to 6 | none | none | none | `sch 1 para 1(1) the provisions of this Schedule govern the reference`; `sch 1 para 1(2) kind of security`; `sch 1 para 1(2) the provisions of this Schedule apply to the security` (and 27 more) | every paragraph is a counting rule: who is taken to have an interest in shares or debentures for ss 254 and 255; the duties that turn on the interest are in those sections (coa5) |
| Schedule 1A, Part 1, paras 1 to 6; Part 2, paras 8 and 9; Part 3, paras 11 to 23 and 25; para 26(3) | none | none | none | `sch 1A para 1 at least one of the specified conditions is met by X in relation to company Y`; `sch 1A para 2 the first condition is met`; `sch 1A para 3 the second condition is met` (and 49 more) | conditions, definitions and counting rules for 'significant control'; the register duties that turn on them are in ss 790C onwards (coa17) |
| sch 1A para 24(1), (3), (5) | not named in the text | claim / duty | the Secretary of State, who must issue guidance, lay a draft, and issue it in the form of the draft | `sch 1A para 24(1) the Secretary of State has issued the guidance`; `sch 1A para 24(3) the Secretary of State has laid a draft of the guidance before Parliament before issuing it`; `sch 1A para 24(5) the Secretary of State must issue and publish the guidance in the form of the draft` | no holder is named |
| sch 1A para 24(2) | not named in the text | claim / duty | whoever interprets the Schedule's references to 'significant influence or control' | `sch 1A para 24(2) regard must be had to the guidance` | regard must be had to the guidance |
| sch 1A para 24(4), (6), (7), (8), (9) | each House of Parliament (its resolution in the 40 days) | power / liability | the Secretary of State, who must then not issue the draft; the counting rules of (7) and (8) are none | `sch 1A para 24(4) the Secretary of State must take no further steps in relation to the draft`; `sch 1A para 24(6) sub-paragraph (4) prevents a new draft of proposed guidance from being laid before Parliament`; `sch 1A para 24(7) the day on which the 40-day period begins` (and 2 more) | (6), (7), (8), (9) give no relation of their own |
| sch 1B para 1(1), (2), (3) | the company | power / liability | the person who failed to comply with the notice | `sch 1B para 1(1) paragraph 1 applies`; `sch 1B para 1(2) the company may give the person a warning notice`; `sch 1B para 1(3) the last day of the period of one month beginning with the date on which the warning notice was given` (and 1 more) | the company may give a warning notice and, after the month, issue the restrictions notice |
| sch 1B para 1(4) | none | none | none | `sch 1B para 1(4) the restrictions notice is issued on the person` | when a notice is issued (by sending it) |
| sch 1B para 1(6) | third parties with rights in respect of the relevant interest | claim / duty | the company (`sch 1B para 1(6) the company's duty to have regard to the rights of third parties`) | `sch 1B para 1(6) the company has had regard to the effect of the notice on the rights of third parties`; `sch 1B para 1(6) action`; `sch 1B para 1(6) the company's duty to have regard to the rights of third parties` | the company must have regard; the text names the third parties' rights, not their claim |
| sch 1B para 2 | none | none | none | `sch 1B para 2(1) the person has a relevant interest in the company`; `sch 1B para 2(2) the thing is the relevant interest`; `sch 1B para 2(3) the person is regarded as having the relevant interest` | what a relevant interest is |
| sch 1B para 3(1) | the company (inferred: the text states the effect on the interest, not whose immunity it is) | immunity / disability | the holder of the relevant interest, who cannot validly transfer it, exercise rights, be issued shares or be paid sums due | `sch 1B para 3(1) the effect of the restrictions notice applies to the act` | the restrictions notice's effect |
| sch 1B para 3(2), (3), (4), (5) | not named in the text | disability (no power to bind) | the parties to an agreement to transfer the interest or an associated right: the agreement is void | `sch 1B para 3(2) the agreement to transfer the interest is void`; `sch 1B para 3(3) sub-paragraph (2) applies to the agreement`; `sch 1B para 3(4) the agreement to transfer the associated right is void` (and 1 more) |  |
| sch 1B para 3(6), (7) | none | none | none | `sch 1B para 3(6) the right is an associated right in relation to the relevant interest`; `sch 1B para 3(7) the provisions of paragraph 3 are subject to the direction`; `sch 1B para 3(1) act` | definition of associated right; the effect is subject to directions |
| sch 1B para 4(1) | a person aggrieved (to apply); the court (to give a direction) | power / liability | the company and the holder of the interest, whose restrictions the direction relaxes | `sch 1B para 4(1) the court may give a direction` |  |
| sch 1B para 4(3), (4), (5) | not named in the text | claim / duty | the court, which must specify the acts an order's direction covers (4(4)(a)); (3) and (5) give no relation of their own | `sch 1B para 4(3) the act does not constitute a breach of the restrictions placed on the relevant interest`; `sch 1B para 4(4)(a) the order containing the direction meets the requirement to specify the acts`; `sch 1B para 4(4)(b) the order may confine the direction to cases where the acts are done by persons or for purposes described in the order` (and 1 more) |  |
| sch 1B para 5(1), (3), (4); para 6 | the State (the offence is public) | claim / duty (the offences) | a person who deals in a restricted interest knowing it is restricted; a person who does not tell a person entitled to vote; a person who enters into a void agreement; the company and every officer in default where shares are issued in contravention of a restriction | `sch 1B para 5(1) the person commits an offence`; `sch 1B para 5(3) the person commits an offence`; `sch 1B para 5(4) the person commits an offence` (and 2 more) | the text states an offence and a penalty; the correlative claim is the State's by inference |
| sch 1B para 5(5) | none | none | none | `sch 1B para 5(5) the interest is subject to restrictions` | definition of 'subject to restrictions' |
| sch 1B para 7 | the court (to impose the penalty) | power / liability | a person guilty of an offence under paragraph 5 or 6 | `sch 1B para 7(1) the penalty for an offence under paragraph 5 or 6`; `sch 1B para 7(2) the provisions of paragraphs 5 and 6 are subject to the direction`; `sch 1B para 5(2) thing` | 7(2) makes the offences subject to directions |
| sch 1B para 8(1), (2), (4), (5) | the company in question; any person aggrieved (to apply); the court (to make the order) | power / liability | the restrictions on the interest (which may cease) and the persons they bind | `sch 1B para 8(2) the person may apply for an order under paragraph 8`; `sch 1B para 8(4) the order may continue the restriction`; `sch 1B para 8(5)(a) an application may be made for an order directing that the relevant interest cease to be subject to those restrictions` (and 1 more) |  |
| sch 1B para 8(3) | not named in the text (the company that issued the notice, whose restrictions the order would lift, is the natural holder) | immunity / disability | the court, which must not make the order unless the information was disclosed and no unfair advantage accrued, or the transfer is for valuable consideration and approved | `sch 1B para 8(3) the court is barred from making an order under paragraph 8` |  |
| sch 1B para 9 | the company (to apply for a sale); the court (to order a sale); the person appointed to effect the sale; any person with an interest | power / liability | the holder of the relevant interest, whose interest may be sold | `sch 1B para 9(1) the court may order that the relevant interest be sold subject to the court's approval as to the sale`; `sch 1B para 9(2) the person may apply for an order under sub-paragraph (1)`; `sch 1B para 9(3) the court may make such further order relating to the sale or transfer of the interest as it thinks fit` (and 2 more) |  |
| sch 1B para 10 | a person beneficially interested in the relevant interest | claim / duty | the court, which must order the proceeds (with interest) paid to the applicant, or a proportion | `sch 1B para 10(1) the amount that must be paid into court`; `sch 1B para 10(2) the person may apply to the court for the whole or part of the proceeds to be paid to the person`; `sch 1B para 10(3) the amount the court must order to be paid to the applicant` (and 1 more) | 10(1), (2), (4) give the payment into court, the application and the costs |
| sch 1B para 11 | not named in the text (the person who was issued the notice is the one affected) | claim / duty (MUST: `sch 1B para 11 the company's duty to withdraw the restrictions notice`) | the company that issued the restrictions notice | `sch 1B para 11 the company must by notice withdraw the restrictions notice`; `sch 1B para 11 action`; `sch 1B para 11 the company's duty to withdraw the restrictions notice` |  |
| sch 1B para 12(3) | none | none | none | `sch 1B para 12(3) the procedure for regulations under paragraph 12` | procedure for the regulations |
| sch 1B paras 13, 14, 14A, 14B | the State (the offences are public) | claim / duty (the offences and penalties) | a person to whom a notice is addressed, or on whom a duty under ss 790G, 790H, 790HA falls; every officer of a legal entity in default; a person who makes a false statement | `sch 1B para 13(1) the person commits an offence by failing to comply with the notice`; `sch 1B para 13(2) the officer of the entity commits an offence`; `sch 1B para 13(3) the penalty for an offence under paragraph 13` (and 9 more) | each paragraph states an offence, an extension to officers and a penalty by place of conviction |
| sch 1C paras 1 to 6 (general principles) | holders of securities of the offeree company; the offeree company; employees (para 2(2)) | claim / duty | the Takeover Panel (to make rules that give effect); through the rules, the offeror, the board of the offeree company and others | `sch 1C para 1(1) the rules must afford the holders equivalent treatment`; `sch 1C para 1(2) the rules must protect the other holders of securities`; `sch 1C para 2(1) the holders must have sufficient time and information to reach a properly informed decision on the takeover bid` (and 7 more) | 'must be afforded', 'must act', 'must announce only after': principles the rules must give effect to |
| sch 1C paras 7 to 10 (mandatory bid, equitable price, cash) | the other holders of securities of the company | claim / duty | the Panel (to make the rules); a person who acquired control (P) and persons acting in concert with P | `sch 1C para 7(1) the rules must require P to make a mandatory takeover bid`; `sch 1C para 7(2) the mandatory takeover bid meets the requirement the rules must ensure`; `sch 1C para 8(1) purchase` (and 10 more) | 8(1) and 9(2) set the price and cash alternative; the powers of the Panel (8(3), 9(4)) are inert 2 |
| sch 1C paras 11 to 12 (information, offer document) | holders of the offeree company's securities; employee representatives or the employees | claim / duty | the offeror and the boards of directors of the offeree company and of the offeror (through the rules the Panel must make) | `sch 1C para 11(1) the decision to make a takeover bid has been made public and the Panel informed as the rules must ensure`; `sch 1C para 11(3) the boards of the offeree company and of the offeror must inform`; `sch 1C para 12(1) the offeror has met the requirement to draw up and make public an offer document` (and 4 more) |  |
| sch 1C para 13 (time for acceptance) | holders of securities of the offeree company | claim / duty | the Panel (to make rules fixing at least two weeks and at most ten weeks) | `sch 1C para 13(1) the time allowed for acceptance is within the limits the rules must ensure`; `sch 1C para 15 company` |  |
| sch 1C paras 15, 16 (disclosure) | holders of securities admitted to trading on a UK regulated market; employee representatives or employees | claim / duty | the Panel (to make rules); the offeror and the offeree company (through the rules) | `sch 1C para 15 the rules must ensure that the takeover bid is made public so as to ensure market transparency and integrity for the securities of the company`; `sch 1C para 16 recipient`; `sch 1C para 16 the rules must ensure that the information and documents are readily and promptly available to the recipient` |  |
| sch 1C paras 17, 18 (the board's obligations) | the general meeting of the offeree company; holders; employees and their representatives | claim / duty | the board of directors of the offeree company (through the rules the Panel must make) | `sch 1C para 17(1) the rules must require the board to obtain the prior authorisation of a general meeting`; `sch 1C para 17(2) the day is within the relevant period`; `sch 1C para 17(3) the rules must require a general meeting to approve or confirm the decision` (and 6 more) | 17(4) says what 'board of directors' means for a two-tier board: none for it |
| sch 1C para 19 | holders of securities | claim / duty | the Panel, which must make rules governing the conduct of takeover bids addressing at least five matters | `sch 1C para 19 the rules must make provision on the topic` |  |
| sch 1C paras 20, 21 | none | none | none | `sch 1C para 20(1) the document is an offer document`; `sch 1C para 20(1) the company is an offeree company`; `sch 1C para 20(1) the person is the offeror in relation to the takeover bid` (and 12 more) | definitions, persons acting in concert, and the meaning of 'company' (with the listed provisions) |

## Marginal readings for a lawyer (coa28)

The brief leaves two readings for a lawyer to decide and asks me to take them as the status quo and list every branch that rests on one, with the other reading stated.
(a) A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if"; and a flat negative counts as the text saying no.
(b) A prohibition or grant limited by its own wording does not: outside the limit the answer is `NOTHING`.
The two sets below were harvested by script from the `-- FALSE-kind` and `-- NOTHING-kind` comments in the eight layer-1 modules (354 tagged branches), classified by the words quoted in the comment, and sorted by hand where the quotation did not decide the class (44 branches).
A branch is listed in exactly one class.
Branches that are not marginal are not listed: a "means" definition whose case is outside it (23 branches), a list closed with "only", the periods the text fixes (ruling (a)), and every `NOTHING` that is `silent`, `points outside the text`, `list not closed`, `includes` or `undefined term`.

Four readings are named, so the lawyer can overrule each as a class:

- **M1: a failed "if", "where", "so long as", "so far as" or "only if" is the text's no.**
  Taken: the function answers `JUST FALSE` when the condition fails.
  Other reading: the text is silent on "not A", so the answer is `NOTHING`.
  (The periods ruling already settles "where" and the stated periods as `JUST FALSE`; they are listed here because the same words rest on M1 when the lawyer's rule differs.)
- **M2: a defined term, a "condition" or a rule of reading introduced with "is", "are", "is that", "is to" or "are to be" and no "means" is read as closed, like a "means" definition.**
  Taken: `JUST FALSE` outside the stated cases.
  Other reading: an "is" statement without "means" or "only" says what is included and leaves the rest open, so `NOTHING`.
- **M3: an "are" or "is" scope statement with no quoted term ("the reference ... is to the claims of ...", "information given in aggregated form, that is ...") answers `NOTHING` outside the list.**
  Taken: `NOTHING`.
  Other reading: it is a closed definition and answers `JUST FALSE`.
- **N2: a flat negative ("does not", "must not", "shall not", "is not") is the text's no.**
  This is ruled (option A of N2, quoted in the fork register), so it is listed for completeness and not for overruling; the other reading is option C (a typed prohibition).

**Name-test flips of 2026-11-12 (one line each).**
A function named for a grant or a power does not turn a failed "if" gate into "may not".
`sch 1B para 1(2) the company may give the person a warning notice` and `sch 1B para 4(1) the court may give a direction` answer `NOTHING` when their "if" gate fails (forks F11 and F12 in the fork register); the other reading, in both, is `JUST FALSE`, a failed "if" read as the text's own no.
They are in the class-(b) table below.

**M1: a failed "if", "where", "so long as", "so far as" or "only if" (84 branches).**

| Function | Site | Words | Answer taken | Other reading |
|---|---|---|---|---|
| `s 1275(5) the draft is to proceed in that House as if it were not a hybrid instrument` | coa28-part44.l4:90 | "If a draft of any regulations to which subsection (10) applies would, apart from this subsection, be treated ...." | `JUST FALSE` | `NOTHING` |
| `s 1279(2) the institution has an interest in the shares` | coa28-part44.l4:214 | "For this purpose an institution has an interest in shares if the shares, or a depositary certificate in respec..." | `JUST FALSE` | `NOTHING` |
| `s 1279(4) the scheme or vehicle is taken to have an interest in the shares` | coa28-part44.l4:236 | "a scheme or vehicle is taken to have an interest in shares if it would be regarded as having such an interest ..." | `JUST FALSE` | `NOTHING` |
| `s 1279(3) the institution is taken to have an interest in the shares` | coa28-part44.l4:248 | "Where an institution has an interest— (a) in a specified description of collective investment scheme ..., or (..." | `JUST FALSE` | `NOTHING` |
| `s 1282(1) 176ZA(1) the expenses of winding up have priority over claims to property comprised in ...` | coa28-part44.l4:406 | "so far as the assets of the company available for payment of general creditors are insufficient to meet them, ..." | `JUST FALSE` | `NOTHING` |
| `s 1282(2) 150ZA(1) the expenses of winding up have priority over claims to property comprised in ...` | coa28-part44.l4:457 | "The expenses of winding up, so far as the assets of the company available for payment of general creditors are..." | `JUST FALSE` | `NOTHING` |
| `s 1283 paragraph 3(1) of Schedule 3 to the Commonhold and Leasehold Reform Act 2002 applies to th...` | coa28-part44.l4:499 | "Where a commonhold association alters its memorandum or articles at a time when the land specified in its memo..." | `JUST FALSE` | `NOTHING` |
| `s 1289 the statutory instrument is subject to annulment in pursuance of a resolution of either Ho...` | coa28-part46.l4:43 | "Where regulations or orders under this Act are subject to “negative resolution procedure” the statutory instru..." | `JUST FALSE` | `NOTHING` |
| `s 1290 the regulations or order are barred from being made` | coa28-part46.l4:60 | "Where regulations or orders under this Act are subject to “affirmative resolution procedure”" | `JUST FALSE` | `NOTHING` |
| `s 1297(1) section 1297 applies` | coa28-part46.l4:285 | "This section applies where any provision of this Act re-enacts (with or without modification) an enactment rep..." | `JUST FALSE` | `NOTHING` |
| `s 1297(3) the thing has effect thereafter as if done under or for the purposes of the correspondi...` | coa28-part46.l4:315 | "This section applies where" | `JUST FALSE` | `NOTHING` |
| `s 1297(4) the reference to the provision of this Act is construed as including a reference to the...` | coa28-part46.l4:335 | "This section applies where" | `JUST FALSE` | `NOTHING` |
| `s 1297(5) the reference to the repealed provision is construed as being or including a reference ...` | coa28-part46.l4:357 | "This section applies where" | `JUST FALSE` | `NOTHING` |
| `sch 1 para 3(1) the person is taken to have an interest in the shares by entering into a contract...` | coa28-sch1.l4:83 | "A person is taken to have an interest in shares if he enters into a contract to acquire them" | `JUST FALSE` | `NOTHING` |
| `sch 1 para 3(2) the person is taken to have an interest in the shares by a right to call for deli...` | coa28-sch1.l4:108 | "A person is taken to have an interest in shares if— (a) he has a right to call for delivery ..., or (b) he has..." | `JUST FALSE` | `NOTHING` |
| `sch 1 para 4(1) the person is taken to have an interest in the shares by an entitlement to exerci...` | coa28-sch1.l4:144 | "A person is taken to have an interest in shares if, not being the registered holder, he is entitled— (a) to ex..." | `JUST FALSE` | `NOTHING` |
| `sch 1 para 4(2) the person is taken to be entitled to exercise or control the exercise of a right...` | coa28-sch1.l4:157 | "a person is taken to be entitled to exercise or control the exercise of a right conferred by the holding of sh..." | `JUST FALSE` | `NOTHING` |
| `sch 1 para 5(2) the voting power of the other body corporate is taken to be exercisable by the pe...` | coa28-sch1.l4:189 | "For the purposes of sub-paragraph (1)(b) where— (a) a person is entitled to exercise or control the exercise o..." | `JUST FALSE` | `NOTHING` |
| `sch 1 para 5(1) the person is taken to be interested in the shares because a body corporate is in...` | coa28-sch1.l4:212 | "A person is taken to be interested in shares if a body corporate is interested in them and— (a) the body corpo..." | `JUST FALSE` | `NOTHING` |
| `sch 1 para 6(1) the beneficiary is taken to have an interest in the shares` | coa28-sch1.l4:224 | "Where an interest in shares is comprised in property held on trust, every beneficiary of the trust is taken to..." | `JUST FALSE` | `NOTHING` |
| `sch 1 para 6(2) the interest in reversion, remainder or fee is disregarded` | coa28-sch1.l4:237 | "So long as a person is entitled to receive, during the lifetime of himself or another, income from trust prope..." | `JUST FALSE` | `NOTHING` |
| `sch 1 para 6(3) the person is treated as not interested in the shares` | coa28-sch1.l4:250 | "A person is treated as not interested in shares if and so long as he holds them" | `JUST FALSE` | `NOTHING` |
| `sch 1 para 3 the person has an interest in the shares by virtue of paragraph 3` | coa28-sch1.l4:310 | "A person ceases to have an interest in shares by virtue of this paragraph" | `JUST FALSE` | `NOTHING` |
| `sch 1 para 3 the person has an interest in the shares by virtue of paragraph 3` | coa28-sch1.l4:314 | "neither sub-paragraph (1) nor (2) holds (marginal reading M1 in NOTES.md)" | `JUST FALSE` | `NOTHING` |
| `sch 1 para 6 the beneficiary has an interest in the shares by virtue of paragraph 6` | coa28-sch1.l4:332 | "an interest in the shares in reversion or remainder or (as regards Scotland) in fee shall be disregarded" | `JUST FALSE` | `NOTHING` |
| `sch 1 paras 2 to 6 the person has an interest in the shares or debentures for sections 254 and 255` | coa28-sch1.l4:346 | "A person is treated as not interested in shares if and so long as he holds them" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 11 the person is treated as holding the share or right` | coa28-sch1a.l4:57 | "If two or more persons each hold a share or right jointly, each of them is treated for the purposes of this Sc..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 12(1) the person is treated as holding the combined shares or rights of both` | coa28-sch1a.l4:68 | "If shares or rights held by a person and shares or rights held by another person are the subject of a joint ar..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 13(2)(a) the right is a holding of shares in the legal entity that does not have a sh...` | coa28-sch1a.l4:146 | "In relation to a legal entity that does not have a share capital" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 13(2)(b) the person holds more than 25% of the shares in the legal entity that does n...` | coa28-sch1a.l4:162 | "In relation to a legal entity that does not have a share capital" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 14(2)(a) the right is a right of exercising voting rights in the entity` | coa28-sch1a.l4:189 | "In relation to a legal entity that does not have general meetings at which matters are decided by the exercise..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 14(2)(b) the person exercises more than 25% of the voting rights in the entity` | coa28-sch1a.l4:203 | "In relation to a legal entity that does not have general meetings at which matters are decided by the exercise..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 17 the reference to a board of directors is read as a reference to the equivalent man...` | coa28-sch1a.l4:226 | "in the case of an entity that does not have such a board" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 18(3) A has a majority stake in B` | coa28-sch1a.l4:262 | "A has a “majority stake” in B if" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 18(1) the person holds the share indirectly` | coa28-sch1a.l4:286 | "A person holds a share “indirectly” if the person has a majority stake in a legal entity and that entity ..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 18(1) the person holds the share indirectly` | coa28-sch1a.l4:291 | "A person holds a share “indirectly” if the person has a majority stake in a legal entity and that entity— (a) ..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 18(2) the person holds the right indirectly` | coa28-sch1a.l4:305 | "A person holds a right “indirectly” if the person has a majority stake in a legal entity and that entity ..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 18(2) the person holds the right indirectly` | coa28-sch1a.l4:310 | "A person holds a right “indirectly” if the person has a majority stake in a legal entity and that entity— (a) ..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 18(4) the legal entity is treated as having the right to appoint the director` | coa28-sch1a.l4:322 | "a legal entity is to be treated as having the right to appoint a director if" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 22(2) the rights are taken into account even while the entity is in those proceedings` | coa28-sch1a.l4:411 | "rights that are exercisable by an administrator or by creditors while a legal entity is in relevant insolvency..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 23 the rights are treated as held by the person who provided the security` | coa28-sch1a.l4:445 | "(a) where apart from the right to exercise them ... the rights are exercisable only in accordance with that pe..." | `JUST FALSE` | `NOTHING` |
| `sch 1A paras 11 to 23 the block is treated as held by X` | coa28-sch1a.l4:463 | "Rights attached to shares held by way of security provided by a person are to be treated for the purposes of t..." | `JUST FALSE` | `NOTHING` |
| `sch 1A paras 11 to 23 the block is treated as held by X` | coa28-sch1a.l4:464 | "(a) where ... and (b) where ..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 24(4) the Secretary of State must take no further steps in relation to the draft` | coa28-sch1a.l4:554 | "If, within the 40-day period, either House of Parliament resolves not to approve the draft guidance" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 24(4) the Secretary of State must take no further steps in relation to the draft` | coa28-sch1a.l4:555 | "If, within the 40-day period, either House of Parliament resolves not to approve the draft guidance" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 24(5) the Secretary of State must issue and publish the guidance in the form of the d...` | coa28-sch1a.l4:567 | "If no such resolution is made within that period, the Secretary of State must issue and publish the guidance i..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 8(2) this sub-paragraph is satisfied` | coa28-sch1a.l4:783 | "This sub-paragraph is satisfied where— (a) ... and (b) ..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 8(1) V holds an interest in company W` | coa28-sch1a.l4:808 | "V holds an interest in company W if" | `JUST FALSE` | `NOTHING` |
| `sch 1A para 9(1) paragraph 9 applies` | coa28-sch1a.l4:822 | "This paragraph applies where V— (a) ... and (b) ..." | `JUST FALSE` | `NOTHING` |
| `sch 1A para 9(2) V holds the interest in company W through the legal entity` | coa28-sch1a.l4:838 | "Where this paragraph applies, V holds the interest in company W— (a) through L, and (b) through each other leg..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 1(1) paragraph 1 applies` | coa28-sch1b.l4:30 | "This paragraph applies if" | `JUST FALSE` | `NOTHING` |
| `sch 1B para 1(3) the company may issue the restrictions notice` | coa28-sch1b.l4:68 | "may issue the restrictions notice if, by the end of the period of one month beginning with the date on which t..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 1(3) the company may issue the restrictions notice` | coa28-sch1b.l4:71 | "if, by the end of the period of one month ..., (a) the person has not complied ..., and (b) the company has no..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 2(1) the person has a relevant interest in the company` | coa28-sch1b.l4:117 | "a person has a relevant interest in a company if the person— (a) holds any shares in the company, (b) holds an..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 5(1) the person commits an offence` | coa28-sch1b.l4:329 | "A person commits an offence if the person does anything listed in sub-paragraph (2) knowing that the interest ..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 5(3) the person commits an offence` | coa28-sch1b.l4:351 | "A person who has a relevant interest that the person knows to be subject to restrictions commits an offence if..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 5(4) the person commits an offence` | coa28-sch1b.l4:367 | "A person commits an offence if the person— (a) either has a relevant interest that the person knows to be subj..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 6(a) the company commits an offence` | coa28-sch1b.l4:390 | "If shares in a company are issued in contravention of a restriction imposed by virtue of a restrictions notice..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 6(b) the officer of the company commits an offence` | coa28-sch1b.l4:404 | "If shares in a company are issued in contravention of a restriction imposed by virtue of a restrictions notice..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 11 the company must by notice withdraw the restrictions notice` | coa28-sch1b.l4:602 | "A company that issues a person with a restrictions notice under paragraph 1 must by notice withdraw the restri..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 13(1) the person commits an offence by failing to comply with the notice` | coa28-sch1b.l4:636 | "A person to whom a notice under section 790D, 790DA, 790E or 790EA is addressed commits an offence if the pers..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 13(2) the officer of the entity commits an offence` | coa28-sch1b.l4:647 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 13(2) the officer of the entity commits an offence` | coa28-sch1b.l4:649 | "the offence is also committed" | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14(1) the person commits an offence by failing to comply with the duty` | coa28-sch1b.l4:680 | "A person commits an offence if the person fails, without reasonable excuse, to comply with a duty under sectio..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14(2) the officer of the entity commits an offence` | coa28-sch1b.l4:691 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14(2) the officer of the entity commits an offence` | coa28-sch1b.l4:693 | "the offence is also committed" | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14A(1) the person commits the basic offence of making a false statement` | coa28-sch1b.l4:724 | "A person commits an offence if, in purported compliance with a notice ... and without reasonable excuse, the p..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14A(2) the officer of the entity commits an offence` | coa28-sch1b.l4:735 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14A(2) the officer of the entity commits an offence` | coa28-sch1b.l4:737 | "the offence is also committed" | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14B(1) the person commits the aggravated offence of making a false statement` | coa28-sch1b.l4:764 | "A person commits an offence if, in purported compliance with a notice ..., the person makes a statement that t..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14B(2) the officer of the entity commits an offence` | coa28-sch1b.l4:775 | "Where the person is a legal entity, the offence is also committed by every officer of the entity who is in def..." | `JUST FALSE` | `NOTHING` |
| `sch 1B para 14B(2) the officer of the entity commits an offence` | coa28-sch1b.l4:777 | "the offence is also committed" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 20(2) the securities are of one class` | coa28-sch1c.l4:32 | "securities are of one class if the rights attached to them are in all respects uniform" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 1(2) the rules must protect the other holders of securities` | coa28-sch1c.l4:51 | "If a person acquires control of a company, the other holders of securities must be protected" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 2(2) the board of the offeree company must give its views on the effect of implementa...` | coa28-sch1c.l4:79 | "Where it advises the holders of securities" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 4 the creation of a false market in the securities of the company is barred` | coa28-sch1c.l4:119 | "(b) if the offeror is a company, that company" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 7(3) the obligation to make a mandatory takeover bid no longer applies` | coa28-sch1c.l4:163 | "where control has been acquired following a voluntary takeover bid to all the holders of securities for all th..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 7(1) the rules must require P to make a mandatory takeover bid` | coa28-sch1c.l4:176 | "the obligation referred to in sub-paragraph (1) to make a mandatory takeover bid no longer applies" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 7(1) the rules must require P to make a mandatory takeover bid` | coa28-sch1c.l4:179 | "Rules must ensure that a person (“P”) is required to make a takeover bid (“a mandatory takeover bid”) where— (..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 9(2) the rules must ensure that cash is offered as an alternative` | coa28-sch1c.l4:296 | "Rules must ensure that cash must be offered— (a) as an alternative where the consideration offered does not co..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 15 the rules must ensure that the takeover bid is made public so as to ensure market ...` | coa28-sch1c.l4:459 | "(b) if the offeror is a company, that company" | `JUST FALSE` | `NOTHING` |
| `sch 1C para 17(4) the body is the board of directors for paragraph 17` | coa28-sch1c.l4:563 | "where a company has a two-tier board structure, “board of directors” means both the management board and the s..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 18(3) the employees' representatives' opinion must be appended to the document` | coa28-sch1c.l4:605 | "where the board of directors of the offeree company receives in good time a separate opinion from the represen..." | `JUST FALSE` | `NOTHING` |
| `sch 1C para 20(4) the two are deemed to be acting in concert` | coa28-sch1c.l4:744 | "where a person (“A”) is a subsidiary undertaking of another person (“B”) within the meaning of section 420 ......" | `JUST FALSE` | `NOTHING` |

**M2: an "is" / "are" / "is that" / "is to" statement read as closed (18 branches).**

| Function | Site | Words | Answer taken | Other reading |
|---|---|---|---|---|
| `sch 1 para 6(5) the body is the Church of Scotland General Trustees or the Church of Scotland Trust` | coa28-sch1.l4:297 | "“The Church of Scotland General Trustees” are the body incorporated by the order confirmed by the Church of Sc..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 12(2) the arrangement is a joint arrangement` | coa28-sch1a.l4:81 | "A “joint arrangement” is an arrangement between the holders of shares (or rights) that they will exercise all ..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 13(1) the person holds more than 25% of the shares in the legal entity that has a sha...` | coa28-sch1a.l4:135 | "a reference to holding “more than 25% of the shares” in that entity is to holding shares comprised in the issu..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 13(2)(b) the person holds more than 25% of the shares in the legal entity that does n...` | coa28-sch1a.l4:167 | "a reference to holding “more than 25% of the shares” in that entity is to holding a right or rights to share i..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 14(1) the right is a voting right in the legal entity` | coa28-sch1a.l4:178 | "A reference to the voting rights in a legal entity is to the rights conferred on shareholders in respect of th..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 14(2)(b) the person exercises more than 25% of the voting rights in the entity` | coa28-sch1a.l4:206 | "a reference to exercising more than 25% of the voting rights in the entity is to be read as a reference to exe..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 16 the person has the right to appoint or remove a majority of the board of directors` | coa28-sch1a.l4:241 | "A reference to the right to appoint or remove a majority of the board of directors of a legal entity is to the..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 19 the share is treated as held by the person` | coa28-sch1a.l4:337 | "to be treated for the purposes of this Schedule as held by the other (and not by the nominee)" | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 20(2) the person controls the right` | coa28-sch1a.l4:355 | "A person “controls” a right if, by virtue of any arrangement between that person and others, the right is exer..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 3 the second condition is met` | coa28-sch1a.l4:720 | "The second condition is that X holds, directly or indirectly, more than 25% of the voting rights in company Y" | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 5 the fourth condition is met` | coa28-sch1a.l4:736 | "The fourth condition is that X has the right to exercise, or actually exercises, significant influence or cont..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 6 the fifth condition is met` | coa28-sch1a.l4:747 | "The fifth condition is that— ... (b) X has the right to exercise, or actually exercises, significant influence..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 6 the fifth condition is met` | coa28-sch1a.l4:750 | "The fifth condition is that— (a) the trustees of a trust or the members of a firm ... meet any of the other sp..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 1 at least one of the specified conditions is met by X in relation to company Y` | coa28-sch1a.l4:762 | "conditions at least one of which must be met by an individual (“X”)" | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1A para 1 at least one of the specified conditions is met by X in relation to company Y` | coa28-sch1a.l4:766 | "the conditions at least one of which must be met" | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1B para 1(4) the restrictions notice is issued on the person` | coa28-sch1b.l4:80 | "A restrictions notice is issued on a person by sending the notice to the person" | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1B para 3(6) the right is an associated right in relation to the relevant interest` | coa28-sch1b.l4:191 | "An “associated right”, in relation to a relevant interest, is— (a) a right to be issued with any shares issued..." | `JUST FALSE` outside the stated cases | `NOTHING` |
| `sch 1C para 17(2) the day is within the relevant period` | coa28-sch1c.l4:496 | "“The relevant period”— (a) begins when the board ... receives the information ..., or at such earlier stage as..." | `JUST FALSE` outside the stated cases | `NOTHING` |

**M3: an "are" / "is" scope statement with no quoted term (4 branches).**

| Function | Site | Words | Answer taken | Other reading |
|---|---|---|---|---|
| `s 1279(1) the shares are shares to which section 1277 applies` | coa28-part44.l4:261 | "The shares to which section 1277 applies are shares— (a) of a description traded on a specified market, and (b..." | `NOTHING` outside the list | `JUST FALSE` (a closed definition) |
| `s 1280(5)(b) the information is information given in aggregated form` | coa28-part44.l4:279 | "information given in aggregated form, that is— (i) ..., or (ii) ..., or (iii) ..." | `NOTHING` outside the list | `JUST FALSE` (a closed definition) |
| `s 1282(1) 176ZA(2)(b) the claim is a claim to property comprised in or subject to a floating charge` | coa28-part44.l4:429 | "the reference to claims to property comprised in or subject to a floating charge is to the claims of— (i) ... ..." | `NOTHING` outside the list | `JUST FALSE` (a closed definition) |
| `s 1282(2) 150ZA(2)(b) the claim is a claim to property comprised in or subject to a floating charge` | coa28-part44.l4:474 | "the reference to claims to property comprised in or subject to a floating charge is to the claims of— (i) ... ..." | `NOTHING` outside the list | `JUST FALSE` (a closed definition) |

**N2: a flat negative (23 branches; ruled, option A).**

| Function | Site | Words | Answer taken | Other reading |
|---|---|---|---|---|
| `s 1281 241A(1) the public authority may disclose the information to any person` | coa28-part44.l4:341 | "(2) Subsection (1) does not apply to—" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `s 1291(3) the regulations or order ceasing to have effect affects the thing` | coa28-part46.l4:171 | "The regulations or order ceasing to have effect does not affect" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `s 1292A the reference to the Bank of England includes the Bank acting as the Prudential Regulatio...` | coa28-part46.l4:229 | "references to the Bank of England do not include the Bank acting in its capacity as the Prudential Regulation ..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `s 1297(2) the repeal and re-enactment affects the continuity of the law` | coa28-part46.l4:293 | "The repeal and re-enactment does not affect the continuity of the law" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1 para 2(3) the lack of identifiability of the shares matters to the interest` | coa28-sch1.l4:62 | "It is immaterial that the shares in which a person has an interest are not identifiable" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1 para 3(3) the right or obligation is to be taken to be a right to acquire, or an obligation...` | coa28-sch1.l4:91 | "Rights or obligations to subscribe for shares are not to be taken for the purposes of sub-paragraph (2) to be ..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1 para 4(3) the person is taken by virtue of paragraph 4 to be interested in the shares by re...` | coa28-sch1.l4:170 | "A person is not by virtue of this paragraph taken to be interested in shares by reason only that— (a) he has b..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1 para 4 the person has an interest in the shares by virtue of paragraph 4` | coa28-sch1.l4:323 | "A person is not by virtue of this paragraph taken to be interested in shares by reason only that" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1A para 21(2) the thing counts as an arrangement` | coa28-sch1a.l4:104 | "something does not count as an arrangement unless there is at least some degree of stability about it" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1A para 21 the thing is an arrangement for this Schedule` | coa28-sch1a.l4:112 | "something does not count as an arrangement unless there is at least some degree of stability about it" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1A para 24(6) sub-paragraph (4) prevents a new draft of proposed guidance from being laid bef...` | coa28-sch1a.l4:584 | "Sub-paragraph (4) does not prevent a new draft of proposed guidance from being laid before Parliament" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1A para 25(1) the individual meets the specified condition by virtue only of being a limited ...` | coa28-sch1a.l4:606 | "An individual does not meet the specified condition in paragraph 2, 3 or 4 in relation to a company by virtue ..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1A para 25(2) the individual meets the specified condition by virtue only of holding shares o...` | coa28-sch1a.l4:618 | "An individual does not meet the specified condition in paragraph 2, 3 or 4 in relation to a company by virtue ..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1A para 25(3) sub-paragraphs (1) and (2) apply` | coa28-sch1a.l4:627 | "Sub-paragraphs (1) and (2) do not apply for the purposes of determining whether the requirement set out in par..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1A paras 2 to 4 and 25 the individual meets the specified condition` | coa28-sch1a.l4:680 | "An individual does not meet the specified condition in paragraph 2, 3 or 4 in relation to a company by virtue ..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1B para 3(3) sub-paragraph (2) applies to the agreement` | coa28-sch1b.l4:199 | "Sub-paragraph (2) does not apply to an agreement to transfer the interest on the making of an order under para..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1B para 3(2) the agreement to transfer the interest is void` | coa28-sch1b.l4:210 | "Sub-paragraph (2) does not apply to an agreement to transfer the interest on the making of an order under para..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1B para 3(5) sub-paragraph (4) applies to the agreement` | coa28-sch1b.l4:221 | "Sub-paragraph (4) does not apply to an agreement to transfer any such right on the making of an order under pa..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1B para 3(4) the agreement to transfer the associated right is void` | coa28-sch1b.l4:233 | "Sub-paragraph (4) does not apply to an agreement to transfer any such right on the making of an order under pa..." | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1B para 8(5)(b) sub-paragraph (3) applies to the making of the order` | coa28-sch1b.l4:483 | "sub-paragraph (3) does not apply in relation to the making of such an order" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1C para 10 the rule is barred` | coa28-sch1c.l4:309 | "must not hinder the normal course of a takeover bid" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1C para 20(1) the offer is a takeover bid` | coa28-sch1c.l4:700 | "but does not include cases where the offer is made by the company itself" | `JUST FALSE` | option C: a typed prohibition, not a plain no |
| `sch 1C para 21(3) section 1 applies for the purposes of the provision` | coa28-sch1c.l4:779 | "Section 1 (meaning of “company”) does not apply for the purposes of the listed provisions" | `JUST FALSE` | option C: a typed prohibition, not a plain no |

**(b): a prohibition or grant limited by its own wording, answered `NOTHING` outside the limit (117 branches; the "subject to any direction" sites are fork F7).**

| Function | Site | Words | Answer taken | Other reading |
|---|---|---|---|---|
| `s 1275(6) the amendments have effect in relation to the exercise of the power` | coa28-part44.l4:99 | "in relation to any exercise of the power ... after this section comes into force" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1277(4) the person may bring civil proceedings to enforce the obligation` | coa28-part44.l4:162 | "The obligation imposed by regulations under this section" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1280(6) the reference to instructions in section 1280 covers the instruction` | coa28-part44.l4:288 | "References in this section to instructions are to instructions of any description" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1281 241A(2) subsection (1) does not apply to the information` | coa28-part44.l4:311 | "Subsection (1) does not apply to— (a) ... (d)" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1281 241A(1) the public authority may disclose the information to any person` | coa28-part44.l4:343 | "A public authority which holds prescribed information to which section 237 applies" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1281 241A(1) the public authority may disclose the information to any person` | coa28-part44.l4:345 | "may disclose that information to any person— (a) for the purposes of, or in connection with, prescribed civil ..." | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1281 241A(5) the person is barred from using the information for the purpose` | coa28-part44.l4:363 | "Information disclosed under this section must not be used by the person to whom it is disclosed" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1281 241A(5) the person is barred from using the information for the purpose` | coa28-part44.l4:365 | "for any purpose other than those specified in subsection (1)" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1282(1) 176ZA(1) the expenses of winding up have priority over claims to property comprised in ...` | coa28-part44.l4:403 | "The expenses of winding up in England and Wales" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1282(1) 176ZA(4) the expense is an expense of the winding up` | coa28-part44.l4:439 | "References in this section to the expenses of the winding up are to all expenses properly incurred in the wind..." | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1282(2) 150ZA(4) the expense is an expense of the winding up` | coa28-part44.l4:484 | "References in this Article to the expenses of the winding up are to all expenses properly incurred in the wind..." | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1284(1) the provision extends to Northern Ireland` | coa28-part45.l4:21 | "The Companies Acts as defined by this Act (see section 2) extend to Northern Ireland" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1284(2) the instrument ceases to have effect` | coa28-part45.l4:36 | "shall cease to have effect accordingly" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1285(1) the enactment extends to Northern Ireland` | coa28-part45.l4:49 | "The enactments in force in Great Britain relating to UK Societas extend to Northern Ireland" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1285(2) the enactment ceases to have effect` | coa28-part45.l4:64 | "The following enactments shall cease to have effect accordingly" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1286(1) the enactments in force in Great Britain relating to the form extend to Northern Ireland` | coa28-part45.l4:101 | "The enactments in force in Great Britain relating to— (a) ... (e) extend to Northern Ireland" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1286(2) the enactment ceases to have effect` | coa28-part45.l4:121 | "The following enactments shall cease to have effect accordingly" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1287(1) the provision extends to Northern Ireland` | coa28-part45.l4:133 | "The provisions of Part 41 of this Act (business names) extend to Northern Ireland" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1287(2) the instrument ceases to have effect` | coa28-part45.l4:145 | "shall cease to have effect accordingly" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1291(2) no account is taken of the time in the interval` | coa28-part46.l4:99 | "both Houses are adjourned for more than four days" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1291(3) the regulations or order ceasing to have effect affects the thing` | coa28-part46.l4:170 | "does not affect— (a) anything previously done under them or it, or (b) the making of new regulations or a new ..." | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1292(2) the provision may be made by order` | coa28-part46.l4:182 | "Any provision that may be made by regulations under this Act may be made by order" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1292(2) the provision may be made by regulations` | coa28-part46.l4:190 | "any provision that may be made by order under this Act may be made by regulations" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1292(3) the provision may be made subject to the procedure` | coa28-part46.l4:203 | "may be made by regulations or order subject to negative or affirmative resolution procedure" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1292(3) the provision may be made subject to the procedure` | coa28-part46.l4:204 | "for which no Parliamentary procedure is prescribed" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1292(4) the provision may be made subject to affirmative resolution procedure` | coa28-part46.l4:213 | "Any provision that may be made by regulations or order under this Act subject to negative resolution procedure" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1292A the reference to the Bank of England includes the Bank acting as the Prudential Regulatio...` | coa28-part46.l4:227 | "except in section 796" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1293 the provision is an enactment` | coa28-part46.l4:255 | "unless the context otherwise requires" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(2) the repeal and re-enactment affects the continuity of the law` | coa28-part46.l4:294 | "This section applies where" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(6) section 1297 yields to a specific transitional provision or saving` | coa28-part46.l4:303 | "This section has effect subject to any specific transitional provision or saving contained in this Act" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(3) the thing has effect thereafter as if done under or for the purposes of the correspondi...` | coa28-part46.l4:319 | "This section has effect subject to any specific transitional provision or saving contained in this Act" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(3) the thing has effect thereafter as if done under or for the purposes of the correspondi...` | coa28-part46.l4:322 | "Anything done ... that could have been done under or for the purposes of the corresponding provision" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(4) the reference to the provision of this Act is construed as including a reference to the...` | coa28-part46.l4:339 | "This section has effect subject to any specific transitional provision or saving contained in this Act" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(4) the reference to the provision of this Act is construed as including a reference to the...` | coa28-part46.l4:341 | "(so far as the context permits)" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(4) the reference to the provision of this Act is construed as including a reference to the...` | coa28-part46.l4:344 | "as respects times, circumstances or purposes in relation to which the corresponding repealed provision had eff..." | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(5) the reference to the repealed provision is construed as being or including a reference ...` | coa28-part46.l4:361 | "This section has effect subject to any specific transitional provision or saving contained in this Act" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(5) the reference to the repealed provision is construed as being or including a reference ...` | coa28-part46.l4:363 | "(so far as the context permits)" | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(5) the reference to the repealed provision is construed as being or including a reference ...` | coa28-part46.l4:366 | "as respects times, circumstances and purposes in relation to which the corresponding provision of this Act has..." | `NOTHING` | `JUST FALSE` outside the limit |
| `s 1297(7) the reference to this Act includes the instrument` | coa28-part46.l4:376 | "References in this section to this Act" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 1(1) the provisions of this Schedule govern the reference` | coa28-sch1.l4:20 | "for the interpretation of references in sections 254 and 255" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 1(2) the provisions of this Schedule apply to the security` | coa28-sch1.l4:33 | "apply to debentures as they apply to shares" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 2(2) the restraint or restriction is disregarded` | coa28-sch1.l4:54 | "Any restraints or restrictions to which the exercise of any right attached to the interest is or may be subjec..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 2(4) the person is deemed to have the interest` | coa28-sch1.l4:72 | "Persons having a joint interest in shares are deemed each of them to have that interest" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 3(3) the right or obligation is to be taken to be a right to acquire, or an obligation...` | coa28-sch1.l4:92 | "the sub-paragraph speaks only of rights and obligations to subscribe" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 3(4) the person ceases to have an interest in the shares by virtue of paragraph 3` | coa28-sch1.l4:128 | "A person ceases to have an interest in shares by virtue of this paragraph" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 4(3) the person is taken by virtue of paragraph 4 to be interested in the shares by re...` | coa28-sch1.l4:171 | "by reason only that" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1 para 6(2) the interest in reversion, remainder or fee is disregarded` | coa28-sch1.l4:234 | "an interest in the shares in reversion or remainder or (as regards Scotland) in fee" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 21(2) the thing counts as an arrangement` | coa28-sch1a.l4:103 | "the sub-paragraph says what does not count, not what does" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 13(2)(a) the right is a holding of shares in the legal entity that does not have a sh...` | coa28-sch1a.l4:149 | "a reference to holding shares in that entity is to holding a right to share in the capital or, as the case may..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 14(2)(a) the right is a right of exercising voting rights in the entity` | coa28-sch1a.l4:192 | "to be read as a reference to exercising rights in relation to the entity that are equivalent to those of a per..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 19 the share is treated as held by the person` | coa28-sch1a.l4:334 | "A share held by a person as nominee for another" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 20(1) the right is treated as held by the person` | coa28-sch1a.l4:369 | "Where a person controls a right" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 22(1) the rights are taken into account` | coa28-sch1a.l4:400 | "Rights that are exercisable only in certain circumstances" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 22(2) the rights are taken into account even while the entity is in those proceedings` | coa28-sch1a.l4:412 | "rights that are exercisable by an administrator or by creditors" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 22(4) the rights continue to be taken into account` | coa28-sch1a.l4:421 | "Rights that are normally exercisable but are temporarily incapable of exercise" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 23 the rights are treated as held by the person who provided the security` | coa28-sch1a.l4:440 | "Rights attached to shares held by way of security provided by a person" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A paras 11 to 23 the block is treated as held by X` | coa28-sch1a.l4:465 | "this constructor does not say whether X provided the security or holds it; paragraph 23 answers JUST FALSE onl..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 24(2) regard must be had to the guidance` | coa28-sch1a.l4:507 | "in interpreting references in this Schedule to “significant influence or control”" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 24(5) the Secretary of State must issue and publish the guidance in the form of the d...` | coa28-sch1a.l4:570 | "If no such resolution is made within that period" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 25(1) the individual meets the specified condition by virtue only of being a limited ...` | coa28-sch1a.l4:607 | "by virtue only of being a limited partner" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 25(2) the individual meets the specified condition by virtue only of holding shares o...` | coa28-sch1a.l4:619 | "by virtue only of, directly or indirectly" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 25(3) sub-paragraphs (1) and (2) apply` | coa28-sch1a.l4:628 | "the sub-paragraph says only where (1) and (2) do not apply" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1A para 9(2) V holds the interest in company W through the legal entity` | coa28-sch1a.l4:842 | "through L, and through each other legal entity in the chain mentioned in sub-paragraph (1)(b)(ii)" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 1(2) the company may give the person a warning notice` | coa28-sch1b.l4:39 | "The company may give the person a notice" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 2(2) the thing is the relevant interest` | coa28-sch1b.l4:126 | "References to “the relevant interest” are to the shares or right in question" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 2(3) the person is regarded as having the relevant interest` | coa28-sch1b.l4:136 | "where the relevant interest is by virtue of paragraph 19 or 20 of that Schedule treated ... as held by a perso..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 3(7) the provisions of paragraph 3 are subject to the direction` | coa28-sch1b.l4:149 | "subject to any directions given under paragraph 4" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 3(1) the effect of the restrictions notice applies to the act` | coa28-sch1b.l4:172 | "The effect of a restrictions notice issued under paragraph 1 with respect to a relevant interest is as follows" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 3(1) the effect of the restrictions notice applies to the act` | coa28-sch1b.l4:176 | "The provisions of this section are subject to any directions given under paragraph 4" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 3(3) sub-paragraph (2) applies to the agreement` | coa28-sch1b.l4:200 | "the sub-paragraph says only where (2) does not apply" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 3(2) the agreement to transfer the interest is void` | coa28-sch1b.l4:213 | "An agreement to transfer an interest that is subject to the restriction in sub-paragraph (1)(a)" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 3(5) sub-paragraph (4) applies to the agreement` | coa28-sch1b.l4:222 | "the sub-paragraph says only where (4) does not apply" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 3(4) the agreement to transfer the associated right is void` | coa28-sch1b.l4:238 | "An agreement to transfer any associated right" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 4(1) the court may give a direction` | coa28-sch1b.l4:252 | "The court may give a direction under this paragraph if, on application by any person aggrieved, the court is s..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 4(3) the act does not constitute a breach of the restrictions placed on the relevant ...` | coa28-sch1b.l4:261 | "a direction that certain acts will not constitute a breach of the restrictions" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 4(4)(b) the order may confine the direction to cases where the acts are done by perso...` | coa28-sch1b.l4:281 | "may confine the direction to cases where those acts are done by persons, or for purposes, described in the ord..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 4(5) the direction may be given subject to the terms` | coa28-sch1b.l4:290 | "subject to such terms as the court thinks fit" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 7(2) the provisions of paragraphs 5 and 6 are subject to the direction` | coa28-sch1b.l4:303 | "subject to any direction given under paragraph 4 or 8" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 5(1) the person commits an offence` | coa28-sch1b.l4:324 | "The provisions of those paragraphs are subject to any direction given under paragraph 4 or 8" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 5(3) the person commits an offence` | coa28-sch1b.l4:345 | "The provisions of those paragraphs are subject to any direction given under paragraph 4 or 8" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 5(4) the person commits an offence` | coa28-sch1b.l4:364 | "The provisions of those paragraphs are subject to any direction given under paragraph 4 or 8" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 5(5) the interest is subject to restrictions` | coa28-sch1b.l4:376 | "References in this Schedule to an interest being “subject to restrictions” are to an interest being subject to..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 6(a) the company commits an offence` | coa28-sch1b.l4:387 | "The provisions of those paragraphs are subject to any direction given under paragraph 4 or 8" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 6(b) the officer of the company commits an offence` | coa28-sch1b.l4:402 | "The provisions of those paragraphs are subject to any direction given under paragraph 4 or 8" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 7(1) the penalty for an offence under paragraph 5 or 6` | coa28-sch1b.l4:423 | "the paragraph distinguishes England and Wales from Scotland and Northern Ireland on summary conviction" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 8(2) the person may apply for an order under paragraph 8` | coa28-sch1b.l4:438 | "may be made by the company in question or by any person aggrieved" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 8(4) the order may continue the restriction` | coa28-sch1b.l4:464 | "may continue, in whole or in part, the restrictions mentioned in paragraph 3(1)(c) and (d) so far as they rela..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 8(5)(a) an application may be made for an order directing that the relevant interest ...` | coa28-sch1b.l4:474 | "Where any restrictions continue in force under sub-paragraph (4)" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 8(5)(b) sub-paragraph (3) applies to the making of the order` | coa28-sch1b.l4:484 | "Where any restrictions continue in force under sub-paragraph (4)" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 9(1) the court may order that the relevant interest be sold subject to the court's ap...` | coa28-sch1b.l4:497 | "the relevant interest subject to restrictions" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 9(3) the court may make such further order relating to the sale or transfer of the in...` | coa28-sch1b.l4:515 | "If the court makes an order under this paragraph, it may make such further order" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 9(5) the court may order that the applicant's costs be paid out of the proceeds of sale` | coa28-sch1b.l4:538 | "On making an order under sub-paragraph (1) or (3)" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 10(2) the person may apply to the court for the whole or part of the proceeds to be p...` | coa28-sch1b.l4:556 | "A person who is beneficially interested in the relevant interest may apply" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 10(4) the applicant is entitled to payment of those costs out of the proceeds before ...` | coa28-sch1b.l4:582 | "If the court has ordered under paragraph 9 that the costs ... of an applicant under that paragraph are to be p..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 13(3) the penalty for an offence under paragraph 13` | coa28-sch1b.l4:670 | "the paragraph distinguishes England and Wales, Scotland and Northern Ireland on summary conviction" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 14(3) the penalty for an offence under paragraph 14` | coa28-sch1b.l4:714 | "the paragraph distinguishes England and Wales, Scotland and Northern Ireland on summary conviction" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 14A(3) the penalty for an offence under paragraph 14A` | coa28-sch1b.l4:754 | "the paragraph gives a penalty "on summary conviction" only" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 14A(3) the penalty for an offence under paragraph 14A` | coa28-sch1b.l4:755 | "the paragraph distinguishes England and Wales, Scotland and Northern Ireland" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1B para 14B(3) the penalty for an offence under paragraph 14B` | coa28-sch1b.l4:798 | "the paragraph distinguishes England and Wales, Scotland and Northern Ireland on summary conviction" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 1(1) the rules must afford the holders equivalent treatment` | coa28-sch1c.l4:42 | "All holders of the securities of an offeree company of the same class" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 2(1) the holders must have sufficient time and information to reach a properly inform...` | coa28-sch1c.l4:60 | "The holders of the securities of an offeree company" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 3 the board of the offeree company complies with the principle` | coa28-sch1c.l4:93 | "The board of directors of an offeree company" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 4 the creation of a false market in the securities of the company is barred` | coa28-sch1c.l4:117 | "False markets must not be created in the securities of— (a) the offeree company, (b) ..., or (c) any other com..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 4 the creation of a false market in the securities of the company is barred` | coa28-sch1c.l4:122 | "in such a way that the rise or fall of the prices of the securities becomes artificial and the normal function..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 6 the hindrance of the offeree company is barred` | coa28-sch1c.l4:148 | "for longer than is reasonable" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 7(2) the mandatory takeover bid meets the requirement the rules must ensure` | coa28-sch1c.l4:191 | "the mandatory takeover bid must be addressed" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 8(1) the equitable price` | coa28-sch1c.l4:222 | "over a period, determined by rules, of not less than 6 and not more than 12 months" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 10 the rule is barred` | coa28-sch1c.l4:306 | "Any rules that make provision to protect the interests of the holders of securities that goes beyond the provi..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 11(3) the boards of the offeree company and of the offeror must inform` | coa28-sch1c.l4:333 | "as soon as the takeover bid has been made public" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 12(3) the boards of the offeree company and of the offeror must communicate the offer...` | coa28-sch1c.l4:366 | "when the offer document is made public" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 13(1) the time allowed for acceptance is within the limits the rules must ensure` | coa28-sch1c.l4:430 | "subject to any provision made in accordance with paragraph 14" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 15 the rules must ensure that the takeover bid is made public so as to ensure market ...` | coa28-sch1c.l4:461 | "the securities of— (a) the offeree company, (b) ..., or (c) any other company affected by the takeover bid" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 17(1) the rules must require the board to obtain the prior authorisation of a general...` | coa28-sch1c.l4:531 | "any action ... which may result in the frustration of the bid" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 18(2) the board must at the same time communicate its opinion to` | coa28-sch1c.l4:593 | "at the same time communicate that opinion" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 20(4) the two are deemed to be acting in concert` | coa28-sch1c.l4:748 | "(a) A is deemed to be acting in concert with B and with any other subsidiary undertakings of B, and (b) B and ..." | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 21(3) section 1 applies for the purposes of the provision` | coa28-sch1c.l4:780 | "the sub-paragraph says only that section 1 does not apply to the listed provisions" | `NOTHING` | `JUST FALSE` outside the limit |
| `sch 1C para 21(1) the body is a company for this Schedule` | coa28-sch1c.l4:789 | "other than in the listed provisions" | `NOTHING` | `JUST FALSE` outside the limit |

Branches not listed above because they are not marginal: 25 "means" or delegated definitions, 28 branches ("unless", "except", bare "must", stated periods) that Part C of the fork register and forks F1 to F12 already cover, 3 where the text says "only", and every `NOTHING` that is silent, points outside the text, list not closed, includes or undefined term.

### Reading a result: FALSE and NOTHING (coa28)

Every decision function in this range answers `JUST TRUE`, `JUST FALSE` or `NOTHING` (a `MAYBE BOOLEAN`), or a `MAYBE NUMBER`, `MAYBE DATE` or `MAYBE Penalty` where the answer is an amount, a day or a penalty.
`JUST FALSE` is a "no" the text says in its own words.
In this subject that means: a definition that says "means" and whose case is outside it; a condition the text introduces with "if", "only if", "unless", "except", "where", "as long as" and whose condition fails; a list closed with "only"; or a flat negative ("does not", "must not", "shall not", "is not entitled").
It is never a guess that the thing is permitted or not required.
`NOTHING` is "not covered".
In this subject it means: the text lists without closing the list; the text says "includes" or "is to" and leaves the rest open; the term is undefined (the borrowed terms of other Acts are inputs); the text is silent (it says what does not count, not what does); the answer is in a regulation, a rule, a rate, a figure or a provision outside the sources (the Takeover Code; the general limit on a magistrates' court's imprisonment; the regulations under s 1277); or the text limits its own grant or prohibition ("subject to any direction", "by virtue only of") and the case falls outside the limit.
A caller must never turn `NOTHING` into `FALSE`.
Where a cross-part seam answers `NOTHING` (`s 2(1)`, `s 1121`, `sch 1B para 1`'s and `para 9`'s "applies", `s 1297(1)`'s "applies", the borrowed FSMA, EU and Interpretation Act terms), the function has an explicit arm that answers `NOTHING`; this was checked by reading every place in the eight modules that compares a `MAYBE` with `EQUALS JUST TRUE`, `EQUALS JUST FALSE`, `EQUALS NOTHING` or `WHEN NOTHING`.
Three other places read a `NOTHING` as something else, on purpose, and they are recorded here so that nobody finds them by surprise (finding 13 lists them):

- **Exception sub-paragraphs.**
  A "subject to", "does not apply to" or "unless" sub-paragraph is its own function; it answers `JUST TRUE` (or `JUST FALSE`) when its own words decide and `NOTHING` otherwise, and the function that takes its answer reads that `NOTHING` as "the exception does not apply" (E1 option B, by hand).
- **`MAYBE DATE` inputs.**
  `NOTHING` means "no such event" (no approval, no resolution, no earlier stage, no end of the relevant period), and the day-counting functions read it that way.
- **Fork F1.**
  The day-counting helper reads an adjournment of four days or fewer as a time that counts.

What a person can read off an answer in this range:

- Offences (sch 1B paras 5, 6, 13, 14, 14A, 14B): `JUST TRUE` means the text makes the conduct an offence on those facts; `JUST FALSE` means the text's own conditions (knowledge, reasonable excuse, an entity's offence, an officer in default) are not met; `NOTHING` means the facts left something open (a direction covers the act, whether an officer is in default under s 1121, a thing not on the list).
- Penalties (sch 1B paras 7, 13(3), 14(3), 14A(3), 14B(3)): the answer is the `Penalty` record of the core; `NOTHING` means the paragraph gives no penalty for that mode of conviction, or leaves a figure (the general limit in England and Wales) to a provision outside the sources.
- The Schedule 1C paragraphs say what the Takeover Panel's rules must require; they say nothing about what a particular bid does, so a `JUST TRUE` there means "the rules must require this", and the Takeover Code itself is outside the sources.
- The conditions of Schedule 1A (significant control) answer whether a condition is met on the counts and facts given; a block of shares or votes the person marks as "held in some other way" makes the count `NOTHING` unless the other blocks already decide the answer at the lower or at the upper bound.

## Seams (coa28)

A seam is a provision of another part whose answer a provision of mine needs.
`PLAN.md` section 4 says to take such an answer as an input named `s <answering section> <the question that section answers>`, of type `MAYBE BOOLEAN` by default, and to use a plain `BOOLEAN` only for a fact a witness can state.
The brief says layer 1 imports the keel's modules; where the two differ the brief governs.
I imported `coa-core.l4` only where a core type is used (`Party`, `Penalty`, `Fine limit`, `Period`, `Mode of conviction`), and took every other part's answer as an input, so that the lead can wire the answering part's function to it at the merge.
The tests wire the keel's own `s 2(1)` through `coa-definitions.l4` in `coa28-tests-part45-47.l4` (the one seam the keel answers).

### Seam inputs taken as named `MAYBE BOOLEAN` inputs (PLAN section 4 form)

| input (as written in layer 1) | taken in | answered by (per PLAN) |
|---|---|---|
| `s 2(1) the provision is one of the Companies Acts` | `s 1284(1)` in `coa28-part45.l4` | the keel (`coa-definitions.l4`) |
| `s 1121 the officer is in default` | `sch 1B para 6(b)`, `13(2)`, `14(2)`, `14A(2)`, `14B(2)` in `coa28-sch1b.l4` | the part that holds s 1121 (liability of officer in default) |

### Seam inputs that depart from the PLAN section 4 name form (names the lead may rewire)

These are plain or `MAYBE` inputs named for the question in the Act's own words, not `s <section> ...`, because the answering section is outside the Act (the Financial Services and Markets Act 2000, the Enterprise Act 2002, the 2004 Act) or is a term PLAN lists only as an implicit seam.
The lead may rename them to the form of section 4 when it wires them.

| input | taken in | the section PLAN names, or why none |
|---|---|---|
| `they are transferable securities` (`MAYBE BOOLEAN`) | `sch 1C para 20(1)` definition of "securities" | "transferable securities" is a term of the FSMA; no part of this Act defines it |
| `the body has securities admitted to trading on a UK regulated market` (`BOOLEAN`); `the consideration offered does not consist of liquid securities admitted to trading on a UK regulated market` (`BOOLEAN`) | `sch 1C para 21(1)`; `sch 1C para 9(2)` | "UK regulated market" and "regulated market": s 1173 [keel] |
| `A is a member of B and has the right to appoint or remove a majority of the board of directors of B`; `A is a member of B and controls alone ...` (`BOOLEAN`) | `sch 1A para 18(3)(b)`, `(c)` | "member": s 112 [coa3] |
| `the board is the board of directors of an offeree company` (`BOOLEAN`) | `sch 1C para 3` and the board paragraphs | "director": s 250 [coa5] |
| `A is a subsidiary undertaking of B within the meaning of section 420 of the Financial Services and Markets Act 2000 ...` (`MAYBE BOOLEAN`) | `sch 1C para 20(4)` | "subsidiary": s 1159 [keel]; the text borrows the FSMA's s 420, not s 1159 |
| `the provision is one of the listed provisions` (`MAYBE BOOLEAN`) | `sch 1C para 21(1)` | the Schedule's own list (para 21(2)); the function `sch 1C para 21(2) the provision is one of the listed provisions` answers it |

### Implicit seams PLAN lists for coa28, one by one

| term (PLAN) | how I took it |
|---|---|
| court (s 1156 [coa25]) | not asked. The court's judgments are plain inputs (`the court is satisfied that ...`, `the court has given a direction under paragraph 4`); no regulative rule in this range names the court as a party |
| interest in shares (s 820 [coa18]) | Schedule 1 is the Act's own definition for ss 254 and 255 and is encoded in `coa28-sch1.l4`; s 820's use of the phrase is another part's |
| share (s 540 [coa13]) | not asked; shares are counted as numbers (nominal value or percent of capital) in Schedule 1A |
| transfer (s 1163 [keel]) | not asked; a transfer is a constructor of `sch 1B para 3(1) act` |
| body corporate (s 1173 [keel]) | plain `BOOLEAN` facts (`a body corporate is interested in the shares`); the keel's `s 1173(1)` answer is `NOTHING` for a UK company, which a witness fact avoids |
| prescribed (s 1167 [keel]) | plain `BOOLEAN` (`it is prescribed by order of the Secretary of State`); prescribed characteristics are inputs (`the individual has the characteristics prescribed by regulations`) |
| officer (s 1173 [keel]) | `s 1121 the officer is in default` (above), the question the text asks |
| firm (s 1173 [keel]) | plain `BOOLEAN` (`the members of a firm that is not a legal person`) |
| member (s 112 [coa3]) | plain `BOOLEAN`, see the table above |
| regulated market, UK regulated market (s 1173 [keel]) | plain `BOOLEAN`, see the table above |
| subsidiary (s 1159 [keel]) | the FSMA s 420 input above; s 1159 is not asked |
| share capital (s 545 [coa13]) | plain `BOOLEAN` (`the entity has a share capital`) |
| Companies Acts (s 2 [keel]) | `s 2(1) the provision is one of the Companies Acts`, wired through the keel in the tests |
| acquisition (s 1163 [keel]) | plain `BOOLEAN` facts about acquiring securities |
| articles (s 18 [coa1]) | plain `BOOLEAN` (`a commonhold association alters its memorandum or articles`) |
| director (s 250 [coa5]) | plain `BOOLEAN`, see the table above |

### Explicit seams PLAN lists, and a seam the plan lacks

PLAN lists `s 1275: s 17 [coa1]`, `s 1281: s 241 [coa5]`, `s 241A: Part 3 [coa1], Part 4 [coa1], s 174 [coa4], s 237 [coa5]`.
The text shows these are citations of other Acts: s 17 is of the Companies (Audit, Investigations and Community Enterprise) Act 2004 (18373-18374), and in the inserted s 241A, "this Act" is the Enterprise Act 2002, so Parts 3 and 4, s 174 and s 237 are its own sections (18461, 18468).
They are not seams to coa1, coa4 or coa5; the encoding names them "of the Enterprise Act 2002" and takes the facts as inputs.
The seams that do reach another part are the ones listed above, plus the cross-references to ss 254 and 255 (answered here, by Schedule 1), s 790C (Schedule 1A feeds it), ss 790D to 790HA (Schedule 1B's notices and duties, taken as plain facts: a notice under one of those sections is addressed to the person) and s 943 (Schedule 1C's rules, which the Panel makes under it).
The remaining PLAN seams (s 796 in s 1292A; Schedules 15 and 16 and Part 43 in ss 1295 and 1300) sit in inert rows or are an input (`the reference is in section 796`).

## Findings: what the text turns out to say (coa28)

Each finding names the lines of `inputs/ukpga-2006-46.txt` it rests on and how I checked it.

1. **"This section" inside a Schedule paragraph.**
   Sch 1A para 24(7) (line 18781) says "In this section “the 40-day period” ... means", and sch 1B para 3(7) (line 18843) says "The provisions of this section are subject to any directions given under paragraph 4".
   Both stand inside a Schedule paragraph, not a section.
   I read "this section" as "this paragraph" in both; the text does not say so.
   Checked by reading the two lines.
2. **The "listed provisions" of sch 1C para 21 have no meaning of "company" at all.**
   Sch 1C para 21(1) gives "company" a meaning "other than in the listed provisions" (a company with securities admitted to trading on a UK regulated market), and para 21(3) says section 1 (meaning of "company") does not apply for the listed provisions (paras 4(b) and (c), 12(4)(b), (l) and (p), 15(b) and (c), lines 19077-19081).
   Neither gives the word a meaning there, so `sch 1C para 21(1) the body is a company for this Schedule` answers `NOTHING` for a listed provision (`NOTHING-kind (limited by its own wording)`; the other reading is that any company will do).
   Checked by reading lines 19076-19081 and by the tests of the function.
3. **Two places show dots where words were removed.**
   S 1278(1)(f) (line 18421) is a row of dots, and s 1286(1)(c) (line 18519) ends "open-ended investment companies, ..." and the text does not say what the dots stand for.
   I filed the first under reason 3 and encoded the second as printed.
   Checked by grep for dots in the range.
4. **Converter artefacts in the rendering.**
   The heading of Part 2 of Schedule 1C is rendered "PART2" (line 18966, no space), and nine lines of inserted text end in two full stops (18362, 18378, 18380, 18382, 18389, 18395, 18475, 18489, 18501).
   I read the second stop as the converter's, not the Act's, and quoted the lines as they are (`-- src:` quotes are copied by script).
   Checked by grep.
5. **PLAN's seam list mistakes other Acts' sections for this Act's.**
   See the Seams section: s 17 of the 2004 Act, s 241, s 237, s 174 and Parts 3 and 4 of the Enterprise Act 2002 are not sections of this Act.
6. **The 28-day and 40-day periods share one counting rule.**
   Section 1291(2) says no account is taken of any time during which Parliament is dissolved or prorogued or both Houses are adjourned for more than four days; sch 1A para 24(8) says the same of the 40-day period of para 24(7), with "more than 4 days" in figures.
   One helper (`s 1291(2) the day on which the last of the days to count falls`) serves both, with the forks F1 and F2 recorded.
   Checked by the tests on both sides of each end day.
7. **Sch 1A paras 2 to 4 count the same blocks in different units.**
   "More than 25% of the shares" is a nominal-value count for a company with a share capital (para 13(1), line 18716) and a share of capital or profits for one without (para 13(2)); the votes of para 3 are reduced by votes the entity holds itself (para 15, line 18725); the board test of para 4 is a majority of the votes at board meetings (para 16, line 18727).
   The encoding takes the whole (nominal value of the issued capital, total votes, total board votes) as an input and tests both sides of 25% and of one half.
8. **Joint holders and nominees are counted in full.**
   Para 11 treats each of two or more joint holders as holding the whole share (line 18710); para 19 treats a share a nominee holds as held by the other person "and not by the nominee" (line 18749).
   The two functions count a joint block in full for each holder and exclude a nominee block from the nominee, and the tests say so.
9. **Sch 1B has an offence by the entity, an offence by the officer, and one penalty table per paragraph.**
   Paragraphs 13(2), 14(2), 14A(2) and 14B(2) extend each offence to "every officer of" a legal entity; the officer's offence depends on `s 1121 the officer is in default`, which this range does not define.
   The penalties differ by place of conviction: a fine without a stated limit on indictment (para 7(1)(a)) and in England and Wales (7(1)(b)(i)); a fine "not exceeding the statutory maximum" in Scotland and Northern Ireland (7(1)(b)(ii)); imprisonment "not exceeding the general limit in a magistrates' court in England and Wales" (13(3)(b)(i)), a figure the Act leaves to another provision, so it is an input.
10. **Sch 1B para 8(3) is a bar with an alternative.**
    The court must not make an order unless it is satisfied that the information was disclosed and no unfair advantage accrued, or the transfer is for valuable consideration and the court approves (lines 18878-18880); para 8(4) lets an order made on the second ground continue the restrictions of para 3(1)(c) and (d) for a right acquired or offer made before the transfer.
    Encoded as a bar function (`JUST TRUE` while barred).
11. **Sch 1C says what rules must require; it does not bind an offeror directly.**
    Every paragraph from 1 to 19 is "Rules must ensure ..." or "Rules may ...".
    A `JUST TRUE` from a Schedule 1C function means the Panel's rules must require the thing; the Takeover Code itself is outside the sources, so no function says that a particular bid broke a rule.
12. **A defined list is not always a closed list.**
    "The listed provisions are—" (sch 1C para 21(2)) hands a definition to a list, so a provision not on it answers `JUST FALSE` (the delegated-definitions ruling); "anything listed in sub-paragraph (2)" (sch 1B para 5(1)) hands an offence to a list, and I answered `NOTHING` for another thing (Part C of the fork register, "listed in Schedule N").
13. **`NOTHING` has two jobs in the modules, and one of them is silent.**
    A `NOTHING` that arrives from another part's seam (`s 2(1)`, `s 1121`, the borrowed terms) always comes out as `NOTHING`: that failure is loud, in the sense that the answer says it is not covered.
    A `NOTHING` that arrives from an exception sub-paragraph of the same range is read as "the exception does not apply", and a `NOTHING` in a `MAYBE DATE` is read as "no such event"; both return a `JUST TRUE` or `JUST FALSE` with exit code 0, so a caller that wires some other `NOTHING` into one of these inputs gets an answer that does not say it is not covered.
    The exception inputs are: `sch 1B para 3(3)` into `3(2)`; `3(5)` into `3(4)`; `3(7)` into `3(1)`; `7(2)` into `5(1)`, `5(3)`, `5(4)`, `6(a)` and `6(b)`; `sch 1 para 4(3)` into `4`, `6(2)` into `6`, and `3(4)` into the `3` gathering; `sch 1A para 21(2)` into `21`; `25(1)` and `25(2)` into the `2 to 4 and 25` gathering; `sch 1C para 7(3)` into `7(1)`; `s 1281 241A(2)` into `241A(1)`; `s 1297(6)` into `1297(3)`, `(4)` and `(5)`.
    The `MAYBE DATE` inputs are: the approval day in `s 1291(1)(b)`; the resolution day in `sch 1A para 24(4)` and `(5)`; the earlier stage and the end of the relevant period in `sch 1C para 17(2)`.
    The seat layer cannot reach any of them with a `NOTHING` from outside, because it asks every such fact as a plain yes or no and calls the exception function itself.
    Checked by reading every `EQUALS JUST TRUE`, `EQUALS JUST FALSE`, `EQUALS NOTHING` and `WHEN NOTHING` in the eight modules (67 lines) and, for each exception function, its `NOTHING` arm.
14. **A seat case caught a bug in layer 1, and its other failure was a test error.**
    The seat case written from the text, "30 per cent of the capital of an entity with no share capital is more than 25 per cent" (`30 0 0 0 0 0 0 0 100`), failed: `sch 1A para 2 the first condition is met` compared the per-cent amount with the threshold without dividing by the whole.
    The fix divides both the amount counted and the further amount that might be counted by `the whole` in the branch for an entity with no share capital (`sch 1A para 13(2)(b)`), and `coa28-tests-sch1a.l4` now pins it with three tests (30 of 100 is more than 25%; 25 of 100 is not; 25 with a further 1 might be, so `NOTHING`).
    The other failure, the expectation that `Under schedule 1 paragraph 3` answers `NOTHING` when neither route holds, was a test error and not a bug: the layer-1 gathering answers `JUST FALSE` there under the failed-"if" reading (marginal reading M1), and the case now says so.

## What the stable binary does not accept (coa28)

Measured on `l4-main-110` (1.6.110) and, where noted, on `l4-main-109` (1.6.109), by running the file or a one-file probe in `work/` (not shipped).
Where the brief or the skills state something I did not re-measure, it is marked "stated, not re-measured".

**Measured, silent (exit code 0, a wrong answer):**

- **`NOT (a) AND b` and `NOT (a) OR NOT (b)` on one line read as `NOT` over everything to the right.**
  Probe `work/p1/probe2.l4`: `p1 = NOT (a) AND b` with a=F, b=F answers TRUE (it should be FALSE); `p2 = NOT (a) OR NOT (b)` with a=T, b=F answers FALSE and with a=F, b=F answers FALSE (both should be TRUE).
  The same expression with `NOT (a)` and `AND b` on separate lines (`p3`) reads correctly: a=F, b=F answers FALSE, a=F, b=T answers TRUE.
  Identical on 1.6.109 and 1.6.110.
  Write `(NOT (a)) OR (NOT (b))`, or put `NOT` and `AND` on separate lines.
  It bit me once: a failing test on `s 1281 241A(5)` exposed it, and I rewrote the line.
  The control is a scan of every template for a single-line `NOT (...)` followed by `AND` or `OR` on the same line: one instance (part 44, fixed); the multi-line instance in `sch 1 para 4(1)` reads correctly and has a discriminating test row so a future edit that flattens it fails.

**Measured, loud (an error that teaches):**

- **A chain of `IF ... ELSE IF ... ELSE` laid out over several lines was rejected with an indentation (layout) error; `BRANCH` with `IF ... THEN` arms and an `OTHERWISE` arm is accepted** and is used for every chain in this encoding.
- **A record built with `OF` needs commas between the fields.**
  `Penalty OF a b c d e` gives an argument-count error; `Penalty OF a, b, c, d, e` is accepted.
- **A list literal whose elements are function applications, written one per line without commas or parentheses, gave `check/wrong-argument-count`.**
  The seat's `LIST` of five `coa28 seat the answer as a MAYBE BOOLEAN x` calls was accepted once each element was parenthesised and the elements were separated by commas.

**A `DEONTIC` cannot be compared in an `#ASSERT`.**
A regulative value cannot be asserted equal to an outcome on the stable builds (stated by the brief; I used `#TRACE` and did not look for another form); the outcome is read from the `#TRACE` output.
There are three regulative rules in this range (`sch 1B para 1(6)`, `sch 1B para 11`, `s 1281 241A(5)`), each with two `#TRACE` runs.
For the two `MUST` rules, a trace with no event prints the rule itself as its residual (`PARTY Company MUST ... HENCE FULFILLED`: the duty stands) and a trace in which the company does the action prints `FULFILLED`.
For the `SHANT` rule, a trace with no event prints `MUST NOT ... HENCE FULFILLED` (the prohibition stands) and a trace in which the recipient uses the information for another purpose prints `DEONTIC BREACHED`.
The six outcomes were read by eye and are the same on 1.6.109 and 1.6.110.
Each duty is also encoded as a decision function over the facts, and the function is asserted: `check.sh` does not see a different `#TRACE` outcome, so these six are the ones to read by hand after any change.

**Stated by the brief, not re-measured:** no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE` (other than `LEST BREACH ... BECAUSE`); no `YMD` of my own (I use `Date d m y`); each `#ASSERT` on one line; `IMPORT` finds only modules in the importing file's folder (the probe that imports all eight layer-1 modules at once, and the seat files, work because every file is in one folder); `TYPICALLY` on a record field is not accepted; `WAIT UNTIL` is `WAITUNTIL`.

## Decisions (coa28)

Choices I made that the text does not make, each with the text or the brief that licenses it.
Where I chose and the choice is a user-visible answer, it is also in the fork register or the marginal readings; these are the rest.

- **Decision functions first; three regulative rules.**
  The brief asks for a regulative rule where a provision puts a duty, permission or prohibition on a named party.
  I wrote three: `sch 1B para 1(6)` (the company MUST have regard to third parties' rights), `sch 1B para 11` (the company MUST withdraw the restrictions notice) and `s 1281 241A(5)` (the recipient SHANT use the information for another purpose).
  Each has no time limit and no consequence because the text gives none; nothing is invented.
  Every other duty in the range is a decision function by choice: the duties on officials (the Secretary of State and the Treasury in ss 1277 to 1280, 1288, 1291 and sch 1A para 24; the court in sch 1B paras 4(4), 10), and the second-order duties of Schedule 1C ("Rules must ensure that ..."), whose first-order bearer (the offeror, the board) is named only through the rules the Panel makes.
  A decision function says what the text requires and whether the facts meet it; a rule would add a `PARTY` and an action the text does not name.
- **A "must ... unless" is a bar function.**
  `s 1290`, `sch 1B para 8(3)` and `sch 1C para 5` answer `JUST TRUE` while the bar holds and `JUST FALSE` once the "unless" or "only after" is met, and never claim that the thing has been done (the "until" ruling, (d)).
- **Gathering by hand (E1 option B).**
  `sch 1 paras 2 to 6 the person has an interest in the shares or debentures for sections 254 and 255` and `sch 1A paras 2 to 4 and 25 the individual meets the specified condition` take the routes (and the exclusions) as `LIST OF MAYBE BOOLEAN` and decide `JUST TRUE` if a route holds, `JUST FALSE` if an exclusion holds, `NOTHING` otherwise.
  No other section's routes are gathered.
- **Amounts, rates and thresholds the text leaves outside the Act are inputs.**
  The general limit on a magistrates' court's imprisonment (sch 1B para 13(3)(b)(i)), the period the rules determine for the equitable price (sch 1C para 8(1)), and the prescribed characteristics of a foreign limited partner (sch 1A para 25(5)(b)): each is a number or a fact the person states, asked with an `@desc`.
- **Dates are `Date d m y`, and a period is a function with a test on both sides of its end day**: the 28 days of s 1291, the 40 days of sch 1A para 24, the month of sch 1B para 1(3), the two and ten weeks of sch 1C para 13(1), the six to twelve months of sch 1C para 8(1).
- **The layer-2 seat.**
  The seat is an individual who is, or may become, a director, company secretary or member of a company, or who deals with one (assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership).
  Every question is `@export` with `@desc`, takes plain inputs only (yes or no, a number, a date, or a choice from a list in the person's words), builds any record, list or `MAYBE` in its own `WHERE`, and calls the layer-1 function that owns the rule.
  A fact another section answers (whether an officer is in default under s 1121; whether the provision is one of the Companies Acts) is asked as `yes`, `no` or `I do not know`, a `coa28 seat answer`, and passed on as `JUST TRUE`, `JUST FALSE` or `NOTHING`.
  Questions are named "Under section N," or "Under schedule N paragraph M," and are grouped under `§` headings in the order of the text, with a comment on a group that arises only in a situation (an institution that votes shares for you, a restrictions notice served on you, a takeover bid, a winding up).
  The seat does not ask a question of an official (what the Secretary of State must do, what the Houses may resolve) except where an individual may rely on the answer (s 1291, regulations a person relies on).
  The seat cases (`coa28-cases-seat.l4`) exercise every question on realistic facts, including a case outside the encoding that answers `NOTHING`.
- **What I did not do.**
  I did not write `README.md`, `encoding.json`, `subject.json` or `SOURCE-LICENSE.md` (the lead writes them).
  I did not read all of `references/source-patterns/` (the brief asks for it); I read the brief, the keel's notes and the supplied example seat, and used the patterns they name (quote and locator lines, `BRANCH`, a bar function, the gathering by hand, the seat's `@export` and `@desc`).
  I did not carry inert text in the modules as labelled strings or stubs (pattern 9 of that area advises it); the inert rows live in the coverage table only.

## Seat questions (coa28)

The 74 questions of `coa28-seat.l4`, in the order of the file, grouped under the file's `§§` headings.
The first column is the text the `@export` shows; the last is the layer-1 function the body calls.

| # | Group | Question (the `@export` text) | `DECIDE` name | Layer-1 function called |
|---|---|---|---|---|
| 1 | Part 44: miscellaneous provisions | Under section 1274(3), am I a member of a professional actuarial body? | `Under section 1274(3), am I a member of a professional actuarial body` | `s 1274(3) the person is a member of a professional actuarial body` |
| 2 | Part 44: miscellaneous provisions | Under section 1275(3), am I within subsection (3A) of section 17 of the 2004 Act (an administrator of a public service pension scheme, or a trustee or manager of an occupational or personal pension scheme)? | `Under section 1275(3), am I within subsection (3A) of section 17 of the 2004 Act` | `s 1275(3) the person is within subsection (3A) of section 17 of the 2004 Act` |
| 3 | Part 44: miscellaneous provisions | Under section 1278(1), is the institution one to which the voting-information power of section 1277 applies? | `Under section 1278(1), is the institution one to which section 1277 applies` | `s 1278(1) the institution is one to which section 1277 applies` |
| 4 | Part 44: miscellaneous provisions | Under section 1279(1), are these shares ones to which the voting-information power of section 1277 applies? | `Under section 1279(1), are the shares ones to which section 1277 applies` | `s 1279(1) the shares are shares to which section 1277 applies` |
| 5 | Part 44: miscellaneous provisions | Under section 1277(4), may I bring civil proceedings because an institution has not given me the information about its voting that the regulations require? | `Under section 1277(4), may I bring civil proceedings to enforce the obligation to provide information about voting` | `s 1277(4) the person may bring civil proceedings to enforce the obligation` |
| 6 | Part 44: miscellaneous provisions | Under section 1281 (section 241A(1) of the Enterprise Act 2002), may a public authority disclose information to me or for my case in civil proceedings? | `Under section 1281 (section 241A(1)), may a public authority disclose the information` | `s 1281 241A(1) the public authority may disclose the information to any person` |
| 7 | Part 44: miscellaneous provisions | Under section 1281 (section 241A(5) of the Enterprise Act 2002), am I barred from using information that was disclosed to me for this purpose? | `Under section 1281 (section 241A(5)), am I barred from using the information for my purpose` | `s 1281 241A(5) the person is barred from using the information for the purpose` |
| 8 | Part 44: miscellaneous provisions | Under section 1282 (section 176ZA(1) of the Insolvency Act 1986), do the expenses of winding up rank ahead of my floating charge in an England and Wales winding up? | `Under section 1282 (section 176ZA(1)), do the expenses of winding up rank ahead of floating charge claims` | `s 1282(1) 176ZA(1) the expenses of winding up have priority over claims to property comprised in or subject to a floating charge` |
| 9 | Part 44: miscellaneous provisions | Under section 1282 (section 176ZA(1) of the Insolvency Act 1986), how much of the expenses of an England and Wales winding up ranks ahead of floating charge claims, in pounds? | `Under section 1282 (section 176ZA(1)), how much of the expenses of winding up ranks ahead of floating charge claims` | `s 1282(1) 176ZA(1) the amount of the expenses that has priority over floating charge claims` |
| 10 | Part 44: miscellaneous provisions | Under section 1282 (Article 150ZA of the Insolvency (Northern Ireland) Order 1989), do the expenses of winding up rank ahead of my floating charge in a Northern Ireland winding up? | `Under section 1282 (Article 150ZA), do the expenses of winding up rank ahead of floating charge claims` | `s 1282(2) 150ZA(1) the expenses of winding up have priority over claims to property comprised in or subject to a floating charge` |
| 11 | Part 44: miscellaneous provisions | Under section 1283, does paragraph 3(1) of Schedule 3 to the Commonhold and Leasehold Reform Act 2002 apply to my commonhold association's alteration of its memorandum or articles? | `Under section 1283, does paragraph 3(1) of Schedule 3 to the Commonhold and Leasehold Reform Act 2002 apply to the alteration` | `s 1283 paragraph 3(1) of Schedule 3 to the Commonhold and Leasehold Reform Act 2002 applies to the alteration` |
| 12 | Part 45: Northern Ireland | Under section 1284(1), do the Companies Acts provision I rely on extend to Northern Ireland? | `Under section 1284(1), does the provision extend to Northern Ireland` | `s 1284(1) the provision extends to Northern Ireland` |
| 13 | Part 45: Northern Ireland | Under section 1284(2), does this Northern Ireland instrument cease to have effect (the Act says it shall)? | `Under section 1284(2), does the instrument cease to have effect` | `s 1284(2) the instrument ceases to have effect` |
| 14 | Part 45: Northern Ireland | Under section 1285(1), does this enactment on UK Societas extend to Northern Ireland? | `Under section 1285(1), does the enactment extend to Northern Ireland` | `s 1285(1) the enactment extends to Northern Ireland` |
| 15 | Part 45: Northern Ireland | Under section 1285(2), does this Northern Ireland enactment on the European Company cease to have effect (the Act says it shall)? | `Under section 1285(2), does the enactment cease to have effect` | `s 1285(2) the enactment ceases to have effect` |
| 16 | Part 45: Northern Ireland | Under section 1286(1), does the Great Britain legislation on this form of business organisation extend to Northern Ireland? | `Under section 1286(1), does the Great Britain legislation on the form extend to Northern Ireland` | `s 1286(1) the enactments in force in Great Britain relating to the form extend to Northern Ireland` |
| 17 | Part 45: Northern Ireland | Under section 1286(2), does this Northern Ireland enactment on a form of business organisation cease to have effect (the Act says it shall)? | `Under section 1286(2), does the enactment cease to have effect` | `s 1286(2) the enactment ceases to have effect` |
| 18 | Part 45: Northern Ireland | Under section 1287(1), do the business names provisions I rely on extend to Northern Ireland? | `Under section 1287(1), does the provision extend to Northern Ireland` | `s 1287(1) the provision extends to Northern Ireland` |
| 19 | Part 45: Northern Ireland | Under section 1287(2), does the Business Names (Northern Ireland) Order 1986 cease to have effect (the Act says it shall)? | `Under section 1287(2), does the instrument cease to have effect` | `s 1287(2) the instrument ceases to have effect` |
| 20 | Part 46: general supplementary provisions | Under section 1288, must the regulations or order I rely on have been made by statutory instrument? | `Under section 1288, must the regulations or order have been made by statutory instrument` | `s 1288 the regulations or order under this Act must be made by statutory instrument` |
| 21 | Part 46: general supplementary provisions | Under section 1291(1)(b), have the regulations or order I rely on, made under the "approval after being made" procedure, ceased to have effect? | `Under section 1291(1)(b), have the regulations or order ceased to have effect` | `s 1291(1)(b) the regulations or order have ceased to have effect` |
| 22 | Part 46: general supplementary provisions | Under section 1293, is the provision I am looking at an "enactment" for the purposes of the Act? | `Under section 1293, is the provision an enactment` | `s 1293 the provision is an enactment` |
| 23 | Part 46: general supplementary provisions | Under section 1297(3), does something done under a repealed provision have effect as if done under the corresponding provision of the 2006 Act? | `Under section 1297(3), does the thing have effect as if done under the corresponding provision` | `s 1297(3) the thing has effect thereafter as if done under or for the purposes of the corresponding provision of this Act` |
| 24 | Part 46: general supplementary provisions | Under section 1297(4), is a reference to a provision of the 2006 Act read as including the corresponding repealed provision? | `Under section 1297(4), is the reference read as including the corresponding repealed provision` | `s 1297(4) the reference to the provision of this Act is construed as including a reference to the corresponding repealed provision` |
| 25 | Part 46: general supplementary provisions | Under section 1297(5), is a reference to a repealed provision read as including the corresponding provision of the 2006 Act? | `Under section 1297(5), is the reference read as including the corresponding provision of the 2006 Act` | `s 1297(5) the reference to the repealed provision is construed as being or including a reference to the corresponding provision of this Act` |
| 26 | Part 47: final provisions | Under section 1299, does this provision of the Act extend to the whole of the United Kingdom? | `Under section 1299, does the provision extend to the whole of the United Kingdom` | `s 1299 the provision extends to the whole of the United Kingdom` |
| 27 | Schedule 1: interests in shares or debentures (the connected persons of sections 254 and 255) | Under schedule 1 paragraph 3, am I taken to have an interest in shares because of a contract or a right to acquire them? | `Under schedule 1 paragraph 3, am I taken to have an interest in the shares by virtue of paragraph 3` | `sch 1 para 3 the person has an interest in the shares by virtue of paragraph 3` |
| 28 | Schedule 1: interests in shares or debentures (the connected persons of sections 254 and 255) | Under schedule 1 paragraph 4, am I taken to have an interest in shares because I can exercise or control the exercise of the rights attached to them? | `Under schedule 1 paragraph 4, am I taken to have an interest in the shares by virtue of paragraph 4` | `sch 1 para 4 the person has an interest in the shares by virtue of paragraph 4` |
| 29 | Schedule 1: interests in shares or debentures (the connected persons of sections 254 and 255) | Under schedule 1 paragraph 5, am I taken to be interested in shares because a body corporate is interested in them? | `Under schedule 1 paragraph 5, am I taken to be interested in the shares because a body corporate is interested in them` | `sch 1 para 5(1) the person is taken to be interested in the shares because a body corporate is interested in them` |
| 30 | Schedule 1: interests in shares or debentures (the connected persons of sections 254 and 255) | Under schedule 1 paragraph 6, do I have an interest in shares as a beneficiary or trustee, once the exceptions are applied? | `Under schedule 1 paragraph 6, do I have an interest in the shares as a beneficiary or trustee` | `sch 1 paras 2 to 6 the person has an interest in the shares or debentures for sections 254 and 255` |
| 31 | Schedule 1: interests in shares or debentures (the connected persons of sections 254 and 255) | Under schedule 1 paragraphs 2 to 6, am I interested in these shares or debentures for the purposes of sections 254 and 255? | `Under schedule 1 paragraphs 2 to 6, am I interested in the shares or debentures for sections 254 and 255` | `sch 1 paras 2 to 6 the person has an interest in the shares or debentures for sections 254 and 255` |
| 32 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 2, do I hold, directly or indirectly, more than 25% of the shares in the company? | `Under schedule 1A paragraph 2, do I hold, directly or indirectly, more than 25% of the shares in the company` | `sch 1A para 2 the first condition is met` |
| 33 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 3, do I hold, directly or indirectly, more than 25% of the voting rights in the company? | `Under schedule 1A paragraph 3, do I hold, directly or indirectly, more than 25% of the voting rights in the company` | `sch 1A para 3 the second condition is met` |
| 34 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 4, do I hold, directly or indirectly, the right to appoint or remove a majority of the company's board of directors? | `Under schedule 1A paragraph 4, do I hold, directly or indirectly, the right to appoint or remove a majority of the board` | `sch 1A para 4 the third condition is met` |
| 35 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 5, do I meet the fourth condition: the right to exercise, or actually exercising, significant influence or control over the company? | `Under schedule 1A paragraph 5, do I meet the fourth condition` | `sch 1A para 5 the fourth condition is met` |
| 36 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 6, do I meet the fifth condition through a trust or a firm that is not a legal person? | `Under schedule 1A paragraph 6, do I meet the fifth condition` | `sch 1A para 6 the fifth condition is met` |
| 37 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 1, do I meet at least one of the specified conditions for significant control over the company? | `Under schedule 1A paragraph 1, do I meet at least one of the specified conditions` | `sch 1A para 1 at least one of the specified conditions is met by X in relation to company Y` |
| 38 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 25(1) and (2), do I meet the first, second or third condition once the carve-outs for a limited partner, and for holding only through one, are applied? | `Under schedule 1A paragraph 25(1) and (2), do I meet the specified condition once limited partners are left out` | `sch 1A paras 2 to 4 and 25 the individual meets the specified condition` |
| 39 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 18(3), do I have a majority stake in the legal entity? | `Under schedule 1A paragraph 18(3), do I have a majority stake in the legal entity` | `sch 1A para 18(3) A has a majority stake in B` |
| 40 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 22(1), are rights that can be exercised only in certain circumstances taken into account? | `Under schedule 1A paragraph 22(1), are rights exercisable only in certain circumstances taken into account` | `sch 1A para 22(1) the rights are taken into account` |
| 41 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 23, are rights attached to shares that I hold as security treated as held by the person who provided the security? | `Under schedule 1A paragraph 23, are the rights treated as held by the person who provided the security` | `sch 1A para 23 the rights are treated as held by the person who provided the security` |
| 42 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 8(1), do I hold an interest in the company for the purposes of section 790C(4) or (8)? | `Under schedule 1A paragraph 8(1), do I hold an interest in the company` | `sch 1A para 8(1) V holds an interest in company W` |
| 43 | Schedule 1A: people with significant control over a company | Under schedule 1A paragraph 24(2), must regard be had to the Secretary of State's guidance on "significant influence or control"? | `Under schedule 1A paragraph 24(2), must regard be had to the guidance` | `sch 1A para 24(2) regard must be had to the guidance` |
| 44 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 1(3), may the company issue a restrictions notice to me now? | `Under schedule 1B paragraph 1(3), may the company issue the restrictions notice to me now` | `sch 1B para 1(3) the company may issue the restrictions notice` |
| 45 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 3(1), does the restrictions notice stop me doing this? | `Under schedule 1B paragraph 3(1), does the restrictions notice stop me doing this` | `sch 1B para 3(1) the effect of the restrictions notice applies to the act` |
| 46 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 3(2), is my agreement to transfer the restricted interest void? | `Under schedule 1B paragraph 3(2), is my agreement to transfer the interest void` | `sch 1B para 3(2) the agreement to transfer the interest is void` |
| 47 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 3(4), is my agreement to transfer an associated right void? | `Under schedule 1B paragraph 3(4), is my agreement to transfer the associated right void` | `sch 1B para 3(4) the agreement to transfer the associated right is void` |
| 48 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 4(1), may the court give a direction to protect my rights as a third party affected by a restrictions notice? | `Under schedule 1B paragraph 4(1), may the court give a direction to protect third party rights` | `sch 1B para 4(1) the court may give a direction` |
| 49 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 5(1), do I commit an offence by doing this with a restricted interest? | `Under schedule 1B paragraph 5(1), do I commit an offence by doing this with a restricted interest` | `sch 1B para 5(1) the person commits an offence` |
| 50 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 5(3), do I commit an offence by not telling a person entitled to vote that the interest is restricted? | `Under schedule 1B paragraph 5(3), do I commit an offence by not notifying a person entitled to vote` | `sch 1B para 5(3) the person commits an offence` |
| 51 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 5(4), do I commit an offence by entering into an agreement that the restrictions make void? | `Under schedule 1B paragraph 5(4), do I commit an offence by entering into a void agreement` | `sch 1B para 5(4) the person commits an offence` |
| 52 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 7(1), what is the penalty for an offence under paragraph 5 or 6? | `Under schedule 1B paragraph 7(1), what is the penalty for an offence under paragraph 5 or 6` | `sch 1B para 7(1) the penalty for an offence under paragraph 5 or 6` |
| 53 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 8(2), may I apply to the court for an order that my interest cease to be subject to restrictions? | `Under schedule 1B paragraph 8(2), may I apply for an order that the interest cease to be subject to restrictions` | `sch 1B para 8(2) the person may apply for an order under paragraph 8` |
| 54 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 8(3), is the court barred from lifting the restrictions on my interest? | `Under schedule 1B paragraph 8(3), is the court barred from making an order lifting the restrictions` | `sch 1B para 8(3) the court is barred from making an order under paragraph 8` |
| 55 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 10(3), how much of the proceeds of the court-ordered sale must the court order paid to me, in pounds? | `Under schedule 1B paragraph 10(3), how much of the proceeds must the court order paid to me` | `sch 1B para 10(3) the amount the court must order to be paid to the applicant` |
| 56 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 11, must the company withdraw the restrictions notice it issued to me? | `Under schedule 1B paragraph 11, must the company by notice withdraw the restrictions notice` | `sch 1B para 11 the company must by notice withdraw the restrictions notice` |
| 57 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 13(1), do I commit an offence by not complying with the company's notice? | `Under schedule 1B paragraph 13(1), do I commit an offence by failing to comply with the notice` | `sch 1B para 13(1) the person commits an offence by failing to comply with the notice` |
| 58 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 13(2), do I commit an offence as an officer of a legal entity that fails to comply with the notice? | `Under schedule 1B paragraph 13(2), do I commit an offence as an officer of the entity` | `sch 1B para 13(2) the officer of the entity commits an offence` |
| 59 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 13(3), what is the penalty for failing to comply with a notice? | `Under schedule 1B paragraph 13(3), what is the penalty for failing to comply with a notice` | `sch 1B para 13(3) the penalty for an offence under paragraph 13` |
| 60 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 14(1), do I commit an offence by not complying with a duty to provide information? | `Under schedule 1B paragraph 14(1), do I commit an offence by failing to comply with the duty` | `sch 1B para 14(1) the person commits an offence by failing to comply with the duty` |
| 61 | Schedule 1B: enforcement of disclosure requirements (restrictions notices and offences) | Under schedule 1B paragraph 14B(1), do I commit an offence by knowingly making a false statement in answer to a notice or duty? | `Under schedule 1B paragraph 14B(1), do I commit the aggravated offence of making a false statement` | `sch 1B para 14B(1) the person commits the aggravated offence of making a false statement` |
| 62 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 1(1), must the rules afford me, as a holder, the same treatment as every other holder of securities of the same class? | `Under schedule 1C paragraph 1(1), must the rules afford me equivalent treatment as a holder` | `sch 1C para 1(1) the rules must afford the holders equivalent treatment` |
| 63 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 3, does our board, as the board of the offeree company, comply with the principle? | `Under schedule 1C paragraph 3, does the board of the offeree company comply with the principle` | `sch 1C para 3 the board of the offeree company complies with the principle` |
| 64 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 5, am I, as offeror, barred from announcing the takeover bid yet? | `Under schedule 1C paragraph 5, am I barred from announcing the takeover bid yet` | `sch 1C para 5 the offeror is barred from announcing the takeover bid yet` |
| 65 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 7(1), must the rules require me to make a mandatory takeover bid? | `Under schedule 1C paragraph 7(1), must the rules require me to make a mandatory takeover bid` | `sch 1C para 7(1) the rules must require P to make a mandatory takeover bid` |
| 66 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 8(1), what is the equitable price for my mandatory takeover bid, in pounds? | `Under schedule 1C paragraph 8(1), what is the equitable price` | `sch 1C para 8(1) the equitable price` |
| 67 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 8(2), what is the lowest the consideration in my mandatory takeover bid may be raised to, in pounds? | `Under schedule 1C paragraph 8(2), what is the lowest the offer consideration may be` | `sch 1C para 8(2) the offer consideration must not be less than` |
| 68 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 9(2), must the rules require cash to be offered as an alternative in my mandatory takeover bid? | `Under schedule 1C paragraph 9(2), must the rules require cash to be offered as an alternative` | `sch 1C para 9(2) the rules must ensure that cash is offered as an alternative` |
| 69 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 12(4), does the offer document state everything the rules must require it to state? | `Under schedule 1C paragraph 12(4), does the offer document state at least what the rules must require` | `sch 1C para 12(4) the offer document states at least the information the rules must require` |
| 70 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 13(1), is the time allowed for acceptance of the takeover bid long enough and not too long? | `Under schedule 1C paragraph 13(1), is the time allowed for acceptance within the limits the rules must ensure` | `sch 1C para 13(1) the time allowed for acceptance is within the limits the rules must ensure` |
| 71 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 17(1), must the rules require our board to obtain a general meeting's prior authorisation before this action? | `Under schedule 1C paragraph 17(1), must the rules require our board to obtain a general meeting's prior authorisation before the action` | `sch 1C para 17(1) the rules must require the board to obtain the prior authorisation of a general meeting` |
| 72 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 18(1), has our board met the requirement to draw up and make public its opinion of the takeover bid? | `Under schedule 1C paragraph 18(1), has the board met the requirement to draw up and make public its opinion` | `sch 1C para 18(1) the board has met the requirement to draw up and make public its opinion` |
| 73 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 20(1), is this offer a "takeover bid" for the purposes of the Schedule? | `Under schedule 1C paragraph 20(1), is the offer a takeover bid` | `sch 1C para 20(1) the offer is a takeover bid` |
| 74 | Schedule 1C: rules of the Takeover Panel (general principles and other provision) | Under schedule 1C paragraph 20(3), am I a person acting in concert with the offeror or the offeree company? | `Under schedule 1C paragraph 20(3), am I a person acting in concert` | `sch 1C para 20(3) the person is a person acting in concert` |

### Seat audit of 2026-11-12

The lead asked for every seat question's name and `@export` text to be read against the function its body calls, for a direction mismatch (a permission titled as a bar or the reverse) and for a subject mismatch ("must I" against "have I", a state against a duty).
I read all 74 questions against their functions.
Six did not ask what their function answers: one by direction, five by subject.
The other 68 were left as they were.
No answer was negated; each question was retitled to ask what the function answers, and the layer-1 functions are unchanged.

| question | kind | what was wrong | now |
|---|---|---|---|
| `Under schedule 1A paragraph 25(1) and (2)` | direction | The `@export` text asked "am I left out of the first, second and third conditions ...", so `JUST TRUE` would have read as "left out"; the function `sch 1A paras 2 to 4 and 25 the individual meets the specified condition` answers `JUST FALSE` when the person is left out | `@export` text: "Under schedule 1A paragraph 25(1) and (2), do I meet the first, second or third condition once the carve-outs for a limited partner, and for holding only through one, are applied?"; the `DECIDE` name, `Under schedule 1A paragraph 25(1) and (2), do I meet the specified condition once limited partners are left out`, already matched and is unchanged |
| `Under section 1275(3)` | subject | The `@export` text added "who can be required to pay the actuarial levy", but the function `s 1275(3) the person is within subsection (3A) of section 17 of the 2004 Act` answers only whether the person is in the class; a levy needs regulations under s 17 of the 2004 Act, which are outside the sources | `@export` text: "Under section 1275(3), am I within subsection (3A) of section 17 of the 2004 Act (an administrator of a public service pension scheme, or a trustee or manager of an occupational or personal pension scheme)?"; the `DECIDE` name is unchanged |
| `Under section 1284(2)` | subject | Asked "has ... ceased to have effect", a fact about now; the function `s 1284(2) the instrument ceases to have effect` states what the Act provides ("shall cease to have effect accordingly"), and the Act commences by order (s 1300(2)) | `@export` text: "Under section 1284(2), does this Northern Ireland instrument cease to have effect (the Act says it shall)?"; `DECIDE` name: `Under section 1284(2), does the instrument cease to have effect` |
| `Under section 1285(2)` | subject | the same | `@export` text: "Under section 1285(2), does this Northern Ireland enactment on the European Company cease to have effect (the Act says it shall)?"; `DECIDE` name: `Under section 1285(2), does the enactment cease to have effect` |
| `Under section 1286(2)` | subject | the same | `@export` text: "Under section 1286(2), does this Northern Ireland enactment on a form of business organisation cease to have effect (the Act says it shall)?"; `DECIDE` name: `Under section 1286(2), does the enactment cease to have effect` |
| `Under section 1287(2)` | subject | the same | `@export` text: "Under section 1287(2), does the Business Names (Northern Ireland) Order 1986 cease to have effect (the Act says it shall)?"; `DECIDE` name: `Under section 1287(2), does the instrument cease to have effect` |

Eight assertions in `coa28-cases-seat.l4` named the four renamed functions (two each); each is restated in place with `-- RECONCILED 2026-11-12: was <the original assertion>; <reason>`, and the facts and expected values are unchanged.
`coa28-seat.l4` and the check totals are unchanged in size: 74 questions, 232 seat assertions.
`Under section 1291(1)(b)` ("have the regulations or order ... ceased to have effect") was read and left as it is: its function computes the state on a given day, so "has ceased" is what it answers.

## What `check.sh` prints (coa28)

Run as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` from this folder, with `L4_BIN` the stable 1.6.110 and `L4_MAIN` the stable 1.6.109 (target `main`: every module is run with both builds and the four counts compared), `JL4_LIBRARY_PATH` unset.
`expected_failed` is empty: no assertion is meant to fail.
The baseline it replaced is the keel's own run in `inputs/KEEL-NOTES.md`: `TOTAL (3 modules) 0 346 0 0`, whose third module, `coa-definitions-tests.l4`, is not in this folder.
This folder holds the two keel files and 17 files of mine, and the new total is below.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa28-cases-seat.l4                            0       232       0        0         0 |      0       232       0        0  same
coa28-part44.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-part45.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-part46.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-part47.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-sch1.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa28-sch1a.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa28-sch1b.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa28-sch1c.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa28-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa28-tests-part44.l4                          0       104       0        0         0 |      0       104       0        0  same
coa28-tests-part45-47.l4                       0        37       0        0         0 |      0        37       0        0  same
coa28-tests-part46.l4                          0        97       0        0         0 |      0        97       0        0  same
coa28-tests-sch1.l4                            0        89       0        0         0 |      0        89       0        0  same
coa28-tests-sch1a.l4                           0       202       0        0         0 |      0       202       0        0  same
coa28-tests-sch1b.l4                           0       189       0        0         0 |      0       189       0        0  same
coa28-tests-sch1c.l4                           0       186       0        0         0 |      0       186       0        0  same
TOTAL (19 modules)                             0      1136       0        0           |      0      1136       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py`, run separately over every `coa28-*.l4` file against the raw text, once with `--refs` and once with `--strict`:

```
$ python3 -I srcrefs.py check --refs inputs/ukpga-2006-46.txt coa28-*.l4
srcrefs check: 527 src: lines, 248 runs, 265 locators, 0 problems

$ python3 -I srcrefs.py check --strict inputs/ukpga-2006-46.txt coa28-*.l4
srcrefs check: 527 src: lines, 248 runs, 265 locators, 0 problems
```

Control: a file with `#ASSERT 1 EQUALS 1` and `#ASSERT 1 EQUALS 2`, run through the same `check.sh`, prints `errors 1, satisfied 1, failed 1` and a red total, so a failing assertion is seen.
The raw text path in the `srcrefs.py` lines above is `inputs/ukpga-2006-46.txt` of the run directory (the command was run with the relative path `../../../inputs/ukpga-2006-46.txt` from this folder).

The files are generated from templates by a script that reads the raw text (`work/build.py`, not shipped), so no quotation is typed by hand.
