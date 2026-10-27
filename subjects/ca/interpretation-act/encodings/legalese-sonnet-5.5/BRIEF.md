# Encoding brief: the Interpretation Act (Canada), in L4

You are producing an L4 encoding of the Interpretation Act (Canada) (R.S.C., 1985, c. I-21), from the English version of the Act (the French version is equally authoritative and is not deposited; say so in NOTES.md and treat it as a fork), in English L4.
This brief is the whole specification. Read it fully before opening any source.

You are the ONLY encoder: no ontology agent, no fleet, no integrator, no independent test author, no subagents.
You do all of it in one context and you check your own work with the diagnostics.

## Why this exists

Other encodings of this jurisdiction's legislation need executable answers to questions such as: when does an enactment come into force or begin to bind; when does a period of "N days", "N weeks", "N months" or "N years" from or after a day end; do rest days and holidays count; when is a document treated as served; what a repeal does; what "day", "month" and "year" mean.
Those answers come from the interpretation provisions, not from the statute being encoded, and different encodings of other statutes give different answers when they guess.
Your job is to make the Interpretation Act (Canada) executable and tested, as a module other encodings can reuse.
Decide every answer from the statute text alone; do not look for the answers anywhere else, and do not import an answer from another jurisdiction's law or from your general knowledge of how this one is applied.

## The subject and the sources

- **the Interpretation Act (Canada)**, R.S.C., 1985, c. I-21.
- Source file(s) in `INPUTS_DIR`: `R.S.C.-1985-c.-I-21.txt`.
- `inputs/SOURCES.md` records where each came from, its version or currency date, its URL and its hashes. **Read it.**
- The `.txt` is a plain-text rendering of the official source made by a converter script; it is not the official text and it is not marked up. Say so in `NOTES.md` and in your row's `SOURCE-LICENSE.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited. Your row's `SOURCE-LICENSE.md` points at it and does not repeat it.


All inputs are under `INPUTS_DIR` (given in your task). Read them there and nowhere else.
Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory.

## Scope, pinned

- **Every section, subsection, schedule and table of the text in `INPUTS_DIR`.** Build the coverage table from the text itself, one row per section (and per schedule), with a disposition for each: `encoded`, `inert` (with a reason of real length), `repealed or blank in this text` (say what the text shows), or `not applicable`.
- **Must be encoded as executable functions with tests, wherever the text has the provision.** If the text has no provision on one of these, its coverage row says "the Act is silent on this", and nothing is invented:
  1. when an enactment comes into force or begins to bind, where it does not say so itself (the day, and the moment within the day);
  2. how a period of days, weeks, months or years is counted from or after a day or an event, and which day is its last (including a start on the 31st, a start on 29 February, and a month that lacks the start day's number);
  3. what happens when the last day of a period is a day of rest, a holiday or a day on which an office is closed, as the text defines it;
  4. deemed service or notice, where the text has a rule on it;
  5. what a repeal does: effect on things done under the repealed text, revival, savings, repeal and re-enactment, where the text has a rule on it;
  6. the meanings the text gives to "day", "week", "month", "year" and any other time word.
- **Everything else:** encode what is computable; mark the rest `inert` in the coverage table with a reason of real length.
  Interpretive canons (the singular includes the plural, gender words, and so on) need not be forced into code.

## The module other encodings will reuse

Put the time-computation functions in ONE self-contained module that imports only `prelude` and `daydate`, with the descriptive ASCII filename `ca-interpretation-time.l4`.
It must answer, as named functions with `@ref` citations to the section of the text, each of these that the text governs:

1. the last day of a period of N days or N weeks counted from a day;
2. the last day of a period of N months or N years counted after an event, including a start on the 31st, a start on 29 February, and a month that lacks the start day's number;
3. what happens to a period whose last day or last days are days of rest, recess or holiday under an enactment;
4. whether a given date falls inside a period;
5. the day, and the moment within the day, from which an enactment binds;
6. the day subordinate legislation (regulations, rules, orders) comes into force, where the text says.

**Days of rest, recess and holiday are an INPUT, never computed.**
Take them as a function or a list that the caller supplies.
Do not hard-code a holiday calendar.
Where the text asks for a period by a calendar the encoding does not have, or where the text is silent on an item above, write a named `REFUSE` saying what is missing; never a plausible default.

## Deliverables, all under your `DEPOSIT` directory (given in your task)

`DEPOSIT` holds exactly one directory, laid out so that it can be copied as it stands into `subjects/ca/interpretation-act/`:

```
DEPOSIT/
  encodings/legalese-sonnet-5.5/
    ca-interpretation-time.l4   the reusable time module
    *.l4                                every other module; ASCII filenames; every module starts with `@lang en`; a nouns module first if you need one
    tests, check.sh, NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md (a copy of this brief)
```

You do not write `subject.json`, `README.md` or `source/`: the subject already exists and is not yours to change.
`encoding.json` and `SOURCE-LICENSE.md` follow `references/canon-deposit.md` of the `encoding-a-subject` skill (status `draft`; `not_reviewed` saying no domain expert has read it against the statute).
The row name is `legalese-sonnet-5.5`; the method is a single Sonnet 5.5 agent working alone from this brief.
Record the pinned `L4_BIN` path and its sha256 in `encoding.json`.

`NOTES.md` carries: what is encoded and what is not; a coverage table with one row per section and schedule and a disposition for each; a **fork register** (every ambiguity, the readings you saw, the one you took, the text that licenses each); an answer table for the worked cases below; what `check.sh` prints; open questions for a domain expert.

## Your context will be compacted: make the disk your memory

This run may exceed your context window, and the harness will then compact your context into a summary.
So write as you go, not at the end:

- Keep `NOTES.md`'s coverage table, fork register and answer table on disk, and update them after each section you finish.
- Keep `PROGRESS.md`: sections done, sections in progress, what is next, decisions taken (with the section that licenses each), and a list of the files you have written.
- After any compaction, re-read `PROGRESS.md`, `NOTES.md` and the statute text, not your summary of them.

## Forks you must look at (they are the point of the exercise)

- Whether a period "from" a day counts that day, and whether a period "after" an event does; and whether the last day is inside the period.
- Whether the rule that moves a last day off a rest day or holiday applies to periods in months and years or only to periods in days, on the words of the text; and what it does when several days at the end of a period are rest days in a row.
- What the text means by "month" and "year" (calendar or fixed length) and what follows for a start on the 31st or on 29 February.
- From what moment on its commencement day an enactment binds, and whether the text says so.
- Which language version or versions of the text have authority, if the text says.
- Anything else the text leaves open. "No ambiguities found" is a claim a reviewer will not believe; say where you looked.

## Tests

Expected values come from the statute text, never from your code.
Decide each expected answer by reading the section, write it down, then run.
A failing assertion is a finding: never edit an expected value to match what the code computed.

Cover at least: every branch of each time rule you encode; month-end and leap-day starts; periods of one day, one week, one month, one year; a last day that is a rest day or holiday, and two in a row, using a rest-day input you supply in the test; the boundary dates on each side of every period (the last day inside, the next day outside); commencement; and every other rule you encode.
Also run these worked cases and put each in the answer table with its section citation, or say that the text is silent on the question:

| period | counted from |
| --- | --- |
| three years | the day 2025-07-16 |
| five years | the day 2025-01-15, and the day 2025-09-01 |
| thirty days | the day 2026-01-01 |
| two years | the day 2024-02-28 |
| one year | the day 2024-02-29 |
| one month | the day 2025-01-31 |

And these commencement cases:

| case | question |
| --- | --- |
| an Act is passed or published on 2026-03-10 and says nothing about when it comes into force | from what day, and what moment of that day, does it bind, on the text? |
| an Act says it comes into force on a day to be fixed later; the day is fixed as 2026-06-01 | from what day and moment does it bind? |
| subordinate legislation is made on 2026-03-10 and says nothing about when it comes into force | from what day does it bind, on the text? |

If you keep some expectations meant to fail, put them in their own file, count them, and say how many.

## Rules that matter

- **Follow the two skills.** Read before writing any L4:
  `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here, and you do not deposit into a repository) and
  `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md` and all of `references/source-patterns/` (especially 04-dates-and-periods and 11-when-the-encoding-cannot-answer).
  Documentation is under `/Users/mengwong/src/legalese/l4-ide/doc/`.
- **Encode isomorphically.** A reader holding the statute beside your module checks it line by line. Cite the section on every rule with `@ref`.
- **Where the source does not answer, `REFUSE "…"`.** Never `FALSE`, never `0`, never a plausible default. Do not invent a home-made three-valued type; the language has `MAYBE` and `REFUSE`.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails or refuses; a failure is a `DiagnosticSeverity_Error` line and a refusal is a Warning. Report the numbers `check.sh` prints (start from the skill's `assets/check.sh`).
- **Dates** need `IMPORT daydate`. Arithmetic on dates without it produces an ambiguous-operator error, not a date. Check how `daydate` handles a start on the 31st and on 29 February instead of assuming; if its behaviour differs from the statute, the statute governs and you write the rule.
- **No sleep-polls and no waiting loops**: there is nothing to wait on. Run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL`, `#ASSERT` and `#TRACE`.
`l4` has no `--version` flag. Run the binary by its absolute path.

## Independence

Do not read any existing encoding of any interpretation law: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon` (the subjects `il/interpretation-law-1981`, `sg/interpretation-act` and `au/acts-interpretation-act-1901` in particular), no directory under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/interp-wave` other than your own `ca-fed/`, and nothing under `~/.claude/` except the two skills named above (no `memory/`, no `projects/`, no `state/`, no `tmp`).
The answers must come from the statute text alone.
You may read `INPUTS_DIR`, the two skills and their references, and the l4-ide `doc/` tree.
Your context may contain an index of someone's notes that mentions other encodings; do not follow it.
If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) the coverage table summary (counts per disposition); (4) the forks you took, each in a line with the reading chosen; (5) the answer table for the worked cases; (6) any failing or refused assertion and what it means; (7) what the source does not answer; (8) `peeked`: nothing, or what you opened by accident.
