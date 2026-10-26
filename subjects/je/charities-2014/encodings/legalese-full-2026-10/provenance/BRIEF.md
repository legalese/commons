# Encoding brief: the Charities (Jersey) Law 2014, the WHOLE Law, in L4

This is the common brief for a fleet. Every agent in the fleet reads it. Your own assignment is a separate short message that names your role (SURVEYOR, ENCODER for a group, INTEGRATOR or TEST AUTHOR) and your group.
Read this brief fully before opening any source.

## The subject

The **Charities (Jersey) Law 2014** (L.41/2014), the official consolidated version on jerseylaw.je, "Showing the law from 2 October 2026 to Current": 43 Articles in 9 Parts, Schedule 1 (Jersey Charity Commissioner), Schedule 2 (Charity Tribunal), and the endnotes (legislation history, renumbering, amendment references).
It establishes a Jersey Charity Commissioner and a register of charities, sets the charity test, imposes duties on governors of registered charities, regulates use of the words "charity" and "charitable", gives the Commissioner powers to demand information, and creates a Charity Tribunal for appeals.
The Law has been amended and was commenced in stages; the text has nine point-in-time versions. Both facts matter (see "Vintages and commencement").

## Where you work

`FLEET_DIR` is `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full`. It holds:

| name | path | yours to |
| --- | --- | --- |
| `INPUTS_DIR` | `FLEET_DIR/inputs` | read |
| `PHASE1` | `FLEET_DIR/phase1` | read (the SURVEYOR writes `PLAN.md` and `coverage.tsv` here) |
| `DEPOSIT` | `FLEET_DIR/deposit` | write only the files your assignment names; read the modules of earlier stages that your assignment names |
| `WORK` | `FLEET_DIR/work/<your role>/` | write: all scratch files, probes and scripts go here, never anywhere else |
| `SKILLS` | `FLEET_DIR/skills` | read: a clean copy of the two skills (see "Skills") |

You may read `INPUTS_DIR`, `PHASE1`, the DEPOSIT files your assignment names, `SKILLS`, and the l4-ide language documentation under `/Users/mengwong/src/legalese/l4-ide/doc/reference/` and `/Users/mengwong/src/legalese/l4-ide/doc/concepts/`. Nothing else.
In particular do NOT read `doc/courses/`, `doc/tutorials/`, `jl4/examples`, `paper/`, or the original `skills/` directory of l4-ide: they carry material drawn from other encodings of this Law.
Do not list or read the parent of `FLEET_DIR`: it holds material from other work that you must not see.
`L4_BIN` is `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4` (sha256 `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475`; the prerelease l4 unstable-20261026-6325439 (darwin-arm64, SHA256SUMS-verified), installed 2026-10-26; an ancestor of origin/unstable 65adfc2de with no jl4-core change in between); use exactly this path.
There is no token budget and no time limit on this task: be thorough, and spend what accuracy needs.
Other agents share this machine: run `l4` under `nice -n 15`, and never run more than two `l4` processes at once.
**Stop only processes you started, by PID (`kill <pid>`), never by pattern.** `pkill -f` and `killall` match other people's processes: other Claude sessions on this machine run `l4` and builds at the same time. Record the PID when you start a background process (`cmd & echo $!`) and kill that.
Do not write to `/tmp`: scratch goes in your WORK directory.

## Skills

Read, in `SKILLS`: `encoding-a-subject/SKILL.md` (steps 1 to 7, 9, 11) and `writing-l4-rules/SKILL.md`, then `writing-l4-rules/references/drafting-patterns.md` and all of `writing-l4-rules/references/source-patterns/` (especially 04, 05, 08 and 11).
These are copies in which some examples were replaced by invented ones; read them as they stand. Do not look for the originals.

## Scope, pinned

- **Every Article 1 to 43, Schedule 1 and Schedule 2, and the endnotes.** Nothing is left `deferred`; a provision that cannot be made executable is `inert` with a reason of real length, or an encoded named `REFUSE`.
- **Depth.** Encode every duty, power, prohibition and offence as a typed regulative rule (who acts, what is done, with its preconditions); encode every number, term, time limit, penalty and precondition the text gives as a computable rule with tests; encode each definition that decides an outcome (for example which kinds of body are an "entity", who is a "governor", what is "misconduct") as typed nouns and rules. Provisions that only describe the composition or housekeeping of a body, or restate another statute, may be `inert`. (ASSUMED, NOT RULED: this is the depth the owner has not yet fixed.)
- **Out of scope:** the text of other enactments the Law refers to (the Trusts (Jersey) Law 1984, the Companies (Jersey) Law 1991, the Foundations (Jersey) Law 2009, the Non-Profit Organizations (Jersey) Law 2008, the Loi (1862), the Revenue Administration (Jersey) Law 2019, the Financial Services laws, the Scottish and UK charity statutes named in Article 28, and so on). Treat what they decide as an INPUT, and say so. Articles 41 and 42 are NOT amendments: they are enabling powers ("The States may by Regulations amend ...") to make Regulations amending other enactments. Encode them like every other power (a `MAY` rule; the content of the Regulations is an input); the other enactments themselves are out of scope.
- **Orders and Regulations the Law empowers** ("prescribed", "specified", "by Order", "by Regulations"): the power is encoded (below); the CONTENT of an Order is an input. Orders and Regulations HAVE been made under the Law (a web search on 2026-10-14 found, for example, the Charities (Core Financial Information) (Jersey) Regulations 2018 R&O.19/2018, the Charities (Additional Information) (Jersey) Order 2018 R&O.59/2018 and the Charities (Restricted Section of Register) (Jersey) Order 2018 R&O.60/2018, and there may be more; the list is not exhaustive). They are separate instruments, they are NOT among the inputs and they are NOT encoded: this row encodes the Law. Treat what they decide as an input, say where the Law defers to one (for example "solicit" and "donation" to Orders under Article 9(3)(b)), and do not guess their content.

## Sources

All inputs are under `INPUTS_DIR`. Read them there and nowhere else.
Quote mechanically: use `srcrefs.py quote` (below) to print a source line, and paste it; never retype statutory text from memory.

| what | file |
| --- | --- |
| the Law (the text to encode; one line per paragraph, indented by level; `src:N` means line N of this file) | `charities-jersey-law-2014-2026-10-02.txt` |
| the same consolidated text as the official PDF's text layer (46 pages, layout mode; a cross-check on numbers, punctuation and structure) | `charities-jersey-law-2014-official-pdf-text-layer.txt` |
| the amending instruments, text layers | `amending/` : R&O.102/2026, R&O.56/2025, R&O.17/2018 (appointed day), R&O.10/2024, R&O.28/2023, R&O.29/2021 (Sch. 2 para 1(e): the Charities Law "Minister" definition), R&O.40/2019, R&O.136/2019 (appointed day of the Revenue Administration Law), L.13/2019, L.1/2017 |
| licence of the source | `SOURCE-LICENSE.md` |
| the pattern for an ambiguity fork | `pattern-r4.l4` |
| tooling from a finished row of another subject (an example of `check.sh`, a trace checker and `srcrefs.py`) | `templates/` |

Where the consolidated text and the PDF text layer differ, say so in a fork; the amending instrument governs over both for what it amended.
`srcrefs.py` is `SKILLS/encoding-a-subject/assets/srcrefs.py`. `python3 -I srcrefs.py quote RAW N M` prints `-- src:N | text` lines; `python3 -I srcrefs.py check --refs RAW FILE...` checks every quotation and `@ref` locator of your modules against RAW. RAW is always `INPUTS_DIR/charities-jersey-law-2014-2026-10-02.txt`. Run `check` on every module you write and report the result.

## Time

There is no vendored time module for this Law: the Interpretation (Jersey) Law 1954 is not among the inputs.
The Law has few periods (the Commissioner retains records for 10 years; payments "in the 12 months preceding the application"; Article 26 speaks of "a period of one year"; a disqualification order "not exceeding 15 years"; the Commissioner's term "not more than 6 years"; "at least 2 weeks before appointing"; the annual return "for the most recent year"; and any periods in Schedules 1 and 2). This list is from a quick read, not a survey: find every one.
For EVERY period you meet, register a fork on the counting convention (is the day of the event inside the period; how a month or a year is added at the end of a month; backward periods "preceding"), name the kind of period, take a reading, and make the other reading a callable alternative with a test. Use the `daydate` library for date arithmetic and read its documentation under `doc/reference/` first; do not hand-roll month arithmetic.
Days of rest and holidays are not mentioned by the Law: do not model them.

## Vintages and commencement

Two temporal facts are part of the subject, not decoration.
1. **Staged commencement.** Per the endnotes ("Table of Legislation History") and R&O.17/2018: Parts 1 to 3, Articles 32, 38, 39, 40, 42, 43 and 44 (as then numbered) and the Schedules in force 21 November 2014; Parts 4, 5, 7, 8 (other than Article 32) and Article 37 in force 1 May 2018; "remainder" in force 1 January 2019. The Law has been renumbered: by the endnotes' "Table of Renumbered Provisions" the original Article 41 is "spent, omitted", the original 42, 43 and 44(1) are now Articles 41, 42 and 43, and the original 44(2) and 44(3) are spent. So the 2014 list means the present Articles 32, 38 to 43 (the original Article 44 whole, including the spent 44(2) and 44(3); R&O.17/2018 Article 2 says that Article 44(2) itself brought the first stage into force); the 2019 remainder is Part 6 and the original Article 41 (spent, omitted; its content is not in the sources: say so). Whether a Part or Article is in force on a given day is a computable rule of the day.
2. **Amendment history.** The text read today is the vintage "from 2 October 2026". Earlier vintages differ at: the definition of "Minister" (Art. 1; amended by R&O.40/2019, R&O.29/2021, R&O.28/2023, R&O.10/2024, R&O.102/2026), the definition of "Comptroller" (Art. 1; L.13/2019), the insertion of paragraph (ba) in Art. 2(1) (R&O.56/2025, from 16 October 2025, made under Art. 2(2)), and two "subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017" additions in Schedule 1 (L.1/2017). The nine point-in-time versions are 1 Jan 2019, 31 May 2019, 16 Dec 2019, 1 Jan 2020, 2 Mar 2021, 12 Apr 2023, 27 Feb 2024, 16 Oct 2025 and 2 Oct 2026.
**Vintages are inputs, never merged.** A function takes the day (or the vintage) as an input; a vintage that does not decide a fact answers silence (`MAYBE`/`REFUSE`), never a value borrowed from another vintage. Anything the instruments in `amending/` do not show, you do not know: say so.

## Deliverables (the fleet writes one row)

The row is `legalese-full-2026-10`. Its directory (the deposit) holds:

- `domain.l4`: the shared nouns, written once by the SURVEYOR; encoders IMPORT it and never edit it. A noun an encoder needs that is missing goes in their fragment as a "nouns request" for the INTEGRATOR.
- One group of ASCII-named modules per group (prefix given in your assignment), importing only `prelude`, `daydate`, `domain` and modules of your OWN group. **No module starts with `@lang en`**: English is the default and the line is not written.
- Tests, in modules of their own: expected values come from the SOURCE, never from your code.
- `FRAGMENT-<group>.md` from each encoder: coverage rows, forks, answer table, "nouns requests", open questions (see below). The INTEGRATOR merges them into `NOTES.md`.
- `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`, `NOTES.md` (INTEGRATOR). `encoding.json` and `SOURCE-LICENSE.md` follow `SKILLS/encoding-a-subject/references/canon-deposit.md` (status `draft`; `not_reviewed` saying no domain expert has read it against the Law). Start `check.sh` from `templates/check.sh` and the skill's `assets/check.sh`.

## Forks: the R4 shape

Every ambiguity you meet becomes a fork, and a fork is encoded in the R4 shape (see `pattern-r4.l4`, which compiles):
- one fork point is one enumeration, with one constructor per reading;
- all the fork points of your group are fields of ONE record `Interpretation of <your scope>` (name it so that it is unique across the fleet), each field `TYPICALLY` the reading you take;
- every public decision of your group that depends on a fork takes that record as an ordinary `GIVEN` and delegates by `CONSIDER` to one private implementation per reading, so that each reading is a callable function with its own test;
- each fork has an entry in your `FRAGMENT-<group>.md` register with: an id, the provision, the readings and the text that licenses each, the reading taken and why, the field and constructors that carry it, and the discriminating case. Register entries map 1:1 to record fields.
A fork with no discriminating case is not yet a fork: either find the case or drop it.

## Dependencies between groups

Groups are encoded in parallel and the INTEGRATOR composes them, so a rule in one group must never hard-wire a fact that another group decides.
Where an Article needs a fact that is decided by a later or parallel group, take it as a `GIVEN` input and say so in a "nouns request" or in your FRAGMENT. The standard inputs are named in `PHASE1/PLAN.md` section (c).
A cross-reference to another Article is an `@ref` and a comment, and a call only into a module of your own group.

## Rules after the survey

`PHASE1/PLAN.md` is the SURVEYOR's proposal. The fleet lead's rulings, added after the survey, are in the section below; where PLAN and that section differ, that section governs. An encoder may still change a disposition or a reading by registering a fork.

The fleet lead's rulings (assumed, not ruled by the owner), made on 2026-10-14 after reading the survey:

1. **No cross-group imports.** Groups run in parallel, so a group module imports only `prelude`, `daydate`, `domain` and modules of its OWN group (acyclic). Every fact another group decides is a `GIVEN` input under the standard name in PLAN section (c); the INTEGRATOR writes composing modules that wire the groups together.
2. **The standard names and types of PLAN section (c) are binding**, with the backticks, so that the integrator can wire a consumer to its producer by name. The module names and rule names that PLAN section (b) proposes are your defaults; they are unique across the fleet, so keep them unless the text makes you change them (then say so in your FRAGMENT). A name you add must also be unique across the fleet: put the Article number or the distinguishing noun in it.
3. **`domain.l4` is read-only.** A noun you need that is missing goes in your FRAGMENT under "nouns requests", and your group defines a local stand-in in your own module until the INTEGRATOR moves it.
4. **Powers are encoded.** A power of the Minister, the Commissioner, the court, the Tribunal or the States (to make an Order or Regulations, to amend a list, to require, to deregister, to direct, to disqualify, to appoint) is a regulative `MAY` rule typed by who acts and what is done, with its procedural preconditions (a recommendation of the Commissioner, a notice, an opportunity to object) as computable conditions. The CONTENT of an Order or of Regulations is an input. This overrides the survey where it marks a power out of scope: **Articles 41 and 42 (and their paragraphs) are powers of the States to make Regulations, and become `encoded` in G7**; the enactments they would amend stay out of scope.
5. **Commencement and vintages (G7 owns them).** Follow PLAN section (c) IP2 to IP4. The table of commencement is in the ORIGINAL article numbers, with the renumbering map as data (PLAN T1, T2). The text of 27 February 2024 begins at 9.30 a.m. (R&O.10/2024): a function of a DATE alone REFUSES on that day and a function of an instant answers (PLAN fork F7.1 is the default). `inputs/amending/` now holds R&O.29/2021 and R&O.136/2019, which the survey did not have: the 2 March 2021 text of "Minister" is "Minister for External Relations and Financial Services" (R&O.29/2021 Sch. 2 para. 1(e)); G7 should check the survey's vintage table against the instruments and record any difference.
6. **Offences.** Encode the prohibition as a regulative rule and the penalty as data, in the penalty type that `domain.l4` declares. Where the Law states a term but no maximum fine ("and to a fine"), the fine is absent and you say so; never invent a figure.
7. **Forks.** PLAN section (g) lists the candidate forks of your group, each with a reading marked "(taken)". That is a proposal: take it or change it, and say why. Every fork you register has the id `F<group number>.<n>` (continuing the survey's numbering for new ones) and is carried in the R4 shape by a field of your group's `Interpretation` record. Every period gets a fork on its counting convention, as the brief says.
8. **Do not look for other people's findings.** The survey's traps (PLAN section (f)) are given to you. Findings of other agents (a blind reading of the Law, the other groups' work in progress, test authors' work) are not, and you must not look in `FLEET_DIR/work` outside your own directory.
9. **Size and context.** Your group is larger than a typical encoding. Work Article by Article: after each Article is encoded, tested and green, record its coverage rows and forks in your FRAGMENT before starting the next, so that a stop at any point leaves a consistent state. Print only counts from your check script (not whole diagnostics) unless you are debugging a failure. If you cannot finish in one context, stop at a clean boundary, say exactly what is left in your FRAGMENT and in your final report, and you will be resumed.
10. **Check script.** Copy the skill's `assets/check.sh` into your WORK directory and adapt it to run only your group's modules (`DEPOSIT/<prefix>*.l4`; the other groups are writing theirs at the same time). Report what it prints. The INTEGRATOR writes the real `check.sh`.
11. **Quotations** come from `srcrefs.py quote` of the Law's text file; run `srcrefs.py check --refs` on every module you write and report the result.
12. **Entry points.** Mark the headline decision functions of your group `@export`, with a sentence that says what question it answers and a `@desc` on every `GIVEN`; a function that depends on a fork takes the group's `Interpretation` record, so that a caller can choose the reading.

## Rules that matter

- **Follow the two skills.** Encode isomorphically: one source provision, one recognisable place in the L4, `@ref` citation on every rule, `§`/`§§` headings that follow the Law's own Parts and Articles.
- **Duties, powers and prohibitions are regulative rules** (PARTY/MUST/MAY/SHANT) typed by the ROLE that acts and by WHAT IS DONE; do not model them as a long enumeration of action constructors named after Articles, and do not model a discretion as a decision. A discretion ("in the opinion of the Commissioner", "if satisfied", "reasonable excuse", "reasonable time", "substantial") is an INPUT.
- **Offences.** Where the Law says that a person "commits an offence and is liable to imprisonment for a term of N and to a fine", encode the prohibition and carry the penalty as data. Where the text states no maximum fine, say so and do not invent one.
- **Where the source does not answer: `REFUSE "…"`** (or `MAYBE`/`NOTHING` where the source itself names an absent case). Never `FALSE`, `0` or a plausible default. Do not invent a three-valued type; the language has `MAYBE` and `REFUSE`.
- **Inputs are `GIVEN`**, threading a record where there are many facts. Use `BRANCH IF … OTHERWISE`, not chains of `ELSE IF`. Mark the headline decision functions `@export` with `@desc` where the language allows (a function-typed parameter cannot be exported). A reader of the exports is a caller who has not read your modules: give each `@export` a sentence that says what question it answers, and each `GIVEN` a `@desc`.
- **REPORT EVERY CONTRADICTION IN THE SOURCE.** Where two Articles give different answers to the same question, or a definition and its use disagree, or a cross-reference points at something that is not there, do not resolve it silently: encode the reading you take, register a fork naming BOTH provisions and the case that discriminates, and give the other reading a callable function and a test. Look for them deliberately, as a separate pass after you have encoded. Note the Table of Renumbered Provisions in the endnotes: the Law has been renumbered, and cross-references may point at the old numbers.
- **An assertion that fails is a finding.** Never edit an expected value to match what the code computed. Keep expectations that are meant to fail in their own file and count them.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails or refuses; failure is a `DiagnosticSeverity_Error` line and refusal a Warning. Report the numbers `check.sh` prints. No module may emit a warning.
- **Coverage is by provision.** Every Article AND every lettered or numbered paragraph that carries its own rule gets a row: its number as the source writes it, a disposition (`encoded`, `inert`, `refused`, `out-of-scope`), the module and rule that carries it. Nothing is `deferred` when you finish.
- **Do not git add, commit or push anything.** Write only under your assigned directory.
- **No other agent's work is yours to edit.** A module you did not write is read-only to you.

## Toolchain

The binary is `L4_BIN` (above, and repeated in your assignment). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it. `L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL`, `#ASSERT` and `#TRACE`. `l4` has no `--version` flag. Run the binary by its absolute path.
Concurrent `l4` runs on DIFFERENT files are safe.

## Independence (cleanroom)

Other encodings of this exact Law exist (more than one). You must not read, list, grep or otherwise inspect any of them: nothing under `/Users/mengwong/src/legalese/commons/`, `commonswt/`, `canon/`, `l4-ide/paper/`, `l4-ide/jl4/examples/`, nor any copy of those on any volume under `/Volumes/` other than your own working directory, nor `~/.claude/` other than what this brief names (no `memory/`, `projects/`, `tmp`).
Do not search any filesystem for `charit*`, `jersey*` or this Law's name. Your context may contain an index of someone's notes that mentions this subject; do not follow it.
If you open a forbidden file by accident, stop reading it and say so under `peeked`. An honest admission costs nothing; a silent peek destroys the comparison.

## Final report (your last message)

Return: (1) the files you wrote; (2) exactly what `check.sh` printed for your modules; (3) your coverage rows summarised by disposition; (4) forks, each in a line with the reading chosen; (5) every contradiction in the source you found, with the discriminating case; (6) any failing or refused assertion and what it means; (7) what the sources do not answer; (8) `peeked`: nothing, or what you opened by accident.
