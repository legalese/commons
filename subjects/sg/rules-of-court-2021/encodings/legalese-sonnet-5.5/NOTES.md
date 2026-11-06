# NOTES: Rules of Court 2021 (Singapore, G.N. No. S 914/2021), whole text with an individual's seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written on 2026-11-05 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel, and merged by the lead agent of the session that ran them.
Target dialect: `main`; every module runs on the main builds 1.6.109 and 1.6.108 with the same four counts.
The source is a plain-text rendering made by a converter script (`SCJA1969-S914-2021.txt`, 12,250 lines), not the official text.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`roc-core.l4`, `roc-definitions.l4`, the tests of the keel's definitions) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and lists the seams between the parts.
12 **part** agents then encoded their ranges in parallel against the same keel, none reading another's work: `roc1` (lines 137 to 727: Orders 2 to 8), `roc2` (lines 728 to 1404: Orders 9 to 14), `roc3` (lines 1405 to 2230: Orders 15 to 18), `roc4` (lines 2231 to 2875: Order 19), `roc5` (lines 2876 to 3555: Orders 20 to 22), `roc6` (lines 3556 to 4193: Orders 23 to 27), `roc7` (lines 4194 to 5050: Orders 28 to 33), `roc8` (lines 5051 to 5510: Orders 34 to 38), `roc9` (lines 5511 to 6101: Orders 39 to 45), `roc10` (lines 6102 to 6795: Orders 46 to 56 (including Order 46A)), `roc11` (lines 6796 to 7399: Orders 57 to 63), `roc12` (lines 7400 to 8829: Orders 64 to 70 and the First to Fourth Schedules).
The keel's range is lines 1 to 136 and 8830 to 12250 (the title block, the enacting words and Order 1 (lines 1 to 136), and the Table of Derivations that closes the text (it begins at line 8830): the shared vocabulary and the Order 1 definitions).
Each part was then read by an independent **Opus** test author (a different agent from the encoder) who decided the answers from the text alone, before opening the encoding or its notes, and wrote tests of its own (`notes/` does not hold them: they were run, not shipped).
The part's encoder then repaired the findings it judged to be the encoding's fault, under Meng's rulings of 2026-11-05 (the two bullets under "The conventions" below), and the lead ran the reviewer's tests again on the repaired part.
The lead merged the parts with a script; nothing in a part's modules was edited at the merge.
Every note a part wrote is kept, unchanged except that the lead's scratchpad path is replaced by a placeholder and the two 2026-11-05 ruling bullets are replaced by the guide's text, as `notes/<agent>-NOTES.md`, with its `PROGRESS.md`, its brief as `notes/<agent>-BRIEF.md` and its `NEEDS-CORE.md` where it wrote one.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here.

## The conventions this row follows

The family's rule of 2026-10-29 for `JUST FALSE` and `NOTHING` (the guide, section 5): a function answers `JUST FALSE` only where the text itself says no to the case in its own words, and `NOTHING` where the text is silent, open, undefined or points outside it.
Four rulings of Meng's, recorded in the Commons guide and repeated here word for word:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**Reading a result** is explained in each part's notes (section "Reading the answers" or "Reading a result") and the keel's (`notes/keel-NOTES.md`).

## Merge decisions (assumed, not ruled)

- **One seat module for the Rules.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `roc-seat.l4` and `roc-cases-seat.l4`, with one banner comment per part and the IMPORT lines merged; the text under each banner is the part's, unchanged. Each part's questions are still those of its own range, so a question about a regulation is found under the banner of the part that owns that regulation.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part or to the keel's definitions, it takes it as an input named for the answering provision (the seams are listed in `notes/keel-PLAN.md`; each part's "Seams" section says what it asks and answers). The merge does not wire one part's output into another's input, so the seat asks the person for the fact.
- **NEEDS-CORE requests are not hoisted.** Three parts asked for a `Years` constructor in the core's `Time unit` (`notes/roc3-NEEDS-CORE.md`, `notes/roc6-NEEDS-CORE.md`, `notes/roc7-NEEDS-CORE.md`): `roc3` (Order 15 rule 11(11), five years) and `roc7` (Order 28 rule 15(2)(c), seven years) wrote the period in months (60 and 84), and `roc6` (Order 27 rules 13 and 14(1), ages of an account in years, not periods that run from an event) uses plain NUMBER constants and says a `Years` unit is needed only if some part states a period that runs in years from an event. None is hoisted.
- **The keel's final `roc-definitions.l4` replaces the parts' copy.** All twelve parts were written and gated with the copy of `roc-definitions.l4` that the keel distributed first. The keel then changed three time-bar functions of Order 1 rule 2(4) (paragraphs (a), (b) and (c): notice of appeal within one month, after permission, and the application for permission within 7 working days) from `NOTHING` to `JUST FALSE` outside the period (ruling (a)); the keel's version is the one in this folder, and the check below was run against it.
- **The merge lost nothing:** the merged folder was gated as it stands and its total is 22238 = 289 (the keel's tests) + 1523 + 1646 + 1522 + 2016 + 1752 + 1274 + 3495 + 1203 + 2049 + 1963 + 1801 + 1705 (each part's test and seat-case assertions, in part order), which are the parts' own totals as the lead measured them after the repairs.

## Where things are

| agent | text (lines) | layer-1 modules | assertions in its test modules | seat questions | seat cases |
| --- | --- | --- | --- | --- | --- |
| keel | 1 to 136 and 8830 to 12250 | 2 (`roc-core`, `roc-definitions`) | 289 | 0 | 0 |
| roc1 | 137 to 727 | 9 | 1305 | 83 | 218 |
| roc2 | 728 to 1404 | 8 | 1357 | 133 | 289 |
| roc3 | 1405 to 2230 | 9 | 1373 | 58 | 149 |
| roc4 | 2231 to 2875 | 5 | 1102 | 293 | 914 |
| roc5 | 2876 to 3555 | 7 | 1090 | 273 | 662 |
| roc6 | 3556 to 4193 | 6 | 1171 | 39 | 103 |
| roc7 | 4194 to 5050 | 8 | 2195 | 397 | 1300 |
| roc8 | 5051 to 5510 | 6 | 1068 | 70 | 135 |
| roc9 | 5511 to 6101 | 7 | 1389 | 350 | 660 |
| roc10 | 6102 to 6795 | 13 | 1433 | 362 | 530 |
| roc11 | 6796 to 7399 | 7 | 1138 | 242 | 663 |
| roc12 | 7400 to 8829 | 15 | 1468 | 68 | 237 |
| seat, all parts | | `roc-seat.l4` (2368 `@export` questions), `roc-cases-seat.l4` (5860 assertions) | | | |

The folder holds 196 `.l4` modules in all: 102 layer-1 modules, 93 test modules (one per layer-1 module of a part, the keel's tests, and the seat cases), and the seat.

## The seat

The seat is the one the keel's brief gave the parts: a party to a civil action in the Singapore courts (a claimant, a defendant, a third party or an appellant), asking on facts they can state what they must file or serve, by when, how, at what cost, what the court may order, and what follows if they do not.
Each part's questions are phrased as that person asks them ("Under Order 9, rule 1(1), on what date is the case conference to be held?") and each has at least one case; the lead's gate found every one of each part's questions called by a case, 2368 questions in all.
The notes of `roc1`, `roc4`, `roc6`, `roc11` and `roc12` (`notes/<agent>-NOTES.md`) have no "Seat" heading; this section is their seat section.

## Dependencies

- **No other Commons module is imported.** The Rules are encoded on the keel's `roc-core.l4` and `roc-definitions.l4` alone; there is no Interpretation Act module in this row.
- **Time is computed by the caller.** Where a rule counts days, weeks or months from an event, the parts take the last day (Order 3 rule 3, the keel's seam S-T1 and S-T1b in `notes/keel-PLAN.md`) as an input rather than computing it; the lists of such inputs are in the parts' notes (section "Seams").
- **The Supreme Court of Judicature Act 1969, other Acts, practice directions and fees orders are not among the sources.** What a rule takes from them is a plain input named for the provision, listed in the parts' notes.

## Unstable dialect

No unstable-dialect encoding of this instrument is held in this folder.

## What check.sh prints

`check.sh` on the merged folder, with `l4` 1.6.109 (main, 4c887e0) as the encoding's build and 1.6.108 (main, 2ae7c9b, 2026-11-02) as the second main build: 196 modules, 0 errors, 22238 assertions satisfied, 0 failed, 0 refused, and every module has the same four counts on both ("same").
`srcrefs.py check --refs` against the converted text in `registers/source-bundle/`: every module checked clean, 10,501 `src:` lines in all over the 196 modules (counted by the lead on the merged folder).

## Independent test pass

Each part's reviewer worked from the text alone (its notes, progress files and own tests were withheld), wrote its answers first, then asserted them against the encoding.
After the encoders' repairs the lead ran the reviewers' assertions again on the final deposits.

| part | assertions | after repair: satisfied / failed |
| --- | --- | --- |
| roc1 | 272 | 254 / 18 |
| roc2 | 398 | 388 / 10 |
| roc3 | 333 | 326 / 7 |
| roc4 | 351 | 345 / 6 |
| roc5 | 312 | 311 / 1 |
| roc6 | 315 | 300 / 15 |
| roc7 | 506 | 487 / 19 |
| roc8 | 255 | 243 / 12 |
| roc9 | 302 | 289 / 13 |
| roc10 | 281 | 255 / 26 |
| roc11 | 309 | 289 / 20 |
| roc12 | 435 | 388 / 47 |

- **What the remaining failures are.** Each part's notes record the reviewer's findings and what the encoder did about them; the failures that remain have not all been sorted here.
- **Edits to the reviewers' files (arguments and names only).** After signature changes the lead re-pointed some of the reviewers' calls. Compared with the oldest backup of each file that the lead kept, the lines edited are: `roc4` 12; `roc5` 1; `roc6` 4; `roc7` 3; `roc8` 2; `roc9` 7; `roc10` 6; `roc12` 9; in 5 of them (`roc5` 1, `roc7` 2, `roc9` 2) the line was rewritten more than its arguments because the function it calls changed its name, an argument type or the shape of its result (for example `5330` became `JUST 5330`); the lead read each of those lines and the expected outcome is the same.
- **The reviewers' files are not shipped** (assumed, not ruled), so the failing assertions are not in this folder.

## What would need doing before the encoding is worth relying on

- A lawyer reads the readings each part flags (`notes/<part>-NOTES.md`, "Marginal readings for a lawyer" and the fork register) and rules on them; none is ruled here beyond Meng's four rulings above.
- The converted text is checked against the official text (Singapore Statutes Online), including anything the converter dropped.
- The inputs the Rules leave to other instruments are filled from their texts.
- The `NEEDS-CORE` requests are decided (see the merge decisions).
- Sort the reviewers' failing assertions, part by part, into the reviewer's mistakes, readings the encoder left open and encoder faults: each part's notes list the readings left open, but the lead has not sorted every one of them here (`roc12`'s notes say its reviewer's hearing-day fee assertions were not re-pointed to the days reading the encoding uses).
- Decide, for each cross-Order seam input (a yes/no or date input in one Order that a rule in another Order answers; `notes/<part>-NOTES.md`, section "Seams", and `notes/keel-PLAN.md`), whether to wire it to the answering rule or keep it an input; this merge keeps them inputs.
