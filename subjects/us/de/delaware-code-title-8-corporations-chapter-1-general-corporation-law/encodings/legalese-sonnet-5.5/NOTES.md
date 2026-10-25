# The Delaware General Corporation Law (8 Del. C. ch. 1): the encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the text. The text is a plain-text rendering, not the official text, and has not been checked against it. The tests' expected values were written by the encoders from the text, not by an independent author.

## What this folder is

It encodes the whole text of the Delaware General Corporation Law (8 Del. C. ch. 1) that is deposited in `../../registers/source-bundle/`.
The text was too long for one agent, so it was cut into 11 pieces along its own divisions (Subchapters and sections), and each piece is a set of whole line ranges of the source file.
A keel agent (`dg-g0`) ran first and wrote the shared vocabulary and the naming conventions, `dg-core*.l4`; the Law has no interpretation section, so the keel has no provisions of its own.
Then 11 piece agents ran in parallel, each over its own lines, each with a read-only copy of the keel's modules.
Every file name starts with the agent's prefix, so the folder is flat and a module imports another by its name.
Each agent's brief is kept verbatim as `BRIEF-<agent>.md`; the paths in it are the run's own and do not exist here.

## The pieces

| agent | covers | source lines | modules | assertions | seat questions | coverage rows: encoded / fork / inert / repealed |
| --- | --- | --- | --- | --- | --- | --- |
| `dg-g0` (keel) | no provisions of its own: the Law has no interpretation section (its definitions sit inside the sections that need them), so the keel writes the shared vocabulary and the naming conventions only | none | 2 | 87 | 0 | 0 / 0 / 1 / 0 |
| `dg1` | the title lines and Subchapter I (formation: incorporators, certificate of incorporation, bylaws, emergency bylaws, forum selection, proxy access and expense reimbursement, document form), §§ 101-116 | 1-239 of de-code-t8-ch1-2026-10-01.txt | 23 | 1332 | 147 | 60 / 33 / 37 / 1 |
| `dg2` | Subchapter II (powers), Subchapter III (registered office and registered agent) and Subchapter IV (directors and officers), §§ 121-147 | 240-464 of de-code-t8-ch1-2026-10-01.txt | 26 | 1471 | 172 | 63 / 45 / 45 / 0 |
| `dg3` | Subchapter V (stock and dividends), §§ 151-174, and the start of Subchapter VI (stock transfers), §§ 201-203 (transfer restrictions; business combinations with interested stockholders) | 465-670 of de-code-t8-ch1-2026-10-01.txt | 15 | 1432 | 156 | 101 / 24 / 56 / 0 |
| `dg4` | Subchapter VI §§ 204-205 (ratification of defective corporate acts; court proceedings on their validity) and Subchapter VII §§ 211-220 (meetings, voting, quorum, voting agreements, stockholder lists, books and records inspection) | 671-889 of de-code-t8-ch1-2026-10-01.txt | 25 | 1171 | 164 | 57 / 25 / 25 / 0 |
| `dg5` | Subchapter VII §§ 221-233 (notice, vacancies, elections, consents, inspectors, delivery of notice) and Subchapter VIII (amendment of certificate of incorporation; changes in capital and capital stock), §§ 241-246 | 890-1057 of de-code-t8-ch1-2026-10-01.txt | 18 | 832 | 118 | 75 / 22 / 39 / 3 |
| `dg6` | Subchapter IX §§ 251-254 (merger or consolidation of domestic corporations; of domestic and foreign corporations; parent and subsidiary; of domestic corporations and partnerships) | 1058-1171 of de-code-t8-ch1-2026-10-01.txt | 14 | 824 | 109 | 35 / 21 / 10 / 2 |
| `dg7` | Subchapter IX §§ 255-262 (merger of nonstock corporations; stock and nonstock corporations; effects of merger; remedies; appraisal rights) | 1172-1276 of de-code-t8-ch1-2026-10-01.txt | 13 | 998 | 121 | 44 / 14 / 17 / 1 |
| `dg8` | Subchapter IX §§ 263-268 (merger with other entities, conversion of other entities to a domestic corporation and of a domestic corporation to other entities, merger of parent entity and subsidiary corporation) | 1277-1385 of de-code-t8-ch1-2026-10-01.txt | 15 | 947 | 121 | 83 / 27 / 21 / 1 |
| `dg9` | Subchapter X (sale of assets, dissolution and winding up), Subchapter XI (insolvency; receivers and trustees) and Subchapter XII (renewal, revival, extension and restoration of certificate of incorporation) | 1386-1631 of de-code-t8-ch1-2026-10-01.txt | 12 | 1150 | 145 | 84 / 18 / 68 / 0 |
| `dg10` | Subchapter XIII (suits against corporations, directors, officers or stockholders), Subchapter XIV (close corporations; special provisions), Subchapter XV (public benefit corporations) and Subchapter XVI (foreign corporations) | 1632-1934 of de-code-t8-ch1-2026-10-01.txt | 13 | 1514 | 165 | 96 / 44 / 106 / 0 |
| `dg11` | Subchapter XVII (domestication and transfer) and Subchapter XVIII (miscellaneous provisions, including the amounts payable to the Secretary of State), §§ 388-398 | 1935-2112 of de-code-t8-ch1-2026-10-01.txt | 14 | 951 | 154 | 69 / 35 / 25 / 1 |
| **whole** | | | **190** | **12709** | **1572** | **767 / 308 / 450 / 9** |

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
Its last line: `TOTAL (190 modules) 1 12709 1 0 | 1 12709 1 0`; exit status 0.
1 module(s) are meant to fail and are listed in `check.sh`'s `expected_failed` with their counts (`dg1-cases-seat-first-reading.l4` 1), so the `TOTAL` line counts 1 error(s) and 1 failed assertion(s) that are the expected ones; `encoding.json` names them under `expected_red`.
`check.sh` in this folder is the skill's own with exactly those `expected_failed` lines added.
`srcrefs.py check --refs`, which verifies every quoted `-- src:N |` line and every `@ref` locator against the text in `../../registers/source-bundle/`, found no problem.
`srcrefs.py check --strict` also compares the width of each quoted run with its locators and reports findings: 121.
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
- 8 top-level names are defined in more than one module: 8 in test modules, as fixtures that share a name.
  `check.sh` checks each module on its own, so it does not see this.
  A module that imports two of them and uses the name gets `There are multiple definitions for the identifier` (measured on a two-module control with the stable `l4`); a module that only imports them does not.
  None is in a core module or a layer-1 module.
- The keel's `NOTES-dg-g0.md` (instruction 15 and ruling F14) tells the pieces to mark the sentence defining "facts" `inert`.
  That reason is not on the brief's closed list of reasons for `inert`, and the lead overruled it: the sentence ("includes, but is not limited to, the occurrence of any event, including a determination or action by any person or body …") is encoded in all 18 places, sections 102(d), 151, 152, 157, 251 to 257, 263 to 267, 388 and 390, as an open list: an event, or a determination or action by any person or body, is a fact, and for anything else the text does not say, so the rule answers `NOTHING`.
  Five pieces record that reading as a fork (`dg1` F18, `dg6` F26, `dg7` F-facts-1, `dg8` F26, `dg11` F-388-4) and `dg3` as a finding; each piece wrote its own rules, so there are several of slightly different shape and no shared type.
- `dg1` keeps one assertion that is meant to fail (`dg1-cases-seat-first-reading.l4`, its first reading of section 110(i); fork F32); `check.sh` in this folder lists it in `expected_failed`.
- Some agents kept files of their own outside their deposit (scripts, templates, probes or check outputs), and none of them is in this repository: `dg1` (inputs/work); `dg2` (dg2-final-check.txt in the run's scratchpad); `dg3` (dg3work in the run's scratchpad); `dg4` (dg4tools in the run's scratchpad); `dg5` (inputs/tools; inputs/work; dg5-out.txt in the run's scratchpad); `dg6` (dg6-work in the run's scratchpad); `dg7` (tools/ beside its deposit); `dg8` (dg8-tools in the run's scratchpad); `dg10` (inputs/tools).
  The list comes from the agents' sandboxes and from the paths their tool calls name; a path is a mention, not proof that anything was read or written there.
  Where an agent's `NOTES-<agent>.md` or `PROGRESS-<agent>.md` mentions such a file, the path is the run's own and does not exist here.
