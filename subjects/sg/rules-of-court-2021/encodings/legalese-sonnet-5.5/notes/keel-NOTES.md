# NOTES.md -- Rules of Court 2021 (Singapore): the keel (`roc-core`, `roc-definitions`)

Written by the keel agent, 2026-11-05.

**Status of this file.**
Measured today: `check.sh` over the three `.l4` modules (numbers below), and `srcrefs.py check --refs` and `--strict` over them (0 problems each).
Read from the text by the keel: Order 1 (lines 8 to 136) end to end, Order 3 whole, Order 4 rules 1 and 2, Orders 6 and 7, Order 20, Order 25 rules 1 to 5, the First Schedule's paragraphs 1 to 3, the Second Schedule heading (lines 7761 to 7763), the Fourth Schedule's Part headings (lines 7788, 8452, 8561, 8715, 8765), the opening of the Table of Derivations (lines 8830 to 8845), and the individual lines `PLAN.md` quotes from O 28, O 33, O 46A, O 53, O 59 and O 62.
Not read by the keel: the rest of Orders 2 to 70.
For those, `PLAN.md` has the rule headings (`RULE-INDEX.md`, built by script) and the cross-Order citations (the Appendix, built by script), and says which statement is which.
Proposed, not landed: every statement in `PLAN.md` about what a part will do, and every seam input there that no part has yet answered.

**The text is a plain-text rendering, not the official text.**
`inputs/SOURCES.md` records it: made by a converter script from Singapore Statutes Online (`https://sso.agc.gov.sg/SL/SCJA1969-S914-2021`, retrieved 2026-11-05, "Current version as at 05 Nov 2026"), sha256 `e15654bfc58bce54611d88534846a5fa1b29af43aa811abfcc2ac9e738e2143d`, with the caveat "SSO reproduces an unofficial consolidation; the text is tag-stripped HTML, so tables and forms lose their layout".
Nothing here is verified against the official text, and no one should read it as legal advice.

## What the keel deposited

**Distribution (2026-11-05):** every part receives read-only copies of `roc-core.l4` AND `roc-definitions.l4` and may import both; `roc-definitions-tests.l4` is not distributed.
So a part calls the Order 1 definitions by their exact names (`PLAN.md` section 4A, and section 6.1 for each part's list) and takes a seam input only for an answer that lives in another part's range or outside the sources.

| file | what it is |
| --- | --- |
| `roc-core.l4` | the shared nouns: `DECLARE` only, no rule (196 lines); one line per type in `PLAN.md` section 4 |
| `roc-definitions.l4` | Order 1, Rules 1 to 3, encoded (72 functions; the file is generated from templates by a script that quotes the text mechanically) |
| `roc-definitions-tests.l4` | 289 assertions, each expected value written from the text beside the assertion |
| `PLAN.md` | the naming rule, the main-dialect cheat sheet, the seams, the twelve parts' ranges, the cross-Order citations |
| `RULE-INDEX.md` | a mechanical index of the text's 900 Order and rule headings (72 Orders and 828 rules), each with its line, and for each Order the rule numbers present |
| `PROGRESS.md` | the keel's working log |
| `check.sh`, `fetch-main-l4.sh`, `srcrefs.py` | given; not edited |

## Check

`L4=<1.6.109> L4_MAIN=<1.6.108> ./check.sh` printed exactly:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions-tests.l4                       0       289       0        0         0 |      0       289       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (3 modules)                              0       289       0        0           |      0       289       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Self-containment of the definitions module: `roc-definitions.l4` imports only `prelude`, `daydate` and `roc-core` (`grep '^IMPORT'`), and `l4 check` in a folder holding just `roc-core.l4` and `roc-definitions.l4` prints `Check succeeded.` with exit 0 on 1.6.109 and on 1.6.108; with `roc-core.l4` removed from that folder it exits 1 with "Module not found: roc-core" (positive control).
A mock part module (not kept) in a folder with all four modules imported and called `o 1 r 3(1) a day is a working day`, stated a `Period` under its own prefix, and passed four assertions with no error on both builds.
`srcrefs.py check --refs` and `check --strict` over the three modules: `137 src: lines, 64 runs, 72 locators, 0 problems`.
`l4 check` on each module prints no diagnostic (so no `is at the end of the file` and no `follows code on its line`).
Two positive controls, each run on a copy of the final files: with the whole-Order matching of finding 2 below taken out, exactly six of the 289 assertions fail (the six written for it); with the three period functions put back to answering `NOTHING` outside the period, exactly eleven of the 289 fail (the eleven written with `EQUALS JUST FALSE` for a filing outside the period).

## Coverage table (the keel's ranges: lines 1 to 136 and 8830 to 12250)

Dispositions: `encoded`, `inert` (reason 1 not operative, 2 machinery), `fork` (points at the fork register), `repealed or blank in this text`.
The right-hand column counts the assertions in `roc-definitions-tests.l4` that call the function(s) named.
A function that is a helper (a `BOOLEAN` that sorts a case into a limb or a column, and answers no legal question) has no assertion of its own; it is exercised by its caller's assertions, which are counted against the caller.

| lines | provision | disposition | where | asserts |
| --- | --- | --- | --- | --- |
| 1 to 5 | number, Act, chapter, title, enacting words ("In exercise of the powers conferred by section 80 ...") | inert, reason 1 | | |
| 6 to 7 | `PART 1 GENERAL PROVISIONS` | inert, reason 1 | | |
| 8 to 9 | `ORDER 1 CITATION, APPLICATION AND DEFINITIONS` | inert, reason 1 | | |
| 10 | heading "Citation and commencement (O. 1, r. 1)" | inert, reason 1 | | |
| 11 | O 1 r 1: the Rules come into operation on 1 April 2022 ("Rules of Court 2021" is the short title, not encoded) | encoded | `o 1 r 1 the day these Rules come into operation` | 1 |
| 12 | heading "Revocation, transitional provisions and application (O. 1, r. 2)" | inert, reason 1 |  |  |
| 13 | O 1 r 2(1): the Rules of Court (R 5) "are revoked" | inert, reason 2 (the revocation of the earlier Rules is machinery; see fork K8) |  |  |
| 13 | O 1 r 2(2): the saving and transitional provisions in the First Schedule have effect | encoded | `o 1 r 2(2) a saving or transitional provision has effect` | 2 |
| 14 to 15 | O 1 r 2(3)(a): the Rules apply to civil proceedings commenced on or after 1 April 2022, including their appeals | fork (K17) | `o 1 r 2(3)(a) these Rules apply to civil proceedings commenced on or after 1 April 2022` | 4 |
| 16 to 17 | O 1 r 2(3)(b): the Rules apply with the necessary modifications to appeals to the Court of Appeal or Appellate Division and originating applications to the Court of Appeal from decisions made under the revoked Rules | fork (K17) | `o 1 r 2(3)(b) these Rules apply with modifications to an appeal or originating application to an appellate court` | 5 |
| 18 to 26 | O 1 r 2(4)(a)(i) to (iv): notice of appeal within one month after the date of the order in chambers, the refusal, the section 29B(4)(b) date or the pronouncement (forks K7, K10) | fork | `o 1 r 2(4)(a) the date after which the one month for the notice of appeal runs`; `o 1 r 2(4)(a) one month`; `o 1 r 2(4)(a) the notice of appeal is filed and served within one month` | 15 |
| 27 to 31 | O 1 r 2(4)(b)(i), (ii): notice of appeal after permission within one month or 14 days of the grant (fork K10) | fork | `o 1 r 2(4)(b) the period after permission is granted`; `o 1 r 2(4)(b) the notice of appeal is filed and served within the period after permission` | 11 |
| 32 to 44 | O 1 r 2(4)(c)(i), (ii)(A) to (C), (CA), (CB): application for permission to appeal within 7 working days (forks K10, K11) | fork | `o 1 r 2(4)(c) the date after which the 7 working days for the permission application run`; `o 1 r 2(4)(c) seven working days`; `o 1 r 2(4)(c) the application for permission to appeal is filed and served in time with its documents` | 17 |
| 45 to 46 | O 1 r 2(5)(a): O 18 r 29(1) to (4) and O 19 r 26(1) to (4) do not apply to the application | encoded | `o 1 r 2(5)(a) a paragraph applies to an application for permission mentioned in paragraph (4)(c)` | 6 |
| 47 to 48 | O 1 r 2(5)(b): "the time provided under this Rule" in O 18 r 29(6)(a) and O 19 r 26(6)(a) is read as the time in paragraph (4)(c)(i) or (ii) | encoded | `o 1 r 2(5)(b) the time provided under the Rule is the time in paragraph (4)(c)(i) or (ii)` | 2 |
| 49 | O 1 r 2(6): after an appeal under these Rules from a decision made under the revoked Rules, these Rules do not apply to the proceedings in the lower Court | encoded | `o 1 r 2(6) these Rules apply to the proceedings in the lower Court following the appeal` | 3 |
| 50 to 51 | O 1 r 2(7): the Court may direct that O 3 r 8, O 8 r 2 or 4A, O 25 r 3(2), O 29A, O 55 or O 64 r 4 or 4A apply with suitable modifications (marker `[S 293/2022 wef 03/04/2022]`) | encoded | `o 1 r 2(7) the Court may direct that a provision applies with suitable modifications` | 13 |
| 52 | O 1 r 2(8): the Rules do not apply to proceedings under the Criminal Procedure Code 2010 unless that Code provides otherwise | encoded | `o 1 r 2(8) these Rules apply to proceedings under the Criminal Procedure Code 2010` | 4 |
| 53 | O 1 r 2(9): the Rules do not apply to proceedings in the Family Division of the High Court | encoded | `o 1 r 2(9) these Rules apply to proceedings in the Family Division of the High Court` | 2 |
| 54 to 61 | O 1 r 2(10)(a) to (d): unless the Court otherwise directs, the Rules do not apply to four kinds of proceedings of the Singapore International Commercial Court (the helper has no assertion of its own; its caller has eight; fork K12, K17) | fork (K12, K17) | `o 1 r 2(10) the proceedings are of a kind in sub-paragraphs (a) to (d)`; `o 1 r 2(10) these Rules apply to proceedings in or relating to the Singapore International Commercial Court` | 8 |
| 62 to 84 | O 1 r 2(11): the Table of four kinds of proceedings to which the Rules do not apply except the provisions in the third column (marker `[S 174/2026 wef 01/04/2026]`); the Table is data in the helper | encoded | `o 1 r 2(11) the provision is in the third column for the kind of proceedings`; `o 1 r 2(11) a provision of the Rules applies to proceedings of a kind in the Table` | 21 |
| 85 | O 1 r 2(12): the Rules apply to an appeal arising from proceedings in paragraphs (9) and (11) | encoded | `o 1 r 2(12) these Rules apply to an appeal arising from proceedings mentioned in paragraphs (9) and (11)` | 3 |
| 86 | O 1 r 2(13): the Second Schedule sets out categories of cases to which specific provisions do not apply or apply with modifications (the Second Schedule is a heading only in this text: lines 7761 to 7763) | fork (K13) | `o 1 r 2(13) specific provisions do not apply, or apply with modifications, to the case` | 3 |
| 13 to 86 | O 1 r 2 as a whole: do these Rules apply to the proceedings? (hand-gathered from paragraphs (3), (8) to (12); fork K9) | fork (K9) | `o 1 r 2 these Rules apply to the proceedings` | 11 |
| 87 | heading "General definitions (O. 1, r. 3)" | inert, reason 1 |  |  |
| 88 | O 1 r 3(1), opening words: "In these Rules, unless the context otherwise requires" | fork (K1) | `o 1 r 3(1) a defined term has its defined meaning` | 2 |
| 88 | O 1 r 3(1) “action” | encoded | `o 1 r 3(1) proceedings commenced by a document are an action` | 3 |
| 89 | O 1 r 3(1) “appellate Court” | encoded | `o 1 r 3(1) a court is the appellate Court` | 2 |
| 90 | O 1 r 3(1) “Appellate Division” | encoded | `o 1 r 3(1) a court is the Appellate Division` | 2 |
| 91 | O 1 r 3(1) “attend” | encoded | `o 1 r 3(1) a person attends` | 3 |
| 92 | O 1 r 3(1) “bailiff” | encoded | `o 1 r 3(1) a person is a bailiff` | 3 |
| 93 | O 1 r 3(1) “case conference” | encoded | `o 1 r 3(1) a meeting is a case conference` | 3 |
| 94 | O 1 r 3(1) “Civil Procedure Convention” | encoded | `o 1 r 3(1) an instrument is a Civil Procedure Convention` | 5 |
| 95 | O 1 r 3(1) “claimant” | encoded | `o 1 r 3(1) a person is a claimant` | 3 |
| 96 | O 1 r 3(1) “counterclaim” | encoded | `o 1 r 3(1) a statement is a counterclaim` | 2 |
| 97-98 | O 1 r 3(1) “Court”, limb (a) | encoded | `o 1 r 3(1) limb (a) the General Division or a judge sitting in it` | 2 |
| 99-100 | O 1 r 3(1) “Court”, limb (b) | encoded | `o 1 r 3(1) limb (b) a District Court or a District Judge` | 2 |
| 101-102 | O 1 r 3(1) “Court”, limb (c) | fork (K4) | `o 1 r 3(1) limb (c) the Appellate Division or the Court of Appeal, or a judge sitting in either` | 2 |
| 103-104 | O 1 r 3(1) “Court”, limb (d) | fork (K4) | `o 1 r 3(1) limb (d) in cases where empowered, a Magistrate or the Registrar` | 2 |
| 97-104 | O 1 r 3(1) “Court” | fork (K2, K3, K4) | `o 1 r 3(1) a decision-maker sitting in a court is the Court` | 16 |
| 105 | O 1 r 3(1) “court fees” | encoded | `o 1 r 3(1) a payment is within court fees` | 3 |
| 106 | O 1 r 3(1) “defence” | encoded | `o 1 r 3(1) a document is a defence` | 3 |
| 107 | O 1 r 3(1) “defendant” | encoded | `o 1 r 3(1) a person is a defendant` | 3 |
| 108 | O 1 r 3(1) “entity” | encoded | `o 1 r 3(1) a person is an entity` | 3 |
| 109 | O 1 r 3(1) “General Division” | encoded | `o 1 r 3(1) a court is the General Division` | 2 |
| 110 | O 1 r 3(1) “Ideals” | encoded | `o 1 r 3(1) an objective is one of the Ideals` | 3 |
| 111 | O 1 r 3(1) “Judge” | fork (K5) | `o 1 r 3(1) a person sitting in a court is a Judge` | 8 |
| 112 | O 1 r 3(1) “lower Court” | encoded | `o 1 r 3(1) a court is the lower Court` | 2 |
| 113 | O 1 r 3(1) “medical report” | encoded | `o 1 r 3(1) a report is a medical report` | 3 |
| 114 | O 1 r 3(1) “non-court day” | fork (K16) | `o 1 r 3(1) a day is a non-court day` | 4 |
| 115 | O 1 r 3(1) “non-party” | encoded | `o 1 r 3(1) a person is a non-party` | 4 |
| 116 | O 1 r 3(1) “officer” | encoded | `o 1 r 3(1) a person is an officer` | 3 |
| 117 | O 1 r 3(1) “originating application” | encoded | `o 1 r 3(1) a document is an originating application` | 4 |
| 118 | O 1 r 3(1) “originating claim” | encoded | `o 1 r 3(1) a document is an originating claim` | 4 |
| 119 | O 1 r 3(1) “originating process” | encoded | `o 1 r 3(1) a document is an originating process` | 3 |
| 120 | O 1 r 3(1) “pleading” | encoded | `o 1 r 3(1) a document is a pleading` | 7 |
| 121-124 | O 1 r 3(1) “practice directions” | encoded | `o 1 r 3(1) directions are practice directions` | 6 |
| 125 | O 1 r 3(1) “Registrar” | fork (K14) | `o 1 r 3(1) a person is the Registrar` | 3 |
| 125 | O 1 r 3(1) “Registrar”, references to the Registry | encoded | `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` | 2 |
| 126 | O 1 r 3(1) “Rules” | encoded | `o 1 r 3(1) an instrument is the Rules` | 2 |
| 127 | O 1 r 3(1) “Sheriff” | encoded | `o 1 r 3(1) a person is the Sheriff` | 2 |
| 128 | O 1 r 3(1) “sign” and “seal” | encoded | `o 1 r 3(1) signing or sealing is signing or sealing` | 3 |
| 129 | O 1 r 3(1) “solicitor” | encoded | `o 1 r 3(1) a person is a solicitor` | 5 |
| 130 | O 1 r 3(1) “statement of claim” | encoded | `o 1 r 3(1) a statement is a statement of claim` | 2 |
| 131 | O 1 r 3(1) “statement of the special damages claimed” | encoded | `o 1 r 3(1) a statement is a statement of the special damages claimed` | 3 |
| 132 | O 1 r 3(1) “summons” | encoded | `o 1 r 3(1) an application is a summons` | 3 |
| 133 | O 1 r 3(1) “summons without notice” | encoded | `o 1 r 3(1) an application is a summons without notice` | 3 |
| 134 | O 1 r 3(1) “third party” | encoded | `o 1 r 3(1) a party is a third party` | 3 |
| 134 | O 1 r 3(1) “fourth party” | encoded | `o 1 r 3(1) a party is a fourth party` | 2 |
| 134 | O 1 r 3(1) “third party”, further parties | fork (K6) | `o 1 r 3(1) a party is a further party` | 2 |
| 135 | O 1 r 3(1) “working day” | fork (K15) | `o 1 r 3(1) a day is a working day` | 3 |
| 136 | O 1 r 3(2): the Forms are those set out in the practice directions; a numbered form means the current version | encoded | `o 1 r 3(2) a reference to a numbered Form is to this form` | 3 |
| 8830 to 12250 | TABLE OF DERIVATIONS (line 8831: "This Table of Derivations is provided for the convenience of users of the Rules of Court 2021. It is not part of the Rules.") | inert, reason 1 (not operative) |  |  |

Lines 137 to 8829 belong to the twelve parts (`PLAN.md` section 6); the keel encodes nothing there.
Every line of the text belongs to exactly one agent (checked against `inputs/PARTS.md`).
`RULE-INDEX.md` gives the parts the rule-start lines of their ranges, to build their own tables from.

## Fork register

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

The keel's own forks follow.
"Assumed, not ruled" means the keel chose and a lawyer has not.
Each names the readings, the text that licenses each, the reading chosen, and the rule that encodes it.

**K1. "unless the context otherwise requires" (line 88).**
(i) A yes/no input `the context otherwise requires`: when it holds, the defined term does not have its defined meaning (the text's own "unless"). (ii) Thread that input through each of the ~40 definitions.
Chosen: (i), once, in `o 1 r 3(1) a defined term has its defined meaning`; the definition functions state each term's meaning and do not take the input; a caller asks the context question first.
Assumed, not ruled.
A part does not thread it (`PLAN.md` section 7, item 9).

**K2. "Court" (lines 97 to 104): four limbs and one gathered answer.**
Each limb (a) to (d) has its own function (option C of ruling E1).
One further function gathers the routes by hand (option B of ruling E1, as guidance for hand-gathering only): `o 1 r 3(1) a decision-maker sitting in a court is the Court`.
No construct gathers by name.
Assumed, not ruled: that a reader wants the single question asked once.

**K3. "Court" and the Magistrate's Court as a body (lines 103 to 104).**
Limb (d) names "a Magistrate or the Registrar", not the Magistrate's Court.
(i) The Magistrate's Court sitting as a body is not "the Court" (the definition "means" a closed list, so JUST FALSE). (ii) The definition is silent on the body (NOTHING, undefined term).
Chosen: (ii).
Assumed, not ruled (marginal reading (a) goes the other way).

**K4. "where appropriate" (limb (c)) and "in cases where he or she is empowered to act" (limb (d)).**
Each is a plain input the asker states (`it is appropriate for a judge sitting in the Appellate Division or the Court of Appeal to act`; `the Magistrate or the Registrar is empowered to act in the case`).
When the input is false, the gathered function answers NOTHING (limited by its own wording), not JUST FALSE.
Other reading: JUST FALSE, because the definition is closed by "means".
Listed under marginal readings.

**K5. "Judge" (line 111): "means ... and includes".**
The "means" part gives JUST TRUE for a judge sitting in the General Division and a District Judge; the "includes" part gives JUST TRUE for the Appellate Division / Court of Appeal judge where appropriate and for a Magistrate or the Registrar where empowered; every other case answers NOTHING (includes), not JUST FALSE.
Other reading: JUST FALSE for a person who is none of these, because the first limb says "means".
Assumed, not ruled.

**K6. Terms with "includes" (attend, bailiff, Civil Procedure Convention, claimant, defence, defendant, pleading, Sheriff, sign and seal, solicitor) and "further parties".**
A member gives JUST TRUE; a non-member gives NOTHING (list not closed).
"third party ... and further parties have corresponding meanings" (line 134) names no term beyond "fourth party", so `o 1 r 3(1) a party is a further party` answers JUST TRUE for a party brought in by a fourth party and NOTHING otherwise (undefined term).
"non-party" is "means ... and includes": a person who is not a party is JUST TRUE; a participant for a statutory duty or because they may be affected is JUST TRUE; everyone else is JUST FALSE (the "means" part closes it).

**K7. O 1 r 2(4)(a)(i): "the date when the order was pronounced or when the appellant first had notice of the order" (line 20).**
(i) The earlier date. (ii) The later date. (iii) Whichever is relevant to the case, the text not saying which.
Chosen: when the two dates are the same the answer is that date; when they differ the answer is NOTHING (silent).
Assumed, not ruled; a lawyer should say which of (i) to (iii) is meant.

**K8. O 1 r 2(1): "the Rules of Court (R 5) ... are revoked".**
(i) Inert, reason 2: a repeal of the earlier Rules is machinery, and the revoked Rules are not among the sources. (ii) Encoded as "the revoked Rules do not apply except as r 2(2) to (7) save them".
Chosen: (i), because the effect that matters to a litigant (which pre-2022 proceedings the revoked Rules still govern) is encoded in paragraphs (2), (3), (4), (6), (7) and in the First Schedule (roc12).
Assumed, not ruled: the brief's reason 2 names "savings and transitional provisions that affect no one now"; a repeal is not named, and the live pre-2022 proceedings are why paragraphs (2) to (7) were encoded.

**K9. The gathered answer to "do these Rules apply?" (`o 1 r 2 these Rules apply to the proceedings`).**
Hand-gathered from paragraphs (3), (8) to (12) (E1 option B, guidance only); each paragraph also has its own function (option C).
Precedence chosen: (12) before (8) to (11); (8) to (11) before (3), because (3) opens "Subject to this Rule" and (12) says "To avoid doubt, these Rules apply to any appeal".
A kind of proceedings in the Table of (11) answers NOTHING here, because (11) disapplies the Rules except for the provisions in its third column and is asked provision by provision (`o 1 r 2(11) a provision of the Rules applies ...`).
A proceeding within (10) where the Court directs otherwise, or another written law provides otherwise, answers NOTHING (points outside the text).
Paragraphs (6) and (7) are not in the gathered function (they speak of proceedings after an appeal and of a power to direct), so they are asked on their own.
Assumed, not ruled.

**K10. A period the text fixes in its own words: `o 1 r 2(4)(a)`, `(b)`, `(c)` "must be filed and served within ...".**
Inside the period: JUST TRUE. Outside it: JUST FALSE, with a FALSE-kind comment quoting the period's words ("must be filed and served within one month after"; "within one month after the date on which such permission is granted" or "within 14 days after the date on which such permission is granted"; "within 7 working days after").
Ruled 2026-11-05 (ruling (a): a period fixed in the text's own words gives JUST FALSE outside it); this replaces the keel's first reading, which answered NOTHING.
Other reading: NOTHING (the text states how long, not what follows a late filing).
Tested on both sides of each period: the day before the last day, the last day, the day after, and each of the two dates (filing, service) late on its own.
In (4)(c) the period decides first: a filing or service after the last day is JUST FALSE whatever the documents answer says.
Inside the period, the separate limb "together with the documents mentioned in Order 18, Rule 29(7) or Order 19, Rule 26(7)" is not a period: documents not filed and served with the application answers NOTHING (limited by its own wording), and an unavailable documents answer is NOTHING (points outside the text); the other reading is JUST FALSE for the missing documents too, because the sentence makes the documents part of what "must be filed and served".
The date- and period-valued functions (`o 1 r 2(4)(a) the date after which the one month ... runs`, `o 1 r 2(4)(b) the period after permission is granted`, `o 1 r 2(4)(c) the date after which the 7 working days ... run`, and the three `Period` constants) are unchanged: they cannot answer JUST FALSE, and each has its yes/no twin above.
O 3 r 2(4)(e) names one consequence of a late filing (a fee of $50 for each day), and O 3 r 4 lets the Court extend; both are roc1's.

**K11. Where the count of a period comes from.**
Each of these three functions takes the period's last day as an input, `o 3 r 3 the last day for doing the act` (a `DATE`), because the count (clear days, non-court days, the next court day) is O 3 r 3, in roc1's range.
The period itself is a `Period` constant in the same section (`o 1 r 2(4)(a) one month`, `o 1 r 2(4)(b) the period after permission is granted`, `o 1 r 2(4)(c) seven working days`).

**K12. O 1 r 2(10): "Unless the Court otherwise directs, and subject to any other written law".**
If either input is true the answer is NOTHING (points outside the text): the text does not say what follows a direction, and the other written law is outside the sources.
When neither holds, a proceeding of kinds (a) to (d) answers JUST FALSE.

**K13. O 1 r 2(13) and the Second Schedule.**
The Second Schedule is a heading in this text (lines 7761 to 7763: `SECOND SCHEDULE`, `O. 1, r. 2(13)`, `Application or disapplication of provisions to categories of cases`), with no table under it.
`o 1 r 2(13) specific provisions do not apply, or apply with modifications, to the case` takes the Second Schedule's answer as an input and answers NOTHING when it is absent (points outside the text).
Whether the table was dropped by the converter or never existed in the consolidation is not known to the keel.

**K14. "Registrar" ("as the case may be").**
The asker states the case's court system and, for the person, which court system's Registrar they are; a Registrar of the other system answers NOTHING (limited by its own wording), a non-Registrar JUST FALSE.

**K15. "working day" (line 135).**
JUST TRUE for a day that is not a non-court day, JUST FALSE for a day that is (the text's own "any day other than"), NOTHING when the non-court-day answer is itself NOTHING.
With the `Court calendar` the asker supplies, the non-court-day function never answers NOTHING, so the NOTHING branch is a guard.

**K16. "public holiday" (line 114) is not defined in these Rules.**
The Holidays Act (or whatever lists the days) is not among the sources.
The asker states the days in `Court calendar`'s `public holidays`; Saturday and Sunday come from `daydate`'s `is weekend`.
Assumed, not ruled: the fixture date in the tests (Thursday 12 November 2026) is a test fixture, not a statement that the day is a holiday.

**K17. Date-limited scope: `o 1 r 2(3)(a)`, `o 1 r 2(3)(b)` and the date limb of `o 1 r 2(10)`.**
"commenced on or after 1 April 2022" (3)(a), "filed on or after 1 April 2022, relating to a decision of a lower Court made in proceedings to which the revoked Rules of Court apply" (3)(b), and "commenced on or after 1 April 2022" in the four limbs of (10), say what the Rules apply to (or do not apply to); they are scope limits, with no "only", and they do not fix a period for an act.
For a case outside the date (commenced before 1 April 2022) the answer stays NOTHING (limited by its own wording for (3)(a) and (b); silent for (10)).
Other reading: JUST FALSE (the Rules do not apply to proceedings commenced before 1 April 2022).
Assumed, not ruled.
The text itself keeps the revoked Rules alive for those proceedings (r 2(2) and the First Schedule), which supports NOTHING.

### Reading a result: FALSE and NOTHING

In this row a **no** (`JUST FALSE`) is the text saying no in its own words: a definition that "means" a closed thing and the case is not that thing ("non-court day" means a Saturday, Sunday or public holiday: a Wednesday that is not a holiday is not one); a flat negative ("These Rules do not apply to proceedings in the Family Division of the High Court"); a condition the text introduces with "unless".
**Not covered** (`NOTHING`) is anything else: a definition that "includes" (the list is not closed), a term the text uses but does not define, a case the text does not mention, a fact that lives outside these Rules (the Third Schedule, Order 25 r 1, the Legal Profession Act), and a grant, power or scope limited by its own wording when the case falls outside the limit.
A **period the text fixes in its own words** is the exception: "must be filed and served within one month after" answers `JUST FALSE` for a filing outside the period (ruling (a) of 2026-11-05), not NOTHING.
A caller must never turn `NOTHING` into `FALSE`.
`BOOLEAN` helpers (which limb a sitting falls in; which column of the Table a provision is in) answer a structural question and no legal one; the `MAYBE BOOLEAN` function that calls each carries the `FALSE-kind` and `NOTHING-kind` comments.

**Every answer in the Rules carries a caveat that no function threads as an input**: O 3 r 2(1) says all requirements in the Rules are subject to the Court's discretion to order otherwise in the interests of justice, "even if they are expressed using imperative words such as 'must'".
It belongs to roc1's range and is not an input anywhere; a reader of any `JUST TRUE` or `JUST FALSE` here should hold it in mind.
The lead should say it once in the merged file (`PLAN.md` section 2).

## Marginal readings for a lawyer

The brief's two readings "for a lawyer": (a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
Flat negatives are ruled (N2 above), so the branches resting on N2 are not listed as marginal.
The branches that rest on (a) or (b), with the other reading:

| branch | rests on | the other reading |
| --- | --- | --- |
| `o 1 r 3(1) a defined term has its defined meaning`: JUST FALSE when the context otherwise requires (line 88) | (a): "unless" is read as the text's no | NOTHING: "unless the context otherwise requires" does not say what the term means then |
| `o 1 r 2(4)(a)`, `(b)`, `(c)` timeliness functions: JUST FALSE outside the period (K10) | (a): a failed condition counts as the text's no (ruling (a) of 2026-11-05) | NOTHING: the text states how long, not what follows a late filing |
| `o 1 r 2(4)(c)` timeliness function: NOTHING inside the period when the documents are not filed and served with the application (K10) | (b): "together with the documents mentioned in ..." limits the requirement | JUST FALSE: the documents are part of what "must be filed and served" |
| `o 1 r 3(1) a decision-maker sitting in a court is the Court`: NOTHING when the Appellate Division / Court of Appeal judge is not "appropriate", or a Magistrate or the Registrar is not "empowered" (K4) | (b) | JUST FALSE: the definition "means" a closed list |
| `o 1 r 3(1) a person sitting in a court is a Judge`: NOTHING for a person who is none of the listed (K5) | "includes" (list not closed) | JUST FALSE for the same person: the first limb "means" a closed list |
| the Magistrate's Court as a body is not "the Court" (K3): NOTHING | undefined term | JUST FALSE |
| `o 1 r 2(7) the Court may direct ...`: NOTHING for a provision not listed | (b): the power is limited by its own list | JUST FALSE: the power is given for the listed provisions and no others |
| `o 1 r 2(3)(a) these Rules apply to civil proceedings commenced on or after 1 April 2022`: NOTHING for proceedings commenced before 1 April 2022 (K17) | (b): "which are commenced on or after 1 April 2022" limits the scope | JUST FALSE: earlier proceedings are not within paragraph (3)(a); but the text also keeps the revoked Rules alive for them (r 2(2), First Schedule), which paragraph (3)(a) does not say |
| `o 1 r 2(3)(b) these Rules apply with modifications to an appeal or originating application to an appellate court`: NOTHING outside its filing-date and lower-Court limit (K17) | (b): "filed on or after 1 April 2022, relating to a decision of a lower Court made in proceedings to which the revoked Rules apply" | JUST FALSE for an appeal outside that limit |
| `o 1 r 3(1) a person is the Registrar`: NOTHING for the Registrar of the other court system (K14) | (b): "(as the case may be)" | JUST FALSE: "means" the Registrar of either system, and the person is not the case's Registrar |
| `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case`: NOTHING when it is another Registry | (b): "construed accordingly" | JUST FALSE for a reference to the other system's Registry |
| `o 1 r 2(2) a saving or transitional provision has effect`: NOTHING for a provision not in the First Schedule | (b) | JUST FALSE: the paragraph gives effect to the First Schedule's provisions, no others |
| `o 1 r 2(4)(a)(i)`: NOTHING when the two dates differ (K7) | silent | the earlier date; the later date |
| `o 1 r 2(10)`: NOTHING for a Singapore International Commercial Court proceeding commenced before 1 April 2022 (K17) | (b): "commenced on or after 1 April 2022" limits the scope | JUST FALSE: paragraph (10) does not apply to it |
| `o 1 r 2(10)`: NOTHING when the Court directs otherwise or another written law provides otherwise (K12) | (b) | JUST TRUE: "Unless the Court otherwise directs" is the text's own condition, so a direction makes the Rules apply |

## Jural relations

Hohfeld kinds are recorded here and are not typed into any person-facing answer (ruling N2).
The keel's range creates two powers and three duties.
Everything else in it is a definition, a counting or scope rule, or machinery, listed as `none`.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| O 1 r 1; r 2(1) to (3), (5) (disapplies O 18 r 29(1) to (4) and O 19 r 26(1) to (4) for the application), (6), (8), (9), (11) to (13); r 3(1) every definition; r 3(2) | none | none | none: scope, definition or machinery | the rules in the coverage table |
| O 1 r 2(7): the Court may direct that listed provisions apply with suitable modifications to proceedings governed by the revoked Rules | the Court | each party to those proceedings | power / liability | `o 1 r 2(7) the Court may direct that a provision applies with suitable modifications` |
| O 1 r 2(10): "Unless the Court otherwise directs" | the Court | each party to proceedings of the four kinds | power / liability | `o 1 r 2(10) these Rules apply to proceedings in or relating to the Singapore International Commercial Court` (input `the Court otherwise directs`) |
| O 1 r 2(4)(a): the notice of appeal "must be filed and served within one month" | the text names none | the appellant | duty (the text names no holder of the claim) | `o 1 r 2(4)(a) the notice of appeal is filed and served within one month` |
| O 1 r 2(4)(b): the notice of appeal "must be filed and served" within the period after permission | the text names none | the appellant | duty (the text names no holder of the claim) | `o 1 r 2(4)(b) the notice of appeal is filed and served within the period after permission` |
| O 1 r 2(4)(c): the application for permission "must be filed and served" within 7 working days | the text names none | the applicant | duty (the text names no holder of the claim) | `o 1 r 2(4)(c) the application for permission to appeal is filed and served in time with its documents` |
| Table of Derivations | none | none | none: not operative | not encoded |

The three duties are answered as timeliness questions (`MAYBE BOOLEAN`), not as deontic rules: the keel found no obligation to derive that the timeliness answer does not already give, and the text names no one who may claim performance.

## Seams

The keel's functions take these answers as inputs (asking section; answering section; input name; type).
`PLAN.md` section 5 has the same list and the seams every part meets.

- O 1 r 3(1) "case conference"; O 9 r 1 (roc2); `o 9 r 1 the meeting is a case conference as described`; `MAYBE BOOLEAN`.
- O 1 r 3(1) "Civil Procedure Convention"; the Third Schedule (roc12); `third schedule the convention is set out in the Third Schedule`; `MAYBE BOOLEAN`.
- O 1 r 3(1) "court fees"; O 25 r 1 (roc6); `o 25 r 1 the payment is within court fees`; `MAYBE BOOLEAN`.
- O 1 r 3(1) "Ideals"; O 3 r 1(2) (roc1); `o 3 r 1(2) the objective is one of the Ideals`; `MAYBE BOOLEAN`.
- O 1 r 3(1) "originating application"; O 6 r 11 (roc1); `o 6 r 11 the document commences an action in Court as described`; `MAYBE BOOLEAN`.
- O 1 r 3(1) "originating claim"; O 6 r 5 (roc1); `o 6 r 5 the document commences an action in Court as described`; `MAYBE BOOLEAN`.
- O 1 r 3(1) "practice directions"; O 26 r 2 (roc6); `o 26 r 2 the directions are issued under Order 26, Rule 2`; `MAYBE BOOLEAN`.
- O 1 r 3(1) "solicitor"; section 2 of the Legal Profession Act (not among the sources); `legal profession act s 2 the person is a solicitor`; `MAYBE BOOLEAN`.
- O 1 r 2(2); the First Schedule (roc12); `the provision is set out in the First Schedule as a saving or transitional provision`; `BOOLEAN`.
- O 1 r 2(4)(a) to (c) (every stated period); O 3 r 3 (roc1); `o 3 r 3 the last day for doing the act`; `DATE`.
- O 1 r 2(4)(c); O 18 r 29(7) (roc3) and O 19 r 26(7) (roc4); `o 18 r 29(7) or o 19 r 26(7) the documents mentioned are filed and served with it`; `MAYBE BOOLEAN`.
- O 1 r 2(13); the Second Schedule (roc12; a heading only in this text); `second schedule the case is in a category it sets out`; `MAYBE BOOLEAN`.

The pattern the keel rests on: a part cannot import another part, so a borrowed answer is an input named for the section it comes from, and the lead wires it at the merge.

## Unstable dialect

I looked at time (the only date logic in Order 1 is a comparison with 1 April 2022 and the three stated periods, which take their last day as an input), at versions (every one of the 116 `wef` markers in the text is on or before 1 April 2026, and the file holds only the current version, so no rule is in force on different days), and at workarounds on main (Order 1 needed none that unstable would remove) and found no shape that earns a second encoding; I looked in Order 1 (lines 8 to 136) and in the whole text's `wef` markers.

## Findings

### What the main binary does not accept

Measured on 1.6.109 and 1.6.108 by running a probe, each rejected or misread by the binary and worked around in these files; the skills show some of these constructs and the binary governs.

- **`WHEN Ctor WITH x THEN` is a parse error**; a constructor pattern binds its fields positionally (`WHEN Entity incorporated THEN`).
- **`x IS IN xs` is not accepted**; membership is `elem x xs`.
- **An unprefixed helper named `count` collides with the prelude's `count`** ("multiple definitions"); `any`, `all` and `elem` are also in the prelude. Every name here carries the section label, so none collides.
- **`#CHECK` on an overloaded name is an error**; the deposited files have no `#CHECK`.
- The names `Monday` to `Sunday`, `January` to `December`, `May`, `Day`, `Month`, `Year`, `Week` and `Date` come from `daydate` and cannot be constructors in the core; the core uses none of them.
Not re-measured by the keel and read from the skills' `dialects.md`: no `REFUSE`, no section-level `GIVEN`, no `TYPICALLY` on a field, no sets, no `YMD`; the keel's files use none of them, and both main builds read all three files the same way (the table above).

### Defects found while writing, and one left

1. **The text has a NO-BREAK SPACE between "Order" and its number and a non-breaking hyphen in words like "non-court".** A first count of cross-Order citations (17 lines) was wrong because it searched with an ordinary space; with `\s` the count is 330 occurrences of "Order", a no-break space and a digit (and 20 with a plain space); `PLAN.md`'s Appendix has 145 citation entries. Every part will make the same mistake once.
2. **Orders cited whole were matched only when the rule number was empty (found by re-reading `o 1 r 2(7)` and `o 1 r 2(11)` before finishing, fixed).** "Order 28", "Order 29A" and "Order 55" are cited whole in the text (lines 50 and 71 to 83), so every rule of them applies; the first version matched only when the asker passed an empty rule number, and so answered JUST FALSE for `("28", "10")`. The fix matches the Order whatever rule number is passed; six assertions were added for it, and the old matching fails exactly those six (positive control).
3. **The Table and the power in (7) key a provision by two strings (`order number`, `rule number`)**, because the core has no type for a reference to a rule. "Parts 3 and 4 of the Fourth Schedule read with Order 25" is a pseudo-order string. A part that builds such a table will want a reference type: record it in `NEEDS-CORE.md`.
4. **Two helpers have no assertion of their own** (`o 1 r 2(10) the proceedings are of a kind ...` and `o 1 r 2(11) the provision is in the third column ...`); they are exercised through their callers (eight and twenty-one assertions) and answer a plain `BOOLEAN`, so their `JUST FALSE`-equivalent carries no `FALSE-kind` comment: the caller's branch does.
5. **Not done by the keel**: the unstable binary was not run on these files (target main only); `l4 check` and `l4 run` were run by the two main builds; no `doc/` page (this is an encoding, not a language feature).
