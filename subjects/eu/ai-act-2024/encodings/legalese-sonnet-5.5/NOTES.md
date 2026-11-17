# NOTES: Regulation (EU) 2024/1689 (the AI Act) as amended by Regulation (EU) 2026/1744, whole Regulation, nine seats

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the Official Journal.
The text it quotes is a Publications Office consolidation, a documentation tool with no legal effect, rendered to plain text by a script (section 'The source').
Written on 2026-11-17 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel, between 08:29 and 12:53 UTC by the first and last timestamps in their transcripts. The lead agent of the session that ran them merged the result.
Built with `l4` 1.6.110 (main, e51181d, 2026-11-11) and compared with `l4` 1.6.109 (main, 4c887e0, 2026-11-04); every module has the same four counts on both builds (section 'What check.sh prints').

## Where the rulings come from

The agents were told to read the Guide for encoders, `docs/ENCODING-GUIDE.md` of this repository, and each part's fork lines cite it by the Guide's line numbers in the copy the agents were given (`inputs/ENCODING-GUIDE.md`).
That copy is byte-identical to `docs/ENCODING-GUIDE.md` at commit fca22c14b of this repository (checked with `cmp` when this file was written).
The lines cited: line 86 (a function answers `JUST FALSE` only where the text itself says no in its own words), line 87 (everywhere else `NOTHING`, including where a grant or prohibition is limited in its own wording and the case falls outside the limit), line 93 (the periods, "where" and scope-limits ruling of 2026-11-05, items (a) to (c)), line 94 (the delegated-definitions, defences and "until" ruling of 2026-11-05, items (a) to (d)) and line 95 (six questions with no convention, decided case by case with one fork line each).
**One ruling the parts cite is not in the Guide**: the grant and power name test, ruled by the coordinating session on 2026-11-12 and recorded in the NOTES of the UK Companies Act encoding, section 'The grant and power name test' (`subjects/uk/companies-act-2006/encodings/legalese-sonnet-5.5/NOTES.md`, merged as commons#95).
It has three limits: flip to `NOTHING` a function named for a grant or a power that answers `JUST FALSE` because an `if` gate failed; keep `JUST FALSE` where the text closes the gate itself; list for a lawyer a "may" gated by "where", "when" or "upon", and the functions named "entitled".
It is the coordinating session's ruling, not a ruling written into the Guide; the Guide does not mention it (no line of `docs/ENCODING-GUIDE.md` contains 2026-11-12).
In the parts' notes, "brief line N" and "the brief's grant ruling" mean the copy of the brief the agent was given, kept as `notes/<part>-BRIEF.md`; "line N" with "Guide" means the Guide.

**Everything marked "assumed, not ruled" in this folder was decided by the encoder or the lead, not by the maintainer.**
The scope, the version and the method (below) were set by the coordinating session on 2026-11-17 and are also assumed, not ruled.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`aia-core.l4`, `aia-timeline.l4`, `aia-definitions.l4`, `aia-scope.l4`, `aia-literacy.l4`, `aia-annex-x.l4`, each with a tests module where it has one) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it takes from the others. The keel is 11 modules in the gate.
Nine **part** agents then encoded their ranges in parallel, each against the same keel, none reading another's work.
The ranges are lines of the consolidated text (`eu-ai-act-2024-1689-consolidated-20260727.txt`), copied from `notes/keel-PLAN.md` section 6:
- `P1` (lines 170-261, 1671-1754): Article 5 (prohibited AI practices), Article 6 (classification as high-risk), Article 7 (amendments to Annex III), Annexes I, II, III. The title of Annex II says it lists the criminal offences referred to in Article 5(1), first subparagraph, point (h)(iii).
- `P2` (lines 156-169, 262-373, 1755-1782): Article 4a (special categories of personal data for bias detection), Articles 8 to 15 (requirements for high-risk AI systems), Annex IV.
- `P3` (lines 374-526): Articles 16 to 27 (obligations of providers and deployers of high-risk AI systems and other parties; quality management; documentation; logs; corrective actions; authorised representatives; importers; distributors; responsibilities along the value chain; deployers; fundamental rights impact assessment).
- `P4` (lines 527-635, 1800-1839, 1958-2010): Articles 28 to 39 (notifying authorities and notified bodies), Annex VII, Annex XIV.
- `P5` (lines 636-748, 1783-1799, 1840-1886): Articles 40 to 49 (standards, conformity assessment, certificates, registration), Annexes V, VI, VIII, IX.
- `P6` (lines 749-842, 1908-1957): Article 50 (transparency obligations), Articles 51 to 56 (general-purpose AI models), Annexes XI, XII, XIII.
- `P7` (lines 843-1112): Articles 57 to 63 (sandboxes, real-world testing, measures for SMEs; including 60a), Articles 64 to 70 (governance: the Board, advisory forum, scientific panel, national competent authorities), Article 71 (EU database).
- `P8` (lines 1113-1313): Articles 72 to 79 (post-market monitoring, serious incidents, enforcement, market surveillance, the AI Office's powers (75a to 75d), testing supervision, powers of authorities protecting fundamental rights, confidentiality, national-level procedure).
- `P9` (lines 1314-1617, 1628-1653): Articles 80 to 98 (procedures, remedies, right to explanation, supervision of general-purpose AI providers, codes of conduct, guidelines, delegation, committee), Articles 99 to 101 (penalties and fines), Articles 102 to 110 (amendments of other acts), Article 112 (evaluation and review).
A tenth agent, `P0`, wrote the seat questions for the keel's own provisions (Articles 2, 3, 4, 111 and 113); its questions are the first banner in each seat module.
The lead verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the keel's modules identical to the keel's) and then merged them with a script that is not shipped.
After the parts returned, these were done:
1. a **seat-question audit**, by each part's own agent, reading each seat question against the body of its function (section 'The seat-question audits');
2. a **name test for functions named for a grant or a power** (section 'Where the rulings come from', and each part's fork register);
3. an **independent test pass** by three readers who saw only the text and the modules (section 'The independent test pass');
4. the **follow-up passes** the readers' findings called for, made by the part agents; the keel's Article 111 date functions were also tried with a gate and the attempt was reverted (section 'The time axis');
5. a **differential** against two earlier encodings of parts of this Regulation (section 'The differential');
6. the lead's **carry-over checks**: the comment scrub, `etc/check-not-precedence.mjs`, `srcrefs.py`, a check that every `#TRACE` does what the `-- EXPECT` comment above it says, and the **merged gate** (section 'What check.sh prints').
Every note a part wrote is kept, with the maintainer's and the coordinator's names and local paths replaced by placeholders, as `notes/<part>-NOTES.md`, with its `PROGRESS.md` and, where it wrote one, its `NEEDS-CORE.md`; the keel's are `notes/keel-*.md`, and the brief each agent was given is `notes/<agent>-BRIEF.md`.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations, seams, split sites and findings are.** They are not repeated or summed here, except as the sections below say.

## Merge decisions (assumed, not ruled)

- **One seat module per seat.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into nine seat modules (`aia-seat-<seat>.l4`) and nine cases modules (`aia-cases-seat-<seat>.l4`), one banner comment per part; the text under each banner is the part's, unchanged. The seats are person, provider, deployer, importer, distributor, rep, manufacturer, gpai and notified.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering provision (each part's notes have a Seams section). The merge does not wire one part's output into another's input, so a seat asks the person each such fact.
- **NEEDS-CORE requests are not hoisted.** They are gathered in `NEEDS-CORE.md` (proposed, not landed); the keel is the keel's, unchanged.
- **Part-local types and helper names stay where they are.** Every top-level name carries its provision label or its part prefix; the nine seat modules import every part module they need and compile in the gate, so no two modules that are imported together define the same name.
- **Cosmetic names were not renamed.** A few helper names do not carry a provision label (`Arts 8 to 15 harmonisation facts`, `Arts 8 to 15 gate`, `Section 3 circumstances`, `Section 3 gate result`, `Arts 72 to 79 party`, and the plural seat names). Renaming them was judged a risk for no gain; they are listed so a reader does not take them for provisions.
- **The merge edited one rule, found by the lead's sweep and not by any test.** In four duty rules of `P9-art-112.l4` (Article 112(2), (3), (6) and (7)) the guard read `NOT (group applies) OR n AT MOST 0`; `NOT` takes the whole expression after it, so it parsed as `NOT (group applies OR n AT MOST 0)` on both builds (measured on a four-line probe on 1.6.110 and 1.6.109). With a report number of 0 or less the rules took the duty branch where the line beside them says nothing is owed. The guard now reads `(NOT (group applies)) OR n AT MOST 0`, and four `#TRACE`s at number 0 were added to `P9-tests-art-112.l4`; run against the file as it stood before the edit, the four traces end in a breach where `-- EXPECT FULFILLED` says nothing is owed. No other line of any rule changed in the merge. The edit is in the merged folder only, not in the part's own deposit.
- **Comments were scrubbed, rules were not:** names and local paths were replaced by placeholders in `.l4` comments and in the notes, and it was proved line by line that no code part of any `.l4` line changed (the scrub tool compares each line outside its comment).

## The source

The text is `../../registers/source-bundle/eu-ai-act-2024-1689-consolidated-20260727.txt` (2,021 lines, sha256 of the plain text `f3bd1086fd086b339cab17c3e31ab393968c1ae179d60f2773b687e4c9118bdc`), a plain-text rendering, made by a script (`xhtml_to_text.py`, in the same folder, sha256 `3c9fae9fb3f7b8b1da253d110d17704ca51a20efcd6afcf61c4f393c2a748d23`), of the Publications Office consolidated version of Regulation (EU) 2024/1689, CELEX `02024R1689-20260727`, which includes the amendments made by Regulation (EU) 2026/1744.
The XHTML it was rendered from (sha256 `5e7719f77e8a606b257dc25958ee3222c4383300a5a34270a5b850a2ce8b8715`, 851,286 bytes) was fetched on 2026-11-17; the fetch record is `../../registers/source-bundle/eu-ai-act-2024-1689-consolidated-20260727.meta.json`.
The consolidated version says of itself that it is a documentation tool with no legal effect; the Official Journal text is authentic. Nothing here is claimed verified against the Official Journal.
**Versions.** The version in force from 27 July 2026 is the text as amended; the encoding carries both versions on a rule-version axis (the time axis, below). Later dated consolidations were **not enumerated** (the fetch record says two web searches on 2026-11-17 found no further amending act, which is not an enumeration).
The text as enacted of the provisions the Omnibus changed is in `eu-ai-act-2024-1689.txt` and the Omnibus's own text in `eu-omnibus-2026-1744.txt`, both in the same folder; a quotation of the as-enacted wording carries the file and line it was taken from.
**Scope** (assumed, not ruled): Articles 1 to 113, with 4a, 60a and 75a to 75d, and Annexes I to XIV; recitals are not encoded. **Commencement is IN**, against the Guide's section 4, which would put it out; the coordinating session's brief for this Regulation said so.
The fetch record's own comparison of the consolidation with the two Official Journal texts is in its `checked` field; it is a reading-aid check, not a verification.

## The time axis

The keel has the time axis; every part uses it. `Omnibus Art 4 the version in force` gives the version from the date asked (the text as enacted before 27 July 2026, as amended from it); `Art 113 the provision group applies` says whether a provision group applies on the date asked (seven groups, each with the date Article 113 gives it, as enacted and as amended), and it takes Article 111(2) into account.
**Layer-1 functions answer `NOTHING` before their provision applies** (a function of this encoding that returns a truth value answers `JUST TRUE`, `JUST FALSE` or `NOTHING`; a regulative rule reads as nothing owed, `FULFILLED`, before then). By the coordinating session's design, each seat has, for each group, a question "does <group> apply on the date asked?" that answers `JUST TRUE` or `JUST FALSE`, so seat applicability answers `JUST FALSE` before the date and a substantive function answers `NOTHING`. That is a design decision, recorded here and not ruled.
- **F-113-groups.** Chapter III Section 5 (Articles 40 to 49) is dated by no point of Article 113 as amended, so the second paragraph's general date (2 August 2026) was applied to it. Part P5 ran a gap test on that reading; its entry is in `notes/P5-NOTES.md`. Assumed, not ruled; for a lawyer.
- **F-111-2-nothing.** A high-risk system placed on the market before 2 August 2026 and not significantly changed is saved from the Regulation by Article 111(2); every function that asks whether the provision applies to it answers `NOTHING` (the keel's reading, not decided again by any part). The Guide's line 86 would, on its words ("only if"), give `JUST FALSE`; the coordinating session ruled to keep `NOTHING`. Each part's notes count its functions that this reaches (section 'Split sites', item (iii)).
- **Articles 111 and 113 date functions answer from entry into force.** The keel's Article 111 date functions answer from the Regulation's entry into force; the other reading is `NOTHING` before 2 August 2026 (Article 111(3) can be read as purposive). The lead asked the keel to gate them, and the keel did, but the gate broke part P6's Chapter V functions, which depend on the Article 111(3) date (56 assertions, and 55 seat cases of P0), so the change was reverted from snapshots, and all modules were gated again. The lesson, recorded here so it is not repeated: grep a keel function's callers before instructing a keel change.

## The seats

There are nine seats: `person`; `provider`; `deployer`; `importer`; `distributor`; `rep`; `manufacturer`; `gpai`; `notified`. There is never a seat for the Commission, the AI Office, the AI Board, the scientific panel, a market surveillance authority, a notifying authority or any other official; their powers and duties appear only as what they mean to one of the nine (`notes/keel-PLAN.md`, section 8).
A seat question is a function marked `@export` with `@desc` on its inputs, named `Under Article N, as <role phrase>, ...` and answering in the direction its name asks. The merged seat modules hold these questions, counted from the files:

| seat | questions (`@export`) | case lines (`#ASSERT`, `#TRACE`, `#EVAL`) in the cases module |
| --- | --- | --- |
| `person` | 81 | 450 |
| `provider` | 461 | 2520 |
| `deployer` | 218 | 1021 |
| `importer` | 81 | 330 |
| `distributor` | 67 | 288 |
| `rep` | 87 | 412 |
| `manufacturer` | 78 | 357 |
| `gpai` | 109 | 604 |
| `notified` | 169 | 891 |
| all nine | 1351 | 6873 |

The seat layer asks the person the facts a role could state: the date asked, when the system was placed on the market, whether its design has been significantly changed since Chapter III began to apply, and which route makes it high-risk (Article 6(1) with Annex I, Article 6(2) with Annex III, or neither). It does not decide the route for them; a caller can compute it with part P1's functions.

## What check.sh prints

`check.sh` was run on the merged folder as `L4=<l4 1.6.110 (main, e51181d, 2026-11-11)> L4_MAIN=<l4 1.6.109 (main, 4c887e0, 2026-11-04)> ./check.sh`, with `JL4_LIBRARY_PATH` unset, and exited 0. The full output is `notes/check-output.txt`; the totals:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
TOTAL (190 modules)                            0     16982       0        0           |      0     16982       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

190 modules, 16,982 assertions satisfied, 0 errors, 0 failed, 0 refused, and the main-build columns equal the stable-build columns for every module.
By group (read from the same log):

| group | modules | assertions satisfied |
| --- | --- | --- |
| keel | 11 | 641 |
| P1 | 14 | 856 |
| P2 | 22 | 1,092 |
| P3 | 24 | 652 |
| P4 | 17 | 826 |
| P5 | 12 | 1,003 |
| P6 | 10 | 740 |
| P7 | 12 | 1,224 |
| P8 | 26 | 997 |
| P9 | 21 | 765 |
| seat questions | 9 | 0 |
| seat cases | 9 | 6,807 |
| independent | 3 | 1,379 |
| total | 190 | 16,982 |

**What `check.sh` does not see, and what was done about it.**
It counts assertions and does not read `#TRACE` outcomes or the `-- EXPECT` comments above them (loud failure: none; silent: a trace that ends differently from its comment passes the gate).
Two instruments cover the traces, both run by the lead and neither shipped. One, run on each part's deposit before the merge, compared every `#TRACE` outcome between the two builds (identical in every deposit). The other, run once on the merged folder on build 1.6.110 (main, e51181d, 2026-11-11), compares each `#TRACE` with the `-- EXPECT` comment directly above it: 1,799 traces, 1,791 with such a comment and all of them matching, 8 without one directly above (eight consecutive traces in `P1-tests-art5-rbi.l4` that the group comment above them covers; each prints an open duty, as that comment says), 0 mismatches.
Before the lead wrote that instrument no machine check of those comments existed, so for the merged folder this is their first check.

## The seat-question audits

Each part's agent audited its seat questions in a second pass, reading each question's name against the body of its function for direction (a question named for a duty must answer about that duty, not about its negation) and for subject (the party and provision the name says). No further audit was run after the later follow-up passes; the parts' question counts below are those of the audit, and the merged seat modules hold the same number of questions (counted from the files, section 'The seats').

| part | questions read | retitled | of which direction | of which subject | where |
| --- | --- | --- | --- | --- | --- |
| P0 | 158 | 5 | 0 | 5 | `notes/P0-NOTES.md:92` |
| P1 | 86 | 0 | 0 | 0 | `notes/P1-NOTES.md:308` |
| P2 | 121 | 3 | 0 | 3 | `notes/P2-NOTES.md:400` |
| P3 | 128 | 0 | 0 | 0 | `notes/P3-NOTES.md:537` |
| P4 | 174 | 3 | 0 | 3 | `notes/P4-NOTES.md:831` |
| P5 | 144 | 0 | 0 | 0 | `notes/P5-NOTES.md:986` |
| P6 | 120 | 5 | 4 | 1 | `notes/P6-NOTES.md:722` |
| P7 | 73 | 4 | 0 | 4 | `notes/P7-NOTES.md:1050` |
| P8 | 260 | 8 | 0 | 8 | `notes/P8-NOTES.md:743` |
| P9 | 87 | 0 | 0 | 0 | `notes/P9-NOTES.md:675` |
| all | 1351 | 28 | 4 | 24 | |

## The independent test pass

Three readers (Sonnet 5.5 agents) each saw only the text and the modules of the parts allotted to them, and wrote tests from the text alone, then ran them and triaged each failure as ENCODER (the encoding answers wrongly), SCENARIO (the reader's expectation was wrong), AMBIGUOUS (the text reads two ways) or GAP (no function can be asked the question). Each reader's prompt, triage and as-returned test file are in `notes/independent/`.

| reader | assertions | failing as returned (the reader's own heading) | restated after triage (lines marked `RECONCILED 2026-11-17`) | satisfied now |
| --- | --- | --- | --- | --- |
| `tests-independent-g1.l4` | 444 | 22 | 22 | 444 |
| `tests-independent-g2.l4` | 441 | 39 | 44 | 441 |
| `tests-independent-g3.l4` | 494 | 20 | 16 | 494 |

The readers' own tallies are in their triage files; the numbers of failures as returned are read from the readers' own headings, not re-counted. The count of restated lines can differ from the failures as returned: a line was also restated when a part's follow-up pass changed a function's inputs. In g2, 8 of the restated lines are of that kind (each says so: part P5's second follow-up replaced an input).
A restated line carries the reader's original expectation and the reason; the lead restated a reader's expectation to the encoding's answer only for a SCENARIO or AMBIGUOUS verdict, or for an ENCODER verdict that the part's own fork line settles (`ENCODER-SETTLED`: no answer changed). An ENCODER verdict that the text did not settle was sent to the part's agent, which changed the encoding (the follow-up passes); the reader's assertion then passed without restating.
**Disclosures about the readers' independence.** Reader g2 read the function bodies in `aia-core`, `P4-gate`, `aia-timeline`, `P4-art-28` and `P4-annex-vii` before writing tests, and `P7-governance.l4` lines 385 to 392 and 474 to 490 and `aia-annex-x.l4` lines 10 to 60, and after its run the bodies of the failing functions; it never opened a brief. Readers g1 and g3 opened nothing forbidden; g3 opened `.l4` files for names and types and ran `#EVAL` probes. A reader that has seen a function's body is not independent of it for that function.
**The readers do not cover everything:** 20 gaps in g1, 26 in g2 and 26 comment lines (covering 42 scenarios) in g3, as the readers wrote them, are questions the encoding cannot be asked; they are the GAP list of this encoding (the triage files give each).

## The differential

Two encodings of parts of this Regulation were made before this one, each by a single agent working alone: `subjects/eu/ai-act-2024/encodings/solo-2026-10` (serious-incident reporting by providers, Articles 3, 20(2), 51, 52(1), 55(1)(c), 73, 75(1a), 99, 101, 111 and 113) and `subjects/comparative/ai-content-labelling/encodings/legalese/eu-ai-act-art50.l4` (Article 50(2) and (4), the definitions they use, and the dates).
Their notes and code were not given to any agent that wrote or tested this encoding, and each of those agents reported that it opened nothing outside its own folder (one reported that a process listing showed other runs' command lines, and opened no file).
The lead of this encoding read them after every part had returned, and compared the answers below.
**The comparison is not blind for Articles 111 and 113**: the lead had read the first 60 lines of `aia-dates.l4` of `solo-2026-10` earlier in the run, so for those two Articles the agreement below is with a text the lead had seen, not independent agreement.
The comparison was made by running this encoding's functions on the facts the earlier encoding states and reading the answer, and, where it was cheaper, by reading this encoding's own function and notes.
It is a spot check of the points below, not a differential over every function; it checks nothing outside them.

#### Against `solo-2026-10`: agreements

| point | the earlier encoding | this encoding | how checked |
| --- | --- | --- | --- |
| Article 73(2), general serious incident | 15 days after becoming aware | 15 | a function run |
| Article 73(3), widespread infringement or point (49)(b) incident | 2 days | 2 | a function run |
| Article 73(4), death | 10 days | 10 | a function run |
| Article 73(3) and (4) both apply | the earlier limit, 2 days | 2 | a function run |
| Article 73(8) | within seven days from receipt | receipt plus 7 | a function run |
| Article 52(1) | within two weeks after the requirement is met or becomes known | `PLUS 14` in `Art 52(1) the provider notified the Commission without delay and within two weeks` | the function read |
| Article 55(1)(c) | no period stated | the rule has no `WITHIN` | the rule read |
| Article 73(5) and (6) | no period stated | no `WITHIN` in the functions and rules of `P8-art73.l4` for them | the file read |
| Article 51(2) threshold | the exact literal `10_000_000_000_000_000_000_000_000`, not `EXPONENT` | the same literal | the function read |
| dates of application | Chapter I 2 February 2025; Chapter III Section 4, Chapters V, VII, XII and Article 78 from 2 August 2025; the general date 2 August 2026, Article 101 included | the same, from `Art 113 as amended the date of application` | a function run |
| Chapter III Sections 1 to 3, as amended | 2 December 2027 (Annex III), 2 August 2028 (Annex I) | the same | a function run |
| Article 111(2) date, Article 111(3) date | 2 August 2030, 2 August 2027 | the same | a function run |
| Article 111(2) saving (their fork F3, finding 5) | as amended, a high-risk system placed before the Chapter III date and not significantly changed is outside the Regulation, for both routes | `Art 113 the provision group applies` answers `FALSE` for the group `General` on those facts and `TRUE` once the placement date is on or after the Chapter III date or the design changed significantly | a function run |
| Article 101 and SMEs (their finding 6) | no reduction for an SME | `Art 101(1) the ceiling in euros of the fine on the provider` takes no SME input; the lower-of rule is in `Art 99` only | the functions read |
| the text as enacted for Article 73 never applied (their finding 4) | the Omnibus entered into force on 27 July 2026, before 2 August 2026 | the same reading in `notes/P1-NOTES.md` (Versions) and in the keel's version function | the notes read |

#### Against `solo-2026-10`: splits (none harmonised)

1. **Article 73 for a system under Article 6(1) with Annex I Section A, in the text as enacted.**
   `solo-2026-10` gives 2 August 2027 ("Article 6(1) and the corresponding obligations").
   This encoding puts Article 73 in the group `General`, from 2 August 2026 whatever the route (`Art 113 as enacted the date of application`, run for `General` and the Annex I route: 2 August 2026).
   No effect on an answer: the text as enacted never applied to a date on which either encoding reads it, because the Omnibus took effect on 27 July 2026.
2. **Article 99 and a failure to report under Article 73 (their fork F8).**
   `solo-2026-10` reasons that a failure to report is not an obligation "pursuant to Article 16", so no ceiling applies to a provider supervised nationally.
   This encoding takes the infringement as an input from a closed list (`Art 99 infringement`) and answers `NOTHING` for `Art 99 another infringement`; it has no function that decides whether a failure to report falls under Article 16.
   The two agree only for a caller who picks `Art 99 another infringement`; the classification step is not encoded here and was not compared.
3. **"Immediately".**
   `solo-2026-10` encodes Article 20(2) and Article 73(2) to (4) "immediately" as a clock that states no period beyond the stated outer limit.
   This encoding reads it two ways: part P3 reads "immediately" in Articles 20(1), 20(2), 22(4), 24(4), 26(5) and 26(10) as the same day (`WITHIN 0`, fork F-immediately, so a late act reaches `BREACH`); part P8 takes "immediately" in Article 73(2) to (4) as a judgment the caller supplies and puts the period on the outer limit.
   The split between P3 and P8 is inside this encoding and is not harmonised; the other reading at each site is named in its fork entry.
4. **The version of the text.**
   `solo-2026-10` takes the version as an input and asserts both; this encoding derives it from the date asked (`Omnibus Art 4 the version in force`), so the text as enacted can be asked only for a date before 27 July 2026.
   A design difference, not a disagreement about the law.

#### Against `eu-ai-act-art50.l4`: agreements

- Article 50 applies from 2 August 2026 and no exception of Article 113 reaches it (group `General` here).
- Article 111(4): a provider of a synthetic-content system placed before 2 August 2026 owes compliance with Article 50(2) from 2 December 2026. The earlier encoding answers `FALSE` for "compliance is owed" before that day; this encoding answers `NOTHING` from 2 August to 1 December 2026 (`notes/P6-NOTES.md`), the same reading in this encoding's convention.
- The exceptions of Article 50(2) (an assistive function for standard editing; no substantial alteration; use authorised by law to detect, prevent, investigate or prosecute criminal offences) and of Article 50(4) (the same law-enforcement exception; human review or editorial control together with editorial responsibility for text) are all inputs of `P6-art-50.l4`.
- The deep fake of Article 3(60) and the deployer of Article 3(4) (the personal non-professional exception) are computed from facts in the keel's definitions.
- The artistic, creative, satirical or fictional limb of Article 50(4) limits the first subparagraph (the deep fake) to a disclosure of existence.

#### Against `eu-ai-act-art50.l4`: splits and differences

1. The earlier encoding raises a fork (its F2) on whether the artistic limb, which speaks of "the transparency obligations set out in this paragraph", also reaches the text of the second subparagraph. Both encodings apply the limb to the first subparagraph only, but part P6 raises no fork on the question (its text functions mention no such limb: 0 occurrences of "artistic" in `Art 50(4)` text functions of `P6-art-50.l4`). A lawyer may want the fork there.
2. This encoding adds what the earlier one does not have: Article 50(1), (3), (5), (6) and (7), the reach of Article 2(2) over Article 50 for a system under Article 6(1) with Section B products (fork F-S14-reach: Article 50 is left out for such a system), seat questions, and the date arithmetic of both texts.
3. The earlier encoding answers `BOOLEAN` for "requires" and "applies"; this encoding answers `JUST TRUE`, `JUST FALSE` or `NOTHING` throughout. Where the earlier one says `FALSE` because the provision has not begun to apply, this one says `NOTHING`.

## Independence and what is disclosed

- No agent was shown `subjects/eu/ai-act-2024/encodings/solo-2026-10` or `subjects/comparative/ai-content-labelling/encodings/legalese/eu-ai-act-art50.l4` until every agent had finished; the lead read them afterwards for the differential. **The lead had read the first 60 lines of `aia-dates.l4` of `solo-2026-10` earlier in the run, so the differential for Articles 111 and 113 is not blind.**
- The briefs forbade the `advisor` tool. The lead scanned every agent's transcript for calls of that tool: the lead's script counted, in the transcript of each of the 15 agent runs (keel, P0, P1, P2, P3 and its resumed run, P4 to P9, and the three readers), the calls of any tool whose name contains the word advisor, and found 0 in every one.
- Part P2 reported a `pgrep -fl` whose output included other runs' command lines; it opened no file belonging to another run.
- Cost: stop line 1.5 billion cache-read tokens all-in (the lead included); measured by the lead's script at 1,127.2 million at 13:26 UTC on 2026-11-17, after the final gate and before the commit (agents 996.2 million, lead 131.1 million since its baseline of 2026-11-17 08:07 UTC).

## Findings the merge leaves open (for a lawyer)

Everything below is an assumed reading, not a ruling. Each part's own fork register names the other reading at each site; this section collects the readings that cut across parts, in the order of consequence.

### 1. F-S14-reach: does Article 2(2) switch off the rest of the Regulation for a system under Article 6(1) with Annex I Section B products? (top of the list)

Article 2(2), in the consolidated text (line 41 of the source file): "For AI systems classified as high-risk AI systems in accordance with Article 6(1) related to products covered by the Union harmonisation legislation listed in Section B of Annex I, only Article 6(1), Article 60a and Articles 102 to 112 shall apply."
The text as enacted reads "only Article 6(1), Articles 102 to 109 and Article 112 apply" (line 420 of `eu-ai-act-2024-1689.txt`).
**Reading taken** (assumed, not ruled), as the parts that call the keel's function state it: the list is closed by "only", so for such a system a provision outside it is left out, and a function "of" such a system answers `JUST FALSE` when the keel's `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` (in `aia-scope.l4`) does, a function that returns a number answers `NOTHING`, and a regulative rule reads `FULFILLED` (nothing owed), per the entries of P8 and P9 quoted below.
**The most consequential site is Article 99** (administrative fines): `Art 99 the non-compliance is subject to administrative fines` calls the keel's function, and P9's entry says it answers `JUST FALSE` when Article 2(2) cuts the provision off; so, on the reading taken, no administrative fine under Article 99 is available against the operator of a system under Article 6(1) with Section B products. A lawyer may find that too strong.
The keel's function is called from these modules, counted from the files (non-test, non-seat modules): `P2-section-2-gate.l4` 1, `P3-section-3.l4` 1, `P4-gate.l4` 1, `P5-section-5.l4` 1, `P6-art-50.l4` 1, `P7-gates.l4` 3, `P8-gate.l4` 2, `P9-art-100-101.l4` 1, `P9-art-81.l4` 7, `P9-art-82-84.l4` 9, `P9-art-99.l4` 1. The seat modules reach it through them. `P1` has no call.
**Other readings, as the parts state them:** `NOTHING` instead of `JUST FALSE` for a provision cut off (P3, `notes/P3-NOTES.md:358`); and, for Article 50, that Article 2(2) speaks of what applies to the high-risk system as such and does not reach Article 50, so no function would call the keel (P6, in its entry below).
Where each part states its reading. The parts that name an entry `F-S14-reach` are quoted from their notes, cut at 600 characters; **P2, P3 and P7 state the reading under another heading and have no fork entry of that name, so they have no stated other reading for this question beyond what is quoted above; the briefs did not name the entry, and the lead did not catch it before the merge:**
- `P1`: `notes/P1-NOTES.md:147`: | F-S14-reach | Art 2(2) (the keel's `aia-scope.l4`), seam S14, as it reaches P1 | no function of P1 calls `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` | no function of P1 is a provision of or about a high-risk AI system under Article 6(1) with Section B products that Article 2(2) leaves out: Article 6(1) and the Annex I functions are the route itself (Article 6(1) is among the provisions Article 2(2) leaves applying; the keel answers `JUST TRUE` for it); Article 5 prohibits practices of any AI system; Article 6(2) to (8), Article 7 and...
- `P2`: no entry named `F-S14-reach`; it mentions the reach at `notes/P2-NOTES.md:303,320` (a seam entry or a list item).
- `P3`: no entry named `F-S14-reach`; it mentions the reach at `notes/P3-NOTES.md:22,358,376,387,545` (a seam entry or a list item).
- `P4`: `notes/P4-NOTES.md:467`: **F-S14-reach** (seam S14, `Article 2(2)`; assumed, not ruled).
- `P5`: `notes/P5-NOTES.md:514`: - **F-S14-reach** (Art 2(2) (consolidated line 41, outside my ranges) with Articles 40 to 49 and Annexes V, VI and VIII).
- `P6`: `notes/P6-NOTES.md:362`: - **F-S14-reach** (Article 2(2), the keel's, over Article 50; seam S14; `Art 50 Article 2(2) leaves the paragraph out for the AI system`, and the eleven Article 50 functions and six rules that call it).
- `P7`: no entry named `F-S14-reach`; it mentions the reach at `notes/P7-NOTES.md:25,209,435,551,559,560` (a seam entry or a list item).
- `P8`: `notes/P8-NOTES.md:305`: | F-S14-reach | Arts 72 to 79: the 50 functions (17 regulative rules) that call the keel's `Art 2(2)` through `Arts 72 to 79 Article 2(2) cuts off the provision` | the 50 functions listed under Seams (S14) | `JUST FALSE` (a function that returns a number: `NOTHING`; a regulative rule: `FULFILLED`, nothing is owed) where the keel answers `JUST FALSE`, which is for a system whose route is Art 6(1) with Annex I and whose products are covered by Section B; where the keel answers `NOTHING` the function answers on its own provision (assumed, not ruled) | a narrower reach (only the provider's duties ...
- `P9`: `notes/P9-NOTES.md:349`: - **F-S14-reach** (Arts 81, 82, 83, 99 and 100 (seam S14); class other). Function: `the 18 functions that call `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` (7 in Article 81, 9 in Articles 82 and 83, `Art 99 the non-compliance is subject to administrative fines`, `Art 100 the non-compliance of the body is subject to administrative fines`; 16 answer JUST FALSE when it does, and the two hand-written regulative rules owe nothing) and the 11 regulative rules built on decision functions`. Answer taken: a function of mine is "of" a high-risk A...
The keel and `P0` have no fork entry for it either; the keel computes the function once and the readings above are the parts'.

### 2. NOTHING or JUST FALSE where a duty, a power or an infringement has an unmet "where", "when", "upon" or "if" (the split sites, side by side)

The Guide's rulings point two ways at these sites, and the parts decided site by site, each with a fork line naming the Guide line it relied on; **no answer was changed to match another part, and none was harmonised here**. The parts classify their sites alike under four heads: (i) an unmet element of an infringement, (ii) a "may" gated by "where", "when", "upon" and the like, (iii) a system saved by Article 111(2) or a group not yet applicable, (iv) a duty whose condition is unmet. Below, each part's own lead line for each head is quoted from its notes with its line number, cut at 420 characters; **the counts are the parts' and were not re-counted by the lead.**

**P1** (`notes/P1-NOTES.md`, section 'Split sites', line 220):
- line 224: **(i) An unmet element of an infringement: 13 sites, all answer `NOTHING`** (fork F-5-1-element): Article 5(1) points (a), (b), (ba), (bb), (c), (d), (e), (f), (g), (h) (10 sites, `Art 5(1)(x) the AI practice is prohibited`); the bar on a decision based solely on the output, Article 5(3) (`Art 5(3) the decision is barred ...`); the bar on sensitive operational data in the notification, Article 5(4) (`Art 5(4) the not...
- line 226: **(ii) A "may" gated by "where", "when", "upon", "in accordance with" or "within the limits": 7 sites.**
- line 233: **(iii) Functions that can answer `NOTHING` because of Article 111(2) or the gate on a placement date: 4 functions and 2 rules.**

**P2** (`notes/P2-NOTES.md`, section 'Split sites', line 326):
- line 328: (i) An unmet element of an infringement: **1 site**, answer `NOTHING`: `Art 14(5) the deployer is barred ...` when the system is not one referred to in point 1(a) of Annex III (the element that makes the prohibition reach it).
- line 332: (ii) A "may" gated by "where", "when", "to the extent" or the like, or a grant limited in its own wording: **7 sites**. Six answer `NOTHING` when the gate fails, on the grant line ("limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87)) as the brief's limit (1) applies it; none of the six gates is introduced by "where", "when" or "upon".
- line 353: (iii) Functions whose answer can be `NOTHING` because a system is saved by Article 111(2) (those that pass the core's placement date to the keel's applicability function, through the gate): **65 decision functions** (all the functions of Articles 8 to 15 and Annex IV that take the AI system: 8(1) 4, 9 14, 10 7, 11 7, 12 3, 13 4, 14 7, 15 9, Annex IV 10, counting the dispatchers once), and the five regulative rules th...

**P3** (`notes/P3-NOTES.md`, section 'Split sites', line 398):
- line 402: (i) An unmet element of an infringement: 5 sites, all prohibitions, because Articles 16 to 27 name no infringement and no penalty (the penalties are in another part).
- line 410: (ii) A "may" gated by "where", "when", "upon", "on application" or "with the consent of": 6 sites, each answering `NOTHING` when the gate fails, when the case falls outside the limit, or (Art 27(3)) when the exemption is the case:

**P4** (`notes/P4-NOTES.md`, section 'Split sites', line 623):
- line 625: (i) **An unmet element of an infringement: 0 sites.**
- line 630: (ii) **A "may" gated by "where", "when", "upon", "on application", "with the consent of" and the like.**
- line 641: (ii-b) **A presumption or a validity gated by "where", which is not a duty and not a "may": three sites, answered `JUST FALSE` when the "where" fails (rule (b), line 93): Article 32 (fork F-32-where), Article 36(8) and Article 36(9) first subparagraph (fork F-36-where).**
- line 663: (iii) **A group not yet applicable, or an AI system saved by Article 111(2): `NOTHING`, the keel's reading, not mine to change.**

**P5** (`notes/P5-NOTES.md`, section 'Split sites', line 854):
- line 856: (i) **An unmet element of an infringement: 0 sites.** Articles 40 to 49 and the four Annexes name no infringement and no prohibited practice; their breach paths are the missed deadlines of Art 43(3) and Art 49(1) to (3), which are not elements of an infringement.
- line 858: (ii) **A "may" gated by "where", "when", "upon", "on application" and the like: 5 sites; 3 answered `JUST FALSE` (a "where" or "upon" gate: the periods ruling, rule (b), and the delegated-definitions ruling, item (c)) and 2 answered `NOTHING` (a gate in other words: the grant rule); the other reading of the 3 is `NOTHING` (the grant ruling).**
- line 871: (iii) **A system saved by Art 111(2), or a group not yet applicable: `NOTHING` (the keel's reading, F-111-2-nothing in the keel's fork register; I did not decide it again).** 59 functions of this part answer `MAYBE` and take the placement date, so they can answer `NOTHING` because Art 111(2) saves the system; 34 regulative rules pass the same facts and read that `NOTHING` as nothing owed (`FULFILLED`); the 74 other `...
- line 874: (iv) **A deeming rule, a presumption or a validity rule gated by "where", "when" or "upon" that is neither a duty nor a "may": 2 sites, both answered `JUST FALSE` where the gate fails (the periods ruling, rule (b)); the other reading is `NOTHING`.**

**P6** (`notes/P6-NOTES.md`, section 'Split sites', line 617):
- line 621: **(i) An unmet element of an infringement: 0 sites.**
- line 626: **(ii) A "may" gated by "where", "when", "upon", "on application", "with the consent of": 2 sites, both answered `JUST FALSE` when the gate fails.**
- line 636: **(iii) A system saved by Article 111(2), or a group not yet applicable: `NOTHING` (the keel's reading, fork F-111-2-nothing in `inputs/KEEL-NOTES.md`; not decided again here).**

**P7** (`notes/P7-NOTES.md`, section 'Split sites', line 804):
- line 806: **(i) An unmet element of an infringement: 0 sites.**
- line 810: **(ii) A "may" gated by "where", "when", "upon", "with the consent of" and the like: 11 sites, 2 answered `JUST FALSE`, 9 answered `NOTHING`.**
- line 833: **(iii) A system saved by Article 111(2), or a group not yet applicable: 0 functions of this part pass a placement date to the keel's applicability function.**

**P8** (`notes/P8-NOTES.md`, section 'Split sites', line 546):
- line 548: **(i) An unmet element of an infringement: 2 sites, both answer `NOTHING`.**
- line 553: **(ii) A "may" gated by "where", "when", "upon" and the like: 20 sites, all `JUST FALSE`.**
- line 586: **(iii) Functions whose answer can be `NOTHING` because of Art 111(2) or a group not yet applicable.**
- line 591: **(iv) A duty whose condition is unmet: 42 sites, 38 answer `JUST FALSE` and 4 answer `NOTHING`.**

**P9** (`notes/P9-NOTES.md`, section 'Split sites', line 546):
- line 550: **(i) An unmet element of an infringement: 7 sites.**
- line 555: **(ii) A "may" gated by "where", "when", "upon", "after": 9 sites, all `JUST FALSE`** (the periods ruling's rule (b), with (c) of the ruling of 2026-11-05 counting "when" and "upon" as "where"): F-88-2 (88(2)), F-90-1 (90(1)), F-90-2 (90(2)), F-91-3 (91(3)), F-92-1a (92(1) "after consulting the Board"), F-92-1b (92(1)(a) "where the information is insufficient"), F-93-1a (93(1) "Where necessary and appropriate"), F-93...
- line 559: **(iii) A system saved by Article 111(2), or a group not yet applicable: `NOTHING` (the keel's reading F-111-2-nothing, not decided again).**

Two things the quoted lines do not show:
- **A duty whose "where" or "if" is unmet.** The Guide's line 95 names it as open, decided site by site. P4's own count of its `NOTHING`-kind branches of that kind is at `notes/P4-NOTES.md:67` (entry `F-unmet-where`), P8's count of its 42 duty sites is its head (iv) above, and P2's entry is `F-duty-where` (`notes/P2-NOTES.md:243`); the lead did not harmonise them.
- **Reader g1's note** (`notes/independent/g1-triage.md:65`): for an unmet "where" the encoding answers `JUST FALSE` at Article 6(7), Article 23(2) and Article 24(2), and `NOTHING` at Article 16(e), Article 16(k), Article 20(2), Article 21(1) and Article 24(5); the reader marked each AMBIGUOUS, and said the `NOTHING` sites would be ENCODER findings if the periods ruling's rule (b) governs duties.
The Guide's line 95 leaves the duty case open ("decided case by case"), so none of this is a defect in the sense of the Guide; it is a place where one question has two answers in one encoding, and a lawyer's reading would let a later pass harmonise it.

### 3. Article 111(2): `NOTHING` for a saved system, where the Guide's line 86 would give `JUST FALSE`

Article 111(2) (line 1623 of the source file) says: "this Regulation shall apply to operators of high-risk AI systems, other than the systems referred to in paragraph 1 of this Article, that have been placed on the market or put into service before the date of application of Chapter III referred to in Article 113, only if, as from that date, those systems are subject to significant changes in their designs" (see the keel's `F-111-2-nothing`, `notes/keel-NOTES.md:100`). On the Guide's line 86 a flat "only if" gives `JUST FALSE`; the coordinating session ruled to keep `NOTHING`, and the keel's one gate returns `FALSE` for both a saved system and a group not yet begun, so every part's function that calls it answers `NOTHING` for a saved system. Each part counts the functions this reaches under head (iii) of its Split sites section (quoted above). A lawyer may prefer `JUST FALSE` for the saved system and `NOTHING` only before the group applies.

### 4. Other readings that a lawyer should look at

- **F-113-groups** (section 'The time axis'): Chapter III Section 5 dated by the general date; part P5 ran a gap test, `notes/P5-NOTES.md`.
- **Articles 111 and 113 date functions answer from entry into force** (section 'The time axis'): the other reading is `NOTHING` before 2 August 2026.
- **Article 2(8) and Article 2(12)** (`notes/independent/g1-triage.md:15-17`): reader g1 found two AMBIGUOUS sites: whether testing in real-world conditions "shall not be covered by that exclusion" restores the Regulation or only withdraws the exclusion, and whether an open-source exclusion lost to an "unless" restores the Regulation or only lifts the exclusion. The keel's answer is `NOTHING` at both. The Guide's line 95 asks for a fork line at a site of the "unless once met" kind, and **the keel's notes have no fork entry for either article** (the nearest, `F-2-order`, `notes/keel-NOTES.md:103`, is about the order of Article 2(1) and the exclusions); the readers' restated assertions carry the question. That is a gap in the keel's fork register, not repaired here.
- **The readers' AMBIGUOUS verdicts:** every restated line of a reader's file that carries `the encoder's reading, not a ruling, for a lawyer` is a place the text reads two ways and the encoding took one. Counted from the files: g1 22 restated lines, g2 44 restated lines, g3 16 restated lines (the lines mix SCENARIO, AMBIGUOUS and ENCODER-SETTLED verdicts; the verdict is on each line).
- **Article 75c(8)** (interruption rules) is not modelled, and the before-the-period answer for it has no Guide line.
- **Article 99 and a failure to report** (differential, split 2): the classification of a failure to report under Article 73 as an infringement of Article 16 is not encoded.
- **"Immediately"** (differential, split 3): `WITHIN 0` in P3 against a judgment input in P8.
- **The consequence of a breach** is stated only where the text states one; where it states none, a regulative rule has no `LEST` (each part's 'Rules with no breach path').

### 5. Findings of the independent readers that no function answers (GAP)

The readers' GAP lists are in their triage files (`notes/independent/g1-triage.md` from line 38, `g2-triage.md` from line 54, `g3-triage.md` from line 41): questions the encoding cannot be asked because no function takes the fact the question varies, for example a function that returns a count of the codes of Annex XIV, a function for the delegated-act powers of Article 43(5) and (6), and the function that classifies a system into a code. The three examples are from g2's list; the other readers' lists are in the triage files. A GAP is a question that cannot be asked, not a wrong answer.

### 6. The licence of the source

`SOURCE-LICENSE.md` of this folder records the source texts as UNDETERMINED, as the subject-level `SOURCE-LICENSE.md` (`../../SOURCE-LICENSE.md`) does for the Official Journal texts, and adds the Publications Office consolidated version under the same status. The TFEU row's reading of Commission Decision 2011/833/EU is not adopted; the terms remain a question for the maintainer.

## What each part's notes hold

- `notes/keel-NOTES.md` (207 lines): What the two dates are made of; Coverage table; Fork register; Jural relations; Reading a result: FALSE and NOTHING; Marginal readings for a lawyer; Split sites (your part); Rules with no breach path (your part); What the stable binary does not accept, and what was met; Seat layer.
- `notes/P0-NOTES.md` (277 lines): Status; Reading a result; What the stable binary does not accept; Seats (P0); Fork register (P0); Marginal readings for a lawyer (P0); Tests.
- `notes/P1-NOTES.md` (385 lines): Coverage (P1); Fork register (P1); Jural relations (P1); Marginal readings for a lawyer (P1); Seams (P1); Split sites (P1); Rules with no breach path (P1); Versions (P1); Seats (P1); Findings: what the text turns out to say; What the stable binary does not accept; What check.sh prints.
- `notes/P2-NOTES.md` (502 lines): Status header; Files (P2); Coverage (P2); Fork register (P2); Jural relations (P2); Marginal readings for a lawyer (P2); Seams (P2); Split sites (P2); Rules with no breach path (P2); Versions (P2); Seats (P2); What the text turns out to say (P2); What the text does not answer (P2); What the stable binary does not accept (P2).
- `notes/P3-NOTES.md` (579 lines): What this part is; Coverage (P3); Fork register (P3); Jural relations (P3); Marginal readings for a lawyer (P3); Seams (P3); Split sites (P3); Rules with no breach path (P3); Versions (P3); What the stable binary does not accept; Seats (P3); Files.
- `notes/P4-NOTES.md` (954 lines): Status header: how each kind of claim in this file was checked; Files; Coverage (P4); Fork register (P4); Jural relations (P4); Marginal readings for a lawyer (P4); Split sites (P4); Rules with no breach path (P4); Seams (P4); Versions (P4); Seats (P4); What the text turns out to say (numbered findings); What the text does not answer (P4); What the stable binary does not accept (and what was met).
- `notes/P5-NOTES.md` (1097 lines): Coverage (P5); Fork register (P5); Jural relations (P5); Marginal readings for a lawyer (P5); Seams (P5); Split sites (P5); Rules with no breach path (P5); Versions (P5); Seats (P5); What the text turns out to say (numbered findings); What check.sh prints.
- `notes/P6-NOTES.md` (980 lines): Coverage (P6); Fork register (P6); Jural relations (P6); Marginal readings for a lawyer (P6); Seams (P6); Split sites (P6); Rules with no breach path (P6); Versions (P6); Seats (P6); Findings: what the text turns out to say; What the text does not answer; What the stable binary does not accept, and what was met; What check.sh prints.
- `notes/P7-NOTES.md` (1250 lines): Coverage (P7); Fork register (P7); Marginal readings for a lawyer (P7); Split sites (P7); Jural relations (P7); Seams (P7); Versions (P7); Rules with no breach path (P7); Seats (P7); What the text turns out to say (numbered findings); What the text does not answer; What the stable binary does not accept; Traces; What srcrefs prints.
- `notes/P8-NOTES.md` (849 lines): Coverage (P8); Fork register (P8); Jural relations (P8); Marginal readings for a lawyer (P8); Seams (P8); Split sites (P8); Rules with no breach path (P8); Versions (P8); Seats (P8); What the text turns out to say (numbered findings); What the stable binary does not accept; What `check.sh` prints.
- `notes/P9-NOTES.md` (938 lines): Status header: how each kind of claim was verified; Files; Coverage (P9); Fork register (P9); Jural relations (P9); Marginal readings for a lawyer (P9); Seams (P9); Split sites (P9); Rules with no breach path (P9); Versions (P9); Seats (P9); What the text turns out to say (numbered findings); What the text does not answer; What the stable binary does not accept.

## What would need doing before the encoding is worth relying on

- A lawyer should read the findings above, starting with F-S14-reach, and each part's fork register, and rule on the readings.
- The split sites (finding 2), the Article 111(2) reading (finding 3) and the reader-restated lines should be harmonised once a lawyer has ruled; none was harmonised here.
- The text should be checked against the Official Journal; the consolidated version here has no legal effect.
- The NEEDS-CORE requests (`NEEDS-CORE.md`) should be taken into the keel, with the gate run again.
- The seams that stay inputs should be wired where a part's output answers another part's input.
- The licence question above should be settled.

## Source not official

The quoted text is a Publications Office consolidated version of the Regulation rendered to plain text by a script. It is not the Official Journal text, it has no legal effect, and nothing in this folder claims to be verified against the official text. See `SOURCE-LICENSE.md`.
