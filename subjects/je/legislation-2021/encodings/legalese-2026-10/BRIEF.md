# Encoding brief: the Legislation (Jersey) Law 2021, in full, in L4

You are producing an L4 encoding of the Legislation (Jersey) Law 2021 from its sources.
This brief is the whole specification.
Read it fully before opening any source, then read the two skills it names.

## The subject

**Legislation (Jersey) Law 2021** (L.8/2021), "A LAW to consolidate and supplement provisions about the making, commencement and repeal of legislation; to provide for the consolidation, revision and publication of legislation; to make provision about the Legislative Drafting Office; to amend and repeal certain other legislation; and for connected purposes".
Part 1 defines terms; Part 2 says when Jersey legislation is made, when it comes into force (Article 3), what a repeal does, and what powers to make subordinate legislation carry (Article 9); Part 3 says how legislation is consolidated, revised, published and which versions are official; Part 4 is the Legislative Drafting Office; Part 5 closes (Articles 24 and 25 are spent and omitted; Article 26 is citation and commencement).
It came into force on 28 September 2021 (the endnotes' Table of Legislation History: R&O.112/2021; Article 26: "comes into force on a day to be specified by the States by Act").
On that day it deleted several provisions of the Interpretation (Jersey) Law 1954, which is encoded separately, by someone else, as its own commons subject; you do not encode the 1954 Law, and you must not copy it.
Where this Law uses a word the 1954 Law defines (for example "month" in Article 15(9)) say so in a comment and take what you need as an input.

## Vintages: two deposited versions

All under `SOURCES` = `subjects/je/legislation-2021/source/`, one `.txt` per version (one paragraph per line, indented by level; `src:N` is line N) and the `.html` it came from.
`RAW` for your quotations is the current text, `l_8_2021.current.txt`; quote the other version as `src:l_8_2021_20240110:N`.

| version | stem | the text shown | difference |
| --- | --- | --- | --- |
| A | `l_8_2021_20240110` | 28 Sep 2021 to 10 Jan 2024 | Article 2(1)(b) reads "by being sanctioned by order of Her Majesty in Council"; the Schedule headings are in capitals |
| B | `l_8_2021.current` | 11 Jan 2024 to current | Article 2(1) "revised on 11 January 2024 by Law Revision Board item 2023/1" (endnote [2]): (b) reads "by being sanctioned by Order in Council"; the Schedule headings are "Schedule 1" and so on |

Verified by comparing the two texts paragraph by paragraph on 2026-10-28: those are the only differences.
So they are editorial and nothing in the Law's operation depends on the version; encode version B, give the 2(1)(b) row both quotations in the coverage table, and say in `NOTES.md` that the change is editorial (Article 15(8) of the Law itself says a revision's changes "have effect as if they were effected by an amendment made by other legislation"; do not claim more than the text says).
Before 28 September 2021 the Law was not in force: a question dated earlier answers "the Law was not in force on that date" (a value, not a refusal), with the commencement cited.

## Scope — the whole Law, pinned

Every paragraph of Articles 1 to 26, Schedule 1, and the placeholders of Articles 24, 25 and Schedules 2, 3 (spent and omitted: `inert`).
The endnotes are evidence, not provisions.
"In full" means every paragraph gets a row and a reason; it does not mean every paragraph is a rule a reader can run:
- a paragraph that only describes an office, a body or an administrative duty with nothing the reader of an enactment could ask about is `inert` or `out-of-scope` with a reason of real length (for example Article 19(2) states an objective; Article 21 is the Principal Legislative Drafter's delegation).
- but a duty on an official is still encoded where it means something to the reader: Article 13(2) (a consolidated version must say it is consolidated legislation compiled under the authority of this Law), Article 14(2) (editorial changes cannot change a provision's meaning), Article 16 (publication), Article 17 (official versions, admissibility, judicial notice), Article 22 (privilege of communications with the Legislative Drafting Office), Article 11 (a subordinate instrument not made by the States ceases to have effect if the States resolve to annul it within 3 sittings), Article 15(9).
Officials get no seat: you encode what each provision means for the person who reads or relies on legislation, or who gives instructions to the Office.

## Claims to verify against the text (they come from a first reading; check each, correct the brief if wrong)

1. **Article 3 (commencement).** (1) Jersey legislation silent as to the commencement of a provision: (a) legislation having effect only to commence other legislation, or an Act of the States referred to in Article 2(2): in force when it is made; (b) any other: on the day after it is made. (2) Legislation expressed to come into force on a particular day: treated as in force at the beginning of that day, unless provision is made to the contrary (a stated time of day is such a provision: the Law does not say so; register how you read it). (4) Where a power to commence is by Act of the States or Order of a Minister on a day specified, different days, times or events may be specified for different provisions. (5) Amendment of uncommenced legislation. (6) **"Nothing in this Article affects the commencement of any Jersey legislation that had commenced before the commencement of this Part."** "This Part" is Part 2, which came into force on 28 September 2021. So Article 3 governs legislation that had not commenced by then; encode `Article 3 governs the commencement of legislation` with an input saying whether the legislation had commenced before 28 September 2021 (the reader derives that from the rule that applied before; the 1954 subject has it), and test the edge days 27 September 2021 and 28 September 2021. (3) is about Regulations being commenced by Ministerial Order. Article 3(2) says nothing about *which instant* of the day a *silent* provision commences on under (1)(b): register it as a fork (I-series is the 1954 row's; use `L1`, `L2`, …), default "the Law does not say: a question about an instant of that day refuses", with the beginning-of-day reading callable.
2. **Article 2 (making).** A Law is made by being (a) adopted by the States Assembly, (b) sanctioned by Order in Council, and (c) registered in the Royal Court; (2) a taxation draft declared by Act of the States to have effect under Article 12(1) of the Public Finances (Jersey) Law 2019 is treated as made though (b) and (c) are not done; (3) Jersey subordinate legislation is made, for Regulations (including Triennial Regulations) or an Act that is Jersey legislation, by the proposition containing them being adopted by the States Assembly, and for any other, by being signed by the person responsible, or if made by a body, by a person acting in accordance with its procedure; (4) "Subject to paragraph (2), Jersey legislation has been made once it has been registered, adopted or signed as the case may be" (for a Law this names registration; (1) requires all three steps: register as a fork what day a Law was made when the three steps have different dates, default the date of registration if all three steps are done, and test a Law with a step missing).
3. **Article 9 (powers to make subordinate legislation)**: (1) a power may be exercised from time to time and includes the power to repeal, amend or replace what was made; (2) made after 28 March 2003: generally or limited, different provision for different cases; (3) "class" includes a single case; (4) a repeal may be brought into force in part; (5) "Unless provision is made to the contrary, a power to make Jersey subordinate legislation also authorises the making of provision incidental to, supplemental to, or consequential upon that legislation"; (6) "However, the power in paragraph (5) is limited — (a) in the case of Regulations, to amending any legislation other than the Human Rights (Jersey) Law 2000 or the legislation giving the power to make the Regulations; and (b) in the case of any legislation not made by the States, to amending any other legislation not made by the States"; (7) legislation stated to be made under a power is treated as made under all the powers under which it may be made. **Question to answer exactly**: can an Order of a Minister (not made by the States, Article 2(3)(b)) use the incidental power of (5) to amend a Law (made by the States)? Encode the question with its inputs (who made the instrument; what is amended; whether provision is made to the contrary) and test both answers.
4. **Article 5 (repeal and expiry)** (1) to (5), **Article 6** (repeal and re-enactment: references to the repealed provisions are construed as references to the re-enacted ones unless provision is made to the contrary), **Article 7**, **Article 8** (the "relevant period" is the period beginning on the day a Law was lodged and ending on the day it was made, and two Laws' relevant periods "overlap to any extent": encode the overlap test from the two periods, with both end days inside the periods because the definition says "beginning on the day" and "ending on the day"), **Article 4** (a power conferred may be exercised after the making of the legislation, whether or not in force; but subordinate legislation made under it may not be brought into force before the provision conferring the power).
5. **Article 11** is about "no later than 3 sittings after the date on which it is laid": sittings are a count, an input; the date of laying and the number of sittings that have passed are inputs. Paragraph (4): for subordinate legislation made before 28 September 2021 the 3 sittings run from that day's commencement of Part 2.
6. **Part 3**: "official version" (Article 17): all as-enacted legislation is an official version; consolidated legislation that is Jersey legislation is an official version if it contains the statement that it is an official version issued under the authority of this Law and either (a) an electronic version displayed on a website under the authority of the Principal Legislative Drafter (or a printed or downloaded copy without alteration) or (b) a printed version issued by or for the Principal Legislative Drafter. (3) an official version of as-enacted legislation is taken to set out correctly its text; (4) an official version of consolidated legislation is, unless the contrary is shown, taken to set out correctly the legislation as at the date it is stated to be consolidated; (5) admissible in evidence, judicial notice. Encode `is this text an official version` and `must the court take notice` from facts the reader can state. The page banner of the deposited source says it is an official version; do not rely on that, state the facts as inputs.
7. **Article 15(9)** says the Law Revision Board's minutes must be laid before the States "within 2 months of the business being transacted": a duty on an official with a period in calendar months (the 1954 Law's definition of "month", which you may not use to add months to a date); encode as an input-driven check (the date laid and the last permitted day as inputs) or `inert` with a reason; do not add months yourself.
8. **Article 22**: confidential communications between a provider of instructions to the Legislative Drafting Office and a Legislative Drafter are subject to legal professional privilege; "confidential communications" includes instructions and related communications and unpublished drafts; "provider of instructions" includes a Member of the States and any officer working in a department, body, office or unit of administration established by or on behalf of the States. A seat question: "Are my communications with the Legislative Drafting Office privileged?"
9. **Schedule 1** lists the powers of the Law Revision Board in preparing a revision (paragraphs (a) to (q)); Article 15(7): the Board may certify a draft revision only if satisfied that the changes are within Article 14 or Schedule 1. Encode as: given the list of changes made, `all within the powers` (each change tagged with the paragraph relied on, as an input), and keep Article 15's other paragraphs as the text allows.

## What the Law does not say — each a refusal or an input, listed in NOTES.md section 7

How a period of days, weeks or years is counted (this Law counts none, apart from its own "relevant period" in Article 8(2)); the instant of the day at which a silent provision commences; the instant at which a day-named provision commences when a time is stated; what a "sitting" is; how the "date" of a Law's making is fixed when the three steps fall on different dates (beyond Article 2(4)); any rule for legislation that commenced before 28 September 2021 (Article 3(6) leaves that to the earlier law, which this Law does not contain).

## Naming and layout

Module prefix `je21-`: `je21-nouns.l4` (nouns only), then for example `je21-art01-definitions.l4`, `je21-art02-making.l4`, `je21-art03-commencement.l4`, `je21-art04-08-effects.l4`, `je21-art09-subordinate-powers.l4`, `je21-art11-annulment.l4`, `je21-part3-versions.l4`, `je21-part4-office.l4`, `je21-schedule1.l4`, and `je21-tests-*.l4` (one tests module per rule module).
A `je21-seat.l4` layer that imports the rule modules and holds the `@export`ed questions in the reader's words is welcome.
`je21-art03-commencement.l4` must import only `prelude`, `daydate` and `je21-nouns`, and each of its functions must be self-contained: another encoding (the Charities (Jersey) Law 2014's) will COPY them by hand, with a comment citing this subject and the Article.

## Where you work (fixed paths; do not use any other)

| name | path |
| --- | --- |
| `DEPOSIT` (your row; write only here) | `subjects/je/legislation-2021/encodings/legalese-2026-10/` |
| `SOURCES` (read only; never edit) | `subjects/je/legislation-2021/source/` |
| `SCRATCH` (temporary files, logs; nothing goes to `/tmp`) | `<scratch directory, not deposited>` |
| `L4_BIN` | `<path to the pinned l4 binary>` |
| skills (read them first) | `skills/encoding-a-subject/` and `skills/writing-l4-rules/` in the legalese/l4-ide repository (open `SKILL.md`, then the `references/` and `assets/` they point at) |
| the Charities (Jersey) Law 2014 row, for style and tools only | `subjects/je/charities-2014/encodings/legalese-full-2026-10/` (read `g7-commencement.l4`, `g7-tests-commencement.l4`, `domain.l4` for house style; `check.sh`, `srcrefs.py`, `check-traces.py` as models; do not edit anything there) |

`DEPOSIT` already holds `tools/extract_law.py` (how the `.txt` sources were made), `srcrefs.py` (the quotation and locator checker), `check.sh.template` (the skill's `check.sh`, to adapt) and `SOURCE-LICENSE.md`.
Do not run git. Do not edit anything outside `DEPOSIT` and `SCRATCH`.
Do not use the network.
Run `l4` under `nice -n 15`, at most two `l4` processes at a time, and kill a stuck process only by its PID (`kill <pid>`), never with `pkill -f` or a pattern.
Never print or write the environment (`env`, `printenv`).
If you wait for a process, wait on its PID (`kill -0`), never with `pgrep -f` on a name.

## Toolchain and target

You run `L4_BIN`, the prerelease `unstable-20261026-6325439` (`L4_BIN --version` prints it; sha256 of the binary `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475`).
**The target is `unstable`** (ruled for this job by the owner, Meng, 2026-10-28: nobody will run this on a `main` build).
So `REFUSE "…"`, `#ASSERT REFUSED … BECAUSE "…"` and everything else `writing-l4-rules` documents for `unstable` are allowed, and you do not need `fetch-main-l4.sh` or a main-build comparison.
Say in `NOTES.md` that no `main` build has read the deposit.
Leave `JL4_LIBRARY_PATH` unset.
`L4_BIN check FILE` typechecks, `L4_BIN run FILE` also evaluates every `#EVAL`/`#ASSERT`.
Never write a bare `#EVAL` of an expression that refuses: it prints a Warning. Test a refusal with `#ASSERT REFUSED … BECAUSE "…"`.
Warnings are not acceptable in the deposit: every module must run with no `DiagnosticSeverity_Warning` and no error other than a failed assertion that `NOTES.md` records as meant to fail.

## Rules that matter (all of them apply)

- **Seat.** Every encoding in commons is written from the seat of the individual to whom the law is applied.
  Here that individual is the *reader of an enactment*: someone who has to know what an enactment means for them, when it bound them, what it lets be done to them, whether a notice reached them in time.
  Phrase each exported question as that person would ask it ("Was this regulation already in force on 1 June 2018?", "On what day am I treated as having been served?", "Does `person` in this offence reach my company?", "What is the most I can be punished?").
  Facts are ones that person could state.
  A provision that addresses only an official is encoded for what it means to the person (what may be done, what they must be given).
  Put `@export` and `@desc` on every question, `@desc` on every input.
  Record the seat in `NOTES.md` and `encoding.json`.
- **Encode isomorphically and cite.** One source provision, one recognisable place in the L4, with the source's numbering and an `@ref` on every rule.
  Quote the source on `-- src:N | text` lines made by `python3 -I srcrefs.py quote RAW N [M]` (never retyped) and put locators on the `@ref` as `references/source-locators.md` in `encoding-a-subject` describes; `python3 -I srcrefs.py check --refs RAW FILE…` must report 0 problems.
  `RAW` is the `.txt` named below; a quotation from another deposited version is `-- src:<stem>:N | text` with that version's stem (`<stem>.txt` beside `RAW`).
- **Vintages are inputs, never merged.** Every deposited version is in scope as its own answer.
  Where two versions differ, the date (or the version) is an input and each version answers by its own text.
  A version that is silent answers with silence (`REFUSE`), never with a rule borrowed from another version.
- **Where the sources do not answer: `REFUSE "…"`**, never `FALSE`, `0` or a plausible default.
  A call that depends on "unless a contrary intention appears", "unless the context otherwise requires" or "unless provision is made to the contrary" takes that fact as an input (a `BOOLEAN` with a `@desc`); never decide it yourself.
- **Never claim a rule the text does not contain.** Neither Law has a general rule for counting a period of days, weeks or years, and neither defines "day", "week" or "year" (verified by search on 2026-10-28 in every deposited version: the only day/period words are those you will meet in the commencement provisions and in the 2021 Law's definition of "relevant period" in Article 8(2), which is that Article's own).
  No function of yours may count days, add years, or add calendar months to a date.
  Where a question needs that, it takes the computed day as an input or refuses; say so in `NOTES.md`.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
  Expected values are written by hand from the source text before you look at the code's answer.
  Some tests may be meant to fail (in their own file, with the count named in `check.sh`'s `expected_failed` table and in `NOTES.md`); each is then a finding.
- **Read the diagnostics, not the exit code.** `check.sh` (below) does this for you; report the numbers it prints.
- **Nouns first.** One module of nouns only (`DECLARE`, nothing else), imported by the others, then rules module by module along the Law's own structure, then tests.
  Several modules, not one: nothing over about 600 lines.
- **Keep what another encoding will copy small and self-contained.** The commencement functions and the definitions that other encodings need will be COPIED, by hand, into other encodings (L4 cannot import across folders yet).
  So put them in modules that import only `prelude`, `daydate` and your own nouns module, give every function a name that is unique in your row, and say in a comment above each what it answers and which Article it comes from.
- **Use the house style of the Charities row**: backtick names that read as prose, `GIVEN … GIVETH … MEANS/DECIDE`, `§` sections in the Law's order, `BRANCH IF … OTHERWISE` rather than chains of `ELSE IF`, `YMD y m d` for dates (`IMPORT daydate`), no `ASSUME`.
- **Inputs are values.** An `@export`ed rule's inputs are never functions.
- **Register every fork**: a place where the words allow more than one reading and you take one.
  Each fork gets an id (`I1`, `I2`, … for the 1954 Law; `L1`, `L2`, … for the 2021 Law), the readings with the text that licenses each, the reading taken and why, a discriminating case, and — unless the alternative cannot be expressed — a callable alternative with a test (an enum input on the function, with the default stated).
  A fork the Law's words do not create is not a fork.
  "No ambiguities found" is not an answer; say where you looked.

## Deliverables, all under `DEPOSIT`

1. `.l4` modules with ASCII file names (prefix given below). Nouns first. No module over about 600 lines.
2. Tests modules, with expected values hand-written from the source: both sides of every threshold and every date edge, one case per branch of each rule, the same scenario asserted against each version where the versions differ, and `#ASSERT REFUSED … BECAUSE "…"` for every refusal you wrote.
3. `check.sh`: adapt `check.sh.template` (delete the template when done).
   It must: run every `.l4` module with `L4` (default `L4_BIN` above), `L4_TARGET=unstable` as its default, count per module errors / satisfied / failed / refused / warnings reading the line after every `Message:`; take an `expected_failed` and an `expected_refused` table (zero unless listed); run `srcrefs.py check --refs` over every module against `RAW` and fail on any problem; check that no module starts with `@lang en`; exit 0 only when everything passed.
   It prints the numbers; paste its output into `NOTES.md`.
4. `NOTES.md`, which a reviewer reads first, with these numbered sections:
   (1) what is encoded and what is not, in a paragraph; (2) the seat; (3) the target and the build (no main build has read it); (4) the **coverage table**: one row for EVERY paragraph of every deposited version in scope, keyed by the Article/paragraph number as the source writes it, the vintages in which it exists, its disposition (`encoded` / `inert` — quoted, no operative content, say why / `out-of-scope` with a reason of real length / `refused`), and the module and rule names that carry it; no row may be left `deferred`; (5) the **vintage table** (which text governs on which date, with the amendment that made each change, from the endnotes); (6) the **fork register**; (7) **what the Law does not say** (the list of questions a reader will ask and the Law does not answer, each with its refusal); (8) an **answer table** for the headline questions with the source cited per cell; (9) **what `check.sh` prints**; (10) open questions for a domain expert; (11) **provenance**: your model and effort, what you read, anything you ran that was not in this brief.
5. `encoding.json` (see `references/canon-deposit.md` in `encoding-a-subject` for the fields, and `subjects/je/charities-2014/encodings/legalese-full-2026-10/encoding.json` for an example): status `draft`, `not_reviewed` saying no domain expert has read it against the source, the seat, the scope, the sources and their versions, the target `unstable` and the binary, the checks and their numbers, `expected_red`.
6. `SOURCE-LICENSE.md` (already there).
7. A short `README.md` (what this row is, how to run `check.sh`, the module list in dependency order).

## When you finish

Reply with: the final `check.sh` totals (modules, satisfied, failed with the expected number, refused, warnings, srcrefs lines/runs/locators/problems); the fork register as a list of ids and one-line questions; every place where the text did NOT say what this brief said it says (the brief's claims are claims to verify against the text, not facts: if you find one wrong, say so first, with the line numbers); anything you assumed; anything you ran or read that the brief did not list.
Do not report green for a run whose output you did not read.
