# NOTES.md: the keel for the Supreme Court of Judicature Act 1969 (Singapore)

Status (2026-11-05): the core and its tests are written and checked (section "Checks run"); `PLAN.md` is written; no rule is encoded here, by design. This file records the keel's own range (lines 1-45 of the plain-text rendering), the shape of the core, and the register the three part agents inherit. The parts' rows, readings and answer tables arrive with the parts and are merged by the lead.
Edition: Supreme Court of Judicature Act 1969, 2020 Revised Edition, informal consolidation, "version in force from 1/7/2024" (line 16 of `SCJA1969.txt`), retrieved 2026-10-01 from https://sso.agc.gov.sg/Act/SCJA1969. **The text is a plain-text rendering made by a converter script; it is not the official text, and nothing in this row claims to have been verified against the official text.** The licence note is `SOURCE-LICENSE.md` (SSO's Terms of Use cl.13; SSO reproduces an unofficial consolidation, cl.8).
Target: `main`. Written and run with main build 1.6.109 (4c887e0, 2026-11-04, sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`); compared by `check.sh` with main build 1.6.108 (2ae7c9b, 2026-11-02). No `unstable` binary was used.

## What is encoded and what is not

The keel encodes the nouns the three parts share and nothing else: `scja-core.l4` (297 lines: courts, Judges and panels, roles and officers, the subject of a case, orders and decisions, the Act's printed figures and dates) and `scja-core-tests.l4` (23 assertions). The keel's own range, lines 1-45, holds no operative provision: it is the title page, the consolidation banner and the first 24 lines of the Arrangement of Sections (table below). Every operative provision of the Act, sections 1-83 and the First to Tenth Schedules, is in `scja1`, `scja2` or `scja3`'s range (`PLAN.md` gives the section map and the 20 seams between the ranges).
**There is no `scja-definitions.l4`**: section 2 (lines 378-433) and every other definition lie in a part's range, so they are the parts' to encode (`PLAN.md` lists them part by part). Encoding section 2 in the keel as well would give two modules the same `s 2 ...` names.

## Seat

The individual to whom the Act is applied: a person who wishes to start, defend or appeal a civil case in the Singapore High Court or Court of Appeal, asking on facts they can state which court hears it, who may appear, what jurisdiction and powers apply, and the time limits the Act itself sets. The courts, the Registrar, the Chief Justice and the Minister get no seat: their powers appear only as what they mean for that person. Nothing in the core addresses an official as a question-asker; the officers in the core (`Officer of the Supreme Court`) are nouns that a rule about what may be done to a person refers to.

## Coverage table: the keel's range, lines 1-45

Dispositions are those the brief allows. Reasons for `inert` are the brief's three: 1 not operative; 2 machinery; 3 shown repealed or blank.

| lines | provision as printed | disposition | what the text shows / where it goes |
| --- | --- | --- | --- |
| 1-3 | "THE STATUTES OF THE REPUBLIC OF SINGAPORE / SUPREME COURT OF JUDICATURE ACT 1969" | inert, reason 1 | the title of the work; creates no rule |
| 5 | "2020 REVISED EDITION" | inert, reason 1 | edition label |
| 7-8 | "This revised edition incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021." | inert, reason 2 | the commencement of the Revised Edition itself, which affects no one now; not held as a constant |
| 10-14 | "Prepared and Published by THE LAW REVISION COMMISSION UNDER THE AUTHORITY OF THE REVISED EDITION OF THE LAWS ACT 1983" | inert, reason 1 | publisher's statement |
| 16-17 | "Informal Consolidation – version in force from 1/7/2024 / 2020 Ed." | inert, reason 1 | the date the consolidated text is in force from is held as the core constant `the day the text is in force from` (1 July 2024), with a test; the line itself creates no rule |
| 19-20 | "Supreme Court of Judicature Act 1969" (running title) | inert, reason 1 | page furniture |
| 22 | "ARRANGEMENT OF SECTIONS" | inert, reason 1 | heading |
| 24-29 | "PART 1 PRELIMINARY / 1. Short title / 2. Interpretation" | inert, reason 1 | headings only; the sections are at lines 375 (s 1) and 378 (s 2), in scja1's range |
| 31-44 | "PART 2 THE SUPREME COURT / 3. Superior courts ... 8A. Court may conduct hearing through electronic means of communication" | inert, reason 1 | headings only; the sections are in scja1's range from line 448 |

No row is `encoded`, `fork` or `repealed or blank` in this range: it holds none. The coverage of the rest of the text belongs to the parts; `PLAN.md` lists, per part, the sections, their start lines, the sections shown repealed (9, 12, 18E, 28B, Eighth Schedule) and the Legislative History (line 6587 on: "It is not part of the Act").

## Fork register

### The rulings that bind this row (word for word, as the brief prints them)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

### Judgment calls

One line per site, in the form: question | provision | function name | file and line | answer taken | other reading. The keel writes no function, so no site arises in its range and none in the core; the parts record their own sites in their own NOTES.md.

- QA | not arising | none: the core holds no rule and lines 1-45 hold no bar with an "unless" | none | none | none
- QB | not arising | none: no bare "must" in lines 1-45 and none in the core | none | none | none
- QC | not arising | none: no "listed in Schedule N" question is asked in lines 1-45 (the Schedules are scja3's, and sections 18(2), 21(1)(b), 29(b), 29A, 29C(2), 36(1), 46, 54(1) and 60E(1) that send to them are seams 1-8 and 14-16 in PLAN.md) | none | none | none
- QD | not arising | none: no duty with an unmet "if" or "where" in lines 1-45 | none | none | none
- QE | not arising | none: no "(other than X)" in lines 1-45 | none | none | none
- QF (F11) | not applicable | none: this encoding writes no events to the state ledger | none | none | none

### Core shape: where the text can be read two ways and the core had to pick a noun

These are not rulings on the Act's rules; each records a reading the core's shape leaves open so a part is not surprised. Each is a fork in the brief's sense only where the parts' sections turn on it, and the parts record that at their own sites.

- **K1. Does "General Division" include the Singapore International Commercial Court?** Reading 1, yes: s 18A says there is "a division of the General Division known as the Singapore International Commercial Court" (line 1317), and s 18C applies the Act's provisions to SICC proceedings "as they apply to proceedings in the General Division exercising its original civil jurisdiction" (line 1344). Reading 2, no: s 18J(4) says "In this section, 'General Division' does not include the Singapore International Commercial Court" (line 1610), s 18I(1) gives the SICC "such powers as the General Division may exercise in its original civil jurisdiction", with two exceptions (line 1566), and the Sixth Schedule para 1(f) lists "an appeal against a decision of the Singapore International Commercial Court" apart from appeals against GD decisions (line 6209). Taken in the core: neither; the SICC is its own constructor of `Court`, so a fact can name it, and each section's part decides whether the SICC is counted. Outcome that differs: which court an appeal goes to (s 29C, Sixth Schedule) and whether s 21, 29, 29A attach to a SICC decision.
- **K2. An unvalued case and the two money tests.** Section 21(1)(a) tests "the amount in dispute, or the value of the subject matter ... (excluding interest and costs)" and s 29A(1)(b) the same figure against $250,000 (lines 1731-1735, 2074-2079). The text does not say what a case with no amount or value is. Reading 1 (taken in the core): the field `amount in dispute or value of the subject matter, excluding interest and costs` of `Decision` is `MAYBE NUMBER` and `NOTHING` means the Act does not say. Reading 2: such a case does not "exceed" the sum, so the permission test is met. Reading 3: its value is 0. Test: `scja-core-tests.l4` asserts the `NOTHING` carrier. The rulings of 2026-11-05 (scope limits answer `NOTHING`) point to reading 1; this is the keel's call, assumed, not ruled.
- **K3. Order of appointments.** Section 4 ranks Judges "according to the order of their appointments" (lines 456-475). The core stores `date of appointment` (a `DATE`); two Judges appointed on one day have an order the date does not show. Reading 1 (taken): the date is the order, and a tie is a case the Act does not settle, which scja1 answers `NOTHING`. Reading 2: an explicit order number. Assumed, not ruled.
- **K4. "Quasi-criminal".** Section 20 speaks of jurisdiction "of a quasi-criminal or civil nature" (lines 1705-1710) and s 74(5) of "civil matter, quasi-criminal matter or criminal matter" (lines 4830-4832). Reading 1 (taken): three kinds, `Nature of the proceeding`. Reading 2: quasi-criminal is a species of criminal, or of civil, and needs no constructor. Taken because the Act itself names the three.
- **K5. A `Role` is a label, not a legal status.** The core's `Role` lists the parts the Act names (appellant, judgment debtor, journalist ...). Whether a person has the role (for example whether a journalist "reports news for a newspaper or a broadcasting service", s 8(5)(a)) is a fact or an open-textured judgment each part asks as a plain input.

## Jural relations

The core creates no relation; it declares nouns. Lines 1-45 hold no provision that creates one.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | section | L4 rule |
| --- | --- | --- | --- | --- |
| title page, banner, running title (lines 1-20) | none | none | none | none |
| Arrangement of Sections (lines 22-45) | none | none | none | none |
| the core's `DECLARE`s and constants | none | none | none (nouns and the Act's printed figures) | none |

The parts' tables (which cover sections 1-83 and the Schedules) are merged by the lead.

## Reading a result: FALSE and NOTHING

The keel's core contains no function, so it has no "no" to flag. This is what the words mean for the Act, so the parts read them alike.
A "no" (`JUST FALSE`, or a constructor that says the text says no) is given only where the Act says no in its own words. In this Act those words are, for example: "has no jurisdiction" (s 17A(1), line 1109); "an appeal cannot be brought" (ss 29, 46, lines 2042, 2812); "no proceeding by way of revision is to be entertained" (s 26, line 1923); "no party has any right to be heard" (s 28(1), line 1973); "must not conduct ... through a live audio link only" (s 8A(3), line 714); "applies only if there is no express provision to the contrary" (s 18F(2), line 1507); "may only be brought with the permission of the Court of Appeal" (s 47(1), line 2819); "only with the permission" (s 21(1), line 1719); a period the Act fixes in its own words (s 29B(2)(b), "the 15th day after", line 2139) once it has run out; a "where" or "if" that is not met.
"Not covered" (`NOTHING`, or a named "not covered" constructor) is given wherever the Act lists without closing the list ("includes", s 2 "Rules of Court ... includes forms", "seal includes stamp"), leaves a term undefined, is silent (a case with no amount in dispute, K2), or points outside the sources: to the Rules of Court (the time for a notice of appeal is not in the Act), to the Chief Justice, to the Minister's power to amend the Third to Ninth Schedules (s 83), to the Registrar or a Judge being "satisfied", to another Act (Administration of Muslim Law Act 1966, Criminal Procedure Code 2010). A scope limit with no "only" answers `NOTHING` outside the scope (ruling of 2026-11-05; its examples are "an employee of" and "below" a minimum age, not words of this Act).
A caller never turns `NOTHING` into `FALSE`: the plan's 20 seams are typed `MAYBE ...` for that reason. The two readings the brief marks "for a lawyer" are taken as the status quo and are not decided here: (a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.

## Marginal readings for a lawyer

None in the keel's files: the core has no branch that answers "no" or "not covered". Each part lists the branches of its own that rest on reading (a) or (b) above, with the other reading stated.

## Dependencies

The keel copied nothing and needs nothing: `scja-core.l4` imports `prelude` and `daydate` only (`"dependencies": []` in `encoding.json`). Staged by the lead for the parts and NOT copied by the keel: `sgia-interpretation-time.l4` (Commons `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/`, blob fe60ab2c1f2326a5b061e163761bd63e4f47e12a, at Commons main d468311a6; s 50 counting of days, s 10, s 2(1) "month" and "year") for any part that counts a period or a day (ss 10B, 29B, 41, 59, 72, 73C, 73D), and `sgia-p1-definitions.l4` (blob ca5e2607c635962769a753d71154ad4ae6055f59; the Interpretation Act s 2(1) table) for a part that needs a borrowed term such as "written law". The core avoids every top-level name those two modules define, checked by importing the core with both in one file (no "multiple definitions" error); `PLAN.md` lists the names.

## Unstable dialect

Looked at time, versions and workarounds across the whole text and found no shape that earns a second, unstable encoding: the text is one consolidation in force from 1 July 2024 (the `wef` tags, e.g. line 533, show amendments already applied, so no section has two vintages here); the only dated tests are the fixed dates in s 17A(3A) ("before 1 March 2009") and s 18D(2)(c) and s 80(2A)(c)(ii) ("immediately before 30 July 2020", another Act's vintage, asked as a fact); and the keel's core needed no workaround on main. A second encoding of these provisions in the unstable dialect does not exist.

## What the main binary does not accept

Found while writing the core and its tests, on 1.6.109:

- There is no `length` on a list; `count (b's judges)` is the spelling that exists (`I could not find a definition for the identifier length`).
- A record built with `WITH`, written unbracketed as the value of a field of another `WITH`, is `unexpected WITH`: `IS Order WITH about IS ..., \`way it went\` IS ...` inside a `Decision WITH ...` failed at 45:31 of the first draft of the tests. The bracketed form `IS (Order WITH ...)` was not tried. Naming the inner record first (`\`the order giving unconditional permission to defend\` MEANS Order WITH ...`) and using the name works (23 assertions satisfied).
- A call compared with `EQUALS` must be bracketed. Unbracketed, `#ASSERT f NOTHING (JUST TRUE) EQUALS JUST TRUE` was a type mismatch ("expected BOOLEAN but is MAYBE OF BOOLEAN"), and in the `WITH` form the `EQUALS` bound into the last field; bracketed, `#ASSERT (f NOTHING (JUST TRUE)) EQUALS JUST TRUE`, the four seam assertions were satisfied. The cause was not isolated.
- A type name is not a value: `#CHECK Court` is "could not find a definition for the identifier Court".
Not tried: an opaque `DECLARE` (the core has none), `REFUSE`, sets, `TYPICALLY`, `YMD` (the core uses `Date day month year`), which `dialects.md` lists as rejected on main.

## Checks run

(Run 2026-11-05 from the deposit folder: `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh`.)

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
scja-core-tests.l4                             0        23       0        0         0 |      0        23       0        0  same
scja-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (2 modules)                              0        23       0        0           |      0        23       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

(`exit=0`. The module list is the two modules in this folder; the main columns are main build 1.6.108.) The main build the check compared with is `1.6.108 (main, 2ae7c9b, 2026-11-02)`; the build the keel wrote with is `1.6.109 (main, 4c887e0, 2026-11-04)`.

- No `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning` from `l4 run` on either file, on 1.6.109 and on 1.6.108 (0 counted by `grep -cE "DiagnosticSeverity_(Error|Warning)"`); no `is at the end of the file`, `follows code on its line` or `Unknown annotation` message from `l4 check`.
- `python3 -I srcrefs.py check --refs SCJA1969.txt scja-core.l4 scja-core-tests.l4` and the same with `--strict`: `srcrefs check: 23 src: lines, 13 runs, 14 locators, 0 problems` (both).
- No test is expected to fail: `expected_failed` in `check.sh` lists none.

## Open questions for a Singapore litigator

1. Does the Singapore International Commercial Court count as "the General Division" in each of ss 21, 29, 29A, 29B and 29C? (K1; the Act says yes in ss 18A and 18C and no in s 18J(4).)
2. For a person who wants to appeal: the Act sets no time for the notice of appeal (the Rules of Court do, and are not among the sources), only when that time begins (s 29B(4)(b)). Which Rules of Court provision should be staged so the seat can answer "by when must I appeal"?
3. What does the Act intend for a case with no amount or value in dispute under ss 21(1)(a) and 29A(1)(b)? (K2.)
