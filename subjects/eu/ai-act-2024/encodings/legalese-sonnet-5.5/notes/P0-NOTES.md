# NOTES: the seat layer P0 (Articles 1 to 4, 111 and 113, and Annex X) of the EU Artificial Intelligence Act

Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744, in L4 on the stable binary.
This is layer 2: nine seat modules and their case files.
The keel's modules (`aia-*.l4`) are read-only, are imported, and were not edited or copied.

## Status

Written and verified on 2026-11-17.
How each claim below was verified:

- **Gate.** `L4=<1.6.110 build> L4_MAIN=<1.6.109 build> ./check.sh` exited 0 with all 24 modules `same`: 950 assertions satisfied, 0 failed, 0 refused, 0 errors, on both builds.
- **Citations.** `python3 -I srcrefs.py check --refs` and `check --strict` over the eighteen `P0-*.l4` files report 0 problems (269 quote lines, 158 runs, 215 locators).
- **Traces.** All 66 `#TRACE`s were compared with their `-- EXPECT` line and between the two builds by `work/tracecheck.py`: 0 differences in the full result text, 0 expectations missed.
  `check.sh` cannot see a trace difference, so this is the check that covers it.
  The scripts (`tracecheck.py`, `mirror.py`, `lint.py`, `cov.py` and the generator) are scratch tools in the run's `work/` folder, outside this deposit.
- **Positive control.** Two expected values were flipped in a scratch copy of a case file; the run reported two `eval/assertion-failed` errors.
  So the harness can fail, and a clean first run is not a harness that never reports.
- **Expected values** were decided from the text before the files were run, and each is written beside its assertion with the words that license it.
  No assertion was edited to match the code, and none failed.
  The second-pass seat audit of 2026-11-17 retitled five questions; each of their 22 assertions keeps its facts and expected value and carries a `-- RECONCILED 2026-11-17` line with the old text (see `## Seats (P0)`).
- **Not done.** The Interact form and `jl4-service` were not run; the exported questions were evaluated through `l4 batch` for three of them (a date question, an Annex X question, a regulative rule), which returned `true`, `2030-12-31` and `<obligation>`.
  No lawyer has reviewed any reading here: every reading below is assumed, not ruled.
- **Commencement is IN** for this Regulation (assumed, not ruled).
  The consolidated text is a rendering that says it has no legal effect (line 2 of the file).

### Counts

| seat | questions | assertions | traces |
| --- | --- | --- | --- |
| person | 11 | 55 | 0 |
| provider | 39 | 248 | 21 |
| deployer | 33 | 175 | 16 |
| importer | 16 | 102 | 6 |
| distributor | 15 | 100 | 6 |
| rep | 12 | 85 | 6 |
| manufacturer | 13 | 94 | 6 |
| gpai | 14 | 67 | 5 |
| notified | 5 | 24 | 0 |
| total | 158 | 950 | 66 |

Thirty-six `-- MIRROR` groups tie cases of different seats together (the same facts asked from two or more seats, with answers that agree).
`work/mirror.py` found every group in at least two seats and no disagreement.

## Reading a result

A question's answer is the keel function's answer, passed through unchanged.
**Loud failures** (they tell you something is wrong):

- A missing input, a wrong type or an unknown name is an error from `l4 run` or `l4 batch`.
- A failed assertion in a case file shows `eval/assertion-failed` at severity Error (but see the first finding below: the exit status is still 0).

**Silent failures** (an answer comes back, with exit code 0 and no diagnostic, and it can be wrong):

- **`NOTHING` is "not covered", not "no".**
  It is the answer before the provision applies (before 2 February 2025 for the questions of Articles 2 and 4; the Article 3 definitions are not gated by Article 113, so only 3(14), 3(14a) and 3(14b) take a date, to select the text), when the text in force on the date asked has no such paragraph (Article 2(13), Article 3(14a), 3(14b), Article 4(2) and Article 111(4) before 27 July 2026), and when the facts fall outside a limit the text sets.
  `JUST FALSE` is the text's own "no".
- **A misspelt Annex X act reads as "not an Annex X system".**
  Under Article 111(1) the act is a `STRING`; a trailing space, lower case or a letter O for a zero gives `NOTHING` with status success and no diagnostic (checked with `l4 batch` on 2026-11-17).
  Write the act exactly as the `@desc` lists it.
- **The seat assumes its role.**
  A question asked by someone who does not hold the role (a distributor asking a provider's question) is answered as if they did; only the Article 3 role question checks the role.
- **The date asked is the whole of the time axis.**
  Giving a date before the Regulation exists, or the wrong side of 27 July 2026, silently selects another text.
- **A regulative answer is not shown as text.**
  An exported obligation prints as the placeholder `<obligation>`; its content is read with `#TRACE`.
  A trace of an obligation that is still pending prints as `PARTY ... MUST ... HENCE FULFILLED` (the residual obligation), not as a word such as OPEN; the case files call that state OPEN in their `-- EXPECT` lines.
- **Article 4(1) has no breach path.**
  Its traces end FULFILLED or still pending, never BREACH: the text states no time limit and no consequence.
  The second sentence of Article 2(8) is a "shall" with no deadline and no consequence too, so its question only says that the duty exists.
- **`TRUE` in the Article 111(2) saving question means the system is saved**, that is, the Regulation does not apply to its operator under the "only if".

## What the stable binary does not accept

Findings from this run (each reproduced on 2026-11-17 on the 1.6.110 build):

1. **`l4 run` exits 0 when an assertion fails.**
   A failed assertion is reported as `eval/assertion-failed` at severity Error, and the process still exits 0.
   A gate must read the diagnostic codes, as `check.sh` does; an exit-code check alone would pass a file whose assertions all fail.
2. **`l4 batch` cannot read a file that contains a multi-line `#TRACE`.**
   Batch re-prints the module and fails with `parse/unexpected-number` on the directive's continuation line, in a file it names `<file>.batch1.l4`.
   The seat modules carry no `#TRACE` (the traces are in the case files), so they batch cleanly.
3. **The entry point for `l4 batch -e` is the `DECIDE` name, without the question mark** that the `@export` line carries.
   Using the `@export` text gives "no @export function named ... found".

## Seats (P0)

One row for each provision of the keel's ranges.
The question name is `Under Article N, as <role phrase>, <text>?`; the table gives N and the text.
Every question below has `@export`, `@desc` and `§` grouping in text order, and cases on both sides of each date it depends on.

Seat audit (second pass): 158 questions read, 5 retitled (direction 0, subject 5)

What the second pass did: each question's name and `@export` text were read against the body of the keel function it calls (every function called was read in its own file: all of aia-scope and aia-literacy, the Article 111 and Article 113 functions of aia-timeline, the called definitions of aia-definitions, and the one Annex X function in aia-annex-x).
No direction mismatch exists: every function is named for the positive reading (`applies`, `affects`, `prejudices`, `precludes`, `may be limited`, `is saved`, `is a ...`) and answers `JUST FALSE` or `FALSE` for the text's "no", and every question asks the same positive question.
The five subject mismatches are in Art 2(1): in limbs (b), (c), (f) and (g) the keel function answers for a narrower party than the old name asked about, and a fact outside the limb (a deployer established in a third country, a provider established in the Union, a representative of a provider established in the Union, a person located outside the Union) comes back `NOTHING` although another limb of the same paragraph may give a plain yes.
Each was retitled to name the party the function answers for; negating an answer was not used, and no `NOTHING` became `JUST FALSE`.
The new names, exactly:

- `Under Article 2(1)(b), as a deployer of an AI system, does the Regulation apply to me as a deployer established or located in the Union?`
- `Under Article 2(1)(c), as a provider of an AI system, does the Regulation apply to me as a provider established or located in a third country because the output of my AI system is used in the Union?`
- `Under Article 2(1)(c), as a deployer of an AI system, does the Regulation apply to me as a deployer established or located in a third country because the output of my AI system is used in the Union?`
- `Under Article 2(1)(f), as an authorised representative, does the Regulation apply to me as an authorised representative of a provider not established in the Union?`
- `Under Article 2(1)(g), as a person affected by an AI system, does the Regulation apply to me as an affected person located in the Union?`

Questions read and left as they were include the ones a keyword search would flag: Art 2(5), 2(9) and 2(11) ("does the Regulation affect / prejudice / preclude", answered `JUST FALSE` for "no"), Art 2(8) second sentence and Art 2(13) ("must" and "may", answered `JUST TRUE` for "yes"), Art 4(1) last sentence ("must I guarantee", answered `JUST FALSE` for "no"), Art 111(2) first sentence ("is my system saved", `TRUE` for saved) and the regulative questions ("what must I do", each answering the duty of the party the seat holds: the operator for Art 111(1), the provider or the deployer for Art 4(1) and Art 111(2), the model provider for Art 111(3), the provider for Art 111(4)).
No question was renamed to negate its answer.

| provision | seats | question text, or `none` and the reason |
| --- | --- | --- |
| Art 1 (1) purpose and (2) contents | all nine | Article 1: `does Chapter I apply on the date asked`. The article creates no rule; the one question a seat asks of it is whether the Chapter it opens applies (Art 113(a)). |
| Art 2(1)(a) | provider, gpai | `does the Regulation apply to me` (the model provider is a provider). |
| Art 2(1)(b) | deployer | `does the Regulation apply to me as a deployer established or located in the Union`. |
| Art 2(1)(c) | provider, deployer | `does the Regulation apply to me as a provider (deployer) established or located in a third country because the output of my AI system is used in the Union`. |
| Art 2(1)(d) | importer, distributor | `does the Regulation apply to me`. |
| Art 2(1)(e) | manufacturer | `does the Regulation apply to me` (also the manufacturer's role question). |
| Art 2(1)(f) | rep | `does the Regulation apply to me as an authorised representative of a provider not established in the Union`. |
| Art 2(1)(g) | person | `does the Regulation apply to me as an affected person located in the Union` (also the person's role question). |
| Art 2(1), notified body | notified | `none`: limbs (a) to (g) name providers, deployers, importers, distributors, product manufacturers, authorised representatives and affected persons, and no limb names a notified body. |
| Art 2(2) | the six operators | `does the provision I name apply to my high-risk AI system with Section B products`. |
| Art 2(3), first subparagraph | provider, deployer | `does the Regulation apply to the matter outside the scope of Union law`. |
| Art 2(3), second subparagraph | the six operators | `does the Regulation apply to the AI system used exclusively for military, defence or national security purposes`. |
| Art 2(3), third subparagraph | provider, deployer | `does the Regulation apply to the AI system not placed on the market in the Union whose output is used exclusively for military, defence or national security purposes`. |
| Art 2(4) | deployer | `does the Regulation apply to me as a public authority in a third country or an international organisation`. |
| Art 2(5) | provider, deployer | `does the Regulation affect the application of the provisions on the liability of providers of intermediary services`. |
| Art 2(6) | provider, deployer; gpai | `does the Regulation apply to the AI system developed for the sole purpose of scientific research and development` (gpai: `the AI model`). |
| Art 2(7) first sentence | provider, deployer, person | `does Union law on the protection of personal data, privacy and the confidentiality of communications apply to ...`. |
| Art 2(7) second sentence | provider, deployer, person | `does the Regulation affect the Union data protection instruments through the provision I name`. |
| Art 2(8) first and third sentences | provider, gpai | `does the Regulation apply to my research, testing or development activity`. |
| Art 2(8) second sentence | provider, gpai | `must my research, testing or development activity be conducted in accordance with applicable Union law`. |
| Art 2(9) | person, manufacturer | `does the Regulation prejudice the rules of another Union legal act related to consumer protection or product safety`. |
| Art 2(10) | deployer, person | `does the Regulation apply to my obligations as a deployer who is a natural person ...` (person: `to the obligations of a deployer who is a natural person ...`). |
| Art 2(11) | person | `does the Regulation preclude a law or collective agreement that is more favourable to me as a worker`. |
| Art 2(12) | the six operators | `does the Regulation apply to the AI system released under a free and open-source licence`. |
| Art 2(13), the limit | provider, manufacturer, importer, distributor, rep | `may the application of the requirement or obligation I name be limited`. |
| Art 2(13), last sentence | none | "By 2 August 2027, the Commission shall adopt delegated acts": the duty is the Commission's, and no seat acts or is benefited (the keel carries the rule and its deadline). |
| Art 3 chapeau; 3(2), 3(12), 3(13), 3(15) to 3(21), 3(24) to 3(48), 3(50) to 3(62), 3(64) to 3(68) | none | every other Article 3 term is called inside the part agents' questions (and 3(21) inside the notified body's 3(22) question); a seat has no use for the answer on its own. |
| Art 3(1) | provider, deployer, person | `is my software an AI system` (deployer: `is the software I use ...`; person: `is the system that affects me ...`). |
| Art 3(3) | provider, gpai | `does the definition of a provider fit me` (gpai in the model wording). |
| Art 3(4) | deployer | `does the definition of a deployer fit me`. |
| Art 3(5) | rep | `does the definition of an authorised representative fit me`. |
| Art 3(6) | importer | `does the definition of an importer fit me`. |
| Art 3(7) | distributor | `does the definition of a distributor fit me`. |
| Art 3(8) | all nine | `am I an operator` (the seat fixes the role; no fact is asked; person and notified body answer FALSE). |
| Art 3(9) | provider, importer, gpai | `is my supply of the AI system (the general-purpose AI model) a placing on the market`. |
| Art 3(10) | importer, distributor | `is my supply a making available on the market`. |
| Art 3(11) | provider | `is my supply a putting into service`. |
| Art 3(14) | provider, manufacturer | `is my component a safety component` (both texts). |
| Art 3(14a), 3(14b) | provider, deployer, gpai | `am I a micro, small or medium-sized enterprise`; `am I a small mid-cap enterprise` (as amended only). |
| Art 3(22) with 3(21) | notified | `does the definition of a notified body fit me`. |
| Art 3(23) | provider, deployer, importer, distributor, notified | `is the change a substantial modification`. |
| Art 3(49) | provider, deployer, importer, distributor, person | `is the event a serious incident`. |
| Art 3(63) | gpai | `is my model a general-purpose AI model`. |
| Art 4 heading | none | inert: a heading. |
| Art 4(1) | provider, deployer | four questions: `do I owe the duty to take measures regarding AI literacy`; `do my measures meet the duty ...`; `must I guarantee a specific level of AI literacy of an individual`; `what must I do about AI literacy on the date asked` (the regulative rule). |
| Art 4(2) | provider, deployer | two questions, one for each sentence: support and facilitation; practical examples. |
| Art 4(3) | none | addressed to the Board, to support the Commission and the Member States: it neither binds nor benefits a provider or a deployer, whose side of the matter is Art 4(2). |
| Art 111(1) first subparagraph | the six operators | `by what date must the AI system be brought into compliance with the Regulation`; `what must I do to bring the AI system into compliance on the date asked`. |
| Art 111(1) second subparagraph | none | addressed to whoever evaluates each large-scale IT system under the acts of Annex X; it creates no duty or entitlement for an operator. |
| Art 111(2) first sentence | the six operators | `is my high-risk AI system saved from the application of the Regulation`. |
| Art 111(2) second sentence | provider, deployer | `by what date must I take the necessary steps to comply with the requirements and obligations`; `what must I do to comply ... on the date asked`. |
| Art 111(3) | gpai | `by what date must I take the necessary steps to comply with the obligations laid down in the Regulation`; `what must I do to comply ... on the date asked`. |
| Art 111(4) | provider | `by what date must I take the necessary steps to comply with Article 50(2)`; `what must I do to comply with Article 50(2) on the date asked`. |
| Art 111, group General | all nine | Article 111: `does General apply on the date asked` (the first Article of this range in the group General). |
| Art 113 first paragraph | none | entry into force: no seat acts on it; every applicability question reads it through the keel. |
| Art 113 second paragraph, point (a) (Chapter I) | all nine | the Article 1 question above. |
| Art 113 second paragraph (General) | all nine | the Article 111 question above. |
| Art 113(a) Chapter II and the Article 5 additions, (b), (c), (d) | none | other groups: the part agents write their applicability questions. |
| Annex X | none of its own | a list of twelve acts that creates no rule; it is called inside Art 111(1) (the operator of an Annex X component asks Art 111(1)), so no `Under Annex X point M` question exists. |

## Fork register (P0)

Each reading this layer took, with the other reading and the text that licenses the one taken.
All are assumed, not ruled.
Line numbers are lines of `eu-ai-act-2024-1689-consolidated-20260727.txt`.
The keel's own forks (F-2-order, F-2-1-f, F-2-13, F-3-1, F-3-3, F-3-14, F-3-22, F-4-1, F-111-1-party, F-111-2-nothing and the rest of its register) are taken as they stand and are not decided again here.

- **P0-1, Art 3(8) asked of all nine seats.**
  Question: `am I an operator`, with the role fixed by the seat and no fact asked; person and notified body answer FALSE.
  Other reading: ask it only of the manufacturer, the one seat whose role Article 3 does not otherwise define, or of no seat.
  Licence: "'operator' means a provider, product manufacturer, deployer, authorised representative, importer or distributor" (line 73) and the brief's table, which lists operator 3(8).
- **P0-2, Art 2(4) asked of the deployer seat only.**
  The paragraph names the authorities and organisations that "use AI systems" (line 46).
  Other reading: also the person seat, as the party whose rights the safeguards protect.
- **P0-3, Art 2(5) asked of the provider and deployer seats.**
  A provider or deployer may also provide an intermediary service; this layer has no seat for a provider of intermediary services (line 47).
  Other reading: no seat at all.
- **P0-4, Art 2(9) asked of the person (consumer protection) and the manufacturer (product safety).**
  Licence: "without prejudice to the rules laid down by other Union legal acts related to consumer protection and product safety" (line 53).
  Other reading: every operator.
- **P0-5, Art 2(10) asked of the deployer and of the person.**
  The deployer asks about its own obligations; the person asks the same relation from the other side (line 54).
- **P0-6, Art 2(11) asked of the person only.**
  The paragraph protects workers; the brief asks a limit's question of the seat it helps (line 55).
  Other reading: also the deployer, as the employer whose use of AI systems is regulated.
- **P0-7, Art 2(12): "placed on the market or put into service as a high-risk AI system" is read from the route.**
  The question asks the route (the keel's seam S1) and passes "high-risk" as "the route is not `Route neither`"; Article 5 and Article 50 are yes/no facts (line 56).
  Other reading: ask "is the AI system high-risk" as a separate yes/no.
  Split site (an "unless" once it is met): the keel answers `NOTHING` when any of the three "unless" facts holds, because the exclusion then does not operate.
  Relies on `inputs/ENCODING-GUIDE.md` section 5, line 95: "Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met"; and line 87: "Everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit."
- **P0-8, Art 2(13) not asked of the deployer.**
  The ranges "Articles 9 to 15 and 17 to 25" (lines 58 to 61) leave out Article 26, the deployer's own obligations (HEADINGS.md: Article 23 importers, Article 24 distributors, Article 25 value chain, Article 26 deployers).
  Other reading: ask the deployer too, because Article 25 can make a deployer a provider.
- **P0-9, Art 3(9) asked of the provider, the importer and the model provider; 3(10) of the importer and the distributor; 3(11) of the provider.**
  Licence: the definitions of placing on the market (line 74), making available (line 75) and putting into service (line 76).
  Other reading: every operator for each.
- **P0-10, Art 3(14a) and 3(14b) asked of the provider, the deployer and the model provider.**
  The SME and small mid-cap facts matter to those who are supported or fined by size; the other operators' use is inside the part agents' questions (lines 82 and 83).
  Other reading: every operator.
- **P0-11, Art 3(23) and 3(49) asked of the seats that could state the facts.**
  Substantial modification: provider, deployer, importer, distributor and notified body.
  Serious incident: provider, deployer, importer, distributor and person (lines 93 and 121 to 125).
- **P0-12, Art 4(1): four questions for each of provider and deployer.**
  Whether the duty is owed, whether the measures meet it, whether a specific level must be guaranteed (the last sentence, a flat negative: `JUST FALSE`), and the regulative rule.
  The keel takes two flags for the role; the seat passes TRUE for its own and FALSE for the other (line 153).
  The judgments "sufficient" and "support the development" are yes/no facts the person states.
  Other reading: fold the four into one question.
  Split sites: the last sentence is a flat negative, and a measure that lacks an element of the duty is a bare "shall" not done (the keel's F-4-1).
  Relies on `inputs/ENCODING-GUIDE.md` section 5, line 86: "a flat negative ("does not", "shall not", "may not")" answers `JUST FALSE`; and line 95: "a bare "must" not done" is decided case by case, one fork line each.
- **P0-13, Art 4(2): one question for each sentence, asked of the provider and the deployer as the party supported.**
  The text addresses the Commission and the Member States and names no remedy; the question says only that the support and the published examples are owed (line 154).
  Other reading: no seat question, as the paragraph is addressed to officials.
- **P0-14, Art 111(1) asked of all six operator seats.**
  The keel's F-111-1-party makes the operator the party; each operator seat asks the date and the duty (line 1620).
  The Annex X facts are two plain inputs: a yes/no for a component of a large-scale IT system and the act as a `STRING` (see NEEDS-CORE.md, request 2).
- **P0-15, Art 111(2) first sentence: the question dispatches between the keel's two functions itself.**
  The keel offers `as enacted` and `as amended` and no dispatcher; the seat chooses with `Omnibus Art 4 the version in force` (line 1623; NEEDS-CORE.md, request 1).
  The seat passes `Chapter III Sections 1 to 3` as the provision group whose application is asked about, because the sentence speaks of "the date of application of Chapter III referred to in Article 113".
  The answer keeps the keel's `BOOLEAN`: `TRUE` is "saved".
  Other reading: ask the question once for each provision group, since the keel's F-111-2-all-groups saves every group except Chapter II and the Article 5 additions.
- **P0-16, Art 111(2) second sentence asked of the provider and the deployer; 111(3) of the model provider; 111(4) of the provider.**
  Licence: "the providers and deployers of high-risk AI systems intended to be used by public authorities" (line 1623), "Providers of general-purpose AI models" (line 1625), "Providers of AI systems, including general-purpose AI systems" (line 1627).
  A provider of a general-purpose AI system asks 111(4) from the provider seat; the model provider seat does not.
- **P0-17, the applicability questions use the core's two constants for the route and the placement date, and FALSE for "design significantly changed".**
  The question is asked of no AI system, and PLAN section 8 says a question about a provision of a group other than `Chapter III Sections 1 to 3` asks only the date and passes the core's constants for the rest.
- **P0-18, a provision named in a question is asked as three plain inputs.**
  An Article reference (Art 2(2), 2(7), 2(13)) is its number, a letter (`a` for Article 60a, 4a; empty for none) and a paragraph number (0 for the whole Article); the question builds the keel's `Article reference` in a `WHERE`.
- **P0-19, trace clocks.**
  A trace of the Article 111(1) to (3) rules counts days from 1 August 2024 (entry into force), and Article 111(4)'s counts from 27 July 2026 (the day the Omnibus enters into force).
  Both are the keel's own anchors, confirmed by the traces: one day inside the deadline is FULFILLED and one day outside is BREACH, on both builds.

## Marginal readings for a lawyer (P0)

Readings a reviewing lawyer could reasonably overrule, most contestable first.

1. **Art 111(2) as amended: who is saved, and when.**
   The saving reaches a high-risk system placed before the date from which Chapter III applies to it, and that date is 2 December 2027 for an Annex III system and 2 August 2028 for an Annex I system (the keel's F-111-2-date).
   So a system placed on 1 December 2027 asked about on 27 July 2026 comes back saved (`TRUE`), while the text as enacted, which saves only systems placed before 2 August 2026, saves none placed on 2 August 2026 or later.
   The two answers differ for the same system because the Omnibus moved the date; whether the transitional wording as amended was meant to reach systems placed after 2 August 2026 is for a lawyer.
2. **Art 2(5), and who asks it.**
   The paragraph protects providers of intermediary services; a provider or deployer of an AI system is only that when it also provides an intermediary service.
   The seat questions are asked of the provider and the deployer on that footing (P0-3).
3. **Art 4(1): "sufficient" and "support the development".**
   The question "do my measures meet the duty" turns on judgments the text does not define; here they are yes/no inputs, so the answer is only as good as the person's judgment.
   A measure that lacks any of the three elements the text names (the staff and other persons, their knowledge and context, the persons the systems are used on) answers `JUST FALSE` (the keel's F-4-1); the other reading is `NOTHING`.
   Split site, relying on `inputs/ENCODING-GUIDE.md` section 5, line 95: "a bare "must" not done" is among the six questions "decided site by site, at encoding time, on the text's own words and the encoder's best judgment".
4. **Art 111(1): the operator as the party that must comply.**
   The text names none (the keel's F-111-1-party), so importers, distributors and authorised representatives are asked the question as operators.
   A lawyer may read the duty as the provider's alone.
5. **Art 2(3), "regardless of the type of entity".**
   The first subparagraph protects the Member States' competences "regardless of the type of entity entrusted" with the task, which is read as covering a provider and a deployer (line 43).
6. **Art 3(8): a seat that is not an operator.**
   The person and the notified body answer `FALSE` to `am I an operator` (line 73); the definition lists six roles and neither is among them.
7. **A "may" gated by "where and to the extent that" (Art 2(13)).**
   When a condition fails the answer is `JUST FALSE`, following the 2026-11-05 ruling on "where" conditions and the keel's F-2-13; the other reading is `NOTHING`.
   Split site (a gated "may"), relying on `inputs/ENCODING-GUIDE.md` section 5, line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`".
8. **The mirror of Art 3(3) and Art 3(7).**
   The provider's `TRUE` and the distributor's `FALSE` for the same facts are complementary rather than identical: a party that develops an AI system and places it on the market under its own name is its provider, and so, by "other than the provider", not its distributor.
   The mirror group marks both cases.

## Tests

- Every question has at least one case for each branch of the keel function it calls, cases on both sides of each date the function depends on (1 and 2 February 2025; 26 and 27 July 2026; 1 and 2 August 2026; the placement bounds of Article 111; 2 December 2026), and an out-of-function case (the explicit `NOTHING`).
- Every regulative rule has traces: discharged inside the deadline, BREACH one day after it, BREACH when the party does nothing and time passes, nothing owed when the facts fall outside the rule, and nothing owed before the Regulation exists.
- The non-lead seats of a question asked by several seats carry a shorter list of cases than the lead seat; the mirror groups tie them back to the lead seat's list.
- No expectation is meant to fail, so `check.sh` has no `expected_failed` entry for this layer.
