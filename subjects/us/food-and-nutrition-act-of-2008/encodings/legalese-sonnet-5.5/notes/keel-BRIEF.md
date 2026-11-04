# Keel brief: the Food and Nutrition Act of 2008 (United States, 7 U.S.C. ch. 51, the SNAP statute) -- the shared vocabulary, in L4 (stable)

You are the KEEL agent for the Food and Nutrition Act of 2008 (United States, 7 U.S.C. ch. 51, the SNAP statute) (7 U.S.C. 2011 to 2036d, Public Law 110-246). The text is too long for one agent, so after you finish, 6 part agents will encode it in parallel, each its own line ranges, each with your core module as a read-only file. They cannot talk to you or to each other. What you write is all they share.
This brief is the whole specification. Read it fully before opening any source. You are the only agent running now; no subagents.

## Your job, in order

1. **Read the text through** (`INPUTS_DIR/usc07-ch51.txt`): all the headings first, then the definitions and the provisions every part will need. `inputs/PARTS.md` gives the line ranges, yours and the parts', and how many words each holds. Line numbers are of the file as it is.
2. **Write the core** `snap-core.l4` in `DEPOSIT/encodings/legalese-sonnet-5.5/`: `DECLARE` and shared constants only, importing `prelude` and `daydate` only, at most about 300 lines. Nouns first: the people (the person, the claimant, a couple, a child, an employer, a decision-maker), the things the Act names (the benefits, payments, awards, periods, the kinds of decision), money as `NUMBER`, dates as `Date` (written `Date day month year`), and the enumerations a rule would otherwise invent twice. The test for membership: could a witness of ordinary competence testify to this fact, or does answering it require reading the Act? Only the first kind belongs in the core. Do not write rules in the core.
3. **Encode the Act's own definitions and interpretation provisions that fall in YOUR ranges (see `inputs/PARTS.md`, rows marked `keel`)** in `snap-definitions.l4` (imports the core), as defined-term functions, with `snap-definitions-tests.l4`. If the Act's definitions sit in the parts' ranges, leave them to those parts and say which in PLAN.md.
4. **Write `PLAN.md`** in `DEPOSIT/encodings/legalese-sonnet-5.5/`: for each part agent (named in `inputs/PARTS.md`): its ranges (copied unchanged), the names in the core it should expect to use, and the SEAMS you can already see: a provision in one part whose answer another part's provision needs. A part cannot import another part (they are in separate sandboxes until the merge), so the dependent part takes that answer as an INPUT fact, named for the section it comes from; PLAN.md lists each seam as: the asking section, the answering section, the name and type of the input. Also state the naming rule below.
5. **Check:** `check.sh` over your deposit: your core, definitions and tests compile on the stable binary with no `DiagnosticSeverity_Error` or `_Warning`.
6. **Stop.** Do not encode any other provision.

## Naming rules every part will follow (put them in PLAN.md)

- A name defined in two modules that are imported together cannot be used at all, so no two parts may define the same name. Every top-level name (function, constant, type constructor not in the core) a part defines **begins with the section label it implements, in the form `s 4(2)(a) ...`** (the Act's own numbering: `s 2014(d) a household with an elderly member`, `sch 3 para 2 the amount is reduced`; parentheses inside a backtick name parse fine on the stable binary). Types and constructors shared across parts live only in the core.
- A part may not edit the core and never waits for it. If a part needs a type or constructor the core lacks, it defines it in its own module under its own prefix, records it in `NEEDS-CORE.md` in its sandbox, and the lead hoists it into the core at the merge.
- File names: every module of part `X` begins with `X-` (the part's id), and every module of yours begins with `snap-`.

## What "whole" means (Meng's ruling of 2026-10-22, applied to this Act)

Every provision of YOUR range (and, in the end, of the whole text, by the parts together) has a row in a coverage table, and each row has exactly one disposition:
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

## What FALSE and NOTHING mean in your answers (the rule of 2026-10-29; assumed, not ruled by a lawyer)

This rule is in force for every row the family has filed since 2026-10-29. Follow it exactly, and flag, do not decide, the two readings marked "for a lawyer".
- A decision function answers `JUST FALSE` (a `BOOLEAN` that is `MAYBE`-wrapped), or a constructor whose meaning is "the text says no" (for example `Not entitled`, `Not barred`, `Not obliged`; choose your own descriptive names), **only** where the text itself says no to the case in its own words: a definition that says "means"; a condition the text introduces with "if", "only if", "as long as" or "unless" (and their plain variants: "so long as", "while", "until", "except", "save", "provided that"); a list the text closes with "only" or "nothing but"; a flat negative ("does not", "shall not", "may not", "is not entitled").
- Everywhere else the function answers `NOTHING` (a `MAYBE` result) or a named "... not covered" constructor: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points to a power, regulation, rate or authority outside your sources, or limits a grant or prohibition in its own wording ("without", "against the will of", "when", a stated period, a named complement) and the case falls outside the limit.
- Every branch that answers a "no" carries a comment `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)` where <why> is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- The function's name carries the section it implements, in this form: `s 47(2) the instrument is valid`, `s 4(2)(a) the claimant has reached the qualifying age`, `sch 3 para 2 the amount is reduced` (the Act's own numbering; parentheses inside a backtick name are fine on the stable binary, checked). Not `is the instrument valid`, not `may I ...`: the name must not claim more than the section says. A caller must never turn `NOTHING` into `FALSE`.
- **For a lawyer, not for you to decide:** (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not. Take these readings as the status quo, and list every branch that rests on one under a heading `## Marginal readings for a lawyer` in `NOTES.md`, with the other reading stated.
- Put a short section `### Reading a result: FALSE and NOTHING` in `NOTES.md` saying this in your own subject's terms: what a "no" is in this row, and what "not covered" is.
- `REFUSE` does not exist on the stable binary: "not covered" is `NOTHING` or a constructor, asserted.

## Rights and duties come in pairs (Hohfeld)

Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability.
In layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In `NOTES.md` keep a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`. Most provisions of this text DO create a relation (a person against the authority that pays or decides, an employer against an employee, a claimant against the Crown), so this section is long; it must cover the whole of your range.

## The subject and the sources

- **the Food and Nutrition Act of 2008 (United States, 7 U.S.C. ch. 51, the SNAP statute)**, 7 U.S.C. 2011 to 2036d, Public Law 110-246.
- Source file in `INPUTS_DIR`: `usc07-ch51.txt`; `inputs/SOURCES.md` records where it came from, its hashes, its URL. **Read it.**
- The text is a plain-text rendering made by a converter script; it is not the official text. Say so in your files, and claim nothing is "verified against the official text".
- **A second source.** `fna-snap-cola-fy2027.txt` (about 1,300 words) holds the fiscal-year 2027 cost-of-living adjustments: the dollar figures (maximum allotments, income standards, deduction amounts) that the Act's formulas take as inputs. It is NOT covered by the line ranges in `inputs/PARTS.md`, which refer to `usc07-ch51.txt` only. Treat its figures as INPUT DATA for the sections they feed (section 2014 income standards and deductions, section 2017 allotments): the part that encodes those sections puts them in a table keyed by the year, and says which fiscal year it is. Your core should have room for them (a record of annual figures).
- `inputs/STUB-SOURCE-LICENSE.md` is the subject's licence note.
- Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory. Follow `encoding-a-subject/references/source-locators.md` (`-- src:` lines and `@ref` locators) and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>`; it must report 0 problems.
- Defaults ruled for Commons (Guide section 4): the Act alone; the actors the text names; a judgment the text hands to someone else is a conditional input, never guessed; the Act's own definitions worked out from facts, borrowed terms asked as facts; the Act's own words, each with a plain gloss in a comment.
- The seat the parts will serve (so that your nouns fit): a member of a household that applies for, or receives, benefits under the Supplemental Nutrition Assistance Program, asking on facts they can state whether the household is eligible, how its income and deductions count, what its allotment is, what disqualifies a member, and what follows from a violation.

## Writing L4 that the stable binary accepts (from the Commons guide, section 5, verbatim)

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Dates: write `Date day month year`, and never define a `YMD` of your own.** `Date` (from `IMPORT daydate`) is in every build. Unstable builds have had a year-first `YMD` in daydate since 29 July 2026, and it is proposed for the stable line (legalese/l4-ide#768, not landed); a file that imports daydate and also defines `YMD` then fails with "There are multiple definitions for the identifier YMD", and so does every file that imports it. Earlier encodings followed this guide's old advice to add a `YMD` shim; on 29 October 2026 the shim was renamed `YearMonthDay` in the 50 files that define it and the 809 others that call it, so that the collision no longer stops them (checked on 29 October 2026 over those files and every file that imports them: no file that checked before fails after, on stable 1.6.98, on unstable-20261028-5e95b5a, or with the daydate of #768). Keep `YearMonthDay` where an encoding already uses it, and do not start a new encoding with it. `Date` and the shim roll an impossible date forward (`Date 29 2 2023` is 1 March 2023); daydate's `YMD` refuses it. When a stable `l4` ships `YMD`, the shims are to be deleted and `YearMonthDay` renamed back. **Smaller gaps:** `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.
- **Lists:** write a list of strings as a vertical `LIST` block, one string per line, not with `•` bullets (those are a parse error on the stable binary).

Your binary is the stable build, so anything it rejects is not available to you. Where the skills describe a construct the stable binary rejects, the binary governs; say so in `NOTES.md` under the finding "What the stable binary does not accept".
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

- **Follow the two skills.** Read before writing any L4: `<the lead's scratchpad>/skills/encoding-a-subject/SKILL.md` (steps 1 to 7) and `<the lead's scratchpad>/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails. Report the numbers `check.sh` prints.
- **No sleep-polls and no waiting loops**: run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.
Run the check as `L4=<L4_BIN> L4_MAIN=<the lead's scratchpad>/bin/l4-main-108 ./check.sh` (the default target `main`: it runs every module with a second stable build as well and goes red when the two read it differently).

## Independence

Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`, no directory under `<the lead's scratchpad>/runs` other than your own `iaw-snap-k/`, and nothing under `~/.claude/` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
You may read `INPUTS_DIR`, the two skills and their references, and the Commons guide copies in `inputs/`. Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message; the report is your final response, not a file)

Return: (1) the files you wrote; (2) exactly what `check.sh` printed; (3) the core's contents in one line per type; (4) the seams you listed, one line each; (5) the definitions you encoded and the ones you left to a part; (6) any difficulty the parts will meet; (7) `peeked`: nothing, or what you opened by accident.
Subagents cannot write report-named files such as `FINDINGS.md`; `PLAN.md`, `NOTES.md`, `PROGRESS.md` and `.l4` files are fine.
