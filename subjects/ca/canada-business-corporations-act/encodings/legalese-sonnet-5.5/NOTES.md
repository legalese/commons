# The Canada Business Corporations Act: the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is a plain-text rendering, not the official text, and has not been checked against it. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Canada Business Corporations Act that is deposited in `../../registers/source-bundle/`.
The text was too long for one agent, so it was cut into 5 pieces along its own divisions (Parts, Chapters, Schedules), and each piece is a set of whole line ranges of the source.
A keel agent (`cbca-g0`) ran first and wrote the shared vocabulary, `cbca-core*.l4` and the interpretation provisions.
Then 5 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `cbca-g0` (keel) | the interpretation provisions: the Part I heading, section 2 (definitions; affiliated bodies corporate, control, holding and subsidiary bodies corporate, exemptions, infants) and section 2.1 (individuals with significant control) | 13-114 of R.S.C.-1985-c.-C-44.txt | 8 | 340 | 0 | 73 / 9 / 18 / 0 |
| `cb1` | the title and section 1, the rest of Part I (application), Part II (incorporation), Part III (capacity and powers), Part IV (registered office and records), Part V (corporate finance) and Part VI (sale of constrained shares) | 1-12, 115-693 of R.S.C.-1985-c.-C-44.txt | 21 | 1516 | 217 | 197 / 0 / 12 / 10 |
| `cb2` | Part VII (security certificates, registers and transfers), Part VIII (trust indentures), Part IX (receivers, receiver-managers and sequestrators) and Part X (directors and officers) | 694-1549 of R.S.C.-1985-c.-C-44.txt | 43 | 3014 | 330 | 247 / 38 / 273 / 2 |
| `cb3` | Part XI (insider trading), Part XII (shareholders), Part XIII (proxies), Part XIV (financial disclosure) and Part XIV.1 (disclosure relating to diversity) | 1550-2095 of R.S.C.-1985-c.-C-44.txt | 21 | 1900 | 299 | 212 / 28 / 5 / 7 |
| `cb4` | Part XV (fundamental changes), Part XVI (going-private and squeeze-out transactions), Part XVII (compulsory and compelled acquisitions) and Part XVIII (liquidation and dissolution) | 2096-2861 of R.S.C.-1985-c.-C-44.txt | 27 | 1911 | 299 | 247 / 15 / 3 / 2 |
| `cb5` | Part XIX (investigation), Part XIX.1 (apportioning award of damages), Part XX (remedies, offences and punishment), Part XX.1 (documents in electronic or other form), Part XXI (general), the Schedule (offences), and the Related Provisions and Amendments Not in Force at the end of the file | 2862-3671 of R.S.C.-1985-c.-C-44.txt | 23 | 1399 | 185 | 174 / 12 / 44 / 4 |
| **whole** | | | **143** | **10080** | **1330** | **1150 / 102 / 355 / 25** |

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
Its last line: `TOTAL (143 modules) 0 10080 0 0 | 0 10080 0 0`; exit status 0.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 257.
They have not been reviewed one by one.

## What is not claimed

- No domain expert has read any row against the official text, and the source is a plain-text rendering made by a converter script.
- The pieces are not wired to each other.
  They were written at the same time, so a provision in one piece that depends on a provision in another takes it as a plain input named for the fact, commented `-- out of range: ...`.
  Each `NOTES-<agent>.md` lists these under `Cross-references out of my ranges`, and what it needs from the keel under `Needs from the core`.
- There are several seat modules, one or two per piece, not one per seat as the Guide's section 3 describes; the questions in each call that piece's layer-1 rules only.
- Provisions are marked inert for four reasons: the Guide's machinery list, an amendment of another instrument, an amendment the source itself shows as not in force, and a pure citation or title.
  The last three are additions made for this run; they were assumed, not ruled.
- `check.sh` does not compare `#TRACE` outcomes; its own header says so.
  The folder was checked on the `main` build only; it was not run on an `unstable` build.
- 6 top-level names are defined in more than one module: 3 in seat modules (`Is the Director entitled to appear and be heard on my application`; `May I, as a shareholder, call the meeting to fill the vacancy`; `Must I give the Director notice of my application`) and 3 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
