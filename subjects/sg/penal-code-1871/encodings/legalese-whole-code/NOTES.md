# Penal Code 1871 (Singapore), the whole Code — row `legalese-whole-code`

A draft encoding of the whole Penal Code 1871, built to the charge generator's contract (`legalese/l4-ide` `ts-apps/charge-generator`).
Version 0.1.0 was made in one 45-minute run of nine agents on 2026-09-26 (443 sections encoded by its own count, 42 deferred for time).
Version 0.2.0 is the completion pass of 2026-11-04 by one Sonnet 5.5 agent: it encoded the 42 deferred sections, moved 28 of the 29 `inert` sections and 19 sub-provisions out of `inert`, and audited the rest.
Every one of the Code's 600 sections now has a disposition: 524 encoded, 75 repealed in this text, 1 `inert` (s 1).
The text is the converter's plain-text rendering of Singapore Statutes Online, not the official text.
It was made to measure how compatible a whole-Code encoding would be with that consumer, not to wire it up.
It sits beside two other rows of the same Code: `legalese` (twelve modules, hand-built, with a bench of reported charges) and `legalese-aswathy` (the whole Code, 45 modules, eight verification passes).
Rows are equal; none is primary.

**Status: draft, not reviewed by a lawyer.** Revised once, on 30 September 2026 (filed here on 8 October): defects found by comparing the encoding with the ladder diagrams in Alex Woon's *Essential Criminal Law* were fixed, each checked against the Code's text. See "Revised 2026-09-30" below.
Completed on 4 November 2026 (version 0.2.0): see "Completion pass 2026-11-04".
**No lawyer or other domain expert has read any of it against the text, the 0.2.0 additions included.**

## Where things are

- `*.l4` — 31 encoding modules and 13 tests modules (44 files, 66,529 lines). The 36 files of version 0.1.0 (27 + 9, 49,537 lines) are as found; version 0.2.0 adds `pc-body-a-deferred`, `pc-body-b-deferred`, `pc-body-b-deferred-images` and `pc-general-moved`, each with a `-tests` module (16,992 lines). `pc-domain.l4` holds the shared nouns and `pc-general.l4` holds Chapter 2, the `Punishment` and `Charge` records and the shared helpers; every other module imports both.
- `check.sh` — runs every module and counts errors, satisfied and failed assertions. `l4 run` exits 0 when an `#ASSERT` fails, so read its counts, not an exit code.
- `notes/PLAN.md` — the conventions every encoder followed.
- `notes/<group>-coverage.md` — every section in the group's chapters, with its disposition and function names.
- `notes/<group>-forks.md` — every ambiguity met, the readings, the one taken and why. `notes/deferred-forks.md` is the register of the 0.2.0 pass (DEF-A1 to DEF-M7).
- **`notes/<group>-coverage.md` are the 0.1.0 record and are now stale for 42 + 28 sections and 19 sub-provisions**: they still say `deferred` or `inert` where this file's "Coverage" says `encoded`. They were not edited; this file supersedes them.
- **Stale statements in the modules of 0.1.0, not edited** (the brief allows an edit to an existing module only to fix a defect shown against the text, and a stale comment is not one): `pc-body-a-life.l4` says deferred at lines 8, 26, 310, 595, 993, 1062 and 1201; `pc-body-b-sexual.l4` at line 34; `pc-body-a-hurt.l4` at lines 6 and 1064; `pc-body-b-kidnapping.l4` at line 754; `pc-general.l4` says "Inert" for ss 6A, 7, 8, 9, 12, 17, 22A, 33, 36, 38 and 44A to 51 in comments at lines 40-66, 212, 640, 683, 710, 767 and 775; `pc-general-part.l4` says s 108B has "no leaf" asking its condition (line 1108). All of these are now encoded in `pc-general-moved.l4` or the deferred modules.
- `generators/deferred/` — the scripts and sources of 0.2.0, run from this folder with relative paths. `build_b1.sh` builds `pc-body-b-deferred.l4`, `build_images.sh` builds `pc-body-b-deferred-images.l4`, and `build_tests.sh` builds `pc-general-moved.l4` (from `moved.in`, through `autoq.py` and `expand.py`) and the four generated tests modules (through `gen_struct_tests.py` and `gen_tests.py`). `pc-body-a-deferred.l4` was written by hand; `expand.py` filled in its quotations. Re-running a script overwrites hand edits to its output. Checked 2026-11-04: `build_b1.sh` and `build_images.sh` reproduce their modules byte for byte (the first only after finding 3 below was repaired). `audit.py` is the script behind the audit.
- `generators/` (the rest) — several groups generated their modules or tests with scripts, kept here. Paths inside them are absolute to the machine they ran on (`/Users/mengwong/...`); a hand edit to a generated `.l4` is lost if its generator is re-run.
- The source text is the subject's `registers/source-bundle/PC1871.txt` (SSO, "Current version as at 09 Sep 2026"); this row read that file byte for byte (sha256 `066301837e6413cf…`).

Run: workflow `sg-penal-code-encode`, run `wf_16958398-5ba`, session `pipeline` (6c6da87c), 2026-09-26.
Nine Opus agents at high effort: one ontology agent, then eight chapter-group encoders in parallel.
About 45 minutes, 3.0M subagent tokens, 472 tool calls.
Toolchain: the `l4` prerelease `unstable-20260926-c76e6b0` (legalese/prereleases), `JL4_LIBRARY_PATH` unset. Canon has no CI: these counts are a point-in-time record from that build.

## Checked after the run, by the integrator rather than the encoders

*These are the figures of version 0.1.0 (2026-10-08). The figures of version 0.2.0 are under "What `check.sh` prints" below.*

Every module was run again after the workflow returned, counting `DiagnosticSeverity_Error` lines and the anchored `Message: assertion satisfied|failed` lines.
The counts are from 2026-10-08, after the revision of 30 September, on the same toolchain: `check.sh` for the last three columns, `grep -c '^#ASSERT'` for the first.
At filing the totals were 1,314 / 1,312 / 2 / 2; the revision added 78 assertions, to body-a (146 to 179), exceptions (153 to 175) and property (195 to 218).

| tests module | #ASSERT | satisfied | failed | errors |
| --- | --- | --- | --- | --- |
| pc-general-tests.l4 | 115 | 115 | 0 | 0 |
| pc-general-part-tests.l4 | 167 | 165 | 2 | 2 |
| pc-exceptions-tests.l4 | 175 | 175 | 0 | 0 |
| pc-state-public-tests.l4 | 151 | 151 | 0 | 0 |
| pc-justice-order-tests.l4 | 92 | 92 | 0 | 0 |
| pc-body-a-tests.l4 | 179 | 179 | 0 | 0 |
| pc-body-b-tests.l4 | 123 | 123 | 0 | 0 |
| pc-property-tests.l4 | 218 | 218 | 0 | 0 |
| pc-documents-defamation-tests.l4 | 172 | 172 | 0 | 0 |
| **total** | **1,392** | **1,390** | **2** | **2** |

The 27 encoding modules have 0 errors each (and had 0 warnings at filing); 36 `.l4` files and 49,519 lines in all (47,973 at filing).
At filing, every figure matched what its encoder reported.

**The two failures are findings about the Code, left red on purpose.**
Both were checked against the source text:

- **s 118's Illustration is stale** (fork GP-14). It says concealing a design to commit gang-robbery is punishable under s 118, which needs "an offence punishable with death or imprisonment for life". s 395 now punishes gang-robbery with 5 to 20 years and caning, so on the current text those facts fall under s 120.
- **s 512(4)'s Illustration treats attempted robbery under s 512** (fork GP-10). s 512(2) applies only "where no express provision is made", and s 393 makes express provision for attempted robbery.

## Coverage

Every one of the Code's 600 sections has a disposition, and there are four: `encoded`, `inert`, `fork`, `repealed or blank in this text`.
There is no `deferred` and no `out-of-scope` any more.
The 0.1.0 column is the script's tally of the old coverage rows (see "Re-disposition audit"), not the 443 / 29 / 72 / 42 (= 586) that 0.1.0 printed, which did not add up to 600.

| disposition | sections at 0.1.0 | sections now |
| --- | --- | --- |
| encoded | 454 (and 1 partly: s 377C) | **524** |
| deferred for time | 41 | **0** |
| inert | 29 | **1** (s 1) |
| repealed or blank in this text | 75 | **75** |
| fork | 0 | **0** |
| **total** | 600 | **600** |

524 = 454 + 42 (the 41 deferred, and s 377C completed) + 28 (moved out of `inert`).
A fork is registered beside the rule it affects, not as the disposition of a whole section; no section's disposition is `fork`.

**Where each unit's row lives.** The coverage table is in three places, and this file is the index to them.
- **The 70 sections whose disposition changed** (the 42 deferred, now encoded, and the 28 moved out of `inert`), the 19 sub-provisions, and the units that are not whole sections: the rows are below, in this section.
- **The 530 sections whose disposition did not change** (454 encoded, 75 repealed, s 1 inert): one row each, with function names, in `notes/<group>-coverage.md` of 0.1.0 (body-a, body-b, documents-defamation, exceptions, general, general-part, justice-order, property, state-public); the 75 repealed rows are also listed with the repeal text found in the body in `../../logs/audit.txt`, section 3.
- **The stale rows**: the 0.1.0 coverage notes still say `deferred` or `inert` for the 70 sections and the 19 sub-provisions; the rows in this file supersede them.

**Units that are not whole sections** (counted by script, `generators/deferred/audit.py`; the rows are in "Re-disposition audit" below):

| unit | count | disposition |
| --- | --- | --- |
| sub-provisions that 0.1.0 left `inert` inside an encoded section, now moved | 19 | encoded, in `pc-general-moved` |
| `s 4B(3)` (the Minister may amend the Schedule by order) | 1 | inert, reason 2 (machinery) |
| `s 1` (short title) | 1 | inert, reason 2 (machinery) |
| title and edition statement, long title, enactment date | 3 | inert, reason 1 (not operative) |
| chapter headings | 26 | inert, reason 1 (not operative) |
| Legislative History, Abbreviations, Comparative Table | 3 | inert, reason 1 (the text says of the Legislative History, line 12703, "It is not part of the Act") |
| Schedule items 1 to 15 | 15 | encoded, in `pc-general-part.l4` (data and a decision), as 0.1.0 had them |

**The only three reasons for `inert`:** 1 not operative; 2 machinery; 3 shown repealed or blank.
The 75 repealed rows are reason 3 and are kept as `repealed or blank in this text`; all 75 were checked against the body text by script, and every body shows "[Repealed by ...]".
The old reasons "a convention", "carried in the `@desc` of a leaf", "addresses an interpretive canon", "no leaf asks it" and "another law's question" are not reasons, and no row rests on one now.

**Defined-term entries.** The script counts 61 in the text (a quoted term followed by means / includes / has the meaning / denotes / is).
By a search for a function whose name contains the term, 41 have one and 20 do not; the 20 are all in sections this pass did not encode (ss 4B, 73, 74, 74A, 292B, 305, 377CB, 379A, 409 and 427), where 0.1.0 carried the term in the `@desc` of a leaf.
This is a name search, not a check that each function says what the definition says, and it was not made for the 41 either.
For the sections this pass encoded, each defined term is a function with a test (for example `s 304B(2) the person is a child`, `s 376G(2) B is a close family relative of A`, `s 335A(6) the abuse is sexual abuse`).

**The 42 sections 0.1.0 deferred for time, now encoded** (derived from the modules by script, 2026-11-04; "other functions" counts the rules of reading, definitions and helpers that cite the section, not the charge items):

| s | module | charge items | records | other functions |
| --- | --- | --- | --- | --- |
| 301 | `pc-body-a-deferred` | none | 0 | 1 |
| 304B | `pc-body-a-deferred` | 304B(1) | 2 | 6 |
| 304C | `pc-body-a-deferred` | 304C(4) | 2 | 5 |
| 308A | `pc-body-a-deferred` | 308A(2) | 1 | 1 |
| 310 | `pc-body-a-deferred` | none | 1 | 1 |
| 311 | `pc-body-a-deferred` | 311 | 1 | 0 |
| 314 | `pc-body-a-deferred` | 314 | 1 | 0 |
| 315 | `pc-body-a-deferred` | 315(1) | 1 | 3 |
| 316 | `pc-body-a-deferred` | 316 | 1 | 0 |
| 335A | `pc-body-a-deferred` | 335A(1), 335A(2) | 1 | 5 |
| 372 | `pc-body-b-deferred` | 372 | 1 | 2 |
| 373 | `pc-body-b-deferred` | 373 | 1 | 2 |
| 373A | `pc-body-b-deferred` | 373A | 1 | 1 |
| 376B | `pc-body-b-deferred` | 376B(1), 376B(2) | 1 | 3 |
| 376C | `pc-body-b-deferred` | 376C(2) | 1 | 1 |
| 376D | `pc-body-b-deferred` | 376D(3) | 1 | 2 |
| 376E | `pc-body-b-deferred` | 376E(4) | 1 | 3 |
| 376EA | `pc-body-b-deferred` | 376EA(4) | 1 | 3 |
| 376EB | `pc-body-b-deferred` | 376EB(3) | 1 | 1 |
| 376EC | `pc-body-b-deferred` | 376EC(3) | 1 | 1 |
| 376ED | `pc-body-b-deferred` | 376ED(1), 376ED(2) | 1 | 2 |
| 376EE | `pc-body-b-deferred` | 376EE(1), 376EE(2) | 1 | 2 |
| 376F | `pc-body-b-deferred` | 376F(2), 376F(3) | 1 | 2 |
| 376G | `pc-body-b-deferred` | 376G(3) | 1 | 5 |
| 376H | `pc-body-b-deferred` | 376H(2) | 1 | 4 |
| 377 | `pc-body-b-deferred` | 377(2), 377(3) | 1 | 2 |
| 377B | `pc-body-b-deferred` | 377B(2), 377B(4) | 1 | 2 |
| 377BB | `pc-body-b-deferred-images` | 377BB(7) | 1 | 2 |
| 377BC | `pc-body-b-deferred-images` | 377BC(3) | 1 | 1 |
| 377BD | `pc-body-b-deferred-images` | 377BD(2), 377BD(6) | 1 | 5 |
| 377BE | `pc-body-b-deferred-images` | 377BE(3) | 1 | 4 |
| 377BF | `pc-body-b-deferred-images` | 377BF(3) | 1 | 1 |
| 377BG | `pc-body-b-deferred-images` | 377BG(2) | 1 | 4 |
| 377BH | `pc-body-b-deferred-images` | 377BH(2) | 1 | 2 |
| 377BI | `pc-body-b-deferred-images` | 377BI(2) | 1 | 1 |
| 377BJ | `pc-body-b-deferred-images` | 377BJ(3) | 1 | 2 |
| 377BK | `pc-body-b-deferred-images` | 377BK(2) | 1 | 3 |
| 377BL | `pc-body-b-deferred-images` | 377BL(2), 377BL(3), 377BL(4) | 1 | 6 |
| 377BM | `pc-body-b-deferred-images` | none | 0 | 2 |
| 377BN | `pc-body-b-deferred-images` | none | 0 | 10 |
| 377BO | `pc-body-b-deferred-images` | 377BO | 1 | 11 |
| 377C | `pc-body-b-deferred-images` | none | 1 | 18 |

A section with no charge item defines or limits and has no punishment of its own: s 301 (the description of a transferred culpable homicide, punished under ss 302 and 304), s 310 (infanticide, punished under s 311), ss 377BM and 377BN (defences) and s 377C (definitions and rules of reading).
s 376C and s 377BO borrow their punishment from another section's record, so each has a `charge under` item and no `punishment prescribed by` record of its own.
A section with several charge items has several punishing subsections, or one offence with punishments that depend on the facts (the charge then states the words that apply).

**The 28 sections moved out of `inert`**, all in `pc-general-moved.l4` (62 functions, each `@export`ed with `@desc`, `@ref`ed to its lines, and tested on both sides of each limb):

| s | what it is now |
| --- | --- |
| 2 | two functions: liability under the Code for an act of which the person is guilty within Singapore, and the text's own "not otherwise" |
| 3 | `Where an act is done`; the borrowed fact "liable by law to be tried" is an input |
| 5 | laws not affected: a flat negative |
| 6 | `Kind of provision`; Illustrations (a) and (b) tested against `exception under s 82` and `exception under s 76` |
| 6A | definitions of ss 22A to 26H apply to other written law, with the two exceptions |
| 7, 8 | rules of reading over two BOOLEANs, and over `Pronoun` and `Sex` |
| 9 | `Grammatical number`, the other number, and "unless the contrary appears" |
| 12, 17, 29A, 51 | "includes": `JUST TRUE` inside, `NOTHING` outside |
| 22A | `Kind of element of an offence` |
| 29B | the Electronic Transactions Act 2010 meaning is an input |
| 32 | words that refer to acts extend to illegal omissions, "except where a contrary intention appears" |
| 33 | `Doing`; "act" and "omission" (1); the poison Illustration (2) |
| 36, 38 | the Illustrations are tested against `commits murder` and `commits culpable homicide not amounting to murder` |
| 42 | "obscene": a "means" definition |
| 44A, 45 to 48, 50 | "denotes": `JUST TRUE` inside, `NOTHING` outside (but "unless the contrary appears" in ss 45 and 46 and "other than a human being" in s 47 are `JUST FALSE`) |
| 49 | `Calendar` |
| 54 | over the `Punishment` record |
| 108B | the abettor's acts outside Singapore change nothing; the offence must be committed in Singapore |

**The 19 sub-provisions moved:** 376A(1B)(a) and (b), 376AA(2)(a) and (b), 79(2), 79 Explanation 1, 79 Explanation 2 (three functions), 79A(2), 80(2), 86(2), 86(3), 26C(3), 26C(4), 26C Explanation, 53 Explanation (rattan), and the six jurisdiction subsections 73(3), 74(3), 74A(4), 74B(4), 74C(4) and 74D(4) (each a Magistrate's Court function and a District Court function, over one shared helper).

**The charge generator's contract.** 344 punishing provisions had the four items at 0.1.0 (general-part 10, state-public 76, justice-order 85, body-a 56, body-b 19, property 67, documents-defamation 31).
The three deferred modules add 47 `charge under s N` items (a-deferred 9, b-deferred 23, b-deferred-images 15), for 391; every one is `@export`ed with `@desc`.
By script, every one of the 42 sections whose text says "punished" has a `punishment prescribed by` record or borrows one, and a `charge under` item.
The exceptions group has none by design: Chapters 4 and 4A create no offence; it exports 18 `exception under s N` ladders and a roll-up instead.

**Forks:** 179 are registered across the nine `*-forks.md` notes at 0.1.0 (174 at filing, and five added by the revision of 30 September), and 22 more in `notes/deferred-forks.md` (DEF-A1 to A8, DEF-B1 to B7, DEF-M1 to M7).

## What integration changed

**Nine helpers were defined in more than one group**, with the same name and the same body: the age tests (below 12, 14, 16, 18 and 21; above 18), `5 or more persons`, `to wit` and `the to-wit clause`.
Each module ran alone, but a module importing two groups could not call the helper: "There are multiple definitions for the identifier" (probed with `pc-body-a-life` + `pc-exceptions-general`).
The one definition of each now lives in `pc-general.l4` under "Shared helpers, hoisted at integration", and the copies are gone from ten group modules.
After the move, all 27 non-test modules import together into one file with 0 errors, the helpers evaluate, and the counts in the table above are unchanged.

**The generators were patched to match**, because four groups generate their modules and a re-run would otherwise restore the duplicates.
State-public (`generators/state-public/`), property, justice-order and body-a were each re-run after the patch, and each reproduced the integrated deposit byte for byte.
The last three had been written to a session scratchpad; the copies in `generators/` are the patched ones. `generators/other/` holds further test-fixture scripts found there; which encoder wrote each is not recorded.

**Ruled.** "above 18 years of age" (s 87; s 300 Exception 5) means 18 or over: Meng, 2026-09-26, "yes 18 or older" (forks F-10 and E-9).

## Revised 2026-09-30

Eight modules changed (`pc-body-a-hurt`, `pc-body-a-life`, `pc-body-a-tests`, `pc-exceptions-private-defence`, `pc-exceptions-tests`, `pc-property-cheating`, `pc-property-tests`, `pc-property-trust`), with their generators and the body-a, exceptions and property notes.
Each change was found by that comparison and checked against the Code's text, and each has tests; forks F-20, E-17 and P-22 to P-24 record the reasoning.

- **s 300 Exception 7.** The abnormality of mind and its listed cause are leaves of their own, required before limbs (a)(i), (a)(ii) and (b). An intoxicated accused with no abnormality of mind no longer comes within the Exception on (a)(ii) alone.
- **s 300 Exception 2 reads Chapter 4A.** `Homicide Facts` carries a `Private Defence Facts`, and the flat "exceeds the power" leaf is replaced by `the right of private defence was exceeded`, so the Exception and the private-defence rules can no longer disagree.
- **Chapter 4A is decided in two stages:** whether the right arose (the kind of act, s 99, its start, s 98(2), s 106A), and whether it extends to the act (continuance, extent, s 98(1)). The answers under s 96 are unchanged. Where continuance and s 98(2) belong is fork E-17, which wants a ruling.
- **A grievous hurt is a hurt.** `causes hurt` reads s 320, and the s 321 fault reads the leaf for aiming at grievous hurt.
- **The murder refusal names each Exception that applies.**
- **s 405's last limb** ("intentionally suffers any other person to do so") is split into leaves: the accused suffers another person, that person acts dishonestly, which of the four acts that person does, and, for use or disposal, the violation. The charge names the other person, so "to do so" always has its antecedent. Whose dishonesty the limb needs is fork P-22, open for a ruling.
- **s 409(1)(b) and (g)** take the trade, role or body as a string particular and recite it (P-23); **s 419**'s recital names the mode of personation.
- **s 415 Explanation 1:** the `deceived the victim` `@desc` carries Poh Yuan Nie v PP [2022] SGCA 74 (P-24). No logic changed.
- **New tests** include the Exception 4 proviso, which no Illustration covers.

**Consumers keyed on field names need migrating:** `CBT Facts` loses one field and gains thirteen, and `Homicide Facts` loses three and gains five (`private defence`, and four for Exception 7).

## Not done, and worth knowing before anyone relies on this

- **No independent test pass.** Every test was written by the agent that wrote the code it tests, the 2,361 assertions of 0.2.0 included (see "Completion pass 2026-11-04" for what that does and does not show). justice-order is the thinnest of the 0.1.0 modules: 92 tests for 85 offences.
- **Not a cleanroom.** Encoders read Meng's 12-module drafts row as the pattern for the charge generator's contract.
- **The charge generator's catalogue is not updated, by choice.** The run was to measure how compatible a whole-Code encoding would be, not to wire it up (Meng, 2026-09-26). Each coverage note proposes its `OFFENCES` rows and family slugs.
- **28 proposed shared nouns** (24 from the encoders, 4 from the ontology agent: weapon, dwelling-house, animal, age helpers and others) are listed in the reports and not merged into `pc-domain.l4`; the age helpers are the part integration has done.

## Returned to Commons 2026-10-21

Moved back on 21 October 2026 from `legalese/solutions` (`Litigate.4/sg/penal-code-1871/legalese-whole-code/`), where it had been kept unchanged since 19 October 2026 (commons commit 699efaaf), to sit beside this Act's baseline encoding (`../baseline-2026-10/`).
It keeps its folder name, `encodings/legalese-whole-code/`.

**What was changed.** The stable `l4` has no `REFUSE`. The three named refusals now return an explicit "not covered" value, NOTHING, with the refusal's text kept in a comment:

- `punishable with imprisonment for` N `months or upwards within section 41` (pc-general) is a MAYBE BOOLEAN: JUST TRUE / JUST FALSE where s 41 answers, NOTHING where the section states no maximum term. Its one caller, s 506's `punishable with death or with imprisonment for a term which may extend to 7 years or more` (pc-documents-defamation-intimidation), is a MAYBE BOOLEAN too (JUST TRUE where death is prescribed, else s 41's answer).
- `the lower punishment within section 72 of` a `and` b (pc-general-part) is a MAYBE Punishment; NOTHING where s 72 gives no way to compare.
- `the fraction` k `of the longest term provided for` p (pc-general-part) is a MAYBE NUMBER; NOTHING where no longest term is stated.
- Tests: the one `#ASSERT REFUSED` (pc-general-tests) became `#ASSERT … EQUALS NOTHING`; the assertions on these four functions compare with `JUST TRUE`, `JUST FALSE`, `JUST n` or `JUST` the expected punishment; the fixture that fed s 506's answer to `included if` compares it with `JUST TRUE`. Two `#EVAL`s that showed a refusal now show NOTHING, and their comments say so. No expected value changed.

`notes/` and `generators/` still describe these as refusals, and the generator for pc-general-part-tests would write the old assertion shapes if re-run.

**Checks** (the l4 shipped in the l4-vscode 1.6.98 extension (JL4_LIBRARY_PATH unset), `l4 run` on every .l4 and runcases.py on every file with #ASSERTs): 36 modules, 0 errors other than the two expected failures; 1,392 assertions written, 1,390 satisfied (the 1,314 of the first filing plus the 78 of the revision). The two failures are the pair in `encoding.json` → `expected_red` (pc-general-part-tests lines 2114 and 2324, forks GP-14 and GP-10), findings about the Code left red on purpose, exactly as under the pre-release `l4`.

## Completion pass 2026-11-04

Version 0.2.0, run `iaw-pc42`, by **one Sonnet 5.5 agent** (no subagents), from a written brief.
The text is the converter's plain-text rendering of Singapore Statutes Online ("Current version as at 09 Sep 2026", `registers/source-bundle/PC1871.txt`, sha256 `066301837e6413cf635bf0dc21a44186705b9d892b04a2cdd1036afbd9e269f2`), **not the official text**.
Toolchain: the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19; sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`), `JL4_LIBRARY_PATH` unset; `check.sh` also runs a second stable build, 1.6.108 (main, 2ae7c9b, 2026-11-02), and compares the counts.

**What was done, in the order the brief fixed.**
1. A baseline `check.sh` before any change: 36 modules, errors 2, satisfied 1390, failed 2, refused 0 (the main build the same).
2. The audit, before any new L4 (below): the text's units counted by script; the 75 repealed rows checked against the body; the 29 `inert` rows and 19 sub-provisions judged against the three allowed reasons.
3. The 42 deferred sections encoded in three new modules, then 28 sections and 19 sub-provisions moved out of `inert` into a fourth, each with a tests module.
4. This file, `PROGRESS.md`, `notes/deferred-forks.md`, `encoding.json` 0.2.0.
The deferred count is now 0.

| new module | lines | exports | quotation lines | its tests | #ASSERT |
| --- | --- | --- | --- | --- | --- |
| `pc-body-a-deferred` (ss 301, 304B, 304C, 308A, 310, 311, 314, 315, 316, 335A) | 1,237 | 40 | 217 | `pc-body-a-deferred-tests` | 429 |
| `pc-body-b-deferred` (ss 372, 373, 373A, 376B to 376H, 377, 377B) | 2,404 | 82 | 403 | `pc-body-b-deferred-tests` | 1,018 |
| `pc-body-b-deferred-images` (ss 377BB to 377BO, 377C) | 2,440 | 96 | 555 | `pc-body-b-deferred-images-tests` | 706 |
| `pc-general-moved` (28 sections, 19 sub-provisions) | 1,094 | 62 | 225 | `pc-general-moved-tests` | 208 |
| **total** | | **280** | **1,400** | | **2,361** |

**How the tests were made.** Every expected value is written from the Code's words and none is copied from output.
The three large tests modules are generated: `gen_struct_tests.py` takes, for each offence, a formula over the facts record's leaves written from the section's text (in `spec_*.py`) and writes a set of facts that meets every element (one per alternative of an "or"), one set per element with that element alone made untrue, a set with nothing established, and the punishment variants; `gen_tests.py` expands the fixtures.
The cases that structure cannot give are written by hand and cite the subsection: the Illustrations and Explanations, both sides of every threshold, the closed lists, the rules of reading, the offences defined over another offence's facts, and the exact words of each charge.
`pc-general-moved-tests` is entirely by hand.

**What the tests show, and do not.** A test written by the author of the code, from the same reading of the text, cannot find a misreading of the text; it finds a slip between that reading and the L4.
To check that the tests can find a slip, 18 mutations were made to a scratch copy of the L4, each of the kind a slip would be, and the tests were run: 18 of 18 were caught.
Eight were on the three large modules: a section left out of the s 376E(2) list of relevant offences (377BG); the s 376G(4) nested consent read as a bare leaf; the s 376G(3) punishment words changed from 5 to 7 years; "below 16" dropped from s 377BN(4); the choice between the two punishments of s 314 swapped; the s 315(2) threshold moved from 28 to 27; a risk limb dropped from s 304C(1)(c); the age of the child in s 304B(2) shifted.
Ten were on `pc-general-moved` (Magistrate's Court threshold 60 to 62 months; the "dishonestly"/"fraudulently" exception of s 6A dropped; s 47's exclusion of a human being dropped; s 9's contrary-context limb inverted; s 22A's fault and physical elements swapped; s 42's AND turned into OR; s 2's "not otherwise" turned into `JUST TRUE`; s 3's liability input ignored; s 108B's "committed in Singapore" ignored; s 79 Explanation 1 turned into "guilty").

**Failing assertions.** None in the final run of the 2,361 new assertions.
On the first run of the three large tests modules none failed (after the two pre-run corrections in finding 1).
On the first run of `pc-general-moved-tests` two failed; both were a defect in the code, not in the assertion, and were repaired in the code (finding 2).

## Re-disposition audit

Written 2026-11-04 by one Sonnet 5.5 agent before any new L4 was written, from `generators/deferred/audit.py` (output kept in `../../logs/audit.txt`).
Status now: every `moves` verdict below has **landed** in `pc-general-moved.l4` and is tested in `pc-general-moved-tests.l4`; the two `stays inert` verdicts (s 1 and s 4B(3)) stand.
The text is the converter's plain-text rendering of Singapore Statutes Online ("Current version as at 09 Sep 2026"), not the official text.

### What the text has, counted by script (not by the old notes)

| unit | count in the text |
| --- | --- |
| sections in the table of contents | 600 (75 of them marked `(Repealed)`) |
| section starts found in the body | 600 (every contents entry has one) |
| numbered subsection markers, `(1)` `(1A)` `(2)` ... at a line start | 421, across 128 sections |
| lettered paragraph markers `(a)` `(b)` ... at a line start | 1,037 |
| Illustration headings | 119 |
| Explanation paragraphs | 108 |
| named Exceptions (the ten of s 300) | 10 |
| defined-term entries (a quoted term followed by means / includes / has the meaning / denotes / is) | 61 |
| chapters in the contents | 26 |
| items in the Schedule | 15 |

The old notes' totals (443 encoded, 29 inert, 72 repealed, 42 deferred = 586) do not add up to the text's 600 sections.
The script's tally of the old coverage rows, taking each section's best disposition, is 454 encoded, 1 partly encoded (s 377C), 41 deferred, 29 inert, 75 repealed = 600, and the 42 deferred sections of this pass are those 41 plus s 377C.
**The 72 was wrong: 75 sections are marked `(Repealed)` in the contents and in the body.**
All 75 have a coverage row that says repealed, and for every one the body shows the repeal ("[Repealed by Act ...]"): none is a live provision wrongly called repealed.

### Units the old tables had no row for

Every one of the 600 section numbers has a row in some group's table (0 missing).
The units that are not sections had none:

| unit | lines | disposition | reason |
| --- | --- | --- | --- |
| title "PENAL CODE 1871" and the edition statement ("2020 Revised Edition ... comes into operation on 3 December 2021") | 1222-1227 | inert | 1 not operative |
| long title "An Act to consolidate the law relating to criminal offences." | 1229 | inert | 1 not operative: states the purpose, creates no rule |
| enactment date "[16 September 1872]" | 1231 | inert | 1 not operative |
| the 26 chapter headings (Chapter 1 Preliminary ... Chapter 23) | in the body | inert | 1 not operative: headings |
| Schedule items 1 to 14 (`the sections named in items 1 to 14 of the Schedule`) and item 15 (`specified offence within the Schedule`) | 12656- | encoded | already data and a decision in `pc-general-part.l4`; the old tables had one row for "Schedule" |
| Legislative History, Abbreviations, Comparative Table | 12698- | inert | 1 not operative: the text says of the Legislative History, at line 12703, "It is not part of the Act" |

### The 75 repealed rows

Kept as `repealed or blank in this text` (the third reason for inert is the same: the text shows the section repealed). 75 of 75 verified by script against the body text, none moved.
The list is `../../logs/audit.txt` section 3.

### The 29 inert rows

Standard applied: a row stays `inert` only for (1) not operative, (2) machinery, (3) shown repealed or blank.
The old reasons "a convention", "carried in the `@desc` of a leaf", "addresses an interpretive canon", "no leaf asks it" and "another law's question" are not among the three.
Status of each verdict: landed (see above).

| s | heading | old reason | verdict | to |
| --- | --- | --- | --- | --- |
| 1 | Short title | a name, not a rule | stays inert, reason 2 (short title) | - |
| 2 | Punishment of offences committed within Singapore | territorial premise | moves: `s 2 the person is liable to punishment under this Code` and its "not otherwise" limb | pc-general-moved |
| 3 | Offences committed beyond Singapore | confers no jurisdiction | moves: the borrowed fact "liable by law to be tried" is an input | pc-general-moved |
| 5 | Certain laws not to be affected | a saving provision | moves: "nothing in this Code is intended to ... affect" is a rule about other laws that still applies | pc-general-moved |
| 6 | Definitions understood subject to exceptions | a convention | moves: rule of reading over a small typed representation, Illustrations (a) and (b) as tests | pc-general-moved |
| 6A | Definitions apply to other written law | concerns other law | moves: rule of reading | pc-general-moved |
| 7 | Expression once explained | a convention | moves | pc-general-moved |
| 8 | "Gender" | `Pronoun` serves | moves | pc-general-moved |
| 9 | "Number" | interpretive | moves | pc-general-moved |
| 12 | "Public" | carried in `@desc` | moves: includes, so NOTHING outside | pc-general-moved |
| 17 | "Government" | carried in `@desc` | moves: includes, so NOTHING outside | pc-general-moved |
| 22A | "Fault element", "physical element" | names two kinds of leaf | moves | pc-general-moved |
| 29A | "Writing" | carried in `@desc` | moves | pc-general-moved |
| 29B | "Electronic record" | out of scope | moves: the Electronic Transactions Act 2010 meaning is an input | pc-general-moved |
| 32 | Acts include illegal omissions | widens every act leaf | moves | pc-general-moved |
| 33 | "Act" and "omission" | rule of causation proof | moves: (1), (2) and the Illustration | pc-general-moved |
| 36 | Effect caused partly by act, partly by omission | widens the act leaf | moves, with the Illustration | pc-general-moved |
| 38 | Several persons, different offences | read separately | moves, with the Illustration | pc-general-moved |
| 42 | "Obscene" | one atom | moves: a "means" definition | pc-general-moved |
| 44A | "Bodily injury" | interpretive | moves | pc-general-moved |
| 45, 46 | "Life", "Death" | interpretive | moves | pc-general-moved |
| 47, 48 | "Animal", "Vessel" | carried in `@desc` | moves | pc-general-moved |
| 49 | "Year" and "month" | Gregorian | moves | pc-general-moved |
| 50 | "Section" | interpretive | moves | pc-general-moved |
| 51 | "Oath" | carried in `@desc` | moves: includes | pc-general-moved |
| 54 | Imprisonment for life | carried by `Punishment` | moves | pc-general-moved |
| 108B | Abetment outside Singapore | no leaf asks it | moves (the old row says "tested") | pc-general-moved |

### Sub-provision rows that were `inert` inside an encoded row

| provision | old note | verdict | to |
| --- | --- | --- | --- |
| 376A(1B), 376AA(2) | consent immaterial | moves: "it is not a defence that B did consent" is a flat negative | pc-general-moved |
| 79(2), 79 Explanations 1 and 2, 79A(2), 80(2), 86(2), 86(3) | declaratory, or evidence | moves: who must prove the fault element, and what intoxication includes | pc-general-moved |
| 26C(3), 26C(4), 26C Explanation | rules of proof | moves | pc-general-moved |
| 53 Explanation (rattan) | inert | moves | pc-general-moved |
| 4B(3) (the Minister may amend the Schedule) | inert | stays inert, reason 2 (power to amend by order) | - |
| 73(3), 74(3), 74A(4), 74B(4), 74C(4), 74D(4) | jurisdiction | moves: a court's jurisdiction and power to impose the full punishment, on the offence's own prescribed punishment | pc-general-moved |

## Changes to existing modules

None. No module, test or generator of 0.1.0 was edited, deleted or renamed: none of the 36 `.l4` files found is newer than `check.sh.pass1` (not shipped).
Outside the `.l4` files, `check.sh` has one added line, `pc-general-part-tests.l4) echo 2`, in `expected_failed` (the brief asked for it); the new tests modules expect 0 failures and need no entry.
`NOTES.md` is rewritten where it was stale (the opening, "Where things are", "Coverage", "Not done").
`notes/<group>-coverage.md` and `notes/<group>-forks.md` of 0.1.0 were not edited; they are stale for the rows this pass moved (see "Where things are").

## Marginal readings for a lawyer

The FALSE/NOTHING rule of 2026-10-29 (assumed, not ruled) lets a function answer `JUST FALSE` only where the text says no in its own words, and `NOTHING` everywhere else.
It leaves two readings that are for a lawyer, not for an encoder.
Every branch that rests on either is listed here, with the other reading, and each carries a `-- FALSE-kind` or `-- NOTHING-kind` comment in its module.
The list was made by script from those comments (`generators/deferred/`'s sources and the modules), and lists the branches of the four 0.2.0 modules only; the branches of the 36 files of 0.1.0 were not re-read under this rule.

### Reading (a): a failed "if" counts as the text's no, clause by clause, and a flat negative counts as no

The branch answers `JUST FALSE` (or a ladder answers `FALSE`, with the comment quoting the words).
**The other reading:** a condition introduced by "if" is a sufficient condition and not a closed one, and a flat negative says what need not be proved or is no defence without saying that the contrary fact is absent; on that reading each of these answers `NOTHING`.

**(a1) Flat negatives and bars** ("No person shall be guilty ...", "it is not necessary to prove", "it is not a defence that", "is not guilty", "not otherwise", "does not need to rely"): 23 branches.
  - `pc-body-a-deferred`: `commits the offence of causing or allowing death in the same household within section 304C(1)`
  - `pc-body-b-deferred`: `obtains the sexual services of a person below 18 years of age within section 376B(1)`; `communicates to obtain the sexual services of a person below 18 years of age within section 376B(2)`; `sexually communicates with a minor below 16 years of age within section 376EB(1)`; `engages in a sexual activity in the presence of a minor below 16 years of age within section 376ED(1)`; `causes a minor below 16 years of age to observe a sexual image within section 376ED(2)`; `has sexual penetration with a close family relative within section 376G(1)` (two branches); `s 376G(5)(a) the prosecution must prove that B did consent`; `s 376G(5)(b) B's consent is a defence`
  - `pc-body-b-deferred-images`: `s 377BE(6)(a) the prosecution must prove that the image or recording mentioned in the threat exists`; `s 377BE(6)(b) the prosecution must prove that the image or recording is in fact an intimate image or recording`; `s 377BN(5) a mistaken belief that the material is not offensive is a defence`
  - `pc-general-moved`: `s 2 the person is liable to punishment otherwise than under this Code`; `s 5 this Code affects the law`; `s 26C(3) the person intends or foresees the result`; `s 26C Explanation the absence of motive or desire stops the act being intentional`; `s 79 Explanation 1 the accused person is guilty`; `s 79 Explanation 2 the accused person needs to rely on the defence of mistake`; `s 376A(1B)(a) the prosecution must prove that B did consent`; `s 376A(1B)(b) B's consent is a defence`; `s 376AA(2)(a) the prosecution must prove whether B did or did not consent`; `s 376AA(2)(b) B's consent is a defence`

**(a2) Definitions by "is one that" and "refers to", read as closed** (DEF-A5; s 304C(5)(b)'s "refers to" is the same kind): 3 branches.
  - `pc-body-a-deferred`: `s 304C(5)(c) the act is unlawful`; `s 304C(5)(b) the household is the same household as B`; `s 335A(3) the act is unlawful`

**(a3) Definitions and conditions by "if", "whether or not", "has the same meaning" and "is to be understood", read as closed:** 13 branches.
  - `pc-body-b-deferred`: `s 376G(2) B is a close family relative of A`; `s 376H(3)(a) the representation is false`
  - `pc-body-b-deferred-images`: `s 377C(2) distributing requires that another person views or gains access to the image`; `s 377C(3)(d) the conduct is sexual`; `s 377C(3)(f) the person is doing a private act`; `s 377BD(4)(a) the person has the electronic image in his possession`; `s 377BK(3)(a) the person has the electronic child abuse material in his possession`; `s 377BN(3) Explanation the act has a legitimate purpose related to art`; `s 377BN(6)(b) the defence of marriage to a charge under section 377BI is made out`; `s 377BN(6)(c) the defence of marriage to a charge under section 377BJ(2) is made out`; `s 377BN(6)(d) the defence of marriage to a charge under section 377BK(1) is made out`
  - `pc-general-moved`: `s 29B the thing is an electronic record`; `s 49 the year or month is reckoned by the calendar`

**(a4) A defence "if" its limbs are met, read as not made out when they are not** (the defence functions answer `JUST FALSE` for "not made out", which is not "the accused is guilty"): 5 branches.
  - `pc-body-b-deferred-images`: `s 377BM(2) the defence of a protected purpose is made out`; `s 377BN(2) the defence of a protected purpose is made out`; `s 377BN(3) the defence of a legitimate purpose is made out`; `s 377BN(4) the defence of the child's own image is made out`; `s 377BN(6)(a) the defence of marriage to a charge under section 377BG(1) or 377BH(1) is made out`

### Reading (b): a prohibition or grant limited by its own wording does not count as the text's no

The branch answers `NOTHING`, with a comment naming what the wording is limited to.
**The other reading:** the wording is the whole of the text's answer, so a case outside it is the text's no (`FALSE`): for a grant, that the grant is not made; for an Explanation that presumes, that nothing is presumed; for a rule of reading, that the reading does not apply.
62 branches:
  - `pc-body-a-deferred`: `s 301(1) the description of the culpable homicide`; `s 304C(5)(a) the person who does not live in the household is a member of it`; `s 315(2) the effect of evidence of the length of the pregnancy`
  - `pc-body-b-deferred`: `s 372 Explanation the intent that she shall be used for prostitution`; `s 373 Explanation the intent that she shall be used for prostitution`; `s 376H(3)(b) the representation is express or implied`
  - `pc-body-b-deferred-images`: `s 377C(3)(a) the penetration is continuing`; `s 377C(3)(e) the observation is observation within the sections`; `s 377BB(9) the effect of the recording`; `s 377BG(3)(a) A has the care of the person below 16 years of age`; `s 377BM(1) the defence of unintended possession or access is made out`; `s 377BN(1) the defence of unintended possession or access is made out`
  - `pc-general-moved`: `s 2 the person is liable to punishment under this Code`; `s 3 where the act is taken to have been done`; `s 6 the provision is understood subject to the General Exceptions and the Right of Private Defence`; `s 6A the definition applies to the offence`; `s 7 the expression is used in conformity with its explanation`; `s 8 the pronoun is used of the person`; `s 22A the kind of element`; `s 32 the words extend to illegal omissions`; `s 33(1) the word (x6)`; `s 33(2) the person is regarded as having caused the effect by the series of acts`; `s 36 causing the effect partly by an act and partly by an omission is the same offence`; `s 38 the persons may be guilty of different offences`; `s 44A the words`; `s 45 the word`; `s 46 the word`; `s 47 the creature is an animal`; `s 48 the thing is a vessel`; `s 50 the portion is a section`; `s 53 Explanation the instrument may be used for caning`; `s 54 imprisonment for life is for the duration of the person's natural life`; `s 108B the person abets an offence`; `s 26C(3) the person intends or foresees the result`; `s 26C(4) the court may rely on the foresight to infer intention`; `s 79(2) the prosecution must prove the fault element`; `s 79 Explanation 1 the accused person is guilty`; `s 79 Explanation 2 the accused person needs to rely on the defence of mistake`; `s 79 Explanation 2 the accused person may allege the mistake to raise a reasonable doubt`; `s 79 Explanation 2 the prosecution must prove the fault element`; `s 79A(2) the prosecution must prove the fault element`; `s 80(2) the prosecution must prove the fault element`; `s 86(2) intoxication is taken into account`; `a Magistrate's Court's jurisdiction on the punishment prescribed` (two branches); `s 73(3)(a) a Magistrate's Court has jurisdiction`; `s 73(3)(b) a District Court has jurisdiction`; `s 74(3)(a) a Magistrate's Court has jurisdiction`; `s 74(3)(b) a District Court has jurisdiction`; `s 74A(4)(a) a Magistrate's Court has jurisdiction`; `s 74A(4)(b) a District Court has jurisdiction`; `s 74B(4)(a) a Magistrate's Court has jurisdiction`; `s 74B(4)(b) a District Court has jurisdiction`; `s 74C(4)(a) a Magistrate's Court has jurisdiction`; `s 74C(4)(b) a District Court has jurisdiction`; `s 74D(4)(a) a Magistrate's Court has jurisdiction`; `s 74D(4)(b) a District Court has jurisdiction`

### Not (a) or (b)

- **"includes", "denotes", "deemed to include", "include but is not limited to":** 24 branches answer `NOTHING` outside the list; the brief's own rule already gives that, and no reading of a lawyer's is needed unless a court would treat the list as closed.
- **Undefined or silent:** 9 branches answer `NOTHING` because a term is undefined in the Code or the text is silent.
- **Explicit "unless", "except", "other than", "means", "excludes":** answered `JUST FALSE` where the words are the text's own; not listed here because they are not marginal.

### Reading a result: FALSE and NOTHING

- **A ladder** (`offence under s N`, `commits ... within section N`, `exception under s N`) is BOOLEAN by the charge generator's contract. An element the investigator has not stated reaches it as FALSE, so a FALSE from a ladder means "the elements are not made out on the facts stated", never "the Code says no".
- **A decision function** (a rule of reading, a definition, a presumption, a jurisdiction rule) answers a MAYBE BOOLEAN, a MAYBE of a type, or a named constructor.
  - `JUST TRUE` and `JUST FALSE` are answers the text gives in its own words.
  - `NOTHING`, or a constructor such as `not covered by this Explanation`, `not covered by s 315(2)` or `not covered by section 377BB(9)`, is "the text does not say". It is not a "no".
- **A caller must never turn `NOTHING` into `FALSE`**, and must not read `NOTHING` as permission. A caller that shows a result to a person should show `NOTHING` as "not covered", with the reason in the branch's comment.
- **Function names carry the section**, so a result can be traced to the words that gave it.


## Jural relations

Hohfeld's eight terms, applied to the provisions of the four new modules.
A column says who holds the position and against whom.
The Code states its offences as liabilities ("shall be guilty", "shall be punished"), so the duty each offence implies is read from the liability, not stated in a free-standing clause. No lawyer has checked these assignments.

| provision (module) | position | holder | against | note |
| --- | --- | --- | --- | --- |
| the 47 offences of the deferred modules: ss 304B to 335A, 372 to 377B, 377BB to 377BO | duty not to do the act (and, in ss 304C and 335A, a duty to take reasonable steps to protect B) | the person described (A) | the State, which holds the claim-right | the Code gives B no private claim-right under these sections |
| the `punishment prescribed by s N` records | liability to the stated punishment on conviction | the accused | the court holds the power to impose it | |
| ss 2, 3, 108B | liability to punishment under the Code (s 2); the same for an act beyond Singapore by a person liable to be tried (s 3); and for an abettor (s 108B) | the person | the State's power to punish | s 2's "not otherwise" is the correlative disability: no other law's power applies to those acts |
| spouse and other bars: ss 376B(3), 376EB(4), 376ED(4), 376G(6), 304C(3) | immunity from conviction | the person within the bar | the State, which has a disability (no power to convict) | flat negatives: marginal reading (a) |
| defences: ss 377BM, 377BN | immunity from conviction when the defence is made out; the privilege to do the act for the stated purpose | the accused | the State | "It is a defence ... if" read as closed: marginal reading (a4) |
| "not a defence" and "not necessary to prove": ss 376A(1B), 376AA(2), 376G(5), 377BE(6), 377BN(5) | no immunity from B's consent or the accused's mistaken belief; B has a disability (B cannot, by consent, remove A's liability) | A; B | the State; A | |
| burden of proof: ss 79(2), 79 Explanations 1 and 2, 79A(2), 80(2) | duty of the prosecution to prove the fault element; claim-right of the accused that it be proved; privilege of the accused to allege a mistake | the prosecution; the accused | each other | Explanation 2 says the accused "may allege" it and "does not need to rely on" the defence |
| presumptions: ss 372 and 373 Explanations, 377BB(9) | liability of the accused to have an intent (or non-consent) presumed until the contrary is proved; power of the prosecution to rely on it | the accused; the prosecution | each other | rebuttable |
| jurisdiction: ss 73(3), 74(3), 74A(4), 74B(4), 74C(4), 74D(4) | power of the Magistrate's Court and the District Court to try and to impose the full punishment; liability of the accused to be tried and sentenced there | the court; the accused | each other | where a grant is limited by its wording the absence of power (a disability) is not asserted: `NOTHING`, marginal reading (b) |
| ss 5, 6, 6A, 7, 8, 9, 12, 17, 22A, 29A, 29B, 32, 33, 36, 42, 44A to 51, 53 Explanation, 54, 26C, 86(2), 86(3) | none: definitions and rules of reading change what other provisions mean and create no relation between persons | | | s 38 (several persons may be guilty of different offences) leaves each person's own liability as above |

## Findings of the completion pass

Numbered; each says what was seen, and how it was seen.

1. **No assertion failed on the first run of the three large tests modules** (a-deferred, b-deferred, b-deferred-images), 2,151 assertions then.
   This is not evidence that the L4 is right.
   The tests are generated from formulas over the leaves that the same agent wrote from the same reading of the text, so they find a slip between the reading and the L4 and cannot find a misreading of the text.
   That they can find a slip is shown by the 18 mutations in "Completion pass 2026-11-04", all caught.
   One more limit on "none failed on the first run": two expected values in the first draft of the hand-written cases for `pc-body-b-deferred` were wrong or unknown, and were corrected before the first run of those cases, not after a failure.
   The expected refusal of s 372 lacked its last clause, and was completed to end "; the elements of section 372 taken together."; the exact refusal of s 376C(2) was a guess, and was replaced by an assertion that the refusal is not empty.
   The Code has no refusal wording: the wording of a refusal is the module's own, in its `missing unless` lists, so these expected values were read from the module, not from the Code.
   The transcript of the run shows these two corrections and no others; it does not rule out an unlogged correction made before a first run in the other two modules.
2. **`NOT (a) AND NOT (b)` on one line is read as `NOT ((a) AND NOT (b))`**, on the stable build and on the main build. Silent: no diagnostic.
   Seen: the first draft of the Magistrate's Court helper in `pc-general-moved.l4` answered `JUST TRUE` for the record of s 302(2) (imprisonment for life, no term of imprisonment) where the text gives `NOTHING`; the two assertions written from the text for that record failed.
   Isolated: `#EVAL NOT (FALSE) AND NOT (TRUE)` prints TRUE, and `#EVAL (NOT (FALSE)) AND (NOT (TRUE))` prints FALSE, on 1.6.98 and on 1.6.108.
   Repaired in the code, with a single `NOT` that is the whole of its condition; the assertions were not touched.
   In a `...` chain the same two `NOT`s on separate lines read as intended (probed with all four combinations on both builds).
   A scan of all 31 encoding modules (comments, quoted strings and backticked names stripped) for a `NOT` followed on the same line by `AND` or `OR` found three lines, all in modules of 0.1.0 (`pc-body-a-life.l4` line 506, `pc-body-b-kidnapping.l4` line 522, `pc-property-mischief.l4` line 1103); in each the `NOT` is applied to a parenthesised group or is itself parenthesised, so each reads as intended.
3. **`pc-body-b-deferred.l4` had drifted from its generator.** Eight lines of `@desc` text and one header comment said "as s 377C(2) says" and pointed at functions named `s 377C(2) the communication is sexual` and its siblings, which do not exist; the definition of "sexual" is `s 377C(3)(d) the conduct is sexual`. Found by rebuilding the module from `build_b1.sh` into a scratch copy and diffing it against the file. The file was rebuilt from the generator, so the text is right; the tests do not depend on `@desc` text and did not change.
4. **What the stable binary does not accept**, sorted by how the failure shows.
   *Loud (an error):* `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` do not exist (the three refusals of 0.1.0 were rewritten as `NOTHING` for that reason); `IMPORT` finds only modules in the same folder; a name defined in two imported modules cannot be used ("multiple definitions"); `ELSE IF` chains on new lines break layout, so `BRANCH ... OTHERWISE` is used.
   *The brief's two rules, both followed in the final files:* every `NOT` is parenthesised (`NOT (x)`) and every `#ASSERT` is on one line. A scan late in the pass found 15 `NOT`s in module code and 227 in the three large tests modules that were not parenthesised (the harmless forms `X AND NOT Y` and `#ASSERT NOT f x`); they were parenthesised through the generator sources (`gen_offences.py`, `gen_defs.py`, `gen_struct_tests.py` and the hand test sources), the modules and tests were rebuilt, and `check.sh` was run again. A scan of the eight new files (comments, `@desc` text, quoted strings and backticked names stripped) finds none unparenthesised now.
   *Quiet (a warning, which `check.sh` does not count):* a parenthesised group that mixes an AND at its top level with an OR at its top level, starting at the same column inside one `...` chain, draws a linter warning; the OR-top-level groups are at column 11 and the AND ones at column 9. `l4 run` on each of the four new modules and each of the four new tests modules printed no Warning-severity diagnostic.
   *Silent (a wrong answer, exit 0):* finding 2 above; `l4 check` does not evaluate `#ASSERT`, so a module that "checks" can carry failing assertions and only `l4 run` shows them; `l4 run` exits 0 when an assertion fails (hence `check.sh` counts the lines after `Message:`).
   The source's curly quotes and em dashes were kept in the quotation lines; both builds accept them in comments, and `srcrefs.py` reports 0 problems.
5. **The old totals did not add up, and the repealed count was wrong.** 443 + 29 + 72 + 42 = 586, not 600. The text marks 75 sections `(Repealed)`, not 72, and all 75 show "[Repealed by ...]" in the body. The script's tally of the old coverage rows is 454 encoded, 1 partly (s 377C), 41 deferred, 29 inert, 75 repealed.
6. **20 of the text's 61 defined-term entries have no function named for them**, all in sections this pass did not encode (ss 4B, 73, 74, 74A, 292B, 305, 377CB, 379A, 409, 427). Found by a name search; see "Coverage".
7. **The scope of the six jurisdiction subsections is an input**, not wired to `enhanced penalty under s N` (DEF-M7).
8. **`check.sh` equal counts do not show equal traces.** Every module has the same four counts on the 1.6.98 and 1.6.108 builds; the script says itself that it does not see a different `#TRACE` outcome, and none of the new modules uses one.
9. **The two failures of 0.1.0 stand** (`pc-general-part-tests.l4`, forks GP-14 and GP-10): findings about the Code, left red on purpose, and listed in `encoding.json` under `expected_red`.

## What the text does not answer

Questions this pass met and the text does not settle. Each is an input, a `NOTHING`, or a registered fork.

- Which punishment of s 304B(1)(a) or (b) the court gives, and when (DEF-A2).
- Whether s 304C(3) bars the whole offence or only the second alternative of (1)(d) (DEF-A4); whether "unlawful" in ss 304C(5)(c) and 335A(3) is closed (DEF-A5).
- What "quick" means in s 316 (DEF-A8); what a "group" is (the Organised Crime Act 2015, DEF-A6); what an "electronic record" is (s 29B, the Electronic Transactions Act 2010); what a "sexual offence" is (ss 304C, 335A, the Criminal Procedure Code 2010 s 2(1)); when a person is "liable by law to be tried" for an act beyond Singapore (s 3). None of those Acts is in the sources, so each is an input.
- Whether the spouse bar of s 376ED(4) covers both offences of that section (DEF-B4); whether a presumption in the Explanations to ss 372 and 373 is an element (DEF-B1).
- Which underlying offence a charge under s 377BO is framed under when the facts make out more than one (DEF-B7: the order of the text's list was taken).
- Whether "caning shall be with a rattan" forbids another instrument (s 53 Explanation, DEF-M3).
- Whether a court that has no jurisdiction under "where ... twice the maximum term ... does not exceed 5 years" lacks it (DEF-M2), and what an offence punished with death alone does to that test (the literal reading is `JUST TRUE`; the scope of the sections excludes such offences).
- Whether "denotes" and "includes" close the term they define (taken as not closed everywhere except where the words are "means").
- Which offences are within ss 73(1), 74(2), 74A(3), 74B(2), 74C(2) and 74D(2) for the jurisdiction subsections: the text lists them, and this pass takes the answer as an input (DEF-M7).

## What `check.sh` prints

Run from this folder, 2026-11-04, with `L4=<1.6.98 stable> L4_MAIN=<1.6.108 stable> ./check.sh` and `JL4_LIBRARY_PATH` unset (log: `deposit/logs/final.check.log`), exit 0:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
TOTAL (44 modules)   errors 2   satisfied 3751   failed 2   refused 0   |  main: errors 2  satisfied 3751  failed 2  refused 0
```

Every one of the 44 modules reads `same` on the main build.
The two errors are the two expected failures of `pc-general-part-tests.l4` (finding 9).
**Replaced:** the baseline of the start of the pass, 36 modules, errors 2, satisfied 1390, failed 2, refused 0.
**Added:** 8 modules and 2,361 satisfied assertions (3,751 = 1,390 + 2,361); every baseline number still holds.
Per module: `pc-body-a-deferred-tests` 429, `pc-body-b-deferred-tests` 1,018, `pc-body-b-deferred-images-tests` 706, `pc-general-moved-tests` 208, each with 0 errors, 0 failed, 0 refused; the four new encoding modules 0 errors.
All 31 non-test modules import together into one file with 0 errors on both builds; that alone does not catch a name defined twice, which only errors when the name is used, so a text scan of every defined name (1,640 names) was run as well and found none duplicated.
The counts are errors and assertion lines, nothing else (see finding 8).
`python3 -I srcrefs.py check --refs` and `check --strict`, each over all 44 `pc-*.l4` files with the raw file `PC1871.txt`, report 1,400 `src:` lines, 83 runs, 397 locators, 0 problems (the 1,400 lines are the four new modules' 217 + 403 + 555 + 225, so no other file carries a `src:` line).
The first `--strict` run, made by the lead after the pass, found 24 problems that `--refs` does not look for: 20 in `pc-general-moved` and 4 in `pc-body-b-deferred-images`.
Eight were a quotation above a `DECLARE` with no `@ref` of its own; sixteen were a section quoted once for several functions, whose first `@ref` was narrower than the quotation (or, for the Magistrate's Court helper of ss 73(3) to 74D(4), sat above its quotation).
Each is mended by one `@ref Penal Code 1871 s N (src:@@)` line, which cites the whole quotation, placed first in the block, ahead of the narrower `@ref` of the first function: 19 in `pc-general-moved` (the s 73(3) quotation was also moved above the helper), and in `pc-body-b-deferred-images` 3 added (ss 377C, 377BM, 377BN) and the `@ref` of the s 377BO record widened from src:9837-9883 to src:9835-9903.
No rule, name or assertion changed, the quotation lines are the same 1,400, and the 13 tests modules are byte-identical (md5 before and after); the two modules were rebuilt from `generators/deferred/moved.in` (`autoq.py`, `expand.py`) and `build_images.sh`, whose sources carry the change (`whole=True` in `spec_defs_b4.py`, read by `gen_defs.py`; the s 377BO line in `after_b4_hand.l4`).

## Before anyone relies on this

- **A Singapore criminal lawyer reads the 0.2.0 modules against the official text.** SSO's text is an unofficial consolidation, and the file read here is a converter's plain-text rendering of it, "Current version as at 09 Sep 2026". Nothing here has been read by any domain expert.
- **The two marginal readings are put to a lawyer** (a failed "if" and flat negatives as the text's no; a limited grant as not the text's no), and the FALSE/NOTHING rule of 2026-10-29, which is assumed and not ruled.
- **An independent test pass.** The 2,361 assertions of 0.2.0 were written by the agent that wrote the code (finding 1).
- **The scope of the jurisdiction subsections is wired** to the existing `enhanced penalty under s N` records, or ruled to stay an input (DEF-M7).
- **The charge generator's catalogue is updated** for the 47 new `charge under s N` items; 0.1.0 chose not to touch it and 0.2.0 did not either.
- **The stale statements are corrected**: the comments listed in "Where things are" and the `notes/<group>-coverage.md` rows, which still say `deferred` and `inert`.
- **The 20 defined-term entries without a function** (finding 6) are looked at.
- **The Code is checked for amendment after 09 Sep 2026.**
- **This encoding is not a cleanroom**: the encoders of 0.1.0 read the `legalese` row as the pattern for the charge generator's contract, and the 0.2.0 modules follow 0.1.0's conventions.

## Generators and checkers used and not shipped

`check.sh.pass1` is a byte-for-byte copy of the `check.sh` that the 0.1.0 row of this encoding shipped (1,754 bytes), kept during the run and used as a time stamp (see "Changes to existing modules" above); it is not in this folder.
The `check.sh` in this folder is the current one, which also runs every module on a main build; the 0.1.0 one is in the history of this repository.

## Bench rulings on negatives and legal effects

**Bench rulings of 2026-11-04** (full text in `docs/ENCODING-GUIDE.md` section 5; they apply to every fork and reading recorded for this row).
These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

## Independent test pass

A separate agent that had not seen this encoding's `NOTES.md`, `PROGRESS.md`, brief or tests wrote `ANSWERS.md` from the text of the Code alone before it opened any `.l4` file: 475 numbered scenarios (478 answers; 86, 209 and 474 carry two) over the 42 sections that the earlier row listed as deferred, at least two for each.
It then wrote `tests-independent.l4`: 583 assertions, and ran it with the stable binary.
`ANSWERS.md` is not kept in this folder; the numbers in the comments of `tests-independent.l4` refer to it.
The author was given the family's rule for "no" and "not said" in its brief (see "Reading a result: FALSE and NOTHING" above) and wrote its expected values by it; it departed from the rule's letter in two places, and every one of the nine failures below comes from them.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run, against the modules as deposited | 583 | 574 | 9 | 0 |
| after the reconciliation below | 583 | 583 | 0 | 0 |

**There were no encoder defects, and nothing in the modules was changed on account of this pass.**
All nine failures are the encoding answering `NOTHING` where the author expected `JUST FALSE`.
They come from two disagreements.
The first is a place where the family's convention gives opposite answers for "means" and for "includes" within one definition.
The second is the second of the two readings that the 2026-10-29 rule leaves for a lawyer (a prohibition or grant limited by its own wording is not counted as the text's no).
No ruling has been made on either.
Each reconciled assertion carries a `-- RECONCILED` comment quoting what the author wrote.

- **Three were one genuine fork, s 377BE(5), reconciled to the encoding's `NOTHING` (scenarios 341, 343 and 348, which use one input vector).**
  The subsection says "intimate image or recording" "means" the things in paragraph (a) and "includes" altered or generated images in paragraph (b), "but excludes" one that no reasonable person would believe depicts B.
  For an image under neither limb (a blouse over the breasts, a bare male chest, a face only) the author expected `JUST FALSE`, because "means" closes the list; the encoding answers `NOTHING`, because the definition carries an "includes" limb, and says so in a comment in its tests ("none of the limbs: 'means ... and includes' does not say that anything else is not one").
  The author's report called its own scenario probably wrong under the letter of the convention, and also said that `NOTHING` for "face only, clothed" is odd in practice, and that the convention gives opposite answers for "means" and for "includes".
  **Which reading is right is for a lawyer.**
- **Six were one convention disagreement, reconciled to the encoding's `NOTHING` (scenarios 399, 400 and 415, and 401, 402 and 414).**
  s 377BM(1) and s 377BN(1) give a defence "for the accused person to prove that" (a) the accused did not intentionally come into possession or gain access, and (b) on becoming aware took all reasonable steps to cease.
  Where only one of the two is proved (399, 400, 415), and where the charge is under a section other than the one the defence names (401, 402, 414), the author expected `JUST FALSE`; the encoding tags the branch "NOTHING-kind (limited by its own wording)": the text says what the accused can prove to have a defence, and does not say that one who cannot prove it, or who is charged under another section, has none.
  The same encoding answers `JUST FALSE` for the sibling defences that open with "if" (s 377BM(2); s 377BN(2) and (3)), and the author's assertions on those pass (scenarios 404 to 409 and 417 to 421).
  The author named that difference as its finding: an unproved purpose defence is "not made out" and an unproved possession defence is "not said", though both functions are called "... is made out".
  **This difference, and the six assertions, are the first thing for a lawyer to look at.**

**The gaps.**
25 scenarios have no assertion; each is kept as a `-- GAP` line at the end of the file with the author's reason (209 has an asserted half, 209b).
By the author's grouping:
nine scenarios turn on a term the text leaves undefined or defines elsewhere, which the encoding takes as one `BOOLEAN` input and so cannot answer "not covered" for (6, 58, 67, 78, 92, 109, 147, 196 and 397);
ten turn on an age, a sex or a place of residence that is folded into one `BOOLEAN` leaf, so the edge cannot be asked (the ages of A at 17 and at exactly 18 in ss 376E, 376EB and 376ED: 165, 166, 198, 199 and 226; "member of the employer's household": 21 and 22; "woman" in s 373A with s 10, and "breasts if B is female" in s 377BB(4): 132, 133 and 300);
and six ask for something the encoding does not model as a function (the split of limbs (a) and (b) of s 304B(1) into separate punishments: 26; the rule that the prosecution need not prove which alternative: 36; the rebuttal of the presumption in the Explanation to s 372: 118; the punishment of s 376C(2), which is that of s 376B: 155; the immateriality of the place of an earlier occasion in s 376E(3): 179; the proviso to s 376EB(2)(b): 209a).

**What the author could not decide from the text** (for comparison with the fork register):
whether the lists in s 304C(5)(c) and s 335A(3), "unlawful act ... is one that", are closed (the author took them as closed);
what happens to guilt under the proviso in ss 376EB(2)(b), 376EC(2)(b), 376ED and 376EE when neither A nor B is in Singapore;
whether "B is a close family relative of A if B is ..." in s 376G(2) closes the list (the convention says so; strict logic would not);
the presumption in the Explanations to ss 372 and 373, which is stated for a female and silent on a male;
a termination "subject to the Termination of Pregnancy Act 1974" in ss 314 and 315, which points outside the Code;
the heading of s 377B ("living animal") against its operative text ("animal"), which s 47 settles for a dead animal;
the maximum term for a victim below 14 in ss 377BB(8), 377BC(3) and (4), 377BD(2), (3), (6) and (7), and 377BE(3) and (4), where the limbs change and the maximum does not rise;
whether the purposes in s 377BM(2)(a) are a closed list (the author took them as closed);
whether "domestic worker" in s 304C(1)(a) must meet the s 73(4) definition;
the two definitions of "image" in s 377C(1);
whether A's intent in s 376E(1)(b)(i) must exist at the time of the acts (the author required it);
and whether the negative in s 304C(3) applies to the whole offence where A killed B (the author said the encoder applies it to the whole offence).

**Independence, as far as it went.**
The author did not open `NOTES.md`, `PROGRESS.md` or the brief, any other encoding, or any other run's directory.
It opened the modules to learn names and types only after `ANSWERS.md` was written; their header comments, which mention the fork identifiers DEF-A1 to DEF-A5, were in front of it.
After the run it also read the encoder's reasoning comments on s 377BE(5), s 377BM(1) and s 377BN(1), to diagnose the nine failures.
It changed the expected answer of scenario 293 (a dead animal under s 377B) from "not covered" to "no" after a field name in the encoding (`the creature is an animal within section 47`) made it read s 47; the change rests on the text of s 47, and a revision note is in its `ANSWERS.md`.
It changed scenarios 215 and 236 to "yes" before it opened any `.l4` file.
The harness loaded the author's context with user-level project instructions and a memory index without being asked; the author opened no memory file and used none of it.
