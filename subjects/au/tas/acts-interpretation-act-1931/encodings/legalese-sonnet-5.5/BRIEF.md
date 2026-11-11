# Encoding brief: Acts Interpretation Act 1931 (Tasmania), whole, in L4

You are producing a full L4 encoding of Acts Interpretation Act 1931 (Tasmania) (No. 59 of 1931 (Tasmania)) from the English-language text deposited with this brief.
This brief is the whole specification. Read it fully before opening any source.
You are the ONLY encoder: no ontology agent, no fleet, no integrator, no independent test author, no subagents. You do all of it in one context and check your own work with the diagnostics.

## What you are building: two layers

**Layer 1: the law, objectively.** The whole text. It is written as isomorphic and tested L4 modules that follow the text's own structure (one module per Part or natural group, a nouns module first if you need one). It is written from the text alone and takes nobody's point of view: a reader holding the text beside a module checks it line by line, and every rule carries a source citation.

**Layer 2: one thin seat layer over it.** Commons requires every Act to be asked about from the position of the individual to whom the law is applied (the "seat"), because the Legalese website turns such a layer into a question form.
Here the seat is: **a person who has a time limit to meet under a Tasmanian Act or statutory rule (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.**
The layer is the two files `tas-seat.l4` and `tas-cases-seat.l4`. It IMPORTs the layer-1 modules and calls their rules; it never restates a rule, and no layer-1 module changes to suit it.
Each question has `@export` and `@desc`, takes plain inputs (one per fact the person can state, each `@desc` worded as that person would be asked), and the questions are grouped under `§` headings in the text's natural order.
Read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 (section 5 includes the rulings on negatives and on `JUST FALSE` and `NOTHING`, which bind you) and `inputs/COMMONS-CLAUDE.md` before you write any L4. `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` is a finished seat layer for a different Act and shows the shape (it imports modules you cannot see; copy its shape, not its content).
Questions are phrased as the person asks them ("Must I ...?", "Am I entitled to ...?"). Provisions that address only an official are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person. There is never a seat for an official.

## What "whole" means

Whole means the whole text. Nothing in the text is skipped: every provision has exactly one disposition, and a provision that cannot be encoded says why in its row.

Every provision of the in-scope text, that is every section, subsection, paragraph, schedule, table row and defined term, has a row in the coverage table, and each row has exactly one disposition:
- `encoded`: a rule, definition or table in layer-1 L4, with a test, citing the provision with `@ref`.
- `inert`: allowed ONLY for the three reasons below.
- `fork`: the text can be read two or more ways with different outcomes. The row points at the fork-register entry (every reading, and the text that licenses each) and at the rule that encodes the chosen reading, or at the explicit "not covered" value when the text does not choose.
- `repealed or blank in this text`: say what the text shows.
There is no `out-of-scope` row and no `deferred` row.

The three reasons for `inert`, and no others:
1. Not operative: the title, long title, enacting words, headings, the date of enactment, a purpose or objects clause that creates no rule.
2. Machinery (Guide section 4): boards and offices and their staffing, the Act's own commencement, short title and extent, regulation-making and rule-making powers, savings and transitional provisions that affect no one now, amendments of other Acts.
3. Text shown repealed or blank.

These are NOT reasons:
- "addresses an official": encode what it means for the individual: what may be done to them, what they must be given, and by when (Guide section 2).
- "an interpretive canon" or "open-textured": encode the rule, and take the open-textured judgment as a plain input.
- "refers to another Act or instrument that is not among the sources": encode the provision as stated and ask the borrowed fact or term as an input (Guide section 4).
- "no input from which an answer would differ": a rule with one answer is still a rule; encode it and test it.

A definition is encoded: a defined-term table or function that returns the term's meaning as the Act states it (the members it names, what it includes or excludes, what it points at), with a test for each entry.
Rules of reading (the singular includes the plural; a reference to an Act includes amendments; and so on) are encoded as functions over a small typed representation of what the rule operates on, with tests on both sides of each limb.

## The time rules, in this Act

Other encodings of this jurisdiction's laws need executable answers from this Act to questions such as: when does an Act or an instrument come into force or begin to bind (the day, and the moment within the day); how is a period of "N days", "N weeks", "N months" or "N years" from or after a day or an event counted, and which day is its last (a start on the 31st, a start on 29 February, a month that lacks the start day's number); what happens when the last day falls on a day of rest, a holiday or a day on which an office is closed, as the text defines it; deemed service or notice; what a repeal does (effect on things done, revival, savings); and what the text says "day", "week", "month" and "year" mean.
Decide every answer from the text alone. Do not import an answer from another jurisdiction's law or from your memory of how courts treat the point. If the text has no provision on one of these, the coverage row says "the Act is silent on this", the encoding returns an explicit not-covered value, and a test asserts it. Nothing is invented.
Put the time-computation functions in ONE self-contained layer-1 module that imports only `prelude` and `daydate`, with the descriptive ASCII filename `tas-interpretation-time.l4`. Each function carries an `@ref` to the section it implements. Check how `daydate` handles a start on the 31st and on 29 February instead of assuming; if its behaviour differs from the text, the text governs and you write the rule.
This module is meant to be copied unchanged, by itself, into other work. It must therefore not import any other module of this encoding, must give every function a name that says what it computes and which section it implements, and must stand alone with its own tests in `tas-tests-time.l4`.
Forks to look at: whether a period "from" a day counts that day, and whether a period "after" an event does; whether the last day is inside the period; whether a rule that moves a last day off a rest day applies to periods in months and years or only to periods in days.
Run these worked cases and put each in an answer table in `NOTES.md` with its section citation, or say the text is silent on the question: three years from 2025-07-16; five years from 2025-01-15 and from 2025-09-01; thirty days from 2026-01-01; two months from 2025-12-31; one month from 2024-01-31; one year from 2024-02-29.


## Cross-references are data

Every reference in the in-scope text from one provision to another provision of the same text becomes a data item with a test.
Build, by a script that reads the text file, a provision index module `tas-provisions.l4`: one entry per provision (section, Part, Schedule, clause) with its identifier as printed and its heading as printed.
Build a cross-reference module `tas-xrefs.l4`: one row per reference, with the citing provision, the words of the citation as printed, the identifier it cites, and the heading of the cited provision as the text prints it. A test per row asserts that the cited identifier is in the index and that the row's heading is the index's heading for it.
A reference to another Act or instrument is a row of its own kind, carrying the instrument and provision as printed; it is not resolved here (the borrowed fact is asked as an input where a rule needs it).
Say in `NOTES.md` how many references there are, by kind, and how the script finds them.

## Rights and duties come in pairs (Hohfeld)

Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability.
In layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In `NOTES.md` keep a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`. In an interpretation Act most provisions create none, so this section is short; it must still cover the whole in-scope text.

## The subject and the sources

- **Acts Interpretation Act 1931 (Tasmania)**, No. 59 of 1931 (Tasmania).
- Source file(s): `act-1931-059.txt`, in the subject's `registers/source-bundle/` folder; from your encoding folder the path is `../../registers/source-bundle/`.
- `inputs/SOURCES.md` records where each came from, its version, its URL and its hashes. **Read it.**
- The text is a plain-text rendering made by a converter script (or taken from a third-party corpus where the deposit notice says so); it is not the official text. Say so in `NOTES.md` and in your `SOURCE-LICENSE.md`, and do not claim anything is "verified against the official text".
- The subject-level licence note is in the subject folder's `SOURCE-LICENSE.md`; your `SOURCE-LICENSE.md` points at it and does not repeat it.
- Encode only from these files. Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory.
- Defaults ruled for Commons (Guide section 4): the Act alone, plus instruments that set its numbers or dates if among your inputs, otherwise make the number an input and say so; the actors the text names; a judgment the text hands to someone else becomes a conditional input and is never guessed; the Act's own definitions are worked out from facts, borrowed terms are asked as facts; one case is the text's natural unit; the Act's own words, each with a plain gloss in a comment.
- Build the coverage table from the text itself with a script, one row per section, subsection, schedule paragraph, defined term and table row, and check that every non-blank line of the in-scope text falls in some row. Keep the script outside the deposit.

## Writing L4 that the stable binary accepts (from the Commons guide, section 5)

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). A name defined in two imported modules cannot be used at all.
- **Dates: write `Date day month year`** and never define a `YMD` or `YearMonthDay` of your own. `Date` rolls an impossible date forward (`Date 29 2 2023` is 1 March 2023); check how `daydate` behaves instead of assuming.
- **Smaller gaps:** `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in the seat layer. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before finishing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a statement of what the Act provides.

Your binary is the stable build, so anything it rejects is not available to you. Where the skills describe a construct the stable binary rejects, the binary governs; say so in `NOTES.md` under "What the stable binary does not accept".

## Rulings on `JUST FALSE` and `NOTHING` (Guide section 5; they bind you)

A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless", a list the text closes with "only", a flat negative.
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
A period the text fixes in its own words: outside it, `JUST FALSE`. A "where ..." condition that fails: `JUST FALSE`. A scope limit with no "only": `NOTHING`.
Questions the rulings do not settle are decided at each site on the text's own words, with one fork line in the fork register (the provision, the function, the answer taken, the other reading).

## Deliverables, all under your `DEPOSIT` directory

```
DEPOSIT/
  encodings/legalese-sonnet-5.5/
    tas-*.l4         layer 1: every module of the law (flat folder: IMPORT finds only modules beside it)
    tas-seat.l4         layer 2: the seat's questions
    tas-cases-seat.l4   layer 2: worked cases, one per question at least
    tests, check.sh, fetch-main-l4.sh, srcrefs.py, NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md
```

All `.l4` files sit directly in that folder (no subfolders), have ASCII filenames beginning with `tas-`, and never define the same name as another module imported with it.
You do not write `subject.json`, `README.md` or the source folder: the subject already exists and is not yours to change.
`check.sh`, `fetch-main-l4.sh` and `srcrefs.py` are already in your folder; do not edit them.
`encoding.json` and `SOURCE-LICENSE.md` follow `references/canon-deposit.md` of the `encoding-a-subject` skill: status `draft`, `not_reviewed` saying no domain expert has read it against the text, `"seat": "<the seat in one line>"`, the scope and the edition encoded, the checks run, and `l4_bin` as the binary's version line and sha256 (no file path).
The encoding's name is `legalese-sonnet-5.5`; the method is a single Sonnet 5.5 agent working alone from this brief. The `encoder` field says exactly that and names nobody else.
`NOTES.md` carries: a `## Seat` section naming the seat and why; the `## Jural relations` table; what is encoded and what is not; the coverage table; a **fork register** (every ambiguity, the readings you saw, the one you took, the text that licenses each); numbered statements of what the text provides ("What the Act turns out to say"), each ending "Asserted." where a case asserts it; what the binary does not accept; what `check.sh` prints; what would need doing before the encoding is worth relying on. `NOTES.md` states the current reading of the encoding; it is not a log of how you got there.
Write markdown one sentence per line.

## Your context will be compacted: make the disk your memory

This run may exceed your context window, and the harness will then compact your context into a summary. So write as you go, not at the end:
- Keep `NOTES.md`'s coverage table and fork register on disk, and update them after each section you finish.
- Keep `PROGRESS.md`: sections done, in progress, next, decisions taken (with the section that licenses each), and the files you have written.
- After any compaction, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary of them.

## Tests

Expected values come from the text, never from your code, and are written beside the assertion.
Decide each expected answer by reading the section, write it down, then run. A failing assertion is information about your reading: never edit an expected value to match what the code computed; re-read the text and decide which of the two readings the text supports.
Cover at least: every branch of each rule you encode; the boundary values on each side of every threshold; every question in the seat layer, with the facts a real person in the seat would state; and a case outside the encoding (an explicit "not covered" value, asserted).
Every case file ends with assertions written equal to assertions satisfied.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `inputs/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here, and you do not deposit into a repository) and `inputs/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** Cite the section on every rule with `@ref`; follow `inputs/skills/encoding-a-subject/references/source-locators.md` for quoting and run `python3 -I srcrefs.py check --refs <the text file> <your .l4 files>`; it must report 0 problems, and so must the same with `--strict`.
- **Encode the text as printed.** Where the text is silent, or cites something that is not among the sources, the encoding says only what the text says and asks the borrowed fact as an input.
- **Where the source does not answer,** return an explicit "not covered" value (a constructor or `NOTHING`) and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails. Report the numbers `check.sh` prints.
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file.
- **No sleep-polls and no waiting loops**: run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The writing binary is the stable build, version 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`, and `check.sh` also runs every module with a second build, 1.6.110 (main, e51181d, 2026-11-11), and goes red when the two read a module differently. Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`<l4> check FILE` typechecks; `<l4> run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path (given in your task prompt).

## Independence

Do not read any existing encoding of any Act. You may read the text, the two skills and their references, and the Commons guide copies in `inputs/`.
The answers must come from the text alone. If you open a forbidden file by accident, stop reading it and say so under `peeked`.
