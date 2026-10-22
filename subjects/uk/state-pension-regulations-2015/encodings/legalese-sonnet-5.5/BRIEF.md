# Encoding brief: the State Pension Regulations 2015, in L4 (stable)

You are producing a full L4 encoding of the State Pension Regulations 2015 (S.I. 2015/173) from the English-language text deposited in `INPUTS_DIR`.
This brief is the whole specification. Read it fully before opening any source.

You are the ONLY encoder: no ontology agent, no fleet, no integrator, no independent test author, no subagents.
You do all of it in one context and you check your own work with the diagnostics.

## What you are building: two layers

**Layer 1: the law, objectively.** The whole text, as isomorphic and tested L4 modules that follow the text's own structure (one module per Part or natural group, a nouns module first if you need one).
Layer 1 is written from the text alone. It takes nobody's point of view: a reader holding the text beside a module checks it line by line, and every rule carries a source citation.

**Layer 2: one thin seat layer over it.** Commons requires every Act to be asked about from the position of the individual to whom the law is applied (the "seat"), because the Legalese website turns such a layer into a question form.
Here the seat is: **a person who is, or will become, entitled to the State Pension, asking what these Regulations mean for when and how their State Pension is claimed, paid and affected by their choices.**
The layer is the two files `spr-seat.l4` and `spr-cases-seat.l4`. It IMPORTs the layer-1 modules and calls their rules; it never restates or copies a rule, and no layer-1 module changes to suit it.
Each question has `@export` and `@desc`, takes plain inputs (one per fact the person can state, each `@desc` worded as that person would be asked), and the questions are grouped under `§` headings in the text's natural order.
Read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md` before you write any L4. `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` is a finished seat layer for a different Act and shows the shape (it imports modules you cannot see; copy its shape, not its content).
Questions are phrased as the person asks them ("Must I ...?", "Am I entitled to ...?"), and the facts are ones that person could state. Provisions that address only an official are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person (what may be done to them, what they must be given, and by when). There is never a seat for an official.

**Rights and duties come in pairs (Hohfeld).** A question about what the person is owed cannot be answered apart from the other party's side of the same relation. Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability. Read the other way, a power the other party holds over the person is the person's liability.
So, in layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In layer 2, wherever the text gives the person a claim, privilege, power or immunity, take as plain inputs the facts about the other party on which the text makes it depend (whom the duty binds, what that party has done or failed to do, any condition on their side). Where the text also puts a duty or a liability on the person, add the paired question ("What do I owe ...?", "What can be done to me if ...?"). Where the other party is an official, their duties and liabilities appear as what the person is owed or exposed to, never as a seat of their own.
In `NOTES.md` add a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`.

## The subject and the sources

- **the State Pension Regulations 2015**, S.I. 2015/173.
- Source file(s) in `INPUTS_DIR`: `uksi-2015-173.txt`.
- `inputs/SOURCES.md` records where each came from, its version or currency date, its URL and its hashes. **Read it.**
- Each `.txt` is a plain-text rendering of the official source made by a converter script; it is not the official text and it is not marked up. Say so in `NOTES.md` and in your `SOURCE-LICENSE.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited. Your `SOURCE-LICENSE.md` points at it and does not repeat it.
- Encode only from these files. Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory.
These are regulations made under Acts that are not among your inputs. Where a regulation depends on a provision of a parent Act, take that provision's effect as a stated input and say so in NOTES.md.

All inputs are under `INPUTS_DIR` (given in your task). Read them there and nowhere else.

## Scope, pinned

- **Every section, subsection, schedule and table of the text in `INPUTS_DIR`.** Build the coverage table from the text itself, one row per section (and per schedule), with a disposition for each: `encoded`, `inert` (with a reason of real length), `repealed or blank in this text` (say what the text shows), or `not applicable`.
- The defaults ruled for Commons (guide section 4) apply: the Act alone, plus the instruments that set its numbers or dates if they are among your inputs, otherwise make the number an input and say so; the actors the text names; a judgment the text hands to someone else becomes a conditional input ("..., if the officer is satisfied that ...") and is never guessed; the Act's own definitions are worked out from facts, borrowed terms are asked as facts; one case is the text's natural unit; the Act's own words, each with a plain gloss in a comment; boards, commencement and regulation-making machinery out (mark them `inert` in the coverage table, with a reason).

## What this text needs, specifically

The text confers or governs an entitlement to a payment or a status. Layer 1 encodes, section by section: who qualifies, the conditions and the dates they are tested at, how the amount or the length is worked out, what has to be claimed or notified and by when, what ends, suspends or reduces it, and recovery or overpayment where the text has it.
Amounts, rates, thresholds and periods that the text leaves to regulations, orders or a minister's decision, and that are not among your inputs: plain inputs with a comment saying so, never invented. Where the text itself states a figure, encode the figure.
Provisions that address only an official (powers to make regulations, appeals machinery, how an officer decides) are `inert` in layer 1 with a reason of real length, unless they decide something for the person, in which case encode what they mean for that person.
Forks to look at: the date at which each condition is tested; whether conditions are cumulative or alternative on the words of the text; what the text does when two rules overlap; every place the text defers to something you do not have. "No ambiguities found" is a claim a reviewer will not believe; say where you looked.


## Writing L4 that the stable binary accepts (from the Commons guide, section 5, verbatim)

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Smaller gaps:** `YMD` is missing from the stable prelude, so add a local shim (`YMD y m d MEANS Date d m y`). `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.

Your binary is the stable build, so anything it rejects is not available to you. Where the skills you are told to read describe a construct the stable binary rejects, the binary governs; say so in `NOTES.md` under the finding "What the stable binary does not accept".

## Deliverables, all under your `DEPOSIT` directory (given in your task)

`DEPOSIT` holds exactly one directory, laid out so that it can be copied as it stands into `subjects/uk/state-pension-regulations-2015/`:

```
DEPOSIT/
  encodings/legalese-sonnet-5.5/
    spr-*.l4        layer 1: every module of the law (flat folder: IMPORT finds only modules beside it)
    spr-seat.l4     layer 2: the seat's questions
    spr-cases-seat.l4   layer 2: worked cases, one per question at least
    tests, check.sh, srcrefs.py, NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md (a copy of this brief)
```

All `.l4` files sit directly in that folder (no subfolders), have ASCII filenames beginning with `spr-`, and never define the same name as another module that is imported with it.
You do not write `subject.json`, `README.md` or `source/`: the subject already exists and is not yours to change.
`encoding.json` and `SOURCE-LICENSE.md` follow `references/canon-deposit.md` of the `encoding-a-subject` skill: status `draft`, `not_reviewed` saying no domain expert has read it against the text, `"seat": "<the seat in one line>"`, the scope and the edition encoded, the checks run, and the `L4_BIN` path with its sha256.
The encoding's name is `legalese-sonnet-5.5`; the method is a single Sonnet 5.5 agent working alone from this brief.

`NOTES.md` carries: a `## Seat` section naming the seat and why; the `## Jural relations` table; what is encoded and what is not; the coverage table; a **fork register** (every ambiguity, the readings you saw, the one you took, the text that licenses each); numbered findings ("What the text turns out to say"), each ending "Asserted." where a case asserts it; what the stable binary does not accept; what `check.sh` prints; what would need doing before the encoding is worth relying on.

## Your context will be compacted: make the disk your memory

This run may exceed your context window, and the harness will then compact your context into a summary. So write as you go, not at the end:

- Keep `NOTES.md`'s coverage table and fork register on disk, and update them after each section you finish.
- Keep `PROGRESS.md`: sections done, sections in progress, what is next, decisions taken (with the section that licenses each), and a list of the files you have written.
- After any compaction, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary of them.

## Tests

Expected values come from the text, never from your code, and are written beside the assertion.
Decide each expected answer by reading the section, write it down, then run. A failing assertion is a finding: never edit an expected value to match what the code computed.
Cover at least: every branch of each rule you encode; the boundary values on each side of every threshold; every question in the seat layer, with the facts a real person in the seat would state; and a case outside the encoding (an explicit "not covered" value, asserted).
If you keep some expectations meant to fail, put them in their own file, count them, record them in `NOTES.md` as a finding, and list them in `check.sh`'s `expected_failed`.
Every case file ends with assertions written equal to assertions satisfied.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/porridge/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here, and you do not deposit into a repository) and `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/porridge/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** Cite the section on every rule with `@ref`; follow `encoding-a-subject/references/source-locators.md` for quoting and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>`; it must report 0 problems.
- **Where the source does not answer,** return an explicit "not covered" value (a constructor or `NOTHING`) and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails; a failure is a `DiagnosticSeverity_Error` line and a refusal is a Warning. Report the numbers `check.sh` prints. Run it as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` (the word `unstable` here only tells the script not to compare with a second binary: your binary is already the stable one).
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file except a registered, deliberately failing one.
- **No sleep-polls and no waiting loops**: there is nothing to wait on. Run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.98, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.

## Independence

Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`, no directory under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/porridge/runs` other than your own `porridge-uk-spr/`, and nothing under `~/.claude/` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
The one exception is `inputs/EXAMPLE-sg-employment-act-seat/`, which is yours to read.
The answers must come from the text alone. You may read `INPUTS_DIR`, the two skills and their references, and the Commons guide copies in `inputs/`.
Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) the coverage table summary (counts per disposition); (4) the forks you took, each in a line with the reading chosen; (5) the seat's questions, one line each; (6) any failing or refused assertion and what it means; (7) what the source does not answer; (8) `peeked`: nothing, or what you opened by accident.
