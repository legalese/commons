# NOTES: Employment Act 1968 (Singapore) and the Employment (Retrenchment Reporting) Notification 2019 (S 200/2019), whole text with individual seats

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written on 2026-11-05 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel, and merged by the lead agent of the session that ran them.
Target dialect: `main`; every module runs on the main builds 1.6.109 and 1.6.108 with the same four counts.
The source is a plain-text rendering made by a converter script (`EmA1968.txt`, 6,790 lines, and `EmA1968-S200-2019.txt`), not the official text.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`ea-core.l4`, `ea-definitions.l4` and the tests of the definitions) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text.
Three **part** agents then encoded their ranges in parallel against the same keel, none reading another's work: `ea1` (lines 785 to 2596: Parts 2 to 6, ss 8 to 66), `ea2` (lines 2597 to 4611: Parts 6A to 14, with the Notification of 2019) and `ea3` (lines 4612 to 6790: Part 15 to the Fifth Schedule, ss 115 to 140).
The keel's range is lines 1 to 784 (the title page, the Arrangement of Sections, Part 1 and the definitions of s 2(1)).
Each part was then read by an independent **Opus** test author (a different agent from the encoder) who decided the answers from the text alone, before opening the encoding or its notes, and wrote tests of its own (`notes/` does not hold them: they were run, not kept; the counts are below).
The part's encoder then repaired the findings it judged to be the encoding's fault, under Meng's rulings of 2026-11-05 (the two bullets under "The conventions" below), and the lead ran the reviewer's tests again on the repaired part.
The lead merged the parts with a script; nothing in a part's modules was edited at the merge.
Every note a part wrote is kept, unchanged except that the lead's scratchpad path is replaced by a placeholder and the two 2026-11-05 ruling bullets are replaced by the guide's text, as `notes/<agent>-NOTES.md`, with its `PROGRESS.md`, `SEAMS-FOUND.md`, `SEAMS-ANSWERED.md` and `NEEDS-CORE.md` where it wrote them; the keel's are `notes/keel-*.md`, and the brief each agent was given is `notes/<agent>-BRIEF.md`.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here.

## The conventions this row follows

The family's rule of 2026-10-29 for `JUST FALSE` and `NOTHING` (the guide, section 5): a function answers `JUST FALSE` only where the text itself says no to the case in its own words, and `NOTHING` where the text is silent, open, undefined or points outside itself.
Four rulings of Meng's, recorded in the Commons guide and repeated here word for word:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**Reading a result** is explained in each part's notes (`notes/ea1-NOTES.md`, `notes/ea2-NOTES.md`, `notes/ea3-NOTES.md`, section "Reading a result: FALSE and NOTHING") and the keel's (`notes/keel-NOTES.md`).
`ea2` records one silent trap there: for `s 81` and `s 105(4)` it added twins that ask the text's own question ("it is not lawful", "must not detain"), and `ea2-duties.l4` takes the older functions' answers as inputs, so feeding it a twin's answer inverts the result.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `ea-seat.l4` and `ea-cases-seat.l4`, with one banner comment per part and the IMPORT lines merged; the text under each banner is the part's, unchanged. Each part's questions are still those of its range of the text. The merged seat module compiles with no name collision between the three; `ea2` prefixes its answer type and wiring functions (`ea2 seat: ...`).
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section (`notes/<part>-SEAMS-FOUND.md` and `notes/<part>-SEAMS-ANSWERED.md` list what each part asks and answers). The merge does not wire one part's output into another's input, so the seat asks the person each such fact. For example `ea2-part-6a-8.l4` takes "the answer of s 2(1) employee" as an input (line 26) and does not call the keel's definition.
- **NEEDS-CORE requests are not hoisted.** `ea2` and `ea3` each recorded what they would like `ea-core.l4` to hold (`notes/ea2-NEEDS-CORE.md`: a shared Yes / No / I am not sure type for the seat, a way to say "no maximum stated" apart from "no imprisonment", a pattern for the public holidays, a convention for `JUST 0` amounts; `notes/ea3-NEEDS-CORE.md`: two officials of s 124(1)(a)). Each declared what it needed in its own module. The keel is the three parts' common core and is byte-identical in all of them, so the lead did not change it.
- **One copy of the Interpretation Act module.** `sgia-interpretation-time.l4` was copied unchanged into the parts that import it (`ea1`, `ea2`, `ea3`); the copies are byte-identical and the merged folder holds one.
- **The compliance-when-no-duty-arises pattern is not reconciled inside this Act.** `ea1` fork F-NODUTY answers `NOTHING` for "was the duty complied with" when the "if" or "where" that creates the duty is not met, and `JUST FALSE` for "does the duty exist"; it names `JUST TRUE` as the other reading and leaves the choice to the lead. The lead has not audited `ea2` and `ea3` for compliance functions of the same shape and made no change.
- **The merge lost nothing:** the merged folder was gated as it stands and its total is 3,926 = 155 (the keel's tests) + 860 and 506 (`ea1` tests and seat cases) + 1,111 and 606 (`ea2`) + 505 and 183 (`ea3`), the parts' own totals as the lead measured them after the repairs (1,366, 1,717 and 688).

## Where things are

| agent | text (lines) | layer-1 modules | assertions in its test modules | seat questions | seat cases |
| --- | --- | --- | --- | --- | --- |
| keel | 1 to 784 | 2 (`ea-core`, `ea-definitions`) | 155 | 0 | 0 |
| ea1 | 785 to 2596 | 8 | 860 | 214 | 506 |
| ea2 | 2597 to 4611, and the Notification | 12 | 1111 | 219 | 606 |
| ea3 | 4612 to 6790 | 4 | 505 | 61 | 183 |
| seat, all parts | | `ea-seat.l4` (494 `@export` questions), `ea-cases-seat.l4` (1295 assertions) | | | |

The folder holds 54 `.l4` modules in all: 27 layer-1 modules (the keel's two, the parts' 24 and the shared `sgia-interpretation-time.l4`), 26 test modules (one per layer-1 module of a part, the keel's tests, and the seat cases), and the seat.
The coverage tables count the units of the text in the keel (64 rows), `ea1` (379), `ea2` (363) and `ea3` (306); the encoders' own splits into encoded, fork, inert and repealed are in each part's notes.

## The seat

The seat is the one the keel's brief gave the parts: an employee working in Singapore (or about to start), asking on facts they can state whether the Act covers them, what they are owed, when, and what they can do if it is not given.
Each part's questions are phrased as that person asks them ("Under section 81, is it not lawful for my employer to ...?") and each has at least one case; the lead's gate found every one of the 494 questions called by a case.
The departures from the guide's seat defaults are in each part's notes, section "Seat".

## Dependencies

- **Interpretation Act 1965 (Singapore):** `sgia-interpretation-time.l4`, the Commons module `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-interpretation-time.l4` (blob fe60ab2c1f2326a5b061e163761bd63e4f47e12a, from Commons main d468311a6), copied unchanged with its three-line header. It supplies s 50: how a period of days is counted and the move of a last day off a Sunday or public holiday. Imported by `ea1-part3a-payment.l4`, `ea1-part4a-rest-hours.l4` and `ea1-part6-contractors.l4`, by `ea2-part-9a.l4`, `ea2-part-12-records.l4` and `ea2-duties.l4`, and by `ea3-claims.l4`, `ea3-schedules.l4`, `ea3-procedure.l4` and `ea3-penalties.l4`. Each part's notes (section "Dependencies") say which provisions use it and where a part counts a period differently, for example `ea1` s 22 (fork F-22).
- **Other Acts and orders are not among the sources.** Their answers are plain inputs named after the section, to be filled later. The lists are in the parts' notes: `ea1` (the Employment Claims Act 2016, the Industrial Relations Act 1960, the Income Tax Act 1947, the Central Provident Fund Act 1953, the Enlistment Act 1970, the Criminal Law (Temporary Provisions) Act 1955, the Companies Act 1967 and the Variable Capital Companies Act 2018, the Insolvency, Restructuring and Dissolution Act 2018, the MediShield Life and CareShield Life schemes, the Trade Unions Act 1940), `ea3` (the Employment Claims Act 2016 s 2(1), the Industrial Relations Act 1960, the Evidence Act 1893, the Penal Code 1871, the Liquor Control (Supply and Consumption) Act 2015).
- **Public holidays** are a list of dates the caller gives (the Holidays Act is not among the sources).

## Unstable dialect

No unstable-dialect encoding of this Act is held in this folder.
The existing `naive-2026-10` and `baseline-2026-10` encodings of the Act are separate rows and were not used.

## What check.sh prints

`check.sh` on the merged folder, with `l4` 1.6.109 (main, 4c887e0) as the encoding's build and 1.6.108 (main, 2ae7c9b) as the second main build: 54 modules, 0 errors, 3926 assertions satisfied, 0 failed, 0 refused, and every module has the same four counts on both ("same").
`srcrefs.py check --refs` against the converted texts in `registers/source-bundle/`: 4,372 `src:` lines checked clean over the 53 modules that quote the Employment Act or the Notification; `sgia-interpretation-time.l4` quotes the Interpretation Act and is excluded.

## Independent test pass

Each part's reviewer worked from the text alone (its notes, progress files and own tests were withheld), wrote its answers first, then asserted them against the encoding.
After the encoders' repairs the lead ran the reviewers' assertions again; the only edits to a reviewer's file were to arguments or names, listed below.

| part | scenarios | assertions | first run: satisfied / failed | after repair: satisfied / failed |
| --- | --- | --- | --- | --- |
| ea1 | 273 | 262 | 222 / 40 | 240 / 22 |
| ea2 | 269 | 258 | 239 / 19 | 246 / 12 |
| ea3 | 255 | 235 | 206 / 29 | 230 / 5 |

- **What the remaining failures are.** `ea1`: 22, all either the reviewer's own mistake, withdrawn by the reviewer, or a reading the encoder left as an open question with a "reviewer expected JUST FALSE/TRUE; open question" line in its fork register (s 14(1), the s 33 and s 35 salary ceilings, the s 22 day count, s 26(1), s 38(2) list, s 38(8), s 40(1) and (3), s 48(3), s 65(1)). `ea2`: 12; eight are open questions in the fork register (s 79(1), s 80(3), s 82 day count, s 88(3), s 74, s 89(4)(b), the Notification schedule, and the domestic worker) and four are older functions that ask the opposite question to the text's ("keeps", "may be published", "may detain", "lawful"), kept beside the new twins that ask the text's own question. `ea3`: 5; the s 115(2) look-back, s 124(1)(a), s 126D(2), s 132, and the domestic worker.
- **The domestic worker.** The `ea2` reviewer's scenario 6 and the `ea3` reviewer's scenario 5 expected `JUST FALSE` for a domestic worker through a part's function; the exclusion is in the keel's definition of "employee" (s 2(1)), and the parts take that answer as an input, so these two still fail. Not repaired at the merge.
- **Edits to the reviewers' files (arguments and names only).** `ea3`: the record of weeks for the Third Schedule item 5 gained fields (the same empty lists were assigned to them), `s 116(1)` gained an argument (the reviewer's cases pass that the sum is payable to a workman, except the non-workman case, which passes FALSE), `s 127` gained an argument. `ea2`: the s 81 seat question was renamed to ask "is it not lawful ..."; the reviewer's scenario 6 for it keeps its meaning but its expected value changed from `JUST FALSE` ("may ... lawfully") to `JUST TRUE` ("is it not lawful"), the exact negation. `ea1`: none.

## What would need doing before the encoding is worth relying on

- A lawyer reads the readings each part flags (`notes/<part>-NOTES.md`, "Marginal readings for a lawyer" and the fork register) and rules on them; none is ruled here beyond Meng's four rulings above.
- The converted text is checked against the official Singapore Statutes Online text, including the tables the converter may have omitted.
- The inputs the Act leaves to regulations, orders and other Acts are filled from their texts.
- The `NEEDS-CORE` requests of `ea2` and `ea3` are decided, and the three parts' seat wiring types are unified if the core takes the Yes / No / I am not sure type.
- The compliance-when-no-duty-arises pattern is decided for the whole Act (see the merge decisions).
- The two failing domestic-worker assertions are settled by wiring the keel's definition of "employee" into the functions that need it, or by recording that the parts must be given that answer.
