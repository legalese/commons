# NOTES: the keel of the EU Artificial Intelligence Act encoding (aia-core, aia-timeline, aia-annex-x, aia-definitions, aia-scope, aia-literacy)

Status header (2026-11-17).
How each kind of claim below was checked: line numbers and quotations by `python3 -I srcrefs.py check --strict` over every `aia-*.l4` (170 quote lines, 137 locators, 0 problems); assertion counts by `check.sh` with L4=1.6.110 and L4_MAIN=1.6.109 (14 modules, 666 assertions satisfied, 0 failed, 0 refused, every module the same on both builds); trace outcomes by running every `#TRACE` on both builds and comparing it by hand with the `-- EXPECT` comment above it (31 traces, 0 differences).
Everything else here is the keel's reading of the text: assumed, not ruled by a lawyer.
The text is the Publications Office consolidated version of 27.7.2026, which says of itself that it "is meant purely as a documentation tool and has no legal effect" (line 2): it is a rendering, not the official text.
The as-enacted wording is quoted from `eu-ai-act-2024-1689.txt`, a mechanical extraction of the Official Journal text.
The consolidation prints the title of Article 1 as `Subject matter'` with a stray apostrophe (line 18; the base text has a stray backtick): a rendering artefact, not a word of the Regulation.

Assumed, not ruled: commencement is IN for this Regulation (the brief says so; the Guide's section 4 would put it out).
So Articles 111 and 113 and the Omnibus's Article 4 are encoded (`aia-timeline.l4`), and every function that states a duty, a power or a consequence takes `the date asked`.

## What the two dates are made of

- Entry into force of the Regulation: publication 12.7.2024 PLUS 20 days = 1.8.2024 (Art 113 first paragraph: "on the twentieth day following that of its publication"; the publication date is in the title block, line 4).
- Entry into force of the Omnibus: publication 24.7.2026 PLUS 3 days = 27.7.2026 (the Omnibus's Article 4: "on the third day following that of its publication"; the publication date is in the list of amending acts, line 9). The consolidated text says the same ("in force 27.7.2026" in the brief), and Art 113(d) as inserted names 27 July 2026.
- Both sums are computed in `aia-timeline.l4` and asserted in `aia-timeline-tests.l4`; the counting convention ("the twentieth day following" = publication date plus 20) is the usual Union one and is assumed, not ruled.

## Coverage table

One row per provision of the keel's ranges (1-155, 1618-1627, 1654-1670, 1887-1907, 2011-2021).
Dispositions: `encoded`, `inert` (reason 1 not operative, 2 machinery, 3 repealed or blank), `fork` (points at the register below), `repealed or blank`.
Function names are in the modules; the tests are in the matching `-tests.l4`.

| lines | provision | disposition | where | note |
| --- | --- | --- | --- | --- |
| 1-2 | file header and the Publications Office disclaimer | inert (1) | | not the Regulation |
| 3-10 | `▼B`, title block, list of amending acts (`▼M1` at 8-9) | inert (1) | | the dates in lines 4 and 9 are read by `aia-timeline.l4` |
| 11-14 | title, date, long title, "Text with EEA relevance" | inert (1) | | |
| 15-16 | Chapter I heading | inert (1) | | |
| 17-19 | Art 1 heading; Art 1(1) purpose | inert (1) | | a purpose clause that creates no rule |
| 20-26, 28 | Art 1(2)(a)-(g), what the Regulation lays down | inert (1) | | a statement of contents, no rule; point (g) was replaced by the Omnibus (SMCs added to the objective): wording only, no answer changes |
| 3, 8, 10, 27, 29, 40, 42, 49, 51, 57, 62, 79, 81, 84, 150, 1622, 1624, 1626, 1659, 1661, 1663, 1667, 1669 | the marker lines `▼B`, `▼M1`, `▼M1 REPLACED`, `▼M1 INSERTED` | inert (1) | | rendering markers: they say which text follows; read by the quote lines' provenance |
| 30-31 | Art 2 heading | inert (1) | | |
| 32-39 | Art 2(1)(a)-(g) | encoded, fork | `aia-scope.l4` `Art 2(1)(a)` to `Art 2(1)(g)` | F-2-1-f, F-2-order |
| 40-41 | Art 2(2), replaced | encoded (both versions) | `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` | |
| 43-45 | Art 2(3), three subparagraphs | encoded | three `Art 2(3) ...` functions | |
| 46 | Art 2(4) | encoded | `Art 2(4) ...` | |
| 47 | Art 2(5) | encoded | `Art 2(5) ...` | |
| 48 | Art 2(6) | encoded | `Art 2(6) ...` | |
| 49-50 | Art 2(7), replaced | encoded (both versions) | two `Art 2(7) ...` functions | the reserved provisions changed from Arts 10(5) and 59 to Arts 4a and 59 |
| 52 | Art 2(8) | encoded | two `Art 2(8) ...` functions | no breach path for the second sentence |
| 53 | Art 2(9) | encoded | `Art 2(9) ...` | |
| 54 | Art 2(10) | encoded | `Art 2(10) ...` | |
| 55 | Art 2(11) | encoded | `Art 2(11) ...` | |
| 56 | Art 2(12) | encoded | `Art 2(12) ...` | |
| 57-61 | Art 2(13), inserted | encoded, fork | `Art 2(13) the application ... may be limited`, the date, the Commission's rule | F-2-13 (split site ii); the delegated-acts deadline reaches BREACH |
| 62-65 | Art 3 heading and the chapeau "For the purposes of this Regulation, the following definitions apply:" | inert (1) | | the chapeau makes the definitions apply to the whole Regulation; that is the module's role, no rule of its own |
| 66-78 | Art 3(1)-(13) | encoded, fork | `Art 3(1)` to `Art 3(13)` | F-3-1, F-3-3, F-3-12 |
| 79-80 | Art 3(14), replaced | encoded, fork (both versions) | `Art 3(14) the component is a safety component` | F-3-14 |
| 81-83 | Art 3(14a), (14b), inserted | encoded (as amended only) | `Art 3(14a)`, `Art 3(14b)` | NOTHING as enacted |
| 84-114 | Art 3(15)-(44) | encoded, fork | `Art 3(15)` to `Art 3(44)` | F-3-22 for (22) |
| 115-117 | Art 3(45)(a), (b) | encoded | three `Art 3(45) ...` functions | |
| 118 | Art 3(46) | encoded | `Art 3(46) ...` | |
| 119-120 | Art 3(47), (48) | encoded | `Art 3(47) ...` (two), `Art 3(48) ...` (two) | the "shall be construed as references to" sentences are functions returning the body to read |
| 121-125 | Art 3(49)(a)-(d) | encoded | `Art 3(49) the event is a serious incident` | |
| 126-143 | Art 3(50)-(62) | encoded, fork | `Art 3(50)` to `Art 3(62)` | F-3-61; (50), (52), (62) are borrowed facts |
| 144-149 | Art 3(63)-(68) | encoded | `Art 3(63)` to `Art 3(68)` | |
| 150-152 | Art 4 heading, replaced | inert (1) | | |
| 153 | Art 4(1), replaced | encoded, fork (both versions) | five `Art 4(1) ...` functions | F-4-1; the duty has no breach path |
| 154 | Art 4(2), inserted | encoded (as amended only) | two `Art 4(2) ...` functions | |
| 155 | Art 4(3), inserted | encoded (as amended only) | `Art 4(3) ...` | |
| 1618-1619 | Art 111 heading | inert (1) | | |
| 1620 | Art 111(1) first subparagraph | encoded, fork | `Art 111(1) the date by which the AI system must be brought into compliance`, `Art 111(1) the duty to bring the AI system into compliance` | F-111-1-party, F-111-annex-x-flag |
| 1621 | Art 111(1) second subparagraph | encoded | `Art 111(1) the requirements of this Regulation are to be taken into account in the evaluation` | no breach path |
| 1622-1623 | Art 111(2), replaced | encoded, fork (both versions) | `Art 111(2) ... is saved` (applicability), `Art 111(2) the date by which providers and deployers ... must comply`, two regulative rules | F-111-2-date, F-111-2-chapter-I, F-111-2-all-groups, F-111-2-nothing |
| 1624-1625 | Art 111(3) | encoded | `Art 111(3) ...` (date and rule) | unchanged by the Omnibus |
| 1626-1627 | Art 111(4), inserted | encoded (as amended only) | `Art 111(4) ...` (date and rule) | |
| 1654-1655 | Art 113 heading | inert (1) | | |
| 1656 | Art 113 first paragraph | encoded | `Art 113 the Regulation enters into force` | publication plus 20 |
| 1657 | Art 113 second paragraph | encoded | `Art 113 second paragraph the general date of application` | 2 August 2026 |
| 1658-1661 | Art 113(a), replaced | encoded, fork (both versions) | `Art 113(a) ...` | F-113-groups; the Article 5 additions exist as amended only |
| 1662-1663 | Art 113(b) | encoded | `Art 113(b) ...` | Art 101 excepted: in the group General |
| 1664-1666 | Art 113(c), replaced | encoded, fork (both versions) | `Art 113(c)(i)`, `Art 113(c)(ii)`, `Art 113(c) as enacted ...` | F-113-6-1 |
| 1667-1668 | Art 113(d), inserted | encoded (as amended only) | `Art 113(d) ...` | as enacted Arts 102 to 110 applied from the general date |
| 1669-1670 | `▼B`; "binding in its entirety and directly applicable" | inert (1) | | enacting formula |
| 1887-1888 | Annex X heading, title | inert (1) | | |
| 1889-1907 | Annex X, 7 points, 12 acts | encoded, fork | `aia-annex-x.l4` | F-annex-x-closed |
| 2011-2021 | footnotes (11): citations of Regulation (EU) No 1025/2012, Directive (EU) 2016/943, Regulation (EU) 2024/1689 (eight times), Directive (EU) 2020/1828 | inert (1) | | OJ citations; the instruments are not among the sources, so the facts they define are inputs where the text needs them |

Every `inert` row is one of the three reasons and none is "addresses an official" or "open-textured".
There is no `deferred` and no `out-of-scope` row.

## Fork register

Each entry: the site, the readings and the text that licenses each, the answer taken, the rule that carries it.
The answer taken is the keel's, assumed, not ruled; a human reviewer may overrule any of them.

- **F-113-groups** (aia-core `Provision group`, `aia-timeline.l4`). Art 113 as amended names six dated sets; the keel's seven constructors split them where a later rule needs the split.
  Reading taken: `Chapter I` and `Chapter II` are separate groups although Art 113(a) dates them together, because Art 111(2) saves operators of legacy high-risk systems "without prejudice to the application of Article 5", so Chapter II (Article 5) must be answerable alone; `Article 5 additions` carries the exception of (a) (2 December 2026); `Notified bodies, GPAI, governance, penalties and Art 78` carries (b); `Chapter III Sections 1 to 3` carries (c), its date chosen by the route; `Articles 102 to 110` carries (d); `General` carries the second paragraph and every provision no point names. Articles 6(5) and 101 are in `General`: point (c) excepts 6(5) and point (b) excepts 101, so the second paragraph's general date reaches them.
  The other reading: one group per point of Art 113 (no Chapter I / Chapter II split). It cannot say that Article 5 is not saved.
- **F-113-6-1** (`Art 113 as enacted the date of application`). As enacted, point (c) reads "Article 6(1) and the corresponding obligations in this Regulation shall apply from 2 August 2027" (src:eu-ai-act-2024-1689:2206).
  Reading taken: "the corresponding obligations" are those of Chapter III Sections 1 to 3 that attach to a system classified under Article 6(1); the date for the Article 6(1) route is 2 August 2027, for the Article 6(2) route 2 August 2026 (the general date).
  The other reading: "the corresponding obligations" are only the obligations that Article 6(1) itself names. The text does not define "corresponding". Only the text as enacted is affected, and it was in force only until 26 July 2026, before either date.
- **F-111-2-date** (`Art 111(2) as amended the system is saved`). As amended, Art 111(2) refers to "the date of application of Chapter III referred to in Article 113", but point (c) gives two dates.
  Reading taken: the date for the system's own route (2 December 2027 for Annex III, 2 August 2028 for Annex I); a system that is high-risk by both routes passes the route it is asked about (the caller's choice, not the keel's).
  The other reading: the earlier of the two dates for every system.
- **F-111-2-chapter-I** (`Art 111(2) the provision group can be saved`). The saving is "without prejudice to the application of Article 5" only. Reading taken: Chapter I (Articles 1 to 4a, including the definitions) is saved for a legacy high-risk system like any other provision; the groups `Chapter II` and `Article 5 additions` are not. The other reading: Chapter I is never saved because its definitions are needed to read Article 5. Tested in `aia-timeline-tests.l4`.
- **F-111-2-all-groups**. "This Regulation shall apply to operators of high-risk AI systems ... only if ..." is a flat "only if" about the whole Regulation. Reading taken: every group except Chapter II and the Article 5 additions is saved, including the group `Notified bodies, GPAI, governance, penalties and Art 78` and `General`. The other reading: the saving reaches only Chapter III Sections 1 to 3 (the context of "the date of application of Chapter III").
- **F-111-2-nothing**. For a saved system the text's own words ("only if") say that the Regulation does not apply, which would be `JUST FALSE`; for a date before the group applies the brief rules `NOTHING`. The keel's one gate answers `FALSE` for both, and the parts answer `NOTHING` for both (assumed). The other reading: `JUST FALSE` for a saved system. A part that wants it can call `Art 111(2) as amended the system is saved` (and its as-enacted twin) with the date of its choice; they are in `aia-timeline.l4` and tested.
- **F-111-1-party**. Art 111(1) says AI systems "shall be brought into compliance" and names no party. Reading taken: the operator (Art 3(8)); the rule is stated once, `PARTY Operator`. The other reading: the provider only (the person who can change a system), or the provider and deployer.
- **F-111-annex-x-flag** (the applicability function has five arguments). An AI system that is a component of an Annex X large-scale IT system is outside Art 111(2) ("other than the systems referred to in paragraph 1") and has its own date, 31 December 2030. The brief fixes the applicability function's arguments, none of which says "Annex X component". Reading taken: the applicability function treats such a system like any other legacy high-risk system; a part that meets one calls the stand-alone `Art 111(1)` functions as well and lets the later date prevail. The other reading: add a sixth argument. Recorded as a trap in PLAN.md section 5.
- **F-2-order** (`Art 2 the Regulation applies given the answers of the paragraphs`). The text states no order between Art 2(1) ("applies to") and the exclusions of paragraphs 3, 4, 6, 8, 10 and 12 ("does not apply"). Reading taken: an exclusion that says no (`JUST FALSE`) comes first, then an inclusion, otherwise `NOTHING`. The other reading: inclusion first, which would let Art 2(1) override every exclusion.
- **F-2-1-f** (`Art 2(1)(f)`). "authorised representatives of providers, which are not established in the Union". Reading taken: the relative clause describes the providers, because Art 3(5) makes every authorised representative one "located or established in the Union", so the clause cannot describe the representatives. The other reading: representatives not established in the Union, which Art 3(5) rules out.
- **F-2-13** (`Art 2(13) the application of the requirement or obligation may be limited`; split site ii). A "may" gated by "where and to the extent that": answer taken `JUST FALSE` when a condition fails (the periods ruling of 2026-11-05, rule (b): a "where" condition that fails). The other reading: `NOTHING` (a grant limited by its own wording). "To the extent" is a matter of degree the function does not measure.
- **F-3-gate**. A definition of Article 3 is not gated by Article 113: it applies with the provision that uses it. Reading taken: only (14), (14a) and (14b) take a date, to select the text. The other reading: gate every definition on Chapter I (2 February 2025). The functions would then answer `NOTHING` before that date.
- **F-3-1** (`Art 3(1)`). "that may exhibit adaptiveness after deployment" is read as what a system MAY do, not as an element a system must have (recital 12: "The adaptiveness that an AI system could exhibit"). The other reading: adaptiveness is an element.
- **F-3-3** (`Art 3(3)`). "develops ... or has ... developed and places it on the market or puts ... into service under its own name or trademark". Reading taken: whoever develops, or has developed, AND places it on the market (or puts the AI system into service) under its own name or trademark. The other reading: whoever develops an AI system is a provider without more.
- **F-3-12** (`Art 3(12)`). The use counts as the intended purpose if any of the named sources (instructions for use; promotional or sales materials and statements; technical documentation) specifies it. The other reading: it must be specified in all of them.
- **F-3-14** (`Art 3(14)`). As enacted "fulfils a safety function" is an open term; as amended the text defines it ("where its intended purpose is to prevent or mitigate risks"). The two functions differ for a component whose purpose is not risk prevention but which someone says fulfils a safety function. Both versions are encoded, with a test on each side of 27 July 2026.
- **F-3-22** (`Art 3(22)`). "notified in accordance with this Regulation and other relevant Union harmonisation legislation": both, where other legislation is relevant; the input is `TRUE` where none is. The other reading: this Regulation alone suffices.
- **F-3-61** (`Art 3(61)`). Limbs (a) and (b) end in semicolons without "or" or "and". Reading taken: alternatives (assumed, not ruled; the text says neither "and" nor "or"). The other reading: both limbs must hold.
- **F-4-1** (`Art 4(1) the measures meet the duty ...`). A bare "shall take measures": a measure that lacks an element does not meet the duty (`JUST FALSE`). The other reading: `NOTHING`, because the text does not say what follows. The judgments ("sufficient", "support the development") are plain inputs.
- **F-annex-x-closed** (`Annex X the act is listed`). Art 111(1) hands the question "which acts?" to the list ("the legal acts listed in Annex X"). Reading taken: an act that is not on it is not one of them (`FALSE`; the ruling of 2026-11-05 on definitions handed to a list). The other reading: a bare list closes nothing, so `NOTHING`.

## Jural relations

One row per provision of the keel's ranges that creates a relation; a provision that creates none is `none`.
The party holding the right, privilege, power or immunity is in the third column, the bearer of the correlative in the fourth.

| provision | relation | holder | bearer | L4 rule |
| --- | --- | --- | --- | --- |
| Art 1 | none (purpose; contents) | | | |
| Art 2(1) | none: it makes persons subject to the Regulation's rules; the relations are in the later Chapters | | | `Art 2(1)(a)` to `(g)` |
| Art 2(2) | immunity | operator of a high-risk system under Art 6(1) with Section B products, from every provision not listed | the authorities that would enforce those provisions (disability) | `Art 2(2) ...` |
| Art 2(3), (4), (6), (8) first sentence, (10), (12) | immunity | the party or system excluded, from the Regulation | the authorities (disability) | the matching `Art 2(N) ...` functions |
| Art 2(5), (7), (9) | none: savings of other law | | | `Art 2(5)`, `Art 2(7)`, `Art 2(9)` |
| Art 2(8) second sentence | duty | whoever conducts the excluded research, testing or development | none named (the duty is to act in accordance with other Union law) | `Art 2(8) the activity must be conducted ...` (no breach path) |
| Art 2(11) | privilege | the Union and the Member States, to maintain or introduce more favourable rules and to encourage or allow collective agreements | no-right of the Regulation (and of whoever would invoke it) to preclude it | `Art 2(11) ...` |
| Art 2(13) | privilege | the provider of a high-risk system under Art 6(1), to have the application of Arts 9 to 15 and 17 to 25 limited where equivalent protection exists | no-right of the authorities to insist on them to that extent | `Art 2(13) the application of the requirement or obligation may be limited` |
| Art 2(13) second sentence | duty | none named | the Commission, to adopt delegated acts by 2 August 2027 | `Art 2(13) the Commission's duty ...` |
| Art 3 | none (definitions; the two "shall be construed" sentences are rules of reading) | | | `Art 3(N) ...` |
| Art 4(1) | duty | none named | providers and deployers, to take measures regarding AI literacy; as amended they need not guarantee any specific level | `Art 4(1) the provider's duty ...`, `Art 4(1) the deployer's duty ...` |
| Art 4(2) | duty | the providers and deployers of AI systems, in particular SMEs, benefit; no claim or remedy is stated | the Commission and the Member States, to support and facilitate; the Commission, to publish practical examples | `Art 4(2) ...` |
| Art 4(3) | duty | none named | the Board, to adopt recommendations | `Art 4(3) ...` |
| Art 111(1) first subparagraph | duty | none named | the operator of a component of an Annex X large-scale IT system, to bring it into compliance by 31 December 2030 | `Art 111(1) the duty to bring the AI system into compliance` |
| Art 111(1) second subparagraph | none named | | whoever undertakes the evaluation of the large-scale IT system | `Art 111(1) the requirements of this Regulation are to be taken into account ...` (no breach path) |
| Art 111(2) first sentence | immunity | the operator of a legacy high-risk system not significantly changed since the date of application | the authorities (disability) | `Art 111(2) ... is saved` |
| Art 111(2) second sentence | duty | none named | providers and deployers of high-risk systems intended for public authorities, by 2 August 2030 | `Art 111(2) the provider's duty ...`, `Art 111(2) the deployer's duty ...` |
| Art 111(3) | duty | none named | the provider of a general-purpose AI model placed before 2 August 2025, by 2 August 2027 | `Art 111(3) the duty ...` |
| Art 111(4) | duty | none named | the provider of an AI system generating synthetic content placed before 2 August 2026, to comply with Art 50(2) by 2 December 2026 | `Art 111(4) the duty ...` |
| Art 113 | none (commencement) | | | `Art 113 ...` |
| Annex X | none (a list) | | | `aia-annex-x.l4` |

## Reading a result: FALSE and NOTHING

In this encoding a `JUST FALSE`, or a plain `FALSE` from a definition, is the text's own "no": a definition that says "means" and an element is missing; a paragraph that says "does not apply" or "shall not affect" and the facts meet it; a list the text closes with "only" and the provision is not on it; a condition ("where", "only if", "unless", "provided that") that is not met within the provision that holds it.
A `NOTHING` is "not covered": the paragraph does not speak to these facts, or the text is silent, or it limits its own grant ("where", "for the sole purpose of", "exclusively") and the case falls outside the limit, or Chapter I has not begun to apply on the date asked (before 2 February 2025), or the provision does not exist in the version asked about (the Omnibus inserted Art 2(13), Art 3(14a), (14b), Art 4(2), (3) and Art 111(4)).
A caller never turns `NOTHING` into `FALSE`.
The definitions of Article 3 return plain `BOOLEAN`s: every one says "means", so a `FALSE` is always the text's own no; only (14a), (14b), (47)'s and (48)'s reading rules and (57)'s consequence return `MAYBE`.
The time axis returns `BOOLEAN` or `MAYBE DATE`; a `NOTHING` date is "the text gives no date to these facts" (for example, Chapter III Sections 1 to 3 give no date to a system that is not high-risk).

## Marginal readings for a lawyer

Each branch that rests on one of the two readings the rule of 2026-10-29 leaves open: (a) a failed "if" counts as the text's no, within the provision that holds it, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
For each, the other reading is stated.

1. Art 2(3) (three), (4), (5), (6), (8) first sentence, (9), (10), (11), (12): reading (a), flat negatives are `JUST FALSE`. Other reading: `NOTHING`, because "does not apply" speaks to the excluded case only.
2. Art 2(2) and Art 2(7): reading (a), a list closed by "only" (`JUST FALSE` for a provision not on it) and "shall not affect" (`JUST FALSE`). Other reading: `NOTHING`.
3. Art 2(4), (8) third sentence, (12): reading (b), where the "provided that", "shall not be covered by that exclusion" or "unless" limb defeats the exclusion the function answers `NOTHING`, not `JUST TRUE` (that the Regulation applies). Other reading: `JUST TRUE`.
4. Art 2(1)(a) to (g): a party outside every limb is `NOTHING` (the list does not close). Other reading: `JUST FALSE` ("applies to" read as a complete list).
5. Art 2(13): `JUST FALSE` when "where and to the extent that" fails (reading (a), the periods ruling). Other reading: `NOTHING` (reading (b)).
6. Art 3(4) "except where", (7) "other than", (40) "unless", (63) "except": the unmet limb gives `FALSE` within a "means" definition. Other reading: none that differs, since a "means" definition states its own limits; listed because each carries an exception.
7. Art 4(1) measures: a missing element is `JUST FALSE` (fork F-4-1). Art 4(1) last sentence: `JUST FALSE` (flat negative).
8. Annex X: an act not on the list is `FALSE` (fork F-annex-x-closed).
9. Art 111(2): a saved system answers `FALSE` from the gate (reading (a): "only if"); the parts turn the gate's `FALSE` into `NOTHING` (fork F-111-2-nothing). Other reading: `JUST FALSE` for a saved system.
10. Every `NOTHING` for "limited by its own wording" in `aia-scope.l4` and `aia-literacy.l4` (reading (b)).

## Split sites (your part)

(i) An unmet element of an infringement: 0 sites. The keel's range names no infringement of the Regulation (the prohibited practices, the fines and the infringements are in other parts).
(ii) A "may" gated by "where", "when", "upon", "on application" or "with the consent of": 1 site, Art 2(13) (`Art 2(13) the application of the requirement or obligation may be limited`), answer `JUST FALSE` when a condition fails; the fork line is F-2-13.
No answer was changed to match any other part.

## Rules with no breach path (your part)

Each is a "shall" with no time limit and no stated consequence. No trace can show it breached: a late action reads `FULFILLED`.
No deadline or consequence was invented.

- Art 2(8) second sentence: "Such activities shall be conducted in accordance with applicable Union law." Decision function only (`Art 2(8) the activity must be conducted in accordance with applicable Union law`).
- Art 4(1), providers and deployers: "shall take measures". Regulative rules `Art 4(1) the provider's duty ...` and `Art 4(1) the deployer's duty ...`; their traces read `FULFILLED`.
- Art 4(2) second sentence: the Commission "shall publish practical examples". Decision function only.
- Art 4(3): the Board "shall adopt recommendations". Decision function only.
- Art 111(1) second subparagraph: the requirements "shall be taken into account in the evaluation". Decision function only.

Rules that do reach `BREACH` (each has a trace on both builds): Art 111(1) first subparagraph (31 December 2030); Art 111(2) second sentence, provider and deployer (2 August 2030); Art 111(3) (2 August 2027); Art 111(4) (2 December 2026); Art 2(13) second sentence, the Commission (2 August 2027).

## What the stable binary does not accept, and what was met

Met while writing this keel (1.6.110, checked also on 1.6.109):

- `JUST x's field` is read as `(JUST x)'s field`: write `JUST (x's field)`. The error is `check/not-a-function` at the possessive.
- The list functions are `count`, `any`, `all`, `filter`, `elem`, `map`; there is no `length`.
- A computed deadline works: `WITHIN (Day d) MINUS (Day s)`, with the trace clock a day number: `AT (Day (Date 2 8 2027))`; `WAITUNTIL (Day (Date ...))` lets time pass. Used for the Art 111 deadlines; traces agree on both builds.
- `AND CONSIDER ... WHEN ...` inside a conjunction, `ELSE CONSIDER`, and a `CONSIDER` returning a `DEONTIC` all compile; so do a `MAYBE BOOLEAN` compared with `EQUALS JUST TRUE` in `#ASSERT`, a `LIST OF MAYBE BOOLEAN` and `EMPTY`.
- Backtick names may hold parentheses, commas, apostrophes and a leading "Art 3(45)(a)"; a field is read as `` `name`'s `field` ``.
- `@export` and `@desc` on a `DECIDE` returning `MAYBE BOOLEAN`, with a `DATE` input and an enumerated input (`Route to high-risk`), compile on both builds; the Interact form and `jl4-service` were not run.
- `srcrefs.py check --strict` wants each `@ref` locator directly below its own quote run: a second function under the same article repeats the quote lines, or carries an `@ref` with no locator.

Listed in the brief and not exercised here: no `REFUSE`; `AFTER ... WITHIN` is rejected; `WAIT UNTIL` is spelled `WAITUNTIL`; no sets, `TYPICALLY`, section `GIVEN`, opaque `DECLARE`; `Date day month year` only, never `YMD`; an input named in a `MUST` action degrades on main; `MAY ... LEST` degrades on main.
A `#TRACE` outcome that differs between the builds is invisible to `check.sh`: all 31 traces were compared by hand with `-- EXPECT` comments (`work/tracecheck.py`, outside the deposit) and none differs.

## Seat layer

The keel writes no seat files: its ranges (Articles 1 to 4, 111 and 113, Annex X) are definitions, scope, a time axis and one literacy duty, and the nine seats are the parts' to write.
`aia-pattern-c-seat.l4` is a worked seat module for the provider seat with the shared inputs (`the date asked` and its @desc) and the applicability question; it is an illustration, not a deliverable seat.
