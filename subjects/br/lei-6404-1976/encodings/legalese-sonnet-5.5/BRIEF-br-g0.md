# Keel brief: the shared vocabulary of the Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976) (L4, stable)

You are the **keel agent** for the encoding of the Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976) (Lei nº 6.404/1976), from the Portuguese-language text deposited in `INPUTS_DIR`.
After you finish, 7 part agents will each encode one contiguous piece of the text, at the same time, each in its own folder and unable to see the others.
They will import the modules you write, and they will take their facts about the whole text from your notes.
So what you write is the keel they build on: a name, a type or a convention you get wrong is copied into 7 pieces.
This brief is the whole specification. Read it fully before opening any source.

You work alone: no subagents. You check your own work with the diagnostics.

## What you are building

1. **The core module `br-core.l4`**: the shared vocabulary, as `DECLARE`d records and enumerations, for the people, things, measures and kinds that the text names and that two or more pieces will need.
   Examples of what belongs: the kinds of person and body the text names; the kinds of the main thing the text governs; enumerations the text lists; units (money, percentage, days) and the one way they are written; the one way a time limit is written.
   A type used by one piece only does not belong: that piece defines it. Keep the core as small as it can be; around 250 lines is a guide and not a limit.
   It imports only `prelude` (and `daydate` if you need dates).
2. **The encoded interpretation provisions of your range, if you have one**, as tested layer-1 modules `br-core-<topic>.l4` that import the core: every definition the text gives that can be worked out from facts becomes a rule (a function from the facts to the defined concept), each with `@ref` and a quoted source line; a definition that points to a provision outside your range ("has the meaning in regulation 89") is not encoded by you: record it in the table of defined terms, naming the piece that encodes it, and give the term a plain input type in the core only if two or more pieces will need it.
   Your range: no provisions of its own: the Law has no interpretation section, so the keel writes the shared vocabulary and the Portuguese naming conventions only.
3. **Tests**: files `br-core-tests-<topic>.l4` with assertions for the core's rules and the definitional rules, expected values written from the text.
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
| br-g0 (keel) | no provisions of its own: the Law has no interpretation section, so the keel writes the shared vocabulary and the Portuguese naming conventions only | none | 0 | none |
| br1 | Capítulos I a IV (características e natureza da companhia ou sociedade anônima, capital social, ações, partes beneficiárias) | 1-371 | 8,718 | Art. 1º to Art. 51 |
| br2 | Capítulos V a IX (debêntures, bônus de subscrição, constituição da companhia, formalidades complementares da constituição, livros sociais) | 372-807 | 9,141 | Art. 52 to Art. 105 |
| br3 | Capítulos X e XI (acionistas, assembléia-geral) | 808-1232 | 10,361 | Art. 106 to Art. 137 |
| br4 | Capítulos XII a XIV (conselho de administração e diretoria, conselho fiscal, modificação do capital social) | 1233-1554 | 8,867 | Art. 138 to Art. 174 |
| br5 | Capítulos XV e XVI (exercício social e demonstrações financeiras; lucro, reservas e dividendos) | 1555-1957 | 8,737 | Art. 175 to Art. 205 |
| br6 | Capítulos XVII a XX (dissolução, liquidação e extinção; transformação, incorporação, fusão e cisão; sociedades de economia mista; sociedades coligadas, controladoras e controladas) | 1958-2325 | 9,033 | Art. 206 to Art. 264 |
| br7 | Capítulos XXI a XXVI (grupo de sociedades, consórcio, sociedades em comandita por ações, prazos de prescrição, disposições gerais, disposições transitórias) | 2326-2593 | 6,476 | Art. 265 to Art. 300 |

Use the table to say, for each defined term, which piece encodes the provision it points to.
The seat the pieces will write for, so that you choose types a person in that position can supply facts for, is: um acionista, inclusive o acionista minoritário, de uma companhia (sociedade anônima), perguntando o que a Lei lhe garante, o que lhe exige, e o que a companhia, os administradores e o acionista controlador podem fazer em relação a ele. (In English: a shareholder (acionista), including a minority shareholder, of a company (sociedade anônima), asking what the Law gives them, what it requires of them, and what the company, its managers and its controlling shareholder may do in relation to them.)
You write no seat layer and no `@export`.

## Reading

Read the headings of the whole text first, through `inputs/SECTION-INDEX.txt` and `grep -n` for `PART`, `Part`, `CAPÍTULO`, `SCHEDULE` and similar lines of the text file; then read your range in full with `sed -n 'A,Bp'`; then sample the sections where the main entities are introduced, enough to choose the types.
**Never read a whole text file in one go**: the texts are far longer than you need.
Also read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md` before you write any L4, and `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` for the shape of a seat layer (which you do not write).

## The subject and the sources

- **the Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976)**, Lei nº 6.404/1976.
- Source file(s) in `INPUTS_DIR`: `lei-6404-1976.pt.txt`. Each line number in this brief refers to lines of those files.
- `inputs/SOURCES.md` records where each came from, its version or currency date, its URL and its hashes. **Read it.**
- Each `.txt` is a plain-text rendering of the official source made by a converter script; it is not the official text and it is not marked up. Say so in `NOTES.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited.
- `inputs/SECTION-INDEX.txt` lists, by line number, where each section or regulation opens, with the heading it sits under; it was made by a script, so the text is authoritative.
- Encode only from these files. Quote the text mechanically; never reconstruct wording from memory.


## Language: the source is in Portuguese

Identifiers (the backticked names), the `@export` question text, the `@desc` text and the `§` headings are in Brazilian Portuguese, worded as the shareholder (`acionista`) would be asked ("Posso exercer o direito de retirada se votei contra a deliberação?").
`NOTES.md`, `PROGRESS.md` and your comments are in English, with a plain English gloss of each rule beside the Portuguese words it quotes; the quoted `-- src:N |` lines stay exactly as the source has them.
Accented letters in identifiers compile on the stable binary: a three-line probe on 1.6.98 on 2026-10-22 accepted backticked names with ç, ã, é, õ and ú, and an `@export` line with accents, and `srcrefs.py check --refs` accepted a quoted accented line from this very text.
So spell words properly; do not strip accents. File names are ASCII.
Write no `@lang` line and no `@nlg:xx` annotation: the stable build does not accept them.
The source wraps wording that Planalto shows struck through, which is superseded wording, as `⟦STRUCK: ...⟧`: treat it as no longer in force (the line beside it that replaces it typically carries "(Redação dada pela ...)", as at line 1211).
Never encode struck text; in the coverage table a provision that is wholly struck is `repealed or blank in this text`, and a provision with struck and live parts is encoded from the live part only, with the struck part named in the row's note.
The source also keeps amendment notes inline ("(Redação dada pela Lei nº 10.303, de 2001)"); they are part of the line you quote, not provisions.

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

`DEPOSIT/encodings/legalese-sonnet-5.5/` already holds `check.sh` and `srcrefs.py`. You add, flat in that folder (no subfolders, ASCII filenames beginning `br-core`): `br-core.l4`, any `br-core-<topic>.l4` interpretation modules, the `br-core-tests-*.l4` tests, `NOTES.md` and `PROGRESS.md`.
You do not write `encoding.json`, `SOURCE-LICENSE.md`, `subject.json`, `README.md` or `source/`, and you do not copy this brief.
Write `NOTES.md` and `PROGRESS.md` yourself and nothing else of the report kind: the harness refuses to let a subagent write report-style files (`FINDINGS.md`, `REPORT.md`, `PLAN.md` and the like) and tells you to return findings as text. The pieces will read your `NOTES.md` as their guide, so it is the one place to put the plan. Your last message is the final report, and the files in the folder are the deliverable.
Keep `PROGRESS.md` current (what is done, what is next, decisions taken and the section that licenses each): if your context is compacted, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/t2/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here) and `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/t2/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
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
Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`; nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/t2` other than your own folder `br6404/keel/`; nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/porridge` except that you run the `L4_BIN` binary named in your task; and nothing under `~/.claude/`.
The one exception is `inputs/EXAMPLE-sg-employment-act-seat/`, which is yours to read.
If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) the vocabulary in one line per type; (4) the naming conventions in one line each; (5) the defined terms and where each is encoded, counted by kind; (6) the coverage summary for your range (counts per disposition, and sections in your range against rows); (7) forks; (8) anything a part agent will trip on; (9) `peeked`: nothing, or what you opened by accident.
