# Keel brief: the shared vocabulary of the Israeli Companies Law, 5759-1999 (חוק החברות, התשנ״ט–1999) (L4, stable)

You are the **keel agent** for the encoding of the Israeli Companies Law, 5759-1999 (חוק החברות, התשנ״ט–1999) (Sefer HaChukim 5759, p 189), from the Hebrew-language text deposited in `INPUTS_DIR`.
After you finish, 6 part agents will each encode one contiguous piece of the text, at the same time, each in its own folder and unable to see the others.
They will import the modules you write, and they will take their facts about the whole text from your notes.
So what you write is the keel they build on: a name, a type or a convention you get wrong is copied into 6 pieces.
This brief is the whole specification. Read it fully before opening any source.

You work alone: no subagents. You check your own work with the diagnostics.

## What you are building

1. **The core module `ic-core.l4`**: the shared vocabulary, as `DECLARE`d records and enumerations, for the people, things, measures and kinds that the text names and that two or more pieces will need.
   Examples of what belongs: the kinds of person and body the text names; the kinds of the main thing the text governs; enumerations the text lists; units (money, percentage, days) and the one way they are written; the one way a time limit is written.
   A type used by one piece only does not belong: that piece defines it. Keep the core as small as it can be; around 250 lines is a guide and not a limit.
   It imports only `prelude` (and `daydate` if you need dates).
2. **The encoded interpretation provisions of your range, if you have one**, as tested layer-1 modules `ic-core-<topic>.l4` that import the core: every definition the text gives that can be worked out from facts becomes a rule (a function from the facts to the defined concept), each with `@ref` and a quoted source line; a definition that points to a provision outside your range ("has the meaning in regulation 89") is not encoded by you: record it in the table of defined terms, naming the piece that encodes it, and give the term a plain input type in the core only if two or more pieces will need it.
   Your range: lines 1-262 of `companies-law-5759-1999.he.wiki.txt` (3,654 words): the title block and table of contents (lines 1-154, one `inert` row) and Part 1, interpretation (section 1, definitions).
3. **Tests**: files `ic-core-tests-<topic>.l4` with assertions for the core's rules and the definitional rules, expected values written from the text.
4. **`NOTES.md`**, which is the shared notes for all the pieces and must say, under exactly these headings:
   - `## Vocabulary`: a table `| name | kind | what it is | licensed by |` of every type and enumeration constructor in the core;
   - `## Naming conventions`: how a rule, an input, an enumeration constructor and a question are named; how amounts, percentages, days and dates are written (the type, the unit, and what a fraction is); how a fact about something outside a piece is taken as an input; anything else two pieces would otherwise do differently;
   - `## Defined terms`: a table `| term | defined at | encoded in | note |` for every term the text defines (in your range or by pointing elsewhere), giving the module and rule that encode it, or "by reference: encoded by piece X, section N, taken there as an input";
   - `## Instructions to the pieces`: a short list of things a part agent must know before it imports your modules;
   - `## Coverage table` (your range, the rule below); `## Fork register`; `## What the stable binary does not accept`; `## What check.sh prints`.
5. **`PROGRESS.md`**: kept up to date as you go.

## The whole range, nothing left out (ruled by Meng, 2026-10-22)

The whole text is encoded in one pass; nothing is left out because it matters little to the seat.
If you have a range, your coverage table has one row per provision of it (per section, and per subsection or paragraph where they differ), with the columns `| provision | source lines | disposition | where | note |`, and a disposition of `encoded`, `inert` (machinery, an amendment of another instrument, an amendment the source shows as not in force, or a pure citation or title, with a reason of real length), `repealed or blank in this text`, or `fork`.
"Out of the seat's scope" is never a reason. A reviewer will count the headings in your range against your rows.

## The pieces that will import your modules

| piece | what it encodes | lines | words | first and last section label opening in it |
| --- | --- | --- | --- | --- |
| ic-g0 (keel) | the title block and table of contents (lines 1-154, one `inert` row) and Part 1, interpretation (section 1, definitions) | 1-262 | 3,654 | 1 to 1 |
| ic1 | Part 2 (formation of the company: incorporation, articles, the Registrar of Companies) and Part 3 chapters 1 to 3 (the organs of the company; the general meeting; the board of directors) | 263-947 | 9,261 | 2 to 118ב |
| ic2 | Part 3 chapter 4 (the general manager), Part 4 (administration: registered office and digital address, registers of shareholders, reporting, internal auditor, external auditor, financial statements), Part 5 (the shareholder: shares, rights and duties, the derivative action) and Part 6 chapter 1 (appointment and term of directors) | 948-1684 | 10,326 | 119 to 249ג |
| ic3 | Part 6 chapters 2 to 5 (other office-holders, duties of office-holders, rights of a director, compensation policy, transactions with interested parties) and Part 7 (the company's capital: securities, capital maintenance and distributions) | 1685-2080 | 6,557 | 250 to 313 |
| ic4 | Part 8 (acquisition of companies: merger, special tender offer, forced sale of shares), Part 8A (dissolution: by a court, voluntary, fast-track, miscellaneous) and the opening of Part 9 (changing types of corporation) | 2081-2515 | 7,213 | 314 to 345 |
| ic5 | Part 9 chapter 1A (the public-benefit company), the longest single chapter of the Law | 2516-2955 | 9,398 | 345א to 345נג |
| ic6 | Part 9 chapters 2 to 6 (foreign company, compromise or arrangement, striking off a company, remedies, financial sanction and defaulting-company registration, public companies and debenture companies, regulations), Part 10 (cancellation, transitional provisions, application and commencement), the Schedules and the signature block | 2956-3556 | 8,782 | 346 to תוספת 4 פרט 2 |

Use the table to say, for each defined term, which piece encodes the provision it points to.
The seat the pieces will write for, so that you choose types a person in that position can supply facts for, is: a person who founds, directs or holds shares in a company under the Companies Law (a founder, a director or officer, a shareholder including a minority shareholder), asking what the Law lets them do, what it requires of them, what they may require of the company, and what can be done to them.
You write no seat layer and no `@export`.

## Reading

Read the headings of the whole text first, through `inputs/SECTION-INDEX.txt` and `grep -n` for `PART`, `Part`, `CAPÍTULO`, `SCHEDULE` and similar lines of the text file; then read your range in full with `sed -n 'A,Bp'`; then sample the sections where the main entities are introduced, enough to choose the types.
**Never read a whole text file in one go**: the texts are far longer than you need.
Also read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md` before you write any L4, and `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` for the shape of a seat layer (which you do not write).

## The subject and the sources

- **the Israeli Companies Law, 5759-1999 (חוק החברות, התשנ״ט–1999)**, Sefer HaChukim 5759, p 189.
- Source file(s) in `INPUTS_DIR`: `companies-law-5759-1999.he.wiki.txt`. Each line number in this brief refers to lines of those files.
- `inputs/SOURCES.md` records where each came from, its version or currency date, its URL and its hashes. **Read it.**
- Each `.txt` is a plain-text rendering of the official source made by a converter script; it is not the official text and it is not marked up. Say so in `NOTES.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited.
- `inputs/SECTION-INDEX.txt` lists, by line number, where each section or regulation opens, with the heading it sits under; it was made by a script, so the text is authoritative.
- Encode only from these files. Quote the text mechanically; never reconstruct wording from memory.
The source file is NOT a plain-text rendering: it is the raw MediaWiki source of the Hebrew Wikisource page, 3,555 lines, with the markup the language section below describes; read that section before the first chunk. The Law has eleven Parts (1 interpretation, 2 formation, 3 structure, 4 administration, 5 the shareholder, 6 office-holders, 7 capital, 8 acquisition of companies, 8A dissolution, 9 general provisions, 10 cancellation, transitional provisions, application and commencement), five Schedules (1, 1A, 2, 3 and 4) and a signature block. Laws, regulations and orders that the text cites (the Securities Law, the Income Tax Ordinance, regulations made under this Law) are NOT among your inputs: where a rule depends on one, take its outcome as a plain input with a comment and list it in `NOTES.md`. Coverage, stated plainly: every heading in your range (the title, the chapter, each subchapter or part and chapter, and each section heading) gets a coverage row, a heading that is not itself a provision getting an `inert` row, its reason being that it is a pure title (a heading); and every non-blank line of your range, History lines and struck or repealed runs included, must fall inside the source-lines cell of some row (write `src:N` or `src:N-M` there). The lead runs a script that lists the non-blank lines no row names, and sends the agent back to fix them.

## Language: the source is in Hebrew, as raw MediaWiki

The source is the Hebrew text of the law as maintained on Hebrew Wikisource, in its raw MediaWiki form: an unofficial consolidation (Israel publishes no free official consolidated text).
Say so in `NOTES.md`; never claim it is verified against the official text.
This overrides the bullet above that calls the text file a plain-text rendering that is not marked up: this file IS marked up, as follows. Each template is part of the line you quote and none of them is a provision.
- `{{ח:סעיף|N|heading|תיקון: ...}}` opens section N (N can carry a Hebrew letter, as in `116א`); the third field is the section's heading, and the `תיקון:` field lists the years of the amending Acts.
  `{{ח:סעיף*|N|heading|עוגן=...}}` opens an item inside a Schedule: the section index labels it with its anchor, such as `תוספת 3 פרט 2`, and you write that same string in the provision cell of its coverage row.
- `{{ח:ת}}` begins the section's own text; `{{ח:תת|(א)}}`, `{{ח:תתת|(1)}}` and `{{ח:תתתת|(א)}}` begin a subsection, a paragraph and a subparagraph; `{{ח:ת|סוג=הגדרה}}` marks a definition.
- `{{ח:קטע1|...}}` to `{{ח:קטע4|...}}` open a Part (חלק), a Chapter (פרק), a Sub-chapter (סימן) and the Schedules (תוספת).
  `{{ח:הערה|(בוטל)}}` and a bare `בוטל` mark text the source shows as repealed.
  `{{ח:פנימי|...|text}}` and `{{ח:חיצוני|...|text}}` are links.
- The section label `351ו` opens two sections in this file (lines 3135 and 3140); quote each by its own line numbers and say in `NOTES.md` which row is which.
- Lines 1 to 154 are the title block and a table of contents made of links. They are not provisions: give them one `inert` row (a pure citation or title).

Language of your work:
- Identifiers (the backticked names), the `@export` and `@desc` texts and the `§` headings are in Hebrew, in the words the law uses, worded as the person in the seat would be asked ("האם אני רשאי לדרוש כינוס אסיפה מיוחדת?").
  After the Hebrew, an `@export` or `@desc` text carries ` / ` and a plain English gloss, which is the convention of the existing Israeli Penal Law encoding in this repository (assumed here, not ruled); the `§` headings are Hebrew only.
- `NOTES.md`, `PROGRESS.md` and your comments are in English, with a plain English gloss of each rule beside the Hebrew words it quotes; the `-- src:N |` quote lines stay exactly as the source has them, markup included.
- Hebrew compiles on the stable binary: a probe on 1.6.98 on 2026-10-25 accepted Hebrew backticked names, `@export` and `@desc` lines in Hebrew followed by ` / ` and English, and an `@ref סעיף 2 (src:268)` over a `-- src:268 |` quote line that carries the `{{ח:ת}}` template, and `srcrefs.py check --refs` reported 0 problems on it.
  Write digits in names as ASCII digits, and cite a section as `סעיף 116א`.
  If the stable build or `srcrefs.py` rejects anything Hebrew, say so under `What the stable binary does not accept` in `NOTES.md`.
- Write no `@lang` line and no `@nlg` annotation: the stable build does not accept them. File names are ASCII.

## Writing L4 that the stable binary accepts

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Smaller gaps:** `YMD` is missing from the stable prelude, so add a local shim (`YMD y m d MEANS Date d m y`). `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.

The target dialect is `main`: the stable build 1.6.98 named as L4_BIN. Read step 0 of `writing-l4-rules/SKILL.md` and `references/dialects.md` (its "write instead" column) before you write; for any construct the stable binary rejects, write what `dialects.md` says to write instead.

Dates are data. Where your range contains the date of enactment or making of the text, or the date it comes into force, or a commencement rule, carry it as a defined value with an `@ref`: the date in the title block or the assent date if the text gives one, and any commencement date the text fixes or defines by a rule such as "three months after passing", derived from the enactment date where the text says so. Where the text leaves commencement to an order, take the commencement date as a stated input and say so in `NOTES.md`. These dates are what rule-effective-date logic needs; they are not "commencement machinery", which stays out. If your range contains no such provision, say so in `NOTES.md` and do nothing.

## Deliverables, all under your `DEPOSIT` directory (given in your task)

`DEPOSIT/encodings/legalese-sonnet-5.5/` already holds `check.sh` and `srcrefs.py`. You add, flat in that folder (no subfolders, ASCII filenames beginning `ic-core`): `ic-core.l4`, any `ic-core-<topic>.l4` interpretation modules, the `ic-core-tests-*.l4` tests, `NOTES.md` and `PROGRESS.md`.
You do not write `encoding.json`, `SOURCE-LICENSE.md`, `subject.json`, `README.md` or `source/`, and you do not copy this brief.
Write `NOTES.md` and `PROGRESS.md` yourself and nothing else of the report kind: the harness refuses to let a subagent write report-style files (`FINDINGS.md`, `REPORT.md`, `PLAN.md` and the like) and tells you to return findings as text. The pieces will read your `NOTES.md` as their guide, so it is the one place to put the plan. Your last message is the final report, and the files in the folder are the deliverable.
Keep `PROGRESS.md` current (what is done, what is next, decisions taken and the section that licenses each): if your context is compacted, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/skills/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here) and `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/skills/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Cite the section on every rule with `@ref`**; follow `encoding-a-subject/references/source-locators.md` for quoting and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>`; it must report 0 problems. 
- **Where the source does not answer,** return an explicit "not covered" value and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** Run `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` and report the numbers it prints: it must show 0 errors, 0 failed and 0 refused.
- **The core must compile before you finish**, and every module you wrote must be importable by a file in the same folder: write a three-line throwaway file that imports each module and calls one of its rules, run it, and delete it.
- **No sleep-polls and no waiting loops.** Do not git add, commit or push anything. Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.98, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.

## Independence

You may read: `INPUTS_DIR`, your own `DEPOSIT`, the two skills and their references, and the Commons guide copies in `inputs/`. Nothing else on disk.
Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`; nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/td` other than your own folder `ic/keel/`; nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/stable` except that you run the `L4_BIN` binary named in your task; and nothing under `~/.claude/`.
The one exception is `inputs/EXAMPLE-sg-employment-act-seat/`, which is yours to read.
If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) the vocabulary in one line per type; (4) the naming conventions in one line each; (5) the defined terms and where each is encoded, counted by kind; (6) the coverage summary for your range (counts per disposition, and sections in your range against rows); (7) forks; (8) anything a part agent will trip on; (9) `peeked`: nothing, or what you opened by accident.
