# Encoding brief: Magna Carta (1215), whole, in L4 (stable)

You are producing a full L4 encoding of Magna Carta (1215) (the Great Charter of King John, as the English translation in the source file prints it) from the English-language text deposited in `INPUTS_DIR`.
This brief is the whole specification. Read it fully before opening any source.
You are the ONLY encoder: no ontology agent, no fleet, no integrator, no independent test author, no subagents. You do all of it in one context and check your own work with the diagnostics.

## What you are building: two layers

**Layer 1: the law, objectively.** The whole text, as isomorphic and tested L4 modules that follow the text's own structure (one module per Part or natural group, a nouns module first if you need one). It is written from the text alone and takes nobody's point of view: a reader holding the text beside a module checks it line by line, and every rule carries a source citation.

**Layer 2: one thin seat layer over it.** Commons requires every body of law to be asked about from the position of the individual to whom the law is applied (the "seat"), because the Legalese website turns such a layer into a question form.
Here the seat is: **a person living under King John's rule who is not the King, a free man, a widow, an heir, a merchant, a tenant who holds land by military service, someone who owes money, asking on facts they can state what the Crown and its officers may and may not do to them under the Charter and what it gives them: for example "May the King imprison me or take my land without a judgment of my peers?", "What relief must my heir pay?", "May I be made to marry again?", "May a merchant leave and enter the country safely?", "Where and by whom may my case be heard?".**
The layer is the two files `mc15-seat.l4` and `mc15-cases-seat.l4`. It IMPORTs the layer-1 modules and calls their rules; it never restates a rule, and no layer-1 module changes to suit it.
Each question has `@export` and `@desc`, takes plain inputs (one per fact the person can state, each `@desc` worded as that person would be asked), and the questions are grouped under `§` headings in the text's natural order.
Read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md` before you write any L4. `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` is a finished seat layer for a different Act and shows the shape (it imports modules you cannot see; copy its shape, not its content).
Questions are phrased as the person asks them ("Must I ...?", "Am I entitled to ...?"). Provisions that address only an official or the King's own acts are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person. There is never a seat for an official.

## What "whole" means (Meng's ruling of 2026-10-22, applied to this text)

Every provision of the text, that is every section, subsection, paragraph, schedule, table row and defined term, has a row in the coverage table, and each row has exactly one disposition:
- `encoded`: a rule, definition or table in layer-1 L4, with a test, citing the provision with `@ref`.
- `inert`: allowed ONLY for the three reasons below.
- `fork`: the text can be read two or more ways with different outcomes. The row points at the fork-register entry (every reading, and the text that licenses each) and at the rule that encodes the chosen reading, or at the explicit "not covered" value when the text does not choose.
- `repealed or blank in this text`: say what the text shows.

There is no `out-of-scope` row and no `deferred` row.

The three reasons for `inert`, and no others:
1. Not operative: the title, long title, enacting words, headings, the date of enactment, a purpose or objects clause that creates no rule.
2. Machinery (Guide section 4): boards and offices and their staffing, the text's own commencement, short title and extent, regulation-making and rule-making powers, savings and transitional provisions that affect no one now, amendments of other Acts.
3. Text shown repealed or blank.

These are NOT reasons. Earlier passes used them and they no longer stand:
- "addresses an official": encode what it means for the individual: what may be done to them, what they must be given, and by when (Guide section 2).
- "an interpretive canon" or "open-textured": encode the rule, and take the open-textured judgment as a plain input.
- "refers to another text or instrument that is not among the sources": encode the provision as stated and ask the borrowed fact or term as an input (Guide section 4).
- "no input from which an answer would differ": a rule with one answer is still a rule; encode it and test it.
- "the earlier brief said it need not be coded": superseded by this brief.

A definition is encoded: a defined-term table or function that returns the term's meaning as the text states it (the members it names, what it includes or excludes, what it points at), with a test for each entry.
A rule with limbs (a condition and its exceptions) is encoded so that each limb can be tested on both sides.



## About this text

- The source is an English translation of King John's Charter, printed in a 1905 commentary and rendered to plain text by a script. It is a preamble and 63 chapters; the division is a modern convenience that the Charter does not itself make. `inputs/magna-carta-1215-mckechnie-translation.txt` has a four-line header, then "Preamble" and "Chapter 1" to "Chapter 63", one paragraph under each. The text gives its own date in chapter 63.
- Encode the text as it reads: the Charter grants, confirms, forbids and orders. You are NOT asked whether any of it is in force today or was ever carried out; make no such claim anywhere in the encoding.
- **Design (ruled by Meng, 2026-10-29: the hybrid).** For this text the encoding is RULES for the whole of it, plus the individual's seat layer: regulative rules and decision functions, as below.
- **One-off chapters are not inert.** Chapters that do something once (the return of hostages and charters, the removal of named persons from office, foreign knights sent from the country, restitution of lands taken without judgment, the five-and-twenty barons and their security, the remission of ill-will, the observance clause) are obligations or entitlements of the moment the Charter speaks. Encode each as a rule (the party, the act, the time the text gives), with a fork entry where the text does not say who may enforce it or by when. Only the three inert reasons stand.
- **Lists of names** (the persons named in the preamble and in the chapters, the witnesses) create no rule when they only name those who advised or witnessed: `inert`, reason 1. A named person who is the subject of a rule is an input or a constant, as the text says.
- **Chapter 39 and chapter 40** (the judgment of peers; no sale, refusal or delay of right or justice) are the best-known chapters. Encode what the translation says and record in the fork register every way it can be read; do not import a reading from later law or history.

## Regulative rules and decision functions

This text mostly says who must, may or must not do what to whom, sometimes by when, and what follows. Encode it the way it reads, chapter by chapter, choosing the form that is closest to the words:
- a **regulative rule** (`PARTY ... MUST / MAY / SHANT ... WITHIN ... HENCE ... LEST ...`, see `writing-l4-rules/references/regulative.md`) where a chapter imposes a duty, permission or prohibition on a named party, with its time limit and consequence if the text gives them;
- a **decision function** (a typed `DECIDE`) where the chapter fixes a sum, a rank, an entitlement, a condition for a lawful act, or a list of who is covered.
Both are tested. A regulative rule is tested by running it (`#TRACE` / `#EVAL` as the skill shows) and asserting what you can assert on the stable binary; if some regulative construct cannot be asserted on this binary, say so under "What the stable binary does not accept", encode the same duty as a decision function over the facts, and assert that.
Do not invent an actor, a deadline, a remedy or a consequence the text does not state: where it does not say who may enforce a duty, or by when, or what follows, say so in the fork register and return an explicit "not covered" value.

Words the text uses and does not define (for example: relief, scutage, aid, knight's fee, escheat, wardship, dower, quarantine, assize, novel disseisin, mort d'ancestor, darrein presentment, the Common Pleas, the Exchequer, a freeman, an earl, a baron, "the lawful judgment of his peers", "the law of the land"): do not define them from memory or from any other source. Take each as a plain input fact or a typed value, list it in a `## Terms the text does not define` section of `NOTES.md`, and put a plain gloss in a comment marked "gloss (not the text's)".
Where the text is open ("reasonable", "moderate", "lawful", "just", "competent"), take the judgment as an input.
Money and measures: keep amounts in the units the text uses (pounds, shillings, and so on); if a comparison needs a conversion the text does not give, make the conversion an input and say so.

Add to `NOTES.md` a section `## What this encoding does not claim`: that no claim is made that any provision is, or ever was, in force or applied; that the text is a translation or an extract and not the official text; and that no domain expert has read the encoding against the source.


## Rights and duties come in pairs (Hohfeld)

Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability.
In layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In `NOTES.md` keep a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`. Most provisions of this text DO create a relation (the Crown against a person, a lord against a tenant, a widow against an heir), so this section is long; it must cover the whole text.

## The subject and the sources

- **Magna Carta (1215)**, the Great Charter of King John, as the English translation in the source file prints it.
- Source file(s) in `INPUTS_DIR`: `magna-carta-1215-mckechnie-translation.txt`.
- `inputs/SOURCES.md` records where each came from, its version, its URL and its hashes. **Read it.**
- The text is not the official text (`inputs/SOURCES.md` says what it is). Say so in `NOTES.md` and in your `SOURCE-LICENSE.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited. Your `SOURCE-LICENSE.md` points at it and does not repeat it.
- Encode only from these files. Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory.
- Defaults ruled for Commons (Guide section 4): the text alone, plus instruments that set its numbers or dates if among your inputs, otherwise make the number an input and say so; the actors the text names; a judgment the text hands to someone else becomes a conditional input and is never guessed; the text's own definitions are worked out from facts, borrowed terms are asked as facts; one case is the text's natural unit; the text's own words, each with a plain gloss in a comment.
- Build the coverage table from the text itself with a script, one row per chapter, sentence or clause that states a rule, preamble paragraph, heading and unnumbered paragraph, and defined or used term, and check that every non-blank line of the text falls in some row.

## Writing L4 that the stable binary accepts (from the Commons guide, section 5; one line changed, as marked)

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Smaller gaps:** Write dates as `Date day month year` (the stable prelude has no `YMD`). **Ruled for new stable rows, superseding the Guide's older advice to add a local shim: define no `YMD`, `YearMonthDay`, `DayMonthYear` or other date shim in this row.** `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.
- **Lists:** write a list of strings as a vertical `LIST` block, one string per line, not with `•` bullets (those are a parse error on the stable binary).

Your binary is the stable build, so anything it rejects is not available to you. Where the skills describe a construct the stable binary rejects, the binary governs; say so in `NOTES.md` under the finding "What the stable binary does not accept".
## Deliverables, all under your `DEPOSIT` directory (given in your task)

```
DEPOSIT/
  encodings/legalese-sonnet-5.5/
    mc15-*.l4            layer 1: every module of the law (flat folder: IMPORT finds only modules beside it)
    mc15-seat.l4         layer 2: the seat's questions
    mc15-cases-seat.l4   layer 2: worked cases, one per question at least
    tests, check.sh, srcrefs.py, NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md (a copy of this brief)
```

All `.l4` files sit directly in that folder (no subfolders), have ASCII filenames beginning with `mc15-`, and never define the same name as another module imported with it.
You do not write `subject.json`, `README.md` or `source/`: the subject already exists and is not yours to change.
`encoding.json` and `SOURCE-LICENSE.md` follow `references/canon-deposit.md` of the `encoding-a-subject` skill: status `draft`, `not_reviewed` saying no domain expert has read it against the text, `"seat": "<the seat in one line>"`, the scope and the edition encoded, the checks run, and the `l4_bin` path with its sha256.
The encoding's name is `legalese-sonnet-5.5`; the method is a single Sonnet 5.5 agent working alone from this brief.
`NOTES.md` carries: a `## Seat` section naming the seat and why; the `## Jural relations` table; what is encoded and what is not; the coverage table; a **fork register** (every ambiguity, the readings you saw, the one you took, the text that licenses each); numbered findings ("What the text turns out to say"), each ending "Asserted." where a case asserts it; what the binary does not accept; what `check.sh` prints; what would need doing before the encoding is worth relying on.

## Your context will be compacted: make the disk your memory

This run may exceed your context window, and the harness will then compact your context into a summary. So write as you go, not at the end:
- Keep `NOTES.md`'s coverage table and fork register on disk, and update them after each section you finish.
- Keep `PROGRESS.md`: sections done, in progress, next, decisions taken (with the section that licenses each), and the files you have written.
- After any compaction, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary of them.

## Tests

Expected values come from the text, never from your code, and are written beside the assertion.
Decide each expected answer by reading the section, write it down, then run. A failing assertion is a finding: never edit an expected value to match what the code computed.
Cover at least: every branch of each rule you encode; the boundary values on each side of every threshold; every question in the seat layer (if the row has one), with the facts a real person in the seat would state; and a case outside the encoding (an explicit "not covered" value, asserted).
If you keep some expectations meant to fail, put them in their own file, count them, record them in `NOTES.md` as a finding, and list them in `check.sh`'s `expected_failed`.
Every case file ends with assertions written equal to assertions satisfied.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `<the lead's scratchpad>/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here, and you do not deposit into a repository) and `<the lead's scratchpad>/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** Cite the section on every rule with `@ref`; follow `encoding-a-subject/references/source-locators.md` for quoting and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>`; it must report 0 problems.
- **Where the source does not answer,** return an explicit "not covered" value (a constructor or `NOTHING`) and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails. Report the numbers `check.sh` prints.
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file except a registered, deliberately failing one.
- **No sleep-polls and no waiting loops**: run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.
Run the check as `L4=<L4_BIN> L4_MAIN=<the lead's scratchpad>/bin/l4-stable-102 ./check.sh` (the default target `main`: it runs every module with a second stable build as well and goes red when the two read it differently).

## Independence

Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`, no directory under `<the lead's scratchpad>/runs` other than your own `iaw-mc15/`, and nothing under `~/.claude/` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
The one exception is `inputs/EXAMPLE-sg-employment-act-seat/`, which is yours to read.
The answers must come from the text alone. You may read `INPUTS_DIR`, the two skills and their references, and the Commons guide copies in `inputs/`.
Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message; the report is your final response, not a file)

Return: (1) the list of files you wrote or changed; (2) exactly what `check.sh` printed, and the baseline numbers it replaced; (3) the coverage table summary (counts per disposition) and the audit counts (text units counted, rows in the table before and after); (4) the forks you took, one line each with the reading chosen; (5) every row you moved out of `inert` and every row you left `inert` with its reason number (1, 2 or 3); (6) any failing or refused assertion and what it means; (7) what the text does not answer; (8) `peeked`: nothing, or what you opened by accident.
Subagents cannot write report-named files such as `FINDINGS.md`; `NOTES.md`, `PROGRESS.md` and `.l4` files are fine.
