# The Social Security Benefits Plans Law (Lei nº 8.213/1991, Planos de Benefícios da Previdência Social): the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is a plain-text rendering, not the official text, and has not been checked against it. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Social Security Benefits Plans Law (Lei nº 8.213/1991, Planos de Benefícios da Previdência Social) that is deposited in `../../registers/source-bundle/`.
The text was too long for one agent, so it was cut into 4 pieces along its own divisions (Títulos, Capítulos, Seções, Subseções), and each piece is a set of whole line ranges of the source file.
A keel agent (`pb-g0`) ran first and wrote the shared vocabulary and the Portuguese naming conventions, `pb-core*.l4`; the Law has no interpretation section, so the keel has no provisions of its own.
Then 4 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `pb-g0` (keel) | no provisions of its own: the Law has no interpretation section, so the keel writes the shared vocabulary and the Portuguese naming conventions only | none | 2 | 47 | 0 | 0 / 0 / 0 / 0 |
| `pb1` | the title lines before Título I, Título I, Título II, and Título III Capítulo I (Seções I to III) and Capítulo II Seções I and II | 1-454 of lei-8213-1991.pt.txt | 23 | 762 | 81 | 117 / 31 / 28 / 16 |
| `pb2` | Título III Capítulo II Seção III (Subseções I and II), Seção IV and Seção V Subseções I to IV | 455-780 of lei-8213-1991.pt.txt | 16 | 766 | 98 | 94 / 24 / 12 / 13 |
| `pb3` | Título III Capítulo II Seção V Subseções V to IX, and Título IV to the end of the Law | 781-1105, 1540-1766 of lei-8213-1991.pt.txt | 16 | 1164 | 152 | 157 / 1 / 7 / 23 |
| `pb4` | Título III Capítulo II Seção V Subseções X to XII, and Seções VI, VII and VIII | 1106-1539 of lei-8213-1991.pt.txt | 17 | 805 | 100 | 96 / 22 / 10 / 31 |
| **whole** | | | **74** | **3544** | **431** | **464 / 78 / 57 / 83** |

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
Its last line: `TOTAL (74 modules) 0 3544 0 0 | 0 3544 0 0`; exit status 0.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 70.
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
- 3 top-level names are defined in more than one module: 3 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
- Identifiers, `@export` question text and `@desc` are in Portuguese; `NOTES-*.md`, `PROGRESS-*.md` and comments are in English; quoted source lines are in the source's Portuguese.
- Some agents kept files of their own outside their deposit (scripts, templates, probes or check outputs), and none of them is in this repository: `pb2` (inputs/_work); `pb3` (a file one level above the run's scratchpad; pb3-fix in the run's scratchpad; pb3-probe in the run's scratchpad; pb3-src in the run's scratchpad).
  The list comes from the agents' sandboxes and from the paths their tool calls name; a path is a mention, not proof that anything was read or written there.
  Where an agent's `NOTES-<agent>.md` or `PROGRESS-<agent>.md` mentions such a file, the path is the run's own and does not exist here.
