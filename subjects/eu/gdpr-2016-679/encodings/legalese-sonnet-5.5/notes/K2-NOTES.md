# NOTES -- K2 of Regulation (EU) 2016/679 (GDPR), the keel completion

> The helper scripts named in this file are in this folder (`notes/*.py`). Their sandbox paths (the `l4` binary and the source text) were replaced by `$L4` and a path relative to the row after their last run, and they were not re-run since.

Written by K2 (Sonnet 5.5), the only agent running; no subagent, no advisor, no reviewer tool was used.
This is K2's part of the notes; a lead merges it with `NOTES.md` of P1.
Every claim below was checked against the files in this folder the day K2 stopped; `check.sh`'s output is under "What check.sh prints".
The rulings used are the Guide's (section 5, rulings of 2026-11-04, 2026-11-05 and 2026-11-12, the last "not confirmed by the maintainer") and the rule of 2026-10-29 (assumed, not ruled by a lawyer).
Nothing here has been read by a lawyer: the status of the whole encoding is `draft`, not reviewed.

## What is encoded

**Scope, as provisions.**
Article 1 (Chapter I heading, Art 1(1), (2) inert, Art 1(3) encoded); Article 2(3) and (4); Article 3 (territorial scope) and the combined answer "this Regulation applies"; Article 4: the lead-in, points (3) 'restriction of processing', (4) 'profiling', (5) 'pseudonymisation' and points (9) to (26); the footnote of point (25); Article 99 as `inert` machinery.
Lines of `eu-gdpr-2016-679-consolidated-20160504.txt`: 12-18, 27-35, 36-38, 41-43, 47-73, 1076-1080, and the footnote at line 1081.
Points (1), (2), (6), (7), (8) of Article 4 are P1's and are not encoded here.

**Edition and status of the text.**
The text is the Publications Office consolidated version of 4.5.2016 (CELEX 02016R0679-20160504, "000.002"), which applies the corrigendum of OJ L 127, 23.5.2018, p. 2.
It is a rendering made by a script from XHTML, and it is a documentation tool with no legal effect: the Official Journal text is authentic.
The file's sha256 is `eed86fd2b91b934e6b2fff2185edd4d1eff071c9a81178f34e9cb9b4500d72f0`, the text sha256 that `inputs/SOURCES.md` gives (checked with `sha256sum`).
No recital was read and none is encoded or quoted as an authority: no comment of K2 says `-- see recital N`.
The corrigendum: none of its fifteen corrections falls in this range.
I counted fifteen `On page ...` headings in `eu-gdpr-2016-679-corrigendum-20180523.txt` (recital 71 and Articles 37(1)(c), 41(3), 41(5), 42(7), 43(3), 43(6), 57(1)(p), 64(1)(c), 64(6) to (8), 65(1)(a), 69(2), 70(1)(l), (o), (p)); the fourteen `▼C1`/`►C1` markers of the consolidated text are at line 6 (the header legend) and at lines 451 and later, so none lies in lines 12-73 or 1076-1081.
There is no date input and no version axis: Art 99(2) says the Regulation applies from 25 May 2018, and K2 records that as `inert` machinery (Open questions).

**Target and binary.**
Target `main`.
Binary `$L4_MAIN`, `1.6.112 (main, e4f4bf3, 2026-11-18)`; `JL4_LIBRARY_PATH` unset.
`check.sh` was run with `L4_TARGET=unstable` because the binary already is the main build (the lead runs both builds afterwards).
`l4 run` prints `Warning | [Import Resolution] Multiple differing copies of module prelude (and daydate)` on this machine because an older copy is in the XDG data directory; it is not a diagnostic of any module and `check.sh` does not count it.

**Method.**
The core's added nouns first (`gdpr-core-2.l4`, DECLARE only), then the Article 4 definitions in `gdpr-definitions-2.l4` with their tests, then one layer-1 module per article (`K2-art-1`, `K2-art-2b`, `K2-art-3`) with its tests, then the two seat layers.
Each rule carries its `@ref` with a source locator and quote lines copied by `srcrefs.py quote` (a script expanded placeholders into the quote lines, so no quotation was typed).
Every expected value in a test was written by hand from the provision before the run (see Findings).
The seat, seat-cases and mirror files were produced by `notes/gen-seats.py`, which reads the names, types and input order of the layer-1 functions from the `.l4` files and holds the hand-written expected values in its case lists; it is kept here, so the 305 seat and mirror assertions can be re-derived.
The `-- FALSE-kind` and `-- NOTHING-kind` comments quote the text; I checked every quoted piece in K2's comments mechanically (a script over K2's files: 99 quoted pieces, all 99 found verbatim in the consolidated text after normalising the quotation marks and treating `...` as an elision).

**Design choices that are mine (assumed, not ruled).**
- K2 adds no shared answer type: every definition answers `MAYBE BOOLEAN` or `MAYBE` of an enumeration, and a gated duty would use P1's `Duty outcome` (none arises in K2's range).
- An argument the text itself declares irrelevant is kept so the clause has a test, and is not read: Art 3(1) `the processing takes place in the Union` ("regardless"), Art 3(2) `a payment of the data subject is required` ("irrespective"), Art 4(9) `the body is a third party` ("whether a third party or not"), Art 4(13) `the data result from an analysis of a biological sample ...` ("in particular", fork FK4-4), Art 4(14) `the data are facial images or dactyloscopic data` ("such as").
- Where a definition leans on a provision of another part or on another instrument, the fact is a plain BOOLEAN input (Article 27, Article 51, Article 98, Directive (EU) 2015/1535, Regulation (EC) No 45/2001, Directive 2000/31/EC); none of them is encoded.
- Art 4 lead-in: encoded as a function that answers JUST TRUE for a term used for the purposes of the Regulation and NOTHING otherwise.
- The `Kind of person or body` of the core is used for Art 4(9), (10), (17), (18) and (21), as P1 uses it for (7) and (8).

### Reading a result: FALSE and NOTHING

Read in this subject's terms.

- `JUST TRUE` means the Regulation says yes in its own words: a definition is met, a limb of the territorial scope is met, a bar stands (Art 1(3): the restriction is barred), a saving stands (Art 2(4): without prejudice).
- `JUST FALSE` means the Regulation itself says no, and only where it does, on the brief's list: a definition that "means" and is not met (Art 4); a flat negative ("does not apply" in Art 2(2), read through P1's answer; "shall not be regarded as recipients" in Art 4(9)); a condition introduced by "provided that" that fails (Art 4(5)).
  Three further inferences are used and are listed for a lawyer: a failed "where" gate gives `JUST FALSE` (Art 3(2); periods ruling (b) of 2026-11-05); the naming of another instrument as the one that applies is read as the Regulation's no (Art 2(3), fork FK2-1); and an unmet "shall" answers `JUST FALSE` as split site (i) (Art 2(3) second sentence, Art 4(9) last clause).
- `NOTHING` means the Regulation does not answer on these facts: it is silent; a term is left undefined; the answer lies in a provision or instrument outside the sources; "includes" leaves the category open (Art 4(18)); or the provision limits a statement to a situation in its own wording and the case falls outside it (Art 1(3) for a movement outside the Union or a measure for another reason; Art 2(3) and Art 4(9) for a case outside the bodies they name; Art 3 for a processing that meets none of its three limbs; Art 4(16) for a controller or processor in one Member State).
- A caller must never turn `NOTHING` into `FALSE`: "the Regulation does not say" is not "the Regulation says no".
  In particular `Art 3 this Regulation applies to the processing of personal data` answers `NOTHING`, not `JUST FALSE`, for a processing that is within none of the three limbs (fork FK3-1).
- From `Art 4(13) to (15) the categories ...`: `JUST EMPTY` means that all three definitions answered `JUST FALSE`, so none gives a category; it does not say that the data are not special.
  `NOTHING` means that at least one of the three definitions answered `NOTHING`, so the list is not decided, whatever the other two answer (changed after the adversarial review, R3: the list used to be given as complete when a definition gave no answer).
  A list is given only when no definition answered `NOTHING` and at least one is met.
- Where the brief and the Guide differ, the Guide governs.
  The brief's list of markers on which the text says no ("if", "only if", "as long as", "unless", "so long as", "while", "until", "except", "save", "provided that") does not contain "where", "when" or "upon"; the Guide's periods ruling (b) and the delegated ruling (c) of 2026-11-05 add them.
  I followed the Guide: a failed "where" gate answers `JUST FALSE`, which is the one place it shows in K2's range (Art 3(2)); I found no other difference between the two documents.
  On the K2 brief's own description of Art 2(3) and (4) as "provisions that say the Regulation does not apply to Union bodies and is without prejudice to Directive 2000/31/EC": Art 2(4) says "without prejudice" in those words; Art 2(3) does not say "does not apply" and names Regulation (EC) No 45/2001 instead, so the brief's description is a reading (FK2-1), not the text's own words.

## Sources, edition and status

Six statements about what this part rests on; each was checked on 2026-11-26 against the source named.

1. **The text quoted is a rendering, not the official text.**
   It is the Publications Office consolidated version of 4.5.2016 (CELEX 02016R0679-20160504), made by a script from XHTML; the Publications Office says it has no legal effect and the Official Journal text (OJ L 119, 4.5.2016, p. 1, with the corrigendum) is the authentic one.
2. **The corrigenda.**
   The 2018 corrigendum has fifteen corrections and none falls in this range (see above).
   The 2016 corrigendum (CELEX 32016R0679R(01)) and the 2021 one (OJ L 74, 4.3.2021, p. 35) are not deposited (`inputs/SOURCES.md`: the Publications Office answered 404 for both on 2026-11-26); K2 did not look for them.
3. **No amending act was looked for.**
   K2 did not search for amendments; it did not use a network.
   `inputs/SOURCES.md` and P1's notes say none was found and name Regulation (EU) 2025/2518 as related and the Digital Omnibus as a proposal; K2 repeats that and has not checked it.
4. **The choice of texts and the split into parts are assumed, not ruled** (`inputs/PARTS.md`).
5. **The licence of the deposited texts is undetermined** (the subject's `SOURCE-LICENSE.md`, held outside this deposit); nothing here says the texts may be redistributed.
6. **No lawyer has read this encoding.**
   Its status is `draft`.

## Seats

- **A data subject** `[subject]` (required): `K2-seat-subject.l4`, 24 questions, `K2-cases-seat-subject.l4` (93 cases).
  The data subject is the natural person whose personal data are processed.
  It asks only what a data subject can state: whether a restriction of the movement of her data is barred (Art 1(3)), whether Regulation (EC) No 45/2001 or this Regulation applies when a Union body processes her data (Art 2(3)), the saving of Directive 2000/31/EC (Art 2(4)), whether this Regulation applies to the processing of her data and each of its three territorial limbs (Art 3), and the definitions she can apply to what she knows: a restriction of processing, profiling, a recipient, a third party, consent, a personal data breach, genetic, biometric and health data and the Art 9(1) category they give, a representative, a supervisory authority and whether it is concerned, an information society service, an international organisation, and whether the processing by an inquiry authority is in compliance (Art 4(9)).
  It has no question on Art 2(3) second sentence, Art 4 lead-in, 4(5), 4(16), 4(18), 4(19), 4(20), 4(23) or 4(24): those address the Union's lawmaker, or turn on facts a data subject cannot state (pseudonymisation measures, central administration, group structure, binding corporate rules, an objection to a draft decision).
- **A controller** `[controller]`: `K2-seat-controller.l4`, 33 questions, `K2-cases-seat-controller.l4` (119 cases).
  It asks every provision of the range that a controller applies to its own processing, grouped by article.
  It has no question on Art 2(3) second sentence (it addresses the Union's lawmaker, fork FK2-2).
- **A processor** `[processor]`: no seat module and no processor question; Art 4(16)(b) is asked from the controller's seat about the controller's processor.
- **Never** a seat for a supervisory authority, the Board, the Commission or a court.
  Art 4(21), (22) and (24) are asked from the person's seat as questions of identification ("is this body a supervisory authority", "is it concerned", "is the objection to the draft decision about me a relevant and reasoned objection"), not as questions an authority asks.
- Mirror cases: `K2-cases-mirror.l4` puts the same facts to both seats and asserts that the answers are equal (93 assertions over the 24 questions both seats ask).
  The two seats' own cases files carry the same cases with their expected values.
- **Direction audit.** I read the name of all 57 seat questions together with their cases.
  None answers in the opposite direction to its name: "is a restriction ... barred" answers `JUST TRUE` for barred; "does this Regulation apply ... where I am a Union institution" answers `JUST FALSE` for no; "is the limb ... met" answers `JUST FALSE` when the limb's own "where" gate fails; "is the processing ... in compliance" answers `JUST TRUE` for in compliance.
  The audit changed one name: the Art 4(9) question was first worded "must a public authority ... process in compliance", a question that `JUST TRUE` would have answered the wrong way round, and now asks "is the processing ... in compliance" (the expected values were not touched).

## Coverage table

Dispositions: `encoded`, `inert` (the reason in brackets), `fork` (row points at its entry in the fork register and at the rule that encodes the chosen reading), `repealed or blank in this text`.
There is no `out-of-scope` and no `deferred` row.
Modules: `defs2` is `gdpr-definitions-2.l4` with `gdpr-definitions-2-tests.l4` (`tests2`); `art-1`, `art-2b`, `art-3` are `K2-art-N.l4` with `K2-tests-art-N.l4`.
Rule names are given by their label; each is the function whose name begins with it.

| provision (consolidated lines) | what it says | disposition | rule | test |
| --- | --- | --- | --- | --- |
| Chapter I heading (12-13) | "CHAPTER I / General provisions" | inert (1): heading (lines assigned to no part by PARTS.md; recorded because they head Article 1) | | |
| Art 1 heading (14-15) | "Article 1 / Subject-matter and objectives" | inert (1): heading | | |
| Art 1(1) (16) | the Regulation lays down rules on protection and on free movement | inert (1): objects clause, creates no rule | | |
| Art 1(2) (17) | the Regulation protects fundamental rights and freedoms | inert (1): objects clause, creates no rule | | |
| Art 1(3) (18) | free movement within the Union neither restricted nor prohibited for data protection reasons | fork FK1-1 | art-1 `Art 1(3) the restriction or prohibition ... is barred` | tests-art-1 (5) |
| Art 2(3) first sentence (27) | for processing by the Union bodies, Regulation (EC) No 45/2001 applies | fork FK2-1 | art-2b `Art 2(3) Regulation (EC) No 45/2001 applies ...`, `Art 2(3) this Regulation applies ...` | tests-art-2b §first sentence (4) |
| Art 2(3) second sentence (27) | 45/2001 and other Union acts to be adapted in accordance with Article 98 | fork FK2-2 | art-2b `Art 2(3) the Union legal act applicable to such processing is adapted ...` | tests-art-2b §second sentence (4) |
| Art 2(4) (28) | the Regulation is without prejudice to Directive 2000/31/EC | encoded | art-2b `Art 2(4) this Regulation is without prejudice ...` | tests-art-2b §Art 2(4) (4) |
| Art 3 heading (29-30) | "Article 3 / Territorial scope" | inert (1): heading | | |
| Art 3(1) (31) | applies to processing in the context of an establishment in the Union, wherever it takes place | encoded | art-3 `Art 3(1) the territorial limb: ...` | tests-art-3 §Art 3(1) (4) |
| Art 3(2) chapeau (32) | applies to processing of data subjects in the Union by a controller or processor not established there, where the activities are related to (a) or (b) | fork FK3-1 | art-3 `Art 3(2) the territorial limb: ...` | tests-art-3 §Art 3(2) (10) |
| Art 3(2)(a) (33) | offering of goods or services, irrespective of payment | encoded | same function | same |
| Art 3(2)(b) (34) | monitoring of behaviour as far as it takes place in the Union | fork FK3-4 | same function | same |
| Art 3(3) (35) | applies to a controller not established in the Union, in a place where Member State law applies by public international law | fork FK3-3 | art-3 `Art 3(3) the territorial limb: ...` | tests-art-3 §Art 3(3) (4) |
| Art 3 with Art 2(1)-(2) and Art 2(3) (21-35) | the combined answer "this Regulation applies" (a join the brief asks for, not a provision) | fork FK3-1, FK3-2, FK2-1 | art-3 `Art 3 this Regulation applies to the processing of personal data` | tests-art-3 §combined (15) |
| Art 4 heading (36-37) | "Article 4 / Definitions" | inert (1): heading | | |
| Art 4 lead-in (38) | "For the purposes of this Regulation:" | encoded | defs2 `Art 4 lead-in ...` | tests2 §lead-in (2) |
| Art 4(3) (41) | 'restriction of processing' | encoded | defs2 `Art 4(3) the act is a restriction of processing` | tests2 §Art 4(3) (5) |
| Art 4(4) (42) | 'profiling' | encoded | defs2 `Art 4(4) the processing is profiling` | tests2 §Art 4(4) (15) |
| Art 4(5) (43) | 'pseudonymisation', provided that the additional information is kept separately and protected | fork FK4-1 | defs2 `Art 4(5) the processing is pseudonymisation` | tests2 §Art 4(5) (5) |
| Art 4(9) first sentence (47) | 'recipient': a body to which the data are disclosed, whether a third party or not | encoded | defs2 `Art 4(9) the body is a recipient` | tests2 §Art 4(9), recipient (18) |
| Art 4(9) "However" clause (47) | public authorities receiving data in a particular inquiry under law are not recipients | fork FK4-2 | same function | same |
| Art 4(9) last clause (47) | their processing of those data shall be in compliance with the applicable rules; regulative | fork FK4-3 | defs2 `Art 4(9) the processing by the public authority ... is in compliance ...`, `Art 4(9) the public authority must process ...` | tests2 §Art 4(9), compliance (5) and the 2 traces |
| Art 4(10) (48) | 'third party' | encoded | defs2 `Art 4(10) the body is a third party` | tests2 §Art 4(10) (11) |
| Art 4(11) (49) | 'consent' | encoded | defs2 `Art 4(11) the indication is the consent of the data subject` | tests2 §Art 4(11) (9) |
| Art 4(12) (50) | 'personal data breach' | encoded | defs2 `Art 4(12) the incident is a personal data breach` | tests2 §Art 4(12) (14) |
| Art 4(13) (51) | 'genetic data' | fork FK4-4 | defs2 `Art 4(13) the data are genetic data` | tests2 §Art 4(13) (5) |
| Art 4(14) (52) | 'biometric data' | encoded | defs2 `Art 4(14) the data are biometric data` | tests2 §Art 4(14) (6) |
| Art 4(15) (53) | 'data concerning health' | fork FK4-5 | defs2 `Art 4(15) the data are data concerning health` | tests2 §Art 4(15) (6) |
| Art 4(13)-(15) feeding Art 9(1) (51-53) | the categories that P1's choice `Art 9(1) category of personal data` takes from these three definitions | fork FK4-6 | defs2 `Art 4(13) to (15) the categories ...`, `Art 4(13) to (15) the category ...` | tests2 §categories (33) |
| Art 4(16) lead-in (54) | 'main establishment' means: | encoded | defs2 `Art 4(16)(a) ...` and `Art 4(16)(b) ...` (the lead-in is quoted in both) | tests2 §Art 4(16)(a), §Art 4(16)(b) |
| Art 4(16)(a) (55) | controller: central administration in the Union, unless the decisions are taken in another establishment with the power to implement them | encoded | defs2 `Art 4(16)(a) the main establishment of a controller` | tests2 §Art 4(16)(a) (8) |
| Art 4(16)(b) (56) | processor: central administration in the Union, or the establishment where the main processing activities take place, to the extent that it is subject to specific obligations | encoded | defs2 `Art 4(16)(b) the main establishment of a processor` | tests2 §Art 4(16)(b) (7) |
| Art 4(17) (57) | 'representative' | encoded | defs2 `Art 4(17) the person is a representative` | tests2 §Art 4(17) (9) |
| Art 4(18) (58) | 'enterprise', including partnerships or associations regularly engaged | fork FK4-7 | defs2 `Art 4(18) the body is an enterprise` | tests2 §Art 4(18) (11) |
| Art 4(19) (59) | 'group of undertakings' | encoded | defs2 `Art 4(19) the set of undertakings is a group of undertakings` | tests2 §Art 4(19) (4) |
| Art 4(20) (60) | 'binding corporate rules' | encoded | defs2 `Art 4(20) the policies are binding corporate rules` | tests2 §Art 4(20) (8) |
| Art 4(21) (61) | 'supervisory authority' | encoded | defs2 `Art 4(21) the body is a supervisory authority` | tests2 §Art 4(21) (9) |
| Art 4(22) lead-in (62) | 'supervisory authority concerned' means a supervisory authority concerned because: | encoded | defs2 `Art 4(22) the supervisory authority is a supervisory authority concerned by the processing` | tests2 §Art 4(22) (7) |
| Art 4(22)(a) (63) | controller or processor established in the Member State | encoded | same function | same |
| Art 4(22)(b) (64) | data subjects residing there substantially affected or likely to be | encoded | same function | same |
| Art 4(22)(c) (65) | a complaint lodged with that authority | encoded | same function | same |
| Art 4(23) lead-in (66) | 'cross-border processing' means either: | encoded | defs2 `Art 4(23) the processing is cross-border processing` | tests2 §Art 4(23) (8) |
| Art 4(23)(a) (67) | establishments in more than one Member State, where the controller or processor is established in more than one | encoded | same function | same |
| Art 4(23)(b) (68) | a single establishment, substantially affecting data subjects in more than one Member State | encoded | same function | same |
| Art 4(24) (69) | 'relevant and reasoned objection' | encoded | defs2 `Art 4(24) the objection is a relevant and reasoned objection` | tests2 §Art 4(24) (6) |
| Art 4(25) (70-72) | 'information society service' by reference to Directive (EU) 2015/1535 | encoded | defs2 `Art 4(25) the service is an information society service` | tests2 §Art 4(25) (2) |
| Art 4(25) footnote 1 (1081) | the citation of Directive (EU) 2015/1535 | inert (1): a citation, not operative | | |
| Art 4(26) (73) | 'international organisation' | encoded | defs2 `Art 4(26) the body is an international organisation` | tests2 §Art 4(26) (4) |
| Art 99 (1076-1080) | entry into force on the twentieth day after publication; applies from 25 May 2018; binding and directly applicable | inert (2): machinery, the Regulation's own commencement (assumed, not ruled; one row) | | |

Terms the range uses and does not define (taken as plain input facts): "freely given", "specific", "informed", "unambiguous" (Art 4(11)); "controlling undertaking", "controlled undertaking" (Art 4(19)); "economic activity" (Art 4(18)); "inquiry" and "Union or Member State law" (Art 4(9)); "central administration", "establishment", "Member State" (Art 4(16), (23)); "substantially affected" (Art 4(22), (23)); "complaint" (Art 4(22)(c)); "draft decision" (Art 4(24)); "independent" (Art 4(21)); "activities of an establishment", "offering", "monitoring" and "in the Union" (Art 3); "technical and organisational measures" (Art 4(5)).
Row count: 50 rows: 28 `encoded`, 14 `fork`, 8 `inert` (4 headings, 2 objects clauses, 1 citation, 1 machinery); none is repealed or blank; there is no out-of-scope row and no deferred row.
Every fork id in the register (FK1-1, FK2-1, FK2-2, FK3-1, FK3-2, FK3-3, FK3-4, FK4-1, FK4-2, FK4-3, FK4-4, FK4-5, FK4-6, FK4-7; 14 entries) is named in the disposition of at least one `fork` row: yes.

## Fork register

Each entry: the provision, the function, the readings with the text that licenses each, the one taken, and why.
"Other reading" is what a human reviewer may overrule.
Every reading below is assumed, not ruled.

| id | provision and function | readings | taken |
| --- | --- | --- | --- |
| FK1-1 | Art 1(3); `Art 1(3) the restriction or prohibition ... is barred` | A: "shall be neither restricted nor prohibited" names no party that restricts or prohibits, so only the decision function is written (as P1's F24-1). B: the addressee is the Member States or the Union's lawmakers, and a prohibition (`SHANT`) with a breach path is written as well. The decision function is the same on both readings; B adds a rule and a trace. | A: the text names no party |
| FK2-1 | Art 2(3) first sentence; `Art 2(3) this Regulation applies ...` and the combined `Art 3 ...` | A: "For the processing of personal data by the Union institutions, bodies, offices and agencies, Regulation (EC) No 45/2001 applies" displaces this Regulation for that processing (the K2 brief's reading): `JUST FALSE` to "this Regulation applies", and the combined answer is `JUST FALSE`. B: the sentence names the instrument that governs those bodies and does not itself disapply this Regulation, so the answer is `NOTHING` and the combined answer follows Art 2(1)-(2) and Art 3. The two differ for processing by a Union body that is within Art 2(1) and Art 3(1): `JUST FALSE` against `JUST TRUE` or `NOTHING`. Whether Regulation (EC) No 45/2001 is still the instrument that applies is a fact outside the sources. | A, as the brief describes; the text says it only by naming the other instrument, so it is listed under Marginal readings |
| FK2-2 | Art 2(3) second sentence; `Art 2(3) the Union legal act applicable to such processing is adapted ...` | A: the passive "shall be adapted ... in accordance with Article 98" names no party: decision function only. B: the Commission or the Union's lawmaker, with a regulative rule. | A |
| FK3-1 | Art 3; the combined `Art 3 ...` and `Art 3(2) ...` | (i) A processing that meets none of the three limbs: A `NOTHING`, because each limb says "applies" and none says "only" (limited by its own wording, periods ruling (c)). B `JUST FALSE`, reading the heading "Territorial scope" and the three limbs as the whole of territorial scope. (ii) A failed "where" in Art 3(2): A `JUST FALSE` from the limb's own function (periods ruling (b), "where the processing activities are related to"). B `NOTHING`, a limb that says "applies" with no "only". The combined function never turns the limb's `JUST FALSE` into a no. | A for both |
| FK3-2 | the combination of Art 2 and Art 3; `Art 3 this Regulation applies ...` | A: both are required: Art 2(2) "does not apply" and Art 2(3) stop the Regulation whatever Art 3 says, and an Art 3 limb alone does not make it apply without the material scope. B: Art 3 is self-sufficient ("This Regulation applies to the processing of personal data in the context of ..."). The answers differ for a household activity (Art 2(2)(c)) by someone with an establishment in the Union: A `JUST FALSE`, B `JUST TRUE`. | A: Art 2 is headed "Material scope" and Art 3 "Territorial scope" |
| FK3-3 | Art 3(3) "in a place where Member State law applies by virtue of public international law"; `Art 3(3) the territorial limb: ...` | A: the "where" describes the place, a scope limit with no gate word: `NOTHING` when unmet (periods ruling (c)). B: a "where" gate (ruling (b)): `JUST FALSE` when the place is not such a place. | A |
| FK3-4 | Art 3(2)(b) "as far as their behaviour takes place within the Union"; `Art 3(2) the territorial limb: ...` | A: the limb needs the monitored behaviour to take place within the Union; monitoring of behaviour outside it fails (b). B: "as far as" limits the extent, so the limb reaches the part of the monitoring that concerns behaviour in the Union even where other behaviour is outside it; no single input could carry B (as P1's F6-1). | A |
| FK4-1 | Art 4(5) "provided that such additional information is kept separately and is subject to technical and organisational measures"; `Art 4(5) the processing is pseudonymisation` | A: the proviso is an element of the definition: failing it, the processing is not pseudonymisation (`JUST FALSE`; "provided that" is on the brief's list). B: the first part defines pseudonymisation and the proviso adds a requirement on the information, so data that can no longer be attributed without additional information are pseudonymised even if the information is kept with them. | A: the proviso is inside "means" |
| FK4-2 | Art 4(9) "public authorities which may receive personal data in the framework of a particular inquiry in accordance with Union or Member State law shall not be regarded as recipients"; `Art 4(9) the body is a recipient` | A: the exception applies to the receipt in a particular inquiry in accordance with law (inputs `...received in the framework of a particular inquiry` and `the receipt is in accordance with Union or Member State law`). B: the exception covers public authorities of the class that "may receive" data in such an inquiry, whenever they receive data. They differ for an authority of that class that receives personal data outside any inquiry. | A: "in the framework of a particular inquiry" scopes the receipt |
| FK4-3 | Art 4(9) "the processing of those data by those public authorities shall be in compliance"; the decision function and the regulative rule | A: "those data" are the data received in the framework of a particular inquiry, so the duty gates on the inquiry. B: all personal data those authorities receive. | A, following FK4-2 |
| FK4-4 | Art 4(13) "which result, in particular, from an analysis of a biological sample"; `Art 4(13) the data are genetic data` | A: an example of where the data come from, so the input is not read. B: a requirement, so data not resulting from the analysis of a sample are not genetic data (`JUST FALSE`). | A: "in particular" |
| FK4-5 | Art 4(15) "which reveal information about his or her health status"; `Art 4(15) the data are data concerning health` | A: the clause qualifies "personal data": data related to health, or to the provision of health care services, count only if they reveal information about the health status. B: it qualifies only "the provision of health care services", so data related to physical or mental health count without it. | A |
| FK4-6 | Art 4(13)-(15) and P1's choice; `Art 4(13) to (15) the categories ...`, `Art 4(13) to (15) the category ...` | List function. A (taken after review R3): `NOTHING` whenever any of the three definitions answers `NOTHING` (the list is not decided: the definition that gives no answer may be met too); `JUST EMPTY` only when all three are `JUST FALSE`; the full list of the definitions that are `JUST TRUE` only when none answers `NOTHING`. B (the first build): a list of the definitions that are met whatever the others answer, which gave `JUST (LIST genetic data)` for genetic met, biometric no, health `NOTHING`, as though complete. Single-choice function. A (taken, unchanged): any definition that is met gives its category whatever the others answer, the first in the order genetic, biometric, health when more than one is met; `NOTHING` when none is met. B: `NOTHING` when more than one is met. They differ for data that are both genetic and about health; both lead to Art 9(1). | A for both; a caller who wants every category asks the list function and gets `NOTHING` until all three definitions are answered |
| FK4-7 | Art 4(18) "including partnerships or associations regularly engaged in an economic activity"; `Art 4(18) the body is an enterprise` | A: `NOTHING` for a public authority, an agency, another body, or a partnership or association not regularly engaged: "including ..." shows that the term reaches beyond natural and legal persons, so "means a natural or legal person" does not close it. B: `JUST FALSE` for those: "means a natural or legal person engaged in an economic activity". | A: "including" |

## Jural relations

One row per provision that creates a relation.
"Right" below is a claim unless it says power, privilege or immunity; the correlative is in the next column.
A definition, a counting rule and a scope rule are `none`.

| provision | holder | right, privilege, power or immunity | bearer | correlative | L4 rule |
| --- | --- | --- | --- | --- | --- |
| Art 1(1), (2) | | none (objects clauses, inert) | | | |
| Art 1(3) | controllers and processors who move personal data within the Union, and the data subjects whose data move | immunity from a restriction or prohibition of the free movement for reasons connected with data protection | whoever would restrict or prohibit (the text names none; in practice a Member State) | disability | art-1 `Art 1(3)` |
| Art 2(3) first sentence | | none (scope rule: which instrument applies) | | | art-2b `Art 2(3) ...` (two) |
| Art 2(3) second sentence | none seat-bearing: a duty on the lawmaker, no party named (FK2-2) | | | | art-2b `Art 2(3) the Union legal act ...` |
| Art 2(4) | an intermediary service provider and anyone who relies on Directive 2000/31/EC | immunity: the application of the Directive, in particular its liability rules, is untouched | those who would apply this Regulation to displace it (data subjects, authorities) | disability | art-2b `Art 2(4)` |
| Art 3 | | none (scope rules) | | | art-3 |
| Art 4 lead-in, (3) to (5), (9) first and "However" clauses, (10) to (26) | | none (definitions) | | | defs2 |
| Art 4(9) last clause | data subjects whose data the authority receives (and a supervisory authority) | claim that the processing is in compliance with the applicable rules | the public authority that receives the data in a particular inquiry | duty | defs2 `Art 4(9) the public authority must process ...` and the decision function |
| Art 99 | | none (machinery) | | | |

## Marginal readings for a lawyer

Rule (a): a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference).
Rule (b): a prohibition or grant limited by its own wording does not count as no, so the answer is `NOTHING`.
Periods ruling (b) and (c) of 2026-11-05 (the Guide, which governs the brief where they differ): a failed "where" gives `JUST FALSE`, and a scope limit with no gate word gives `NOTHING`.

**Branches that rest on an inference (`JUST FALSE`), other reading `NOTHING`.**
- Art 2(3) first sentence, and every answer that depends on it (`Art 2(3) this Regulation applies ...`, and the first arm of `Art 3 this Regulation applies ...`): the naming of Regulation (EC) No 45/2001 as the instrument that applies is read as the Regulation's no (FK2-1).
- Art 3(2): a failed "where" (neither offering nor monitoring in the Union) answers `JUST FALSE` from the limb's function (FK3-1 (ii)); the combined answer does not repeat it.
- Art 2(3) second sentence and Art 4(9) last clause: an unmet "shall" answers `JUST FALSE` as the provision's own question (split site (i)).
- Art 4(9) "However" clause: the exception is read as applying to the receipt in the inquiry (FK4-2).
- Art 4(5): the proviso "provided that" is an element of the definition (FK4-1).

**Branches that rest on rule (b) or on a term left open (`NOTHING`), other reading `JUST FALSE`.**
Art 1(3) for a movement outside the Union, a case with no measure, and a measure for another reason; Art 2(3) first sentence for processing by anyone but the Union bodies (both functions); Art 2(3) second sentence for an act that is not applicable to such processing; Art 2(4) for another instrument; Art 3(1), Art 3(3) and the combined Art 3 when no limb is met (FK3-1, FK3-3); Art 3(2) for data subjects outside the Union or a controller established in the Union; Art 4 lead-in outside this Regulation; Art 4(9) decision function outside "those public authorities"; Art 4(16)(a) and (b) for a controller or processor with establishments in one Member State, (a) for a controller with no central administration in the Union and no exception, and (b) "to the extent that the processor is subject to specific obligations" and for a processor with neither central administration nor main processing establishment in the Union; Art 4(18) for another body or a partnership not regularly engaged (FK4-7); Art 4(13) to (15) categories when a definition gives no answer or none is met (FK4-6).

## Split sites (your part)

Two questions the Guide leaves to me, decided site by site on the text's own words.

**(i) An unmet element of an infringement: JUST FALSE or NOTHING?**
3 sites: 3 have a NOTHING branch and 2 have a JUST FALSE branch (the two with both are Art 2(3) second sentence and Art 4(9) last clause); 3 + 2 - 2 = 3.
- Art 1(3) (`Art 1(3) ...`): NOTHING when an element is unmet (the movement is not within the Union, there is no measure, or the reason is another): the provision is limited to a restriction or prohibition "within the Union" and "for reasons connected with the protection of natural persons"; other reading `JUST FALSE`.
- Art 2(3) second sentence (`Art 2(3) the Union legal act ... is adapted ...`): NOTHING when the act is not "applicable to such processing" (a scope limit with no gate word); JUST FALSE when it is applicable and not adapted ("shall be adapted", the provision's own question); other reading NOTHING for the second.
- Art 4(9) last clause (`Art 4(9) the processing by the public authority ... is in compliance ...`): NOTHING outside "those public authorities" (not in an inquiry, not in accordance with law, or not a public authority); JUST FALSE when the processing does not comply ("shall be in compliance"); other reading NOTHING for the second.

**(ii) A grant or "may" gated by "where", "when", "upon", "insofar as", "provided that":**
0 sites.
The text of K2's range has one "may" that could look like a site: Art 4(9) "public authorities which may receive personal data in the framework of a particular inquiry in accordance with Union or Member State law".
It describes the class of authorities and is not a grant to the person asked about, and the function that reads it answers a definition's question ("is the body a recipient"); it is therefore not counted here, and its readings are in FK4-2.

## Rules with no breach path (your part)

A `MUST` with no time limit and no consequence stated can only stand or be fulfilled; no `#TRACE` can show it breached, and no deadline or consequence has been invented.
There are 2 traces in 1 file (both in `gdpr-definitions-2-tests.l4`); each result was read from the diagnostics (`l4 run` prints each as an `eval/result` diagnostic): the first is `FULFILLED`, the second prints the standing obligation (`PARTY ... MUST ... HENCE FULFILLED`) after `(WAITUNTIL 1000)`.

| rule | provision | what the traces give |
| --- | --- | --- |
| `Art 4(9) the public authority must process the data it receives in a particular inquiry in compliance with the applicable data protection rules` | Art 4(9) last clause | FULFILLED when the authority processes in compliance; standing obligation after `WAITUNTIL 1000` |

K2 has no rule with a breach path: no provision of its range names a party and a prohibition, and none gives a deadline or a consequence.
Art 1(3) ("shall be neither restricted nor prohibited") and Art 2(3) second sentence ("shall be adapted") name no party and are decision functions only (FK1-1, FK2-2).

## What the stable binary does not accept

Binary 1.6.112 (main), measured on 2026-11-26.
Silent (the answer is wrong and nothing is reported):
- A one-line `NOT a OR b` reads as `NOT (a OR b)`: `#EVAL NOT FALSE OR TRUE` printed FALSE, `#EVAL NOT TRUE AND FALSE` printed TRUE and `#EVAL (NOT FALSE) OR TRUE` printed TRUE (measured with a probe, deleted).
  Every `NOT` in K2's files is parenthesised (`grep` finds none outside a comment without a bracket).
- A `#TRACE` is not counted by `check.sh`: both results were read from the diagnostics.
Loud (the binary or the gate stops with an error):
- `GIVETH A MAYBE LIST OF X` is a parse error (`unexpected LIST`, expecting `(`, `A`, `AN`, ...); `MAYBE (LIST OF X)` is accepted.
- The main prelude has no `head` (`I could not find a definition for the identifier head`); `at list 0` (0-based) is accepted.
- `srcrefs.py check` refuses a quote line that has no text (a raw line that is only `);`, line 72 of the text): quote lines 70-71 of point (25) and cite `src:70-71`.
Measured to be accepted (so a later part need not wonder): `EQUALS JUST (LIST ...)` on a `MAYBE` of a list; `any`, `null`, `at` and `append` on lists of enumeration constructors; `IF ... THEN ... ELSE ...` and `BRANCH` arms with `--` comment lines between them; a `DEONTIC` whose party and action types each have one constructor; `@export` on a question whose inputs are enumerations and whose result is a `MAYBE` of an enumeration; a regulative rule with a `MUST` and no `WITHIN`, `HENCE` or `LEST`.
Not tried, because the dialect table says main rejects them: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` outside `LEST BREACH`, a section `GIVEN`, `TYPICALLY`, sets, an opaque `DECLARE`, `YMD`, `@lang`, `@nonexhaustive`, an input named in an action.
Where a skill describes a construct main rejects, the binary governs, and K2 did not use the construct.

## What check.sh prints

Refreshed 2026-11-26 after the R3 fix (the list function of Art 4(13) to (15)), from this folder, target main with `L4_TARGET=unstable` (the binary already is the main build, so the second main run is skipped and the lead runs both builds): the main build 1.6.112 (`$L4_MAIN`) as `L4`, `JL4_LIBRARY_PATH` unset, exit status 0.
The folder now holds more than K2's files, so the listing is longer than the one K2 first printed; the first line is `check.sh`'s own and goes to stderr.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
gdpr-core-2.l4                                 0         0       0        0         0
gdpr-core.l4                                   0         0       0        0         0
gdpr-definitions-2-tests.l4                    0       217       0        0         0
gdpr-definitions-2.l4                          0         0       0        0         0
gdpr-definitions-tests.l4                      0       121       0        0         0
gdpr-definitions.l4                            0         0       0        0         0
K2-art-1.l4                                    0         0       0        0         0
K2-art-2b.l4                                   0         0       0        0         0
K2-art-3.l4                                    0         0       0        0         0
K2-cases-mirror.l4                             0        93       0        0         0
K2-cases-seat-controller.l4                    0       119       0        0         0
K2-cases-seat-subject.l4                       0        93       0        0         0
K2-seat-controller.l4                          0         0       0        0         0
K2-seat-subject.l4                             0         0       0        0         0
K2-tests-art-1.l4                              0         5       0        0         0
K2-tests-art-2b.l4                             0        12       0        0         0
K2-tests-art-3.l4                              0        33       0        0         0
P2-art-12.l4                                   0         0       0        0         0
P2-art-13.l4                                   0         0       0        0         0
P2-art-14.l4                                   0         0       0        0         0
P2-art-15.l4                                   0         0       0        0         0
P2-art-16.l4                                   0         0       0        0         0
P2-art-17.l4                                   0         0       0        0         0
P2-art-18.l4                                   0         0       0        0         0
P2-art-19.l4                                   0         0       0        0         0
P2-art-20.l4                                   0         0       0        0         0
P2-art-21.l4                                   0         0       0        0         0
P2-art-22.l4                                   0         0       0        0         0
P2-art-23.l4                                   0         0       0        0         0
P2-cases-mirror.l4                             0       251       0        0         0
P2-cases-seat-controller.l4                    0       403       0        0         0
P2-cases-seat-subject.l4                       0       399       0        0         0
P2-seat-controller.l4                          0         0       0        0         0
P2-seat-subject.l4                             0         0       0        0         0
P2-tests-art-12.l4                             0        80       0        0         0
P2-tests-art-13.l4                             0        48       0        0         0
P2-tests-art-14.l4                             0        86       0        0         0
P2-tests-art-15.l4                             0        44       0        0         0
P2-tests-art-16.l4                             0        12       0        0         0
P2-tests-art-17.l4                             0        61       0        0         0
P2-tests-art-18.l4                             0        34       0        0         0
P2-tests-art-19.l4                             0        15       0        0         0
P2-tests-art-20.l4                             0        35       0        0         0
P2-tests-art-21.l4                             0        34       0        0         0
P2-tests-art-22.l4                             0        43       0        0         0
P2-tests-art-23.l4                             0        33       0        0         0
(the lead's independent test files and the folder's total line are in the section "Independent test pass" below, from the lead's final run)
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Whose modules these are.
- **K2's (14 modules):** `gdpr-core-2.l4`, `gdpr-definitions-2.l4`, `gdpr-definitions-2-tests.l4` and the eleven `K2-*.l4` files.
  K2's own total: 0 errors, **572 assertions satisfied**, 0 failed, 0 refused: 217 (`gdpr-definitions-2-tests.l4`) + 5 + 12 + 33 (`K2-tests-art-1`, `-2b`, `-3`) + 93 + 119 + 93 (`K2-cases-seat-subject`, `K2-cases-seat-controller`, `K2-cases-mirror`); `grep -c '^#ASSERT'` over those files gives 572.
  Before the fix the total was 556; the fix added 16 assertions to `gdpr-definitions-2-tests.l4` (201 to 217) and changed the expected value of one (see Findings).
- **P1's keel files (3 modules):** `gdpr-core.l4`, `gdpr-definitions.l4`, `gdpr-definitions-tests.l4`: 0 errors, 121 assertions satisfied.
- **Not K2's:** the `P2-*` modules and the lead's independent test files (`tests-independent-2*.l4`); K2 did not write or change them.
- The folder total at this refresh was 48 modules; the final folder total, after the lead's last files, is under "Independent test pass" (49 modules).
- No K2 assertion is expected to fail: K2 listed nothing in `check.sh`'s `expected_failed`.
- `srcrefs.py check --refs` and `--strict` over K2's files (`gdpr-core-2.l4`, `gdpr-definitions-2.l4`, `gdpr-definitions-2-tests.l4`, `K2-*.l4`): `66 src: lines, 37 runs, 36 locators, 0 problems`, both times; over every `.l4` file in the folder: `247 src: lines, 133 runs, 132 locators, 0 problems`, both times (RAW is `inputs/eu-gdpr-2016-679-consolidated-20160504.txt`).
- All 108 quoted pieces in the comments of K2's files (99 in the first build, more after the R3 fix) were found verbatim in the consolidated text, after normalising the quotation marks and treating `...` as an elision.
- `check.sh` counts no trace: the two `#TRACE` directives (both in `gdpr-definitions-2-tests.l4`) were read by eye on the main build: FULFILLED, and the standing obligation after `WAITUNTIL 1000`.
- The unstable build was not run by K2; the lead runs the second build.

## Independent test pass (written by the lead, 2026-11-26)

An independent Sonnet author wrote 242 answers from the consolidated text before opening any file of the deposit (`lead/answers.md`; 61 of them on K2's range: Art 1(3), 2(3), 2(4), 3 and Article 4; 14 marked OPEN across both ranges) and asserted them in `tests-independent-2.l4` and `tests-independent-2-items.l4`.
On K2's range: 61 blocks, every one asked by a K2 seat question or a layer-1 function (none left unasked); 1 failing assertion, K2-006.
- **K2-006, Art 2(3) first sentence, OPEN, recorded as fork FK2-1 (assumed, not ruled).** The question "does this Regulation apply to my processing, where I am a Union institution, body, office or agency" is answered `JUST FALSE` by the encoding (reading A of FK2-1: the sentence assigns Union bodies to Regulation (EC) No 45/2001 and so displaces this Regulation, the reading the K2 brief itself states) and `NOTHING` by the author (reading B: the sentence says only "Regulation (EC) No 45/2001 applies", it does not say in its own words that this Regulation does not). The author's assertion is in `tests-independent-2-open.l4` and counted in `check.sh`'s `expected_failed` (4 for that file, one per open reading of the part-2 pass).
- No encoder's error and no author's error was found in K2's range by this pass; the refuter's R3 (the list function of Art 4(13) to (15)) was found by review and fixed (see Findings).
Final run of the folder (the lead, both builds, 2026-11-26): `TOTAL (49 modules)  4 errors  2646 satisfied  4 failed  0 refused` on UNSTABLE and on MAIN, every module `same`; the 4 failed are the four expected failures of `tests-independent-2-open.l4`; 2650 `#ASSERT` lines in the folder = 2646 + 4.

## Findings

- **The text findings.**
  Art 2(3) does not say "does not apply": it says "Regulation (EC) No 45/2001 applies", and the "does not apply" to Union bodies is a reading (FK2-1).
  Art 3 has three limbs that each say "applies" and no "only", so the text does not say that a processing within none of them is outside the Regulation (FK3-1).
  Art 3(2)'s "where the processing activities are related to" is a gate of the limb: the limb fails when neither offering nor monitoring in the Union holds, while Art 3(1) and (3) may still apply.
  Art 4(9) says in one sentence that authorities receiving data in a particular inquiry are not recipients and in the next clause that their processing shall comply with the applicable rules, a duty with a named party and no deadline.
  Art 4(16)(a) names "the place of its central administration in the Union": for a controller with none there, and no establishment taking the decisions with the power to implement them, the text gives no main establishment.
  Art 4(21) 'supervisory authority' leans on Article 51 and Art 4(17) 'representative' on Article 27; both are plain inputs here.
- **No expected value was edited to match the code's output.**
  Every assertion of K2 passed on its first run (556 assertions: 201 in the definitions tests, 5 + 12 + 33 in the three article tests, 93 + 119 in the seat cases and 93 in the mirror).
  Two changes came later.
  The Art 4(9) direction fix changed a seat question's name and not a value (see Seats).
  The adversarial review's R3 changed ONE expected value, with a visible comment in the file: `Art 4(13) to (15) the categories ...` for `(JUST TRUE) NOTHING FALSE NOTHING` was `JUST (LIST genetic data)` and is `NOTHING`, because a definition that gives no answer may be met too and the list was given as complete; the code was changed first, on the text (the three definitions "mean" their terms), and 16 assertions were added, one for each position of `NOTHING` and for the single-choice function that keeps its answer (572 assertions now).
- **Mutation spot checks.**
  Six one-line changes to the encoding were made on a copy of the folder, each was run against the tests of its module with `check.sh`'s counting of failed assertions, and the copy was deleted: Art 4(5) `AND` to `OR` (4 assertions failed), the Art 3 combined answer `NOTHING` to `JUST FALSE` when no limb is met (3), the Art 4(9) exception without its `the receipt is in accordance with ...` condition (1), Art 2(3) `JUST FALSE` to `NOTHING` (1), the Art 3 combined answer `NOTHING` for `JUST FALSE` material scope (2), and Art 4(22) with the "likely to be substantially affected" limb dropped (1).
  After the R3 fix three more were made on a copy holding only K2's keel files and the definitions tests, and the copy was deleted: the list function's `NOTHING` arm answering `JUST EMPTY` (12 assertions failed), the single-choice function without its health arm (2), and the list function without the health position of `NOTHING`, which is the old R3 bug (4).
  Every change was caught.
  This is a spot check, not a mutation-testing run.
- **Lines 12-13** (the Chapter I heading) are assigned to no part by `inputs/PARTS.md`; K2 recorded them as an inert heading of its own Article 1.
- **The seam name `Art 2(1) and (2) the processing is within the material scope of this Regulation`** was taken from PLAN.md sections 3.3 and 4.1 and NOTES.md fork F2-1; when K2 was written P1's modules were not in the builder's folder, so the name was not read in P1's code and the wiring was not run against it; in this row the name matches `P1-art-2.l4` exactly (checked 2026-11-26), and the wiring is still not run.
- **The kind of a body is as the person states it.**
  `Kind of person or body` has `legal person` and `public authority` as separate members: a public authority that is a legal person is stated as either, and Art 4(17) (natural or legal person only) and Art 4(21) (public authority only) answer `JUST FALSE` for the kind not named.
- **K2 itself ran no independent test pass and no adversarial review** (a single agent, no subagent); the closing pass was run afterwards, and its test pass and review (R3) are described above.
- **Unread arguments are by design**; the list is in "Design choices that are mine".

## Open questions

For a lawyer.
- Does Art 2(3) first sentence disapply this Regulation for processing by the Union institutions, bodies, offices and agencies, or does it only name the instrument that governs them (FK2-1)? Is Regulation (EC) No 45/2001, which the sources do not contain, still the instrument that applies?
- Do the three limbs of Art 3 exhaust the territorial scope, so that a processing within none of them is outside the Regulation (FK3-1)? Must Art 2 and Art 3 both be met (FK3-2)?
- Is the "where" of Art 3(2) a gate (`JUST FALSE`) or a scope limit (`NOTHING`), and the "where" of Art 3(3) (FK3-1, FK3-3)? Does "as far as their behaviour takes place within the Union" in Art 3(2)(b) limit the extent of the monitoring or require that the monitored behaviour be in the Union (FK3-4)?
- Should Art 1(2), which says what the Regulation protects, weigh as an input to an open-textured judgment of a later part (for example "freely given" in Art 4(11), or a "reasonable" step)? K2 encodes no function for it (inert, reason 1).
- Art 99(2) says the Regulation applies from 25 May 2018: should a processing before that date be answered by a date input? K2, as the brief says, records Art 99 as inert machinery and has no date axis.
- Art 4(5): is the proviso an element of "pseudonymisation" (FK4-1)? Art 4(9): does the "However" exception cover the receipt in the inquiry only (FK4-2), and does the duty cover the data received in the inquiry only (FK4-3)?
- Art 4(13): is the analysis of a biological sample an example or a requirement (FK4-4)? Art 4(15): what does "which reveal information about his or her health status" qualify (FK4-5)? Art 4(18): is a public authority, an agency or another body an enterprise when it is engaged in an economic activity (FK4-7)?
- Art 4(16)(a): what is the main establishment of a controller whose central administration is outside the Union and whose decisions are taken in no establishment with the power to implement them? The text names only a central administration in the Union.
- Art 4(11): the four qualities "freely given", "specific", "informed" and "unambiguous" are plain inputs; how do they relate to Art 7(4) (P1), which tells a person assessing whether consent is freely given to take utmost account of conditionality?

## Provenance of the other files

`check.sh`, `fetch-main-l4.sh` and `srcrefs.py` were given and are unchanged by K2 (K2 listed no failing module in `check.sh`'s `expected_failed`: none is expected to fail).
`gdpr-core.l4`, `gdpr-definitions.l4` and `gdpr-definitions-tests.l4` are P1's, read-only, and were not touched.
`NEEDS-CORE.md` is not written: the types K2 needed are in `gdpr-core-2.l4`, which K2 may add under the brief.
`notes/gen-seats.py` is K2's: it wrote the five seat files and is kept so that they can be re-derived (run from the folder: `python3 -I notes/gen-seats.py`).
