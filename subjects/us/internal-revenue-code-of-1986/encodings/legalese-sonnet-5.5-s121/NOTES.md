# NOTES: 26 U.S.C. section 121, exclusion of gain from sale of principal residence

Encoding `legalese-sonnet-5.5-s121`: a single Sonnet 5.5 agent working alone from the brief (a copy is in `BRIEF.md`).

**Status: draft, written 2026-11-17 and revised 2026-11-18 after an independent reader's findings (what changed is in `PROGRESS.md`).**
No domain expert has read it against the text.
How each claim below was checked: statements about what the text says are quotations, checked mechanically by `srcrefs.py check --refs` and `srcrefs.py check --strict` (0 problems at each, at the last run);
statements that a rule exists, and which tests cover it, are checked by `coverage.py` (0 problems at the last run);
every count is printed by `check.sh` or by `coverage.py`, not typed by hand; the marginal-readings list is made by a script that reads the tags in the `.l4` files.

**Target: `main`.**
Written with `l4` 1.6.110 (main, e51181d, 2026-11-11), path `<scratchpad>/bin/l4-main-110`, sha256 `9c7656f74151383da2c7344ad53269a8754bd874af8eb513180d61dc145016c7`.
Compared with the second stable build `l4` 1.6.109 (main, 4c887e0, 2026-11-04) by `check.sh`; the output is in the section "What check.sh prints".

**The text is a plain-text rendering, not the official text.**
`usc26-s121.txt` was made by a converter script (`uslm_section_to_text.py`) from the OLRC's USLM XML at release point Public Law 119-142 (current through 2026-11-10).
Under 1 U.S.C. 204 the Code is prima facie evidence of the law, and Title 26 is not positive law.
Nothing here is verified against the official text.
The OLRC's own notes (`usc26-s121-notes.txt`) were used as context only and have no coverage rows.

## Seat

The seat is an individual taxpayer who has sold, or is thinking of selling, a home (or whose home was destroyed, stolen, condemned or taken), asking on facts they can state whether the gain is left out of gross income, how much of it, and what stops or reduces the exclusion.

Why this seat: section 121 is a rule about what one person may leave out of their own gross income, so the person to whom the law is applied is the taxpayer.

The questions are asked from the taxpayer's own facts: how long they owned it, how long they lived in it, whether they are married and file jointly, what they sold it for, what they used it for.

There is no seat for the Internal Revenue Service or the Treasury: their side of each relation appears only as what it means for the taxpayer (see "Jural relations").

Layer 2 is `s121-seat.l4` (20 questions, each with `@export` and `@desc`, grouped under `§` headings in the Act's order) and `s121-cases-seat.l4` (worked cases, every question at least once).

The questions in the first groups assume the taxpayer has none of the special facts the later groups ask about; the header of `s121-seat.l4` lists them.

Three of those facts are also asked by the questions that give an amount, because a person in those situations could not otherwise ask how much is left out.

The four filing-alone questions (how much is left out, how much is still taxed, what stops or reduces the exclusion, and the most that can be left out) ask whether the spouse died before the sale and the taxpayer has not remarried, with the late spouse's dates of owning, living in the home and any earlier sale (the rules of (b)(4) and (d)(2)), and one stay in a care facility with whether it is licensed ((d)(7)).

The three of them that give an amount of the gain, and the two joint-return questions, also ask whether the taxpayer elects under (f) not to have the section apply; the two joint-return questions ask the taxpayer's stay in a care facility but not a surviving spouse, because a joint return is not an unmarried individual's.

The question on the 5-year period asks whose the service is, the taxpayer's own or the spouse's ((d)(9)(A): "such individual or such individual's spouse"), and takes one period of service; the election it asks is always the taxpayer's own.

Not asked by the amount questions: any service abroad (use the question on the 5-year period or the layer-1 module that takes the whole record), the spouse's own stay in a care facility or incapacity on a joint return, the late spouse's service, and more than one stay in a care facility.

The two-year tests, the reduced exclusion, the limit on a joint return, depreciation and nonqualified use keep the narrower assumption, so each of them answers as for a taxpayer with none of these facts; the amount questions are the ones to ask when any of them is true.

The layer-1 module `s121-whole.l4` takes every such fact, as the two records `Individual facts` and `Sale facts`, and the seat builds those records from plain inputs with the constructors there.

The language of the stable binary has no record update, so each constructor takes every field; a field that no question asks about is given a fixed "none" and the seat's header says which.

A date a taxpayer cannot give because the fact does not apply (a second stay, an earlier sale) is "enter any date": the yes/no answer before it decides whether the date is read.

Substituted numbers: none.

The text lets no Minister substitute a figure; the figures $250,000, $500,000, 5 years, 2 years, 10 years, 90 days, 50 miles and the dates May 6, 1997 and January 1, 2009 are the text's own.

What the regulations would add is asked as an input: whether a reason counts as "unforeseen circumstances" ((c)(2)(B), (b)(5)(C)(ii)(III)); the regulations and the Secretary's specification are not among the sources.

## What is encoded and what is not

Every provision of the text has a row in the coverage table below; none is out of scope or deferred.

Layer 1 is nine modules: `s121-nouns.l4` (types), `s121-support.l4` (span arithmetic and three-valued helpers, not provisions), then one module per natural group of the section, in import order: `s121-a-exclusion.l4` (a), `s121-d9-service.l4` ((d)(9) to (d)(12)), `s121-d1-special.l4` ((d)(1) to (d)(8)), `s121-b-limitations.l4` ((b)(1) to (b)(5)), `s121-c-reduced.l4` (c), `s121-efg.l4` ((e), (f), (g)) and `s121-whole.l4` (the assembly), with six test files `s121-tests-*.l4`.

`s121-whole.l4` calls the rules of the other modules in the order the text's cross-references give and states no rule of its own: the gates ((d)(5)(A), (e), (f), (d)(10), (d)(8)); each individual's holding with (d)(2) to (d)(5)(C), (d)(7) and (g) applied, over the 5-year period of (a) as extended by (d)(9) or (d)(12); the route (a) with (d)(1) and (b)(3), or else (c); the limitation ((b)(1), (b)(2), (b)(4), reduced by (c)(1)); the gain after (d)(6) and then (b)(5), as (b)(5)(D) orders; the smaller of that gain and the limitation.

The section creates no duty on any named party (every provision gives, takes away or counts), so no regulative rule (the `PARTY`, `MUST`, `MAY`, `SHANT` form) is encoded; every provision is a decision function.

Borrowed terms are inputs, never memory: sections 216, 267(b), 707(b), 877(a)(1), 1031, 1033, 1041(a), 1223(6) (repealed), 1250(b)(3) and the whole of section 1034 (repealed); title 10 section 101(a)(5); title 5 section 2105; the Foreign Service Act section 103; the Peace Corps Act sections 5 and 6.

What the gain is, what the date of the sale or exchange is, and what makes a place the taxpayer's principal residence are not defined by the section and are facts the person states.

Not modelled: a trust, an estate or a partnership as the taxpayer; a taxpayer who is married but files separately (the spouse's own ownership, use and earlier sales are not asked unless a joint return is made; `Sale facts` carries, for such a taxpayer, the periods a spouse or former spouse used the home and, under fork F30, the spouse's periods of service); more than one earlier sale (the most recent decides both rules that read earlier sales); more than two stays in the seat layer (layer 1 takes any number); a spouse's section 877(a)(1) status on a joint return (fork F18); a reduced exclusion on a joint return (fork F17).

## Jural relations

Hohfeld's correlatives: a claim and a duty; a privilege and a no-right; a power and a liability; an immunity and a disability.

The two parties are the taxpayer (T) and the United States as the taxing authority (US).

Section 121 is a series of immunities (T cannot be made to include the gain in gross income, to a limit) and of the powers and disabilities that bound them; it creates no claim and no duty.

Each relation is stated once, between the two parties, and named neutrally; a provision that only defines or counts is listed once as `none`.

| provision | holder | bearer of the correlative | relation | L4 rule |
| --- | --- | --- | --- | --- |
| (a) | T | US | immunity of T from including the gain in gross income / disability of US to include it | s121-a-exclusion: s 121(a) gross income does not include the gain |
| (b)(1) | T | US | the immunity of (a) is limited to $250,000 / the disability of US is limited to the same amount | s121-b-limitations: s 121(b)(1) |
| (b)(2)(A) | T and spouse (joint return) | US | immunity enlarged to $500,000 / disability enlarged to match | s121-b-limitations: s 121(b)(2)(A) |
| (b)(2)(B) | T and spouse (joint return) | US | immunity to the sum of what each would have if unmarried / disability to match | s121-b-limitations: s 121(b)(2)(B) |
| (b)(3) | US | T | immunity of US from the claim of (a) for a second sale within 2 years / disability of T to claim it | s121-b-limitations: s 121(b)(3) |
| (b)(4) | T (surviving spouse) | US | immunity enlarged to $500,000 for 2 years after the death / disability to match | s121-b-limitations: s 121(b)(4) |
| (b)(5)(A) | US | T | immunity of US from the claim of (a) for gain allocated to nonqualified use / disability of T | s121-b-limitations: s 121(b)(5)(A) |
| (b)(5)(B), (C), (D) | none | none | none (a ratio, a definition and an order of application) | s121-b-limitations: s 121(b)(5)(B), (C), (D) |
| (c)(1) | T | US | immunity at a reduced limit where (c)(2) holds / disability of US to that extent | s121-c-reduced: s 121(c)(1) |
| (c)(2) | none | none | none (the condition on which (c)(1) operates) | s121-c-reduced: s 121(c)(2) |
| (d)(1) | T and spouse (joint return) | US | the immunities of (a) and (c) pass to the joint return if either spouse satisfies the requirements | s121-d1-special: s 121(d)(1) |
| (d)(2), (d)(3), (d)(4), (d)(5), (d)(7) | none | none | none (counting and treating-as rules) | s121-d1-special |
| (d)(6) | US | T | immunity of US from the claim of (a) for gain up to the depreciation adjustments / disability of T | s121-d1-special: s 121(d)(6) |
| (d)(8)(A) first limb | T | US | power of T to elect that the section not fail to apply to a remainder interest / liability of US to that election | s121-d1-special: s 121(d)(8)(A) |
| (d)(8)(A) second limb, (d)(8)(B) | US | T | immunity of US from the claim for another interest sold separately, and for a sale to a related person / disability of T | s121-d1-special: s 121(d)(8)(A), (B) |
| (d)(9)(A), (d)(12)(A) | T | US | power of T to elect that the 5-year period be suspended / liability of US to the suspension | s121-d9-service: s 121(d)(9)(A) the running of the 5-year period; s 121(d)(12)(A) |
| (d)(9)(B), (d)(12)(B) | US | T | immunity of US from an extension beyond 10 years / disability of T | s121-d9-service: s 121(d)(9)(B) |
| (d)(9)(C) | none | none | none (definitions) | s121-d9-service: s 121(d)(9)(C) |
| (d)(9)(D)(i) | US | T | immunity of US from a second election while one is in effect / disability of T | s121-d9-service: s 121(d)(9)(A) the running of the 5-year period |
| (d)(9)(D)(ii) | T | US | power of T to revoke the election / liability of US to the revocation | s121-d9-service: s 121(d)(9)(A) the running of the 5-year period |
| (d)(10) | US | T | immunity of US from the claim of (a) for like-kind property sold within 5 years of acquisition / disability of T | s121-d9-service: s 121(d)(10) |
| (d)(11) | none | none | none (repealed) | none |
| (e) | US | T | immunity of US from the claim of (a) where section 877(a)(1) applies / disability of T | s121-efg: s 121(e) |
| (f) | T | US | power of T to elect that the section not apply / liability of US to that election | s121-efg: s 121(f) |
| (g) | none | none | none (a counting rule) | s121-efg: s 121(g) |

## Coverage table

Built by `coverage.py` from the text itself: one row for the header, the title, every subsection, paragraph, subparagraph, clause and subclause (each from its label line to the line before the next label), every item of the list in (d)(9)(C)(iv), the source credit and the footnote, and then a row for each defined or borrowed term.

Every row has one disposition: `encoded`, `fork` (the row points at the fork register and at the rule that encodes the chosen reading), `inert` (with the reason number, 1 not operative, 2 machinery, 3 shown repealed or blank), or `repealed or blank in this text`.

`coverage.py` fails if a unit has no disposition, if a rule named in a row is not defined in the module named, if a test file is missing, or if any non-blank line of the text falls in no row.

Audit: text lines 159, non-blank 156, covered by a row 156, uncovered 0

Audit: rows from the text's units 101 (of which the office rows 10), defined-term rows added 11, rows in all 112

Audit: dispositions encoded 71, fork 28, inert 12, repealed or blank in this text 1

Audit: inert rows by reason: 1 -> 12, 2 -> 0, 3 -> 0

Audit: problems 0

| row | lines | text | disposition | rule (module: name begins) | tests | forks / reason |
| --- | --- | --- | --- | --- | --- | --- |
| header | 1-11 | Internal Revenue Code of 1986 | inert | none | none | 1: not operative (the converter's header: source, release point, licence note) |
| title | 12 | § 121. Exclusion of gain from sale of principal residence | inert | none | none | 1: not operative (the section's number and heading) |
| (a) | 13-14 | Exclusion | fork | s121-a-exclusion: s 121(a); s121-whole: s 121(a) | s121-tests-a, s121-tests-whole, s121-cases-seat | F1, F2, F3, F4, F5, F6 |
| (b) | 15 | Limitations | inert | none | none | 1: not operative (heading: Limitations) |
| (b)(1) | 16-17 | In general | encoded | s121-b-limitations: s 121(b)(1) | s121-tests-b, s121-tests-whole, s121-cases-seat |  |
| (b)(2) | 18-19 | Special rules for joint returns | encoded | s121-b-limitations: s 121(b)(2)(A) paragraph (1) is applied; s121-whole: s 121(b) the limitation before | s121-tests-b, s121-tests-whole, s121-cases-seat |  |
| (b)(2)(A) | 20-21 | $500,000 Limitation for certain joint returns | encoded | s121-b-limitations: s 121(b)(2)(A) paragraph (1) is applied; s121-b-limitations: s 121(b)(2)(A) the limitation | s121-tests-b, s121-tests-whole |  |
| (b)(2)(A)(i) | 22 | either spouse meets the ownership requirements of subsection... | encoded | s121-b-limitations: s 121(b)(2)(A)(i) | s121-tests-b, s121-tests-whole |  |
| (b)(2)(A)(ii) | 23 | both spouses meet the use requirements of subsection (a) wit... | encoded | s121-b-limitations: s 121(b)(2)(A)(ii) | s121-tests-b, s121-tests-whole |  |
| (b)(2)(A)(iii) | 24 | neither spouse is ineligible for the benefits of subsection ... | encoded | s121-b-limitations: s 121(b)(2)(A)(iii) | s121-tests-b, s121-tests-whole |  |
| (b)(2)(B) | 25-26 | Other joint returns | fork | s121-b-limitations: s 121(b)(2)(B); s121-whole: s 121(b)(2)(B) | s121-tests-b, s121-tests-whole, s121-cases-seat | F13, F16, F27 |
| (b)(3) | 27-28 | Application to only 1 sale or exchange every 2 years | fork | s121-b-limitations: s 121(b)(3); s121-whole: s 121(b)(3) | s121-tests-b, s121-tests-whole, s121-cases-seat | F26, F29 |
| (b)(4) | 29-30 | Special rule for certain sales by surviving spouses | fork | s121-b-limitations: s 121(b)(4) | s121-tests-b, s121-tests-whole, s121-cases-seat | F5, F14 |
| (b)(5) | 31 | Exclusion of gain allocated to nonqualified use | inert | none | none | 1: not operative (heading: Exclusion of gain allocated to nonqualified use) |
| (b)(5)(A) | 32-33 | In general | encoded | s121-b-limitations: s 121(b)(5)(A) | s121-tests-b, s121-tests-whole, s121-cases-seat |  |
| (b)(5)(B) | 34-35 | Gain allocated to periods of nonqualified use | fork | s121-b-limitations: s 121(b)(5)(B) | s121-tests-b, s121-tests-whole | F9 |
| (b)(5)(B)(i) | 36 | the aggregate periods of nonqualified use during the period ... | encoded | s121-b-limitations: s 121(b)(5)(C) the aggregate days | s121-tests-b, s121-tests-whole |  |
| (b)(5)(B)(ii) | 37 | the period such property was owned by the taxpayer. | fork | s121-whole: s 121 the treatment of the gain | s121-tests-whole | F16 |
| (b)(5)(C) | 38-39 | Period of nonqualified use | encoded | s121-b-limitations: s 121(b)(5)(C) the aggregate days | s121-tests-b, s121-tests-whole, s121-cases-seat |  |
| (b)(5)(C)(i) | 40-41 | In general | fork | s121-b-limitations: s 121(b)(5)(C)(i) | s121-tests-b, s121-tests-whole, s121-cases-seat | F22 |
| (b)(5)(C)(ii) | 42-43 | Exceptions | encoded | s121-b-limitations: s 121(b)(5)(C) the aggregate days | s121-tests-b, s121-tests-whole |  |
| (b)(5)(C)(ii)(I) | 44 | any portion of the 5-year period described in subsection (a)... | fork | s121-b-limitations: s 121(b)(5)(C)(ii)(I) | s121-tests-b, s121-tests-whole | F23, F28 |
| (b)(5)(C)(ii)(II) | 45 | any period (not to exceed an aggregate period of 10 years) d... | fork | s121-b-limitations: s 121(b)(5)(C)(ii)(II); s121-d9-service: s 121(d)(9)(A) the days of service on qualified official | s121-tests-b, s121-tests-d9, s121-tests-whole | F10, F30 |
| (b)(5)(C)(ii)(III) | 46 | any other period of temporary absence (not to exceed an aggr... | fork | s121-b-limitations: s 121(b)(5)(C)(ii)(III) | s121-tests-b, s121-cases-seat | F10 |
| (b)(5)(D) | 47-48 | Coordination with recognition of gain attributable to deprec... | encoded | s121-b-limitations: s 121(b)(5)(D) | s121-tests-b, s121-tests-whole |  |
| (b)(5)(D)(i) | 49 | subparagraph (A) shall be applied after the application of s... | encoded | s121-b-limitations: s 121(b)(5)(D)(i) | s121-tests-b, s121-tests-whole, s121-cases-seat |  |
| (b)(5)(D)(ii) | 50 | subparagraph (B) shall be applied without regard to any gain... | encoded | s121-b-limitations: s 121(b)(5)(D)(ii) | s121-tests-b, s121-tests-whole, s121-cases-seat |  |
| (c) | 51 | Exclusion for taxpayers failing to meet certain requirements | inert | none | none | 1: not operative (heading: Exclusion for taxpayers failing to meet certain requirements) |
| (c)(1) | 52-53 | In general | encoded | s121-c-reduced: s 121(c)(1) the ownership and use requirements; s121-c-reduced: s 121(c)(1) the dollar limitation | s121-tests-c, s121-tests-whole, s121-cases-seat |  |
| (c)(1)(A) | 54 | the amount which bears the same ratio to such limitation (de... | fork | s121-c-reduced: s 121(c)(1) the dollar limitation as reduced | s121-tests-c, s121-tests-whole, s121-cases-seat | F9 |
| (c)(1)(B) | 55 |  | encoded | s121-c-reduced: s 121(c)(1)(B)(i) the shorter; s121-c-reduced: s 121(c)(1)(B)(ii) | s121-tests-c, s121-tests-whole |  |
| (c)(1)(B)(i) | 56 | the shorter of— | fork | s121-c-reduced: s 121(c)(1)(B)(i) the shorter | s121-tests-c, s121-tests-whole | F11 |
| (c)(1)(B)(i)(I) | 57 | the aggregate periods, during the 5-year period ending on th... | fork | s121-c-reduced: s 121(c)(1)(B)(i)(I) | s121-tests-c, s121-tests-whole | F1 |
| (c)(1)(B)(i)(II) | 58 | the period after the date of the most recent prior sale or e... | fork | s121-c-reduced: s 121(c)(1)(B)(i)(II) | s121-tests-c, s121-tests-whole, s121-cases-seat | F25 |
| (c)(1)(B)(ii) | 59 | 2 years. | fork | s121-c-reduced: s 121(c)(1)(B)(ii) | s121-tests-c, s121-tests-whole | F6 |
| (c)(2) | 60-61 | Sales and exchanges to which subsection applies | encoded | s121-c-reduced: s 121(c)(2) this subsection applies | s121-tests-c, s121-tests-whole, s121-cases-seat |  |
| (c)(2)(A) | 62 | subsection (a) would not (but for this subsection) apply to ... | encoded | s121-c-reduced: s 121(c)(2)(A) subsection (a) | s121-tests-c, s121-tests-whole |  |
| (c)(2)(A)(i) | 63 | a failure to meet the ownership and use requirements of subs... | encoded | s121-c-reduced: s 121(c)(2)(A)(i) | s121-tests-c, s121-tests-whole |  |
| (c)(2)(A)(ii) | 64 | subsection (b)(3), and | encoded | s121-c-reduced: s 121(c)(2)(A)(ii) | s121-tests-c, s121-tests-whole |  |
| (c)(2)(B) | 65 | such sale or exchange is by reason of a change in place of e... | encoded | s121-c-reduced: s 121(c)(2)(B) | s121-tests-c, s121-tests-whole, s121-cases-seat |  |
| (d) | 66 | Special rules | inert | none | none | 1: not operative (heading: Special rules) |
| (d)(1) | 67-68 | Joint returns | fork | s121-d1-special: s 121(d)(1); s121-whole: s 121 the treatment of the gain | s121-tests-d1, s121-tests-whole | F12 |
| (d)(2) | 69-70 | Property of deceased spouse | fork | s121-d1-special: s 121(d)(2); s121-whole: s 121(d) the individual's holding | s121-tests-d1, s121-tests-whole, s121-cases-seat | F24 |
| (d)(3) | 71-72 | Property owned by spouse or former spouse | encoded | s121-whole: s 121(d) the individual's holding | s121-tests-whole |  |
| (d)(3)(A) | 73-74 | Property transferred to individual from spouse or former spo... | encoded | s121-d1-special: s 121(d)(3)(A) | s121-tests-d1, s121-tests-whole |  |
| (d)(3)(B) | 75-76 | Property used by former spouse pursuant to divorce decree, e... | encoded | s121-d1-special: s 121(d)(3)(B) | s121-tests-d1, s121-tests-whole, s121-cases-seat |  |
| (d)(3)(C) | 77-78 | Divorce or separation instrument | encoded | s121-d1-special: s 121(d)(3)(C) the instrument is a divorce | s121-tests-d1, s121-cases-seat |  |
| (d)(3)(C)(i) | 79 | a decree of divorce or separate maintenance or a written ins... | encoded | s121-d1-special: s 121(d)(3)(C)(i) | s121-tests-d1 |  |
| (d)(3)(C)(ii) | 80 | a written separation agreement, or | encoded | s121-d1-special: s 121(d)(3)(C)(ii) | s121-tests-d1 |  |
| (d)(3)(C)(iii) | 81 | a decree (not described in clause (i)) requiring a spouse to... | encoded | s121-d1-special: s 121(d)(3)(C)(iii) | s121-tests-d1 |  |
| (d)(4) | 82-83 | Tenant-stockholder in cooperative housing corporation | encoded | s121-whole: s 121(d) the individual's holding | s121-tests-whole |  |
| (d)(4)(A) | 84 | the holding requirements of subsection (a) shall be applied ... | encoded | s121-d1-special: s 121(d)(4)(A) | s121-tests-d1 |  |
| (d)(4)(B) | 85 | the use requirements of subsection (a) shall be applied to t... | encoded | s121-d1-special: s 121(d)(4)(B) | s121-tests-d1 |  |
| (d)(5) | 86 | Involuntary conversions | inert | none | none | 1: not operative (heading: Involuntary conversions) |
| (d)(5)(A) | 87-88 | In general | encoded | s121-d1-special: s 121(d)(5)(A); s121-whole: s 121(d)(5)(A) | s121-tests-d1, s121-tests-whole, s121-cases-seat |  |
| (d)(5)(B) | 89-90 | Application of section 1033 | encoded | s121-d1-special: s 121(d)(5)(B) | s121-tests-d1, s121-cases-seat |  |
| (d)(5)(C) | 91-92 | Property acquired after involuntary conversion | encoded | s121-d1-special: s 121(d)(5)(C) | s121-tests-d1 |  |
| (d)(6) | 93-94 | Recognition of gain attributable to depreciation | fork | s121-d1-special: s 121(d)(6); s121-whole: s 121 the treatment of the gain | s121-tests-d1, s121-tests-whole, s121-cases-seat | F20 |
| (d)(7) | 95-96 | Determination of use during periods of out-of-residence care | fork | s121-d1-special: s 121(d)(7) | s121-tests-d1, s121-tests-whole, s121-cases-seat | F21 |
| (d)(7)(A) | 97 | becomes physically or mentally incapable of self-care, and | encoded | s121-d1-special: s 121(d)(7) | s121-tests-d1, s121-cases-seat |  |
| (d)(7)(B) | 98-99 | owns property and uses such property as the taxpayer’s princ... | fork | s121-d1-special: s 121(d)(7) | s121-tests-d1, s121-cases-seat | F21 |
| (d)(8) | 100-101 | Sales of remainder interests | encoded | s121-d1-special: s 121(d)(8)(A); s121-whole: s 121 whether the section reaches | s121-tests-d1, s121-tests-whole |  |
| (d)(8)(A) | 102-103 | In general | encoded | s121-d1-special: s 121(d)(8)(A) | s121-tests-d1, s121-tests-whole, s121-cases-seat |  |
| (d)(8)(B) | 104-105 | Exception for sales to related parties | encoded | s121-d1-special: s 121(d)(8)(B) | s121-tests-d1, s121-tests-whole, s121-cases-seat |  |
| (d)(9) | 106 | Uniformed services, Foreign Service, and intelligence commun... | inert | none | none | 1: not operative (heading: Uniformed services, Foreign Service, and intelligence community) |
| (d)(9)(A) | 107-108 | In general | fork | s121-d9-service: s 121(d)(9)(A) the service is qualified; s121-d9-service: s 121(d)(9)(A) the running | s121-tests-d9, s121-tests-whole, s121-cases-seat | F7, F19, F30 |
| (d)(9)(A)(i) | 109 | as a member of the uniformed services, | encoded | s121-d9-service: s 121(d)(9)(A) the service is qualified | s121-tests-d9, s121-cases-seat |  |
| (d)(9)(A)(ii) | 110 | as a member of the Foreign Service of the United States, or | encoded | s121-d9-service: s 121(d)(9)(A) the service is qualified | s121-tests-d9 |  |
| (d)(9)(A)(iii) | 111 | as an employee of the intelligence community. | encoded | s121-d9-service: s 121(d)(9)(A) the service is qualified | s121-tests-d9, s121-cases-seat |  |
| (d)(9)(B) | 112-113 | Maximum period of suspension | fork | s121-d9-service: s 121(d)(9)(B) | s121-tests-d9, s121-tests-whole, s121-cases-seat | F7 |
| (d)(9)(C) | 114-115 | Qualified official extended duty | encoded | s121-d9-service: s 121(d)(9)(C)(i) | s121-tests-d9 |  |
| (d)(9)(C)(i) | 116-117 | In general | encoded | s121-d9-service: s 121(d)(9)(C)(i) | s121-tests-d9, s121-cases-seat |  |
| (d)(9)(C)(ii) | 118-119 | Uniformed services | encoded | s121-d9-service: s 121(d)(9)(C)(ii) | s121-tests-d9 |  |
| (d)(9)(C)(iii) | 120-121 | Foreign Service of the United States | encoded | s121-d9-service: s 121(d)(9)(C)(iii) | s121-tests-d9 |  |
| (d)(9)(C)(iv) | 122-123 | Employee of intelligence community | encoded | s121-d9-service: s 121(d)(9)(C)(iv) the person is an employee | s121-tests-d9, s121-cases-seat |  |
| (d)(9)(C)(iv)(I) | 124 | the Office of the Director of National Intelligence, | encoded | s121-nouns: `Office of the intelligence community` constructor: the Office of t...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(II) | 125 | the Central Intelligence Agency, | encoded | s121-nouns: `Office of the intelligence community` constructor: the Central Int...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(III) | 126 | the National Security Agency, | encoded | s121-nouns: `Office of the intelligence community` constructor: the National Se...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(IV) | 127 | the Defense Intelligence Agency, | encoded | s121-nouns: `Office of the intelligence community` constructor: the Defense Int...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(V) | 128 | the National Geospatial-Intelligence Agency, | encoded | s121-nouns: `Office of the intelligence community` constructor: the National Ge...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(VI) | 129 | the National Reconnaissance Office, | encoded | s121-nouns: `Office of the intelligence community` constructor: the National Re...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(VII) | 130 | any other office within the Department of Defense for the co... | encoded | s121-nouns: `Office of the intelligence community` constructor: another office ...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(VIII) | 131 | any of the intelligence elements of the Army, the Navy, the ... | encoded | s121-nouns: `Office of the intelligence community` constructor: an intelligence...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(IX) | 132 | the Bureau of Intelligence and Research of the Department of... | encoded | s121-nouns: `Office of the intelligence community` constructor: the Bureau of I...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(iv)(X) | 133 | any of the elements of the Department of Homeland Security c... | encoded | s121-nouns: `Office of the intelligence community` constructor: an element of t...; s121-d9-service: s 121(d)(9)(C)(iv) the clause that names the office | s121-tests-d9 |  |
| (d)(9)(C)(v) | 134-135 | Extended duty | encoded | s121-d9-service: s 121(d)(9)(C)(v) | s121-tests-d9, s121-cases-seat |  |
| (d)(9)(D) | 136 | Special rules relating to election | inert | none | none | 1: not operative (heading: Special rules relating to election) |
| (d)(9)(D)(i) | 137-138 | Election limited to 1 property at a time | encoded | s121-d9-service: s 121(d)(9)(A) the running | s121-tests-d9, s121-tests-whole, s121-cases-seat |  |
| (d)(9)(D)(ii) | 139-140 | Revocation of election | fork | s121-d9-service: s 121(d)(9)(A) the running | s121-tests-d9, s121-tests-whole | F19 |
| (d)(10) | 141-142 | Property acquired in like-kind exchange | encoded | s121-d9-service: s 121(d)(10); s121-whole: s 121 whether the section reaches | s121-tests-d9, s121-tests-whole, s121-cases-seat |  |
| (d)(11) | 143 | Repealed. Pub. L. 111–312, title III, § 301(a), Dec. 17, 201... | repealed or blank in this text | none | none | the text shows `[(11) Repealed. Pub. L. 111-312, title III, s 301(a), Dec. 17, 2010, 124 Stat. 3300]` and nothing else |
| (d)(12) | 144 | Peace Corps | inert | none | none | 1: not operative (heading: Peace Corps) |
| (d)(12)(A) | 145-146 | In general | fork | s121-d9-service: s 121(d)(12)(A) | s121-tests-d9, s121-tests-whole, s121-cases-seat | F30 |
| (d)(12)(A)(i) | 147 | on qualified official extended duty (as defined in paragraph... | encoded | s121-d9-service: s 121(d)(12)(A) the service is serving | s121-tests-d9 |  |
| (d)(12)(A)(ii) | 148 | as an enrolled volunteer or volunteer leader under section 5... | encoded | s121-d9-service: s 121(d)(12)(A) the service is serving | s121-tests-d9, s121-cases-seat |  |
| (d)(12)(B) | 149-150 | Applicable rules | fork | s121-d9-service: s 121(d)(12)(B) | s121-tests-d9 | F8 |
| (e) | 151-152 | Denial of exclusion for expatriates | fork | s121-efg: s 121(e); s121-whole: s 121 whether the section reaches | s121-tests-c, s121-tests-whole, s121-cases-seat | F18 |
| (f) | 153-154 | Election to have section not apply | encoded | s121-efg: s 121(f); s121-whole: s 121 whether the section reaches | s121-tests-c, s121-tests-whole, s121-cases-seat |  |
| (g) | 155-156 | Residences acquired in rollovers under section 1034 | fork | s121-efg: s 121(g); s121-whole: s 121(g) the days added | s121-tests-c, s121-tests-whole, s121-cases-seat | F15 |
| source credit | 157 | (Added Pub. L. 88–272, title II, § 206(a), Feb. 26, 1964, 78... | inert | none | none | 1: not operative (the date of enactment and the amendments) |
| footnote | 158 | [^1] See References in Text note below. | inert | none | none | 1: not operative (a pointer to the OLRC's notes, which are context and get no rows) |
| term: divorce or separation instrument | 77-78 | (the defining or borrowing provision is row (d)(3)(C)) | encoded | s121-d1-special: s 121(d)(3)(C) the instrument is a divorce | s121-tests-d1 |  |
| term: qualified official extended duty | 116-117 | (the defining or borrowing provision is row (d)(9)(C)(i)) | encoded | s121-d9-service: s 121(d)(9)(C)(i) | s121-tests-d9 |  |
| term: uniformed services | 118-119 | (the defining or borrowing provision is row (d)(9)(C)(ii)) | encoded | s121-d9-service: s 121(d)(9)(C)(ii) | s121-tests-d9 |  |
| term: member of the Foreign Service of the United States | 120-121 | (the defining or borrowing provision is row (d)(9)(C)(iii)) | encoded | s121-d9-service: s 121(d)(9)(C)(iii) | s121-tests-d9 |  |
| term: employee of the intelligence community | 122-123 | (the defining or borrowing provision is row (d)(9)(C)(iv)) | encoded | s121-d9-service: s 121(d)(9)(C)(iv) the person is an employee | s121-tests-d9 |  |
| term: extended duty | 134-135 | (the defining or borrowing provision is row (d)(9)(C)(v)) | encoded | s121-d9-service: s 121(d)(9)(C)(v) | s121-tests-d9 |  |
| term: period of nonqualified use | 40-41 | (the defining or borrowing provision is row (b)(5)(C)(i)) | fork | s121-b-limitations: s 121(b)(5)(C)(i) | s121-tests-b | F22 |
| term: 5-year period described in subsection (a) | 13-14 | (the defining or borrowing provision is row (a)) | encoded | s121-a-exclusion: s 121(a) the 5-year period | s121-tests-a |  |
| term: tenant-stockholder, cooperative housing corporation (section 216) | 82-83 | (the defining or borrowing provision is row (d)(4)) | encoded | s121-d1-special: s 121(d)(4)(A) | s121-tests-d1 | borrowed term, asked as a fact |
| term: depreciation adjustments (section 1250(b)(3)) | 93-94 | (the defining or borrowing provision is row (d)(6)) | encoded | s121-d1-special: s 121(d)(6) | s121-tests-d1 | borrowed term, asked as a fact |
| term: divorce or separation instrument kinds (section 1041(a) transfer) | 73-74 | (the defining or borrowing provision is row (d)(3)(A)) | encoded | s121-d1-special: s 121(d)(3)(A) | s121-tests-d1 | borrowed term, asked as a fact |

The table has no `out-of-scope` row and no `deferred` row.

Every `inert` row is reason 1 (a heading, the title, the converter's header, the source credit, the footnote); none is reason 2 or 3, and the one repealed paragraph, (d)(11), is a `repealed or blank in this text` row.

The brief's earlier passes moved no row: this is the first encoding of this section, so no row was moved out of `inert`.

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes.

Each entry names the provision, the readings, the one taken, the text that licenses each, and the rule that encodes the one taken.

The numbers F1 to F30 are cited by the comments in the `.l4` files.

### F1: (a) and (c)(1)(B)(i)(I): "owned and used"

Readings: (i) two requirements: 2 years of ownership, and 2 years of use as the principal residence, each aggregated in the 5-year period, not necessarily at the same time; (ii) one requirement: 2 years of days that are both owned and used.
Taken: (i) for (a); (ii) for (c)(1)(B)(i)(I), which needs one number.
Text: (a), line 14: "has been owned and used by the taxpayer as the taxpayer's principal residence for periods aggregating 2 years or more"; (b)(2)(A)(i) and (ii), lines 22-23, and (d)(4)(A) and (B), lines 84-85, speak of "the ownership requirements", "the use requirements", "the holding requirements" separately; (c)(1)(B)(i)(I), line 57, speaks of one aggregate period "during which the property has been owned and used".
Rule: s121-a-exclusion: s 121(a) the ownership requirement is met, the use requirement is met; s121-c-reduced: s 121(c)(1)(B)(i)(I). The outcomes differ for someone who lived in the home as a tenant for 2 years and then bought it and let it out: (i) met, (ii) not met.

### F2: (a): the 5-year period

Readings: (i) the 5 calendar years ending on the sale date, beginning the day after the date 5 years earlier; (ii) beginning on that earlier date, one day longer.
Taken: (i).
Text: line 14: "during the 5-year period ending on the date of the sale or exchange".
Rule: s121-a-exclusion: s 121(a) the 5-year period ending on the date of the sale or exchange; s121-support: the span of the years ending on.

### F3: (a): stretches that overlap

Readings: (i) a day owned or used counts once however many stretches cover it; (ii) the lengths of the stretches are added.
Taken: (i).
Text: line 14: "periods aggregating 2 years or more" (an aggregate of periods of time).
Rule: s121-support: the spans with no day counted twice, applied in s121-whole to every list before it is counted.

### F4: (a), (b)(3), (b)(4), (c)(1)(B)(ii): "2 years" as an amount of time

Readings: (i) the days in the 2 calendar years ending on the date of the sale (730, or 731 when a 29 February falls in them); (ii) a flat 730 days; (iii) 24 months added up from stays measured in months.
Taken: (i). The text contains no "24 months" (finding 1).
Text: line 14: "periods aggregating 2 years or more"; line 59: "(ii) 2 years."
Rule: s121-a-exclusion: s 121(a) 2 years, counted in days, ending on the date of the sale or exchange; s121-c-reduced: s 121(c)(1)(B)(ii).

### F5: every span of time: both ends, and impossible dates

Readings: (i) a stay includes its first day and its last day, and the day of the sale counts as a day owned and lived in if the stay includes it; (ii) the last day is not counted. For "2 years after the date of death", a death on 29 February: (i) the date rolls forward (1 March of the year 2 years later); (ii) it stops at 28 February.
Taken: (i), and the roll forward that `Date` gives.
Text: the text counts "periods" and "the 5-year period ending on the date" without saying whether the end day counts; it says "not later than 2 years after the date of death" (line 30).
Rule: s121-nouns: Span; s121-support; s121-b-limitations: s 121(b)(4) paragraph (1) is applied...; tests in s121-tests-b (death on 29 February 2024).

### F6: every other length of N years

Readings: (i) the days in the N calendar years ending on the date (the 1 year of (d)(7)(B), the 10 and 2 years of (b)(5)(C)(ii), the 5 and 10 years of (d)(9)(B), and a 15-year lookback that is the 5 years plus the 10 the extension may add); (ii) a flat 365 x N days.
Taken: (i).
Text: lines 98-99, 45, 46, 113: "at least 1 year", "not to exceed an aggregate period of 10 years", "2 years", "shall not be extended more than 10 years".
Rule: s121-support: the days in the years ending on; used by each rule that measures N years.

### F7: (d)(9)(B): the extension of the 5-year period

Readings: (i) walk back from the sale date counting only the days not suspended until 5 years' worth is reached, never going back more than 15 years from the sale; (ii) move the ordinary period back by the days of service inside it (no second round), up to 10 years.
Taken: (i).
Text: line 108: "the running of the 5-year period ... shall be suspended during any period"; line 113: "shall not be extended more than 10 years by reason of subparagraph (A)".
Rule: s121-d9-service: s 121(d)(9)(B) the 5-year period as extended, by no more than 10 years.

### F8: (d)(12)(B): "rules similar to the rules of subparagraphs (B) and (D) of paragraph (9)"

Readings: (i) the same functions as (d)(9)(B) and (d)(9)(D); (ii) similar rules left for the reader to state.
Taken: (i).
Text: lines 149-150.
Rule: s121-d9-service: s 121(d)(12)(B) the 5-year period as extended by rules similar to (d)(9)(B); s 121(d)(12)(A) the running of the 5-year period is suspended at the individual's election.

### F9: (b)(5)(B) and (c)(1)(A): rounding and order of arithmetic

Readings: (i) the ratio and the product computed as written, with no rounding step; (ii) the ratio rounded to some number of places, or the result rounded to the dollar.
Taken: (i); the text names no rounding.
Text: lines 34-37 "based on the ratio which"; line 54 "the amount which bears the same ratio to such limitation".
Rule: s121-b-limitations: s 121(b)(5)(B), s 121(b)(5)(A); s121-c-reduced: s 121(c)(1) the dollar limitation as reduced. The gain is multiplied by the ratio; the limitation is multiplied by the ratio.

### F10: (b)(5)(C)(ii)(II) and (III): the caps

Readings: (i) a cap in days (the days in the 10, or 2, calendar years ending on the sale), applied to the days of such duty or absence that lie in the nonqualified use left after exception (I), with (III) applied to what remains after the days of (II); (ii) caps in years or months; (iii) caps over the whole ownership instead.
Taken: (i).
Text: lines 45-46: "not to exceed an aggregate period of 10 years", "any other period of temporary absence (not to exceed an aggregate period of 2 years)".
Rule: s121-b-limitations: s 121(b)(5)(C)(ii)(II), s 121(b)(5)(C)(ii)(III), s 121(b)(5)(C) the aggregate days.

### F11: (c)(1)(B)(i) when there is no earlier sale

Readings: (i) the shorter of (I) and (II) is (I) alone; (ii) the answer is not covered; (iii) (II) is unbounded.
Taken: (i).
Text: lines 56-58: "the shorter of— (I) ... (II) the period after the date of the most recent prior sale or exchange by the taxpayer to which subsection (a) applied".
Rule: s121-c-reduced: s 121(c)(1)(B)(i) the shorter of (I) and (II) (a lawyer's call: the text does not say what the shorter of one period is).

### F12: (d)(1): not a joint return

Readings: (i) outside the provision's scope, not covered (NOTHING); (ii) the answer is no (JUST FALSE).
Taken: (i).
Text: line 68: "If a husband and wife make a joint return for the taxable year of the sale or exchange of the property, then subsections (a) and (c) shall apply if either spouse satisfies the requirements".
Rule: s121-d1-special: s 121(d)(1).

### F13: (b)(2)(B): a spouse who would not be entitled

Readings: (i) the limitation is 0 (JUST 0); (ii) not covered (NOTHING).
Taken: (i). An "entitled"-named function: the ruling of 2026-11-12 asks that it be listed here for the maintainer or a lawyer.
Text: lines 25-26: "the sum of the limitations under paragraph (1) to which each spouse would be entitled if such spouses had not been married".
Rule: s121-b-limitations: s 121(b)(2)(B) the limitation under paragraph (1) to which the spouse would be entitled if the spouses had not been married.

### F14: (b)(4): "immediately before such date of death"

Readings: (i) as at the day before the date of death, each spouse on their own periods, the 5-year and 2-year periods ending that day; (ii) as at the date of death; (iii) the two spouses' periods pooled.
Taken: (i).
Text: line 30: "the requirements of paragraph (2)(A) were met immediately before such date of death".
Rule: s121-b-limitations: s 121(b)(4) the requirements of paragraph (2)(A) were met immediately before the date of death.

### F15: (g): earlier residences

Readings: (i) the caller states the days the earlier residences were owned and used, and they are added to the days in the 5-year period for both requirements; (ii) the earlier periods are placed on the calendar and only those inside the 5-year period count.
Taken: (i).
Text: line 156: "the taxpayer shall be treated as having owned and used such property for the periods during which he owned and used such other residence" (as the text reads; section 1034 is repealed and not among the sources).
Rule: s121-efg: s 121(g); s121-whole: s 121(g) the days added for the individual.

### F16: joint return: whose ownership and use fixes the (b)(5) ratio

Readings: (i) the ownership and use of both spouses together (the union); (ii) the first spouse's only.
Taken: (i), as (b)(2)(B)'s second sentence treats each spouse as owning when either owned.
Text: line 26: "each spouse shall be treated as owning the property during the period that either spouse owned the property"; lines 36-37 "the period such property was owned by the taxpayer".
Rule: s121-whole: s 121 the treatment of the gain from the sale or exchange; s 121(b)(2)(B) the individual meets the ownership requirement, treated as owning the property when either spouse owned it.

### F17: joint return and the reduced exclusion of (c)

Readings: (i) not covered (NOTHING) where the reason holds, JUST 0 where it does not; (ii) the better spouse's shorter period; (iii) the sum; (iv) the first spouse's.
Taken: (i).
Text: line 68 makes (c) apply to a joint return "if either spouse satisfies the requirements"; lines 56-58 measure periods of "the taxpayer" ("the shorter of").
Rule: s121-whole: s 121 the treatment of the gain from the sale or exchange (route C). A joint return that meets (a) through (d)(1) while both spouses are barred by (b)(3), and so might use (c), is not modelled: the answer under (a) is given.

### F18: (e) on a joint return: the spouse is an individual to whom section 877(a)(1) applies

Readings: (i) not covered (NOTHING); (ii) the section does not apply to the joint return; (iii) the section applies to the other spouse's share.
Taken: (i).
Text: line 152: "This section shall not apply to any sale or exchange by an individual if the treatment provided by section 877(a)(1) applies to such individual."
Rule: s121-whole: s 121 whether the section reaches the sale or exchange.

### F19: (d)(9)(D)(ii): a revoked election

Readings: (i) a revoked election suspends nothing, and the 5-year period is the one (a) gives; (ii) days already suspended stay suspended.
Taken: (i); the election function answers NOTHING for both "not elected" and "revoked".
Text: line 140: "An election under subparagraph (A) may be revoked at any time."
Rule: s121-d9-service: s 121(d)(9)(A) the running of the 5-year period is suspended at the individual's election.

### F20: (d)(6): a depreciation adjustment attributable to a period that straddles May 6, 1997

Readings: (i) not covered (NOTHING); (ii) divided pro rata by days; (iii) counted whole; (iv) not counted.
Taken: (i).
Text: line 94: "the portion of the depreciation adjustments ... attributable to periods after May 6, 1997".
Rule: s121-d1-special: s 121(d)(6) the gain to which subsection (a) shall not apply.

### F21: (d)(7): "periods aggregating at least 1 year"

Readings: (i) the days both owned and used inside the 5-year period are at least the days of the 1 calendar year ending on the sale (365 or 366); (ii) 12 months; (iii) a flat 365 days.
Taken: (i).
Text: lines 98-99: "owns property and uses such property as the taxpayer's principal residence during the 5-year period described in subsection (a) for periods aggregating at least 1 year".
Rule: s121-d1-special: s 121(d)(7).

### F22: (b)(5)(C)(i): "other than the portion of any period preceding January 1, 2009"

Readings: (i) 1 January 2009 itself counts as nonqualified use if not used as the home; (ii) counting starts on 2 January 2009.
Taken: (i), since 1 January 2009 is not a day "preceding" January 1, 2009.
Text: line 41.
Rule: s121-b-limitations: s 121(b)(5)(C)(i) the periods of nonqualified use (asserted in s121-cases-seat: the 2 January 2009 case).

### F23: (b)(5)(C)(ii)(I): never used as the principal residence

Readings: (i) there is no "last date", so no part of the 5-year period is excepted; (ii) the whole 5-year period is excepted.
Taken: (i).
Text: line 44: "any portion of the 5-year period ... which is after the last date that such property is used as the principal residence".
Rule: s121-b-limitations: s 121(b)(5)(C)(ii)(I).

### F24: (d)(2): "before death"

Readings: (i) through the day before the date of death; (ii) through the date of death.
Taken: (i).
Text: line 70: "the period such deceased spouse owned and used such property before death".
Rule: s121-d1-special: s 121(d)(2) ...

### F25: (c)(1)(B)(i)(II): "the period after the date of the most recent prior sale or exchange ... and before the date of such sale"

Readings: (i) the days strictly between the two dates; (ii) including one or both end dates.
Taken: (i).
Text: line 58.
Rule: s121-c-reduced: s 121(c)(1)(B)(i)(II).

### F26: (b)(3): the 2-year period

Readings: (i) the period includes the date of this sale and the first day after the date 2 years earlier, so another sale on either day bars; (ii) either end excluded.
Taken: (i).
Text: line 28: "during the 2-year period ending on the date of such sale or exchange, there was any other sale or exchange by the taxpayer to which subsection (a) applied".
Rule: s121-b-limitations: s 121(b)(3) (asserted at both ends in s121-tests-b and s121-cases-seat).

### F27: (b)(2)(A)(iii): whose earlier sales

Readings: (i) each spouse's own earlier sales bar that spouse; (ii) either spouse's earlier sale bars both.
Taken: (i).
Text: line 24: "neither spouse is ineligible for the benefits of subsection (a) with respect to such property by reason of paragraph (3)".
Rule: s121-whole: s 121(b) the limitation before any reduction under (c)(1); s121-b-limitations: s 121(b)(2)(A)(iii).

### F28: (b)(5)(C)(ii)(I): "the 5-year period described in subsection (a)"

Readings: (i) the taxpayer's own 5-year period, as extended by an election under (d)(9) or (d)(12) that holds; (ii) always the ordinary 5 years.
Taken: (i).
Text: line 44; and line 113, which extends "The 5-year period described in subsection (a)".
Rule: s121-whole: s 121 the treatment of the gain from the sale or exchange (taxpayerWindow).

### F29: (b)(3) and (c)(1)(B)(i)(II): "any other sale or exchange ... to which subsection (a) applied"

Readings: (i) the person states which earlier sales count, and the seat asks "did you sell another home earlier and leave its gain out of your gross income under this section?"; (ii) a sale that received a reduced exclusion under (c) counts; (iii) it does not.
Taken: (i): the judgment is the person's.
Text: lines 28 and 58.
Rule: s121-seat: the inputs on earlier sales.

### F30: (d)(9)(A), (d)(12)(A) and (b)(5)(C)(ii)(II): "such individual's spouse" is serving

Readings: (i) the service of the individual's spouse, as the person states it, suspends the electing individual's 5-year period and is exempt from nonqualified use under (b)(5)(C)(ii)(II), on any return, joint or not, the person stating only service during which the spouse was the individual's spouse; (ii) only on a joint return; (iii) only the service of the spouse the individual has on the date of the sale, never a former spouse's; (iv) the individual's own service alone.
Taken: (i). The election is the electing individual's own: a spouse's election suspends the individual's period only if the individual elects.
Stakes, from scenario 21 of `s121-tests-whole.l4` (a sale on 15 March 2026 on a return that is not joint, a gain of 5,918 chosen to equal the days owned, the spouse's service 1 January 2014 to 31 December 2022): under reading (i) the amount excluded is 4,822; under reading (ii), which looks to a joint return only, or reading (iv), which counts the individual's own service alone, it is 1,535.
The difference is whether 3,287 days of the spouse's service come out of the nonqualified days (4,383 down to 1,096).
Text: line 108: "during any period that such individual or such individual's spouse is serving on qualified official extended duty"; line 146 says the same for the Peace Corps ("serving outside the United States"); line 45: "the taxpayer or the taxpayer's spouse is serving on qualified official extended duty". None of them says "on a joint return".
Rule: s121-whole: s 121(a), (d)(9) and (d)(12) the period for the individual, as extended by an election that holds (its `partner` is the individual's spouse; the days of service of both are passed to (d)(9)(B)), and `dutyDays` in s 121 the treatment of the gain from the sale or exchange. A former spouse's service is not asked: the person states service during the marriage only.

### The rulings the `NOTHING`-kind tags follow, recorded word for word

These are copied by script from the brief (`BRIEF.md`, lines 115 to 124); each row that carries `NOTHING-kind` tags records them here.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.
- **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits:
  1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed;
  2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question;
  3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).
  The ruling and the counts it produced are recorded in `subjects/uk/companies-act-2006/encodings/legalese-sonnet-5.5/NOTES.md`, section "The grant and power name test".

## Marginal readings for a lawyer

The rule of 2026-10-29 leaves two readings for a lawyer: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not count as the text saying no.

This encoding takes both as the status quo.

Below, every branch that rests on reading (a) is listed with the other reading (the branch would be `NOTHING`), and every `NOTHING-kind (limited by its own wording)` branch is listed with the other reading (the branch would be `JUST FALSE`).

The list is made by a script that reads the tags in the `.l4` files.

### Branches that rest on reading (a): `JUST FALSE` for a failed "if" or a fixed period; the other reading answers `NOTHING`

| module:line | rule |
| --- | --- |
| s121-a-exclusion:43 | s 121(a) the ownership requirement is met |
| s121-a-exclusion:58 | s 121(a) the use requirement is met |
| s121-d9-service:216 | s 121(d)(10) subsection (a) shall not apply to the sale of property acquired in a like-kind exchange |
| s121-d9-service:239 | s 121(d)(12)(A) the service is serving outside the United States as described in clause (i) or (ii) |
| s121-d9-service:245 | s 121(d)(12)(A) the service is serving outside the United States as described in clause (i) or (ii) |
| s121-b-limitations:70 | s 121(b)(2)(A) paragraph (1) is applied by substituting $500,000 for $250,000 |
| s121-b-limitations:99 | s 121(b)(2)(B) the limitation under paragraph (1) to which the spouse would be entitled if the spouses had not been married |
| s121-b-limitations:138 | s 121(b)(3) subsection (a) shall not apply because of another sale or exchange within 2 years |
| s121-b-limitations:153 | s 121(b)(4) paragraph (1) is applied by substituting $500,000 for $250,000 |
| s121-c-reduced:49 | s 121(c)(2)(B) the sale is by reason of a change in place of employment, health, or unforeseen circumstances |
| s121-whole:552 | s 121 the treatment of the gain from the sale or exchange |
| s121-whole:604 | s 121 the treatment of the gain from the sale or exchange |

### Branches that rest on reading (b): `NOTHING` for a case outside a limit in the text's own wording; the other reading answers `JUST FALSE`

| module:line | rule |
| --- | --- |
| s121-d9-service:135 | s 121(d)(9)(A) the service is qualified official extended duty described in clause (i), (ii) or (iii) |
| s121-d9-service:152 | s 121(d)(9)(A) the running of the 5-year period is suspended at the individual's election |
| s121-d9-service:210 | s 121(d)(10) subsection (a) shall not apply to the sale of property acquired in a like-kind exchange |
| s121-d9-service:213 | s 121(d)(10) subsection (a) shall not apply to the sale of property acquired in a like-kind exchange |
| s121-d9-service:247 | s 121(d)(12)(A) the service is serving outside the United States as described in clause (i) or (ii) |
| s121-d1-special:23 | s 121(d)(1) subsections (a) and (c) apply to the joint return |
| s121-d1-special:38 | s 121(d)(2) the periods the deceased spouse owned the property before death are included |
| s121-d1-special:51 | s 121(d)(2) the periods the deceased spouse used the property before death are included |
| s121-d1-special:65 | s 121(d)(3)(A) the period the transferor owned the property is included |
| s121-d1-special:116 | s 121(d)(3)(B) the individual is treated as using the property as the principal residence while a spouse or former spouse is granted use |
| s121-d1-special:133 | s 121(d)(4)(A) the holding requirement is applied to the holding of the stock |
| s121-d1-special:146 | s 121(d)(4)(B) the use requirement is applied to the house or apartment the taxpayer was entitled to occupy |
| s121-d1-special:186 | s 121(d)(5)(C) the holding and use of the converted property are treated as holding and use of the property sold |
| s121-d1-special:230 | s 121(d)(7) the taxpayer is treated as using the property as the principal residence while residing in a licensed facility |
| s121-d1-special:249 | s 121(d)(8)(A) this section does not fail to apply to the sale of the interest by reason of its being a remainder interest |
| s121-b-limitations:72 | s 121(b)(2)(A) paragraph (1) is applied by substituting $500,000 for $250,000 |
| s121-b-limitations:84 | s 121(b)(2)(A) the limitation under paragraph (1) as substituted |
| s121-b-limitations:115 | s 121(b)(2)(B) the limitation for other joint returns |
| s121-b-limitations:124 | s 121(b)(2)(B) the limitation for other joint returns |
| s121-b-limitations:155 | s 121(b)(4) paragraph (1) is applied by substituting $500,000 for $250,000 |
| s121-c-reduced:138 | s 121(c)(1) the ownership and use requirements of subsection (a), and subsection (b)(3), shall not apply to the sale |
| s121-efg:21 | s 121(e) this section applies to the sale or exchange by the individual |
| s121-efg:35 | s 121(f) this section applies to the sale or exchange |
| s121-efg:50 | s 121(g) the days the other residence was owned and used are included |
| s121-whole:357 | s 121(g) the days added for the individual |

Branches that answer `JUST FALSE` because the text itself says no (a "means" definition: `s 121(d)(9)(C)(v)`, `s 121(d)(9)(C)(i)`, `s 121(d)(9)(C)(iv)`, `s 121(d)(3)(C)`; a flat negative: `s 121(e)`, `s 121(f)`, `s 121(d)(8)(B)`, the second limb of `s 121(d)(8)(A)`, and `s 121(d)(9)(A)` where another election is in effect) are not marginal.

The three-valued answers also appear in the seat layer: `Does section 121 reach my sale at all` maps layer 1's constructors to `JUST TRUE`, `JUST FALSE` and `NOTHING` and adds no judgment of its own.

### Reading a result: FALSE and NOTHING

In this row a "no" is an answer of `JUST FALSE` (or, in `s121-whole.l4`, the constructor `Section 121 does not apply because`, or the amount `JUST 0` with the reason listed by `s 121 what stops or reduces the exclusion`).

It means the text itself says no to the case in its own words: a "means" definition; a condition introduced by "if" that fails; a period the text fixes, outside it; a flat negative ("shall not apply", "may not be made").

A "not covered" answer is `NOTHING` (or the constructor `Not covered because`).

It means the text lists without closing the list (an event other than the five of (d)(5)(A)), leaves a term undefined (a loss is not "gain"), is silent (a remainder interest sold without the election of (d)(8)(A); a depreciation adjustment that straddles May 6, 1997), points outside the sources (section 1031, the regulations), or limits a grant in its own wording (the suspension of (d)(9)(A) is given "at the election of an individual", and with no election the text says nothing) and the case falls outside the limit.

A caller must never turn `NOTHING` into `FALSE`: for the taxpayer, "not covered" is not "you owe tax" and not "you are excused"; it says the text does not answer.

One place a `NOTHING` is read as the base rule: `s 121(a), (d)(9) and (d)(12) the period for the individual, as extended by an election that holds` uses the ordinary 5 years of (a) when the election function says `NOTHING` or `JUST FALSE`, because (a) itself gives the ordinary period; that is a fallback to the general rule, not a no.

## Seat polarity (independent reader)

An independent reader checked the wording of every seat question against the value it returns.

One question was worded as a yes/no and returned days: the question on (d)(3) read "While my spouse or former spouse is granted the use of the home under our divorce or separation, do I count as living in it (s 121(d)(3))?" and returns a number of days (`MAYBE NUMBER`).

It now reads "For how many days while my spouse or former spouse is granted the use of the home under our divorce or separation do I count as living in it (s 121(d)(3))?"; the value it returns, its inputs, its function name (`For how many days do I count as living in my home while my former spouse has the use`) and every other question are unchanged.

The cases cite the function name, not the wording of the question, so none needed to change.

The other 19 questions were re-read against their types after the report: each yes/no question returns a `MAYBE BOOLEAN`, each "how much" or "how many days" question a `MAYBE NUMBER` (or `NUMBER`), the question on the 5-year period a `DATE`, and the question on what stops or reduces the exclusion a list of strings.

No companion yes/no question is added.

The text speaks of the days "during any period of ownership while such individual's spouse or former spouse is granted use" under an instrument, and where there is none the answer is `NOTHING` (limited by its own wording, marginal reading (b)), so a yes/no companion could only answer `JUST TRUE` or `NOTHING`; it would not answer "no, not under (d)(3)", which the text does not say, and it would add nothing the days do not show (more than 0 days is a yes).

A person who wants the honest "no" has none to be given under this convention; the other reading, `JUST FALSE`, is listed with the marginal readings of reading (b), above.

## Findings: what the text turns out to say

1. The brief lists "24 months" among the figures the text states; the text has none. Subsection (a) says "periods aggregating 2 years or more" and (b)(3) and (c)(1)(B)(ii) say "2 years". `grep -i "24 month"` over `usc26-s121.txt` finds nothing. The 2 years are measured in days (forks F4, F6). Asserted: the 730-day boundary (`s121-cases-seat.l4`, 16 March 2024 against 17 March 2024).
2. Subsection (a) says "owned and used", but (b)(2)(A)(i) and (ii) and (d)(4)(A) and (B) treat the ownership and use requirements separately, while (c)(1)(B)(i)(I) needs one aggregate of days that are both (fork F1). Asserted (`s121-tests-a.l4`; `s121-tests-c.l4`).
3. Subsection (d)(1) lets a joint return use (a) if either spouse meets the requirements, but the $500,000 of (b)(2)(A) needs both spouses to meet the use requirements: a couple of whom only one lived in the home may leave out some gain, but only up to $250,000. Asserted (`s121-cases-seat.l4`, the spouse who never lived there).
4. Under (b)(2)(B), each spouse is treated as owning the home when either did, but use is not shared: a spouse who never lived in it has a limitation of $0 in the sum. Asserted.
5. The $500,000 of (b)(4) lasts to the day two years after the death and no longer: for a death on 1 March 2025 the last day is 1 March 2027. Asserted (`s121-cases-seat.l4`, 1 March 2027 against 2 March 2027).
6. (b)(4) also needs the requirements of (b)(2)(A) to have been met immediately before the death, including (iii): an earlier sale by either spouse within the 2 years before the death bars. Asserted.
7. (b)(5)(D) makes (d)(6) apply before (b)(5): on a gain of 200,000 with 40,000 of depreciation and half the time not lived in, 80,000 is excluded, not 60,000. Asserted (`s121-tests-whole.l4`; `s121-cases-seat.l4`).
8. (c)(2)(A)(ii) lets the reduced exclusion rescue a sale barred by (b)(3), and (c)(1) switches (b)(3) off for it. Asserted.
9. A boundary the text states in words: an extended duty is a call "in excess of 90 days", so 90 days is not extended duty and 91 is. Asserted.
10. A boundary the text states in words: a duty station "at least 50 miles" from the property, so 50 miles qualifies and 49 does not. Asserted.
11. (d)(10)'s "5-year period beginning with the date of such acquisition" ends the day before the fifth anniversary: for a home acquired on 1 June 2020, a sale on 31 May 2025 is barred and a sale on 1 June 2025 is not. Asserted.
12. (d)(9)(A) lists three capacities, and the Peace Corps has its own paragraph, (d)(12), with the same suspension: a Peace Corps employee needs qualified official extended duty, a volunteer or volunteer leader needs only service outside the United States. Asserted.
13. (e) and (f) are flat negatives ("shall not apply"): the answer is `JUST 0` excluded, not `NOTHING`. Asserted.
14. A remainder interest sold without the election of (d)(8)(A), or to a related person (when (d)(8)(B) takes the election away), is not said to fall outside the section: the answer is not covered. Asserted.
15. The section speaks only of "gain": a loss is not addressed, and the answer is not covered. Asserted.
16. Paragraph (d)(11) is repealed; the text shows `[(11) Repealed. Pub. L. 111-312, title III, s 301(a), Dec. 17, 2010, 124 Stat. 3300]` and nothing else. It has a `repealed or blank in this text` row and no rule.
17. Subsection (g) refers to section 1034, which is repealed and not among the sources: it is encoded as a number of days the person states (fork F15). Asserted.
18. "Unforeseen circumstances" appears in (b)(5)(C)(ii)(III) (as the Secretary specifies) and in (c)(2)(B) (to the extent provided in regulations): both are inputs, and the seat's `@desc` says so. Asserted (the reduced exclusion on the unforeseen-circumstances input).
19. A depreciation adjustment attributable to a period that straddles May 6, 1997 has no rule in the text for how to divide it (fork F20): not covered. Asserted.
20. January 1, 2009 is not "preceding" January 1, 2009: a day not used as the home on that date is nonqualified use (fork F22). Asserted (`s121-cases-seat.l4`, 957,100 of gain, 1 day of 9,571 owned).
21. (d)(9)(A) and (d)(12)(A) suspend the electing individual's 5-year period while "such individual or such individual's spouse" is serving, and (b)(5)(C)(ii)(II) exempts the days when "the taxpayer or the taxpayer's spouse" is serving: the spouse's service counts on both, and none of the three says it counts only on a joint return (fork F30). For a sale on 15 March 2022 of a home owned from 1 January 2012 and used to 31 December 2013, with the spouse on qualified duty from 1 January 2014 to 31 December 2021, the 5-year period begins on 16 March 2009 and all of a gain of 100,000 is left out; without the spouse's service the period has no day of use in it and nothing is. Asserted (`s121-tests-whole.l4`, scenarios 20 and 21; `s121-cases-seat.l4`, the question on the 5-year period with the service the spouse's).
22. The 2-year cap on a temporary absence in (b)(5)(C)(ii)(III) is a cap on the days that count, so an absence of ten years counts for only the days of the 2 calendar years ending on the sale (731 days for a sale on 31 December 2021). Asserted (`s121-tests-b.l4`).

## What the stable binary does not accept

The binary governs where a skill describes something it rejects; these were met while writing this encoding (the first six are in the brief and were not exercised here).

- `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` (except `LEST BREACH ... BECAUSE`), section-level `GIVEN`, sets, `TYPICALLY`, opaque `DECLARE`, and a `YMD` of one's own: not used; "not covered" is `NOTHING` or a constructor, asserted.
- A record cannot be updated: `r1 WITH b IS TRUE` on an existing record is rejected ("You are trying to apply r1 ... (which is not a function)"). The constructors in `s121-whole.l4` therefore take every field.
- `CONSIDER x WHEN a THEN ... WHEN b THEN ...` with the arms on one line is a parse error ("unexpected WHEN"); each arm goes on its own line.
- An `IF ... THEN ... ELSE IF ...` chain whose last `ELSE` sits at the indent of the first `IF` fails with "incorrect indentation"; `BRANCH` is used.
- A constructor with several fields needs commas between its arguments: `Holding OF a, b` (`Holding OF a b` reports "expects 2 arguments"); a list of such constructors goes one item per line, not `LIST Span OF a, b, Span OF c, d` on one line.
- `CONCAT` takes a comma-separated list (`CONCAT "a", "b"`), not juxtaposed arguments; the list-length function is `count`, not `length`.
- Overloaded `min`, `max`, `MINUS`, `PLUS` and `Day` need typed helper functions (`the larger of`, `the smaller of`, `the day number of` in `s121-support.l4`); a genitive binds looser than application, so a call is written `f (x's y)`; a multi-line `LIST` of bare names needs leading commas; `NOT` is parenthesised, `NOT (x EQUALS NOTHING)`; each `#ASSERT` is one line.
- `IMPORT` finds only modules in the importing file's folder, and a name defined in two imported modules cannot be used: every module's names are unique, and `s121-seat.l4` defines none of the layer-1 names.

Nothing in the stable binary prevented an encoding of the whole section; the deontic constructs were not needed because the section imposes no duty.

## What check.sh prints

`L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`, target `main`, run in this folder; there is no earlier baseline, this being the first encoding of the section.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
s121-a-exclusion.l4                            0         0       0        0         0 |      0         0       0        0  same
s121-b-limitations.l4                          0         0       0        0         0 |      0         0       0        0  same
s121-c-reduced.l4                              0         0       0        0         0 |      0         0       0        0  same
s121-cases-seat.l4                             0       146       0        0         0 |      0       146       0        0  same
s121-d1-special.l4                             0         0       0        0         0 |      0         0       0        0  same
s121-d9-service.l4                             0         0       0        0         0 |      0         0       0        0  same
s121-efg.l4                                    0         0       0        0         0 |      0         0       0        0  same
s121-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
s121-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
s121-support.l4                                0         0       0        0         0 |      0         0       0        0  same
s121-tests-a.l4                                0        57       0        0         0 |      0        57       0        0  same
s121-tests-b.l4                                0        86       0        0         0 |      0        86       0        0  same
s121-tests-c.l4                                0        41       0        0         0 |      0        41       0        0  same
s121-tests-d1.l4                               0        62       0        0         0 |      0        62       0        0  same
s121-tests-d9.l4                               0        62       0        0         0 |      0        62       0        0  same
s121-tests-whole.l4                            0        98       0        0         0 |      0        98       0        0  same
s121-whole.l4                                  0         0       0        0         0 |      0         0       0        0  same
TOTAL (17 modules)                             0       552       0        0           |      0       552       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`check.sh` counts error diagnostics and assertion lines and sees no difference in a `#TRACE` outcome; no `#TRACE` is used in this encoding.

`l4 run` was also read for warnings: `DiagnosticSeverity_Warning` appears in no module's output (the last run is in the progress note).

The case file ends with assertions written equal to assertions satisfied (146 and 146).

## What would need doing before the encoding is worth relying on

- A US tax practitioner reads every rule against the official text of section 121, not this rendering, and rules on the forks, above all F1, F4, F6, F7, F11, F16, F17 and the marginal readings.
- The borrowed provisions are obtained and either encoded or confirmed as inputs: sections 216, 267(b), 707(b), 877(a)(1), 1031, 1033, 1041(a), 1250(b)(3); title 10 section 101(a)(5); title 5 section 2105; the Foreign Service Act section 103; the Peace Corps Act sections 5 and 6; the regulations under (c)(2)(B) and the Secretary's specification under (b)(5)(C)(ii)(III).
- The reduced exclusion on a joint return (F17) and an expatriate spouse (F18) are decided, not left not covered.
- A person from the seat answers the questions on real facts and reads each `@desc`; the wording has not been tested on anyone.
- The effect of the effective-date notes in `usc26-s121-notes.txt` on sales before the amendments is not encoded: the section is encoded as in force (the brief's rule), with no earlier version.
- Cases a domain expert writes independently of this author: every expected value here is the author's own reading, worked by hand from the text and the calendar.
