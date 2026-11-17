# NOTES (P4): Articles 28 to 39, Annex VII and Annex XIV of Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744

Status 2026-11-17.
Written by the part agent P4 (run `dst-aia-P4`, model Claude Sonnet 5.5) on the stable binary 1.6.110 (main, e51181d, 2026-11-11), cross-checked against the stable binary 1.6.109 (main, 4c887e0, 2026-11-04).
Ranges: lines 527-635 (Articles 28 to 39), 1800-1839 (Annex VII) and 1958-2010 (Annex XIV) of `eu-ai-act-2024-1689-consolidated-20260727.txt`.

## Status header: how each kind of claim in this file was checked

| kind of claim | how it was checked |
| --- | --- |
| what a provision says | every quotation in the `.l4` files is a mechanical slice of the consolidated text made by `srcrefs.py quote`; `srcrefs.py check --strict` on the layer-1 and test files printed: `srcrefs check: 413 src: lines, 210 runs, 225 locators, 0 problems` (layer-1, gate and test files) and `srcrefs check: 0 src: lines, 0 runs, 0 locators, 0 problems` (seat and case files, which carry no quotations) |
| the words quoted inside `FALSE-kind` and `NOTHING-kind` comments | a script of mine outside the deposit (`quotecheck.py`) looked every quoted segment up in the text: quotecheck: 415 segments, 0 not found |
| what the L4 does | `check.sh` (below): 1800 assertions satisfied, none failed, none refused, with the same four counts on both binaries, and in every test and case file the number of `#ASSERT` lines written equals the number `check.sh` reports satisfied (compared file by file by script); each `#TRACE` has an `-- EXPECT` comment written before it was run, and a script of mine outside the deposit (`traces.py`) ran every trace on both binaries and compared the outcome with the comment: 150 traces, all as expected and equal on both builds |
| the counts and tables in this file | computed by a script from the files in this folder when this file was generated; none is typed by hand |
| what the law means | not checked against anything outside this folder: no lawyer has read it, and nothing is "verified against the official text" |

**The consolidated text is a rendering.**
`eu-ai-act-2024-1689-consolidated-20260727.txt` is a plain-text rendering made by a converter script.
It is not the official text and has no legal effect, and so neither has anything in this folder.

**Commencement is IN (assumed, not ruled).**
Every function of Articles 28 to 39 and of Annex XIV takes `the date asked` and answers `NOTHING` before the group `Notified bodies, GPAI, governance, penalties and Art 78` applies (2 August 2025, Article 113 as the keel encodes it).
Annex VII is given effect by Article 43 (Chapter III Section 5), so it is in the group `General` (from 2 August 2026) and carries the keel's Article 111(2) saving for high-risk AI systems placed on the market earlier and not significantly changed.
Annex XIV is given effect by Article 30(2), so it follows the group of Articles 28 to 39.
No commencement provision is itself encoded here; the dates come only from the keel (`Art 113 the provision group applies`, `Omnibus Art 4 the version in force`).
The group of Annex VII and of Annex XIV is assumed, not ruled (PLAN.md section 3, "An Annex takes the group of the Article that gives it effect").

**Follow-up pass 1 (2026-11-17).**
The lead asked for three things and "nothing else": a second seat-question audit (see Seats), a Guide line or ruling named in each fork entry at a split site (see the fork register, Split sites and Marginal readings), and the seam S14 through the keel's `Art 2(2)` (see Seams, fork F-S14-reach).
Two kinds of answer changed, each restated in place with `-- RECONCILED 2026-11-17: was ...`: Article 36(8) and Article 36(9) first subparagraph now answer `JUST FALSE` where no designation has been suspended, restricted or withdrawn (fork F-36-where; it was `NOTHING`), and every function and rule of Annex VII now answers `JUST FALSE` (rules: `FULFILLED`) for a high-risk AI system under Article 6(1) with Section B products (fork F-S14-reach; it answered on its own provision).
Annex VII functions and rules take two more inputs for it, so their seat questions ask two more facts; no other answer changed.

**Follow-up pass 2 (2026-11-17).**
The lead asked for one thing and "nothing else": Article 32, a presumption gated by "Where" that answered `NOTHING` while Article 36(8) and (9) apply the periods ruling's rule (b) to a "where".
Article 32 now answers `JUST FALSE` when the "Where" fails and `NOTHING` only for "in so far as the applicable harmonised standards cover those requirements" (fork F-32-where); the two assertions it broke are restated in place with `-- RECONCILED 2026-11-17`, in `P4-tests-art-31-32.l4` and `P4-cases-seat-notified.l4`.
I looked for other sites of the same shape (table under Split sites, (ii-b)) and found none to change.
One count was corrected, with no answer changed: three branches of duties with a "where" gate (Article 28(7) second sentence, Article 28(8) first and second subparagraphs as amended) carried no `fork F-unmet-where` tag although their glosses name it; they are tagged now, so F-unmet-where is 52 branches, not 49.

**PLAN.md and the brief.**
For these ranges PLAN.md and the brief do not differ; where they would, the brief governs.
One point of form: the brief's example names (`s 47(2) ...`) are the generic template; the names here carry the provision's own label as PLAN.md section 2 gives it (`Art 28(1) ...`, `Annex VII point 3.1(a) ...`), which is the Regulation's own numbering.

## Files

All files are in this folder (`DEPOSIT/encodings/legalese-sonnet-5.5/`).

- `aia-annex-x.l4`, `aia-core.l4`, `aia-definitions.l4`, `aia-timeline.l4`: the keel's modules, read-only; I did not edit them.
- `P4-gate.l4`: the two gates and the month helper the P4 modules share (it restates no date of Article 111 or 113; it calls the keel's applicability function).
- Layer 1, with its tests (`P4-tests-<same name>.l4`):

| module | functions | regulative rules | test asserts | traces | traces that reach BREACH |
| --- | --- | --- | --- | --- | --- |
| `P4-art-28.l4` | 20 | 5 | 101 | 12 | 2 |
| `P4-art-29-30.l4` | 20 | 9 | 96 | 18 | 0 |
| `P4-art-31-32.l4` | 15 | 3 | 79 | 6 | 0 |
| `P4-art-33-35.l4` | 12 | 8 | 56 | 16 | 0 |
| `P4-art-36.l4` | 24 | 16 | 127 | 40 | 8 |
| `P4-art-37-39.l4` | 10 | 7 | 44 | 14 | 0 |
| `P4-annex-vii.l4` | 45 | 18 | 254 | 40 | 0 |
| `P4-annex-xiv.l4` | 12 | 1 | 69 | 4 | 0 |
| total | 158 | 67 | 826 | 150 | 10 |

- Layer 2: `P4-seat-notified.l4`, `P4-seat-provider.l4`, `P4-seat-rep.l4` and `P4-cases-seat-notified.l4`, `P4-cases-seat-provider.l4`, `P4-cases-seat-rep.l4` (see Seats).
- `NOTES.md` (this file), `PROGRESS.md`; `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` as supplied.
- `NEEDS-CORE.md` is not written: no type or constructor was missing from the core (every party and act type here is declared under its provision's label).

The `-- FALSE-kind` and `-- NOTHING-kind` comments of the layer-1 modules number 157 and 163; 107 of the FALSE-kind branches are bare "shall" duties (F-bare-shall) and 52 of the NOTHING-kind branches are unmet "where" or "if" gates of a duty (F-unmet-where).

## Coverage (P4)

**Audit.**
The three ranges hold 202 lines, all non-blank (counted by script from the raw file).
A table with one row per line would have 202 rows.
This table has 197 rows, because 27 rows each span several lines (a heading with its title, a category heading, an Article as a whole), together absorbing 79 lines, and 68 lines are the home of more than one row (a paragraph of several sentences that carry different rules, a point and its sub-points, the whole-Article rows).
A script checks that every one of the 202 lines falls inside at least one row (uncovered lines: 0), and that every function and rule of every layer-1 module is named by at least one row (functions and rules named by no row: 0).
Rows were counted before and after this audit: the first draft of the table, built from the line ranges, had 196 rows; the audit found five functions that no row named: the two `code is on the list` functions of Annex XIV (one new row, the list taken as a whole, whose lookup function `Annex XIV points 2 and 3 the code is on the list` is the home of the question F-annex-xiv-closed) and three that an existing row named under the wrong prefix (the Article 28(8) duty, Article 29(4) as enacted, Article 30(2) as enacted), repaired in their rows; the table now has 197 rows.

**Summary of dispositions.**

| disposition | rows |
| --- | --- |
| encoded | 130 |
| fork | 26 |
| inert (reason 1) | 40 |
| inert (reason 2) | 1 |
| total | 197 |

A row is `fork` when any fork-register entry below is cited in its note, including the cross-cutting F-months and F-passive, so a row that merely counts a period in months or years is a `fork` row.
`inert` rows and their reasons (1 not operative, 2 machinery, 3 text shown repealed or blank): the reason numbers are in the table; the repeated heading, marker and column-header rows are all reason 1.
No row is `repealed or blank in this text`: the lines marked `DELETED` in the consolidated file (lines 1865-1871 and the like) are outside my ranges.

**Inert rows that are not headings or markers** (the ones a reader could dispute):

- lines 562, Art 30(2), second subparagraph (power to amend Annex XIV by delegated act): inert (reason 2) (machinery: a rule-making power of the Commission (Guide section 4); affects no one now)
- lines 1837, Annex VII point 5.1: inert (reason 1) (a statement of the purpose of the surveillance that creates no rule)
- lines 1963, Annex XIV point 1, first sentence (conformity assessment may require the involvement of conformity assessment bodies): inert (reason 1) (a statement of fact that creates no rule)
- the other 38 inert rows are headings, titles, version markers and the column headers of the Annex XIV tables (reason 1 each); they are listed in the table.

**The table.**
The L4 names are the layer-1 functions and rules, each with its module in parentheses; where a provision has two versions, the dispatcher and the `as enacted` and `as amended` functions are all named.

| # | lines | unit | disposition | L4 name(s) (module) | note |
| --- | --- | --- | --- | --- | --- |
| 1 | 527 | marker `▼B` (the text that follows is as enacted) | inert (reason 1) | none | version marker, not text |
| 2 | 528-529 | SECTION 4, Notifying authorities and notified bodies | inert (reason 1) | none | heading |
| 3 | 530-531 | Article 28, Notifying authorities | inert (reason 1) | none | heading |
| 4 | 532 | Art 28(1) | encoded | `Art 28(1) the Member State has met the duty to designate or establish a notifying authority` (`P4-art-28.l4`)<br>`Art 28(1) the duty of the Member State to designate or establish a notifying authority` (`P4-art-28.l4`) |  |
| 5 | 533 | Art 28(2) | fork | `Art 28(2) the Member State may decide that the assessment and monitoring are carried out by a national accreditation body` (`P4-art-28.l4`) | F-28-2 |
| 6 | 534 | Art 28(3) | encoded | `Art 28(3) the notifying authority is established, organised and operated as required` (`P4-art-28.l4`) |  |
| 7 | 535 | Art 28(4) | encoded | `Art 28(4) the notifying authority is organised as required` (`P4-art-28.l4`) |  |
| 8 | 536 | Art 28(5) | fork | `Art 28(5) the notifying authority has kept to the bar on offering or providing activities and consultancy` (`P4-art-28.l4`)<br>`Art 28(5) the bar on the notifying authority offering or providing an activity that conformity assessment bodies perform` (`P4-art-28.l4`)<br>`Art 28(5) the bar on the notifying authority offering or providing consultancy services on a commercial or competitive basis` (`P4-art-28.l4`) | F-28-5 |
| 9 | 537 | Art 28(6) | encoded | `Art 28(6) the notifying authority has safeguarded the confidentiality of the information` (`P4-art-28.l4`)<br>`Art 28(6) the duty of the notifying authority to safeguard the confidentiality of the information` (`P4-art-28.l4`) |  |
| 10 | 538 | Art 28(7), first sentence | encoded | `Art 28(7) first sentence the notifying authority has an adequate number of competent personnel` (`P4-art-28.l4`) |  |
| 11 | 538 | Art 28(7), second sentence | encoded | `Art 28(7) second sentence the competent personnel have the necessary expertise` (`P4-art-28.l4`) |  |
| 12 | 539 | marker `▼M1 INSERTED` (Art 28(8) and (9)) | inert (reason 1) | none | version marker; the passages are in the Versions table |
| 13 | 540 | Art 28(8), first subparagraph | encoded | `Art 28(8) as amended first subparagraph the notifying authority has ensured the single application and the unified assessment` (`P4-art-28.l4`)<br>`Art 28(8) first subparagraph the notifying authority has ensured the single application and the unified assessment` (`P4-art-28.l4`)<br>`Art 28(8) the duty of the notifying authority to ensure the single application and the unified assessment` (`P4-art-28.l4`) | inserted: as amended only; a function and a regulative rule |
| 14 | 541 | Art 28(8), second subparagraph | fork | `Art 28(8) as amended second subparagraph the single application and the unified assessment are made available to a notified body already designated` (`P4-art-28.l4`)<br>`Art 28(8) second subparagraph the single application and the unified assessment are made available to a notified body already designated` (`P4-art-28.l4`) | inserted: as amended only; F-passive |
| 15 | 542 | Art 28(8), third subparagraph | encoded | `Art 28(8) as amended third subparagraph the number of times the body has to apply for designation pursuant to this Regulation` (`P4-art-28.l4`)<br>`Art 28(8) as amended third subparagraph the designation pursuant to this Regulation is applicable for the legislation` (`P4-art-28.l4`)<br>`Art 28(8) third subparagraph the number of times the body has to apply for designation pursuant to this Regulation` (`P4-art-28.l4`)<br>`Art 28(8) third subparagraph the designation pursuant to this Regulation is applicable for the legislation` (`P4-art-28.l4`) | inserted: as amended only; two functions |
| 16 | 543 | Art 28(8), fourth subparagraph | encoded | `Art 28(8) as amended fourth subparagraph the single application and the unified assessment procedure are shaped as required` (`P4-art-28.l4`)<br>`Art 28(8) fourth subparagraph the single application and the unified assessment procedure are shaped as required` (`P4-art-28.l4`) | inserted: as amended only |
| 17 | 544 | Art 28(9) | encoded | `Art 28(9) as amended the notifying authority is also the notifying authority for the single application and unified assessment procedure` (`P4-art-28.l4`)<br>`Art 28(9) the notifying authority is also the notifying authority for the single application and unified assessment procedure` (`P4-art-28.l4`) | inserted: as amended only |
| 18 | 545 | marker `▼B` | inert (reason 1) | none | version marker |
| 19 | 546-547 | Article 29, Application of a conformity assessment body for notification | inert (reason 1) | none | heading |
| 20 | 548 | Art 29(1) | encoded | `Art 29(1) the conformity assessment body has submitted its application to the right notifying authority` (`P4-art-29-30.l4`)<br>`Art 29(1) the duty of the conformity assessment body to submit an application for notification` (`P4-art-29-30.l4`) |  |
| 21 | 549 | Art 29(2), first subparagraph | encoded | `Art 29(2) first subparagraph the application for notification is accompanied as required` (`P4-art-29-30.l4`) |  |
| 22 | 550 | Art 29(2), second subparagraph | encoded | `Art 29(2) second subparagraph the valid documents on existing designations have been added` (`P4-art-29-30.l4`) |  |
| 23 | 551 | Art 29(3) | encoded | `Art 29(3) the conformity assessment body has provided the documentary evidence` (`P4-art-29-30.l4`)<br>`Art 29(3) the duty of the conformity assessment body to provide the documentary evidence` (`P4-art-29-30.l4`) |  |
| 24 | 552 | marker `▼M1 REPLACED` (Art 29(4)) | inert (reason 1) | none | version marker |
| 25 | 553 | Art 29(4), first subparagraph | fork | `Art 29(4) as amended first subparagraph the documents and certificates may be used` (`P4-art-29-30.l4`)<br>`Art 29(4) first subparagraph the documents and certificates may be used` (`P4-art-29-30.l4`)<br>`Art 29(4) as enacted first sentence the documents and certificates may be used` (`P4-art-29-30.l4`) | replaced: both versions; the same answer on the facts the function takes (F-29-4) |
| 26 | 554 | Art 29(4), second subparagraph | encoded | `Art 29(4) as amended second subparagraph the notified body has submitted the single application` (`P4-art-29-30.l4`)<br>`Art 29(4) second subparagraph the notified body has submitted the single application` (`P4-art-29-30.l4`)<br>`Art 29(4) the duty of the notified body to submit the single application` (`P4-art-29-30.l4`) | replaced: second subparagraph is new, as amended only |
| 27 | 555 | Art 29(4), third subparagraph | encoded | `Art 29(4) third subparagraph the notified body has updated the documentation` (`P4-art-29-30.l4`)<br>`Art 29(4) the duty of the notified body to update the documentation` (`P4-art-29-30.l4`) | unchanged by the Omnibus |
| 28 | 556 | marker `▼B` | inert (reason 1) | none | version marker |
| 29 | 557-558 | Article 30, Notification procedure | inert (reason 1) | none | heading |
| 30 | 559 | Art 30(1) | encoded | `Art 30(1) the notifying authority may notify the conformity assessment body` (`P4-art-29-30.l4`) |  |
| 31 | 560 | marker `▼M1 REPLACED` (Art 30(2)) | inert (reason 1) | none | version marker |
| 32 | 561 | Art 30(2), first subparagraph | encoded | `Art 30(2) as enacted the notifying authority has notified the conformity assessment body` (`P4-art-29-30.l4`)<br>`Art 30(2) as amended first subparagraph the notifying authority has notified the conformity assessment body` (`P4-art-29-30.l4`)<br>`Art 30(2) first subparagraph the notifying authority has notified the conformity assessment body` (`P4-art-29-30.l4`)<br>`Art 30(2) the duty of the notifying authority to notify the Commission and the other Member States` (`P4-art-29-30.l4`) | replaced: both versions (the as-amended text adds the Annex XIV basis) |
| 33 | 562 | Art 30(2), second subparagraph (power to amend Annex XIV by delegated act) | inert (reason 2) | none | machinery: a rule-making power of the Commission (Guide section 4); affects no one now |
| 34 | 563 | marker `▼B` | inert (reason 1) | none | version marker |
| 35 | 564 | Art 30(3), first sentence | encoded | `Art 30(3) first sentence the notification includes the full details` (`P4-art-29-30.l4`) |  |
| 36 | 564 | Art 30(3), second sentence | encoded | `Art 30(3) second sentence the notifying authority has provided the documentary evidence` (`P4-art-29-30.l4`)<br>`Art 30(3) the duty of the notifying authority to provide the documentary evidence` (`P4-art-29-30.l4`) |  |
| 37 | 565 | Art 30(4) | fork | `Art 30(4) the last day on which an objection may be raised` (`P4-art-29-30.l4`)<br>`Art 30(4) the conformity assessment body may perform the activities of a notified body` (`P4-art-29-30.l4`) | F-30-4, F-months |
| 38 | 566 | Art 30(5) | encoded | `Art 30(5) first sentence the Commission has entered into consultations` (`P4-art-29-30.l4`)<br>`Art 30(5) second and third sentences the Commission has decided and addressed its decision` (`P4-art-29-30.l4`)<br>`Art 30(5) the duty of the Commission to enter into consultations` (`P4-art-29-30.l4`)<br>`Art 30(5) the duty of the Commission to decide whether the authorisation is justified` (`P4-art-29-30.l4`)<br>`Art 30(5) the duty of the Commission to address its decision` (`P4-art-29-30.l4`) | three regulative rules |
| 39 | 567-568 | Article 31, Requirements relating to notified bodies | inert (reason 1) | none | heading |
| 40 | 569 | Art 31(1) | encoded | `Art 31(1) the notified body is established as required` (`P4-art-31-32.l4`) |  |
| 41 | 570 | Art 31(2) | encoded | `Art 31(2) the notified body satisfies the requirements as required` (`P4-art-31-32.l4`) |  |
| 42 | 571 | Art 31(3) | encoded | `Art 31(3) the organisational structure ensures confidence` (`P4-art-31-32.l4`) |  |
| 43 | 572 | Art 31(4) | encoded | `Art 31(4) first and second sentences the notified body is independent` (`P4-art-31-32.l4`)<br>`Art 31(4) third sentence the independence requirement precludes the use of the assessed high-risk AI system` (`P4-art-31-32.l4`) | three sentences, two functions |
| 44 | 573 | Art 31(5) | encoded | `Art 31(5) the conformity assessment body, its management and its personnel have kept to the bar on involvement and conflicting activity` (`P4-art-31-32.l4`) |  |
| 45 | 574 | Art 31(6) | encoded | `Art 31(6) the notified body is organised and operated as required` (`P4-art-31-32.l4`)<br>`Art 31(6) the duty of the notified body to document and implement a structure and procedures` (`P4-art-31-32.l4`) |  |
| 46 | 575 | Art 31(7) | encoded | `Art 31(7) the notified body has the procedures and the professional secrecy required` (`P4-art-31-32.l4`) |  |
| 47 | 576 | Art 31(8) | encoded | `Art 31(8) the notified body has procedures that take due account of the provider and the AI system` (`P4-art-31-32.l4`) |  |
| 48 | 577 | Art 31(9) | encoded | `Art 31(9) the notified body has the liability insurance required` (`P4-art-31-32.l4`)<br>`Art 31(9) the duty of the notified body to take out liability insurance` (`P4-art-31-32.l4`) |  |
| 49 | 578 | Art 31(10) | encoded | `Art 31(10) the notified body is capable of carrying out all its tasks as required` (`P4-art-31-32.l4`) |  |
| 50 | 579 | Art 31(11) | encoded | `Art 31(11) the notified body has the internal competences and the permanent personnel required` (`P4-art-31-32.l4`) |  |
| 51 | 580 | Art 31(12) | encoded | `Art 31(12) the notified body participates in coordination and keeps up with standards as required` (`P4-art-31-32.l4`)<br>`Art 31(12) the duty of the notified body to participate in coordination activities` (`P4-art-31-32.l4`) | two sentences, one function |
| 52 | 569-580 | Art 31 as a whole (the paragraphs together) | encoded | `Art 31 the notified body has satisfied the requirements given the answers of the paragraphs` (`P4-art-31-32.l4`) | combiner over the answers of the paragraphs |
| 53 | 581-582 | Article 32, Presumption of conformity with requirements relating to notified bodies | inert (reason 1) | none | heading |
| 54 | 583 | Art 32 | fork | `Art 32 the conformity assessment body is presumed to comply with the requirement set out in Article 31` (`P4-art-31-32.l4`) | F-32-where |
| 55 | 584-585 | Article 33, Subsidiaries of notified bodies and subcontracting | inert (reason 1) | none | heading |
| 56 | 586 | Art 33(1) | encoded | `Art 33(1) the notified body has ensured the requirements are met and informed the notifying authority` (`P4-art-33-35.l4`)<br>`Art 33(1) the duty of the notified body to ensure that the subcontractor or the subsidiary meets the requirements` (`P4-art-33-35.l4`)<br>`Art 33(1) the duty of the notified body to inform the notifying authority` (`P4-art-33-35.l4`) | two regulative rules |
| 57 | 587 | Art 33(2) | encoded | `Art 33(2) the notified body takes full responsibility for the tasks performed by subcontractors and subsidiaries` (`P4-art-33-35.l4`) |  |
| 58 | 588 | Art 33(3), first sentence | encoded | `Art 33(3) first sentence the activities may be subcontracted or carried out by a subsidiary` (`P4-art-33-35.l4`) | closed by "only": JUST FALSE |
| 59 | 588 | Art 33(3), second sentence | encoded | `Art 33(3) second sentence the notified body has made the list of its subsidiaries publicly available` (`P4-art-33-35.l4`)<br>`Art 33(3) the duty of the notified body to make a list of its subsidiaries publicly available` (`P4-art-33-35.l4`) |  |
| 60 | 589 | Art 33(4) | fork | `Art 33(4) the five years from the termination date of the subcontracting are running` (`P4-art-33-35.l4`)<br>`Art 33(4) the notified body has kept the documents at the disposal of the notifying authority` (`P4-art-33-35.l4`) | F-months (five years); F-passive |
| 61 | 590-591 | Article 34, Operational obligations of notified bodies | inert (reason 1) | none | heading |
| 62 | 592 | Art 34(1) | encoded | `Art 34(1) the notified body has verified the conformity of the high-risk AI system` (`P4-art-33-35.l4`)<br>`Art 34(1) the duty of the notified body to verify the conformity of high-risk AI systems` (`P4-art-33-35.l4`) |  |
| 63 | 593 | Art 34(2) | encoded | `Art 34(2) first sentence the notified body has avoided unnecessary burdens and taken due account of the provider and the system` (`P4-art-33-35.l4`)<br>`Art 34(2) second sentence the notified body has respected the degree of rigour and the level of protection required` (`P4-art-33-35.l4`) | two sentences, two functions |
| 64 | 594 | Art 34(3) | encoded | `Art 34(3) the notified body has submitted the documentation upon request` (`P4-art-33-35.l4`)<br>`Art 34(3) the duty of the notified body to make available and submit the documentation upon request` (`P4-art-33-35.l4`) |  |
| 65 | 595-596 | Article 35, Identification numbers and lists of notified bodies | inert (reason 1) | none | heading |
| 66 | 597 | Art 35(1) | encoded | `Art 35(1) the Commission has assigned a single identification number to the notified body` (`P4-art-33-35.l4`)<br>`Art 35(1) the duty of the Commission to assign a single identification number` (`P4-art-33-35.l4`) |  |
| 67 | 598 | Art 35(2) | encoded | `Art 35(2) the Commission has made the list publicly available and kept it up to date` (`P4-art-33-35.l4`)<br>`Art 35(2) the duty of the Commission to make the list publicly available` (`P4-art-33-35.l4`)<br>`Art 35(2) the duty of the Commission to keep the list up to date` (`P4-art-33-35.l4`) | two regulative rules |
| 68 | 599-600 | Article 36, Changes to notifications | inert (reason 1) | none | heading |
| 69 | 601 | Art 36(1) | encoded | `Art 36(1) the notifying authority has notified the relevant change` (`P4-art-36.l4`)<br>`Art 36(1) the duty of the notifying authority to notify the relevant change` (`P4-art-36.l4`) |  |
| 70 | 602 | Art 36(2), first subparagraph | encoded | `Art 36(2) the procedures that apply to the change to the notification` (`P4-art-36.l4`) | one function for both subparagraphs |
| 71 | 603 | Art 36(2), second subparagraph | fork | `Art 36(2) the procedures that apply to the change to the notification` (`P4-art-36.l4`) | F-36-2 |
| 72 | 604 | Art 36(3), first sentence | fork | `Art 36(3) first sentence the notified body has informed the notifying authority and the providers of its cessation` (`P4-art-36.l4`)<br>`Art 36(3) the duty of the notified body to inform the notifying authority and the providers of a planned cessation` (`P4-art-36.l4`) | F-months; planned cessation: BREACH trace |
| 73 | 604 | Art 36(3), second sentence | fork | `Art 36(3) second sentence the certificates may remain valid after the cessation` (`P4-art-36.l4`) | F-36-3, F-months |
| 74 | 604 | Art 36(3), third sentence | fork | `Art 36(3) third sentence the latter notified body has completed the full assessment before issuing new certificates` (`P4-art-36.l4`) | F-36-3, F-months |
| 75 | 604 | Art 36(3), fourth sentence | encoded | `Art 36(3) fourth sentence the notifying authority has withdrawn the designation of a notified body that has ceased` (`P4-art-36.l4`)<br>`Art 36(3) the duty of the notifying authority to withdraw the designation` (`P4-art-36.l4`) |  |
| 76 | 605 | Art 36(4), first sentence | encoded | `Art 36(4) first sentence the notifying authority has investigated the matter` (`P4-art-36.l4`)<br>`Art 36(4) the duty of the notifying authority to investigate the matter` (`P4-art-36.l4`) |  |
| 77 | 605 | Art 36(4), second sentence | encoded | `Art 36(4) second sentence the notified body has been informed of the objections and given the possibility to make its views known` (`P4-art-36.l4`)<br>`Art 36(4) the duty of the notifying authority to inform the notified body of the objections` (`P4-art-36.l4`) |  |
| 78 | 605 | Art 36(4), third sentence | encoded | `Art 36(4) third sentence the notifying authority has restricted, suspended or withdrawn the designation` (`P4-art-36.l4`)<br>`Art 36(4) the duty of the notifying authority to restrict, suspend or withdraw the designation` (`P4-art-36.l4`) |  |
| 79 | 605 | Art 36(4), fourth sentence | encoded | `Art 36(4) fourth sentence the notifying authority has immediately informed the Commission and the other Member States` (`P4-art-36.l4`)<br>`Art 36(4) the duty of the notifying authority to inform the Commission and the other Member States` (`P4-art-36.l4`) |  |
| 80 | 606 | Art 36(5) | encoded | `Art 36(5) the notified body has informed the providers concerned within 10 days` (`P4-art-36.l4`)<br>`Art 36(5) the duty of the notified body to inform the providers concerned within 10 days` (`P4-art-36.l4`) | 10 days: BREACH trace |
| 81 | 607 | Art 36(6) | encoded | `Art 36(6) the notifying authority has taken the steps to keep the files and make them available` (`P4-art-36.l4`)<br>`Art 36(6) the duty of the notifying authority to take appropriate steps to keep the files` (`P4-art-36.l4`) |  |
| 82 | 608 | Art 36(7), chapeau | encoded | `Art 36(7)(a) the notifying authority has assessed the impact on the certificates` (`P4-art-36.l4`)<br>`Art 36(7)(a) the duty of the notifying authority to assess the impact on the certificates` (`P4-art-36.l4`) | the conditions of the chapeau are inputs of each limb's function |
| 83 | 609 | Art 36(7)(a) | encoded | `Art 36(7)(a) the notifying authority has assessed the impact on the certificates` (`P4-art-36.l4`)<br>`Art 36(7)(a) the duty of the notifying authority to assess the impact on the certificates` (`P4-art-36.l4`) |  |
| 84 | 610 | Art 36(7)(b) | fork | `Art 36(7)(b) the notifying authority has submitted the report within three months` (`P4-art-36.l4`)<br>`Art 36(7)(b) the duty of the notifying authority to submit the report within three months` (`P4-art-36.l4`) | F-months; three months: BREACH trace |
| 85 | 611 | Art 36(7)(c) | encoded | `Art 36(7)(c) the notifying authority has required the notified body to suspend or withdraw the certificates unduly issued` (`P4-art-36.l4`)<br>`Art 36(7)(c) the duty of the notifying authority to require the suspension or withdrawal of the certificates unduly issued` (`P4-art-36.l4`) |  |
| 86 | 612 | Art 36(7)(d) | encoded | `Art 36(7)(d) the notifying authority has informed the Commission and the Member States about the certificates` (`P4-art-36.l4`)<br>`Art 36(7)(d) the duty of the notifying authority to inform the Commission and the Member States about the certificates` (`P4-art-36.l4`) |  |
| 87 | 613 | Art 36(7)(e) | encoded | `Art 36(7)(e) the notifying authority has provided the national competent authorities with the information` (`P4-art-36.l4`)<br>`Art 36(7)(e) the national competent authority has taken the appropriate measures where necessary` (`P4-art-36.l4`)<br>`Art 36(7)(e) the duty of the notifying authority to provide the national competent authorities with the information` (`P4-art-36.l4`) | two functions (authority, national competent authority) |
| 88 | 614 | Art 36(8), chapeau | fork | `Art 36(8) the certificates remain valid after a suspension or restriction` (`P4-art-36.l4`) | F-36-8; F-36-where; F-36-unduly |
| 89 | 615 | Art 36(8)(a) | fork | `Art 36(8)(a) the circumstance of point (a) holds` (`P4-art-36.l4`) | F-months (one month) |
| 90 | 616 | Art 36(8)(b) | fork | `Art 36(8)(b) the circumstance of point (b) holds` (`P4-art-36.l4`)<br>`Art 36(8)(b) the duty of the provider to confirm in writing within three months` (`P4-art-36.l4`) | F-months (three months); three months: BREACH trace |
| 91 | 617 | Art 36(9), first subparagraph, chapeau | fork | `Art 36(9) first subparagraph the certificates remain valid for nine months after a withdrawal` (`P4-art-36.l4`) | F-months (nine months); F-36-where; F-36-unduly |
| 92 | 618 | Art 36(9), first subparagraph, (a) | encoded | `Art 36(9) first subparagraph the certificates remain valid for nine months after a withdrawal` (`P4-art-36.l4`) | an input of the function |
| 93 | 619 | Art 36(9), first subparagraph, (b) | encoded | `Art 36(9) first subparagraph the certificates remain valid for nine months after a withdrawal` (`P4-art-36.l4`) | an input of the function |
| 94 | 620 | Art 36(9), second subparagraph | fork | `Art 36(9) second subparagraph the national competent authority may extend the provisional validity by a further three months` (`P4-art-36.l4`) | F-36-9, split site (ii) |
| 95 | 621 | Art 36(9), third subparagraph | encoded | `Art 36(9) third subparagraph the national competent authority or the notified body has immediately informed the Commission, the Member States and the other notified bodies` (`P4-art-36.l4`)<br>`Art 36(9) the duty of the national competent authority to inform the Commission, the Member States and the other notified bodies` (`P4-art-36.l4`) |  |
| 96 | 622-623 | Article 37, Challenge to the competence of notified bodies | inert (reason 1) | none | heading |
| 97 | 624 | Art 37(1) | encoded | `Art 37(1) the Commission has investigated the case` (`P4-art-37-39.l4`)<br>`Art 37(1) the duty of the Commission to investigate` (`P4-art-37-39.l4`) |  |
| 98 | 625 | Art 37(2) | encoded | `Art 37(2) the notifying authority has provided the Commission with the information on request` (`P4-art-37-39.l4`)<br>`Art 37(2) the duty of the notifying authority to provide the Commission with the information on request` (`P4-art-37-39.l4`) |  |
| 99 | 626 | Art 37(3) | encoded | `Art 37(3) the Commission has treated the sensitive information confidentially` (`P4-art-37-39.l4`)<br>`Art 37(3) the duty of the Commission to treat the sensitive information confidentially` (`P4-art-37-39.l4`) | Article 78 is another part's (seam S-78) |
| 100 | 627 | Art 37(4), first sentence | encoded | `Art 37(4) first sentence the Commission has informed the notifying Member State and requested the corrective measures` (`P4-art-37-39.l4`)<br>`Art 37(4) the duty of the Commission to inform the notifying Member State and request the corrective measures` (`P4-art-37-39.l4`) |  |
| 101 | 627 | Art 37(4), second sentence | fork | `Art 37(4) second sentence the Commission may suspend, restrict or withdraw the designation by means of an implementing act` (`P4-art-37-39.l4`) | F-37-4, split site (ii) |
| 102 | 627 | Art 37(4), third sentence | encoded | `Art 37(4) third sentence the implementing act has been adopted in accordance with the examination procedure` (`P4-art-37-39.l4`) | Article 98(2) is another part's (seam S-98) |
| 103 | 628-629 | Article 38, Coordination of notified bodies | inert (reason 1) | none | heading |
| 104 | 630 | Art 38(1) | encoded | `Art 38(1) the Commission has ensured the coordination and cooperation between notified bodies` (`P4-art-37-39.l4`)<br>`Art 38(1) the duty of the Commission to ensure the coordination and cooperation` (`P4-art-37-39.l4`) |  |
| 105 | 631 | Art 38(2) | encoded | `Art 38(2) the notifying authority has ensured that the bodies notified by it participate in the work of the group` (`P4-art-37-39.l4`)<br>`Art 38(2) the duty of the notifying authority to ensure that the notified bodies participate` (`P4-art-37-39.l4`) |  |
| 106 | 632 | Art 38(3) | encoded | `Art 38(3) the Commission has provided for the exchange of knowledge and best practices` (`P4-art-37-39.l4`)<br>`Art 38(3) the duty of the Commission to provide for the exchange of knowledge and best practices` (`P4-art-37-39.l4`) |  |
| 107 | 633-634 | Article 39, Conformity assessment bodies of third countries | inert (reason 1) | none | heading |
| 108 | 635 | Art 39 | fork | `Art 39 the conformity assessment body of a third country may be authorised to carry out the activities of notified bodies` (`P4-art-37-39.l4`) | F-39 |
| 109 | 1800-1801 | ANNEX VII, title | inert (reason 1) | none | heading |
| 110 | 1802 | Annex VII, 1. Introduction (heading) | inert (reason 1) | none | heading |
| 111 | 1803 | Annex VII point 1 | encoded | `Annex VII point 1 the conformity assessment is the procedure based on points 2 to 5` (`P4-annex-vii.l4`) |  |
| 112 | 1804 | Annex VII, 2. Overview (heading) | inert (reason 1) | none | heading |
| 113 | 1805 | Annex VII point 2, first sentence | encoded | `Annex VII point 2 first sentence the approved quality management system has been examined and is under surveillance` (`P4-annex-vii.l4`) |  |
| 114 | 1805 | Annex VII point 2, second sentence | encoded | `Annex VII point 2 second sentence the technical documentation has been examined` (`P4-annex-vii.l4`) |  |
| 115 | 1806 | Annex VII, 3. Quality management system (heading) | inert (reason 1) | none | heading |
| 116 | 1807 | Annex VII point 3.1, chapeau | encoded | `Annex VII point 3.1 the application of the provider includes everything listed given the answers of the limbs` (`P4-annex-vii.l4`) | combiner over the six limbs |
| 117 | 1808 | Annex VII point 3.1(a) | encoded | `Annex VII point 3.1(a) the application includes the name and address of the provider and of the authorised representative` (`P4-annex-vii.l4`) |  |
| 118 | 1809 | Annex VII point 3.1(b) | encoded | `Annex VII point 3.1(b) the application includes the list of AI systems covered` (`P4-annex-vii.l4`) |  |
| 119 | 1810 | Annex VII point 3.1(c) | encoded | `Annex VII point 3.1(c) the application includes the technical documentation for each AI system covered` (`P4-annex-vii.l4`) |  |
| 120 | 1811 | Annex VII point 3.1(d) | encoded | `Annex VII point 3.1(d) the application includes the documentation concerning the quality management system covering all the aspects of Article 17` (`P4-annex-vii.l4`) | Article 17 is another part's (seam S-17) |
| 121 | 1812 | Annex VII point 3.1(e) | encoded | `Annex VII point 3.1(e) the application includes a description of the procedures to keep the quality management system adequate and effective` (`P4-annex-vii.l4`) |  |
| 122 | 1813 | Annex VII point 3.1(f) | encoded | `Annex VII point 3.1(f) the application includes the written declaration that it has not been lodged with any other notified body` (`P4-annex-vii.l4`) |  |
| 123 | 1814 | Annex VII point 3.2, first sentence | encoded | `Annex VII point 3.2 first sentence the notified body has assessed the quality management system and determined whether it satisfies Article 17` (`P4-annex-vii.l4`)<br>`Annex VII point 3.2 the duty of the notified body to assess the quality management system and determine whether it satisfies Article 17` (`P4-annex-vii.l4`) |  |
| 124 | 1815 | Annex VII point 3.2, second paragraph | fork | `Annex VII point 3.2 second paragraph the decision has been notified to the provider or its authorised representative` (`P4-annex-vii.l4`)<br>`Annex VII point 3.2 the duty of the notified body to notify the decision` (`P4-annex-vii.l4`) | the bearer of the notification is read as the notified body (F-passive) |
| 125 | 1816 | Annex VII point 3.2, third paragraph | encoded | `Annex VII point 3.2 third paragraph the notification contains the conclusions of the assessment and the reasoned assessment decision` (`P4-annex-vii.l4`) |  |
| 126 | 1817 | Annex VII point 3.3 | encoded | `Annex VII point 3.3 the provider has kept the approved quality management system implemented, maintained, adequate and efficient` (`P4-annex-vii.l4`)<br>`Annex VII point 3.3 the duty of the provider to continue to implement and maintain the approved quality management system` (`P4-annex-vii.l4`) |  |
| 127 | 1818 | Annex VII point 3.4, first paragraph | encoded | `Annex VII point 3.4 first paragraph the provider has brought the intended change to the attention of the notified body` (`P4-annex-vii.l4`)<br>`Annex VII point 3.4 the duty of the provider to bring the intended change to the attention of the notified body` (`P4-annex-vii.l4`) |  |
| 128 | 1819 | Annex VII point 3.4, second paragraph | encoded | `Annex VII point 3.4 second paragraph the notified body has examined the proposed changes and decided` (`P4-annex-vii.l4`)<br>`Annex VII point 3.4 the duty of the notified body to examine the proposed changes and decide` (`P4-annex-vii.l4`) |  |
| 129 | 1820 | Annex VII point 3.4, third paragraph, first sentence | encoded | `Annex VII point 3.4 third paragraph first sentence the notified body has notified the provider of its decision` (`P4-annex-vii.l4`)<br>`Annex VII point 3.4 the duty of the notified body to notify the provider of its decision on the changes` (`P4-annex-vii.l4`) |  |
| 130 | 1820 | Annex VII point 3.4, third paragraph, second sentence | encoded | `Annex VII point 3.4 third paragraph second sentence the notification contains the conclusions of the examination and the reasoned assessment decision` (`P4-annex-vii.l4`) |  |
| 131 | 1821 | Annex VII, 4. Control of the technical documentation (heading) | inert (reason 1) | none | heading |
| 132 | 1822 | Annex VII point 4.1 | encoded | `Annex VII point 4.1 the provider has lodged the application for the assessment of the technical documentation` (`P4-annex-vii.l4`)<br>`Annex VII point 4.1 the duty of the provider to lodge the application for the assessment of the technical documentation` (`P4-annex-vii.l4`) |  |
| 133 | 1823 | Annex VII point 4.2, chapeau | encoded | `Annex VII point 4.2 the application includes everything listed given the answers of the limbs` (`P4-annex-vii.l4`) | combiner over the three limbs |
| 134 | 1824 | Annex VII point 4.2(a) | encoded | `Annex VII point 4.2(a) the application includes the name and address of the provider` (`P4-annex-vii.l4`) |  |
| 135 | 1825 | Annex VII point 4.2(b) | encoded | `Annex VII point 4.2(b) the application includes the written declaration that it has not been lodged with any other notified body` (`P4-annex-vii.l4`) |  |
| 136 | 1826 | Annex VII point 4.2(c) | encoded | `Annex VII point 4.2(c) the application includes the technical documentation referred to in Annex IV` (`P4-annex-vii.l4`) | Annex IV is another part's (seam S-IV) |
| 137 | 1827 | Annex VII point 4.3, first sentence | encoded | `Annex VII point 4.3 first sentence the technical documentation has been examined by the notified body` (`P4-annex-vii.l4`)<br>`Annex VII point 4.3 the duty of the notified body to examine the technical documentation` (`P4-annex-vii.l4`) |  |
| 138 | 1827 | Annex VII point 4.3, second sentence | fork | `Annex VII point 4.3 second sentence the notified body has been granted full access to the data sets` (`P4-annex-vii.l4`) | F-passive |
| 139 | 1828 | Annex VII point 4.4, first sentence | fork | `Annex VII point 4.4 first sentence the notified body may require the provider to supply further evidence or carry out further tests` (`P4-annex-vii.l4`) | F-AVII-44, split site (ii) |
| 140 | 1828 | Annex VII point 4.4, second sentence | encoded | `Annex VII point 4.4 second sentence the notified body has itself carried out adequate tests` (`P4-annex-vii.l4`)<br>`Annex VII point 4.4 the duty of the notified body to carry out adequate tests itself` (`P4-annex-vii.l4`) |  |
| 141 | 1829 | Annex VII point 4.5, first sentence | fork | `Annex VII point 4.5 first sentence the notified body has been granted access to the training and trained models` (`P4-annex-vii.l4`) | F-AVII-45, F-passive |
| 142 | 1829 | Annex VII point 4.5, second sentence | encoded | `Annex VII point 4.5 second sentence the access is subject to existing Union law on intellectual property and trade secrets` (`P4-annex-vii.l4`) |  |
| 143 | 1830 | Annex VII point 4.6, first paragraph | fork | `Annex VII point 4.6 first paragraph first sentence the decision of the notified body has been notified to the provider or its authorised representative` (`P4-annex-vii.l4`)<br>`Annex VII point 4.6 first paragraph second sentence the notification contains the conclusions of the assessment and the reasoned assessment decision` (`P4-annex-vii.l4`)<br>`Annex VII point 4.6 the duty of the notified body to notify the decision` (`P4-annex-vii.l4`) | two sentences, two functions; the bearer of the notification is read as the notified body (F-passive) |
| 144 | 1831 | Annex VII point 4.6, second paragraph | encoded | `Annex VII point 4.6 second paragraph first sentence the notified body has issued the certificate` (`P4-annex-vii.l4`)<br>`Annex VII point 4.6 second paragraph second sentence the certificate indicates what it must indicate` (`P4-annex-vii.l4`)<br>`Annex VII point 4.6 the duty of the notified body to issue the certificate` (`P4-annex-vii.l4`) | two sentences, two functions |
| 145 | 1832 | Annex VII point 4.6, third paragraph | encoded | `Annex VII point 4.6 third paragraph the certificate and its annexes contain all relevant information` (`P4-annex-vii.l4`) |  |
| 146 | 1833 | Annex VII point 4.6, fourth paragraph | encoded | `Annex VII point 4.6 fourth paragraph the notified body has refused to issue the certificate and informed the applicant giving detailed reasons` (`P4-annex-vii.l4`)<br>`Annex VII point 4.6 the duty of the notified body to refuse the certificate and inform the applicant` (`P4-annex-vii.l4`) |  |
| 147 | 1834 | Annex VII point 4.6, fifth paragraph | encoded | `Annex VII point 4.6 fifth paragraph first sentence the AI system has been re-trained before the application for a new conformity assessment` (`P4-annex-vii.l4`)<br>`Annex VII point 4.6 fifth paragraph second sentence the reasoned assessment decision contains specific considerations on the quality of the training data` (`P4-annex-vii.l4`) | two sentences, two functions |
| 148 | 1835 | Annex VII point 4.7 | encoded | `Annex VII point 4.7 first sentence the change has been assessed by the notified body which issued the certificate` (`P4-annex-vii.l4`)<br>`Annex VII point 4.7 second sentence the provider has informed the notified body of the change` (`P4-annex-vii.l4`)<br>`Annex VII point 4.7 third sentence the notified body has assessed the intended changes and decided` (`P4-annex-vii.l4`)<br>`Annex VII point 4.7 fourth sentence the notified body has assessed the changes, notified the provider and, where the changes are approved, issued a supplement` (`P4-annex-vii.l4`)<br>`Annex VII point 4.7 the duty of the provider to inform the notified body of the change` (`P4-annex-vii.l4`)<br>`Annex VII point 4.7 the duty of the notified body to assess the changes and decide` (`P4-annex-vii.l4`)<br>`Annex VII point 4.7 the duty of the notified body to assess the changes, notify the provider and issue a supplement` (`P4-annex-vii.l4`) | four sentences, four functions, three regulative rules |
| 149 | 1836 | Annex VII, 5. Surveillance of the approved quality management system (heading) | inert (reason 1) | none | heading |
| 150 | 1837 | Annex VII point 5.1 | inert (reason 1) | none | a statement of the purpose of the surveillance that creates no rule |
| 151 | 1838 | Annex VII point 5.2 | encoded | `Annex VII point 5.2 first sentence the provider has allowed the notified body to access the premises` (`P4-annex-vii.l4`)<br>`Annex VII point 5.2 second sentence the provider has shared all necessary information with the notified body` (`P4-annex-vii.l4`)<br>`Annex VII point 5.2 the duty of the provider to allow the notified body to access the premises` (`P4-annex-vii.l4`)<br>`Annex VII point 5.2 the duty of the provider to share all necessary information with the notified body` (`P4-annex-vii.l4`) | two sentences, two functions, two regulative rules |
| 152 | 1839 | Annex VII point 5.3 | fork | `Annex VII point 5.3 first sentence the notified body has carried out periodic audits and provided an audit report` (`P4-annex-vii.l4`)<br>`Annex VII point 5.3 second sentence the notified body may carry out additional tests of the AI systems` (`P4-annex-vii.l4`)<br>`Annex VII point 5.3 the duty of the notified body to carry out periodic audits and provide an audit report` (`P4-annex-vii.l4`) | F-AVII-53, split site (ii); first sentence has a regulative rule |
| 153 | 1958 | marker `▼M1 INSERTED` (Annex XIV) | inert (reason 1) | none | version marker |
| 154 | 1959-1960 | ANNEX XIV, title | inert (reason 1) | none | heading |
| 155 | 1961-1962 | Annex XIV, 1. Introduction (heading) | inert (reason 1) | none | heading |
| 156 | 1963 | Annex XIV point 1, first sentence (conformity assessment may require the involvement of conformity assessment bodies) | inert (reason 1) | none | a statement of fact that creates no rule |
| 157 | 1963 | Annex XIV point 1, second sentence | encoded | `Annex XIV as amended point 1 second sentence the conformity assessment body may carry out the conformity assessment` (`P4-annex-xiv.l4`)<br>`Annex XIV point 1 second sentence the conformity assessment body may carry out the conformity assessment` (`P4-annex-xiv.l4`) | closed by "Only": JUST FALSE |
| 158 | 1963 | Annex XIV point 1, third sentence | encoded | `Annex XIV as amended point 1 third sentence the type of AI systems is within the scope of the designation` (`P4-annex-xiv.l4`)<br>`Annex XIV point 1 third sentence the type of AI systems is within the scope of the designation` (`P4-annex-xiv.l4`) | the function takes a list of codes: no seat question |
| 159 | 1964-1965 | Annex XIV, 2. List of Codes, categories, and corresponding AI systems (heading) | inert (reason 1) | none | heading |
| 160 | 1966-1967 | Annex XIV point 2.a, AI systems subject to Annex I (category heading) | encoded | `Annex XIV as amended points 2 and 3 the category of the code` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the category of the code` (`P4-annex-xiv.l4`) | the category field of the rows below |
| 161 | 1968 | Annex XIV point 2.a, table header | inert (reason 1) | none | a column header, not a row of the list |
| 162 | 1969 | Annex XIV point 2.a, code AIP 0102 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 163 | 1970 | Annex XIV point 2.a, code AIP 0103 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 164 | 1971 | Annex XIV point 2.a, code AIP 0104 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 165 | 1972 | Annex XIV point 2.a, code AIP 0105 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 166 | 1973 | Annex XIV point 2.a, code AIP 0106 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 167 | 1974 | Annex XIV point 2.a, code AIP 0107 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 168 | 1975 | Annex XIV point 2.a, code AIP 0108 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 169 | 1976 | Annex XIV point 2.a, code AIP 0109 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 170 | 1977 | Annex XIV point 2.a, code AIP 0110 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 171 | 1978 | Annex XIV point 2.a, code AIP 0111 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 172 | 1979 | Annex XIV point 2.a, code AIP 0112 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 173 | 1980-1981 | Annex XIV point 2.b, AI systems subject to point 1 of Annex III (category heading) | encoded | `Annex XIV as amended points 2 and 3 the category of the code` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the category of the code` (`P4-annex-xiv.l4`) | the category field of the rows below |
| 174 | 1982 | Annex XIV point 2.b, table header | inert (reason 1) | none | a column header, not a row of the list |
| 175 | 1983 | Annex XIV point 2.b, code AIB 0201 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 176 | 1984 | Annex XIV point 2.b, code AIB 0202 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 177 | 1985 | Annex XIV point 2.b, code AIB 0203 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 178 | 1986-1987 | Annex XIV, 3. AI technology-specific codes (heading) | inert (reason 1) | none | heading |
| 179 | 1988-1989 | Annex XIV point 3.a, Symbolic AI and expert systems (category heading) | encoded | `Annex XIV as amended points 2 and 3 the category of the code` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the category of the code` (`P4-annex-xiv.l4`) | the category field of the rows below |
| 180 | 1990 | Annex XIV point 3.a, table header | inert (reason 1) | none | a column header, not a row of the list |
| 181 | 1991 | Annex XIV point 3.a, code AIH 0101 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 182 | 1992-1993 | Annex XIV point 3.b, Machine learning, excluding generative AI and general-purpose AI systems (category heading) | encoded | `Annex XIV as amended points 2 and 3 the category of the code` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the category of the code` (`P4-annex-xiv.l4`) | the category field of the rows below |
| 183 | 1994 | Annex XIV point 3.b, table header | inert (reason 1) | none | a column header, not a row of the list |
| 184 | 1995 | Annex XIV point 3.b, code AIH 0201 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 185 | 1996 | Annex XIV point 3.b, code AIH 0202 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 186 | 1997 | Annex XIV point 3.b, code AIH 0203 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 187 | 1998 | Annex XIV point 3.b, code AIH 0204 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 188 | 1999 | Annex XIV point 3.b, code AIH 0205 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 189 | 2000-2001 | Annex XIV point 3.c, AI systems based on general-purpose AI models or generative AI (category heading) | encoded | `Annex XIV as amended points 2 and 3 the category of the code` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the category of the code` (`P4-annex-xiv.l4`) | the category field of the row below |
| 190 | 2002 | Annex XIV point 3.c, table header | inert (reason 1) | none | a column header, not a row of the list |
| 191 | 2003 | Annex XIV point 3.c, code AIH 0301 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 192 | 2004-2005 | Annex XIV point 3.d, Emerging AI technologies (category heading) | encoded | `Annex XIV as amended points 2 and 3 the category of the code` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the category of the code` (`P4-annex-xiv.l4`) | the category field of the row below |
| 193 | 2006 | Annex XIV point 3.d, table header | inert (reason 1) | none | a column header, not a row of the list |
| 194 | 2007 | Annex XIV point 3.d, code AIH 0401 | encoded | `Annex XIV as amended points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the type of AI systems the code stands for` (`P4-annex-xiv.l4`) | table row |
| 195 | 1964-2007 | Annex XIV points 2 and 3, the list as a whole (is a code on the list?) | fork | `Annex XIV as amended points 2 and 3 the code is on the list` (`P4-annex-xiv.l4`)<br>`Annex XIV points 2 and 3 the code is on the list` (`P4-annex-xiv.l4`) | F-annex-xiv-closed |
| 196 | 2008-2009 | Annex XIV, 4. Application for designation (heading) | inert (reason 1) | none | heading |
| 197 | 2010 | Annex XIV point 4 | encoded | `Annex XIV as amended point 4 the application for designation uses the codes of the lists` (`P4-annex-xiv.l4`)<br>`Annex XIV point 4 the application for designation uses the codes of the lists` (`P4-annex-xiv.l4`)<br>`Annex XIV point 4 the duty of the conformity assessment body to use the lists of codes` (`P4-annex-xiv.l4`) | the function takes a list of codes: no seat question |

## Fork register (P4)

Each entry gives the provision, the function, the reading taken, the other reading, and the text that licenses each.
The two conventions F-bare-shall and F-unmet-where, and the sites F-31-7, F-31-9, F-36-unduly and F-annex-xiv-closed, are the case-by-case questions the Guide leaves to the encoder (ENCODING-GUIDE.md, "Questions with no convention", the maintainer, typed 2026-11-05T10:25:24Z: "an unless or except once it is met; a bare must not done; listed in Schedule N; a duty whose if or where is unmet; (other than X)").
Each site below is for the human reviewer to overrule.


**F-bare-shall** (every "shall" duty without a "where" or "if" gate, in all eight modules: 107 branches; Marginal readings M-a1).
Question: when the facts say the duty was not done, is the answer `JUST FALSE` or `NOTHING`?
Taken: `JUST FALSE`, with a `FALSE-kind` comment that quotes the "shall" (a bare "shall" not done).
Other reading: `NOTHING`, because the text does not say what follows from a duty not done.
Text: each branch quotes its own sentence; the keel's F-4-1 takes the same reading, and PLAN.md's worked example (line 366) is a bare "shall" not done, taken case by case.

**F-unmet-where** (every duty whose "where", "if", "whenever", "in the event" or "with the exception of" is not met: 52 branches; M-b1).
Question: for a function that asks whether a duty was met, what does a failed gate answer?
Taken: `NOTHING` (limited by its own wording): the duty never arose, so the text does not answer whether it was met.
Other reading: `JUST FALSE`, as the periods ruling's rule (b) gives for a failed "where" and as reading (a) gives for a failed "if".
Text: the gate words are quoted in each branch (for example Article 36(4), "Where a notifying authority has sufficient reason to consider"; Annex VII point 4.6 fourth paragraph, "Where the AI system is not in conformity with the requirements set out in Chapter III, Section 2").
Authority (ENCODING-GUIDE.md section 5, line 95, "Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z)"): "a duty whose "if" or "where" is unmet" is one of the six questions the rulings "leave open", "decided site by site, at encoding time, on the text's own words and the encoder's best judgment", each site with "one fork line".
That line gives no answer, so `NOTHING` is my judgment (assumed, not ruled) and no ruling supports it or rules it out.
Where the rulings, read literally, point the other way: 21 branches quote the word "where" in their gate and 5 quote "when", "upon", "whenever" or "on request"; the periods ruling's rule (b) (line 93: "a "where ..." condition: when it fails the answer is `JUST FALSE`") and the delegated-definitions ruling's rule (c) (line 94: ""when", "upon" and "whenever" count as "where"") would give `JUST FALSE` there.
I kept `NOTHING` because every one of these functions asks whether a duty was met, which is the case line 95 names as open.
7 branches quote "if" or "in the event of" (line 86 lists "if" among the words after which a failed condition is the text's no); 19 quote none of these words, the subject of the sentence has not arisen ("The certificate", "The proposed changes"), which line 87 calls "is silent".
The sites whose gate quotes "where", "when", "upon", "whenever" or "on request" (the "when" group is Art 28(8) as amended second subparagraph, Art 29(4) third subparagraph, Art 34(3), Art 37(2), Annex XIV as amended point 4; the "where" group is listed in M-b1) are the ones a lawyer is most likely to overrule.

**F-months** (every period counted in months or years: Article 30(4) two months; Article 33(4) five years; Article 36(3) one year before a planned cessation and nine months; Article 36(7)(b) three months; Article 36(8)(a) one month and (b) three months; Article 36(9) nine months).
Question: how is a month or a year counted from a date?
Taken (assumed, not ruled): by the `add months` and `add years` of the `daydate` library, the same day of the month or the last day of the month where there is none (`P4-gate.l4`); "two weeks" is 14 days.
Other readings: 30-day months and 365-day years; or a period that ends on the day before the corresponding date. They differ only at the end of a month or across a leap day.
Text: the periods are stated in the text without a counting rule ("one month", "three months", "nine months", "five years").

**F-passive** (where the text puts a duty or power in the passive and names no bearer).
Taken: no regulative rule where the bearer is not named: Article 28(8) second subparagraph ("shall also be made available"), Article 33(4) ("shall be kept at the disposal"), Annex VII point 4.3 second sentence ("shall be granted full access"), Annex VII point 4.5 first sentence ("shall also be granted access"), and Article 39 ("may be authorised"); each is a function over the facts.
Taken, the other way: a rule where the text names the owner of the decision that is to be notified, the notified body: Annex VII point 3.2 second paragraph ("The decision shall be notified") and point 4.6 first paragraph ("The decision of the notified body shall be notified").
Other reading: no rule at those two (the bearer is not named), and a rule at the first five (the evident operator: the notifying authority, the notified body, the provider, an authority).
Text: the sentences quoted.

**F-annex-xiv-closed** (Annex XIV points 2 and 3, function `Annex XIV points 2 and 3 the code is on the list`).
Question: is a code that is not on the list an Annex XIV code, or does the text not say?
Taken: `JUST FALSE`.
Other reading: `NOTHING` (a bare list).
Text for the taken reading: the Annex "sets out" the list of codes the bodies "shall use" (point 4) and Article 30(2) as amended refers to "the list of codes, categories, and corresponding types of AI systems referred to in Annex XIV"; the Guide's ruling of 2026-11-05 (a) answers `JUST FALSE` for a definition the text hands to a list, as the keel's F-annex-x-closed reads Annex X.
Authority (ENCODING-GUIDE.md line 94, delegated-definitions ruling, (a)): "a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`".
Whether Article 30(2) as amended and point 4 "hand" the question to the list is my reading, listed as M-a6.

**F-31-9** (Article 31(9), `Art 31(9) the notified body has the liability insurance required`).
Question: what is the answer when the "unless" is met (the Member State assumes the liability or is itself directly responsible)?
Taken: `JUST TRUE`, the duty counts as met.
Other reading: `NOTHING`, because the duty does not apply.
Text: "unless liability is assumed by the Member State in which they are established in accordance with national law or that Member State is itself directly responsible for the conformity assessment".
Authority (ENCODING-GUIDE.md line 95): ""an "unless" or "except" once it is met" is one of the six questions "decided site by site, at encoding time"; no ruling covers it.
Line 86 lists "unless" among the words after which a failed condition is the text's no; here the exception is met, which is the case line 95 leaves open.

**F-31-7** (Article 31(7), `Art 31(7) the notified body has the procedures and the professional secrecy required`).
Question: are the two "except" clauses ("except when its disclosure is required by law"; "except in relation to the notifying authorities of the Member State in which their activities are carried out") separate limbs?
Taken: no; each exception is asked inside the fact it qualifies, so the function never sees an exception once met apart from its rule.
Other reading: separate inputs for the rule and the exception, with `JUST TRUE` where the exception applies.

**F-36-unduly** (Article 36(8) and Article 36(9) first subparagraph: "With the exception of certificates unduly issued").
Taken: `NOTHING` for a certificate unduly issued: the paragraph does not speak of it.
Other reading: `JUST FALSE`, the text excluding such a certificate from the validity the paragraph gives.
Authority (ENCODING-GUIDE.md line 95): ""an "unless" or "except" once it is met" is left to the encoder, site by site, with a fork line; line 86 names "except" among the "plain variants" of "unless" after which the text says no in its own words, which is the other reading.

**F-28-2** (Article 28(2), `Art 28(2) the Member State may decide that the assessment and monitoring are carried out by a national accreditation body`).
Taken: `JUST TRUE` when the body is a national accreditation body within the meaning of Regulation (EC) No 765/2008 and the assessment and monitoring are carried out in accordance with it; otherwise `NOTHING` (a power named by "may", limited by a named complement; grant ruling of 2026-11-12, limit (1)).
Other reading: `JUST FALSE` ("within the meaning of, and in accordance with" read as an "if").
Authority (ENCODING-GUIDE.md line 87): `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit", as applied by the ruling of 2026-11-12, limit (1), which BRIEF.md records: a function "NAMED for a grant or a power" ("may") that answers `JUST FALSE` because an "if" gate failed "reads as "may not", a grant turned into a bar".

**F-28-5** (Article 28(5), the two bars).
Taken: "on a commercial or competitive basis" qualifies the consultancy services only; an activity that conformity assessment bodies perform is barred whether or not it is offered commercially.
Other reading: the phrase qualifies both limbs, so an activity offered on a non-commercial basis is not barred.
Text: "shall offer or provide neither any activities that conformity assessment bodies perform, nor any consultancy services on a commercial or competitive basis" (the "neither ... nor" puts the phrase at the end of the second limb).

**F-29-4** (Article 29(4) first subparagraph, both versions).
The Omnibus changed "designated under" to "designated pursuant to" and "to support their designation procedure" to "to support and expedite their designation procedure".
Taken: the same permission on the facts the function asks (one input for the use of the documents), so the as-enacted and the as-amended functions answer alike; `NOTHING` where the notified body is not designated under other legislation (a named complement).
Other reading: "expedite" widens the permission from 27 July 2026, so a use only to expedite counts only as amended; the input then needs two facts.
Authority (ENCODING-GUIDE.md line 87): `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit", as applied by the ruling of 2026-11-12, limit (1), which BRIEF.md records: a function "NAMED for a grant or a power" ("may") that answers `JUST FALSE` because an "if" gate failed "reads as "may not", a grant turned into a bar". The limit here is a named complement ("designated under", "pursuant to", other Union harmonisation legislation).

**F-30-4** (Article 30(4), `Art 30(4) the conformity assessment body may perform the activities of a notified body`).
Taken: the body may perform the activities of a notified body only once the period (two weeks for a notification with an accreditation certificate, two months for one with documentary evidence) has run with no objection raised in it; a notification with both or with neither kind of evidence has no period in the text: `NOTHING` (undefined term).
Other readings: the body may begin on notification unless an objection is raised within the period; or "within" the period reads as "by the end of" the period (the same day counts).
Text: "may perform the activities of a notified body only where no objections are raised by the Commission or the other Member States within two weeks ... or within two months ...".
Authority: line 86 (a condition "the text introduces with "if", "only if" ..." answers `JUST FALSE` where it fails) and the ruling of 2026-11-12, limit (2) (BRIEF.md): "Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only")"; the periods ruling, rule (a) (line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`", for the two weeks and the two months.
The `NOTHING` branch (a notification with both kinds of evidence or with neither, so no period): line 87, the text "leaves a term undefined".

**F-36-2** (Article 36(2) second subparagraph, `Art 36(2) the procedures that apply to the change to the notification`).
Taken: "paragraphs (3) to (9)" are the paragraphs of Article 36, the Article that holds the sentence; "other than extensions of its scope" is its own input.
Other reading: paragraphs of Article 29 or 30, named in the sentence before; Article 29 has four paragraphs and Article 30 five (lines 548-555 and 559-566), so they cannot hold paragraphs (3) to (9).

**F-36-3** (Article 36(3) second and third sentences).
(a) "The certificates ... may remain valid for a period of nine months ..., on condition that another notified body has confirmed in writing": `NOTHING` where the condition is not met (a grant limited by a condition); other reading: `JUST FALSE`.
Authority (ENCODING-GUIDE.md line 87): `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit", as applied by the ruling of 2026-11-12, limit (1), which BRIEF.md records: a function "NAMED for a grant or a power" ("may") that answers `JUST FALSE` because an "if" gate failed "reads as "may not", a grant turned into a bar". "On condition that" is a plain variant of "if" (line 86), which for a function not named for a power would answer `JUST FALSE`; the grant ruling is what decides it.
The nine months themselves are a period the text fixes in its own words: outside it `JUST FALSE` (line 93, rule (a)).
(b) "The latter notified body shall complete a full assessment ... by the end of that nine-month-period before issuing new certificates": read as complete on or before the day of the first issue and within nine months of the cessation; other reading: strictly before the day of the first issue.

**F-36-8** (Article 36(8), `Art 36(8) the certificates remain valid after a suspension or restriction`).
Taken: when neither circumstance (a) nor (b) holds the text is silent: `NOTHING` (the list is not closed with "only").
Other reading: `JUST FALSE` ("shall remain valid in one of the following circumstances" read as exhaustive).
Circumstance (a) counts "within one month of the suspension or restriction" (F-months); circumstance (b) is a conjunction of the authority's confirmation and, where it finds the notified body incapable, the provider's written confirmation within three months.
Authority (ENCODING-GUIDE.md line 87): `NOTHING` "where the text lists without closing the list"; the list of circumstances is not closed with "only".

**F-32-where** (Article 32, `Art 32 the conformity assessment body is presumed to comply with the requirement set out in Article 31`; seat question `Under Article 32, as a notified body, am I presumed to comply with the requirement set out in Article 31?`).
Text: "Where a conformity assessment body demonstrates its conformity with the criteria laid down in the relevant harmonised standards or parts thereof, the references of which have been published in the Official Journal of the European Union, it shall be presumed to comply with the requirements set out in Article 31 in so far as the applicable harmonised standards cover those requirements."
Question: what does the presumption function answer when the "Where" condition fails (the body does not demonstrate conformity with the criteria, or the references have not been published), and when it holds but the standards do not cover the requirement?
Taken: `JUST FALSE` when the "Where" fails; `NOTHING` only when the "Where" holds and the standards do not cover the requirement; `JUST TRUE` when all three hold.
Authority: the periods ruling of 2026-11-05, rule (b) (ENCODING-GUIDE.md line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`", for the "Where"; and rule (c) (same line): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`", for "in so far as the applicable harmonised standards cover those requirements".
A presumption is not a duty (line 95, "a duty whose "if" or "where" is unmet", does not reach it) and not a "may" (the ruling of 2026-11-12, limit (3), does not reach it), so no line sends it to a lawyer and the same ruling (b) applies as for F-36-where.
Changed 2026-11-17 (follow-up 2): the first pass answered `NOTHING` for a failed "Where" ("the text says nothing about a body that does not meet those conditions"); the answer did not follow line 93 and was inconsistent with F-36-where, so I changed it and restated the two assertions it broke, in place, with `-- RECONCILED 2026-11-17` (`P4-tests-art-31-32.l4`, and `P4-cases-seat-notified.l4`).
Other readings: `NOTHING` for a failed "Where" (the presumption is limited in its own wording and the case falls outside the limit, line 87); `JUST FALSE` also where the standards do not cover the requirement ("in so far as" read as a condition, line 86).
A presumption answered `JUST FALSE` means "the text does not presume the body to comply", not "the body does not comply".

**F-36-where** (Article 36(8), "where a designation has been suspended or restricted", and Article 36(9) first subparagraph, "where a designation has been withdrawn"; `Art 36(8) the certificates remain valid after a suspension or restriction` and `Art 36(9) first subparagraph the certificates remain valid for nine months after a withdrawal`).
Question: when no designation has been suspended or restricted (or withdrawn), what does the validity function answer?
Taken: `JUST FALSE`.
Authority: the periods ruling of 2026-11-05, rule (b) (ENCODING-GUIDE.md line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`".
The two functions are named for an effect ("remain valid"), not for a grant or a power ("may"), so the grant ruling of 2026-11-12 does not apply to them.
Changed 2026-11-17: the first pass answered `NOTHING` and filed both gates under F-unmet-where as if the functions asked whether a duty was met; on reading line 93 the answer did not follow the Guide's line, so I changed it and restated the six assertions it broke, in place, with `-- RECONCILED 2026-11-17` (two in `P4-tests-art-36.l4`, two in each of the notified-body and provider case files).
Other reading: `NOTHING`, because the text limits the validity in its own wording and the case falls outside the limit (line 87).
Same shape, not a duty and not a "may": Article 32, a presumption gated by "Where" (F-32-where).

**F-36-9** (Article 36(9) second subparagraph, `Art 36(9) second subparagraph the national competent authority may extend the provisional validity by a further three months`; split site (ii)).
(a) The gate "In the circumstances referred to in the first subparagraph" fails: `JUST FALSE` (periods ruling, rule (b)); other reading `NOTHING` (the grant ruling).
(b) "additional periods of three months, which shall not exceed 12 months in total": taken A, the further periods add up to at most 12 months (the function takes the months already extended); other reading B, the provisional validity is at most 12 months in all, counted from the withdrawal (nine months plus one three-month extension).
Text for B: point (b) of the first subparagraph requires the other notified body to complete its assessment "within 12 months of the withdrawal", which fits a total of 12 months from the withdrawal.
Text for A: "which" follows "additional periods of three months".
The question is for a lawyer; the answers differ for a second and later extension.
Authority for (a): none of the Guide's lines names the words "In the circumstances referred to in the first subparagraph".
I read them as a plain variant of "where" and answer as the periods ruling's rule (b) does (line 93: "a "where ..." condition: when it fails the answer is `JUST FALSE`").
The function is named for a power ("may"), so line 87 and the ruling of 2026-11-12 point to `NOTHING`, and that ruling's limit (3) (BRIEF.md) names "may" functions gated by "where", "when" or "upon" as "a question for a lawyer" and says to "leave the answer as the guide's rulings give it".
This site fits no line literally and is listed in Marginal readings (M-a7).

**F-37-4** (Article 37(4) second sentence, `Art 37(4) second sentence the Commission may suspend, restrict or withdraw the designation by means of an implementing act`; split site (ii)).
Taken: `JUST FALSE` where the Member State has not failed to take the corrective measures ("Where the Member State fails ... the Commission may ...": a "may" gated by "where", periods ruling rule (b)).
Other reading: `NOTHING` (the grant ruling).
Authority: the periods ruling's rule (b), ENCODING-GUIDE.md line 93: "a "where ..." condition: when it fails the answer is `JUST FALSE`"; the gate is the word "Where".
The function is named for a power ("may"), so line 87 and the ruling of 2026-11-12 point to `NOTHING`; that ruling's limit (3) (BRIEF.md) leaves "may" functions gated by "where" as "a question for a lawyer" and says to "leave the answer as the guide's rulings give it" (M-a7).

**F-39** (Article 39, `Art 39 the conformity assessment body of a third country may be authorised to carry out the activities of notified bodies`).
Taken: `NOTHING` where the proviso is not met ("provided that they meet the requirements laid down in Article 31 or they ensure an equivalent level of compliance"); the text does not say who authorises (F-passive).
Other reading: `JUST FALSE`.
Authority (ENCODING-GUIDE.md line 87): `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit", as applied by the ruling of 2026-11-12, limit (1), which BRIEF.md records: a function "NAMED for a grant or a power" ("may") that answers `JUST FALSE` because an "if" gate failed "reads as "may not", a grant turned into a bar". "Provided that" is a plain variant of "if" (line 86), which for a function not named for a power would answer `JUST FALSE`; the grant ruling is what decides it.

**F-AVII-44** (Annex VII point 4.4 first sentence, `Annex VII point 4.4 first sentence the notified body may require the provider to supply further evidence or carry out further tests`; split site (ii)).
Taken: `JUST FALSE` where the notified body is not examining the technical documentation ("In examining the technical documentation, the notified body may require ...").
Other reading: `NOTHING`.
Authority: none of the Guide's lines names "In examining".
I read it as a plain variant of "when" ("when examining the technical documentation"), which the delegated-definitions ruling's rule (c) (line 94) counts as "where": ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above", so rule (b) (line 93) gives `JUST FALSE`.
The function is named for a power ("may"), and line 87 and the ruling of 2026-11-12 point to `NOTHING` (limit (3): "a question for a lawyer").
This site fits no line literally and is listed in Marginal readings (M-a7).

**F-AVII-45** (Annex VII point 4.5 first sentence, `Annex VII point 4.5 first sentence the notified body has been granted access to the training and trained models`).
The conditions "where necessary", "after all other reasonable means to verify conformity have been exhausted and have proven to be insufficient" and "upon a reasoned request" are judgments of the notified body or the provider: plain inputs.
Taken: when one is not met the answer is `NOTHING` (F-unmet-where: a grant of access limited by its own wording).
Other reading: `JUST FALSE`, the access being a last resort.
Authority: line 95, "a duty whose "if" or "where" is unmet", left open (the function asks whether access "has been granted", a claim or duty, not a "may").
The gates "Where necessary" and "upon a reasoned request" are words of the periods ruling's rule (b) and of the delegated-definitions ruling's rule (c), which read literally would give `JUST FALSE`; `NOTHING` is my judgment, listed in Marginal readings (M-b1).

**F-AVII-53** (Annex VII point 5.3 second sentence, `Annex VII point 5.3 second sentence the notified body may carry out additional tests of the AI systems`; split site (ii)).
Taken: `JUST FALSE` where the tests are not in the context of the periodic audits ("In the context of those audits, the notified body may carry out additional tests").
Other reading: `NOTHING`.
Authority: none of the Guide's lines names "In the context of".
I read it as a plain variant of "when" ("when carrying out those audits"), which rule (c) (line 94) counts as "where", so rule (b) (line 93) gives `JUST FALSE`; the function is named for a power ("may"), and line 87 and the ruling of 2026-11-12 point to `NOTHING`.
This site fits no line literally and is listed in Marginal readings (M-a7).

**F-S14-reach** (seam S14, `Article 2(2)`; assumed, not ruled).
Question: which functions of my ranges are a provision of or about a high-risk AI system under Article 6(1) with Section B products, so that the keel's `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` can cut them off?
Taken: every function and every regulative rule of `P4-annex-vii.l4`, because Annex VII is the conformity assessment procedure of Article 43 for one high-risk AI system, and Article 43 is not among the provisions that Article 2(2) lets apply to such a system ("only Article 6(1), Article 60a and Articles 102 to 112 shall apply"; Articles 6(1), 102 to 109 and 112 as enacted).
Each asks the keel about the Article reference for Article 43 (number 43, letter "", paragraph 0), through `Annex VII Article 2(2) cuts Article 43 off from the AI system` in `P4-gate.l4`, after the keel's group test.
Where the keel answers `JUST FALSE` the function answers `JUST FALSE` and the rule reads "nothing is owed" (`FULFILLED`); where it answers `NOTHING` or `JUST TRUE` the function answers on its own provision (PLAN.md seam S14).
Each therefore takes two more inputs after the four of the keel's applicability function: the Section B flag and the integration flag (43 functions and 18 rules, all that take the four gate inputs).
Not taken: Articles 28 to 39 and Annex XIV, which concern notifying authorities and notified bodies, not a high-risk AI system as such, answer on their own provisions.
Article 34(1) is the one provision there that has a high-risk AI system as its object ("Notified bodies shall verify the conformity of high-risk AI systems in accordance with the conformity assessment procedures set out in Article 43"); I left it on its own provision because it binds notified bodies as a class and its function takes no single system's facts.
Other readings: (1) no part of Annex VII is cut off, because the Annex describes what a notified body does and Article 2(2) speaks of operators of such systems; (2) Article 34(1), and all of Chapter III Section 4, are cut off too, because "only ... shall apply" is a closed list and Articles 28 to 39 are not on it; (3) the Article reference to pass is not Article 43 but a reference to the Annex itself, which the keel's `Article reference` cannot name.
The keel's own reading of Article 2(2) as a closed list (`JUST FALSE` for a provision not on it) is its fork, not mine to reopen.


### Reading a result: FALSE and NOTHING (P4)

How to read an answer from a function of this part.
`JUST TRUE` is a yes on the facts given.
`JUST FALSE` is the text's own no, and only in these kinds of case: a "shall" that was not done (F-bare-shall); a flat negative, as in Article 28(5) ("shall offer or provide neither ... nor ...") and Article 31(5); a gate the text itself closes with "only" or "only where" (Article 30(1), Article 30(4), Article 33(3) first sentence, Annex XIV point 1 second sentence); an "unless" that is not met (Article 31(9)); a period the text fixes in its own words (the one year of Article 36(3), the nine months of Article 36(3) and of Article 36(9), the one month of Article 36(8)(a), the three months of Article 36(7)(b) and Article 36(8)(b), the five years of Article 33(4), the two weeks and two months of Article 30(4)); a "may" gated by "where", "when", "in the circumstances", "in examining" or "in the context of" (split site (ii), periods ruling rule (b)); a validity or a presumption gated by "where" that fails (Article 36(8), Article 36(9) first subparagraph, Article 32; F-36-where and F-32-where, periods ruling rule (b)); a code that is not on the list of Annex XIV (F-annex-xiv-closed); the provisions of Annex VII for a high-risk AI system under Article 6(1) with Section B products, which Article 2(2) lets only Article 6(1), Article 60a and Articles 102 to 112 reach (F-S14-reach; a rule reads `FULFILLED`).
Every one of these carries a `-- FALSE-kind (the text says no in its own words): "<the words>"` comment.

`NOTHING` is "the text does not answer this on these facts".
It is the answer in these cases, each with a `-- NOTHING-kind (<why>)` comment naming one of the six reasons (silent, list not closed, includes, undefined term, points outside the text, limited by its own wording):
- the date asked is before the group applies, or Annex VII does not apply to the AI system (before 2 August 2026, a system saved by Article 111(2), or the route is `Route neither`): limited by its own wording;
- a provision inserted by the Omnibus (Article 28(8) and (9), the second subparagraph of Article 29(4), Annex XIV) asked for a date on which the text as enacted was in force: silent;
- a duty whose "where", "if", "whenever" or "with the exception of" is not met (F-unmet-where);
- a grant ("may") with a named complement or a condition ("provided that", "on condition", "within the meaning of, and in accordance with"), where the case falls outside it (Article 28(2), Article 29(4) first subparagraph, Article 36(3) second sentence, Article 39);
- a list the text does not close with "only" (Article 36(8) circumstances (a) and (b); Article 36(9) first subparagraph);
- a scope limit with no "only" that the case falls outside (Article 32, "in so far as the applicable harmonised standards cover those requirements", when the "Where" holds: periods ruling rule (c));
- a term the text leaves undefined ("without delay", "as soon as possible", "immediately", "a reasonable period", "appropriate", "adequate"): not turned into a number, and a notification that includes both or neither kind of evidence in Article 30(4);
- another part's question (Article 17, Article 43(4), Article 78, Article 98(2), Annex IV, Chapter III Section 2): taken as an input fact, so the function asks it and does not answer it.

A regulative rule cannot answer `NOTHING`; before its group applies a rule answers `FULFILLED` ("nothing is owed").
A caller must never turn `NOTHING` into `FALSE`.
There is no `REFUSE` on the stable binary, so "not covered" is `NOTHING`, asserted in the tests.

**A limit of the rules.**
A regulative rule here starts from the event that triggers the duty: the caller supplies that event's date (for example the date of the suspension, in Article 36(8)(b)) and the rule says what is owed and by when.
The rule does not re-test the "where" conditions of its provision; the sibling function of the same provision does (and answers `NOTHING` when the condition is not met).
A caller who asks the rule when the "where" is not met will get a `BREACH` the text does not support.

## Jural relations (P4)

One row per provision that creates a relation; a provision that creates none is listed once as `none`.
The right-holder is "not named" where the text names no one (a duty owed to the Union's scheme, not to a person).
Each relation is stated once, neutrally.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | the relation | L4 rule or function |
| --- | --- | --- | --- | --- |
| Art 28(1) | not named | Member State | duty: designate or establish at least one notifying authority | rule `Art 28(1) the duty of the Member State to designate or establish a notifying authority` |
| Art 28(2) | Member State | not named | privilege: decide that assessment and monitoring are carried out by a national accreditation body | function `Art 28(2) the Member State may decide that the assessment and monitoring are carried out by a national accreditation body` |
| Art 28(3), (4), (7) | not named | notifying authority | duty (standing requirements: no conflict of interest, decisions taken by persons other than the assessors, enough competent personnel); no act to trace | functions `Art 28(3)`, `Art 28(4)`, `Art 28(7) first sentence`, `Art 28(7) second sentence` |
| Art 28(5) | not named | notifying authority | duty not to offer or provide an activity that conformity assessment bodies perform, and not to provide consultancy services on a commercial or competitive basis | the two bars `Art 28(5) the bar on ...` |
| Art 28(6) | not named | notifying authority | duty to safeguard the confidentiality of the information it obtains | rule `Art 28(6) the duty of the notifying authority to safeguard the confidentiality of the information` |
| Art 28(8) first subparagraph (as amended) | the conformity assessment body that applies under this Regulation and under Section A legislation | notifying authority responsible for Section A AI systems | duty to ensure the single application and unified assessment, and to cooperate | rule `Art 28(8) the duty of the notifying authority to ensure the single application and the unified assessment` |
| Art 28(8) second to fourth subparagraphs (as amended) | notified bodies already designated under Section A legislation; a body designated under several of them | not named (passive, F-passive) | claim of access to the single application and the unified procedure; immunity from applying more than once | functions only |
| Art 28(9) (as amended) | none | none | none: allocates which authority is the notifying authority for the single application (a status rule) | function `Art 28(9) the notifying authority is also the notifying authority for the single application and unified assessment procedure` |
| Art 29(1) | notifying authority of the Member State of establishment | conformity assessment body | duty to submit an application for notification | rule `Art 29(1) the duty of the conformity assessment body to submit an application for notification` |
| Art 29(2) | none | none | none: what the application must be accompanied by (content of a document, no act); the existing designations to be added | functions `Art 29(2) first subparagraph`, `Art 29(2) second subparagraph` |
| Art 29(3) | notifying authority | conformity assessment body that cannot provide an accreditation certificate | duty to provide the documentary evidence | rule `Art 29(3) the duty of the conformity assessment body to provide the documentary evidence` |
| Art 29(4) first subparagraph | notified body designated under other Union harmonisation legislation | not named | privilege: its documents and certificates may be used to support (as amended: and expedite) its designation | function `Art 29(4) first subparagraph the documents and certificates may be used` (both versions) |
| Art 29(4) second subparagraph (as amended) | notifying authority designated under the Section A legislation | notified body that undergoes the unified assessment | duty to submit the single application | rule `Art 29(4) the duty of the notified body to submit the single application` |
| Art 29(4) third subparagraph | authority responsible for notified bodies | notified body | duty to update the documentation whenever relevant changes occur | rule `Art 29(4) the duty of the notified body to update the documentation` |
| Art 30(1) | conformity assessment bodies that have not satisfied Article 31 | notifying authority | immunity from notification (the authority's disability: it may notify only bodies that have satisfied Article 31); the authority's power to notify the others | function `Art 30(1) the notifying authority may notify the conformity assessment body` |
| Art 30(2) | Commission and the other Member States | notifying authority | duty to notify each conformity assessment body (as amended: based on the Annex XIV list) | rule `Art 30(2) the duty of the notifying authority to notify the Commission and the other Member States` |
| Art 30(2) second subparagraph (as amended) | Commission | none named | power to amend Annex XIV by delegated act: inert, reason 2 (machinery) | none |
| Art 30(3) | Commission and the other Member States | notifying authority | content of the notification (first sentence); duty to provide documentary evidence where no accreditation certificate (second sentence) | function `Art 30(3) first sentence`; rule `Art 30(3) the duty of the notifying authority to provide the documentary evidence` |
| Art 30(4) | conformity assessment body | Commission and the other Member States (their power to object) | privilege to perform the activities of a notified body, only where no objection is raised in the period; power of objection | function `Art 30(4) the conformity assessment body may perform the activities of a notified body` |
| Art 30(5) | Member State concerned and the conformity assessment body | Commission | duty to consult, to decide whether the authorisation is justified, and to address the decision | rules `Art 30(5) the duty of the Commission to enter into consultations`, `Art 30(5) the duty of the Commission to decide whether the authorisation is justified`, `Art 30(5) the duty of the Commission to address its decision` |
| Art 31(1) to (4), (6) to (8), (10), (11) | not named | notified body | duty (standing requirements on its status, capacity, independence, procedures and competence); no act to trace | functions of `P4-art-31-32` |
| Art 31(4) third sentence | notified body (and, for personal purposes, its personnel) | not named | the independence requirement does not preclude the use of assessed high-risk AI systems needed for its operations or for personal purposes | function `Art 31(4) third sentence the independence requirement precludes the use of the assessed high-risk AI system` |
| Art 31(5) | not named | conformity assessment body, its top-level management and its personnel | duty not to be directly involved in design, development, marketing or use of high-risk AI systems, nor to represent the parties, nor to engage in conflicting activity | function `Art 31(5) the conformity assessment body, its management and its personnel have kept to the bar on involvement and conflicting activity` |
| Art 31(6), (9), (12) | not named | notified body | duty to document and implement an impartiality structure (6); to take out liability insurance unless the Member State assumes the liability (9); to participate in coordination activities (12) | rules `Art 31(6) ...`, `Art 31(9) ...`, `Art 31(12) ...` |
| Art 32 | conformity assessment body that demonstrates conformity with the published harmonised standards | not named | presumption: it is presumed to comply with the Article 31 requirements the standards cover | function `Art 32 the conformity assessment body is presumed to comply with the requirement set out in Article 31` |
| Art 33(1) | notifying authority | notified body that subcontracts or has recourse to a subsidiary | duty to ensure the subcontractor or subsidiary meets Article 31 and to inform the notifying authority | rules `Art 33(1) the duty of the notified body to ensure that the subcontractor or the subsidiary meets the requirements`, `Art 33(1) the duty of the notified body to inform the notifying authority` |
| Art 33(2) | not named | notified body | duty (liability): full responsibility for the tasks of subcontractors and subsidiaries | function `Art 33(2) the notified body takes full responsibility for the tasks performed by subcontractors and subsidiaries` |
| Art 33(3) | the provider | notified body | power of consent of the provider, with the notified body's disability to subcontract or use a subsidiary without it; duty of the notified body to publish the list of its subsidiaries | function `Art 33(3) first sentence the activities may be subcontracted or carried out by a subsidiary`; rule `Art 33(3) the duty of the notified body to make a list of its subsidiaries publicly available` |
| Art 33(4) | notifying authority | not named (passive, F-passive) | documents on the assessment of the subcontractor or subsidiary kept at its disposal for five years | function `Art 33(4) the five years from the termination date of the subcontracting are running` |
| Art 34(1), (3) | notifying authority (3); not named (1) | notified body | duty to verify conformity under Article 43 (1); to make documentation available on request (3) | rules `Art 34(1) the duty of the notified body to verify the conformity of high-risk AI systems`, `Art 34(3) the duty of the notified body to make available and submit the documentation upon request` |
| Art 34(2) | providers | notified body | duty to avoid unnecessary burdens and to take account of size, sector, structure and complexity | functions `Art 34(2) first sentence ...`, `Art 34(2) second sentence ...` |
| Art 35(1), (2) | not named (the public, for the list) | Commission | duty to assign a single identification number; to make the list public; to keep it up to date | rules `Art 35(1) ...`, two rules `Art 35(2) ...` |
| Art 36(1) | Commission and the other Member States | notifying authority | duty to notify any relevant change via the electronic notification tool | rule `Art 36(1) the duty of the notifying authority to notify the relevant change` |
| Art 36(2) | none | none | none: says which procedures apply to which change (a routing rule) | function `Art 36(2) the procedures that apply to the change to the notification` |
| Art 36(3) | notifying authority and the providers concerned | notified body that ceases its activities | duty to inform as soon as possible and one year ahead of a planned cessation; privilege of its certificates to stay valid nine months on a condition; duty of the successor to complete a full assessment; duty of the notifying authority to withdraw the designation | rules `Art 36(3) the duty of the notified body to inform the notifying authority and the providers of a planned cessation`, `Art 36(3) the duty of the notifying authority to withdraw the designation`; functions `Art 36(3) second sentence ...`, `Art 36(3) third sentence ...` |
| Art 36(4) | notified body concerned; Commission and the other Member States | notifying authority | duty to investigate, to inform the notified body of the objections, to restrict, suspend or withdraw, and to inform the Commission | four rules `Art 36(4) the duty ...` |
| Art 36(5) | providers concerned | notified body whose designation has been suspended, restricted or withdrawn | duty to inform within 10 days | rule `Art 36(5) the duty of the notified body to inform the providers concerned within 10 days` |
| Art 36(6) | notifying authorities in other Member States and market surveillance authorities | notifying authority | duty to keep the files and make them available at their request | rule `Art 36(6) the duty of the notifying authority to take appropriate steps to keep the files` |
| Art 36(7)(a) to (e) | Commission, the other Member States and the national competent authorities | notifying authority; the national competent authority (e) | duties to assess the impact on certificates, to report within three months, to require suspension or withdrawal of unduly issued certificates within a reasonable period, to inform the Commission and the Member States, and to inform the national competent authorities; measures by the national competent authority | rules `Art 36(7)(a) ...`, `(b) ...`, `(c) ...`, `(d) ...`, `(e) ...` |
| Art 36(8) | notified body whose certificates are affected; providers | notifying authority (confirmations); provider (written confirmation within three months) | conditions on which certificates stay valid after a suspension or restriction; duty of the provider to confirm in writing | functions `Art 36(8)(a)`, `Art 36(8)(b)`, `Art 36(8) the certificates remain valid ...`; rule `Art 36(8)(b) the duty of the provider to confirm in writing within three months` |
| Art 36(9) | providers and holders of certificates | national competent authority; notified body assuming the functions | privilege of certificates to remain valid nine months; power of the national competent authority to extend by three-month periods; duty to inform immediately | function `Art 36(9) first subparagraph ...`, `Art 36(9) second subparagraph ...`; rule `Art 36(9) the duty of the national competent authority to inform the Commission, the Member States and the other notified bodies` |
| Art 37(1) to (3) | not named | Commission (1), (3); notifying authority (2) | duty to investigate doubts about a notified body's competence; to provide information on request; to treat sensitive information confidentially | rules `Art 37(1) ...`, `Art 37(2) ...`, `Art 37(3) ...` |
| Art 37(4) | notifying Member State | Commission | duty to inform the Member State and request corrective measures; power to suspend, restrict or withdraw the designation by implementing act where the Member State fails | rule `Art 37(4) the duty of the Commission to inform the notifying Member State and request the corrective measures`; function `Art 37(4) second sentence the Commission may suspend, restrict or withdraw the designation by means of an implementing act` |
| Art 38(1) to (3) | not named | Commission (1), (3); notifying authority (2) | duty to put in place a sectoral group; to ensure the notified bodies participate; to provide for exchange of knowledge | rules `Art 38(1) ...`, `Art 38(2) ...`, `Art 38(3) ...` |
| Art 39 | conformity assessment bodies of a third country with an agreement with the Union | not named (passive: who authorises is not said) | power to be authorised to carry out the activities of notified bodies, provided Article 31 is met or an equivalent level is ensured | function `Art 39 the conformity assessment body of a third country may be authorised to carry out the activities of notified bodies` |
| Annex VII points 1, 2 | none | none | none: introduction and overview of the procedure | functions `Annex VII point 1`, `Annex VII point 2 ...` |
| Annex VII points 3.1, 4.2 | none | none | none: what an application must include (the content of a document, no act) | the limb functions and the two combiners of `P4-annex-vii` |
| Annex VII points 3.2, 3.4, 4.3, 4.4, 4.6, 5.3 | provider, or its authorised representative (notifications) | notified body | duties to assess, examine, notify, issue or refuse the certificate with reasons, carry out tests itself, audit periodically; power to require further evidence or tests and to carry out additional tests | rules and functions of `P4-annex-vii` |
| Annex VII points 3.3, 3.4, 4.1, 4.7, 5.2 | notified body | provider | duties to maintain the approved system, to bring changes to the notified body's attention, to apply for the technical-documentation assessment, to inform of changes, to allow access to the premises and share information | rules of `P4-annex-vii` |
| Annex VII points 4.3 second sentence, 4.5 | notified body | not named (passive, F-passive) | claim to full access to the training, validation and testing data sets; to the training and trained models as a last resort | functions only |
| Annex VII point 5.1 | none | none | none: states the purpose of the surveillance; inert, reason 1 | none |
| Annex XIV points 1, 4 | notifying authority | conformity assessment body | duty to use the Annex's codes when specifying the types of AI systems in an application; the designation scope is limited to the codes it names | rule `Annex XIV point 4 the duty of the conformity assessment body to use the lists of codes`; function `Annex XIV point 1 second sentence the conformity assessment body may carry out the conformity assessment` |
| Annex XIV points 2, 3 | none | none | none: a table of codes, categories and types | table `Annex XIV table` and the lookup functions |

## Marginal readings for a lawyer (P4)

Every branch that rests on reading (a) (a failed "if" counts as the text's no, within the provision that holds the "if"; flat negatives count as the text saying no) or on reading (b) (a prohibition or grant limited by its own wording does not).
The counts below are computed from the `-- FALSE-kind` and `-- NOTHING-kind` comments in the modules; the line numbers are those of the files as they are in this folder, and the command that finds them again is in each heading.

### Reading (a): a failed condition, or a flat negative, counts as the text saying no

**M-a1. A "shall" not done is `JUST FALSE` (F-bare-shall): 107 branches.**
Other reading: `NOTHING`, because the text does not say what follows from a duty not done.
Find them again: `grep -n 'FALSE-kind.*bare "shall" not done' P4-*.l4`.
Lines: `P4-art-28.l4`: 12, 40, 83, 98, 151, 175, 188, 212, 228, 268; `P4-art-29-30.l4`: 49, 82, 96, 112, 175, 219, 258, 272, 318, 331, 390, 407; `P4-art-31-32.l4`: 35, 49, 62, 79, 128, 155, 173, 216, 234, 253; `P4-art-33-35.l4`: 52, 87, 110, 152, 166, 202, 212, 227, 252, 283; `P4-art-36.l4`: 57, 108, 158, 171, 198, 214, 227, 240, 336, 364, 419, 435, 451, 465, 630; `P4-art-37-39.l4`: 47, 74, 99, 127, 165, 179, 206, 230; `P4-annex-vii.l4`: 84, 99, 122, 139, 156, 176, 193, 210, 227, 249, 266, 283, 312, 334, 356, 376, 393, 419, 435, 452, 470, 483, 503, 525, 566, 591, 611, 630, 647, 668, 696, 719, 744, 789, 812, 834, 857, 883, 907, 922, 939; `P4-annex-xiv.l4`: 357.

**M-a2. A flat negative is `JUST FALSE` when the prohibited act is done:** the two bars of Article 28(5) ("shall offer or provide neither ... nor ..."; the rules reach `BREACH`) and Article 31(5) ("shall not engage in").
Other reading: none that differs; a flat negative is the text's own no.

**M-a3. A gate the text closes with "only" is `JUST FALSE` when it fails:** Article 30(1) ("may notify only conformity assessment bodies which have satisfied"), Article 30(4) ("only where no objections are raised"), Article 33(3) first sentence ("only with the agreement of the provider"), Annex XIV point 1 second sentence ("Only conformity assessment bodies that have been designated").
Other reading: `NOTHING` (a power limited by its own wording); the Guide's own rule gives `JUST FALSE` for "only", so this is listed for completeness.

**M-a4. An "unless" that is met counts as the duty met (F-31-9):** Article 31(9). Other reading: `NOTHING` where the exception applies.

**M-a5. A period the text fixes in its own words: outside it the answer is `JUST FALSE` (periods ruling, rule (a)):** `P4-art-29-30.l4`: 374; `P4-art-33-35.l4`: 139, 152; `P4-art-36.l4`: 110, 143, 158, 304, 383, 534, 552, 602, 617.
Provisions: Article 30(4) two weeks and two months (also M-a3); Article 33(4) five years; Article 36(3) one year and nine months; Article 36(9) first subparagraph nine months; Article 36(8)(a) one month and (b) three months; Article 36(7)(b) three months.
Other reading: `NOTHING`, because the text limits a grant by a stated period and the case falls outside it (the Guide's "In short" sentence names "a stated period"); the periods ruling of 2026-11-05 rule (a) settles it as `JUST FALSE`, so this is the Guide's answer, listed because it is a marginal reading.

**M-a6. A code that is not on the Annex XIV list is `JUST FALSE` (F-annex-xiv-closed):** the function `Annex XIV points 2 and 3 the code is on the list` and the functions that call it. Other reading: `NOTHING` (a bare list with no hand-off).

**M-a7. A "may" gated by "where", "when", "in the circumstances", "in examining" or "in the context of" is `JUST FALSE` when the gate fails (split site (ii), periods ruling rule (b)):** four sites, listed under Split sites with the authority each relies on. Other reading: `NOTHING` (the grant ruling, line 87).
Only Article 37(4) second sentence has the Guide's own word "Where". The other three (Article 36(9) second subparagraph, "In the circumstances referred to in the first subparagraph"; Annex VII point 4.4 first sentence, "In examining"; Annex VII point 5.3 second sentence, "In the context of") fit no line of the Guide literally: I read them as plain variants of "where" or "when" (lines 93 and 94), which the ruling of 2026-11-12, limit (3), calls "a question for a lawyer".

**M-a8. A validity or a presumption gated by "where" is `JUST FALSE` when the gate fails (F-36-where, F-32-where):** Article 36(8), "where a designation has been suspended or restricted"; Article 36(9) first subparagraph, "where a designation has been withdrawn"; Article 32, "Where a conformity assessment body demonstrates its conformity ... the references of which have been published". The periods ruling's rule (b) (line 93) gives `JUST FALSE`; none is a duty or a "may". Other reading: `NOTHING` (the text limits the validity or the presumption in its own wording, line 87). These three are the answers changed in the follow-ups of 2026-11-17: the first pass answered `NOTHING`.

### Reading (b): a prohibition or grant limited by its own wording does not

**M-b1. A duty whose "where", "if", "whenever", "in the event" or "with the exception of" is unmet is `NOTHING` (F-unmet-where): 52 branches.**
Other reading: `JUST FALSE`, the periods ruling's rule (b) for a "where" and reading (a) for an "if". The Guide leaves this question to the encoder case by case (ENCODING-GUIDE.md line 95, "Questions with no convention"); the authority and the counts are in the fork entry.
By the gate word the branches quote: 21 quote "where" (Art 28(7) second sentence, Art 28(8) as amended first subparagraph, Art 29(3), Art 30(3) second sentence, Art 30(5) first sentence, Art 30(5) second and third sentences, Art 33(1), Art 36(3) first sentence, Art 36(3) fourth sentence, Art 36(4) first sentence, Art 36(4) second sentence, Art 36(5), Art 36(7)(e), Art 37(1), Art 37(4) first sentence, Annex VII point 4.3 second sentence, Annex VII point 4.4 second sentence, Annex VII point 4.5 first sentence, Annex VII point 4.6 second paragraph first sentence, Annex VII point 4.6 fourth paragraph, Annex VII point 4.6 fifth paragraph first sentence); 5 quote "when", "upon", "whenever" or "on request" (Art 28(8) as amended second subparagraph, Art 29(4) third subparagraph, Art 34(3), Art 37(2), Annex XIV as amended point 4); 7 quote "if" or "in the event of"; 19 quote none of these words (the subject of the sentence has not arisen). The first two groups, 26 branches, are the ones where the periods ruling's rule (b) and the delegated-definitions ruling's rule (c), read literally, give `JUST FALSE`; they fit no line of the Guide literally, because line 95 names "a duty whose "if" or "where" is unmet" as left open.
Find them again: `grep -n 'NOTHING-kind.*fork F-unmet-where' P4-*.l4`.
Lines: `P4-art-28.l4`: 187, 213, 229; `P4-art-29-30.l4`: 95, 111, 176, 218, 330, 389, 404; `P4-art-33-35.l4`: 50, 226; `P4-art-36.l4`: 55, 106, 170, 197, 212, 226, 239, 302, 334, 363, 381, 417, 434, 450, 464, 629; `P4-art-37-39.l4`: 46, 73, 126; `P4-annex-vii.l4`: 308, 333, 354, 375, 417, 524, 565, 590, 610, 667, 692, 717, 741, 765, 787, 811, 833, 855, 880, 906; `P4-annex-xiv.l4`: 355.

**M-b2. A grant limited by a named complement or a condition is `NOTHING` where the case falls outside it (the grant ruling of 2026-11-12, limit (1)):** Article 28(2) (F-28-2), Article 29(4) first subparagraph in both versions (F-29-4), Article 36(3) second sentence (F-36-3), Article 39 (F-39). Other reading: `JUST FALSE`. Authority: ENCODING-GUIDE.md line 87 ("limits a grant or prohibition in its own wording and the case falls outside the limit") and the ruling of 2026-11-12 (BRIEF.md).

**M-b3. A list the text does not close with "only" is `NOTHING` when no item holds:** Article 36(8) circumstances (a) and (b) (F-36-8) and Article 36(9) first subparagraph (a) and (b). Other reading: `JUST FALSE`.

**M-b4. "With the exception of certificates unduly issued" is `NOTHING` for such a certificate (F-36-unduly):** two sites, Article 36(8) and Article 36(9) first subparagraph. Other reading: `JUST FALSE`.

**M-b5. The date before the group applies, and the Annex VII group not applying to the system, is `NOTHING`:** the keel's reading (F-111-2-nothing), not mine to change.

**M-b6. A term the text leaves undefined is not turned into a number:** "without delay" (Articles 30(5), 36(4)), "as soon as possible" (Article 36(3)), "immediately" (Articles 36(4), 36(9)), "within a reasonable period of time determined by the notifying authority" (Article 36(7)(c)), "periodic" (Annex VII point 5.3). The rules carry no deadline for these, so they have no breach path.

**M-b7. A scope limit with no "only" is `NOTHING` outside the scope (the periods ruling's rule (c)):** Article 32, "in so far as the applicable harmonised standards cover those requirements" (F-32-where), where the "Where" holds and the standards do not cover the requirement. Other reading: `JUST FALSE` ("in so far as" read as a condition, line 86).

### Reading (c): which provisions Article 2(2) reaches

**M-c1. Annex VII is cut off, for a high-risk AI system under Article 6(1) with Section B products, by Article 2(2) (F-S14-reach, assumed, not ruled).** Taken: every function and rule of `P4-annex-vii.l4` asks the keel and answers `JUST FALSE` (rules: `FULFILLED`) where the keel says Article 43 is not among the provisions that apply. Other readings: none of Annex VII is cut off (it describes what a notified body does); or Article 34(1) and the rest of Articles 28 to 39 are cut off too (a closed "only" list that does not name them). I did not call the keel from Articles 28 to 39 or Annex XIV, whose provisions concern notifying authorities and notified bodies, not a high-risk AI system as such.

## Split sites (P4)

(i) **An unmet element of an infringement: 0 sites.**
No provision of my ranges names an infringement of the Regulation with elements (the prohibited practices, the fines and the infringements are in other parts).
The two bars that have two limbs (Article 28(5), Article 31(5)) are standing bars on an authority and on a conformity assessment body; an element not met there means the bar is kept, which is `JUST TRUE`, so nothing is split.
F-28-5 is the one reading choice about the elements of such a bar.

(ii) **A "may" gated by "where", "when", "upon", "on application", "with the consent of" and the like.**
Four sites, all answered `JUST FALSE` (the periods ruling's rule (b), ENCODING-GUIDE.md line 93); the other reading is `NOTHING` (the grant ruling of 2026-11-12 and line 87).
One site has the Guide's own word "Where"; the other three have a gate that no line of the Guide names, so each says so in its fork entry and is listed in Marginal readings (M-a7):

| provision | function | the gate | answer taken | fork line | authority |
| --- | --- | --- | --- | --- | --- |
| Art 36(9) second subparagraph | `Art 36(9) second subparagraph the national competent authority may extend the provisional validity by a further three months` | "In the circumstances referred to in the first subparagraph" | JUST FALSE | F-36-9 | no line names these words; read as a plain variant of "where" or "when" (line 93 rule (b), line 94 rule (c)); fits no line literally, so also in Marginal readings |
| Art 37(4) second sentence | `Art 37(4) second sentence the Commission may suspend, restrict or withdraw the designation by means of an implementing act` | "Where the Member State fails to take the necessary corrective measures" | JUST FALSE | F-37-4 | line 93, rule (b), literally: "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| Annex VII point 4.4 first sentence | `Annex VII point 4.4 first sentence the notified body may require the provider to supply further evidence or carry out further tests` | "In examining the technical documentation" | JUST FALSE | F-AVII-44 | no line names these words; read as a plain variant of "where" or "when" (line 93 rule (b), line 94 rule (c)); fits no line literally, so also in Marginal readings |
| Annex VII point 5.3 second sentence | `Annex VII point 5.3 second sentence the notified body may carry out additional tests of the AI systems` | "In the context of those audits" | JUST FALSE | F-AVII-53 | no line names these words; read as a plain variant of "where" or "when" (line 93 rule (b), line 94 rule (c)); fits no line literally, so also in Marginal readings |

(ii-b) **A presumption or a validity gated by "where", which is not a duty and not a "may": three sites, answered `JUST FALSE` when the "where" fails (rule (b), line 93): Article 32 (fork F-32-where), Article 36(8) and Article 36(9) first subparagraph (fork F-36-where).**
The first pass answered `NOTHING` at all three; see Follow-up passes 1 and 2 above.
Article 32 keeps `NOTHING` for "in so far as the applicable harmonised standards cover those requirements", a scope limit with no "only" (rule (c)).
The sites of this shape that I looked for in Articles 28 to 39 and Annexes VII and XIV (a presumption, a deeming or applying rule, a validity or a status, with a gate of "where", "when" or "upon") and what I did with each:

| site | shape | gate | what I did |
| --- | --- | --- | --- |
| Art 32 | presumption | "Where a conformity assessment body demonstrates ... the references of which have been published"; "in so far as the applicable harmonised standards cover those requirements" | changed: `JUST FALSE` where the "Where" fails (rule (b)); `NOTHING` for "in so far as" (rule (c)); F-32-where |
| Art 36(8) | validity | "where a designation has been suspended or restricted" | `JUST FALSE` where it fails (rule (b)), changed in follow-up 1; F-36-where |
| Art 36(9) first subparagraph | validity | "where a designation has been withdrawn" | `JUST FALSE` where it fails (rule (b)), changed in follow-up 1; F-36-where |
| Art 28(8) third subparagraph, second sentence (as amended) | effect ("shall be applicable") | a relative clause, "for which the conformity assessment body is designated"; no "where", "when" or "upon" | left: `NOTHING`, a scope limit with no "only" (rule (c)); the rule gives the answer, so no fork line |
| Art 28(9) (as amended) | status ("is also the notifying authority") | a relative clause, "that has been designated"; "unless"; no "where", "when" or "upon" | left: not of this shape |
| Art 36(2) | rule of application ("shall apply to extensions of the scope") | no "where", "when" or "upon" | left: not of this shape |
| Annex VII point 4.5, second sentence | limit ("Such access shall be subject to ...") | the anaphor "Such access", which refers to the first sentence's gated access; no "where", "when" or "upon" of its own | left: `NOTHING` where no access was granted (line 87, "is silent"), already under F-unmet-where |
| Annex VII point 4.6, fifth paragraph, first sentence | statement of necessity ("re-training ... will be needed") | "Where the AI system does not meet the requirement relating to the data used to train it" | left, borderline: read as a requirement on the provider, so a duty whose "where" is unmet (line 95): `NOTHING`, F-unmet-where, in M-b1 |

Every other "where", "when" or "upon" gate in my ranges whose failure answers `NOTHING` is on a duty (F-unmet-where, 52 branches) or on a "may" (the grant sites); I found it by listing every `NOTHING-kind` comment that quotes such a word, tagged or not, and none of the others is on a presumption, a deeming rule or a validity.

Not split sites, listed so the count is checkable: the "may" gated by "only where" or "only with" is closed by the text itself, so `JUST FALSE` follows the Guide's own rule (Article 30(1), Article 30(4), Article 33(3) first sentence, Annex XIV point 1 second sentence); and the "may" gated by "provided that", "on condition", "within the meaning of, and in accordance with" or a named complement is a grant limited by its own wording, so `NOTHING` follows line 87 ("limits a grant or prohibition in its own wording and the case falls outside the limit") and the grant ruling of 2026-11-12 limit (1) (Article 28(2), Article 29(4) first subparagraph, Article 36(3) second sentence, Article 39; forks F-28-2, F-29-4, F-36-3, F-39).
The duties whose "where" or "if" is unmet (F-unmet-where, 52 branches) are a further kind of split site: the Guide's line 95 names them as open, decided "site by site" with a fork line, so the entry names that line and says what the rulings would give if read literally.
There is no "entitled"-named function in my ranges (the word does not occur in them).

(iii) **A group not yet applicable, or an AI system saved by Article 111(2): `NOTHING`, the keel's reading, not mine to change.**
43 functions of `P4-annex-vii.l4` pass the placement date, the route and the change flag to the keel's applicability function (through `Annex VII the group of Article 43 applies to the AI system on the date asked`), and each can answer `NOTHING` because the group does not yet apply on the date asked, or because Article 111(2) saves the system.
They also pass the Section B flag and the integration flag to the keel's `Art 2(2) ...` (through `Annex VII Article 2(2) cuts Article 43 off from the AI system`), and answer `JUST FALSE` where Article 2(2) cuts Article 43 off from the system (fork F-S14-reach, assumed, not ruled).
The other 18 rules of the same module take the same inputs and answer `FULFILLED` ("nothing is owed") in that case and where Article 2(2) cuts Article 43 off, since a regulative rule has no `NOTHING` and no `JUST FALSE`.
No function of Articles 28 to 39 or of Annex XIV passes a placement date: they are not about one AI system, so they pass the keel's two constants for "no AI system in question" and `FALSE`, and Article 111(2) saves nothing for their group (`P4-gate.l4`).
The seat files repeat the route, the placement date and the change flag in 90 questions across the three seats (every Annex VII question, the applicability questions of Annex VII included), and the two Article 2(2) inputs in 87 of them (the 3 applicability questions do not ask them).
The keel's fork line is F-111-2-nothing in the keel's `NOTES.md`: for a saved system the text's own "only if" could make the saved case `JUST FALSE`; the keel keeps `NOTHING`, and so does every function of this part.
I did not decide the question again.

## Rules with no breach path (P4)

A rule is listed here if it is a `MUST` with no time limit and no stated consequence, so no trace can show it breached: a late action reads `FULFILLED`.
There are 67 regulative rules in layer 1; 61 are listed here and the other 6 reach `BREACH` in at least one trace (listed after the table).
Open-textured time words ("without delay", "immediately", "as soon as possible", "a reasonable period") are not turned into numbers, and no consequence is invented where the text states none.
The 18 rules of `P4-annex-vii.l4` and the rule of Annex XIV point 4 are all here: the Annex states no period for any of them.

| provision | party | modal and act | rule |
| --- | --- | --- | --- |
| Art 28(1) | `Art 28 Member State` | MUST `Art 28(1) designate or establish at least one notifying authority` | `Art 28(1) the duty of the Member State to designate or establish a notifying authority` (P4-art-28.l4) |
| Art 28(6) | `Art 28 notifying authority` | MUST `Art 28(6) safeguard the confidentiality of the information obtained` | `Art 28(6) the duty of the notifying authority to safeguard the confidentiality of the information` (P4-art-28.l4) |
| Art 28(8) | `Art 28 notifying authority` | MUST `Art 28(8) ensure the single application and the unified assessment procedure` | `Art 28(8) the duty of the notifying authority to ensure the single application and the unified assessment` (P4-art-28.l4) |
| Art 29(1) | `Art 29 conformity assessment body` | MUST `Art 29(1) submit an application for notification to the notifying authority of the Member State in which the body is established` | `Art 29(1) the duty of the conformity assessment body to submit an application for notification` (P4-art-29-30.l4) |
| Art 29(3) | `Art 29 conformity assessment body` | MUST `Art 29(3) provide the notifying authority with all the documentary evidence necessary` | `Art 29(3) the duty of the conformity assessment body to provide the documentary evidence` (P4-art-29-30.l4) |
| Art 29(4) | `Art 29 notified body` | MUST `Art 29(4) submit the single application for assessment to the notifying authority designated pursuant to the Union harmonisation legislation` | `Art 29(4) the duty of the notified body to submit the single application` (P4-art-29-30.l4) |
| Art 29(4) | `Art 29 notified body` | MUST `Art 29(4) update the documentation whenever relevant changes occur` | `Art 29(4) the duty of the notified body to update the documentation` (P4-art-29-30.l4) |
| Art 30(2) | `Art 30 notifying authority` | MUST `Art 30(2) notify the Commission and the other Member States of each conformity assessment body` | `Art 30(2) the duty of the notifying authority to notify the Commission and the other Member States` (P4-art-29-30.l4) |
| Art 30(3) | `Art 30 notifying authority` | MUST `Art 30(3) provide the Commission and the other Member States with documentary evidence` | `Art 30(3) the duty of the notifying authority to provide the documentary evidence` (P4-art-29-30.l4) |
| Art 30(5) | `Art 30 Commission` | MUST `Art 30(5) enter into consultations with the relevant Member States and the conformity assessment body` | `Art 30(5) the duty of the Commission to enter into consultations` (P4-art-29-30.l4) |
| Art 30(5) | `Art 30 Commission` | MUST `Art 30(5) decide whether the authorisation is justified` | `Art 30(5) the duty of the Commission to decide whether the authorisation is justified` (P4-art-29-30.l4) |
| Art 30(5) | `Art 30 Commission` | MUST `Art 30(5) address the decision to the Member State concerned and to the relevant conformity assessment body` | `Art 30(5) the duty of the Commission to address its decision` (P4-art-29-30.l4) |
| Art 31(6) | `Art 31 notified body` | MUST `Art 31(6) document and implement a structure and procedures to safeguard impartiality` | `Art 31(6) the duty of the notified body to document and implement a structure and procedures` (P4-art-31-32.l4) |
| Art 31(9) | `Art 31 notified body` | MUST `Art 31(9) take out appropriate liability insurance for the conformity assessment activities` | `Art 31(9) the duty of the notified body to take out liability insurance` (P4-art-31-32.l4) |
| Art 31(12) | `Art 31 notified body` | MUST `Art 31(12) participate in coordination activities as referred to in Article 38` | `Art 31(12) the duty of the notified body to participate in coordination activities` (P4-art-31-32.l4) |
| Art 33(1) | `Art 33 notified body` | MUST `Art 33(1) ensure that the subcontractor or the subsidiary meets the requirements laid down in Article 31` | `Art 33(1) the duty of the notified body to ensure that the subcontractor or the subsidiary meets the requirements` (P4-art-33-35.l4) |
| Art 33(1) | `Art 33 notified body` | MUST `Art 33(1) inform the notifying authority of the subcontracting or the recourse to a subsidiary` | `Art 33(1) the duty of the notified body to inform the notifying authority` (P4-art-33-35.l4) |
| Art 33(3) | `Art 33 notified body` | MUST `Art 33(3) make a list of its subsidiaries publicly available` | `Art 33(3) the duty of the notified body to make a list of its subsidiaries publicly available` (P4-art-33-35.l4) |
| Art 34(1) | `Art 34 notified body` | MUST `Art 34(1) verify the conformity of high-risk AI systems in accordance with the conformity assessment procedures set out in Article 43` | `Art 34(1) the duty of the notified body to verify the conformity of high-risk AI systems` (P4-art-33-35.l4) |
| Art 34(3) | `Art 34 notified body` | MUST `Art 34(3) make available and submit upon request all relevant documentation to the notifying authority` | `Art 34(3) the duty of the notified body to make available and submit the documentation upon request` (P4-art-33-35.l4) |
| Art 35(1) | `Art 35 Commission` | MUST `Art 35(1) assign a single identification number to each notified body` | `Art 35(1) the duty of the Commission to assign a single identification number` (P4-art-33-35.l4) |
| Art 35(2) | `Art 35 Commission` | MUST `Art 35(2) make publicly available the list of the bodies notified under this Regulation` | `Art 35(2) the duty of the Commission to make the list publicly available` (P4-art-33-35.l4) |
| Art 35(2) | `Art 35 Commission` | MUST `Art 35(2) keep the list up to date` | `Art 35(2) the duty of the Commission to keep the list up to date` (P4-art-33-35.l4) |
| Art 36(1) | `Art 36 notifying authority` | MUST `Art 36(1) notify the Commission and the other Member States of the relevant change via the electronic notification tool` | `Art 36(1) the duty of the notifying authority to notify the relevant change` (P4-art-36.l4) |
| Art 36(3) | `Art 36 notifying authority` | MUST `Art 36(3) withdraw the designation of the notified body that has ceased its activity` | `Art 36(3) the duty of the notifying authority to withdraw the designation` (P4-art-36.l4) |
| Art 36(4) | `Art 36 notifying authority` | MUST `Art 36(4) investigate the matter with the utmost diligence` | `Art 36(4) the duty of the notifying authority to investigate the matter` (P4-art-36.l4) |
| Art 36(4) | `Art 36 notifying authority` | MUST `Art 36(4) inform the notified body of the objections and give it the possibility to make its views known` | `Art 36(4) the duty of the notifying authority to inform the notified body of the objections` (P4-art-36.l4) |
| Art 36(4) | `Art 36 notifying authority` | MUST `Art 36(4) restrict, suspend or withdraw the designation` | `Art 36(4) the duty of the notifying authority to restrict, suspend or withdraw the designation` (P4-art-36.l4) |
| Art 36(4) | `Art 36 notifying authority` | MUST `Art 36(4) inform the Commission and the other Member States of the measure` | `Art 36(4) the duty of the notifying authority to inform the Commission and the other Member States` (P4-art-36.l4) |
| Art 36(6) | `Art 36 notifying authority` | MUST `Art 36(6) take appropriate steps to ensure that the files of the notified body are kept and made available` | `Art 36(6) the duty of the notifying authority to take appropriate steps to keep the files` (P4-art-36.l4) |
| Art 36(7)(a) | `Art 36 notifying authority` | MUST `Art 36(7)(a) assess the impact on the certificates issued by the notified body` | `Art 36(7)(a) the duty of the notifying authority to assess the impact on the certificates` (P4-art-36.l4) |
| Art 36(7)(c) | `Art 36 notifying authority` | MUST `Art 36(7)(c) require the notified body to suspend or withdraw the certificates which were unduly issued` | `Art 36(7)(c) the duty of the notifying authority to require the suspension or withdrawal of the certificates unduly issued` (P4-art-36.l4) |
| Art 36(7)(d) | `Art 36 notifying authority` | MUST `Art 36(7)(d) inform the Commission and the Member States about the certificates the suspension or withdrawal of which it has required` | `Art 36(7)(d) the duty of the notifying authority to inform the Commission and the Member States about the certificates` (P4-art-36.l4) |
| Art 36(7)(e) | `Art 36 notifying authority` | MUST `Art 36(7)(e) provide the national competent authorities with all relevant information about the certificates` | `Art 36(7)(e) the duty of the notifying authority to provide the national competent authorities with the information` (P4-art-36.l4) |
| Art 36(9) | `Art 36 national competent authority` | MUST `Art 36(9) inform the Commission, the other Member States and the other notified bodies of the change of designation` | `Art 36(9) the duty of the national competent authority to inform the Commission, the Member States and the other notified bodies` (P4-art-36.l4) |
| Art 37(1) | `Art 37 Commission` | MUST `Art 37(1) investigate the cases where there are reasons to doubt the competence of a notified body` | `Art 37(1) the duty of the Commission to investigate` (P4-art-37-39.l4) |
| Art 37(2) | `Art 37 notifying authority` | MUST `Art 37(2) provide the Commission, on request, with all relevant information` | `Art 37(2) the duty of the notifying authority to provide the Commission with the information on request` (P4-art-37-39.l4) |
| Art 37(3) | `Art 37 Commission` | MUST `Art 37(3) treat the sensitive information obtained in the course of its investigations confidentially` | `Art 37(3) the duty of the Commission to treat the sensitive information confidentially` (P4-art-37-39.l4) |
| Art 37(4) | `Art 37 Commission` | MUST `Art 37(4) inform the notifying Member State and request it to take the necessary corrective measures` | `Art 37(4) the duty of the Commission to inform the notifying Member State and request the corrective measures` (P4-art-37-39.l4) |
| Art 38(1) | `Art 38 Commission` | MUST `Art 38(1) put in place and properly operate coordination and cooperation in the form of a sectoral group` | `Art 38(1) the duty of the Commission to ensure the coordination and cooperation` (P4-art-37-39.l4) |
| Art 38(2) | `Art 38 notifying authority` | MUST `Art 38(2) ensure that the bodies notified by it participate in the work of the group` | `Art 38(2) the duty of the notifying authority to ensure that the notified bodies participate` (P4-art-37-39.l4) |
| Art 38(3) | `Art 38 Commission` | MUST `Art 38(3) provide for the exchange of knowledge and best practices between notifying authorities` | `Art 38(3) the duty of the Commission to provide for the exchange of knowledge and best practices` (P4-art-37-39.l4) |
| Annex VII point 3.2 | `Annex VII notified body` | MUST `Annex VII 3.2 assess the quality management system and determine whether it satisfies the requirements referred to in Article 17` | `Annex VII point 3.2 the duty of the notified body to assess the quality management system and determine whether it satisfies Article 17` (P4-annex-vii.l4) |
| Annex VII point 3.2 | `Annex VII notified body` | MUST `Annex VII 3.2 notify the decision to the provider or its authorised representative` | `Annex VII point 3.2 the duty of the notified body to notify the decision` (P4-annex-vii.l4) |
| Annex VII point 3.3 | `Annex VII provider` | MUST `Annex VII 3.3 continue to implement and maintain the approved quality management system` | `Annex VII point 3.3 the duty of the provider to continue to implement and maintain the approved quality management system` (P4-annex-vii.l4) |
| Annex VII point 3.4 | `Annex VII provider` | MUST `Annex VII 3.4 bring the intended change to the attention of the notified body` | `Annex VII point 3.4 the duty of the provider to bring the intended change to the attention of the notified body` (P4-annex-vii.l4) |
| Annex VII point 3.4 | `Annex VII notified body` | MUST `Annex VII 3.4 examine the proposed changes and decide whether a reassessment is necessary` | `Annex VII point 3.4 the duty of the notified body to examine the proposed changes and decide` (P4-annex-vii.l4) |
| Annex VII point 3.4 | `Annex VII notified body` | MUST `Annex VII 3.4 notify the provider of its decision on the changes` | `Annex VII point 3.4 the duty of the notified body to notify the provider of its decision on the changes` (P4-annex-vii.l4) |
| Annex VII point 4.1 | `Annex VII provider` | MUST `Annex VII 4.1 lodge an application for the assessment of the technical documentation with a notified body of the provider's choice` | `Annex VII point 4.1 the duty of the provider to lodge the application for the assessment of the technical documentation` (P4-annex-vii.l4) |
| Annex VII point 4.3 | `Annex VII notified body` | MUST `Annex VII 4.3 examine the technical documentation` | `Annex VII point 4.3 the duty of the notified body to examine the technical documentation` (P4-annex-vii.l4) |
| Annex VII point 4.4 | `Annex VII notified body` | MUST `Annex VII 4.4 itself directly carry out adequate tests` | `Annex VII point 4.4 the duty of the notified body to carry out adequate tests itself` (P4-annex-vii.l4) |
| Annex VII point 4.6 | `Annex VII notified body` | MUST `Annex VII 4.6 notify the decision to the provider or its authorised representative` | `Annex VII point 4.6 the duty of the notified body to notify the decision` (P4-annex-vii.l4) |
| Annex VII point 4.6 | `Annex VII notified body` | MUST `Annex VII 4.6 issue a Union technical documentation assessment certificate` | `Annex VII point 4.6 the duty of the notified body to issue the certificate` (P4-annex-vii.l4) |
| Annex VII point 4.6 | `Annex VII notified body` | MUST `Annex VII 4.6 refuse to issue a Union technical documentation assessment certificate and inform the applicant accordingly, giving detailed reasons` | `Annex VII point 4.6 the duty of the notified body to refuse the certificate and inform the applicant` (P4-annex-vii.l4) |
| Annex VII point 4.7 | `Annex VII provider` | MUST `Annex VII 4.7 inform the notified body of the intended change or of the occurrence of such a change` | `Annex VII point 4.7 the duty of the provider to inform the notified body of the change` (P4-annex-vii.l4) |
| Annex VII point 4.7 | `Annex VII notified body` | MUST `Annex VII 4.7 assess the changes and decide whether they require a new conformity assessment` | `Annex VII point 4.7 the duty of the notified body to assess the changes and decide` (P4-annex-vii.l4) |
| Annex VII point 4.7 | `Annex VII notified body` | MUST `Annex VII 4.7 assess the changes, notify the provider of its decision and, where the changes are approved, issue a supplement` | `Annex VII point 4.7 the duty of the notified body to assess the changes, notify the provider and issue a supplement` (P4-annex-vii.l4) |
| Annex VII point 5.2 | `Annex VII provider` | MUST `Annex VII 5.2 allow the notified body to access the premises where the design, development and testing of the AI systems is taking place` | `Annex VII point 5.2 the duty of the provider to allow the notified body to access the premises` (P4-annex-vii.l4) |
| Annex VII point 5.2 | `Annex VII provider` | MUST `Annex VII 5.2 share with the notified body all necessary information` | `Annex VII point 5.2 the duty of the provider to share all necessary information with the notified body` (P4-annex-vii.l4) |
| Annex VII point 5.3 | `Annex VII notified body` | MUST `Annex VII 5.3 carry out periodic audits and provide the provider with an audit report` | `Annex VII point 5.3 the duty of the notified body to carry out periodic audits and provide an audit report` (P4-annex-vii.l4) |
| Annex XIV point 4 | `Annex XIV conformity assessment body` | MUST `Annex XIV 4 use the lists of codes, categories and corresponding types of AI systems when specifying the types of AI systems in the application for designation` | `Annex XIV point 4 the duty of the conformity assessment body to use the lists of codes` (P4-annex-xiv.l4) |

The rules that reach `BREACH` (a trace of each ends in `BREACH`, run on both builds): 

| provision | party | modal and act | rule | time limit or consequence |
| --- | --- | --- | --- | --- |
| Art 28(5) | `Art 28 notifying authority` | SHANT `Art 28(5) offer or provide an activity that conformity assessment bodies perform` | `Art 28(5) the bar on the notifying authority offering or providing an activity that conformity assessment bodies perform` | a flat prohibition: the forbidden act reaches `BREACH` |
| Art 28(5) | `Art 28 notifying authority` | SHANT `Art 28(5) offer or provide consultancy services on a commercial or competitive basis` | `Art 28(5) the bar on the notifying authority offering or providing consultancy services on a commercial or competitive basis` | a flat prohibition: the forbidden act reaches `BREACH` |
| Art 36(3) | `Art 36 notified body` | MUST `Art 36(3) inform the notifying authority and the providers concerned of the planned cessation` | `Art 36(3) the duty of the notified body to inform the notifying authority and the providers of a planned cessation` | a stated period: a missed deadline reaches `BREACH` |
| Art 36(5) | `Art 36 notified body` | MUST `Art 36(5) inform the providers concerned` | `Art 36(5) the duty of the notified body to inform the providers concerned within 10 days` | a stated period: a missed deadline reaches `BREACH` |
| Art 36(7)(b) | `Art 36 notifying authority` | MUST `Art 36(7)(b) submit a report on its findings to the Commission and the other Member States` | `Art 36(7)(b) the duty of the notifying authority to submit the report within three months` | a stated period: a missed deadline reaches `BREACH` |
| Art 36(8)(b) | `Art 36 provider` | MUST `Art 36(8)(b) confirm in writing that another qualified notified body is temporarily assuming the functions` | `Art 36(8)(b) the duty of the provider to confirm in writing within three months` | a stated period: a missed deadline reaches `BREACH` |

## Seams (P4)

A part cannot import another part, so a question that belongs to another part is taken as an input fact, named for the provision it comes from.
The first six rows are PLAN.md section 4's seams as they touch my ranges; the rest are seams the plan does not list.

| seam | asking provision | answering provision | the input as taken | in PLAN.md section 4? |
| --- | --- | --- | --- | --- |
| S1 | Annex VII (every function and rule of `P4-annex-vii.l4`): the AI systems the procedure applies to | Article 6 with Annexes I and III (P1) | `the route by which the AI system is high-risk` (`Route to high-risk`), passed to the keel's `Art 113 the provision group applies` through `Annex VII the group of Article 43 applies to the AI system on the date asked`: `Route neither` gives `NOTHING` | yes, as the plan gives it |
| S13 | Annex VII | Articles 111 and 113 (keel) | `the date asked`, `the date the AI system was placed on the market or put into service`, `the AI system has been significantly changed in its design since the date of application of Chapter III` (in 61 functions and rules of `P4-annex-vii.l4`, with the two inputs of S14 after them); Articles 28 to 39 and Annex XIV take `the date asked` only and pass the core's constants for "no AI system in question" | yes |
| S2 | the role questions of the seat layer | Article 3 (keel) | none: `Art 3(22) the body is a notified body`, `Art 3(3) the party is a provider` and `Art 3(5) the party is an authorised representative` are called by the role questions; the layer-1 modules use their own party types and do not call the Art 3 functions | yes |
| S6 (provided to others) | Article 16 (P3), Article 71 (P7) | Articles 43, 47, 48, 49 (P5) | not mine: my ranges neither ask nor answer the completion of the conformity assessment procedure; Annex VII describes the procedure | yes (S6 is asked of P5) |
| S8 | Annex VII point 4.6 second paragraph (issue the certificate) and fourth paragraph (refuse it): the notified body's judgment that the AI system is, or is not, in conformity with Chapter III Section 2 | Articles 8 to 15 (P2) | `the AI system is in conformity with the requirements set out in Chapter III, Section 2` (`BOOLEAN`, in 2 functions); the plan's name for it is `the high-risk AI system complies with the requirements set out in Chapter III, Section 2`; the wording here follows the Annex's own words, so the lead must wire the two names at the merge | yes, under a different name |
| S14 | Annex VII (every function and rule of `P4-annex-vii.l4`: the procedure of Article 43 for one high-risk AI system) | Article 2(2) (keel, `aia-scope.l4`) | `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products`, asked about the Article reference for Article 43 through `Annex VII Article 2(2) cuts Article 43 off from the AI system`; two inputs more than the four of S13: `the products are covered by Union harmonisation legislation listed in Section B of Annex I` and `the requirements for high-risk AI systems under this Regulation have been integrated in that Union harmonisation legislation` (BOOLEAN). Where the keel answers `JUST FALSE` the function answers `JUST FALSE` and the rule `FULFILLED`; otherwise it answers on its own provision (fork F-S14-reach, assumed, not ruled). Not taken for Articles 28 to 39 and Annex XIV: they concern notifying authorities and notified bodies, not a high-risk AI system as such; Article 34(1) is the one with a high-risk AI system as its object and stays on its own provision | yes, as the plan gives it |
| S15 | none of my provisions | Article 2(13) (keel) | not taken: nothing in my ranges is limited by Article 2(13), which speaks of the requirements and obligations of Articles 9 to 15 and 17 to 25 | n/a |
| S-17 | Annex VII point 3.1(d) and 3.2 (the documentation of the quality management system covers all the aspects Article 17 lists; the notified body determines whether the system satisfies Article 17) | Article 17 (P3) | `that documentation covers all the aspects listed under Article 17` and `the notified body has determined whether the quality management system satisfies the requirements referred to in Article 17` (`BOOLEAN`) | no: not in the plan |
| S-43 | Annex VII point 3.4 and 4.7 (Article 43(4): a new conformity assessment or a supplement); Article 34(1) (the procedures of Article 43); Annex VII as a whole (which points apply to Section A products, Article 43(3)) | Article 43 (P5) | `the notified body has decided whether those changes require a new conformity assessment in accordance with Article 43(4) or whether they could be addressed by means of a supplement` and `the notified body has verified the conformity of the high-risk AI system in accordance with the conformity assessment procedures set out in Article 43` (`BOOLEAN`); Annex VII's applicability to a system is Article 43's question and is not encoded | no |
| S-IV | Annex VII point 4.2(c) | Annex IV (P2) | `the application for the assessment of the technical documentation includes the technical documentation referred to in Annex IV` (`BOOLEAN`) | no |
| S-78 | Articles 28(6), 31(7), 37(3) (confidentiality "in accordance with Article 78") | Article 78 (P8) | `the notifying authority safeguards the confidentiality of the information that it obtains, in accordance with Article 78`, the notified-body counterpart and `the Commission treats all sensitive information ... confidentially in accordance with Article 78` (`BOOLEAN`) | no |
| S-98 | Article 37(4) third sentence (the implementing act adopted by the examination procedure of Article 98(2)) | Article 98 (P9) | `the implementing act has been adopted in accordance with the examination procedure referred to in Article 98(2)` (`BOOLEAN`) | no |
| S-Annex-I-A | Articles 28(8), 28(9), 29(4) (Union harmonisation legislation listed in Section A of Annex I) | Annex I (P1) | plain `BOOLEAN` facts, for example `the notified body is designated pursuant to the Union harmonisation legislation listed in Section A of Annex I` | no: the Annex is not asked, the fact is |
| S-Art-97 | Article 30(2) second subparagraph (delegated acts under Article 97) | Article 97 (P9) | none: inert, reason 2 (machinery) | no |

## Versions (P4)

One row per `▼M1` passage of my ranges (`AMENDMENTS.md` lists them).
Annex VII carries no `▼M1` marker: the Omnibus did not change it, so it has one text.
The dispatchers choose between the two versions with the keel's `Omnibus Art 4 the version in force` (cut on 27 July 2026); each version's text is kept in its own function so that the old text can be tested on its own, because the as-enacted branch of a dispatcher can be dead behind the group gate.

| consolidated lines | provision | what the Omnibus changed | encoded | why |
| --- | --- | --- | --- | --- |
| 540-544 (`▼M1 INSERTED`, marker at 539) | Article 28(8) (four subparagraphs) and 28(9) | inserted: the single application and unified assessment procedure for bodies designated also under Section A legislation; the authority for that procedure | as amended only: `Art 28(8) as amended ...` and `Art 28(9) as amended ...`, each behind a dispatcher that answers `NOTHING` (silent) on a date when the text as enacted was in force, and the rule answers `FULFILLED` | the passage did not exist before the Omnibus, so there is no text as enacted to encode |
| 553-555 (`▼M1 REPLACED`, marker at 552) | Article 29(4) | first subparagraph: "designated under" became "designated pursuant to" and "support" became "support and expedite"; second subparagraph inserted (the single application by notified bodies under Section A legislation); third subparagraph (the duty to update the documentation) unchanged in substance | first subparagraph: both versions (`Art 29(4) as enacted first sentence ...`, `Art 29(4) as amended first subparagraph ...`; same answer on the facts, F-29-4); second subparagraph: as amended only; third subparagraph: one text (the rule is the same in both versions) | the first subparagraph exists in both versions and the wording differs; the second did not exist before; the third reads the same |
| 561-562 (`▼M1 REPLACED`, marker at 560) | Article 30(2) | first paragraph: notification now "based on the list of codes, categories, and corresponding types of AI systems referred to in Annex XIV"; second paragraph inserted (the Commission's power to amend Annex XIV by delegated act) | first paragraph: both versions (`Art 30(2) as enacted ...`, `Art 30(2) as amended first subparagraph ...`; the as-amended function takes the Annex XIV basis as an input); second paragraph: inert, reason 2 (machinery: a rule-making power) | the first paragraph differs on whether the notification is "based on the Annex XIV list"; the second is a delegated-act power that affects no one now |
| 1959-2021 (`▼M1 INSERTED`, marker at 1958; my range ends at line 2010) | Annex XIV | inserted: the whole Annex, a table of 22 codes, categories and types of AI systems for the notification procedure of Article 30 | as amended only (`Annex XIV as amended ...` behind dispatchers that answer `NOTHING` before 27 July 2026) | the Annex did not exist before the Omnibus |

## Seats (P4)

Layer 2 is one pair of files per seat that my ranges address: `P4-seat-<slug>.l4` (the questions) and `P4-cases-seat-<slug>.l4` (the cases).
A seat module imports the layer-1 modules and the keel's; each question is `@export`ed with an `@desc` on every input, takes the facts that seat could state as plain inputs, and calls the layer-1 function; no rule is restated.
The names begin `Under Article N, as <role phrase>, ...` (`Under Annex N point M, as ...` for the Annexes); the questions sit under `§` headings in the text's order.

| seat | questions | of which role | of which applicability | of which asked of a layer-1 function or built from its facts | case asserts | mirror cases |
| --- | --- | --- | --- | --- | --- | --- |
| notified body (`notified`) | 119 | 1 | 2 | 116 | 636 | 9 |
| provider of an AI system (`provider`) | 50 | 1 | 2 | 47 | 301 | 9 |
| authorised representative (`rep`) | 5 | 1 | 1 | 3 | 37 | 3 |
| total | 174 | | | | 974 | 21 |

**Seats with no files, and why.**
- *a person affected by an AI system* (`person`): no provision of my ranges addresses an affected person, so there is no person seat; Articles 28 to 39 and Annexes VII and XIV address Member States, notifying authorities, conformity assessment bodies, notified bodies, the Commission, providers and (once) authorised representatives.
- *deployer, importer, distributor, product manufacturer, provider of a general-purpose AI model* (`deployer`, `importer`, `distributor`, `manufacturer`, `gpai`): no provision of my ranges addresses them; Annex VII speaks of the provider and of its authorised representative only.
- There is never a seat for the Commission, a notifying authority, a national competent authority or any other official: their powers and duties appear only in layer 1, and in layer 2 only as what they mean to a notified body, a provider or an authorised representative (for example, "has the notifying authority been informed of my cessation", asked of the notified body).

**Questions asked from each seat.**
- The notified body is asked about Articles 28(8) (as a body designated also under Section A legislation), 29 to 36 (its application, notification, requirements, subcontracting, operational duties, number and changes to its notification), 37(3) and (4), 38(2), 39, Annex VII (as the assessor) and Annex XIV (as the body that specifies the types of AI systems in an application).
- The provider is asked about Article 33(3) (whether the notified body's activities may be subcontracted), Article 36(3), (5), (8) and (9) (what a cessation, suspension, restriction or withdrawal means for its certificates and for the notice it is owed), and Annex VII (its application under points 3.1 and 4.2, the notices, the access of points 4.3 and 4.5, the premises of point 5.2, and the further evidence and tests the notified body may require).
- The authorised representative is asked about the points of Annex VII where the text names it: the application it lodges (point 3.1(a)) and the notification of a decision to the provider or to it (points 3.2 and 4.6), besides its role question and the applicability of Annex VII.

**Role questions.**
Each seat has one role question that asks, once, the facts that make a person that role, and calls the keel's own definition: `Art 3(22) the body is a notified body`, `Art 3(3) the party is a provider`, `Art 3(5) the party is an authorised representative`; the other questions of the seat do not re-ask them.

**Applicability questions.**
One question per group and seat asks whether the group applies on the date asked: `Notified bodies, GPAI, governance, penalties and Art 78` (the date asked only; for the notified body and the provider) and `General` for Annex VII (the date asked, the route, the placement date and the change flag; all three seats).

**Mirror cases (Guide section 3).**
The same facts are asked from both seats of a relation, with answers that agree, and each such case is marked `-- MIRROR` in the case files (9 in the notified-body file, 9 in the provider file, 3 in the representative file; each case is repeated in the file of every seat it is asked from):
- Article 36(5): the notified body tells the providers within 10 days of a suspension on 1 September 2025.
- Article 33(3): activities may be subcontracted only with the provider's agreement.
- Annex VII point 3.4: the provider brings an intended change to the notified body's attention.
- Annex VII point 4.6: the notified body issues the certificate where the AI system is in conformity.
- Annex VII point 4.7: the provider informs the notified body of a change to the AI system.
- Annex VII point 5.2: the provider allows the notified body to access the premises.
- Annex VII point 3.2: the decision is notified to the provider or its authorised representative (notified body, provider, authorised representative).
- Annex VII point 4.6: the decision of the notified body is notified to the provider or its authorised representative (notified body, provider, authorised representative).
- Annex VII point 3.1(a): the application names the provider and, where an authorised representative lodges it, the representative (notified body, provider, authorised representative).

**Seat audit.**
Seat audit (second pass): 174 questions read, 3 retitled (direction 0, subject 3)
First pass: I listed every seat question beside the layer-1 function it calls and checked that the name asks the question the body answers, in the same direction and about the same subject; I found none that differs.
Second pass (2026-11-17): I read every question name and `@export` text again, beside the function its body calls, in all three seat files, for a direction mismatch (a permission asked where the function answers a bar or an exception, or the reverse) and a subject mismatch ("have I" against "has the notified body", "does the authority" against a duty of the provider). I found no direction mismatch and three subject mismatches, retitled (the question name and its `@export` text; the inputs and their `@desc` do not mention the subject and are unchanged), with every case assertion that names the question restated in place with `-- RECONCILED 2026-11-17`:
- was `Under Article 39, as a notified body, may I be authorised to carry out the activities of notified bodies?`; now `Under Article 39, as a notified body, may a conformity assessment body of a third country be authorised to carry out the activities of notified bodies?`.
- was `Under Annex VII point 4.6, as a provider of an AI system, has the notified body refused to issue the certificate and informed me, giving detailed reasons?`; now `Under Annex VII point 4.6, as a provider of an AI system, has the notified body refused to issue the certificate and informed the applicant, giving detailed reasons?`.
- was `Under Annex VII point 4.6, as a provider of an AI system, have I re-trained the AI system before the application for a new conformity assessment?`; now `Under Annex VII point 4.6, as a provider of an AI system, has my AI system been re-trained before the application for a new conformity assessment?`.
The three differ from their first titles only in who the question is about: the function of Article 39 is about a conformity assessment body of a third country, not about the notified body that asks; the two functions of Annex VII point 4.6 say that the applicant was informed and that the AI system has been re-trained, not that the asker was informed or re-trained it.
The notified-body twins of those two questions ("have I refused to issue the certificate and informed the applicant, giving detailed reasons"; "has the AI system been re-trained before the application for a new conformity assessment") already asked what their functions answer and are unchanged.
The questions that restate a function in the first person ("have I informed ...", "has my decision been notified ...") are the function's own direction.
The "may" questions ask the permission (`JUST TRUE` is "yes, I may"): Article 33(3) ("may the activities ... be subcontracted"), Article 36(3) and 36(9), Annex VII points 4.4 and 5.3.
The bar of Article 31(5) is asked as the bar kept ("have my body, its top-level management and its personnel kept to the bar"), never negated; the bars of Article 28(5) bind a notifying authority and have no seat question.

**Layer-1 functions with no seat question: 28.**
- 20 address only an official (the Member State, a notifying authority, the Commission or a national competent authority): Article 28(1) to (9) and the like, Article 36(4), (6), (7)(a) (b) (d) (e), Article 37(1) and (2), Article 38(3). Layer 2 has no seat for an official.
- 5 are covered by a custom question built from the facts: Article 36(8) with its circumstances (a) and (b), and the Annex VII combiners of points 3.1 and 4.2 (notified body and provider; not offered to the authorised representative).
- 2 take a list of codes as an input: Annex XIV point 1 third sentence and point 4. The brief asks for plain inputs, and a list of codes is not one fact a person states. A probe on 1.6.110 shows that `l4 check` accepts an `@export` question with a list input, so this is my choice, not a limit of the binary; a reviewer who wants these two questions can add them to `P4-seat-notified.l4`.
- 1 is a combiner over the other answers of its Article (`Art 31 the notified body has satisfied the requirements given the answers of the paragraphs`), whose inputs are `MAYBE BOOLEAN` answers, not facts a person states.

## What the text turns out to say (numbered findings)

1. **Article 36(8)(b) starts the provider's clock at the suspension, not at the authority's finding.** The provider "shall confirm in writing ... within three months of the suspension or restriction" where the notifying authority "determines that the notified body does not have the capability"; the clock is the suspension or restriction itself, so a late finding by the authority leaves the provider less than three months. The rule takes the date of the suspension as its only clock (tested in `P4-tests-art-36.l4`: for a suspension on 1 December 2025 the three months end on 1 March 2026, 90 days later; confirming on day 90 fulfils the duty and on day 91 it breaches).
2. **Article 36(9) has two twelves and a nine.** The first subparagraph keeps certificates valid for nine months; point (b) lets the other notified body take twelve months from the withdrawal to complete its assessment; the second subparagraph lets the national competent authority extend "for additional periods of three months, which shall not exceed 12 months in total". Whether the twelve months are the total validity or the sum of the extensions is not settled by the words (F-36-9).
3. **Annex XIV exists only in the text as amended.** Article 30(2) as enacted tells the notifying authority to notify "using the electronic notification tool" with no list; the Omnibus adds "based on the list of codes ... referred to in Annex XIV" and inserts the Annex. For a date from 2 August 2025 to 26 July 2026 the Annex is not in the text, and its functions answer `NOTHING` (asserted); from 27 July 2026 they answer from the table of 22 codes.
4. **Article 30(4) gives a period for two kinds of notification and none for the others.** Two weeks for a notification that includes an accreditation certificate, two months for one that includes documentary evidence; a notification that includes both, or neither, has no period, and the function answers `NOTHING` (undefined term).
5. **Annex VII names no one to grant the access of points 4.3 and 4.5.** "The notified body shall be granted full access" and "shall also be granted access" are passive (F-passive); there is no rule that the provider must grant it. Article 28(8) second subparagraph ("shall also be made available"), Article 33(4) ("shall be kept at the disposal") and Article 39 ("may be authorised") are passive in the same way.
6. **Annex VII gives the provider no period to inform the notified body.** Point 3.4 ("brought to the attention of the notified body") and point 4.7 ("shall inform such notified body of the intended change or of the occurrence of such a change") set no time limit, so the provider's duties have no breach path; the same is true of every Annex VII rule.
7. **Only 6 of the 67 regulative rules can be breached.** Two prohibitions (Article 28(5)) and four duties with a stated period (Article 36(3) one year before a planned cessation, Article 36(5) 10 days, Article 36(7)(b) three months, Article 36(8)(b) three months); every other duty reads `FULFILLED` however late the act, because the text states no time limit and no consequence (see Rules with no breach path).
8. **"Without delay", "immediately", "as soon as possible" and "a reasonable period" are everywhere in Articles 30, 36 and 37 and none is a number.** They are undefined terms; the functions do not invent a number, and the rules that use them carry no deadline.
9. **The three Article 36 notice duties run from different events.** Article 36(5) (10 days) runs from the suspension, restriction or withdrawal; Article 36(7)(b) (three months) from the notifying authority's own notification of the changes; Article 36(3) (one year) backwards from the date the notified body ceases. The fixed-period functions take each start date as an input rather than deriving it.
10. **Article 28(8) and (9), the second subparagraph of Article 29(4) and Annex XIV are new law from 27 July 2026.** Before that date their functions answer `NOTHING` (silent: the text as enacted has no such provision) and their rules read `FULFILLED` (nothing is owed); both are asserted.
11. **The Annex VII group follows Article 43.** The Annex carries no date of its own; it applies from 2 August 2026 (the group `General`) and a high-risk AI system placed on the market earlier and not significantly changed is saved by Article 111(2) (assumed, not ruled).
12. **The rules do not carry their "where" gates.** The sibling function answers whether the "where" holds; the rule starts after it (see Reading a result, "A limit of the rules").

## What the text does not answer (P4)

- Whether a month or a year is counted by the library's calendar arithmetic or in days (F-months).
- Whether the 12 months of Article 36(9) second subparagraph are the total provisional validity or the sum of the extensions (F-36-9).
- What "without delay", "as soon as possible", "immediately", "a reasonable period of time", "periodic", "appropriate" and "adequate" mean in days; no function turns them into a number.
- Who must grant the access of Annex VII points 4.3 and 4.5, who must make the single application available (Article 28(8)), who must keep the documents of Article 33(4), and who authorises a third-country body (Article 39) (F-passive).
- The period after which a Member State "fails" to take corrective measures (Article 37(4)).
- Whether a notification that includes both or neither kind of evidence has an objection period (Article 30(4)).
- Which points of Annex VII apply to the high-risk AI systems of Section A of Annex I (Article 43(3), another part's question), and whether Annex VII is the procedure that applies to a given system.
- Whether the group of Annex VII and of Annex XIV is the group of the Article that gives it effect (assumed, not ruled).
- What the text says about a body that is not a notified body but performs the activities of one before the period of Article 30(4) has run: only that it "may perform ... only where no objections are raised"; no penalty or consequence is stated in my ranges (the penalties are Article 99, another part's).

## What the stable binary does not accept (and what was met)

The binary governs where the skills say otherwise.
Met in this part (each cost an error or a wrong answer here):

Silent (a wrong answer with no error):
1. `IF NOT a OR NOT b` evaluated wrongly, and three assertions in Article 36(7)(c) to (e) failed, until every `NOT` was parenthesised: `IF (NOT a) OR (NOT b)`. This is the trap PLAN.md section 5 names (`NOT a AND b` parses as `NOT (a AND b)`).

Loud (an error):
2. No `ELEM` (as an infix or as `elem`) and no `LENGTH` or `length` were found by the binary: Annex XIV tests the code list with `any (GIVEN c YIELD c EQUALS x) list`, and the test counts rows with a recursive helper.

Known from the skills and PLAN.md and designed around without being met:
3. No `REFUSE`: "not covered" is `NOTHING` or a constructor.
4. `AFTER ... WITHIN` is rejected: every deadline is computed as `WITHIN (Day <end>) MINUS (Day <start>)`.
5. An input named in a `MUST` action degrades on the main build: none of my rules names an input in its action (the actions are constructors), and every trace was run on both builds and compared.
6. A trace outcome is invisible to `check.sh`: every `#TRACE` has an `-- EXPECT` comment, and `traces.py` compared both builds.
7. A name defined in two imported modules cannot be used: every top-level name and every declared constructor here begins with its provision's label (`Art 36 notifying authority`, `Annex VII notified body`, ...).

Probed and found to work: an `@export` question with a list input (`l4 check` on 1.6.110 accepts it); see Seats for why two such questions are not offered.

## What `check.sh` prints

The baseline, run on the four keel modules alone before any P4 file existed (the numbers this run replaced):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
aia-annex-x.l4                                 0         0       0        0         0 |      0         0       0        0  same
aia-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
aia-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
aia-timeline.l4                                0         0       0        0         0 |      0         0       0        0  same
TOTAL (4 modules)                              0         0       0        0           |      0         0       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

The final run, `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` in this folder, exit code 0:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
aia-annex-x.l4                                 0         0       0        0         0 |      0         0       0        0  same
aia-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
aia-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
aia-scope.l4                                   0         0       0        0         0 |      0         0       0        0  same
aia-timeline.l4                                0         0       0        0         0 |      0         0       0        0  same
P4-annex-vii.l4                                0         0       0        0         0 |      0         0       0        0  same
P4-annex-xiv.l4                                0         0       0        0         0 |      0         0       0        0  same
P4-art-28.l4                                   0         0       0        0         0 |      0         0       0        0  same
P4-art-29-30.l4                                0         0       0        0         0 |      0         0       0        0  same
P4-art-31-32.l4                                0         0       0        0         0 |      0         0       0        0  same
P4-art-33-35.l4                                0         0       0        0         0 |      0         0       0        0  same
P4-art-36.l4                                   0         0       0        0         0 |      0         0       0        0  same
P4-art-37-39.l4                                0         0       0        0         0 |      0         0       0        0  same
P4-cases-seat-notified.l4                      0       636       0        0         0 |      0       636       0        0  same
P4-cases-seat-provider.l4                      0       301       0        0         0 |      0       301       0        0  same
P4-cases-seat-rep.l4                           0        37       0        0         0 |      0        37       0        0  same
P4-gate.l4                                     0         0       0        0         0 |      0         0       0        0  same
P4-seat-notified.l4                            0         0       0        0         0 |      0         0       0        0  same
P4-seat-provider.l4                            0         0       0        0         0 |      0         0       0        0  same
P4-seat-rep.l4                                 0         0       0        0         0 |      0         0       0        0  same
P4-tests-annex-vii.l4                          0       254       0        0         0 |      0       254       0        0  same
P4-tests-annex-xiv.l4                          0        69       0        0         0 |      0        69       0        0  same
P4-tests-art-28.l4                             0       101       0        0         0 |      0       101       0        0  same
P4-tests-art-29-30.l4                          0        96       0        0         0 |      0        96       0        0  same
P4-tests-art-31-32.l4                          0        79       0        0         0 |      0        79       0        0  same
P4-tests-art-33-35.l4                          0        56       0        0         0 |      0        56       0        0  same
P4-tests-art-36.l4                             0       127       0        0         0 |      0       127       0        0  same
P4-tests-art-37-39.l4                          0        44       0        0         0 |      0        44       0        0  same
TOTAL (28 modules)                             0      1800       0        0           |      0      1800       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Reading it: 0 errors, 0 failed, 0 refused; the main build reads every module the same way (every row says `same`); 1800 assertions satisfied in the P4 test and case files (the keel's four modules carry none).
