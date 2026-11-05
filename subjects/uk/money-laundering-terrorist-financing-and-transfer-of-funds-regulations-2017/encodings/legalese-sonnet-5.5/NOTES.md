# NOTES: Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (S.I. 2017/692, United Kingdom), whole text with an individual's seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written on 2026-11-05 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel, and merged by the lead agent of the session that ran them.
Target dialect: `main`; every module runs on the main builds 1.6.109 and 1.6.108 with the same four counts.
The source is a plain-text rendering made by a converter script (`uksi-2017-692.txt`, 3,808 lines), not the official text.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`mlr-core.l4`, `mlr-definitions.l4`, the tests of the keel's definitions) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and lists the seams between the parts.
5 **part** agents then encoded their ranges in parallel against the same keel, none reading another's work: `mlr1` (lines 233 to 1008: regulations 8 to 32), `mlr2` (lines 1009 to 1585: regulations 33 to 45ZB (enhanced and simplified due diligence, reliance, record-keeping, beneficial ownership information)), `mlr3` (lines 1586 to 2199: regulations 45A to 64H), `mlr4` (lines 2200 to 3054: regulations 65 to 110 and Schedules 1, 2, 3 and 3AZA), `mlr5` (lines 3055 to 3808: Schedules 3ZA, 3A, 4, 5, 6, 6A, 6B and 7, and the explanatory note).
The keel's range is lines 1 to 232 (the title block, the enacting words and Part 1 (regulations 1 to 7): the shared vocabulary `mlr-core.l4` and the definitions `mlr-definitions.l4`).
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

- **One seat module for the Regulations.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `mlr-seat.l4` and `mlr-cases-seat.l4`, with one banner comment per part and the IMPORT lines merged; the text under each banner is the part's, unchanged. Each part's questions are still those of its own range, so a question about a regulation is found under the banner of the part that owns that regulation.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part or to the keel's definitions, it takes it as an input named for the answering provision (the seams are listed in `notes/keel-PLAN.md`; each part's "Seams" section says what it asks and answers). The merge does not wire one part's output into another's input, so the seat asks the person for the fact.
- **NEEDS-CORE requests are not hoisted.** `mlr5` recorded one request (`notes/mlr5-NEEDS-CORE.md`): a `medium risk` constructor in the core's `Level of risk`, which Schedule 4 item 6 names in its own words; `mlr5` declared a small type of its own for that one item and says the three assertions on it would change if the core took the constructor.
- **The keel's `mlr-core.l4` appears once.** Every part imported the keel's core; the copies in the parts' deposits are byte-identical (the merge stops on a file of the same name with different bytes, and did not stop), and the merged folder holds one.
- **The merge lost nothing:** the merged folder was gated as it stands and its total is 8033 = 462 (the keel's tests) + 1702 + 1490 + 1499 + 1734 + 1146 (each part's test and seat-case assertions, in part order), which are the parts' own totals as the lead measured them after the repairs.

## Where things are

| agent | text (lines) | layer-1 modules | assertions in its test modules | seat questions | seat cases |
| --- | --- | --- | --- | --- | --- |
| keel | 1 to 232 | 2 (`mlr-core`, `mlr-definitions`) | 462 | 0 | 0 |
| mlr1 | 233 to 1008 | 11 | 1565 | 75 | 137 |
| mlr2 | 1009 to 1585 | 6 | 1266 | 49 | 224 |
| mlr3 | 1586 to 2199 | 4 | 988 | 143 | 511 |
| mlr4 | 2200 to 3054 | 5 | 1444 | 99 | 290 |
| mlr5 | 3055 to 3808 | 7 | 947 | 67 | 199 |
| seat, all parts | | `mlr-seat.l4` (433 `@export` questions), `mlr-cases-seat.l4` (1361 assertions) | | | |

The folder holds 70 `.l4` modules in all: 35 layer-1 modules, 34 test modules (one per layer-1 module of a part, the keel's tests, and the seat cases), and the seat.

## The seat

The seat is the one the keel's brief gave the parts: a business that is a relevant person under the Regulations (a bank, an accountancy or legal firm, an estate agent, a money service business and so on) and its compliance officer, asking on facts they can state whether the Regulations apply, what customer due diligence is required for a given customer or transaction, what to record and keep, and by when.
Each part's questions are phrased as that person asks them ("Under regulation 27, is customer due diligence required for ...?") and each has at least one case; the lead's gate found every one of each part's questions called by a case, 433 questions in all.
The notes of `mlr2` and `mlr4` (`notes/<agent>-NOTES.md`) have no "Seat" heading; this section is their seat section.

## Dependencies

- **No other Commons module is imported.** The Regulations are encoded on the keel's `mlr-core.l4` alone; there is no Interpretation Act module in this row.
- **Other instruments are not among the sources.** What the Regulations take from the Proceeds of Crime Act 2002, the Terrorism Act 2000, the Financial Services and Markets Act 2000, the Companies Act and other instruments is a plain input named for the provision; the lists are in the parts' notes (section "Seams") and in `notes/keel-PLAN.md`.
- **The 'Part 1' definitions are a module of the keel (`mlr-definitions.l4`).** The parts do not import it; each takes the answer as a seam input (the plan's S-K1 to S-K4).

## Unstable dialect

No unstable-dialect encoding of this instrument is held in this folder.

## What check.sh prints

`check.sh` on the merged folder, with `l4` 1.6.109 (main, 4c887e0) as the encoding's build and 1.6.108 (main, 2ae7c9b, 2026-11-02) as the second main build: 70 modules, 0 errors, 8033 assertions satisfied, 0 failed, 0 refused, and every module has the same four counts on both ("same").
`srcrefs.py check --refs` against the converted text in `registers/source-bundle/`: every module checked clean, 3,699 `src:` lines in all (310 in the keel's modules, 768, 690, 560, 884 and 487 in the parts', the parts' own gate counts, which the merged folder reproduces).

## Independent test pass

Each part's reviewer worked from the text alone (its notes, progress files and own tests were withheld), wrote its answers first, then asserted them against the encoding.
After the encoders' repairs the lead ran the reviewers' assertions again on the final deposits.

| part | assertions | after repair: satisfied / failed |
| --- | --- | --- |
| mlr1 | 396 | 385 / 11 |
| mlr2 | 322 | 313 / 9 |
| mlr3 | 265 | 260 / 5 |
| mlr4 | 453 | 443 / 10 |
| mlr5 | 269 | 248 / 21 |

- **What the remaining failures are.** Each part's notes record the reviewer's findings and what the encoder did; the failures that remain are the reviewer's own mistakes, readings the encoder left open with a fork line (or "Marginal readings for a lawyer" entry) giving the other reading, and, for `mlr5`, Schedule 3A paragraph-level questions and four regulations the notes list. Not every one is sorted here.
- **Edits to the reviewers' files (arguments and names only).** After signature changes the lead re-pointed some of the reviewers' calls. Compared with the oldest backup of each file that the lead kept, the lines edited are: `mlr2` 5; `mlr3` 2; `mlr4` 10; in none of them does the expected value differ.
- **The reviewers' files are not shipped** (assumed, not ruled), so the failing assertions are not in this folder.

## What would need doing before the encoding is worth relying on

- A lawyer reads the readings each part flags (`notes/<part>-NOTES.md`, "Marginal readings for a lawyer" and the fork register) and rules on them; none is ruled here beyond Meng's four rulings above.
- The converted text is checked against the official text (legislation.gov.uk; the parts' notes list the places where the rendering shows `...`), including anything the converter dropped.
- The inputs the Regulations leave to other instruments are filled from their texts.
- The `NEEDS-CORE` requests are decided (see the merge decisions).
- The reviewers' failing assertions are sorted, part by part, into the reviewer's mistakes, readings the encoder left open and encoder faults; each part's notes list the readings left open, but the lead has not sorted every one of them here.
