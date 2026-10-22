# The Universal Credit Regulations 2013: the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is a plain-text rendering, not the official text, and has not been checked against it. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Universal Credit Regulations 2013 that is deposited in `../../registers/source-bundle/`.
The text was too long for one agent, so it was cut into 4 pieces along its own divisions (Parts, Chapters, Schedules), and each piece is a set of whole line ranges of the source.
A keel agent (`uc-g0`) ran first and wrote the shared vocabulary, `uc-core*.l4` and the interpretation provisions.
Then 4 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `uc-g0` (keel) | regulation 2 (interpretation) | 12-117 of uksi-2013-376.txt | 8 | 144 | 0 | 31 / 6 / 36 / 5 |
| `uc1` | the preamble and regulation 1 (citation and commencement), the rest of Part 1 (introduction), Part 2 (entitlement), Part 3 (awards) and Part 4 (elements of an award) | 1-11, 118-742 of uksi-2013-376.txt | 21 | 1567 | 116 | 147 / 43 / 23 / 11 |
| `uc2` | Part 6 (calculation of capital and income), Part 7 (the benefit cap) and Schedule 10 (capital to be disregarded) | 845-1358, 2814-2872 of uksi-2013-376.txt | 19 | 1510 | 130 | 206 / 3 / 30 / 11 |
| `uc3` | Schedules 1 to 5 (meaning of payments in respect of accommodation; liability to make payments; occupation of accommodation; housing costs element for renters; housing costs element for owner-occupiers) | 1821-2721 of uksi-2013-376.txt | 25 | 1137 | 55 | 203 / 43 / 75 / 20 |
| `uc4` | Part 5 (capability for work or work-related activity), Part 8 (claimant responsibilities), Schedules 6 to 9 (the assessments of limited capability for work, and for work and work-related activity, and the cases in which it is treated as present) and Schedule 11 (application of ESA or JSA sanctions) | 743-844, 1359-1820, 2722-2813, 2873-2914 of uksi-2013-376.txt | 30 | 1812 | 68 | 133 / 67 / 43 / 11 |
| **whole** | | | **103** | **6170** | **369** | **720 / 162 / 207 / 58** |

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
Its last line: `TOTAL (103 modules) 0 6170 0 0 | 0 6170 0 0`; exit status 0.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 54.
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
- 32 top-level names are defined in more than one module: 1 in seat modules (`Am I a pre-2026 claimant for the LCWRA element`) and 31 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
