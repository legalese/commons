# The Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976): the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is a plain-text rendering, not the official text, and has not been checked against it. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976) that is deposited in `../../registers/source-bundle/`.
The text was too long for one agent, so it was cut into 7 pieces along its own divisions (Parts, Chapters, Schedules), and each piece is a set of whole line ranges of the source.
A keel agent (`br-g0`) ran first and wrote the shared vocabulary, `br-core*.l4`.
Then 7 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `br-g0` (keel) | no provisions of its own: the Law has no interpretation section, so the keel writes the shared vocabulary and the Portuguese naming conventions only | none | 3 | 68 | 0 | 0 / 0 / 0 / 0 |
| `br1` | Capítulos I a IV (características e natureza da companhia ou sociedade anônima, capital social, ações, partes beneficiárias) | 1-371 of lei-6404-1976.pt.txt | 20 | 1236 | 165 | 168 / 0 / 21 / 2 |
| `br2` | Capítulos V a IX (debêntures, bônus de subscrição, constituição da companhia, formalidades complementares da constituição, livros sociais) | 372-807 of lei-6404-1976.pt.txt | 20 | 845 | 48 | 126 / 23 / 3 / 3 |
| `br3` | Capítulos X e XI (acionistas, assembléia-geral) | 808-1232 of lei-6404-1976.pt.txt | 27 | 1361 | 191 | 129 / 31 / 1 / 3 |
| `br4` | Capítulos XII a XIV (conselho de administração e diretoria, conselho fiscal, modificação do capital social) | 1233-1554 of lei-6404-1976.pt.txt | 18 | 1443 | 215 | 161 / 19 / 0 / 4 |
| `br5` | Capítulos XV e XVI (exercício social e demonstrações financeiras; lucro, reservas e dividendos) | 1555-1957 of lei-6404-1976.pt.txt | 17 | 722 | 76 | 59 / 41 / 1 / 9 |
| `br6` | Capítulos XVII a XX (dissolução, liquidação e extinção; transformação, incorporação, fusão e cisão; sociedades de economia mista; sociedades coligadas, controladoras e controladas) | 1958-2325 of lei-6404-1976.pt.txt | 23 | 1171 | 111 | 122 / 27 / 7 / 5 |
| `br7` | Capítulos XXI a XXVI (grupo de sociedades, consórcio, sociedades em comandita por ações, prazos de prescrição, disposições gerais, disposições transitórias) | 2326-2593 of lei-6404-1976.pt.txt | 14 | 1089 | 121 | 113 / 2 / 16 / 4 |
| **whole** | | | **142** | **7935** | **927** | **878 / 143 / 49 / 30** |

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
Its last line: `TOTAL (142 modules) 0 7935 0 0 | 0 7935 0 0`; exit status 0.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 41.
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
- 5 top-level names are defined in more than one module: 1 in seat modules (`O conselho fiscal pode convocar a assembleia-geral`) and 4 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
- Identifiers, `@export` question text and `@desc` are in Portuguese; `NOTES-*.md`, `PROGRESS-*.md` and comments are in English; quoted source lines are in the source's Portuguese.
