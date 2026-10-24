# The Canada Pension Plan Act and the Canada Pension Plan Regulations: the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is a plain-text rendering, not the official text, and has not been checked against it. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Canada Pension Plan Act and the Canada Pension Plan Regulations that is deposited in `../../registers/source-bundle/`: the Act and the Regulations, as two text files.
The texts were too long for one agent, so each was cut into pieces along its own divisions (Parts, Divisions, Schedules), 8 pieces in all, and each piece is a set of whole line ranges of one source file.
A keel agent (`cp-g0`) ran first and wrote the shared vocabulary, `cpp-core*.l4`, and the interpretation provisions; the Act and the Regulations share it.
Then 8 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `cp-g0` (keel) | the Act's title, section 1 and the interpretation provisions (section 2 and the definitions that follow it), with the vocabulary shared by the Act and the Regulations | 1-121 of R.S.C.-1985-c.-C-8.txt | 9 | 227 | 0 | 69 / 2 / 13 / 5 |
| `cp1` | Part I (contributions), Division A (contributions payable) and Division B (calculation of contributions) | 122-586 of R.S.C.-1985-c.-C-8.txt | 21 | 967 | 73 | 104 / 26 / 21 / 2 |
| `cp2` | Part I (contributions), Division C (collection of contributions), Division D (collection in respect of self-employed earnings) and Division E (general) | 587-920 of R.S.C.-1985-c.-C-8.txt | 18 | 1095 | 177 | 86 / 22 / 19 / 2 |
| `cp3` | Part II (pensions and supplementary benefits): the Part's opening provisions, Division A (benefits payable) and Division B (calculation of benefits) as far as the division of first additional unadjusted pensionable earnings | 921-1569 of R.S.C.-1985-c.-C-8.txt | 25 | 980 | 86 | 99 / 33 / 14 / 4 |
| `cp4` | Part II, the rest of Division B (division of second additional unadjusted pensionable earnings, from the heading at line 1570) and Division C (payment of benefits: general provisions) | 1570-2251 of R.S.C.-1985-c.-C-8.txt | 28 | 799 | 102 | 100 / 44 / 8 / 2 |
| `cp5` | Part II, Divisions D to G (payment of benefits: special rules, amount payable under the Canada Pension Plan, reconsiderations and appeals, general), and the Related Provisions and Amendments Not in Force at the end of the Act's file | 2252-2627, 3138-3329 of R.S.C.-1985-c.-C-8.txt | 23 | 734 | 91 | 82 / 8 / 67 / 9 |
| `cp6` | Part III (administration) | 2628-3137 of R.S.C.-1985-c.-C-8.txt | 24 | 886 | 57 | 127 / 0 / 21 / 26 |
| `cr1` | the Regulations' title and interpretation, Parts I to IV (collection and payment of contributions, information returns, employment included in or excepted from pensionable employment, prescribed interest and refunds), Part VIII (miscellaneous), Schedules I to IX and the Related Provisions | 1-416, 822-1163 of C.R.C.-c.-385.txt | 30 | 1145 | 113 | 162 / 29 / 50 / 14 |
| `cr2` | the Regulations' Part V (pensions and supplementary benefits) | 417-821 of C.R.C.-c.-385.txt | 37 | 923 | 130 | 120 / 28 / 36 / 17 |
| **whole** | | | **215** | **7756** | **829** | **949 / 192 / 249 / 81** |

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
Its last line: `TOTAL (215 modules) 0 7756 0 0 | 0 7756 0 0`; exit status 0.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem in either file.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 339 (274 against the Act, 65 against the Regulations).
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
- 20 top-level names are defined in more than one module: 20 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
- Some agents kept files of their own outside their deposit (scripts, templates, probes or check outputs), and none of them is in this repository: `cp-g0` (cpg0 in the run's scratchpad); `cp1` (cp1work in the run's scratchpad; probe-cp1 in the run's scratchpad); `cp2` (work/ beside its deposit); `cp3` (work-cp3 in the run's scratchpad); `cp4` (final-check.txt in the run's scratchpad; warn-scan.txt in the run's scratchpad); `cp5` (probe5 in the run's scratchpad; tools5 in the run's scratchpad); `cp6` (check.final2.out in the run's scratchpad; check.final3.out in the run's scratchpad; cp6work in the run's scratchpad; run.out in the run's scratchpad); `cr1` (scratch/ beside its deposit; work/ beside its deposit; final-check.exit in the run's scratchpad; final-check.txt in the run's scratchpad); `cr2` (inputs/work).
  The list comes from the agents' sandboxes and from the paths their tool calls name; a path is a mention, not proof that anything was read or written there.
  Where an agent's `NOTES-<agent>.md` or `PROGRESS-<agent>.md` mentions such a file, the path is the run's own and does not exist here.
