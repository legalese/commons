# Part brief: wra4 of the Welfare Reform Act 2012 (United Kingdom) -- encoded in parallel with 3 other part agents, in L4 (stable)

You are part agent `wra4` for the Welfare Reform Act 2012 (United Kingdom) (2012 c. 5). A keel agent has already written the shared vocabulary; 3 other part agents are encoding the other line ranges at the same time, each in its own sandbox. You cannot see them and they cannot see you. This brief is the whole specification; `inputs/PLAN.md` is the keel's plan and governs the details of names, labels, seams and the core (where PLAN.md and this brief differ, this brief governs; say so in your NOTES.md).
You are the only agent on your ranges: no subagents. You do all of it in one context and check your own work with the diagnostics.

## Your ranges

| line ranges | words |
| --- | --- |
| 1520-2474 | 17120 |

Line numbers are of `INPUTS_DIR/ukpga-2012-5.txt` (1-based, inclusive). A provision whose heading is in your ranges is yours, whatever it cites. Read the whole text wherever a cross-reference needs it, but encode only your ranges. Every non-blank line of your ranges falls in some row of your coverage table.
Read `inputs/PLAN.md` before anything else, in particular its sections 2 (rules every part follows), 3 (your part), 5 to 8 (reading the raw text, labels, values the regulations supply, the SEAMS), 11 (difficulties) and 12 (shapes). Its seams list says which answers you take as INPUTS because another part computes them.

## What you are building: two layers

**Layer 1: the law, objectively.** The provisions of your ranges, as isomorphic and tested L4 modules that follow the text's own structure. It is written from the text alone and takes nobody's point of view, and every rule carries a source citation. It IMPORTs the keel's modules `wra-core.l4` and `wra-definitions.l4` from your folder; the keel's files are READ-ONLY copies in your sandbox: do not edit them, do not copy their names, and the lead keeps one copy at the merge.

**Layer 2: one thin seat layer over it.** Commons requires every Act to be asked about from the position of the individual to whom the law is applied (the "seat"). Here the seat is: **a person who claims, receives or is moved to Universal Credit, or who claims Personal Independence Payment, or whose benefits are capped, asking on facts they can state whether they are entitled, what conditions they must meet, what happens if they do not, how a decision about them is revised or appealed, and what they can be made to repay.**
Your layer is the two files `wra4-seat.l4` and `wra4-cases-seat.l4`, covering the questions your ranges answer for that person. It IMPORTs your layer-1 modules and calls their rules; it never restates a rule. Each question has `@export` and `@desc`, takes plain inputs (one per fact the person can state, each `@desc` worded as that person would be asked), and the questions are grouped under `§` headings in the text's order.
**Name every seat question so that it begins "Under section N," (or "Under schedule N paragraph M,")**, with the Act's own numbering, so that no two parts' questions can ever share a name and each says the scope its answer claims. Read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md`; `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` shows the shape of a seat layer for a different Act (copy its shape, not its content).
Provisions that address only an official are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person. There is never a seat for an official.

## What "whole" means (Meng's ruling of 2026-10-22, applied to this Act)

Every provision of YOUR ranges, that is every section, subsection, paragraph, schedule, table row and defined term, has a row in your coverage table, and each row has exactly one disposition:
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
- A decision function answers `JUST FALSE` (a `BOOLEAN` that is `MAYBE`-wrapped), or a constructor whose meaning is "the text says no" (for example `s 39 not entitled`, `s 39 not barred`, `s 39 not obliged`: **every constructor and type you declare begins with the section label, like every function**, so that no two parts declare the same name; the merged seat layer imports all the parts at once, and a name defined in two modules cannot be used at all), **only** where the text itself says no to the case in its own words: a definition that says "means"; a condition the text introduces with "if", "only if", "as long as" or "unless" (and their plain variants: "so long as", "while", "until", "except", "save", "provided that"); a list the text closes with "only" or "nothing but"; a flat negative ("does not", "shall not", "may not", "is not entitled").
- Everywhere else the function answers `NOTHING` (a `MAYBE` result) or a named "... not covered" constructor: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points to a power, regulation, rate or authority outside your sources, or limits a grant or prohibition in its own wording ("without", "against the will of", "when", a stated period, a named complement) and the case falls outside the limit.
- Every branch that answers a "no" carries a comment `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)` where <why> is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- The function's name carries the section it implements, in this form: `s 47(2) the instrument is valid`, `s 4(2)(a) the claimant has reached the qualifying age`, `sch 3 para 2 the amount is reduced` (the Act's own numbering; parentheses inside a backtick name are fine on the stable binary, checked). Not `is the instrument valid`, not `may I ...`: the name must not claim more than the section says. A caller must never turn `NOTHING` into `FALSE`.
- **For a lawyer, not for you to decide:** (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not. Take these readings as the status quo, and list every branch that rests on one under a heading `## Marginal readings for a lawyer` in `NOTES.md`, with the other reading stated.
- Put a short section `### Reading a result: FALSE and NOTHING` in `NOTES.md` saying this in your own subject's terms: what a "no" is in this row, and what "not covered" is.
- `REFUSE` does not exist on the stable binary: "not covered" is `NOTHING` or a constructor, asserted.

## Rules, duties and decision functions

The text says who is entitled to what, who must do what by when, and what follows. Encode it the way it reads, provision by provision, choosing the form closest to the words:
- a **decision function** (a typed `DECIDE`) where the provision fixes a sum, a rate, a rank, an entitlement, a condition for a lawful act, a period, or a list of who is covered;
- a **regulative rule** (`PARTY ... MUST / MAY / SHANT ... WITHIN ... HENCE ... LEST ...`, see `writing-l4-rules/references/regulative.md`) where a provision imposes a duty, permission or prohibition on a named party, with its time limit and consequence if the text gives them.
Both are tested. A regulative rule is run (`#TRACE` / `#EVAL`) and you assert what you can assert on the stable binary; if some regulative construct cannot be asserted on it, say so under "What the stable binary does not accept" and also encode the same duty as a decision function over the facts.
Do not invent an actor, a deadline, a remedy or a consequence the text does not state: where it does not say who decides, by when, or what follows, say so in the fork register and return a "not covered" value.
Amounts, rates and thresholds the text leaves to regulations, orders or a Minister are INPUTS (a number the person states), asked with an `@desc`; never a number from memory.
Dates are `Date day month year`; a period measured in days, weeks, months or years is a function with a test on both sides of its end.

## Rights and duties come in pairs (Hohfeld)

Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability.
In layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In `NOTES.md` keep a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`. Most provisions of this text DO create a relation (a person against the authority that pays or decides, an employer against an employee, a claimant against the Crown), so this section is long; it must cover the whole of your range.

## The subject and the sources

- **the Welfare Reform Act 2012 (United Kingdom)**, 2012 c. 5. Source file in `INPUTS_DIR`: `ukpga-2012-5.txt`; `inputs/SOURCES.md` records where it came from, its version and hashes. **Read it.**
- The text is a plain-text rendering made by a converter script; it is not the official text. Say so in NOTES.md, and claim nothing is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject's licence note. You do not write `SOURCE-LICENSE.md`, `encoding.json`, `subject.json` or `README.md`: the lead writes them for the merged folder.
- Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory. Follow `encoding-a-subject/references/source-locators.md` (`-- src:` lines and `@ref` locators) and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>` and with `--strict`; both must report 0 problems for your files.
- Defaults ruled for Commons (Guide section 4): the Act alone, plus instruments that set its numbers or dates if among your inputs, otherwise the number is an input; the actors the text names; a judgment the text hands to someone else becomes a conditional input and is never guessed; the Act's own definitions are worked out from facts, borrowed terms are asked as facts; one case is the text's natural unit; the Act's own words, each with a plain gloss in a comment.
- Build the coverage table from the text itself with a script, one row per section, subsection, paragraph, schedule paragraph, defined term and table row of YOUR ranges, and check that every non-blank line of your ranges falls in some row.

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
## Deliverables, all under your `DEPOSIT` directory (given in your task)

```
DEPOSIT/encodings/legalese-sonnet-5.5/
  wra-core.l4, wra-definitions.l4   the keel's, read-only
  wra4-*.l4                         layer 1: your modules (flat folder: IMPORT finds only modules beside it)
  wra4-tests-*.l4                   tests for them
  wra4-seat.l4, wra4-cases-seat.l4
  NOTES.md, PROGRESS.md                 yours; NEEDS-CORE.md only if you needed a type or constructor the core lacks
  check.sh, srcrefs.py, fetch-main-l4.sh  supplied
```
All `.l4` files have ASCII names beginning `wra4-`, sit directly in that folder, and never define a name that the core defines or that another part could define (every top-level name begins with the label of its provision, in the form `s 4(2)(a) ...`). **That covers every `DECLARE`d type and every constructor, not only functions and constants**, including the constructors that mean "the text says no" or "not covered": write `` DECLARE `s 39 couple status` IS ONE OF `s 39 a couple`, `s 39 not a couple` ``, never a bare `Not entitled`. If a core type lacks a constructor you need, you cannot extend it from another module: declare a small type of your own under your prefix for those cases, use it, and record the constructor you wanted in `NEEDS-CORE.md` for the lead to hoist.
`NOTES.md` carries, for YOUR ranges only: `## Coverage (wra4)` (one row per unit with exactly one disposition and the L4 name), `## Fork register (wra4)` (every ambiguity, the readings you saw, the one you took, the text that licenses each), `## Jural relations (wra4)`, `## Marginal readings for a lawyer (wra4)`, `### Reading a result: FALSE and NOTHING (wra4)`, `## Seams (wra4)` (each seam input you took, as PLAN.md section 8 names it; any seam you found that the plan lacks), numbered findings ("What the text turns out to say"), what the binary does not accept, and what `check.sh` prints.

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

- **Follow the two skills.** Read before writing any L4: `<the lead's scratchpad>/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; you do not deposit into a repository) and `<the lead's scratchpad>/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** Cite the section on every rule with `@ref`.
- **Where the source does not answer,** return an explicit "not covered" value (a constructor or `NOTHING`) and assert it, per the FALSE and NOTHING section above.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails. Report the numbers `check.sh` prints.
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file except a registered, deliberately failing one.
- **No sleep-polls and no waiting loops**: run each command in the foreground, except that you may start a full `check.sh` with `run_in_background` writing to a log if you expect it to pass the ten-minute command limit.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT` (and, if you need scratch space, under `DEPOSIT/../work/`, which is not shipped).

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.
Run the check as `L4=<L4_BIN> L4_MAIN=<the lead's scratchpad>/bin/l4-main-108 ./check.sh` (the default target `main`: it runs every module with a second stable build as well and goes red when the two read it differently).

## Independence

Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`, no directory under `<the lead's scratchpad>/runs` other than your own `iaw-wra4/`, and nothing under `~/.claude/` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
The answers must come from the text alone. You may read `INPUTS_DIR` (including the keel's `PLAN.md` and `KEEL-NOTES.md`), the two skills and their references, and the Commons guide copies in `inputs/`.
Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message; the report is your final response, not a file)

Return: (1) the list of files you wrote or changed; (2) exactly what `check.sh` printed, and the baseline numbers it replaced; (3) the coverage table summary (counts per disposition) and the audit counts (text units counted, rows in the table before and after); (4) the forks you took, one line each with the reading chosen; (5) every row you left `inert`, with its reason number (1, 2 or 3); (6) any failing or refused assertion and what it means; (7) what the text does not answer; (8) `peeked`: nothing, or what you opened by accident.
Subagents cannot write report-named files such as `FINDINGS.md`; `NOTES.md`, `PROGRESS.md` and `.l4` files are fine.
