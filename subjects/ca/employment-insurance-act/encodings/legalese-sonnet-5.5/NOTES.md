# The Employment Insurance Act and the Employment Insurance Regulations: the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is a plain-text rendering, not the official text, and has not been checked against it. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Employment Insurance Act and the Employment Insurance Regulations that is deposited in `../../registers/source-bundle/`: the Act and the Regulations, as two text files.
The texts were too long for one agent, so each was cut into pieces along its own divisions (Parts, Divisions, Schedules), 13 pieces in all, and each piece is a set of whole line ranges of one source file.
A keel agent (`ei-g0`) ran first and wrote the shared vocabulary, `eia-core*.l4`, and the interpretation provisions; the Act and the Regulations share it.
Then 13 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `ei-g0` (keel) | the Act's title, sections 1 to 3 and the interpretation provisions (section 2 and the definitions that follow it), with the vocabulary shared by the Act and the Regulations | 1-132 of S.C.-1996-c.-23.txt | 8 | 218 | 0 | 46 / 9 / 35 / 4 |
| `ei1` | Part I (unemployment benefits), first part: from the opening of Part I (line 133) to line 669 | 133-669 of S.C.-1996-c.-23.txt | 20 | 1345 | 119 | 149 / 21 / 11 / 14 |
| `ei2` | Part I (unemployment benefits), second part (lines 670 to 1048), and Part II (employment support measures and National Employment Service) | 670-1126 of S.C.-1996-c.-23.txt | 23 | 882 | 101 | 101 / 29 / 65 / 9 |
| `ei3` | Part III (premiums and other financial matters), Part IV (insurable earnings and collection of premiums) and Part V (pilot projects) | 1127-1803 of S.C.-1996-c.-23.txt | 28 | 1187 | 88 | 148 / 46 / 36 / 12 |
| `ei4` | Part VI (administrative provisions), Part VII (benefit repayment), Part VIII (self-employed persons engaged in fishing), Part VIII.1 (alternate access to special benefits), Part VIII.2 (regulations: provincial plans) and Part VIII.3 (interim orders) | 1804-2108, 2689-2762 of S.C.-1996-c.-23.txt | 16 | 663 | 76 | 99 / 11 / 42 / 15 |
| `ei5` | Part VII.1 (benefits for self-employed persons) | 2109-2688 of S.C.-1996-c.-23.txt | 22 | 1061 | 146 | 144 / 37 / 26 / 5 |
| `ei6` | Part VIII.4 (Employment Insurance Emergency Response Benefit), Part VIII.5 and Part VIII.6 (temporary measures), Part IX (repeals, transitional provisions, related and conditional amendments and coming into force) and the Schedules | 2763-3598 of S.C.-1996-c.-23.txt | 34 | 1305 | 109 | 127 / 17 / 14 / 8 |
| `ei7` | the Related Provisions and the Amendments Not in Force at the end of the Act's file | 3599-4202 of S.C.-1996-c.-23.txt | 15 | 509 | 69 | 89 / 1 / 51 / 0 |
| `er1` | the Regulations' title and interpretation, and Part I (benefits), first part: hours of insurable employment, adjustment of self-employed earnings, interruption of earnings, undeclared earnings and rates of unemployment (to line 339) | 1-339 of SOR-96-332.txt | 20 | 958 | 63 | 83 / 35 / 23 / 9 |
| `er2` | Regulations Part I (benefits), second part: information relating to employment history, record of employment, allocation of hours and earnings, week of benefits, election, claims, payments in advance, the full working week, teachers and the family supplement (lines 340 to 539) | 340-539 of SOR-96-332.txt | 15 | 660 | 61 | 106 / 29 / 19 / 2 |
| `er3` | Regulations Part I (benefits), third part: determination and allocation of earnings, supplemental unemployment benefit plans, the waiting period, sickness, pregnancy, medical certificates, and the division of benefits (lines 540 to 992) | 540-992 of SOR-96-332.txt | 27 | 987 | 91 | 181 / 18 / 25 / 15 |
| `er4` | Regulations Part II (National Employment Service), Part III (reduction of premium for employers with wage-loss plans) and Part III.1 (reduction of premiums for employees covered by a provincial plan) | 993-1393 of SOR-96-332.txt | 25 | 758 | 45 | 97 / 29 / 54 / 3 |
| `er5` | Regulations Part IV (pilot projects) and Part V (administrative provisions) | 1394-1708 of SOR-96-332.txt | 26 | 777 | 115 | 111 / 27 / 29 / 3 |
| `er6` | Regulations Part VI (alternate access to special benefits), Part VII (transitional provisions and coming into force), the Schedules, the Related Provisions and the Amendments Not in Force | 1709-2537 of SOR-96-332.txt | 16 | 3618 | 66 | 142 / 16 / 40 / 7 |
| **whole** | | | **295** | **14928** | **1149** | **1623 / 325 / 470 / 106** |

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
Its last line: `TOTAL (295 modules) 0 14928 0 0 | 0 14928 0 0`; exit status 0.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem in either file.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 182 (99 against the Act, 83 against the Regulations).
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
- 15 top-level names are defined in more than one module: 10 in seat modules (`Am I disentitled from receiving benefits`; `Are benefits payable to me because of my pregnancy`; `Have I accumulated a violation`; `Is my cancelled benefit period treated as never having begun`; `Is our division of the weeks of parental benefits within the limits`; `May benefits be paid to me for this week`; `Must I have a Social Insurance Number`; `What class is my violation`; `What is the value of my violation`; `Will a benefit period be established for me`) and 5 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
- Some agents kept files of their own outside their deposit (scripts, templates, probes or check outputs), and none of them is in this repository: `ei1` (inputs/work); `ei2` (inputs/_work); `ei3` (inputs/ei3-expand.py; inputs/ei3-notes-add.py; ei3probe in the run's scratchpad; final-check.txt in the run's scratchpad); `ei4` (ei4-check.out in the run's scratchpad; ei4-expand.py in the run's scratchpad; ei4-seat-table.md in the run's scratchpad; expand.py in the run's scratchpad; run1.sh in the run's scratchpad); `ei5` (ei5-work in the run's scratchpad); `ei7` (inputs/gen); `er1` (er1-work in the run's scratchpad); `er2` (er2-probes in the run's scratchpad); `er3` (checksh-er3-final.out in the run's scratchpad); `er5` (work in the run's scratchpad); `er6` (inputs/er6-gen).
  The list comes from the agents' sandboxes and from the paths their tool calls name; a path is a mention, not proof that anything was read or written there.
  Where an agent's `NOTES-<agent>.md` or `PROGRESS-<agent>.md` mentions such a file, the path is the run's own and does not exist here.
