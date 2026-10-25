# Encoding brief: the Delaware General Corporation Law (8 Del. C. ch. 1), piece dg8 (L4, stable)

You are one of 12 agents producing a full L4 encoding of the Delaware General Corporation Law (8 Del. C. ch. 1) (8 Del. C. §§ 101-398) from the English-language text deposited in `INPUTS_DIR`.
The text is split into contiguous pieces; every line of it belongs to exactly one piece; the pieces are being encoded at the same time, each by one agent in its own folder.
Your piece is **dg8**: Subchapter IX §§ 263-268 (merger with other entities, conversion of other entities to a domestic corporation and of a domestic corporation to other entities, merger of parent entity and subsidiary corporation).
Your ranges are lines 1277-1385 of `de-code-t8-ch1-2026-10-01.txt` (8,955 words).
This brief is the whole specification. Read it fully before opening any source.

You are the ONLY encoder of your piece: no integrator, no independent test author, no subagents.
You do all of it in one context and you check your own work with the diagnostics.
A keel agent has already encoded the interpretation provisions (where the text has them) and written the shared vocabulary (see "The shared core").
After every piece is done, the lead merges the pieces into one folder for the whole text and checks it.

## The table of pieces

| piece | what it encodes | lines | words | first and last section label opening in it |
| --- | --- | --- | --- | --- |
| dg-g0 (keel) | no provisions of its own: the Law has no interpretation section (its definitions sit inside the sections that need them), so the keel writes the shared vocabulary and the naming conventions only | none | 0 | none |
| dg1 | the title lines and Subchapter I (formation: incorporators, certificate of incorporation, bylaws, emergency bylaws, forum selection, proxy access and expense reimbursement, document form), §§ 101-116 | 1-239 | 11,867 | 101 to 116 |
| dg2 | Subchapter II (powers), Subchapter III (registered office and registered agent) and Subchapter IV (directors and officers), §§ 121-147 | 240-464 | 14,053 | 121 to 147 |
| dg3 | Subchapter V (stock and dividends), §§ 151-174, and the start of Subchapter VI (stock transfers), §§ 201-203 (transfer restrictions; business combinations with interested stockholders) | 465-670 | 12,201 | 151 to 203 |
| dg4 | Subchapter VI §§ 204-205 (ratification of defective corporate acts; court proceedings on their validity) and Subchapter VII §§ 211-220 (meetings, voting, quorum, voting agreements, stockholder lists, books and records inspection) | 671-889 | 11,892 | 204 to 220 |
| dg5 | Subchapter VII §§ 221-233 (notice, vacancies, elections, consents, inspectors, delivery of notice) and Subchapter VIII (amendment of certificate of incorporation; changes in capital and capital stock), §§ 241-246 | 890-1057 | 9,766 | 221 to 246 |
| dg6 | Subchapter IX §§ 251-254 (merger or consolidation of domestic corporations; of domestic and foreign corporations; parent and subsidiary; of domestic corporations and partnerships) | 1058-1171 | 9,058 | 251 to 254 |
| dg7 | Subchapter IX §§ 255-262 (merger of nonstock corporations; stock and nonstock corporations; effects of merger; remedies; appraisal rights) | 1172-1276 | 10,608 | 255 to 262 |
| dg8 | Subchapter IX §§ 263-268 (merger with other entities, conversion of other entities to a domestic corporation and of a domestic corporation to other entities, merger of parent entity and subsidiary corporation) | 1277-1385 | 8,955 | 263 to 268 |
| dg9 | Subchapter X (sale of assets, dissolution and winding up), Subchapter XI (insolvency; receivers and trustees) and Subchapter XII (renewal, revival, extension and restoration of certificate of incorporation) | 1386-1631 | 13,069 | 271 to 314 |
| dg10 | Subchapter XIII (suits against corporations, directors, officers or stockholders), Subchapter XIV (close corporations; special provisions), Subchapter XV (public benefit corporations) and Subchapter XVI (foreign corporations) | 1632-1934 | 12,993 | 321 to 385 |
| dg11 | Subchapter XVII (domestication and transfer) and Subchapter XVIII (miscellaneous provisions, including the amounts payable to the Secretary of State), §§ 388-398 | 1935-2111 | 11,531 | 388 to 398 |

## What you are building: two layers

**Layer 1: the law, objectively.** Your whole range, as isomorphic and tested L4 modules that follow the text's own structure (one module per Part, Chapter or natural group; modules written by you start with `dg8-`).
Layer 1 is written from the text alone. It takes nobody's point of view: a reader holding the text beside a module checks it line by line, and every rule carries a source citation.

**Layer 2: one thin seat layer over it, for your range.** Commons requires every text to be asked about from the position of the individual to whom the law is applied (the "seat"), because the Legalese website turns such a layer into a question form.
Here the seat is: **a person who incorporates, directs or holds stock in a Delaware corporation under the General Corporation Law (an incorporator, a director or officer, a stockholder including a minority stockholder), asking what the Law lets them do, what it requires of them, what they may require of the corporation, and what can be done to them.**
The layer is the two files `dg8-seat.l4` and `dg8-cases-seat.l4`. It IMPORTs your layer-1 modules and the core and calls their rules; it never restates or copies a rule, and no layer-1 module changes to suit it.
Each question has `@export` and `@desc`, takes plain inputs (one per fact the person can state, each `@desc` worded as that person would be asked), and the questions are grouped under `§` headings in the text's natural order.
Ask a question for every provision of your range that gives the person a claim, privilege, power or immunity, puts a duty or liability on them, or decides something they would ask.
A provision that decides nothing the person could ask about gets no question, but it is still encoded in layer 1 or marked `inert` with a reason: the seat never decides what is left out.
Every top-level name you define (rules, types, constructors, questions) must be specific to what it decides, because after the merge the names of all pieces sit in one folder: write `` `must give notice of the meeting` ``, never `` `notice` `` or `` `is eligible` ``.
Read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md` before you write any L4. `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` is a finished seat layer for a different Act and shows the shape (it imports modules you cannot see; copy its shape, not its content).
Questions are phrased as the person asks them ("Must I ...?", "Am I entitled to ...?"), and the facts are ones that person could state. Provisions that address only an official are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person (what may be done to them, what they must be given, and by when). There is never a seat for an official.

**Rights and duties come in pairs (Hohfeld).** A question about what the person is owed cannot be answered apart from the other party's side of the same relation. Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability. Read the other way, a power the other party holds over the person is the person's liability.
So, in layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In layer 2, wherever the text gives the person a claim, privilege, power or immunity, take as plain inputs the facts about the other party on which the text makes it depend (whom the duty binds, what that party has done or failed to do, any condition on their side). Where the text also puts a duty or a liability on the person, add the paired question ("What do I owe ...?", "What can be done to me if ...?"). Where the other party is an official, their duties and liabilities appear as what the person is owed or exposed to, never as a seat of their own.
In `NOTES.md` add a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`.

## The whole range, nothing left out (ruled by Meng, 2026-10-22)

The whole text is encoded in one pass. A provision is never left out because it matters little to the seat.
The seat decides only which questions layer 2 asks; it never decides what layer 1 covers.
Meng's reason: leaving out provisions by seat "invites a misalignment down the road when we want to do the bits that we left out", and backfilling afterwards is worse than doing everything in one pass.

So the coverage table in `NOTES.md` has one row per provision in your ranges: one per section, and one per subsection or paragraph wherever the subsections differ in disposition or in the rule they state (a section whose subsections are encoded together as one rule may be one row listing them).
Each row has exactly these columns: `| provision | source lines | disposition | where | note |`.
`provision` is the section or regulation as the text numbers it, such as `s 122(1)` or `reg 36`; `source lines` is a locator such as `src:1204-1210`; `where` is the module and the rule that encode it.
The disposition is one of:
- `encoded`: it is in layer 1 (and in layer 2 where the person would ask about it). This includes provisions addressed to an official, encoded for what they decide for the person, as the Guide says.
- `inert`: left out, for a reason from this list and no other, written with real length and naming what the provision does: machinery (boards, commencement and regulation-making powers, as the Guide lists them), an amendment of another instrument, an amendment that the source itself shows as not in force, or a pure citation or title. (The last three reasons are not in the Guide's list; they are accepted because the text itself makes them inert.)
- `repealed or blank in this text`: say what the text shows (`[Repealed ...]`, a run of dots, `⟦STRUCK: ...⟧`).
- `fork`: the text does not settle the reading. The row points to an entry in the fork register; you encode the reading you took, or return an explicit not-covered value, and say which.
"Out of the seat's scope", "not relevant to the person", "official only" and "too long" are not reasons. A reviewer will count the headings in your ranges against your rows, and will read every `inert` row.
A provision that is defined by reference to a provision outside your ranges is encoded as far as your range lets you, with the rest taken as an input (see "Cross-references").

## The shared core

The keel agent has written the shared vocabulary and encoded the interpretation provisions (where the text has them). Its modules are the files `dg-core*.l4` in your `DEPOSIT/encodings/legalese-sonnet-5.5/` folder, already there, and its notes are `inputs/KEEL-NOTES.md`. **Read `inputs/KEEL-NOTES.md` first.**
They are read-only: do not edit them, and do not copy them; if you change one, your change is discarded at the merge.
`IMPORT` them from your modules (they sit in the same folder, which is the only place `IMPORT` looks) and use their types and rules; never define again a name they define.
The core's encoding of the interpretation provisions counts as done: where a provision of yours merely uses a defined term, call the core's rule for it by name.
If you need a shared type or term the core lacks, define a local one under a distinct, specific name, and list it in `NOTES.md` under `## Needs from the core` with the reason; the lead decides afterwards whether to promote it. Do not wait for an answer: nobody can reply while you work.

## Cross-references out of your range

Many provisions refer to provisions outside your ranges ("the amount determined under section 46", "a director", "a person described in regulation 8").
The other pieces are being written at the same time by agents you cannot see, so you cannot import their rules, and you must never write an `IMPORT` of another piece's module: it does not exist yet.
For a reference to a rule outside your ranges: take that rule's outcome as a plain input of the right type, named for the fact and not for the section, with a comment `-- out of range: section N (piece X)`, where piece X is read from the table of pieces; and list it in `NOTES.md` under `## Cross-references out of my ranges` as a table `| your provision | the provision it depends on | its piece | the input you made |`.
For a term the text defines in its interpretation provisions, use the core (it holds that section already encoded; see "The shared core").
A term defined elsewhere in the text, outside your ranges, is a cross-reference like any other.
Reach a provision outside your ranges by section number with `grep -n` on `inputs/SECTION-INDEX.txt` and then `sed -n 'A,Bp'` on the text file; never read the whole text file, and never read more of another piece's range than the reference needs.

## The subject and the sources

- **the Delaware General Corporation Law (8 Del. C. ch. 1)**, 8 Del. C. §§ 101-398.
- Source file(s) in `INPUTS_DIR`: `de-code-t8-ch1-2026-10-01.txt`. Each line number in this brief refers to lines of those files.
- `inputs/SOURCES.md` records where each came from, its version or currency date, its URL and its hashes. **Read it.**
- Each `.txt` is a plain-text rendering of the official source made by a converter script; it is not the official text and it is not marked up. Say so in `NOTES.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited.
- `inputs/SECTION-INDEX.txt` lists, by line number, where each section or regulation opens, with the heading it sits under; it was made by a script, so the text is authoritative.
- Encode only from these files. Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory.
This is Title 8, Chapter 1 of the Delaware Code, in eighteen subchapters, §§ 101-398. For each section the file holds a heading line (which can carry a bracketed note such as `[For application of this section, see 82 Del. Laws, c. 256, § 23]`), the text, and a `History:` line citing the 1953 Code and the Laws of Delaware that enacted or amended it: headings and History lines are not provisions, but they are lines of your range. Two sections are printed `[Reserved.]`. Delaware statutes and rules that the text cites (the Limited Liability Company Act, the Revised Uniform Limited Partnership Act and other chapters of Title 6, Title 10, Title 29, the Court of Chancery Rules and the federal statutes) are NOT among your inputs: where a rule depends on one, take its outcome as a plain input with a comment and list it in `NOTES.md`. Coverage, stated plainly: every heading in your range (the title, the chapter, each subchapter or part and chapter, and each section heading) gets a coverage row, a heading that is not itself a provision getting an `inert` row, its reason being that it is a pure title (a heading); and every non-blank line of your range, History lines and struck or repealed runs included, must fall inside the source-lines cell of some row (write `src:N` or `src:N-M` there). The lead runs a script that lists the non-blank lines no row names, and sends the agent back to fix them.
- **Read your own ranges with `sed -n 'A,Bp'` in chunks. Never read a whole text file in one go**: the texts are far longer than your range, and the whole file would use up a large part of your context for nothing.

All inputs are under `INPUTS_DIR` (given in your task). Read them there and nowhere else.

## Scope, pinned

- The defaults ruled for Commons (guide section 4) apply: the text alone, plus the instruments that set its numbers or dates if they are among your inputs, otherwise make the number an input and say so; the actors the text names; a judgment the text hands to someone else becomes a conditional input ("..., if the officer is satisfied that ...") and is never guessed; the text's own definitions are worked out from facts (they are in the core), borrowed terms are asked as facts; one case is the text's natural unit; the text's own words, each with a plain gloss in a comment; boards, commencement and regulation-making machinery out (`inert`, with a reason, in the coverage table).

## What this text needs, specifically

The text governs a company (a corporation) and the people around it: those who form it, run it, own shares in it, lend to it, deal with it, and the authorities that supervise it.
Layer 1 encodes, provision by provision: who may do what and on what conditions; which decisions need which approval (the directors, an ordinary resolution, a special resolution, a class vote, a stated fraction or percentage) with the quorum, notice and time limits attached to each; what the company must keep, file, send or disclose and by when; the duties of directors and officers and the defences the text gives them; the rights and remedies the text gives shareholders, creditors and others, and who may exercise them; the offences and penalties the text itself states; and the definitions all of this depends on.
Figures the text states (percentages, numbers of days, amounts) are encoded as the text states them.
A figure the text leaves to the articles, the by-laws, a shareholder agreement, the regulations or the decision of a court or an authority is a plain input, with a comment saying so, never invented.
A rule the text lets the articles or by-laws vary becomes a rule with an input for whether and how they vary it, so that the default and the variation are both encoded.
Powers and duties of an official (a Director, a Registrar, a court) are encoded for what they decide for the person (what may be done to them, what they may require, by when), as the Guide says; their procedure is `inert` only where it is machinery.
Forks to look at: which approval each decision needs, and whether the text says "special resolution" or a fraction; whether a condition is cumulative or alternative on the text's own words; who the text says holds a discretion; how the statute, the articles, the by-laws and any shareholder agreement interact; time limits (from what event, and whether the last day is inside the period); whether a provision applies to every corporation or only to one of a kind (an offering or distributing corporation, a listed company); anything that depends on a definition in another piece (take its answer as an input, see "Cross-references").
"No ambiguities found" is a claim a reviewer will not believe; say where you looked.


## Writing L4 that the stable binary accepts (from the Commons guide, section 5, verbatim)

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Smaller gaps:** `YMD` is missing from the stable prelude, so add a local shim (`YMD y m d MEANS Date d m y`). `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.

The target dialect is `main`: the stable build 1.6.98 named as L4_BIN. Read step 0 of `writing-l4-rules/SKILL.md` and `references/dialects.md` (its "write instead" column) before you write; for any construct the stable binary rejects, write what `dialects.md` says to write instead.

Dates are data. Where your range contains the date of enactment or making of the text, or the date it comes into force, or a commencement rule, carry it as a defined value with an `@ref`: the date in the title block or the assent date if the text gives one, and any commencement date the text fixes or defines by a rule such as "three months after passing", derived from the enactment date where the text says so. Where the text leaves commencement to an order, take the commencement date as a stated input and say so in `NOTES.md`. These dates are what rule-effective-date logic needs; they are not "commencement machinery", which stays out. If your range contains no such provision, say so in `NOTES.md` and do nothing.

## Deliverables, all under your `DEPOSIT` directory (given in your task)

`DEPOSIT` holds exactly one directory, `encodings/legalese-sonnet-5.5/`, which already holds `check.sh`, `srcrefs.py` and the keel's `dg-core*.l4`:

```
DEPOSIT/
  encodings/legalese-sonnet-5.5/
    dg8-*.l4          layer 1: every module of your range (flat folder: IMPORT finds only modules beside it)
    dg8-seat.l4       layer 2: the seat's questions for your range
    dg8-cases-seat.l4 layer 2: worked cases, one per question at least
    dg8-tests-*.l4    tests of layer 1
    NOTES.md, PROGRESS.md
```

All `.l4` files sit directly in that folder (no subfolders), have ASCII filenames beginning with `dg8-` (the keel's begin with `dg-core`), and never define the same name as another module that is imported with it.
You do not write `encoding.json`, `SOURCE-LICENSE.md`, `subject.json`, `README.md` or `source/`: the lead writes the first two when it merges, and the rest already exist or are not yours. You do not copy this brief.

`NOTES.md` carries, under exactly these headings: `## Seat` (the seat and why); `## Jural relations`; `## Coverage table` (the rule above: one row per provision of your ranges); `## Fork register` (every ambiguity, the readings you saw, the one you took, the text that licenses each); `## Cross-references out of my ranges`; `## Needs from the core`; `## What the text turns out to say` (numbered findings, each ending "Asserted." where a case asserts it); `## What the stable binary does not accept`; `## What check.sh prints`; `## Before this is worth relying on`.
Write `NOTES.md` and `PROGRESS.md` yourself and nothing else of the report kind: the harness refuses to let a subagent write report-style files (`FINDINGS.md`, `REPORT.md`, `SUMMARY.md` and the like) and tells you to return findings as text. Your last message is the final report, and the files in the folder are the deliverable.

## Your context will be compacted: make the disk your memory

This run may exceed your context window, and the harness will then compact your context into a summary. So write as you go, not at the end:

- Keep `NOTES.md`'s coverage table and fork register on disk, and add rows after each section you finish.
- Keep `PROGRESS.md`: sections done, sections in progress, what is next, decisions taken (with the section that licenses each), and a list of the files you have written.
- After any compaction, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary of them.

## Tests

Expected values come from the text, never from your code, and are written beside the assertion.
Decide each expected answer by reading the section, write it down, then run. A failing assertion is a finding: never edit an expected value to match what the code computed.
Cover at least: every branch of each rule you encode; the boundary values on each side of every threshold; every question in the seat layer, with the facts a real person in the seat would state; and a case outside the encoding (an explicit "not covered" value, asserted).
If you keep some expectations meant to fail, put them in their own file, count them, record them in `NOTES.md` as a finding, and list them in `check.sh`'s `expected_failed`.
Every case file ends with assertions written equal to assertions satisfied.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/skills/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here, and you do not deposit into a repository) and `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/skills/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** Cite the section on every rule with `@ref`; follow `encoding-a-subject/references/source-locators.md` for quoting and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>`; it must report 0 problems. 
- **Where the source does not answer,** return an explicit "not covered" value (a constructor or `NOTHING`) and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails; a failure is a `DiagnosticSeverity_Error` line and a refusal is a Warning. Report the numbers `check.sh` prints. Run it as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` (the word `unstable` here only tells the script not to compare with a second binary: your binary is already the stable one).
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file except a registered, deliberately failing one.
- **No sleep-polls and no waiting loops**: there is nothing to wait on. Run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.98, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.

## Independence

You may read: `INPUTS_DIR`, your own `DEPOSIT`, the two skills and their references, and the Commons guide copies in `inputs/`. Nothing else on disk.
Do not read any existing encoding of any Act: nothing under `/Users/mengwong/src/legalese/commons`, `commonswt` or `canon`; nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/td` other than your own folder `dg/dg8/` (in particular, not the folders of the other pieces, which are being written at the same time); nothing under `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-commons/13faa5dd-0489-4b66-8599-941241b16104/scratchpad/stable` except that you run the `L4_BIN` binary named in your task; and nothing under `~/.claude/` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
The one exception is `inputs/EXAMPLE-sg-employment-act-seat/`, which is yours to read.
The answers must come from the text alone.
Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) the coverage table summary (counts per disposition, and the number of headings or sections in your ranges against the number of rows); (4) the forks you took, each in a line with the reading chosen; (5) the seat's questions, one line each; (6) any failing or refused assertion and what it means; (7) the cross-references out of your ranges (count, and the ones that matter most) and what you need from the core; (8) what the source does not answer; (9) `peeked`: nothing, or what you opened by accident.
