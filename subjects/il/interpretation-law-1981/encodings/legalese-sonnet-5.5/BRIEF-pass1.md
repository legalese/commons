# Encoding brief: Israel's rules for counting time, in L4

You are producing an L4 encoding of two Israeli interpretation statutes, from the Hebrew, in English L4.
This brief is the whole specification. Read it fully before opening any source.

You are the ONLY encoder: no ontology agent, no fleet, no integrator, no independent test author.
You do all of it in one context and you check your own work with the diagnostics.

## Why this exists

Other encodings of Israeli legislation need executable answers to questions such as: when does a period of "N days", "N months" or "N years" from or after a day end; do rest days and holidays count; when do regulations come into force; from what moment does a statute bind.
Those answers come from the interpretation statutes, not from the statute being encoded, and today different encodings give different answers.
Your job is to make the interpretation statutes executable and tested, as a module other encodings can reuse.
Decide every answer from the statute text alone; do not look for the answers anywhere else.

## The subject and the sources

- **חוק הפרשנות, התשמ״א–1981** (the Interpretation Law 5741-1981), 33 sections: `inputs/law.wiki`.
- **פקודת הפרשנות [נוסח חדש]** (the Interpretation Ordinance [New Version]): `inputs/ordinance.wiki`.
  The Law of 1981 repealed most of the Ordinance, so most of this file's sections are blank; read the text to see which still carry content.
- `inputs/SOURCES.md` records where each came from. **Read it.**
  Both are unofficial Wikisource consolidations, and the official PDFs could not be fetched.
  Say so in `NOTES.md` and in `SOURCE-LICENSE.md`, and do not claim anything is "verified against the gazette".

All inputs are under `INPUTS_DIR` (given in your task). Read them there and nowhere else.
Quote Hebrew from these files mechanically (copy it, or script it as long as the script reads the file); never reconstruct it from memory.

## Scope, pinned

- **Part A: the Interpretation Law, every section 1 to 33.**
  Sections 27 to 30 look blank in the text; find out why from the text and say so.
- **Part B: the Ordinance, every section the text still carries content for**, which includes at least ss. 16, 17 and 19; every other section of the Ordinance text gets a coverage row saying what the text shows (blank, repealed, or content).
- **Must be encoded as executable functions with tests:**
  s. 10 of the Law in all three subsections; s. 8 ("עד"); the s. 3 definitions of "יום", "שנה" and "חודש"; s. 21 (the moment a statute begins to bind); and the Ordinance's rule on when legislative regulations come into force.
- **Everything else:** encode what is computable; mark the rest `inert` in the coverage table with a reason of real length.
  Interpretive canons (singular includes plural, and so on) need not be forced into code.

## The module other encodings will reuse

Put the time-computation functions in ONE self-contained module that imports only `prelude` and `daydate`, with a descriptive ASCII filename.
It must answer, as named functions with `@ref` citations to the section:

1. the last day of a period of N days or N weeks counted from a day;
2. the last day of a period of N months or N years counted after an event, including a start on the 31st, a start on 29 February, and a month that lacks the start day's number;
3. what happens to a period whose last day or last days are days of rest, recess or holiday under an enactment;
4. whether a given date falls inside a period;
5. the day, and the moment within the day, from which a statute binds;
6. the day regulations come into force.

**Days of rest, recess and holiday are an INPUT, never computed.**
Take them as a function or a list that the caller supplies.
Do not hard-code a holiday calendar and do not compute the Hebrew calendar.
Where the statute asks for a period by the Hebrew calendar, answer with a named `REFUSE` saying what is missing.

## Deliverables, all under your `DEPOSIT` directory (given in your task)

`DEPOSIT` is laid out as a canon subject, so that it can be copied as it stands into `subjects/il/interpretation-law-1981/`:

```
DEPOSIT/
  subject.json              facts about the LAW (id, display_name, citation, extent, source with the provenance above)
  README.md                 the law in a paragraph, for a human, and a table of the rows
  source/                   copies of inputs/ (law.wiki, ordinance.wiki, SOURCES.md, revisions.json)
  encodings/legalese-sonnet-5.5/
    *.l4                    ASCII filenames; every module starts with `@lang en`; nouns module first if you need one
    tests, check.sh, NOTES.md, encoding.json, SOURCE-LICENSE.md
```

`encoding.json` and `SOURCE-LICENSE.md` follow `references/canon-deposit.md` of the `encoding-a-subject` skill (status `draft`; `not_reviewed` saying no domain expert has read it against the statute).
The row name is `legalese-sonnet-5.5`; the method is a single Sonnet 5.5 agent working alone from this brief.
For `SOURCE-LICENSE.md`: there is no copyright in statutes under the Israeli Copyright Act 5768-2007, s. 6; Wikisource's own editorial additions, if any survive, are CC BY-SA 4.0; the official text could not be fetched.

`NOTES.md` carries: what is encoded and what is not; a coverage table with one row per section of Part A and Part B and a disposition for each; a **fork register** (every ambiguity, the readings you saw, the one you took, the text that licenses each); an answer table for the worked cases below; what `check.sh` prints; open questions for a domain expert.

## Forks you must look at (they are the point of the exercise)

- Which of s. 10(a) and s. 10(b) governs a period of years or months that is written "from" a day rather than "after" an event; and does it matter for the answer?
- Whether s. 10(c) applies to periods in months and years or only to periods in days, on the words of the text.
- What s. 10(c) does when several days at the end of a period are rest days in a row.
- Whether "עד" in s. 8 settles a case you would otherwise leave to a convention.
- Anything else the text leaves open. "No ambiguities found" is a claim a reviewer will not believe; say where you looked.

## Tests

Expected values come from the statute text, never from your code.
Decide each expected answer by reading the section, write it down, then run.
A failing assertion is a finding: never edit an expected value to match what the code computed.

Cover at least: every branch of s. 10(a), (b) and (c); month-end and leap-day starts; periods of one day, one week, one month, one year; a last day that is a rest day, and two rest days in a row, using a rest-day input you supply in the test; the boundary dates on each side of every period (the last day inside, the next day outside); s. 8; s. 21.
Also run these worked cases and put each in the answer table with its section citation:

| period | counted from |
| --- | --- |
| three years | the day 2025-07-16 |
| five years | the day 2025-01-15, and the day 2025-09-01 |
| thirty days | the day 2026-01-01 |
| two years | the day 2024-02-28 |
| one year | the day 2024-02-29 |
| one month | the day 2025-01-31 |

If you keep some expectations meant to fail, put them in their own file, count them, and say how many.

## Rules that matter

- **Follow the two skills.** Read before writing any L4:
  `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here, and you do not deposit into a repository) and
  `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md` and all of `references/source-patterns/` (especially 04-dates-and-periods and 11-when-the-encoding-cannot-answer).
  Documentation is under `/Users/mengwong/src/legalese/l4-ide/doc/`.
- **Encode isomorphically.** A reader holding the Hebrew beside your module checks it line by line. Cite the section on every rule with `@ref`.
- **Where the sources do not answer, `REFUSE "…"`.** Never `FALSE`, never `0`, never a plausible default. Do not invent a home-made three-valued type; the language has `MAYBE` and `REFUSE`.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails or refuses; a failure is a `DiagnosticSeverity_Error` line and a refusal is a Warning. Report the numbers `check.sh` prints (start from the skill's `assets/check.sh`).
- **Dates** need `IMPORT daydate`. Arithmetic on dates without it produces an ambiguous-operator error, not a date. Check how `daydate` handles a start on the 31st and on 29 February instead of assuming; if its behaviour differs from the statute, the statute governs and you write the rule.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL`, `#ASSERT` and `#TRACE`.
`l4` has no `--version` flag. Run the binary by its absolute path.

## Independence

Do not read any existing encoding of Israeli legislation under `/Users/mengwong/src/legalese/commons`, `commonswt`, `canon` or `il`, and nothing under `~/.claude/` except the two skills named above (no `memory/`, no `projects/`, no `thermostat-oracle`, no `tmp`).
The answers must come from the statute text alone.
You may read `INPUTS_DIR`, the two skills and their references, and the l4-ide `doc/` tree.
Your context may contain an index of someone's notes that mentions Israeli encodings; do not follow it.
If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) the coverage table summary (counts per disposition); (4) the forks you took, each in a line with the reading chosen; (5) the answer table for the worked cases; (6) any failing or refused assertion and what it means; (7) what the sources do not answer; (8) `peeked`: nothing, or what you opened by accident.
