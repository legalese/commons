# The Israeli Companies Law, 5759-1999 (חוק החברות, התשנ״ט–1999): the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is the raw MediaWiki source of an unofficial Hebrew Wikisource consolidation, not the official text of Sefer HaChukim, and has not been checked against the official text. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Israeli Companies Law, 5759-1999 (חוק החברות, התשנ״ט–1999) that is deposited in `../../registers/source-bundle/`.
The text was too long for one agent, so it was cut into 6 pieces along its own divisions (Parts, chapters and Schedules), and each piece is a set of whole line ranges of the source file.
A keel agent (`ic-g0`) ran first and wrote the shared vocabulary, `ic-core*.l4`, and the provisions of the opening Part (the title block, the table of contents and the definitions).
Then 6 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `ic-g0` (keel) | the title block and table of contents (lines 1-154, one `inert` row) and Part 1, interpretation (section 1, definitions) | 1-262 of companies-law-5759-1999.he.wiki.txt | 11 | 256 | 0 | 74 / 8 / 23 / 2 |
| `ic1` | Part 2 (formation of the company: incorporation, articles, the Registrar of Companies) and Part 3 chapters 1 to 3 (the organs of the company; the general meeting; the board of directors) | 263-947 of companies-law-5759-1999.he.wiki.txt | 24 | 1829 | 268 | 224 / 20 / 60 / 4 |
| `ic2` | Part 3 chapter 4 (the general manager), Part 4 (administration: registered office and digital address, registers of shareholders, reporting, internal auditor, external auditor, financial statements), Part 5 (the shareholder: shares, rights and duties, the derivative action) and Part 6 chapter 1 (appointment and term of directors) | 948-1684 of companies-law-5759-1999.he.wiki.txt | 35 | 2483 | 363 | 241 / 15 / 51 / 28 |
| `ic3` | Part 6 chapters 2 to 5 (other office-holders, duties of office-holders, rights of a director, compensation policy, transactions with interested parties) and Part 7 (the company's capital: securities, capital maintenance and distributions) | 1685-2080 of companies-law-5759-1999.he.wiki.txt | 18 | 1259 | 129 | 57 / 11 / 31 / 2 |
| `ic4` | Part 8 (acquisition of companies: merger, special tender offer, forced sale of shares), Part 8A (dissolution: by a court, voluntary, fast-track, miscellaneous) and the opening of Part 9 (changing types of corporation) | 2081-2515 of companies-law-5759-1999.he.wiki.txt | 17 | 1334 | 163 | 146 / 15 / 29 / 0 |
| `ic5` | Part 9 chapter 1A (the public-benefit company), the longest single chapter of the Law | 2516-2955 of companies-law-5759-1999.he.wiki.txt | 27 | 1550 | 211 | 150 / 26 / 24 / 1 |
| `ic6` | Part 9 chapters 2 to 6 (foreign company, compromise or arrangement, striking off a company, remedies, financial sanction and defaulting-company registration, public companies and debenture companies, regulations), Part 10 (cancellation, transitional provisions, application and commencement), the Schedules and the signature block | 2956-3556 of companies-law-5759-1999.he.wiki.txt | 33 | 1560 | 180 | 158 / 20 / 50 / 29 |
| **whole** | | | **165** | **10271** | **1314** | **1050 / 115 / 268 / 66** |

Each agent's files are `NOTES-<agent>.md` (fixed headings, the coverage table and the fork register among them) and `PROGRESS-<agent>.md`.
A coverage row names a provision, its source lines, a disposition (encoded, fork, inert, or repealed or blank in the text), and where in the modules it is encoded.
An inert row gives its reason; titles and headings are inert because they state no rule, and a heading has a row of its own, so the inert count is large where the text has many headings.

## Target

The encoding is written for the `main` compiler, the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19).
Where a piece needed something the stable build does not accept, its `NOTES-<agent>.md` says so under `What the stable binary does not accept`.

## What was checked

The output of `./check.sh` in this folder, run at its default target (`main`) with `L4` and `L4_MAIN` both set to the stable build above and `JL4_LIBRARY_PATH` unset, is in `encoding.json` under `checks`.
The build written with and the main build compared with are the same build, so the main columns are a second run of one compiler, not a comparison between two.
Its main columns read `same` for every module.
Its last line: `TOTAL (165 modules) 0 10271 0 0 | 0 10271 0 0`; exit status 0.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 135.
They have not been reviewed one by one.

## What is not claimed

- No domain expert has read any row against the official text, and the source is not an official text: it is the raw MediaWiki source of the Hebrew Wikisource page (see `encoding.json`, `edition`), an unofficial consolidation.
  Israel publishes no free official consolidated text; the official version is the original publication in Reshumot together with every amending Act, and nothing here was compared with it.
- The pieces are not wired to each other.
  They were written at the same time, so a provision in one piece that depends on a provision in another takes it as a plain input named for the fact, commented `-- out of range: ...`.
  Each `NOTES-<agent>.md` lists these under `Cross-references out of my ranges`, and what it needs from the keel under `Needs from the core`.
- There are several seat modules, one or two per piece, not one per seat as the Guide's section 3 describes; the questions in each call that piece's layer-1 rules only.
- Provisions are marked inert for four reasons: the Guide's machinery list, an amendment of another instrument, an amendment the source itself shows as not in force, and a pure citation or title.
  The last three are additions made for this run; they were assumed, not ruled.
- `check.sh` does not compare `#TRACE` outcomes; its own header says so.
  The folder was checked on the `main` build only; it was not run on an `unstable` build.
- 11 top-level names are defined in more than one module: 11 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
- Identifiers are in Hebrew, and the Hebrew of each `@export` and `@desc` is followed by ` / ` and a plain English gloss (assumed here, not ruled; the Penal Law 5737-1977 encoding in `il/penal-law-1977` does the same); `NOTES-*.md`, `PROGRESS-*.md` and comments are in English; quoted source lines are in the source's Hebrew, with its MediaWiki markup.
- The seat layer of `ic2` (`ic2-seat.l4` and `ic2-cases-seat.l4`) was written mostly by four forks of the `ic2` agent, against the brief's "no subagents"; `NOTES-ic2.md` says so under `Before this is worth relying on`, with the review that was done and its limit.
- The source file has two sections headed `351ו`, at lines 3135 and 3140, with the same words (the deposit's meta file records the duplicate as not investigated); `ic6` took them as one provision that the Wikisource page repeats and gave each copy its own coverage rows (fork F-ic6-9 in `NOTES-ic6.md`).
- Some agents kept files of their own outside their deposit (scripts, templates, probes or check outputs), and none of them is in this repository: `ic1` (ic1-work in the run's scratchpad); `ic2` (ic2-tools in the run's scratchpad); `ic3` (work/ beside its deposit; cases-run.out in the run's scratchpad; checksh3.out in the run's scratchpad); `ic4` (inputs/_work; fixsec.py in the run's scratchpad; seatq.txt in the run's scratchpad); `ic5` (inputs/work); `ic6` (inputs/work).
  The list comes from the agents' sandboxes and from the paths their tool calls name; a path is a mention, not proof that anything was read or written there.
  Where an agent's `NOTES-<agent>.md` or `PROGRESS-<agent>.md` mentions such a file, the path is the run's own and does not exist here.
