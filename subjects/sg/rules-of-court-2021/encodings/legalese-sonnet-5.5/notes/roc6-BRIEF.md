# Part brief: roc6 of the Rules of Court 2021 (Singapore) -- encoded in parallel with 11 other part agents, in L4 (main)

You are part agent `roc6` for the Rules of Court 2021 (Singapore) (G.N. No. S 914/2021, current version as at 5 November 2026). A keel agent has already written the shared vocabulary; 11 other part agents are encoding the other line ranges at the same time, each in its own sandbox. You cannot see them and they cannot see you. This brief is the whole specification; `inputs/PLAN.md` is the keel's plan and governs the details of names, labels, seams and the core (where PLAN.md and this brief differ, this brief governs; say so in your NOTES.md).
You are the only agent on your ranges: no subagents. You do all of it in one context and check your own work with the diagnostics.

## Your ranges

| line ranges | words |
| --- | --- |
| 3556-4193 | 12531 |

Line numbers are of `INPUTS_DIR/SCJA1969-S914-2021.txt` (1-based, inclusive). A provision whose heading is in your ranges is yours, whatever it cites. Read the whole text wherever a cross-reference needs it, but encode only your ranges. Every non-blank line of your ranges falls in some row of your coverage table.
Read `inputs/PLAN.md` before anything else, in particular its sections 2 (rules every part follows), 3 (your part), 5 to 8 (reading the raw text, labels, values the regulations supply, the SEAMS), 11 (difficulties) and 12 (shapes). Its seams list says which answers you take as INPUTS because another part computes them.

## What you are building: two layers

**Layer 1: the law, objectively.** The provisions of your ranges, as isomorphic and tested L4 modules that follow the text's own structure. It is written from the text alone and takes nobody's point of view, and every rule carries a source citation. It IMPORTs the keel's modules `roc-core.l4` and `roc-definitions.l4`, which sit in your folder. The keel's files are READ-ONLY copies in your sandbox: do not edit them, do not copy their names, and the lead keeps one copy at the merge.

**Layer 2: one thin seat layer over it.** Commons requires every Act to be asked about from the position of the individual to whom the law is applied (the "seat"). Here the seat is: **a party to a civil action in the Singapore courts (a claimant, a defendant, a third party or an appellant), asking on facts they can state what they must file or serve, by when, how, at what cost, what the court may order, and what follows if they do not**
Your layer is the two files `roc6-seat.l4` and `roc6-cases-seat.l4`, covering the questions your ranges answer for that person. It IMPORTs your layer-1 modules and calls their rules; it never restates a rule. Each question has `@export` and `@desc`, takes plain inputs (one per fact the person can state, each `@desc` worded as that person would be asked), and the questions are grouped under `§` headings in the text's order.
**Name every seat question so that it begins "Under section N," (or "Under schedule N paragraph M,")**, with the Act's own numbering, so that no two parts' questions can ever share a name and each says the scope its answer claims. Read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md`; `inputs/EXAMPLE-sg-silver-support-seat/sssa-seat.l4` shows the shape of a seat layer for a different Act (copy its shape, not its content).
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

- **Label form.** The Rules cite as `O 6 r 7(1)`: function names begin with that label (`o 6 r 7(1) the defence is served in time`; ASCII, lower-case `o` and `r`); a schedule item is `sch 4 part 2 item 5`.
- **Structure.** 70 Orders in two Parts (Orders 1 to 32 general, 33 to 70 specific procedures), four Schedules (the Fourth is the court fees: tables of fees to encode as data) and a final Table of Derivations (lines shown in `inputs/PARTS.md`; one `inert` coverage row for the whole table, reason 1, not operative). A form that is only a form is `inert` (reason 1); content requirements it carries are encoded.
- **Seat questions** begin "Under Order 6, rule 7," (the Rules' own numbering) where the part brief says "Under section N,".
- **Time.** Many Orders count periods in days (service, filing, appeal). Decide each from the Rules' own provision on computing time (find it); `daydate` has the date arithmetic.

## What FALSE and NOTHING mean in your answers (the rule of 2026-10-29; assumed, not ruled by a lawyer)

This rule is in force for every row the family has filed since 2026-10-29. Follow it exactly, and flag, do not decide, the two readings marked "for a lawyer".
- A decision function answers `JUST FALSE` (a `BOOLEAN` that is `MAYBE`-wrapped), or a constructor whose meaning is "the text says no" (for example `s 39 not entitled`, `s 39 not barred`, `s 39 not obliged`: **every constructor and type you declare begins with the section label, like every function**, so that no two parts declare the same name; the merged seat layer imports all the parts at once, and a name defined in two modules cannot be used at all), **only** where the text itself says no to the case in its own words: a definition that says "means"; a condition the text introduces with "if", "only if", "as long as" or "unless" (and their plain variants: "so long as", "while", "until", "except", "save", "provided that"); a list the text closes with "only" or "nothing but"; a flat negative ("does not", "shall not", "may not", "is not entitled").
- Everywhere else the function answers `NOTHING` (a `MAYBE` result) or a named "... not covered" constructor: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points to a power, regulation, rate or authority outside your sources, or limits a grant or prohibition in its own wording ("without", "against the will of", "when", a stated period, a named complement) and the case falls outside the limit.
- Every branch that answers a "no" carries a comment `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)` where <why> is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- The function's name carries the section it implements, in this form: `s 47(2) the instrument is valid`, `s 4(2)(a) the claimant has reached the qualifying age`, `sch 3 para 2 the amount is reduced` (the Act's own numbering; parentheses inside a backtick name are fine on your main binary, checked). Not `is the instrument valid`, not `may I ...`: the name must not claim more than the section says. A caller must never turn `NOTHING` into `FALSE`.
- **For a lawyer, not for you to decide:** (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not. Take these readings as the status quo, and list every branch that rests on one under a heading `## Marginal readings for a lawyer` in `NOTES.md`, with the other reading stated.
- Put a short section `### Reading a result: FALSE and NOTHING` in `NOTES.md` saying this in your own subject's terms: what a "no" is in this row, and what "not covered" is.
- `REFUSE` does not exist on your main binary: "not covered" is `NOTHING` or a constructor, asserted.

## The rulings of 2026-11-04 and 2026-11-05 on negatives, legal effects, periods, "where" conditions and scope limits (recorded in the Commons guide, section 5)

These rulings are Meng's. They bind this row. L4 itself takes no position on them; they are this corpus's drafting conventions, which each row follows and flags.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

What they mean for your work:
- **E1.** Do not look for, or propose, a language construct that gathers a legal effect "by name" from every section that gives it. Where several sections give the same legal effect, encode each section's answer on its own (option C). You may, by hand and in plain L4, write one function that gathers the routes to a legal effect where that helps a reader (option B as guidance for hand-gathering only); say in the fork register where you did. The Magna Carta pilot is not to be run.
- **N2.** A flat negative in the text ("shall not", "is not", "no person") counts as the text's no, so the answer is `JUST FALSE`, and where the text names who bears a prohibition, the prohibition (`SHANT`) is derived from that answer. Do not type the Hohfeld kind into the person-facing answer. Record the kinds in `NOTES.md` under `## Jural relations`.
- **Periods, "where" and scope limits (ruled 2026-11-05; this refines the rule of 2026-10-29).** (a) Where the text fixes a period in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment", "not later than"), outside the period the answer is `JUST FALSE`. (b) A "where ..." condition that is not met answers `JUST FALSE`, like "if". (c) A scope limit with no "only" (the rule reaches "terms below" a minimum age, "an employee of" an employer) answers `NOTHING` outside the scope. Apply all three everywhere in your range, not only at the example sites; where you cannot tell which of (a), (b) and (c) a clause is, record it as a fork and say which you took.
- Put the three bullets above (E1, N2 and the periods line), word for word as printed above, in the fork register of `NOTES.md` (solo rows and keels; for a part agent the lead copies them into the merged `NOTES.md`).

## Main first; a second encoding on unstable only if the text earns it (Meng, 2026-11-05)

This row goes into the public Commons repository and is encoded against a `main` build: your binary is the main build named under Toolchain. The main row is the primary encoding, and it is complete without anything else.
If while encoding you find a shape in the source text that the unstable dialect would express better than a workaround on main, you may ALSO write a second encoding of the affected provisions in the unstable dialect. Examples: rules that depend on time (a rule in force on different dates, amendments in force from different days, deadlines counted from events), rule versions, and anything the main dialect forces you into a workaround for (say what the workaround is).
Do it only after the primary encoding is complete and checked, never instead of it.
Put it in `DEPOSIT/../unstable/encodings/legalese-sonnet-5.5-unstable/` (beside, not inside, the main row), use the unstable binary given under Toolchain, run `L4_TARGET=unstable ./check.sh` there, and write its own `NOTES.md` that names the main row it pairs with, says which provisions and which shape made unstable worth it, and says what each construct buys.
The second encoding goes into a private repository, not Commons: so nothing in the main row may mention its path; the main row's `NOTES.md` says only that a second, unstable encoding of these provisions exists (no path), under `## Unstable dialect`.
If you find no such shape, write one line under `## Unstable dialect` in `NOTES.md` saying you looked at time, versions and workarounds and found none, and where you looked.
The second encoding is optional and yours to judge. Do not invent a shape to justify one.

## Reuse what Commons already encodes (assumed, not ruled; Meng asked whether encoders reuse foundational Acts without being reminded)

- When a provision of your text depends on the Interpretation Act (counting a period, the day a law takes effect, what "month" means, deemed service) or on another Act that Commons already encodes, REUSE that encoding's module. Do not re-encode its provisions inside this row.
- On main there is no import across subject folders: an `IMPORT` finds a module by name only, in the importing file's own folder or the libraries. So copy the staged module UNCHANGED from `inputs/DEPENDENCIES/` into your encoding folder (the staged copy carries a header naming its Commons path and blob; keep it) and `IMPORT` it by name. Do not use `JL4_LIBRARY_PATH`. A copied module keeps its own file name (it does not take your row's prefix), and `srcrefs.py` is run on your own files only.
- `inputs/DEPENDENCIES.md` says which modules are staged for your text and what each covers. If no staged module covers the provision, take its effect as a named input citing the section, and record it under `## Dependencies` in `NOTES.md` as one to fill later.
- Never edit a copied module. If it seems wrong, record a finding against it in `NOTES.md`. Refreshing a copy later is a deliberate re-copy, recorded in `NOTES.md` with the date and the new blob. (Meng, relaying the Commons reviewer's advice, 2026-11-05: copy dependencies, do not live-reference them.)
- List each dependency (module, Commons path, blob, the sections you used, or the section you took as an input) in `NOTES.md` under `## Dependencies` and in `encoding.json` under the key `"dependencies"`. If you copied nothing and needed nothing, say so in one line.
- Where your own text has a rule that overrides the Interpretation Act for its own purposes (the Rules of Court count their own periods), your text governs for those; use the Interpretation Act module for periods and dates that an Act sets.

## Rules, duties and decision functions

The text says who is entitled to what, who must do what by when, and what follows. Encode it the way it reads, provision by provision, choosing the form closest to the words:
- a **decision function** (a typed `DECIDE`) where the provision fixes a sum, a rate, a rank, an entitlement, a condition for a lawful act, a period, or a list of who is covered;
- a **regulative rule** (`PARTY ... MUST / MAY / SHANT ... WITHIN ... HENCE ... LEST ...`, see `writing-l4-rules/references/regulative.md`) where a provision imposes a duty, permission or prohibition on a named party, with its time limit and consequence if the text gives them.
Both are tested. A regulative rule is run (`#TRACE` / `#EVAL`) and you assert what you can assert on your main binary; if some regulative construct cannot be asserted on it, say so under "What your main binary does not accept" and also encode the same duty as a decision function over the facts.
Do not invent an actor, a deadline, a remedy or a consequence the text does not state: where it does not say who decides, by when, or what follows, say so in the fork register and return a "not covered" value.
Amounts, rates and thresholds the text leaves to regulations, orders or a Minister are INPUTS (a number the person states), asked with an `@desc`; never a number from memory.
Dates are `Date day month year`; a period measured in days, weeks, months or years is a function with a test on both sides of its end.

## Rights and duties come in pairs (Hohfeld)

Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability.
In layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In `NOTES.md` keep a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`. Most provisions of this text DO create a relation (a party against another party, against a court, or against a regulator), so this section is long; it must cover the whole of your range.

## The subject and the sources

- **the Rules of Court 2021 (Singapore)**, G.N. No. S 914/2021, current version as at 5 November 2026. Source file in `INPUTS_DIR`: `SCJA1969-S914-2021.txt`; `inputs/SOURCES.md` records where it came from, its version and hashes. **Read it.**
- The text is a plain-text rendering made by a converter script; it is not the official text. Say so in NOTES.md, and claim nothing is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject's licence note. You do not write `SOURCE-LICENSE.md`, `encoding.json`, `subject.json` or `README.md`: the lead writes them for the merged folder.
- Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory. Follow `encoding-a-subject/references/source-locators.md` (`-- src:` lines and `@ref` locators) and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>` and with `--strict`; both must report 0 problems for your files.
- Defaults ruled for Commons (Guide section 4): the Act alone, plus instruments that set its numbers or dates if among your inputs, otherwise the number is an input; the actors the text names; a judgment the text hands to someone else becomes a conditional input and is never guessed; the Act's own definitions are worked out from facts, borrowed terms are asked as facts; one case is the text's natural unit; the Act's own words, each with a plain gloss in a comment.
- Build the coverage table from the text itself with a script, one row per section, subsection, paragraph, schedule paragraph, defined term and table row of YOUR ranges, and check that every non-blank line of your ranges falls in some row.

## Writing L4 that your main binary accepts (from the Commons guide, section 5, verbatim; the guide says "stable binary"; your build is a main build)

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Dates: write `Date day month year`, and never define a `YMD` of your own.** `Date` (from `IMPORT daydate`) is in every build. Unstable builds have had a year-first `YMD` in daydate since 29 July 2026, and it is proposed for the stable line (legalese/l4-ide#768, not landed); a file that imports daydate and also defines `YMD` then fails with "There are multiple definitions for the identifier YMD", and so does every file that imports it. Earlier encodings followed this guide's old advice to add a `YMD` shim; on 29 October 2026 the shim was renamed `YearMonthDay` in the 50 files that define it and the 809 others that call it, so that the collision no longer stops them (checked on 29 October 2026 over those files and every file that imports them: no file that checked before fails after, on stable 1.6.98, on unstable-20261028-5e95b5a, or with the daydate of #768). Keep `YearMonthDay` where an encoding already uses it, and do not start a new encoding with it. `Date` and the shim roll an impossible date forward (`Date 29 2 2023` is 1 March 2023); daydate's `YMD` refuses it. When a stable `l4` ships `YMD`, the shims are to be deleted and `YearMonthDay` renamed back. **Smaller gaps:** `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.
- **Lists:** write a list of strings as a vertical `LIST` block, one string per line, not with `•` bullets (those are a parse error on main).

Those rules were measured on build 98; your build is newer. If your binary accepts something a rule forbids, use it only if the main column of `check.sh` (build 108) reads it the same way. Anything your binary rejects is not available to you. Where the skills describe a construct that main rejects, the binary governs; say so in `NOTES.md` under the finding "What the main binary does not accept".
## Deliverables, all under your `DEPOSIT` directory (given in your task)

```
DEPOSIT/encodings/legalese-sonnet-5.5/
  roc-core.l4, roc-definitions.l4   the keel's, read-only
  roc6-*.l4                         layer 1: your modules (flat folder: IMPORT finds only modules beside it)
  roc6-tests-*.l4                   tests for them
  roc6-seat.l4, roc6-cases-seat.l4
  NOTES.md, PROGRESS.md                 yours; NEEDS-CORE.md only if you needed a type or constructor the core lacks
  check.sh, srcrefs.py, fetch-main-l4.sh  supplied
```
All `.l4` files have ASCII names beginning `roc6-`, sit directly in that folder, and never define a name that the core defines or that another part could define (every top-level name begins with the label of its provision, in the form `s 4(2)(a) ...`). **That covers every `DECLARE`d type and every constructor, not only functions and constants**, including the constructors that mean "the text says no" or "not covered": write `` DECLARE `s 39 couple status` IS ONE OF `s 39 a couple`, `s 39 not a couple` ``, never a bare `Not entitled`. If a core type lacks a constructor you need, you cannot extend it from another module: declare a small type of your own under your prefix for those cases, use it, and record the constructor you wanted in `NEEDS-CORE.md` for the lead to hoist.
`NOTES.md` carries, for YOUR ranges only: `## Coverage (roc6)` (one row per unit with exactly one disposition and the L4 name), `## Fork register (roc6)` (every ambiguity, the readings you saw, the one you took, the text that licenses each), `## Jural relations (roc6)`, `## Marginal readings for a lawyer (roc6)`, `### Reading a result: FALSE and NOTHING (roc6)`, `## Seams (roc6)` (each seam input you took, as PLAN.md section 8 names it; any seam you found that the plan lacks), numbered findings ("What the text turns out to say"), what the binary does not accept, and what `check.sh` prints.

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

- **Follow the two skills.** Read before writing any L4: `<scratch>` (steps 1 to 7, 9 and 11; you do not deposit into a repository) and `<scratch>`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** Cite the section on every rule with `@ref`.
- **Where the source does not answer,** return an explicit "not covered" value (a constructor or `NOTHING`) and assert it, per the FALSE and NOTHING section above.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails. Report the numbers `check.sh` prints.
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file except a registered, deliberately failing one.
- **No sleep-polls and no waiting loops**: run each command in the foreground, except that you may start a full `check.sh` with `run_in_background` writing to a log if you expect it to pass the ten-minute command limit.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT` (and, if you need scratch space, under `DEPOSIT/../work/`, which is not shipped).

## Toolchain

The binary is `L4_BIN` (given in your task): a MAIN build, version 1.6.109 (main, 4c887e0, 2026-11-04), sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`. Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.
Run the check as `L4=<L4_BIN> L4_MAIN=l4 (main 1.6.108) ./check.sh` (target `main`, the default): it runs every module with a second main build, 1.6.108 (main, 2ae7c9b, 2026-11-02), as well, and goes red when the two read a module differently. Report the numbers it prints.
An UNSTABLE build is also supplied, for the optional second encoding only (see the section 'Main first'): l4 (unstable-20261104-68498bc), version unstable-20261104-68498bc (unstable, 68498bc, 2026-11-04), sha256 `7b64926ba7eb92a62a55ba402343bd777c19d4cdb59f26e0cd027cc2f71a8bc1`. Never use it for the main row.

## Independence

Do not read any existing encoding of any Act: nothing under `<home>`, `commonswt` or `canon`, no directory under `<scratch>` other than your own `iaw-roc6/`, and nothing under `~/.claude/` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
The answers must come from the text alone. You may read `INPUTS_DIR` (including the keel's `PLAN.md` and `KEEL-NOTES.md`), the two skills and their references, and the Commons guide copies in `inputs/`.
Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message; the report is your final response, not a file)

Return: (1) the list of files you wrote or changed; (2) exactly what `check.sh` printed, and the baseline numbers it replaced; (3) the coverage table summary (counts per disposition) and the audit counts (text units counted, rows in the table before and after); (4) the forks you took, one line each with the reading chosen; (5) every row you left `inert`, with its reason number (1, 2 or 3); (6) any failing or refused assertion and what it means; (7) what the text does not answer; (8) `peeked`: nothing, or what you opened by accident.
Subagents cannot write report-named files such as `FINDINGS.md`; `NOTES.md`, `PROGRESS.md` and `.l4` files are fine.
