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

## Procedure layer (DEONTIC), added beside the Boolean encoding

This section lists the modules that were added to lay the Act's procedures out as regulative rules (`DEONTIC`, with traces).
They are additive: no existing module was edited, and no existing assertion count moved.
Each unit is a module, a test module and a notes file (`notes/procedure-<unit>.md`) that says what it encodes, its timeline unit and counting rule, its forks and what it leaves out.
Every `#TRACE` in the test modules has a `-- EXPECT` line decided from the text before the trace was run, and each was checked against it on two builds: the unstable prerelease `unstable-20261125-a50cbd0` and the stable line, main build 112.
`check.sh` counts assertions and never reads a `#TRACE` outcome, so it cannot see the differences below; they were found by running each trace on both builds.
The two builds differ on traces in four known ways: a `MAY` that lapses, a `LEST` continuation's clock, two parties in breach at once, and the first event after a wait device lapses.
Where a unit's traces read differently on main, its test module ends with a `READS-DIFFERENTLY-ON-MAIN` block listing them, and the count is in the table.
The traces are the ones to read on unstable; main 112 gives a different class for the listed ones.
Convention for every unit (assumed, not ruled): BREACH is kept only for a duty or a prohibition that the text lays on a named party; a power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end FULFILLED, with the reason in a comment beside the branch and in the unit's notes under `### Closed routes (not breaches)`.
The counting fork F1 that three units borrow is in `NOTES-ic4.md`, scoped there to the Part 8 sections, and the notes of the derivative-claim and merger units cite it there.

| unit (module) | provisions | traces | read differently on main 112 |
| --- | --- | --- | --- |
| `ic-proc-register-access` | ss 124-129 | 26 | 0 |
| `ic-proc-derivative-claim` | ss 194-198 | 68 | 6 |
| `ic-proc-forced-sale` | ss 336-341 | 44 | 7 |
| `ic-proc-merger` | ss 316-327 | 43 | 0 |
| `ic-proc-own-shares` | ss 301-311; s 312 not encoded (own-share purchase is a distribution by the s 1 definition, src:209) | 44 | 0 |
| `ic-proc-foreign-company` | ss 346-349א | 50 | 0 |
| `ic-proc-interested-transactions` | ss 269-272, 278, 280, 283 | 46 | 0 |

### Observations on the existing modules (nothing was changed)

- This encoding had no `DEONTIC` anywhere before this layer.
- `ic6-foreign-company.l4:74-81`, the Boolean for s 346(ג), tests changes in the documents, directors and the particulars of the persons named in s 346(ב)(3) and (4) only.
  Section 346(ד) (src:2967) also makes the foreign company notify the Registrar of changes in the further documents the Minister may require; that limb is not encoded in the Boolean (its comment says the power is taken into s 346(ב)).
  It matters only if the Minister has set further documents, and none are in the bundle.
  `ic-proc-foreign-company` has its own helper for it.
- Reduction of issued capital has no route in the Law (no hits for הפחתת הון, הקטנת הון or הפחתה); ss 286-287 only increase registered capital and cancel unallotted registered capital.

### Changes after the independent review of the procedure layer

Each line below is a change that altered an answer; the unit's notes say more under `### Changes after the independent review`.
- `ic-proc-foreign-company`, s 348: the annual report now has a clock ("אחת לשנה", src:2974), assumed from the registration day and then from each report, and a missed report is a BREACH BY the company; four traces changed class and four were added (the 5,000-day trace no longer ends open).
- `ic-proc-foreign-company`, ss 346(א) and 349: keeping the place of business unregistered is now a BREACH BY the company (and by a participating office-holder or agent) with the fine named in the reason, where it was a duty to pay the fine; seven traces changed class.
- `ic-proc-interested-transactions`, ss 270-272: the approvals rule no longer ends FULFILLED for routes it does not encode (272(ג) and (ג1), 273, 274, 275, the articles' route); it stays open on a permission named for the route (RESIDUAL), two traces changed class and two were added.
- `ic-proc-interested-transactions`, s 269(א): for a board meeting already past, no meeting clock applies and the without-delay input decides; one trace changed class (BREACH to FULFILLED) and one was added.
- `ic-proc-forced-sale`, s 341(א): the offeror's window opens when the two months end, so day 0 is that day and the traces were re-timed; no class changed. The 341(ג) reading, which opens the duty at the ruling when the court rules early, was not changed, because the clock cannot wait out the rest of the month after an early ruling.
- `ic-proc-own-shares`, s 302(ב): the six months are measured back from the distribution date, so statements to 30 June are in time for a distribution on 31 December; and s 303: the court's decision follows the notice to creditors; three assertions were added and no trace changed class.
- `ic-proc-register-access`, s 126(א): the entitlement to inspect is derived from section 129 for the two registers of 124(7); one trace was added.
- `ic-proc-derivative-claim` and `ic-proc-merger`: no answer changed; the counting forks F1 and F6 are cited from `NOTES-ic4.md`, and the derivative-claim unit has a new fork that delivery is receipt.
- `encoding.json`: the check table is the `check.sh` output of the stable build 112 taken before these changes, with the two rows whose assertion counts rose (own-shares tests 15 to 18, foreign-company tests 18 to 21) and the total patched by hand, not re-run: 179 modules and 10,328 assertions satisfied, where it said 165 and 10,271.
