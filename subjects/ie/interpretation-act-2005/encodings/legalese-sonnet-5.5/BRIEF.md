# Completion brief: the Interpretation Act 2005 (Ireland), to "whole" in L4 (unstable)

You are completing an existing, draft L4 encoding of the Interpretation Act 2005 (Ireland) (No. 23 of 2005) so that every provision of the text is accounted for to the standard below.
This brief is the whole specification. Read it fully before opening any source.
You are the ONLY agent on this row: no subagents. You work in one context and check your own work with the diagnostics.

## What "whole" means (Meng's ruling of 2026-10-22, applied to this Act)

Every provision of the text, that is every section, subsection, paragraph, schedule, table row and defined term, has a row in the coverage table, and each row has exactly one disposition:
- `encoded`: a rule, definition or table in layer-1 L4, with a test, citing the provision with `@ref`.
- `inert`: allowed ONLY for the three reasons below.
- `fork`: the text can be read two or more ways with different outcomes. The row points at the fork-register entry (every reading, and the text that licenses each) and at the rule that encodes the chosen reading, or at the explicit "not covered" value when the text does not choose.
- `repealed or blank in this text`: say what the text shows.

There is no `out-of-scope` row and no `deferred` row.

The three reasons for `inert`, and no others:
1. Not operative: the title, long title, enacting words, headings, the date of enactment, a purpose or objects clause that creates no rule.
2. Machinery (Guide section 4): boards and offices and their staffing, the Act's own commencement, short title and extent, regulation-making and rule-making powers, savings and transitional provisions that affect no one now, amendments of other Acts.
3. Text shown repealed or blank.

These are NOT reasons. Earlier passes used them and they no longer stand:
- "addresses an official": encode what it means for the individual: what may be done to them, what they must be given, and by when (Guide section 2).
- "an interpretive canon" or "open-textured": encode the rule, and take the open-textured judgment as a plain input.
- "refers to another Act or instrument that is not among the sources": encode the provision as stated and ask the borrowed fact or term as an input (Guide section 4).
- "no input from which an answer would differ": a rule with one answer is still a rule; encode it and test it.
- "the earlier brief said it need not be coded": superseded by this brief.

A definition is encoded: a defined-term table or function that returns the term's meaning as the Act states it (the members it names, what it includes or excludes, what it points at), with a test for each entry.
Rules of reading (the singular includes the plural; a reference to an Act includes amendments; and so on) are encoded as functions over a small typed representation of what the rule operates on, as an existing module of this family does, with tests on both sides of each limb.

## Your starting point

`DEPOSIT/encodings/legalese-sonnet-5.5/` already holds a draft encoding of this Act (pass 1): modules, tests, `NOTES.md`, `encoding.json`, `PROGRESS.md`, `check.sh`, `srcrefs.py`, and the pass-1 brief as `BRIEF-pass1.md`.
It is a copy; the repository is not touched. READ IT FIRST: `NOTES.md` (coverage table, fork register, findings), `encoding.json` (its `scope.not_encoded`), then the modules.
Pass 1 worked to a narrower standard of what to skip. Do not trust its dispositions; re-derive them from the text.

Pass 1's 38 `inert` rows are your audit list. `tests-red-control.l4` is meant to fail 8 times (keep that). The deposited text is the enacted text, not a revision; say so in NOTES.md.

## Steps, in order

1. **Baseline.** Run `check.sh` before you change anything and keep the numbers it prints in `PROGRESS.md` under "baseline". At the end every baseline number must still hold, plus your additions, unless you log a defect fix (step 5).
2. **Count and audit, before you encode.** Count the text's units (every section heading, subsection, schedule paragraph, defined-term entry and table row) from the text with a script. Compare with the coverage table's rows. Write a section `## Re-disposition audit` in `NOTES.md` with: the counts; each unit missing from the table; and, for every row that is not `encoded`, a one-line verdict: it keeps its disposition (name which of the three inert reasons) or it moves to `encoded` or `fork`. Write this section before you write any new L4, and keep it current.
3. **Encode what the audit moved.** New layer-1 modules beside the existing ones, named in the folder's own pattern (read `ls` first), following the text's own structure. Every rule has an `@ref`; quote and cite per `encoding-a-subject/references/source-locators.md`. Reuse the existing modules' definitions by IMPORT; never copy a rule.
4. **Tests from the text** for every new rule, as described under Tests below.
5. **Existing files.** You may not edit an existing module or test except to fix a defect you can show against the text (a failing assertion the text supports; a wrong citation). Log every such edit under `## Changes to existing modules` in `NOTES.md`: the file, what changed, why, and the text that licenses it. Never delete a module or a test.
6. **Bookkeeping.** `NOTES.md`: the coverage table complete (one row per unit, dispositions as above), the fork register, numbered findings, the `## Jural relations` section, what `check.sh` prints, and what would need doing before the encoding is worth relying on. `encoding.json`: version `0.2.0`, `scope.encoded` rewritten, `scope.not_encoded` empty or absent, `checks` updated, `l4_bin` with its sha256 and version line, status stays `draft`, `not_reviewed` says no domain expert has read it against the text.

## Rights and duties come in pairs (Hohfeld)

Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability.
In layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In `NOTES.md` keep a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`. In an interpretation Act most provisions create none, so this section is short; it must still cover the whole text.

## The subject and the sources

- **the Interpretation Act 2005 (Ireland)**, No. 23 of 2005.
- Source file(s) in `INPUTS_DIR`: `No.-23-of-2005.txt`.
- `inputs/SOURCES.md` records where each came from, its version, its URL and its hashes. **Read it.**
- Each text is a plain-text rendering made by a converter script; it is not the official text. Say so in `NOTES.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject's licence note. Your `SOURCE-LICENSE.md` points at it and does not repeat it.
- Encode only from these files. Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory.
- Defaults ruled for Commons (Guide section 4): the Act alone, plus instruments that set its numbers or dates if among your inputs, otherwise make the number an input and say so; the actors the text names; a judgment the text hands to someone else becomes a conditional input and is never guessed; the Act's own definitions are worked out from facts, borrowed terms are asked as facts; the Act's own words, each with a plain gloss in a comment.

## Dialect: this folder is written for `unstable`

The existing modules use `REFUSE`, `#ASSERT REFUSED ... BECAUSE`, `YMD` and `@lang`, which the stable binary rejects. The folder's target is `unstable` and your binary is the unstable prerelease. Write every new module in the same dialect so the folder stays one unit that one binary reads. `writing-l4-rules/references/dialects.md` says what `main` would read differently; it does not bind you here, and porting this folder to stable is a separate job that is not yours.
Where the source does not answer, `REFUSE "..."` (as the existing modules do), asserted with `#ASSERT REFUSED`. Do not use a construct your own binary rejects.
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

- **Follow the two skills.** Read before writing any L4: `<the lead's scratchpad>/skills/encoding-a-subject/SKILL.md` (steps 1 to 7 and 9; you do not deposit into a repository) and `<the lead's scratchpad>/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** One source provision, one recognisable place in the L4, with the source's numbering and an `@ref`. Run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>` for each raw text file the folder's `check.sh` or pass-1 `NOTES.md` says to; it must report 0 problems.
- **Where the source does not answer,** return an explicit "not covered" value and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails. Report the numbers `check.sh` prints.
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file except a registered, deliberately failing one.
- **No sleep-polls and no waiting loops**: run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28), sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.
Run the check as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` (the word `unstable` tells the script not to compare with a second binary: this folder is written for unstable).

## Independence

You may read: `INPUTS_DIR`, `DEPOSIT` (including pass 1), the two skills and their references, and the Commons guide copies in `inputs/`.
Do not read any other encoding of any other Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`, no other directory under `<the lead's scratchpad>/runs` than your own `iaw-ie/`, and nothing under `~/.claude/` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message; the report is your final response, not a file)

Return: (1) the list of files you wrote or changed; (2) exactly what `check.sh` printed, and the baseline numbers it replaced; (3) the coverage table summary (counts per disposition) and the audit counts (text units counted, rows in the table before and after); (4) the forks you took, one line each with the reading chosen; (5) every row you moved out of `inert` and every row you left `inert` with its reason number (1, 2 or 3); (6) any failing or refused assertion and what it means; (7) what the text does not answer; (8) `peeked`: nothing, or what you opened by accident.
Subagents cannot write report-named files such as `FINDINGS.md`; `NOTES.md`, `PROGRESS.md` and `.l4` files are fine.
