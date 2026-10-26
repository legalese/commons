# Three encodings of the Charities (Jersey) Law 2014, compared

Written by the comparer agent of the October 2026 fleet, on 2026-10-27 (work began about 02:25 and ended about 03:25, +08).
Status: draft.
No domain expert has read any of the three encodings, and none has read this comparison.
Nothing here is legal advice, and nothing here says which reading of the Law is right.

How to read the marks.
**M** means measured: a command or script I ran produced the figure, and section 11 lists it.
**J** means my judgement.
**C** means taken from the cleanroom's own `COMPARISON.md` and not re-run by me.
Where a cell has no mark, the column or the section heading says which kind it is.

## 0. The three things, and the versions measured

| | July corpus ("July") | Cleanroom | New row ("ours", `legalese-full-2026-10`) |
| --- | --- | --- | --- |
| What it is | 12 modules in `paper/case-studies/charities-jersey-2014` of `legalese/l4-ide`, extracted with `git archive` from `origin/unstable` at `0a9d0474d` (26 October 2026); the directory was last changed on 2026-09-13 (`4921d4b6e` renamed 94 fields to drop a doubled verb, `bea7c4460` six exemptions and one rewording; no change in line or assertion counts), so the files I ran are not byte-identical to the ones the July report and PDFs describe | an encoding of Articles 5 to 7 only, written 2 to 3 August 2026 without sight of the July corpus | the whole Law, by nine group encoders and an integrator, 26 to 27 October 2026 |
| Text of the Law it read | consolidation showing the law from 16 October 2025 | the same (fetched 2026-08-02) | consolidation showing the law from 2 October 2026 |
| Dates | report PDF created 14 July 2026; companion PDF 15 July 2026 (for CALC 2026); the cleanroom's `COMPARISON.md` says the corpus file was committed on 2026-07-18 (C) | `README.md` and `COMPARISON.md` dated 2026-08-03; deposited in the commons row 2026-09-23 | deposit files dated 26 to 27 October 2026 |
| What I ran | `l4 run` on each of the 12 modules, `JL4_LIBRARY_PATH` unset, `nice -n 15`, one process at a time | `l4 run charity-test.l4`, same way | `check.sh` on copies taken at 02:30:44 and 03:02:35, and a harness of my own on a copy of the G2 modules |
| Binary | the fleet's `l4`, sha256 `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475` (M) | same | same |

Ours was changing while I measured, so every figure for it carries a time.
I took two copies of the deposit: at 02:30:44 (129 `.l4` files; 146 files in all) and at 03:02:35 (162 `.l4` files; 179 files in all).
Their hashes are in `run/deposit-snap.sha256` and `run/deposit-snap2.sha256` (M).
Between the two, the integrator re-wired the integration layer for G2's thirteenth fork, one more integration test module (`int-tests-repairs`) appeared, `check.sh` was changed (G2's red file pinned at 15, and expected refusals for some of the independent authors' files), and the independent test authors added 32 modules (`ind-a-*`, `ind-b-*`, `ind-c-*`), which were not in my brief to analyse; I report their counts only from `check.sh`.
The 02:30 copy was red in its integration layer: G2 had gained a thirteenth fork (F2.13), so `Interpretation of Articles 3 to 7` has 13 fields, and `int-readings.l4` still supplied 12 (M; the error text is "you have not supplied these inputs: `whether the Commissioner's staff exercising the Commissioner's function are bound`").
The 03:02 copy printed `check.sh: GREEN` (M).
The integrator's `NOTES.md` was rewritten at 03:13:28, after my first report (it now has 15 sections, 136 forks and a section 11.1 table of 162 modules); until then its table and its fork count of 135 described neither copy.
I re-read the finished file at about 03:23 (section 12 below); its section 11.1 table now equals my 03:02 run, and the 162 `.l4` files of the finished deposit are byte-identical to my 03:02 copy (M).
The group modules (G1 to G9) are byte-identical in the two copies except `FRAGMENT-G2.md` prose, and give the same counts in both runs.
The finished deposit also differs from my 03:02 copy in three non-code files only: `NOTES.md`, `README.md` and `encoding.json` (M).

## 1. Headline figures

- **A. Size and shape (M).**
  July: 12 files, 12,762 lines, 682 rules, 754 assertions, all 754 satisfied, 156 traces with no guard.
  Cleanroom: 1 file, 1,428 lines, 90 rules, 102 assertions, all satisfied, no traces.
  Ours at 03:02: 162 files (domain 1, group 102, integration 27, independent tests 32), 56,280 lines, 3,828 rules, 7,953 assertions, 467 `@export`s, 976 traces; `check.sh` printed GREEN: 7,787 assertions satisfied, 156 failed on purpose, 10 refused on purpose, all 976 traces as expected.
  Ours at 02:30 (the copy I started from): 129 files, 6,110 assertions; the group modules gave 5,432 satisfied and 134 failed on purpose, and the integration layer was red.
- **B. Coverage (M and J).**
  July: 33 of 43 Articles have operative rules, 8 are stubs only (3, 24, 25, 32, 38, 39, 42, 43), Article 2 is partial, Article 1 is not encoded, both Schedules are partial.
  Cleanroom: Articles 5 to 7 only, and within them not 5(4) to 5(8), 6(3), 6(4) or 7(4).
  Ours: 851 provisions; 755 encoded, 80 inert, 2 refused, 14 out of scope; 35 of the 43 Articles have every row encoded, and the other 8 (1, 3, 4, 25, 28, 32, 40, 43) have at least one row that is not.
- **C. Registers of places where the Law reads two ways (M and J).**
  Ours: 136 forks (the first `NOTES.md` said 135; the rewritten one says 136), 35 further entries for conflicts, commencement oddities and slips, and 71 open-question bullets (some hold more than one question).
  July: 20 findings in its report, about 39 interpretation calls in its module headers (J), and 189 `WITHIN <number>` deadlines of which 67 lines are marked as placeholders.
  Cleanroom: 12 numbered ambiguities.
  For Articles 5 to 7 the three registers hold 20 distinct questions: 1 registered by all three, 5 by two, 14 by one.
  For the rest of the Law, July has 43 identifiable items; ours registers the same question for 16 of them (10 with the same reading, 6 with a different default), a related question for 9, and nothing for 18.
- **D. Different defaults where both sides registered the question (J, with M evidence).**
  Nine: three in Articles 5 to 7 (no purposes; a defective determination; who Article 7 binds) and six between July and ours in Articles 4, 11, 21, 27 and 37.
  Two more differ where only one side registered the question (6(2)(e); an ancillary purpose alone).
- **E. Outcomes on the cleanroom's 25 worlds (M).**
  Eight decisions per world, 200 comparisons: ours agrees on 192 (96.0%) under its favoured readings, 199 when F2.1 and F2.10 are both read as their second reading.
  The 8 disagreements have three causes: F2.1 (3), F2.10 (4) and the scope of "properly made" (1).
- **F. What each has that the others lack.**
  See section 8.
  Ours has no NLG, no projection, no golden file and no wizard; the cleanroom has a DMN projection, four golden files and a pinned case file; July has two PDFs for drafters.

## 2. A. Size and shape

All figures are **M** unless stated; the commands are in section 11.
"Rules" is a proxy: lines that start in column 1 and contain `MEANS` (or start with `DECIDE`).
Ours includes fixture and test modules in its totals, and the tables below split them.

| | July | Cleanroom | Ours, copy of 02:30 | Ours, copy of 03:02 |
| --- | --- | --- | --- | --- |
| `.l4` files | 12 | 1 | 129 (domain 1, group 102, integration 26) | 162 (domain 1, group 102, integration 27, independent tests 32) |
| lines | 12,762 | 1,428 | 48,723 | 56,280 |
| bytes | 973,620 | 104,085 | 4,546,194 | 5,249,898 |
| rules (proxy) | 682 | 90 | 3,349 (rule modules 1,736) | 3,828 (rule modules 1,736) |
| rules typed `GIVETH A DEONTIC` | 93 | 0 | 284 in rule modules | 286 (284 in rule modules, 2 in tests) |
| `DECLARE` (types) | 70 | 4 | 405 | 406 |
| `@export` | 0 | 1 | 467 (13 in the integration layer) | 467 (13 in the integration layer) |
| `@ref` lines / `-- src:` quotation lines | 0 / 0 | 45 / 0 (its 62 quoted strings are matched against the Law by its own audit, C) | 1,509 / 1,702 | 1,509 / 1,725 (`srcrefs.py` counts 1,724 and finds 0 problems in 1,666 locators) |
| `#ASSERT` directives | 754 | 102 | 6,110 | 7,953 |
| assertions satisfied (run) | 754 | 102 | 5,640 (group modules 5,432; integration modules 208, not green); the earlier `NOTES.md` table said 5,773 | 7,787 (group 5,432; integration 586; independent 1,769); the finished `NOTES.md` section 11.1 prints the same 7,787 |
| assertions failed (run) | 0 | 0 | 470, of which 134 are the group modules' by design | 156, all expected: 134 in the group red files (G2's holds 15), 6 in `int-tests-red`, 16 in the independent authors' files |
| assertions refused (run) | 0 | 0 | 0 | 10, all expected, in the independent authors' `ambiguous` and `disagree` files |
| diagnostics above Information (errors, warnings) | 0 | 0 | integration layer: 387 errors | none besides the expected failures and refusals |
| `#TRACE` | 156 | 0 | 917 | 976 |
| traces guarded by an `-- EXPECT:` comment | 0 | not applicable | 926 `EXPECT` lines; 900 of 917 traces behaved as expected; the 17 that did not are in `int-tests-chains` and `int-tests-contravention`, whose imports did not compile | 985 `EXPECT` lines; all 976 traces behaved as expected |
| `#EVAL` | 34 | 0 | 0 | 0 |
| golden files | 0 | 4 (`tests/`) | 0 | 0 |
| time to run all modules | about 10 seconds for the 12 modules, one at a time | 0.6 seconds | 446 seconds for `check.sh` | 362 seconds for `check.sh` (162 modules, the quotation check and the trace check), on a loaded machine |

By group, for ours (M).
The group rows are identical in the two copies.

| group | scope | files | lines | rules (proxy) | `#ASSERT` | `#TRACE` | `@export` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| domain | shared nouns | 1 | 261 | 0 | 0 | 0 | 0 |
| G1 | Articles 1, 2 | 7 | 2,897 | 262 | 406 | 3 | 19 |
| G2 | Articles 3 to 7 | 12 | 3,775 | 265 | 385 | 62 | 40 |
| G3 | Articles 8 to 10 | 14 | 4,057 | 304 | 461 | 52 | 42 |
| G4 | Articles 11, 12 | 11 | 4,292 | 302 | 423 | 117 | 27 |
| G5 | Articles 13, 14 | 12 | 4,755 | 325 | 362 | 97 | 46 |
| G6 | Articles 15 to 20 | 12 | 5,932 | 409 | 450 | 195 | 74 |
| G7 | Articles 21 to 25, 37 to 43, endnotes | 13 | 5,983 | 343 | 1,444 | 131 | 79 |
| G8 | Articles 26 to 36 | 12 | 5,830 | 309 | 995 | 112 | 59 |
| G9 | Schedules 1, 2 | 9 | 5,025 | 449 | 640 | 131 | 68 |
| integration, 02:30 | wiring, six headlines | 26 | 5,916 | 381 | 544 | 17 | 13 |
| integration, 03:02 | the same, re-wired, plus `int-tests-repairs` | 27 | 6,168 | 404 | 592 | 17 | 13 |
| independent tests, 03:02 | `ind-a-*`, `ind-b-*`, `ind-c-*`; appeared mid-work | 32 | 7,305 | 456 | 1,795 | 59 | 0 |

Three notes on how far these numbers can be trusted.
**How recent is the integrator's table?**
The table in the first version of `NOTES.md` section 11.1 (last written at 01:50, 129 modules) differed from my 02:30 run in six modules, all in G2 and G7.
The `NOTES.md` rewritten at 03:13 prints a new table of 162 modules, 7,787 satisfied, 156 failed (expected 156), 10 refused (expected 10), `srcrefs` 1,724 lines, 1,666 locators, 0 problems, 976 traces; every one of those figures equals my 03:02 run (M).
**The cleanroom's own line count.**
Its `COMPARISON.md` says 1,472 lines; its `README.md` and `wc -l` say 1,428 (M).
I use 1,428.
**July under a newer binary.**
The July corpus was written for an earlier `l4`; with the fleet's binary it runs with no error and no warning, and gives the 754 satisfied assertions its report states (M), so there is no tool-vintage effect to separate from the Law-vintage effect.

## 3. B. Coverage by Article and Schedule

Ours is **M** (from `coverage-all.tsv`, 851 rows, which is the integrator's table of the nine groups' coverage tables).
July and the cleanroom are **J**: I read every module's headings, rule names and stub markers (`INERT`, `STUB`) and the header comments, and I did not read every rule.
"Operative" means rules or data decide something; "stub" means the Article's words are quoted and carry no logic.

| Article | July corpus (J) | Cleanroom (J) | Ours (M): rows / encoded / inert / refused / out-of-scope |
| --- | --- | --- | --- |
| Article 1 | none: no Article 1 definition is encoded; "Minister" is an actor and a comment | carried inert (the definitions the test uses) | 40 / 5 / 23 / 0 / 12 |
| Article 2 | partial: 2(1), 2(1)(ba), 2(3), 2(7), 2(8), 2(9)(a), 2(10); not 2(2), 2(4) to 2(6) | 2(4), (6), (7) carried inert | 71 / 71 / 0 / 0 / 0 |
| Article 3 | stub (inert prose) | not encoded | 3 / 0 / 3 / 0 / 0 |
| Article 4 | operative: 4(1) to 4(4) | not encoded | 19 / 13 / 6 / 0 / 0 |
| Article 5 | operative | 5(1) to 5(3) operative; 5(4) to 5(8) out of scope | 21 / 21 / 0 / 0 / 0 |
| Article 6 | operative | 6(1), (2), (5) operative; 6(3), (4) out of scope | 36 / 36 / 0 / 0 / 0 |
| Article 7 | operative | 7(2), (3) operative (7(1) applied to everyone: A5); 7(4) out of scope | 11 / 11 / 0 / 0 / 0 |
| Article 8 | operative | not encoded | 38 / 38 / 0 / 0 / 0 |
| Article 9 | operative; 9(3) stub | not encoded | 33 / 33 / 0 / 0 / 0 |
| Article 10 | operative; 10(2) stub | not encoded | 11 / 11 / 0 / 0 / 0 |
| Article 11 | operative; 11(3), (7), (8) stubs | not encoded | 55 / 55 / 0 / 0 / 0 |
| Article 12 | operative | not encoded | 18 / 18 / 0 / 0 / 0 |
| Article 13 | operative; 13(8), (9), (10), (12) stubs | not encoded | 35 / 35 / 0 / 0 / 0 |
| Article 14 | operative; 14(5), (6) inert prose | not encoded | 23 / 23 / 0 / 0 / 0 |
| Article 15 | operative | not encoded | 6 / 6 / 0 / 0 / 0 |
| Article 16 | operative | not encoded | 7 / 7 / 0 / 0 / 0 |
| Article 17 | operative | not encoded | 20 / 20 / 0 / 0 / 0 |
| Article 18 | operative | not encoded | 18 / 18 / 0 / 0 / 0 |
| Article 19 | operative | not encoded | 31 / 31 / 0 / 0 / 0 |
| Article 20 | operative | not encoded | 17 / 17 / 0 / 0 / 0 |
| Article 21 | operative | not encoded | 33 / 33 / 0 / 0 / 0 |
| Article 22 | operative | not encoded | 12 / 12 / 0 / 0 / 0 |
| Article 23 | operative | not encoded | 17 / 17 / 0 / 0 / 0 |
| Article 24 | stub | not encoded | 8 / 8 / 0 / 0 / 0 |
| Article 25 | stub | not encoded | 13 / 2 / 11 / 0 / 0 |
| Article 26 | operative | not encoded | 22 / 22 / 0 / 0 / 0 |
| Article 27 | operative | not encoded | 13 / 13 / 0 / 0 / 0 |
| Article 28 | operative (categorization and severance) | not encoded | 11 / 7 / 2 / 0 / 2 |
| Article 29 | operative | not encoded | 8 / 8 / 0 / 0 / 0 |
| Article 30 | operative | not encoded | 3 / 3 / 0 / 0 / 0 |
| Article 31 | operative | not encoded | 7 / 7 / 0 / 0 / 0 |
| Article 32 | stub / inert (32(1) inert, 32(3) stub) | not encoded | 4 / 0 / 4 / 0 / 0 |
| Article 33 | operative | not encoded | 15 / 15 / 0 / 0 / 0 |
| Article 34 | operative | not encoded | 9 / 9 / 0 / 0 / 0 |
| Article 35 | operative | not encoded | 5 / 5 / 0 / 0 / 0 |
| Article 36 | operative; 36(1), (2) stubs | not encoded | 7 / 7 / 0 / 0 / 0 |
| Article 37 | operative | not encoded | 5 / 5 / 0 / 0 / 0 |
| Article 38 | stub | not encoded | 1 / 1 / 0 / 0 / 0 |
| Article 39 | stub | not encoded | 3 / 3 / 0 / 0 / 0 |
| Article 40 | 40(1) operative; 40(2), (3) stubs | not encoded | 4 / 3 / 1 / 0 / 0 |
| Article 41 | 41(1) operative; 41(2) stub | not encoded | 6 / 6 / 0 / 0 / 0 |
| Article 42 | stub | not encoded | 3 / 3 / 0 / 0 / 0 |
| Article 43 | stub | not encoded | 1 / 0 / 1 / 0 / 0 |
| Sch 1 | partial: 4(3) (reserved decisions) and the numeric bounds 1(5), 3(4)(c), 4(9) are operative; the rest inert prose | not encoded | 55 / 43 / 12 / 0 / 0 |
| Sch 2 | partial: 1(1) (member count), 3(4) (report longstop) and 4(1) (presiding cascade) are operative; the rest inert prose | not encoded | 48 / 37 / 10 / 1 / 0 |
| Title, long title, commencement note, endnote rows (E, R, N) | none | none | 25 / 17 / 7 / 1 / 0 |
| **All** | | | **851 / 755 / 80 / 2 / 14** |

**Articles a predecessor does not encode (J).**
July: Article 1 (none of its definitions is encoded; "registered charity" is a primitive boolean in Part 6, "Minister" is an actor); Article 2(2) and 2(4) to 2(6); the commencement stages, the nine texts and the endnotes.
Its own stubs: Articles 3, 24, 25, 32, 38, 39, 42, 43 whole, and 9(3), 10(2), 11(3), 11(7), 11(8), 13(8), 13(9), 13(10), 13(12), 36(1), 36(2), 40(2), 40(3), 41(2).
The reason it gives is that these are Order- or Regulation-making powers or bare constitutive text with no computable content, and that "encoding one would mean inventing the Order" (report section 9).
One inconsistency inside July: the stub for Article 32(3) says "Schedule 2 is not encoded in this corpus" (`part-8-appeals.l4:160`), while `schedules-1-and-2.l4` encodes parts of Schedule 2.
Cleanroom: everything outside Articles 5 to 7 and the definitions it uses.
It names its omissions: 5(4) to 5(8) ("procedural; the only deontic material nearby"), 6(3) and 6(4) ("amendment power, not a test"), 7(4), and Parts 2 and 4 to 7 entirely.

**What ours encodes as inert, refused or out of scope, and why (M for the counts and the reasons; the reasons are the survey's, in `phase1/coverage.tsv`, with the group's changes).**
96 of 851 rows: 80 inert, 2 refused, 14 out of scope.

| rows | Articles | disposition | reason |
| --- | --- | --- | --- |
| 35 | Article 1 definitions | 23 inert, 12 out of scope | 21 are pure pointers to rules encoded elsewhere; 3 are role definitions carried by an actor constructor (`the Commissioner`, `the court`, `the Charity Tribunal`); "prescribed" is implemented by the fleet convention that an Order's content is an input; 12 define terms of other enactments that are not among the sources (company, foundation, trust, 1862 association, fidéicommis, Loi, JFSC, property, and the four limbs of "regulated financial services business") |
| 2 | Title, Long title | inert | heading and statement of purposes; gate nothing |
| 3 | Article 3 | inert | constitutive; the office is the actor `the Commissioner`; who holds it is Schedule 1 |
| 6 | Article 4(1)(a), (b), (c), (e), (f), (g) | inert | functions with no precondition or outcome; they only fix the reach of 4(2) |
| 11 | Article 25(2) | inert | illustrates what an Order under 25(1) may contain; Orders are inputs |
| 4 | Article 28(2)(b) | 2 inert, 2 out of scope | content of an Order; the Scottish and UK Acts it names are not in the sources |
| 4 | Article 32 | inert | constitutive; pointer to Schedule 2 |
| 2 | Article 40(1), Article 43 | inert | a rule of construction with no input or outcome; citation only |
| 23 | Schedules 1 and 2 | 22 inert, 1 refused | capacities of a corporation sole, restatements of terms of appointment, and subject matter of Regulations; `Sch2 4(3)(e)` (quorum and voting) is refused because the Regulations are not in the sources |
| 6 | commencement note, endnote rows | 1 refused, 5 inert | the commencement note is a pointer; R1 (what the original Article 41 provided) is not in the sources, so it is a named refusal; R5, R6 are spent; N3, N4 are typographical corrections |

Differences of disposition between ours and the others (J).
Ours treats Article 40(1) as inert where July encodes it as a non-derogation rule with a three-limb conjunction.
Ours encodes Articles 24, 25(1), 41(2) and 42 as rules for the States or the Minister (a power, with its content an input), where July quotes 24, 25, 41(2) and 42 as stubs.
Both treat Article 3 as inert.

## 4. C. Registers of places where the Law reads two ways

### 4.1 What each register is

| | Ours | July | Cleanroom |
| --- | --- | --- | --- |
| Main register | forks: 136, each a field of an `Interpretation of ...` record, `TYPICALLY` the reading taken, with the other readings callable and tested (M) | 20 findings in the report: 8 with a section each and 12 in one-line bullets (M, by reading); about 39 interpretation calls in the module headers marked `>>>` (J, counted by reading the headers of 10 modules; test-level `>>>` commentary not counted) | 12 ambiguities A1 to A12, each marked `-- AMBIGUITY A<n>` at the site (M) |
| Other registers | 35 entries S1 to S35 for conflicts, commencement oddities and slips (25 that change an answer, 3 on commencement, 7 slips; S35 is F2.13, added at 03:13); 71 open-question bullets; the independent authors' ambiguity rows kept in section 12.3; non-fork readings listed in G2 (8), G4 (13), G6 (18) and G7 (4) (M) | 189 `WITHIN <number>` deadlines invented where the Law gives none, of which 67 lines are marked as placeholders; the report says "roughly forty" (M) | a thirteenth reading recorded as "not an ambiguity" (M) |
| Stale or inconsistent | the first `NOTES.md` section 5 said 135 and omitted F2.13; the rewritten one says 136, and its fork table still has an empty question for all 14 G7 forks (M) | the report counts "about twenty" findings and the `>>>` markers are more than twice that (J) | its `COMPARISON.md` counts 1,472 lines against 1,428 (M) |

How ours' forks divide by kind (J: my classification of each fork's question; the lists are in `scripts/fork-classes.py`).

| kind of question | forks |
| --- | --- |
| meaning, scope or relation of provisions | 77 |
| time arithmetic: when a period starts or ends, how days, months, years and units are counted, which date | 49 |
| promptness: "reasonable time", "promptly", "as soon as practicable" | 7 |
| commencement and which text of the Law is in force | 3 |
| all | 136 |

Four of the 136 are one question asked in four groups: the unit of a term of imprisonment (F6.16, F7.8, F8.8, F9.13).
July flags one time-arithmetic choice with a `>>>` (a period of one year is taken as 365 days, `part-7-information.l4:307`) and does not register the others; where the Law gives no period it writes a number and marks it as a placeholder.

### 4.2 Articles 5 to 7: all three compared, question by question (J)

"Registered" means a numbered or named entry in the encoding's own register of readings (a fork, an `A<n>`, a `>>>` call, or, for ours, a contradiction entry).
"Not recorded" means I found no such entry; the encoding may still carry a reading, and where it does the cell says what.

| Q | Provision | The question | Ours | Cleanroom | July | Registered by |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | 5(1)(a) | "all of its purposes" when the entity has no purposes | F2.1 (fork) | A10 (register) | header call (part-3 line 52) and README Sidebar 8 | all three |
| Q2 | 5(1)(a)(ii) | an ancillary purpose when no charitable purpose stands beside it ("any of its charitable purposes") | F2.1 (same fork as Q1) | A9 (register) | not recorded | ours and cleanroom |
| Q3 | 6(2)(e) | "(1)(n) includes relief given by accommodation or care": widening or declaratory | not recorded | A2 (register) | not recorded | cleanroom only |
| Q4 | 6(2)(c) | "sport that involves physical skill and exertion": both, or either | not recorded (one input fact) | A1 (register) | not recorded (one boolean) | cleanroom only |
| Q5 | 6(1)(p) | "may reasonably be regarded as analogous": open standard or closed list | listed in G2 section 8 as a judgement the caller records (not a register entry) | A3 (register) | not recorded (a boolean) | cleanroom only |
| Q6 | 6(5) | political carve-out: purpose-level or entity-level | not recorded | A4 (register) | README section 5 (per-purpose, at both gates), not as a question | cleanroom only |
| Q7 | 7(1), 7(3)(b) | who Article 7 binds: everyone who determines, or only the officers it names | A-14 and A7-01b in NOTES section 12.3 (independent authors' ambiguity rows, kept; not forks); F2.13 is adjacent (staff) | A5 (register) | not recorded | ours and cleanroom |
| Q8 | 7(3)(b) | "accordingly must not treat ... as providing public benefit": operative bar or evidential | noted inside F2.10 ("not subject to the fork"), not a register entry | A6 (register) | README section 5 ("hortatory in form, operative in substance"), not a register entry | cleanroom only |
| Q9 | 7(2)(b) | "unduly restrictive": a defeater of public benefit, or a consideration only | not recorded | A7 (register) | README section 5 (7(2) carried as duties, not truth-conditional), not as a question | cleanroom only |
| Q10 | 7(2), 7(3)(a), 5(5) | what follows from a determination made in breach of the duties on its maker | F2.10 (fork) | A8 (register) | README section 5 (duties on the determiner), not as a question | ours and cleanroom |
| Q11 | 5(1)(b) | who may rely on "intends to provide": applicants only, or anyone | C2 (contradictions list, not a fork) | A11 (register) | not recorded (one boolean, per the cleanroom's D4) | ours and cleanroom |
| Q12 | 5(2) | reach of the list (a) to (c): both the direction mode and the governor mode | not recorded | A12 (register) | not recorded | cleanroom only |
| Q13 | 5(2) | "acting in that capacity" | F2.2 (fork) | encoded as a conjunct, not registered | folded into a field name, not registered | ours only |
| Q14 | 5(2)(a) | "a Minister" or "the Minister" | F2.3 (fork) | not registered | not registered | ours only |
| Q15 | 6(1)(l) | "equality and diversity": both or either | F2.11 (fork) | not registered (one boolean) | not registered | ours only |
| Q16 | 6(2)(f), 6(1)(p), 6(1)(c) | philosophical belief: head (p) or head (c) | F2.5 (fork; matters for Article 28) | encoded via (p), not registered | not registered | ours only |
| Q17 | 5(7), 5(8) | "within a reasonable time" and "as soon as practicable" | F2.4 (fork) and F2.6 (day counting) | out of scope | WITHIN 90/30 placeholders flagged (part-3 lines 362-363) | ours and July |
| Q18 | 5(6) | "before issuing or amending guidance": strictly an earlier day | F2.7 (fork) | out of scope | not recorded | ours only |
| Q19 | 5(6) to 5(8), 11(6)(b) | which guidance Articles 5(6) to 5(8) apply to | F2.12 (fork) | out of scope | not recorded | ours only |
| Q20 | 7(1), 5(5), Sch 1 4(3) | staff exercising the Commissioner's function: bound as the Commissioner is | F2.13 (fork) | out of scope | not recorded | ours only |

Counts, from the table (M): 20 distinct questions.
Registered by all three: 1 (Q1).
Registered by two: 5 (Q2, Q7, Q10, Q11 by ours and the cleanroom; Q17 by ours and July).
Registered by one: 14, of which 7 by the cleanroom alone (Q3 to Q6, Q8, Q9 and Q12) and 7 by ours alone (Q13 to Q16 and Q18 to Q20).
Q7 changed status in the re-read at 03:23: the first `NOTES.md` did not record it, and the rewritten section 12.3 records it twice (A-14 from ind-b and A7-01b from ind-c, both "ambiguity kept"); my first report counted 1, 4 and 15.
July registers only Q1 and Q17 in Articles 5 to 7, and describes Q6, Q8, Q9 and Q10 in prose without presenting them as questions.

Which side saw a question the other did not (J).
The cleanroom saw seven that ours did not register: 6(2)(c) conjunctive or not (Q4), the analogy standard in 6(1)(p) (Q5, which ours lists as a judgement the caller records), whether 6(5) works at purpose or entity level (Q6), whether 7(3)(b) is operative (Q8), whether "unduly restrictive" defeats public benefit (Q9), the reach of the list in 5(2) (Q12), and 6(2)(e) (Q3).
The cleanroom's own `COMPARISON.md` called 6(2)(e) "the single most useful thing this whole exercise produced", because the July corpus took the widening reading without recording that a choice was made.
Ours repeats that: ours widens (`g2-art6-purposes.l4:268-283`; `g2-tests-art6.l4:139-144` asserts it) and nothing in any fragment, in the rewritten `NOTES.md` or `README.md`, or in any module comment I found records 6(2)(e) as contestable (M: `grep` for "accommodation" and "6(2)(e)" across all fragments finds only the coverage row, the answer table and a test inventory, and finds nothing in `NOTES.md` or `README.md`; re-run at 03:23).
Ours registered seven that nobody else did: four inside the cleanroom's scope, which the cleanroom encoded without registering ("acting in that capacity", Q13; "a Minister", Q14; "equality and diversity", Q15; the philosophical-belief head, Q16), and three outside the cleanroom's scope (the "before" of 5(6), Q18; which guidance 5(6) to 5(8) reach, Q19; the Commissioner's staff, Q20).
Ours and July both registered the promptness of 5(7) and 5(8) (Q17), in different ways: ours as a fork with no number, July as a flagged placeholder number.
July saw none that the other two missed in Articles 5 to 7 (its only registered call there, Q1, was also seen by both).

### 4.3 The rest of the Law: July against ours (J, with M evidence for the counts)

The cleanroom does not cover this part, so at most two registers can agree.
Each row is an item in July's report or module headers, matched to the nearest entry in ours.
"Not recorded" means I searched all nine fragments, `NOTES.md` (including the rewritten section 12.3), and the `.l4` module comments for the provision and its keywords and found no register entry; for six of the eighteen I also read the module and saw the reading encoded (rows 9, 10, 18, 19, 41, 42).
Match: SAME is the same question with the same reading taken; DIFF is the same question with a different default; REL is a related question, a different aspect of the same provision, or a question that ours registers and declines to answer (row 11); JONLY is a July item with no register entry in ours.

| # | Provision | July's item | Ours | Match | July's reading | Ours' reading |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2(1)(ba), 2(3)(a) | part-1 header call; README Finding 1 | F1.1 (also F3.13, S3) | SAME | (ba) is inside the range "(a) to (h)" | (ba) is inside the range "(a) to (h)" |
| 2 | 4(2), 4(3) | part-2 header call (1) | F2.8 | DIFF | 4(3) is an independent route that "need not pass the 4(2) gate" (neither the function nexus nor the governor carve-out; part-2-commissioner.l4:184, 188-201; its own assertions at 430-431 hold assisting the Guernsey Registrar to be outside 4(2) and inside 4(3)) | the 4(3) examples illustrate 4(2) and are bound by its conditions (function nexus and carve-out) |
| 3 | 4(4) | part-2 header call (2); README Finding 7 | F2.9 | DIFF | one gate over the whole sentence: NOT gate OR (a AND b) | each limb binds so far as it appeared practicable |
| 4 | 4(4) | part-2 header call (2)(i); README Finding 7 | S28 (G2 C1) | SAME | the missing "as" read as "so far as appears", text quoted (sic) | the same |
| 5 | 4(4)(b) | part-2 header call (3) | not recorded | JONLY | "registered charities" shared by two conjuncts | encoded alike (two limbs) |
| 6 | 11(4), 11(5) | part-4 header call [1]; README Finding 2 | F4.3 (also S1) | DIFF | both kept; the unqualified rule "the registration decision" is the two-arm reading (gate failure folded into refusal) | reading A taken: no duty to register or refuse while the application does not comply (July's "literal three-way") |
| 7 | 8(4)(b), (c) | part-4 header call [2]; README Finding 8 | F3.10 | SAME | a private dwelling house yields no address under (b); the cascade falls to (c) | the same |
| 8 | 11(4)(c)(ii), 12(1), 12(4), 12(7)(b)(ii) | part-4 header call [3] | NOTES 6.7 and 9 (inputs, not forks) | SAME | "in the opinion of the Commissioner" folded into the atom | each judgement is an input |
| 9 | 10(4), 10(5) | part-4 header call [4] | not recorded (encoded in g3-art10-public-access.l4:103) | JONLY | a designation without the 10(4) condition is no designation | designation available only where 10(4) applies |
| 10 | 9(6) | part-4 header call [5]; README bullet | not recorded (encoded in g3-art9-restricted-section.l4:264-272) | JONLY | satisfied: may enter; not satisfied: shall not; no duty to enter | the same (may; prohibition bites only when not satisfied) |
| 11 | 12(3), 12(4) | part-4 header call [6]; README bullet | G4 section 8 (open question; the function answers NOTHING) | REL | no duty to grant; permission stays discretionary | left open (ours declines to answer where no ground applies; July decides) |
| 12 | 8(6) | part-4 header call [7] | F3.1 (also S10) | REL | a retention period, not a performance deadline | asks from when the ten years run |
| 13 | 13(13) | part-4-effects header; README bullet | not recorded | JONLY | "to the extent that" collapsed to one boolean | not found in the registers |
| 14 | 15(3) | part-4-effects header | F6.1 (also F9.8) | REL | forced choice; limb (b) only on grounds relating to the proposals | asks what follows where 15(2) is not complied with |
| 15 | 14(1) | part-4-effects header; README bullet | not recorded (encoded as the application input) | JONLY | standing is a conjunct; the court cannot act of its own motion | not found in the registers |
| 16 | 17(4) | part-4-effects header; README bullet | G6 section (2a) (non-fork); F6.3 | REL | a safety property tested against an independently criminal act | "before the date of the notice" strictly before; which notice |
| 17 | 17(9) | part-4-effects header | S17 | REL | gates the Article 14 action on the 17(9) conditions | 17(9) lends Article 14 but the Commissioner is not an applicant |
| 18 | 18(4)(a), 2(10)(b) | part-5 header call; README Finding 4 | not recorded (the attribution is in the type Conduct of a governor) | JONLY | the actor must be this governor | encoded by type |
| 19 | 18(3) | part-5 header call; README bullet | not recorded (a judgement of the caller, g6-art18-governor-duties.l4:191) | JONLY | "to any extent" collapsed to booleans | the same collapse, by comment |
| 20 | 19(6) | part-5 header call | S24 (also F4.3) | SAME | one-way: non-compliance makes incomplete; do not infer completeness | "complete" is not "includes what 11(2) requires" |
| 21 | 19(1)(a) | part-5 header call; README bullet | G6 section (2a) (non-fork) | SAME | "being" restrictive: bare misconduct with no notice is not reportable | the link is a determination supplied as a fact; some notice must exist |
| 22 | 19(10) | part-5 header call; README bullet | not recorded | JONLY | "unless": permission AND compliance with its conditions | permission modelled by dates (given, withdrawn, determined, ends); conditions not found |
| 23 | 21(2)(b)(ii), 21(4)(b)(ii), 21(6)(b)(ii), 23(2)(b)(ii) | part-6 header call 2 | F7.5 (also S20) | DIFF | one shared predicate carrying the wider wording ("or other advantage") | the difference is kept as printed |
| 24 | 21(2), 21(4), 21(6), 23(2) | part-6 header call 3 | not recorded | JONLY | both the objective fact and the mens rea are required | not found in the registers |
| 25 | 21, 23 | part-6 header call 4 | not recorded | JONLY | cause or permit modelled as the same act, attributed | not found in the registers |
| 26 | 22(3)(a), 22(4) | part-6 header call 6 | not recorded | JONLY | the entity's actual jurisdiction of establishment, whatever 22(4) disapplies | not found in the registers |
| 27 | 21(1), 22(3)(b) | README Finding 5 | not recorded (G7 scenario 12 tests the registration claim) | JONLY | an excepted foreign charity always breaches 21(1) | encoded; not registered as a question |
| 28 | 29(1) | part-7 header (26(9)/29(1)) | F8.11 | SAME | both consents are required | both consents are required |
| 29 | 27(1) | part-7 header (belief chapeau) | F8.14 | DIFF | belief AND the limb's content (borne out) | reading A taken: the belief alone is the ground |
| 30 | 26(3) | part-7 header (lien) | G8 open question 2 | REL | the lien is saved: true exactly when claimed | whether a lien is a reasonable excuse under 26(7) |
| 31 | 33(5) | part-8 header call (1); README Finding 3 | F8.18 (also S9) | SAME | ground-wise: one ground at both times | each ground must hold at both times |
| 32 | 33(5)(b) | part-8 header call (2); README Sidebar 8 | not recorded | JONLY | "if" is a requirement of the ground, not a material implication | not found in the registers |
| 33 | 34(1) | part-8 header call (3) | not recorded | JONLY | cross product (wrong or unreasonable) x (merits, facts, law) | not found in the registers |
| 34 | 34(1), 35(1) | README Finding 6 | F8.5 (also S13) | SAME | appeal to the court only on the ground in 35(1) | the same |
| 35 | 37 | part-9 header call (1) | not recorded | JONLY | the attribution is surfaced as a SHANT | not found in the registers |
| 36 | 37(1)(a) | part-9 header call (2) | F7.10 (also F7.6) | DIFF | flat disjunction of capacities; no cross-gate | capacity as printed for each kind of body (cross-gated) |
| 37 | 37 | part-9 header call (3) | not recorded | JONLY | consent or connivance one proved fact; no neglect limb | not found in the registers |
| 38 | Sch 1 4(3) | schedules header call; README bullet | F9.8 (also S12) | SAME | the reservation covers both arms of the decision | both outcomes are reserved |
| 39 | 20(5) | README bullet | F6.14 | REL | 15-year cap enforced; passing 20(4) is not having the power | asks how the fifteen years are counted |
| 40 | 28(3) | README bullet | S14, F6.15, F8.15 | REL | severance requirement by requirement | conflict with 19(9)(e)(i); scope of 27(2) notices |
| 41 | 26(8) | README bullet | not recorded (encoded in g8-art26-demand.l4:442) | JONLY | privileged material was never validly required | privilege takes the requirement outside 26 |
| 42 | 36(4) | README bullet | not recorded (encoded in g8-art32-36-appeals.l4:663-672) | JONLY | "merely": an independently criminal act stays criminal | the act before the order is protected |
| 43 | 36(2) | part-8 header (5) | F8.6, F8.12 | REL | placeholders (28 and 90 days), flagged | asks from when the time limit runs, and the first day |

Counts (M, from the table): 43 July items; SAME 10; DIFF 6; REL 9; JONLY 18.
So ours registers the same question as July for 16 of the 43.
Of ours' 136 forks, 12 are matched to a SAME or DIFF row (F1.1, F3.10, F4.3, F7.5, F7.10, F8.5, F8.11, F8.14, F8.18, F9.8 outside G2, and F2.8 and F2.9 inside it); 8 more relate to a REL row (F3.1, F6.1, F6.3, F6.14, F6.15, F8.6, F8.12, F8.15); and 105 of the 123 forks outside G2 have no July counterpart that I found.
July's deadline placeholders (189 numbers) correspond in ours to seven promptness forks and to inputs, and not to numbers.

## 5. D. Where both sides saw the same question and took different readings

The nine rows where both registers have the question and ours takes a different default.
The first three are in Articles 5 to 7 (ours against the cleanroom, with July's reading added); the other six are ours against July.
A question that ours registers and declines to answer is not counted here (12(3), 12(4): row 11 of section 4.3).

| # | Provision | Ours | The other | One discriminating case | Evidence |
| --- | --- | --- | --- | --- | --- |
| D1 | 5(1)(a), "all of its purposes" with no purposes (F2.1; A10; July's call) | reading A: fails (a); at least one charitable purpose is required | cleanroom A10 and July: passes (a) by vacuous truth; 5(1)(b) decides | an entity with no purposes and a sound finding of public benefit (cleanroom world 06): cleanroom and July meet the test, ours does not | M: harness, world 06 (decisions E1, E2) and 07 (E2); ours agrees under F2.1 B |
| D2 | 7(2), 7(3)(a), 5(5), consequence of a defective determination (F2.10; A8) | reading A: the determination does not answer; the encoding refuses | cleanroom (and July, in prose): the finding stands; the test is met on the merits | the Commissioner presumed a charitable purpose to be for the public benefit and found that the entity provides it (world 23); also world 24, where 7(2)(b) was not asked | M: harness, worlds 23 and 24 (E1, E3); ours agrees under F2.10 B |
| D3 | 7(1) with 7(3)(b), who is bound (A5; A-14 and A7-01b in `NOTES.md` section 12.3) | only the Commissioner, the Tribunal, the court (and staff on F2.13 reading A); a finding by anyone else stands | cleanroom A5(i) and July: the bar applies to every candidate (July: `part-3-charity-test.l4:305-318`) | the grandchildren's trust with a finding of public benefit made by `any person` | M, probe `cmp-a5.l4`: the same finding gives FALSE for the Commissioner, the Tribunal and a member of staff, and TRUE for `any person` and for `a governor` |
| D4 | 4(2), 4(3) (F2.8) | the 4(3) examples are bound by 4(2)'s conditions (the function nexus, and the governor carve-out) | July: 4(3) is "an INDEPENDENT route: they need not pass the 4(2) gate" (`part-2-commissioner.l4:184`), so neither condition applies to 4(3); its own assertions at lines 430-431 hold assisting the Guernsey Registrar of Charities to be outside 4(2) and inside 4(3); its header call (1) is about the carve-out alone | assisting an equivalent body outside Jersey where it relates to no function of the Commissioner: ours no power, July power | M for July (its own assertions at lines 430-431); J for the reading of ours' rule at `g2-art3-4-commissioner.l4:100-110` |
| D5 | 4(4), "so far as ... practicable" (F2.9) | each limb binds so far as it appeared practicable | July: one gate over the whole sentence, `NOT gate OR (a AND b)` (`part-2-commissioner.l4:249-255`) | first limb practicable and not sought, last limb impracticable: ours broken, July not bound | J |
| D6 | 11(4), 11(5), an application that does not comply (F4.3) | reading A: no duty to register or refuse | July keeps both; its unqualified rule is the two-arm reading, so it must refuse | everything found but the copy of the constitution is missing | J (`part-4-register-and-application.l4:898-918`) |
| D7 | 21(2)(b)(ii) against 21(4)(b)(ii), 21(6)(b)(ii), 23(2)(b)(ii), "or other advantage" (F7.5) | the wording differs as printed | July: one predicate carrying the wider wording | intent to induce volunteers to give their time: ours no offence under 21(4), July an offence | J (G7 scenario 11; July call 2) |
| D8 | 27(1), "if the Commissioner believes that" (F8.14) | reading A: the belief alone is the ground | July: belief and the limb's content both required (`part-7-information.l4:496-503`) | a belief that misconduct occurred when the facts show none | J |
| D9 | 37(1)(a), officers of "the partnership" and "the body corporate" (F7.10) | capacity as printed for each kind of body | July: flat disjunction; "cross-gate" expressly rejected | a director of a limited liability partnership who connived | J |

Two more differences in default, where only one side registered the question (J):

| # | Provision | Readings | One discriminating case | Evidence |
| --- | --- | --- | --- | --- |
| D10 | 6(2)(e), accommodation or care | ours and July widen head (n); the cleanroom (A2) reads (e) as declaratory and gives it no operand | a commercial care home: ours and July charitable on that ground alone; cleanroom not | M for ours' reading (module and test); C for the cleanroom and July |
| D11 | 5(1)(a)(ii), an ancillary purpose with no charitable purpose beside it | ours (F2.1 A, B) and the cleanroom (A9): fails. July: passes (the ancillary flag is taken as given) | a charity shop with nothing behind it (world 02): ours and cleanroom fail it | M for ours and the cleanroom (world 02 agrees on all 8 decisions); C for July (cleanroom `COMPARISON.md` D2) |

One case that looks like a disagreement and is a difference of definition (J).
World 21 (the grandchildren's trust), decision "the determination was properly made": the cleanroom says TRUE, ours says FALSE under every reading (M).
In the cleanroom, 7(3)(b) is a bar on the finding of public benefit and "properly made" covers only 7(2)(a), 7(2)(b) and 7(3)(a); in ours, a finding that such an entity provides public benefit is itself a breach of 7(3)(b), so the determination is not properly made.
Both give the same answer to the question the Law asks (the entity does not provide public benefit), so I count it as a difference of scope in a helper predicate, not of outcome.

## 6. E. Outcomes on shared scenarios, Articles 5 to 7

### 6.1 What I did

The cleanroom ships `charity-test.cases.json`: 25 worlds, each an entity with its purposes, constitution, applicant flag and public-benefit finding, with 40 decisions pinned to what its own L4 gave.
I expressed each world as inputs to ours' exports, with `scripts/gen-harness.py`, and evaluated them with `#EVAL` under the group's own named readings, in a copy of the G2 modules (`run/e/`).
G2 version: the module hashes in `run/e/e-inputs.sha256`; they are the same as at 02:28 when I began and, at the time of the last check (section 12), the same as in the live deposit.
Eight of the cleanroom's 40 decisions have a counterpart in ours' exports (called E1 to E8 below):

| # | Cleanroom decision | Ours |
| --- | --- | --- |
| E1 | `the_entity_meets_the_charity_test` | `Art 5 the entity meets the charity test` |
| E2 | `_5_1_a_all_of_its_purposes_are_charitable_or_ancillary` | `Art 5(1)(a) all of the entity's purposes are charitable or purely ancillary` |
| E3 | `_5_1_b_public_benefit` | `Art 5(1)(b) the entity provides public benefit to a reasonable degree` |
| E4 | `_5_2_the_government_control_disqualification_applies` | `Art 5(2) the bar applies to the entity` (with the Order input) |
| E5 | `_5_the_purpose_is_excluded_as_political` | `Art 6(5) the purpose is neither charitable nor ancillary` |
| E6 | `the_purpose_is_charitable_or_purely_ancillary_or_incidental` | `Art 5(1)(a) the purpose counts` |
| E7 | `the_purpose_falls_within_paragraph_1` | `Art 6(1) the purpose falls within a paragraph of paragraph (1)` |
| E8 | `the_public_benefit_determination_was_properly_made` | `Art 7 the determination complies with the duties on its maker` |

The other 32 decisions are the 16 heads and the intermediate limbs.
Ours has no counterpart for the 16 heads as decisions, because a purpose's head is recorded by the caller (a purpose is given its head, so "the purpose falls under head (a)" is true of whatever was recorded); comparing them would compare the harness with itself.
I did not compare the intermediate limbs.

### 6.2 How the vocabularies map, and what did not

| cleanroom field | ours | note |
| --- | --- | --- |
| purpose with up to 16 head booleans | `Purpose` with one `head` (MAYBE) | no world has two heads; the generator would have reported one |
| extension and gate booleans (sickness, regeneration, civic, sport skill, recreation need and public, equality, diversity) | `Facts about a purpose under Article 6` | `object of improving the conditions of life` set TRUE for the two recreation worlds because the cleanroom's head (i) boolean already includes it; equality and diversity both TRUE for the one world with the compound head |
| `constitution` with six permission booleans and one capacity boolean | list of `Permission that a constitution expressly makes` | the one capacity boolean is copied onto each permission; "a Minister" maps to `a Minister` with no office |
| `an_applicant` | `standing on the register`: `an applicant for registration` or `entered in the general section` | |
| `the_public_benefit_finding` | `Determination of public benefit` | ours has `regard had to the guidance` (Article 5(5)), which the cleanroom does not model: set TRUE for every world; and `treated identified persons as a section of the public`: set FALSE; the determiner is `the Commissioner` |
| "the condition is unduly restrictive" (a fact, world 22) | no field | ours records only whether regard was had to the question; neither encoding lets the fact change an answer (A7), so world 22 maps except for this one fact |
| entity-ness (Article 2) | every entity is `a company`, a Jersey entity | neither the cleanroom nor this comparison tests Article 2 |
| the Order of 5(3) | the Boolean `an Order under Article 5(3) disapplies Article 5(2) for the entity` | |
| office of the Minister | `the Chief Minister` (text of 2 October 2026) | affects only F2.3 reading B |

All 25 worlds mapped; one input (world 22) has a fact with no field.

### 6.3 Result

R0 to R7 in the table are the readings of ours defined in the second table below.

| # | Cleanroom world (shortened) | Cleanroom: meets the test | Ours, favoured: meets the test | Decisions agreeing under the favoured reading (of 8) | Readings of ours under which all 8 decisions agree |
| --- | --- | --- | --- | --- | --- |
| 00 | the St Helier poverty trust + a poverty-relief purpose | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 01 | the poverty trust with a charity shop + an ancillary fundraising | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 02 | the charity shop with nothing behind it + an ancillary fundraisi | FALSE | FALSE | 8 | R0, R1, R3, R4, R5, R6, R7 |
| 03 | the poverty trust with a party-political object + a party-politi | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 04 | the poverty trust with incidental campaigning + an ancillary par | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 05 | the grocery company + a purely commercial purpose | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 06 | the entity with no purposes + a poverty-relief purpose | TRUE | FALSE | 6 | R1, R2, R7 |
| 07 | the entity with no purposes and no benefit + a poverty-relief pu | FALSE | FALSE | 7 | R1, R2, R7 |
| 08 | the disease-prevention trust + a sickness-prevention purpose | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 09 | the pigeon fanciers' association + a spectator-pastime purpose | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 10 | the island swimming association + a physical-sport purpose | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 11 | the members-only tennis club + a members-only recreation purpose | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 12 | the public recreation ground trust + an open recreation purpose | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 13 | the humanist society + a philosophical-belief purpose | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 14 | the Ministerially directed trust + a poverty-relief purpose | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R7 |
| 15 | the Ministerially directed trust exempted by Order + a poverty-r | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 16 | the States-governed foundation + a poverty-relief purpose | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 17 | the Guernsey-governed foundation + a poverty-relief purpose | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 18 | the trust with a Minister in a private capacity + a poverty-reli | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R6, R7 |
| 19 | the dormant registered charity + a poverty-relief purpose | FALSE | FALSE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 20 | the applicant not yet operating + a poverty-relief purpose | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 21 | the grandchildren's trust + a poverty-relief purpose | FALSE | FALSE | 7 | none |
| 22 | the school with an unduly restrictive fee + a poverty-relief pur | TRUE | TRUE | 8 | R0, R1, R2, R3, R4, R5, R6, R7 |
| 23 | the church whose benefit was presumed + a poverty-relief purpose | TRUE | REFUSED | 6 | R3, R7 |
| 24 | the entity whose determiner skipped 7(2)(b) + a poverty-relief p | TRUE | REFUSED | 6 | R3, R7 |

Agreement by reading of ours, over all 200 comparisons (M):

| reading of ours | agree | refused |
| --- | --- | --- |
| R0 favoured interpretation | 192 | 4 |
| R1 F2.1 read as B (an entity with no purposes passes vacuously) | 195 | 4 |
| R2 F2.1 read as C (ancillary alone passes) | 192 | 4 |
| R3 F2.10 read as B (the finding stands) | 196 | 0 |
| R4 F2.10 read as C (treated as no public benefit) | 192 | 0 |
| R5 F2.2 read as B (capacity not required) | 190 | 4 |
| R6 F2.3 read as B (only the defined Minister) | 190 | 4 |
| R7 F2.1 and F2.10 both read as B | 199 | 0 |

By decision, under the favoured reading: E1 22 of 25; E2 23; E3 23; E4 25; E5 25; E6 25; E7 25; E8 24.

The eight disagreements under the favoured reading, with their causes (M):

| world | decision | cleanroom | ours | cause | ours agrees under |
| --- | --- | --- | --- | --- | --- |
| 06 | meets the test | TRUE | FALSE | F2.1: no purposes (provision 5(1)(a)) | F2.1 B, F2.1 C, R7 |
| 06 | 5(1)(a) | TRUE | FALSE | F2.1 | F2.1 B, F2.1 C, R7 |
| 07 | 5(1)(a) | TRUE | FALSE | F2.1 (the headline agrees: both FALSE, for different limbs) | F2.1 B, F2.1 C, R7 |
| 23 | meets the test | TRUE | REFUSED | F2.10: determination made in breach of 7(3)(a) | F2.10 B, R7 |
| 23 | 5(1)(b) | TRUE | REFUSED | F2.10 | F2.10 B, R7 |
| 24 | meets the test | TRUE | REFUSED | F2.10: 7(2)(b) not asked | F2.10 B, R7 |
| 24 | 5(1)(b) | TRUE | REFUSED | F2.10 | F2.10 B, R7 |
| 21 | determination properly made | TRUE | FALSE | scope of "properly made" (section 5, last paragraph) | no reading |

Controls (M).
The harness can disagree: it does, 8 times, and the 8 move with the readings the group provides (R1, R3, R7), which is what a harness that measured the readings and not itself would do.
It is sensitive to inputs: worlds 14 and 15 differ only by the Order flag and give FALSE and TRUE; world 18 flips under F2.2 B (capacity), and world 14 flips under F2.3 B.
It is deterministic: three runs gave identical results.
One parsing slip of mine, found and fixed: the last evaluation in the file carried the trailing `Evaluation[n]` listing into its message and was first read as a refusal; the first summary I printed had one extra refusal for that reason, and every figure above is from the corrected parse.

What this does not show.
It does not test the 32 decisions that I did not compare.
It does not test Article 2.
It says nothing on which reading of the Law is right.
It cannot test the cleanroom's A1, A2, A3, A4 and A12 against ours, because ours has no field that varies them (section 5, D10).

## 7. Judgements I am least sure of

1. **The match of July items to ours (section 4.3).**
   18 rows say "not recorded in ours".
   I searched fragments, `NOTES.md` and module comments by keyword and read six modules; for the other twelve a register entry could have a name I did not think to search.
   The count 16 of 43 is therefore a floor.
2. **The count of "about 39" interpretation calls in July.**
   I counted the `>>>` calls in the headers of ten modules by reading them, separating interpretation calls from deadline policies and from architecture notes.
   Another reader might count 35 or 45.
3. **What counts as "registered" in section 4.2.**
   I excluded the non-fork lists (G2 has 8 items, for example) from the count; including them would move some "one" rows to "two".
   After the 03:13 rewrite of `NOTES.md` I did count its new section 12.3 (the independent authors' ambiguity rows, kept) as part of ours' register, for Q7; I checked every row of that section against my two tables and found no other that matches a cleanroom-only or a July-only item.
4. **The classification of the 136 forks by kind (section 4.1).**
   Mine, by reading each fork's question; 49 "time arithmetic" and 77 "meaning" could each move by a handful.
5. **D4 and D5 (July against ours in Article 4).**
   I read July's code for 4(2)/4(3) and 4(4) and ours' module and fork text, and did not run a discriminating case through July.
   D4 is the one I am least sure of: July's own header call is about the governor carve-out, and I read the further difference (no function nexus for 4(3)) from its rule and its comment "they need not pass the 4(2) gate".
6. **D11 (July and an ancillary purpose).**
   Taken from July's code (`is purely ancillary ...` flag, no gate) and from the cleanroom's diff oracle (C), not from a run of July.
7. **Whether the world-21 "properly made" difference is a difference of definition (section 5).**
   Ours' reading, that a finding which treats such an entity as providing public benefit breaches 7(3)(b), is the more literal; the cleanroom's is a separate bar.
   A domain expert might say they differ in substance.
8. **The vintage statement (section 9).**
   It is measured for the text of Articles 5 to 7 and the definition of "Minister"; for the rest of the Law it rests on the Table of Legislation History and on R&O.102/2026.

## 8. F. What each has that the others lack

Plain statements; no ranking.
Items marked M were found by looking in the three trees.

**Ours has, and neither predecessor has (M):**
- Every Article and Schedule as a row in a coverage table (851 rows), with a disposition and a module for each; July says only that "there are no silent gaps".
- The commencement and text-of-the-law layer: nine consolidated texts, three stages of commencement, and headline functions that refuse by name for a day before a unit was in force or before the first consolidated text.
- A typed record of readings for each group (136 fields in 9 records), each field with the other readings callable and a test for each, and a "red" file per group that states the discriminating case under the reading taken.
- Mechanical checks in `check.sh`: every quotation and locator against the Law's text (`srcrefs.py`: 1,724 `src:` lines, 1,666 locators, 0 problems in my 03:02 run), a shape check on the import graph, and the trace checker that reads each `-- EXPECT:` comment against `l4 run --json`, with a positive control (NOTES section 11.3).
- A register of 35 conflicts, slips and commencement oddities, and 71 open-question bullets for an expert, with discriminating cases; and, in `NOTES.md` section 12.3, every assertion of the independent authors that did not pass, with its provision and disposition.
- Six headline questions that cross the groups (application, register, contravention, offence and penalty, text in force, appeal), answered by 13 integration-layer `@export`s whose every input has an `@desc` (the integrator's check; the other 454 `@export`s are in the group modules).
- Mutation testing claimed by the groups (G2 42 mutants, G3 97, G5 52, G4 28 rows, G6 a sweep) and 16 by the integrator.
  I did not re-run any.
- An independent test pass: 32 modules by three independent authors (1,769 assertions satisfied, 16 failed and 10 refused on purpose, where the failure or refusal is the finding), which appeared in the deposit between my two copies.
  I report only their `check.sh` counts and did not read them.

**Ours lacks, and a predecessor has (M):**
- NLG: the cleanroom has `tests/charity-test.nlg.golden`; ours has no `@nlg` and no golden file.
- A projection: the cleanroom has a DMN with 40 decisions and 2 input data, the engine runs on KIE and Camunda (neither executes it), and an account of why (`PROJECTIONS.md`).
  Ours has none; the integrator notes that no `@export` was tried through `l4 export` or the service (`NOTES.md` section 14).
- A pinned case file: 25 worlds by 40 decisions, each value evaluated by the L4 binary.
  Ours has answer tables in prose and tests, but no case file in the same form.
- An independence audit and a "where this is most likely to be wrong" section: the cleanroom's `README.md` section 6 and 7.
  Ours has no provenance section yet (`NOTES.md` section 15 still reads "to be written by the launching session").
- A report for drafters (July): a 21-page PDF in plain language with sidebars that teach the logic, a 6-page companion of annotated excerpts prepared for CALC 2026, and a list of findings framed as questions to a drafter ("is this worth a tidying amendment?").
  Ours has `NOTES.md`, which is written for a maintainer.
- A different place for the statute's words: July and the cleanroom carry them inside the expressions as inert strings joined by `...` and `..`, so the left margin of a rule reads as the Article.
  Ours carries them in `-- src:` comment lines and `@ref` locators above each rule (checked mechanically against the Law's text) and uses short inert labels such as "(i)" inside the expressions; I did not judge which is easier to audit.

**None of the three has (M, by search of each tree's documents):** a web wizard, a ladder diagram of the logic, a docassemble or OpenFisca or Catala output, or a service deployment.
(The cleanroom's DMN carries one DMN diagram element, `PROJECTIONS.md:120`; I mean a diagram of the logic that a reader would study.)

**Test counts, side by side (M; ours at 03:02).**
Assertions: 754, 102, 7,953 (6,110 at 02:30).
Assertions per 100 lines: 5.9, 7.1, 14.1.
Traces: 156, 0, 976.
Kept-failing assertions that state what the Law seems to say where the readings taken do not deliver it: 0, 0, 156 (134 in the groups' red files, 6 in the integrator's, 16 in the independent authors' files), and 10 deliberate refusals in the independent authors' files.

## 9. Vintage: what the difference between the texts can explain

The July corpus and the cleanroom read the text showing the law from 16 October 2025; ours reads 2 October 2026.

What differs (M).
The Table of Legislation History in the 2 October 2026 text lists two amending instruments after the 2024 ones: R&O.56/2025 (16 October 2025) and R&O.102/2026 (2 October 2026).
R&O.102/2026 mentions the Charities (Jersey) Law 2014 once, in its Article 1: in Article 1 (interpretation), "Minister for External Relations" is replaced by "Chief Minister".
So between the two texts the only amendment is the definition of "Minister".
I checked this against the text itself for Articles 5 to 7: of the 133 blockquoted paragraphs in the cleanroom's `SOURCE-EXTRACT.md` (taken from the 16 October 2025 text), 132 appear verbatim, after normalising quotation marks and spacing, in the 2 October 2026 text, and the one that does not is `"Minister" means the Minister for External Relations;`.
I could not check the rest of the Law the same way, because the 16 October 2025 consolidation is not in any tree I may read.

What I can attribute to the vintage difference (J).
In July and the cleanroom, nothing computed depends on which office "the Minister" is: July names it only in a comment (`charities-common.l4`), and the cleanroom quotes the definition as inert text (`charity-test.l4:70`).
Both are now stale by one phrase and no answer changes.
In ours, the office matters only on the second reading of F2.3 (the "Minister" of Article 5(2)(a) as the defined office): reading B bars a constitution that permits the Minister for External Relations on the text of 16 October 2025 and not on the text of 2 October 2026, and the group tests it (`NOTES.md` section 6.5).
In my run, world 14 flips under F2.3 B for a different reason (the harness gives "a Minister" no office).

What I cannot attribute to the vintage difference.
Every difference in section 5 and in the registers of section 4: none of them depends on a provision that changed.
The differences between July and ours outside Articles 5 to 7 are differences between encoders, and where the provision is in a part both read, they are differences of reading.
The one place the texts may differ beyond what I could check is any editorial change the consolidation made outside the amending instruments (`NOTES.md` section 9 says this is unknown).

## 10. What I could not do, and why

- I did not re-run the cleanroom's diff oracle or its 2,115-row batteries: the oracle (`etc/go/lib/denovo-diff.mjs`) is on a branch of the repository that I did not check out, since I was to change no checkout, and the cleanroom's `COMPARISON.md` already reports 99.07% agreement of the cleanroom with the July corpus on 21,420 evaluations and four root causes, which I use as the baseline.
  Its four root causes are 6(2)(e) (D10 here), the ancillary purpose with nothing behind it (D11), "acting in that capacity" as a field (Q13) and the applicant's intention limb (Q11).
- I could not run July's modules on a discriminating case of my own for D4 to D9 and D11; those rows rest on reading its code.
- I could not obtain the 16 October 2025 consolidation; see section 9.
- I obtained a green run of the whole deposit only on the second copy (03:02); the first (02:30) was red in its integration layer (section 0).
  The deposit was still changing, so a later `check.sh` may differ from both.
- I did not run any `@export` through `l4 export` or the service.
- No lawyer has read any of this, and I have not tested any reading against the Law's meaning.

## 11. Commands and files

All under `FLEET_DIR/work/compare/`; `FLEET_DIR` is as in the brief.
Nothing outside that directory was written, and nothing in `deposit/` was touched.

| what | how |
| --- | --- |
| July corpus extracted | `git -C /Users/mengwong/src/legalese/l4-ide archive origin/unstable paper/case-studies/charities-jersey-2014 \| tar -x -C july` (`origin/unstable` was `0a9d0474d`) |
| July run | `scripts/run-july.sh` (`nice -n 15 l4 run <module>.l4`, one at a time, `JL4_LIBRARY_PATH` unset); outputs in `july-run/`; counted by `scripts/count-l4out.py` (assertions counted from `Message:` blocks and from unique file and range: equal) |
| July PDFs | `pdftotext -layout` into `july-pdf/`; `scripts/pdfdiff.py` compared the report PDF to `README.md`: word-level ratio 0.9963, no run of 8 or more words in the PDF that is not in the README |
| Static counts | `scripts/metrics.py <label> <files>` for all three |
| Copy of the deposit | `cp -R deposit run/deposit-snap` at 02:30:44 and `run/deposit-snap2` at 03:02:35; hashes in `run/deposit-snap.sha256` and `run/deposit-snap2.sha256` |
| Ours, full check | `L4=bin/l4 RAW=inputs/charities-jersey-law-2014-2026-10-02.txt nice -n 15 ./check.sh` in each copy; output in `run/check-snap.out` (02:30, RED) and `run/check-snap2.out` (03:02, GREEN) |
| Coverage | `data/table-coverage.md` from `coverage-all.tsv` and `phase1/coverage.tsv` by `scripts/tables.py` |
| Registers | `data/zone1-arts5-7.tsv`, `data/zone2-july-vs-ours.tsv` (written by hand from the reading described above); counts by `scripts/tables.py` |
| Fork kinds | `scripts/fork-classes.py` |
| Vintage check | `scripts/vintage-check.py` (cleanroom `SOURCE-EXTRACT.md` blockquotes against the 2 October 2026 text) |
| Cleanroom run | `l4 run charity-test.l4` in `run/cr/`: 102 satisfied, 0 failed, 0 other diagnostics |
| E harness | `scripts/gen-harness.py` writes `run/e/cmp-harness.l4` (1,600 `#EVAL`s) and its index; `l4 run`; `scripts/parse-harness.py`; `scripts/summarise-e.py`; `scripts/table-e.py`; probe in `run/e/cmp-a5.l4` |
| This file | `COMPARISON.template.md` filled by `scripts/build.py` from the data files |

## 12. Re-read at the end of the work

There were two re-reads.
The first was at 03:10, before the integrator finished; the second was at about 03:23, after the lead reported the finished deposit and `NOTES.md` rewritten at 03:13:28.

### 12.1 First re-read, 03:10

I compared the 02:30 copy of `FRAGMENT-G2.md` section 2 and `NOTES.md` section 5 with the live files, and the hashes taken at 02:28 with the live hashes (M).
`FRAGMENT-G2.md` section 2 had eight changed lines in four pairs, all rewording: the "Provisions" and "Not subject to the fork" lines of F2.10 now say that 7(1) names the Commissioner, the Tribunal and the court and that F2.13 adds the Commissioner's staff on its first reading, and the "Readings" and "Representation" lines of F2.13 were reworded and shortened.
The 13 fork headings, their questions, their readings and the reading taken in each were unchanged.
`NOTES.md` was then byte-identical to its state at 02:28 and still listed 135 forks and 12 for G2.

### 12.2 Second re-read, about 03:23, of the finished deposit

**The code.**
All 162 `.l4` files of the finished deposit are byte-identical to my 03:02 copy (`cmp` on each file; no file only in one place) (M).
The only files that differ from the 03:02 copy are `NOTES.md` (written 03:13:28), `README.md` and `encoding.json`.
So every measurement of the code in this report, including the E results and the `check.sh` run of 03:02, stands for the finished deposit; I did not need to re-run them.

**What I re-read in the finished `NOTES.md` (now 15 sections), and what I found.**

| section I had cited | finished `NOTES.md` | effect on this report |
| --- | --- | --- |
| 5, fork index | now 136 forks (G2 13), F2.13 added, the other 135 rows byte-identical to the old table; the question column of all 14 G7 forks is still empty | the fork count I used (136) is now the file's own; the statement that the file was stale is withdrawn; the empty G7 questions remain true |
| 4, coverage | section byte-identical; 851 rows and the group table are unchanged; `coverage-all.tsv` unchanged | none |
| 6, consistency register | items 6.1 to 6.12 kept, a new 6.13 (staff and F2.13), and a paragraph on the empty `kinds of entity` guard in G2 and G7 | none to a figure |
| 7, contradictions | S35 added (Article 7(1), 5(5), Schedule 1 4(3): the F2.13 question); the old list was S1 to S34 | 34 entries became 35 (25 that change an answer, 3 commencement, 7 slips; was 24, 3, 7) |
| 8, open questions | three bullets added (staff and Article 7; the text of "Minister", "Comptroller" and the kinds of entity before 1 January 2019; which Part the original Article 41 stood in) | open-question bullets 68 became 71 |
| 9, what the sources do not answer | two bullets added; the sentence I cited, that whether the consolidated text equals the enacted text is not known, is unchanged (now at line 905) | none |
| 10, answer table | new 10.8 (`int-tests-repairs.l4`, 48 assertions R1 to R6) | none to a figure of mine; `int-tests-repairs` is among the 27 integration modules I counted |
| 11.1, `check.sh` table | now 162 modules, 7,787 satisfied, 156 failed (expected 156), 10 refused (expected 10), `srcrefs` 1,724 lines / 1,666 locators / 0 problems, 976 traces; the lead's clean copy gave the same, 5 minutes 19 seconds | equals my 03:02 run on every figure; the sentences that called the table stale are replaced |
| 11.3, trace checker and positive control | present | none |
| 12, independent tests | new section: 1,769 satisfied, 16 failed, 10 refused, 59 traces; the authors' frozen expectations are in `work/ind-*`, which I did not read | equals my counts from `check.sh`; its section 12.3 records "who Article 7 binds" (A-14 from ind-b and A7-01b from ind-c, "ambiguity kept") |
| 13, defects | now 13.1 repaired (including ic-D2/ib-A14 = F2.13, ib-V20, ib-E6-2d4), 13.2 found and not repaired, 13.3 notes | none; what I called "section 13" for the `l4 export` remark is now section 14 and I changed the reference |
| 14 / 15 | section 14 is "what is not wired" (the `@export` functions were not exercised through `l4 export` or the service: unchanged); section 15, provenance, still reads "to be written by the launching session" | section numbers corrected in this report |

**What changed in this report as a result (old figure, new figure).**
- Statements that `NOTES.md` was stale or not rewritten (sections 0, 2, 4.1): replaced by the facts above.
- S-register entries: 34 became 35; the number of entries that change an answer: 24 became 25.
- Open-question bullets: 68 became 71.
- Cleanroom question Q7 (who Article 7 binds): "not recorded in ours" became "recorded in `NOTES.md` section 12.3 (A-14, A7-01b), kept, not a fork".
  That moves the Articles 5 to 7 split from 1 / 4 / 15 to 1 / 5 / 14 (all three / two / one), the cleanroom-only questions from 8 to 7, and the headline D count from eight (plus three one-sided) to nine (plus two one-sided): the "who Article 7 binds" row moved from the one-sided table (was D10) to the main table (now D3), and the later rows were renumbered.
  The reading, the probe and the discriminating case did not change.
- The harness decisions were relabelled E1 to E8, because "D1 to D8" clashed with section 5; no figure changed.
- References to `NOTES.md` sections 13 and 14 became 14 and 15.

**What did not change:** every figure in sections 2, 3 and 6 (size, coverage, the 192 of 200 and 199 of 200), the vintage statement, and every other row of the register tables.
