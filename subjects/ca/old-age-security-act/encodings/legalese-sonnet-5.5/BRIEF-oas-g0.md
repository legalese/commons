# Keel brief: the shared vocabulary of the Old Age Security Act and the Old Age Security Regulations (L4, stable)

You are the **keel agent** for the encoding of the Old Age Security Act and the Old Age Security Regulations (R.S.C. 1985, c. O-9 and C.R.C., c. 1246), from the English-language text deposited in `INPUTS_DIR`.
After you finish, 3 part agents will each encode one contiguous piece of the text, at the same time, each in its own folder and unable to see the others.
They will import the modules you write, and they will take their facts about the whole text from your notes.
So what you write is the keel they build on: a name, a type or a convention you get wrong is copied into 3 pieces.
This brief is the whole specification. Read it fully before opening any source.

You work alone: no subagents. You check your own work with the diagnostics.

## What you are building

1. **The core module `oas-core.l4`**: the shared vocabulary, as `DECLARE`d records and enumerations, for the people, things, measures and kinds that the text names and that two or more pieces will need.
   Examples of what belongs: the kinds of person and body the text names; the kinds of the main thing the text governs; enumerations the text lists; units (money, percentage, days) and the one way they are written; the one way a time limit is written.
   A type used by one piece only does not belong: that piece defines it. Keep the core as small as it can be; around 250 lines is a guide and not a limit.
   It imports only `prelude` (and `daydate` if you need dates).
2. **The encoded interpretation provisions of your range, if you have one**, as tested layer-1 modules `oas-core-<topic>.l4` that import the core: every definition the text gives that can be worked out from facts becomes a rule (a function from the facts to the defined concept), each with `@ref` and a quoted source line; a definition that points to a provision outside your range ("has the meaning in regulation 89") is not encoded by you: record it in the table of defined terms, naming the piece that encodes it, and give the term a plain input type in the core only if two or more pieces will need it.
   Your range: lines 13-91 of `R.S.C.-1985-c.-O-9.txt` (1,801 words): the Act's interpretation provisions: sections 2, 2.1 and 2.2 (definitions and the amount of a full monthly pension), with the vocabulary shared by the Act and the Regulations.
3. **Tests**: files `oas-core-tests-<topic>.l4` with assertions for the core's rules and the definitional rules, expected values written from the text.
4. **`NOTES.md`**, which is the shared notes for all the pieces and must say, under exactly these headings:
   - `## Vocabulary`: a table `| name | kind | what it is | licensed by |` of every type and enumeration constructor in the core;
   - `## Naming conventions`: how a rule, an input, an enumeration constructor and a question are named; how amounts, percentages, days and dates are written (the type, the unit, and what a fraction is); how a fact about something outside a piece is taken as an input; anything else two pieces would otherwise do differently;
   - `## Defined terms`: a table `| term | defined at | encoded in | note |` for every term the text defines (in your range or by pointing elsewhere), giving the module and rule that encode it, or "by reference: encoded by piece X, section N, taken there as an input";
   - `## Instructions to the pieces`: a short list of things a part agent must know before it imports your modules;
   - `## Coverage table` (your range, the rule below); `## Fork register`; `## What the stable binary does not accept`; `## What check.sh prints`.
5. **`PROGRESS.md`**: kept up to date as you go.

## The whole range, nothing left out (ruled by Meng, 2026-10-22)

The whole text is encoded in one pass; nothing is left out because it matters little to the seat.
If you have a range, your coverage table has one row per provision of it (per section, and per subsection or paragraph where they differ), with the columns `| provision | source lines | disposition | where | note |`, and a disposition of `encoded`, `inert` (machinery, an amendment of another instrument, an amendment the source shows as not in force, or a pure citation or title, with a reason of real length), `repealed or blank in this text`, or `fork`.
"Out of the seat's scope" is never a reason. A reviewer will count the headings in your range against your rows.

## The pieces that will import your modules

| piece | what it encodes | lines | words | first and last section label opening in it |
| --- | --- | --- | --- | --- |
| oas-g0 (keel) | the Act's interpretation provisions: sections 2, 2.1 and 2.2 (definitions and the amount of a full monthly pension), with the vocabulary shared by the Act and the Regulations | R.S.C.-1985-c.-O-9: 13-91 | 1,801 | R.S.C.-1985-c.-O-9: 2 to 2.2 |
| oa1 | the Act's title and section 1, Part I (monthly pension), Part IV (general), and the Related Provisions and Amendments Not in Force at the end of the Act's file | R.S.C.-1985-c.-O-9: 1-12; R.S.C.-1985-c.-O-9: 92-226; R.S.C.-1985-c.-O-9: 823-1239 | 12,688 | R.S.C.-1985-c.-O-9: 1 to 1; R.S.C.-1985-c.-O-9: 3 to 9.3; R.S.C.-1985-c.-O-9: 26.1 to 26.02 |
| oa2 | the Act's Part II (monthly Guaranteed Income Supplement) and Part III (monthly Allowances) | R.S.C.-1985-c.-O-9: 227-822 | 14,908 | R.S.C.-1985-c.-O-9: 10 to 26 |
| oa3 | the whole of the Old Age Security Regulations, C.R.C., c. 1246: Part I (applications), Part II (reconsiderations) and the Schedule | C.R.C.-c.-1246: 1-418 | 9,457 | C.R.C.-c.-1246: 1 to 48 |

Use the table to say, for each defined term, which piece encodes the provision it points to.
The seat the pieces will write for, so that you choose types a person in that position can supply facts for, is: a person who is 65 or older, or approaching it, asking whether they qualify for the Old Age Security pension, the Guaranteed Income Supplement or an Allowance, how much they would receive, and what they must do or tell the Minister.
You write no seat layer and no `@export`.

## Reading

Read the headings of the whole text first, through `inputs/SECTION-INDEX.txt` and `grep -n` for `PART`, `Part`, `CAPÍTULO`, `SCHEDULE` and similar lines of the text file; then read your range in full with `sed -n 'A,Bp'`; then sample the sections where the main entities are introduced, enough to choose the types.
**Never read a whole text file in one go**: the texts are far longer than you need.
Also read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md` before you write any L4, and `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` for the shape of a seat layer (which you do not write).

## The subject and the sources

- **the Old Age Security Act and the Old Age Security Regulations**, R.S.C. 1985, c. O-9 and C.R.C., c. 1246.
- Source file(s) in `INPUTS_DIR`: `R.S.C.-1985-c.-O-9.txt`, `C.R.C.-c.-1246.txt`. Each line number in this brief refers to lines of those files.
- `inputs/SOURCES.md` records where each came from, its version or currency date, its URL and its hashes. **Read it.**
- Each `.txt` is a plain-text rendering of the official source made by a converter script; it is not the official text and it is not marked up. Say so in `NOTES.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited.
- `inputs/SECTION-INDEX.txt` lists, by line number, where each section or regulation opens, with the heading it sits under; it was made by a script, so the text is authoritative.
- Encode only from these files. Quote the text mechanically; never reconstruct wording from memory.
Both the Act and the Old Age Security Regulations are among your inputs. Use the Regulations' figures and conditions where the Act leaves them to regulations, and say in `NOTES.md` which instrument each rule comes from. The Act and the Regulations are two separate text files. The Act's text ends with `RELATED PROVISIONS` (from line 1146 of the Act: transitional and savings provisions of amending Acts, shown for information) and `AMENDMENTS NOT IN FORCE` (from line 1176: amendments the source shows as enacted but not yet in force, which change nothing today); both belong to piece oa1. Encode a related provision for what it still decides for a person, and mark one that is spent `inert` with that reason. Mark each amendment not in force `inert`, naming the section it would amend, and never merge its wording into the rules for the text in force. The Regulations end with a Schedule from line 373 of the Regulations file.

## Writing L4 that the stable binary accepts

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Smaller gaps:** `YMD` is missing from the stable prelude, so add a local shim (`YMD y m d MEANS Date d m y`). `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.

The target dialect is `main`: the stable build 1.6.98 named as L4_BIN. Read step 0 of `writing-l4-rules/SKILL.md` and `references/dialects.md` (its "write instead" column) before you write; for any construct the stable binary rejects, write what `dialects.md` says to write instead.

Dates are data. Where your range contains the date of enactment or making of the text, or the date it comes into force, or a commencement rule, carry it as a defined value with an `@ref`: the date in the title block or the assent date if the text gives one, and any commencement date the text fixes or defines by a rule such as "three months after passing", derived from the enactment date where the text says so. Where the text leaves commencement to an order, take the commencement date as a stated input and say so in `NOTES.md`. These dates are what rule-effective-date logic needs; they are not "commencement machinery", which stays out. If your range contains no such provision, say so in `NOTES.md` and do nothing.

## Deliverables, all under your `DEPOSIT` directory (given in your task)

`DEPOSIT/encodings/legalese-sonnet-5.5/` already holds `check.sh` and `srcrefs.py`. You add, flat in that folder (no subfolders, ASCII filenames beginning `oas-core`): `oas-core.l4`, any `oas-core-<topic>.l4` interpretation modules, the `oas-core-tests-*.l4` tests, `NOTES.md` and `PROGRESS.md`.
You do not write `encoding.json`, `SOURCE-LICENSE.md`, `subject.json`, `README.md` or `source/`, and you do not copy this brief.
Write `NOTES.md` and `PROGRESS.md` yourself and nothing else of the report kind: the harness refuses to let a subagent write report-style files (`FINDINGS.md`, `REPORT.md`, `PLAN.md` and the like) and tells you to return findings as text. The pieces will read your `NOTES.md` as their guide, so it is the one place to put the plan. Your last message is the final report, and the files in the folder are the deliverable.
Keep `PROGRESS.md` current (what is done, what is next, decisions taken and the section that licenses each): if your context is compacted, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/t2/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here) and `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/t2/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Cite the section on every rule with `@ref`**; follow `encoding-a-subject/references/source-locators.md` for quoting and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>`; it must report 0 problems. The Act is `R.S.C.-1985-c.-O-9.txt` and the Regulations are `C.R.C.-c.-1246.txt`: check the Act's modules against the Act file and the Regulations' modules against the Regulations file, in one `srcrefs.py check --refs` run each.
- **Where the source does not answer,** return an explicit "not covered" value and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** Run `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` and report the numbers it prints: it must show 0 errors, 0 failed and 0 refused.
- **The core must compile before you finish**, and every module you wrote must be importable by a file in the same folder: write a three-line throwaway file that imports each module and calls one of its rules, run it, and delete it.
- **No sleep-polls and no waiting loops.** Do not git add, commit or push anything. Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.98, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.

## Independence

You may read: `INPUTS_DIR`, your own `DEPOSIT`, the two skills and their references, and the Commons guide copies in `inputs/`. Nothing else on disk.
Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`; nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/t2` other than your own folder `oas/keel/`; nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/porridge` except that you run the `L4_BIN` binary named in your task; and nothing under `~/.claude/`.
The one exception is `inputs/EXAMPLE-sg-employment-act-seat/`, which is yours to read.
If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) the vocabulary in one line per type; (4) the naming conventions in one line each; (5) the defined terms and where each is encoded, counted by kind; (6) the coverage summary for your range (counts per disposition, and sections in your range against rows); (7) forks; (8) anything a part agent will trip on; (9) `peeked`: nothing, or what you opened by accident.
