# EU AI Act: serious-incident reporting by providers (solo-2026-10)

**Not for use as advice.**
This is a DRAFT.
No domain expert and no lawyer qualified in EU law has read it against the source.
Nothing here claims to be correct, reviewed, or fit to be relied on as legal advice.

## What is encoded

The provisions of Regulation (EU) 2024/1689 (the AI Act) that decide when a **provider** must report a serious incident, to whom, by when, and what may be done to it if it does not, in two vintages: the text as published in the Official Journal on 12.7.2024, and that text as amended by Regulation (EU) 2026/1744 (the "Digital Omnibus on AI", OJ L 24.7.2026, in force 27 July 2026).

- **High-risk AI systems:** Article 73(1) to (6), (8) to (10), with Article 2(2) (Section B products), Article 75(1) and (1a) as inserted by the Omnibus (reports go to the AI Office for some systems), and Article 20(2) (informing of a risk).
- **General-purpose AI models with systemic risk:** Articles 51 and 52 as far as they decide whether Article 55 applies, the Article 52(1) notification clock, and Article 55(1)(c).
- **Penalties:** Article 99(1), (4), (6), (6a as amended), Article 75c(4) (as inserted), and Article 101(1)(a).
- **Dates:** Article 113 (as enacted and as amended), Article 111(2) and (3), and the Omnibus's own entry into force.
- **Definitions:** Article 3, points (3), (49) and (61).

Method: the solo `encoding-a-subject` workflow, one session, from the brief in the coordinator's scratchpad (`BRIEF-eu-ai-act.md`), target compiler `main`.
Every quotation is copied mechanically from the deposited texts with `srcrefs.py quote` and checked with `srcrefs.py check --refs`.
An independent test pass followed (`tests-independent.l4`, 159 assertions, all satisfied); it and the changes made in response are described under "The independent test pass" below.

## Seat

**The provider**, a company or other body that develops an AI system or a general-purpose AI model and places it on the market under its own name (Article 3(3)).
Questions are worded as the provider asks them ("Must I report this incident?", "To whom?", "By when?", "What is the most I can be fined for not reporting it?").
Facts are ones the provider can state.
Provisions addressed to officials (the market surveillance authority, the AI Office, the Commission) are encoded only for what they mean to the provider: who receives the report (Articles 73(1), (10), 75(1a)), the date by which the authority must take measures (Article 73(8)), and the ceilings on fines (Articles 99, 101, 75c).
The deployer has no seat here; Article 26(5) is quoted, not encoded (fork F1).

Design defaults (CLAUDE.md, 2026-10-18), followed: the Act alone; the actors the text names; judgments left to someone else asked as facts ("serious", "presents a risk within Article 79(1)", "necessary to ensure timely reporting"); the Act's own definitions worked out from facts (Articles 3(3), 3(49), 3(61), 51); borrowed terms asked as facts ("critical infrastructure", which Article 3(62) takes from Directive (EU) 2022/2557; "general-purpose AI model"; SME and SMC).
Departure: **whether a system is high-risk** (Article 6, Annexes I and III) is not worked out but asked as a fact, the "route", because the brief puts classification out of scope.
The Commission's power to amend the 10^25 threshold (Article 51(3)) is recorded as an assumption: the Regulation's own figure is used, and a delegated act would change the answers.

## Edition encoded, and the two vintages

| vintage | source | used |
| --- | --- | --- |
| as enacted | `registers/source-bundle/eu-ai-act-2024-1689.txt`, OJ L 12.7.2024 | the law before 27 July 2026 |
| as amended by 2026/1744 | the same, read with `registers/source-bundle/eu-omnibus-2026-1744.txt` (OJ L 24.7.2026) | the law from 27 July 2026 |

The core rules take the vintage as an input, and the tests assert the same facts against both.
The seat module derives the vintage from the date asked about (`the version in force on`, `aia-dates.l4`): published 24.7.2026, "in force on the third day following" (Omnibus Art 4, line 764) is 27 July 2026, the date the Omnibus itself gives for new Article 113(d).

### What the Omnibus amends (read in full, 2026-10-24)

The brief, and the note in `subjects/comparative/ai-content-labelling/source/sources.json`, say the Omnibus "replaces Article 50(7) and adds Article 111(4)".
**It does much more.**
Its Article 1 has 43 points amending Regulation 2024/1689: Articles 1(2)(g), 2(2), 2(7), 2(13), 3(14), 3(14a), 3(14b), 4, 4a, 5, 6(1a)-(1c), 10, 11(1), 17(2), 25(2) and (4), 27(4) and (5), 28(8) and (9), 29(4), 30(2), 40(2), 42(3), 43(3), 50(7), 56(6), 57, 58(1), 60(1) and (2), 60a, 63(1), 64(3), 69(2), 70(8), 72(3), 75 (heading, (1), (1a)-(1e), (2a)), 75a to 75d, 76(1), 77, 95(4), 96(1), 97(2), (3) and (6), 99(1), (4)(da) and (6a), 111(2) and (4), 113 (third paragraph, points (a), (c), (d)), and Annexes I, VIII and XIV (new).
Its Articles 2 and 3 amend Regulations (EU) 2018/1139 and 2023/1230; the latter requires delegated acts reflecting Articles 17, 19, 72 and **73** of the AI Act for machinery, to apply by 2 August 2028 (Omnibus lines 745-746).

**Of the scoped provisions, the Omnibus amends:** Article 2(2) (line 136), Article 75(1) and inserts 75(1a) (lines 417-434), inserts Article 75c(4) (lines 499-502), Article 99(1), (4)(da) and (6a) (lines 591-600), Article 111(2) (line 606), and Article 113(c) (lines 622-626).
**It does not amend** Articles 3(3), 3(49), 3(61), 20, 26, 51, 52, 55, 73 or 101.
So Article 55 keeps one vintage, and the Article 73 clocks are the same in both; what changes is who receives the report, which systems the duty reaches and when, and the fines.

**The arXiv claim is verified.**
The Arcadia Impact / The Future Society paper (arXiv 2608.19278) describes an "Article 75(1a) inserted by the 2026 Digital Omnibus on AI" that changes who receives reports.
The deposited Omnibus contains it, at line 434: "By way of derogation from Article 73, providers of high-risk AI systems subject to the competence of the AI Office pursuant to paragraph 1 of this Article shall report any serious incidents to the AI Office. Article 73 (2) to (9), shall apply mutatis mutandis."
Only that one claim of the paper was checked.

## Findings ("what the Act turns out to say")

1. **Article 55(1)(c) states no period.** A provider of a GPAI model with systemic risk reports "without undue delay" (line 1369), with no number of days. The encoding answers `no period stated "without undue delay"`, never Article 73's 15, 10 or 2 days. Asserted.
2. **A failure to report under Article 73 has no fine ceiling in the Regulation for a nationally supervised provider.** Article 99(4)(a) fixes ceilings for "obligations of providers pursuant to Article 16" (line 2014). Article 16 (lines 870-896) does not name Article 73; it names Article 17 (a quality management system, which must include reporting *procedures*, 17(1)(i), line 917) and Article 20 (16(j), line 892). So the failure to *report* falls to the Member State rules under Article 99(1). As amended, Article 75c(4)(a) brings "infringement of any applicable provision of this Regulation, including those not listed in Article 99(4)" under the Article 99(4) ceiling for providers the AI Office supervises. Asserted both ways. Fork F8.
3. **The recipient changes with the vintage.** As amended, a provider of a high-risk system built on its own (or its undertaking's) general-purpose AI model, outside the exceptions, or one that is part of a designated very large online platform or search engine, reports to the AI Office (Art 75(1a)), not to the market surveillance authorities. Asserted.
4. **The as-enacted dates for Article 73 never came into application.** The Omnibus entered into force on 27 July 2026, six days before the general date of 2 August 2026, so the amended Article 113(c) and 111(2) were already law when Article 73 would first have applied. The as-enacted answers for dates after 27 July 2026 are counterfactual; they are kept because vintages are inputs.
5. **As amended, no high-risk system is reached by Article 73 before the Chapter III date.** Article 73 is in Chapter IX and on the plain reading applies from 2 August 2026, but amended Article 111(2) keeps the Regulation off any high-risk system placed on the market before "the date of application of Chapter III" (2 December 2027 for Annex III, 2 August 2028 for Annex I) unless its design changes significantly from then. Fork F3.
6. **Article 101 carries no SME reduction.** Article 99(6) speaks of "each fine referred to in this Article" (line 2028), so the "whichever is lower" rule for SMEs does not reach Article 101, whose ceiling is "whichever is higher" for every provider (line 2079). Asserted.
7. **The Article 51(2) threshold is lost in the text file.** The extraction reads "greater than 1025" (line 1309); the XHTML has a superscript, 10^25. Recorded in `registers/source-bundle/eu-ai-act-2024-1689.formulas.md`.
8. **A tooling finding, not law.** On the main build 1.6.99, `EXPONENT 10 25` evaluates to `10000000000000000905969664`, a floating-point value wrong by about 9 x 10^8. The encoding writes the exact literal `10_000_000_000_000_000_000_000_000`; the boundary tests (exactly 10^25 is not "greater than", 10^25 + 1 is) pass with it.

## Answer table: every reporting clock in scope

"Day 0" is the day of the trigger; "last day" is the trigger plus N calendar days (fork F7).

| who reports | what | to whom | clock | provision | encoded as |
| --- | --- | --- | --- | --- | --- |
| provider, high-risk system | serious incident, general | market surveillance authorities of the Member States where it occurred | immediately after a causal link (or its reasonable likelihood) is established, **and not later than 15 days** after becoming aware | Art 73(2) (line 1731) | `no later than` aware + 15 |
| same | widespread infringement, or a 3(49)(b) critical-infrastructure incident | same | immediately, **and not later than two days** after becoming aware | Art 73(3) (line 1733) | aware + 2 |
| same | death of a person | same | immediately after a causal relationship is established or suspected, **not later than 10 days** after becoming aware | Art 73(4) (line 1734) | aware + 10 |
| same | the complete report after an incomplete initial one | same | **no period stated** ("followed by a complete report") | Art 73(5) (line 1735) | `no period stated` |
| same | investigation after reporting | (cooperate with competent authorities) | **no period stated** ("without delay") | Art 73(6) (line 1736) | `no period stated` |
| same, medical device, national route | point (c) incidents only | the national competent authority chosen by the Member State | as Art 73(2)-(4) | Art 73(10) (line 1741) | recipient changes |
| same, AI Office route (as amended) | every serious incident, a medical device included (F14) | **the AI Office** | Art 73(2) to (9) "mutatis mutandis", not (10) | Art 75(1a) (Omnibus line 434) | recipient changes; clocks as above |
| provider, high-risk system | risk within Art 79(1) | market surveillance authorities, and the notified body where applicable | **no period stated** ("immediately") | Art 20(2) (line 951) | `no period stated` |
| market surveillance authority (what it means for me) | measures on my report | (me) | **within seven days** from receipt | Art 73(8) (line 1739) | receipt + 7 |
| provider, GPAI model | the Article 51(1)(a) condition is met or known to be going to be met | the Commission | without delay, **within two weeks** | Art 52(1) (line 1313) | `no later than` date + 14 |
| provider, GPAI model with systemic risk | relevant information about serious incidents | the AI Office and, as appropriate, national competent authorities | **no period stated** ("without undue delay") | Art 55(1)(c) (line 1369) | `no period stated` |
| deployer (not this seat) | serious incident | the provider first, then importer or distributor and the authorities | "immediately" | Art 26(5) (line 1023) | quoted, not encoded |

Where Art 73(3) and (4) both apply, the earlier limit (two days) is taken (fork F2).

### Dates of application

| provision | as enacted | as amended |
| --- | --- | --- |
| Art 3 (Chapter I) | 2 Feb 2025 | same |
| Arts 51, 52, 55 (Chapter V); Art 99 (Chapter XII) | 2 Aug 2025 | same |
| Art 55 for a model placed before 2 Aug 2025 | bound from 2 Aug 2027 (Art 111(3), fork F4) | same |
| Art 101 | 2 Aug 2026 (excepted from 113(b)) | same |
| Art 73, Annex III system | 2 Aug 2026 | 2 Aug 2026 on the plain reading; reaches no system placed before 2 Dec 2027 unless its design changed significantly from then (Art 111(2)) |
| Art 73, Annex I Section A system | 2 Aug 2027 ("Article 6(1) and the corresponding obligations") | 2 Aug 2026 on the plain reading; reaches no system placed before 2 Aug 2028 unless changed (Art 111(2)) |
| Art 73, Annex I Section B system | never (Art 2(2)) | never (Art 2(2) as replaced) |
| Arts 16, 20, 26 (Chapter III s 1-3), Annex III | 2 Aug 2026 | 2 Dec 2027 |
| Same, Annex I Section A | 2 Aug 2027 | 2 Aug 2028 |
| Art 75(1a), 75c | (not in the text) | 2 Aug 2026 (Chapter IX, general date) |
| legacy high-risk system intended for public authorities | bound from 2 Aug 2030 (fork F4) | same |

## Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| Art 2(2) | Section B products | encoded, both vintages (`aia-art73.l4`) |
| Art 3(3) | provider | encoded (`aia-definitions.l4`) |
| Art 3(14a), (14b) (as amended) | SME, SMC | input (`size of the provider`); the definitions borrow Recommendations 2003/361/EC and (EU) 2025/1099, not deposited |
| Art 3(26), (47), (48) | market surveillance authority, AI Office, national competent authority | encoded as constructors of `recipient` |
| Art 3(49) | serious incident | encoded |
| Art 3(61) | widespread infringement | encoded |
| Art 3(62) | critical infrastructure | input: borrowed from Directive (EU) 2022/2557, not deposited |
| Art 3(63)-(65) | general-purpose AI model, high-impact capabilities, systemic risk | input (63); through Art 51 (64, 65) |
| Art 6, Annexes I and III | classification as high-risk | out-of-scope by the brief: asked as the input "route", and Annex III points 2 and 8(a) as inputs for Art 75(1) |
| Art 16(c), (j); Art 17(1)(i) | provider obligations | quoted in `aia-penalties.l4` for the reach of Art 99(4)(a) |
| Art 20(1) | corrective action, informing the supply chain | out-of-scope: a duty to inform distributors, deployers, importers, not a report to an authority |
| Art 20(2) | informing of a risk | encoded |
| Art 26(5) | deployer's duty on a serious incident | inert: quoted; the deployer has no seat (fork F1) |
| Art 51(1), (2) | classification | encoded |
| Art 51(3) | power to amend thresholds | inert: an assumption that no delegated act has changed 10^25 |
| Art 52(1) | notification to the Commission | encoded |
| Art 52(2), (3) | arguments against classification | encoded as the input "the Commission has accepted my arguments" (fork F5) |
| Art 52(4) | designation | input |
| Art 52(5), (6) | reassessment, published list | out-of-scope: they do not decide whether Art 55 applies on a date |
| Art 55(1)(a), (b), (d) | evaluation, risk mitigation, cybersecurity | out-of-scope: not reporting duties |
| Art 55(1)(c) | serious incidents | encoded |
| Art 55(2) | codes of practice | out-of-scope: a separate subject handles the GPAI Code of Practice |
| Art 55(3) | confidentiality | out-of-scope: binds the authorities |
| Art 73(1)-(6) | reporting, clocks, initial report, investigation | encoded |
| Art 73(7) | the authority informs Art 77 bodies; Commission guidance | out-of-scope: official duties with no effect on what the provider must do or by when |
| Art 73(8) | the authority's measures within seven days | encoded, for what it means to the provider |
| Art 73(9), (10) | limits to point (c) incidents; medical devices | encoded |
| Art 73(11) | authorities notify the Commission | out-of-scope: official duty |
| Art 75(1), (1a) (as amended) | AI Office competence; reports to the AI Office | encoded |
| Art 75(1b)-(1e), (2a); Arts 75a, 75b, 75d (as inserted) | AI Office powers, commitments, safeguards | out-of-scope: governance machinery |
| Art 75c(4) (as inserted) | fines for AI-Office-supervised operators | encoded |
| Art 75c(5) (as inserted) | periodic penalty payments. The ceiling, verbatim (Omnibus line 523): "Those penalty payments shall be effective and proportionate, and, where applicable, shall not exceed 5 % of the average daily income or worldwide annual turnover in the preceding financial year per day, calculated from the date appointed by the decision." This reads as garbled: "average daily income or worldwide annual turnover in the preceding financial year per day" does not resolve to one base for the 5 %. It is quoted as it stands and not tidied | **deferred**: what may be done to me, but it compels compliance with decisions rather than punishing a missed report; not reached in the time budget, and the base of the ceiling would have to be settled first |
| Art 99(1) | Member State penalties | encoded as the outcome "no maximum in this Regulation" |
| Art 99(3) | Article 5 prohibitions | out-of-scope |
| Art 99(4), (6) | ceilings; SMEs | encoded |
| Art 99(4)(da) (as amended) | Art 25(2), (4) | out-of-scope: not a reporting duty |
| Art 99(5) | incorrect information in reply to a request | **deferred**: a reply to a request is not the report itself; worth adding next |
| Art 99(6a) (as amended) | SMCs | encoded |
| Art 99(7) | factors for the amount | inert: judgments for the authority; the encoding gives ceilings only |
| Art 101(1)(a) | Commission fines on GPAI providers | encoded |
| Art 101(1)(b)-(d), (2)-(6) | other infringements; procedure | out-of-scope |
| Art 111(1) | Annex X large-scale IT systems | out-of-scope: public-sector systems listed in Annex X, not deposited for this purpose |
| Art 111(2) | legacy high-risk systems | encoded, both vintages |
| Art 111(3) | legacy GPAI models | encoded (fork F4) |
| Art 111(4) (as added) | Art 50(2) legacy | out-of-scope: transparency, in `comparative/ai-content-labelling` |
| Art 113 | entry into force and application | encoded, both vintages |
| Omnibus Art 4 | entry into force | encoded |

No row is left `deferred` without a reason; two are deferred (Art 75c(5), Art 99(5)).

## Fork register

**F1. Whose awareness starts the clock.** Art 73(2)-(4): "after the provider or, where applicable, the deployer, becomes aware".
Readings: (i) the provider's clock runs from the provider's awareness, and "where applicable, the deployer" covers the case where the deployer reports itself because it cannot reach the provider (Art 26(5), line 1023: "If the deployer is not able to reach the provider, Article 73 shall apply mutatis mutandis"); (ii) the clock runs from the earlier of the provider's and the deployer's awareness.
Taken: (i), because Art 26(5) gives "where applicable" a natural referent, and reading (ii) would put a provider in breach for days before it could know.
Reading (ii) would shorten the provider's deadline whenever a deployer was slow to tell it.
The independent test author took reading (ii) (its answers-first F2: "earlier of provider's and deployer's awareness").
The encoding has no input for the deployer's awareness, so the two readings could not be tested against each other: every independent assertion supplies one awareness date, which both readings treat alike.
An extra input, the date the deployer became aware (a `MAYBE DATE`, `NOTHING` where there is no deployer or it learned no earlier), would change only the anchor.
On reading (ii) every Art 73 clock would run from the earlier of the two dates, so a provider told late by its deployer would get a shorter deadline, or one already past on the day it learned of the incident; on reading (i) the input would matter only where the deployer reports itself under Art 26(5), which this seat does not encode.

**F2. Overlapping clocks.** A death in a widespread infringement, or a death from a critical-infrastructure disruption, falls under both Art 73(3) (two days) and (4) (10 days); each is "notwithstanding paragraph 2", neither is notwithstanding the other.
Taken: the earlier limit, two days, since reporting by then satisfies both.

**F3. When Article 73 applies, as amended.** Amended Art 113(c) (Omnibus lines 622-626) moves "Chapter III, Sections 1, 2, and 3" to 2 December 2027 / 2 August 2028 and drops the as-enacted words "and the corresponding obligations".
Article 73 is in Chapter IX.
Readings: (i) Art 73 applies from the general date, 2 August 2026, and Art 111(2) (as amended) is what keeps it off systems placed before the Chapter III date; (ii) Art 73 cannot apply before Art 6, which defines "high-risk", applies.
Taken: (i), the plain reading of Art 113, with Art 111(2) applied as written.
The two readings agree on every consistent set of facts, because a system placed on or after the Chapter III date is not caught by Art 111(2), and one placed before it is reached only by a significant design change from that date; the encoding never borrows the Chapter III date for Art 73.
They differ only where the day on which Art 73's reach is judged precedes the system's first placing on the market, which no rule excludes: reading (i) then reaches a system placed on or after the Chapter III date that is not yet on the market, and reading (ii) does not.
That day was the date asked until 2026-10-24, and is now the day of awareness (F13).
The independent test author took reading (ii): Art 73 applies only from 2 December 2027 (Annex III) and 2 August 2028 (Annex I), because before Art 6 applies it has no high-risk system to bind (its answers-first F4).
Its date-of-application assertions all place the system on the day asked, so they are consistent facts, and all of them pass.
As enacted, an Art 6(1) system's Art 73 duty is read as one of "the corresponding obligations" (line 2206), so it waits until 2 August 2027.

**F4. "Shall take the necessary steps to comply ... by".** Art 111(2), second sentence (public-authority systems, 2 August 2030) and Art 111(3) (GPAI models placed before 2 August 2025, 2 August 2027).
Readings: (i) the obligations bind from that date; (ii) they bind earlier, and the date is a deadline for completing compliance steps.
Taken: (i).

**F5. Accepted Article 52(2) arguments.** Art 52(3) (line 1315) says only that rejected arguments leave the model classified.
Taken: an accepted argument takes the model out of Art 51(1)(a), from Art 52(2)'s "should not be classified"; a Commission designation (Art 51(1)(b), 52(4)) classifies it regardless.

**F6. Article 3(61).** (a) "other than the Member State in which: (i) ...; (ii) ...; or (iii) ..." does not say which Member State is excluded when (i), (ii) and (iii) name different ones; the provider supplies the count of "other" Member States.
(b) requires harm to collective interests, common features, concurrence, the same operator, and at least three Member States; the encoding asks common features and same operator as facts, and folds harm and concurrence into the count of Member States "in which it is occurring concurrently".

**F7. Counting days.** The day of the trigger is day 0; "not later than N days after" makes trigger + N the last day, inclusive; days are calendar days, because Art 73 says "days" without qualification and Art 52(1) says "two weeks" (read as 14 days).
Regulation (EEC, Euratom) No 1182/71, which lays down rules for periods, dates and time limits in Union acts, may change this, including for a period ending on a weekend or public holiday.
It is **not deposited and was not read** for this encoding.

**F8. The fine for not reporting under Art 73.** Readings: (i) Art 99(4)(a) does not reach it (Art 16 does not name Art 73), so Member State rules under Art 99(1) apply with no ceiling in the Regulation; (ii) Art 99(4)(a) reaches it through Art 16(c) and Art 17(1)(i).
Taken: (i). Reading (ii) reaches the absence of reporting *procedures* in the quality management system, not the failure to make a report.
As amended, Art 75c(4)(a) settles it for AI-Office-supervised providers: the Art 99(4) ceiling applies.

**F9. "Article 99(3) to (7)" in Art 75c(4).** Taken to include paragraph 6a, which the same Omnibus inserts between 6 and 7, so an SMC supervised by the AI Office gets "whichever is lower".

**F10. Article 73(9) and (10) with a death.** Both limit "the notification of serious incidents" to point (c) incidents.
An incident that infringes fundamental-rights obligations and also kills someone is a point (c) incident, so it is reported, and the encoding still applies the 10-day clock of Art 73(4).

**F11. "Serious incident" for a model.** Art 3(49) defines a serious incident as one "of an AI system"; Art 55(1)(c) asks the model's provider to report "relevant information about serious incidents".
Taken: the same Art 3(49) test on the incident's facts; the encoding does not decide which systems' incidents are "relevant" to a model.

**F12. "Where that incident occurred".** Art 73(1) sends the report to the market surveillance authorities "of the Member States" (plural) where the incident occurred; an incident in several Member States goes to each.
The encoding names the recipient class, not the list of states.

**F13. On which day Art 73's reach is judged.** Art 113 says when Art 73 applies, Art 111(2) whether the Regulation reaches a system placed before the cut-off "as from" a significant design change, and Art 73(2)-(4) run every clock from the day the provider "becomes aware".
Readings: (i) judge the reach on the date the question is asked; (ii) judge it on the day of awareness.
Until 2026-10-24 the encoding took (i), and the independent pass showed what that does (open question 7): a system placed before the cut-off whose design then changed significantly, with awareness before the change and the question asked after it, was told "must report", with a deadline that had passed before any duty could have existed.
Taken now: (ii). If the Regulation did not reach the system on the day of awareness, no duty arose for that incident, and a later design change does not create one.
Residual doubt: an incident that occurred before the Regulation reached the system but became known to the provider after it is reported on reading (ii); the clocks run from awareness, and the encoding has no date of occurrence.
The seat still takes the version in force from the date asked; for a question asked on or after the day of awareness this cannot change an answer, because neither version applies Art 73 before 2 August 2026, by which time the amended text was in force.
Asserted, with both sides (`aia-tests.l4`, "Article 73 judged on the day of awareness").

**F14. Art 73(10) on the AI Office route.** Art 75(1a) (Omnibus line 434) has providers under the AI Office's competence "report any serious incidents to the AI Office", and applies "Article 73 (2) to (9)" mutatis mutandis, which leaves out (10).
A medical device cannot come under Art 75(1)(a), whose exception (i) excludes Annex I products, but it can under Art 75(1)(b), if it constitutes or is part of a designated very large online platform or search engine.
Until 2026-10-24 the encoding applied (10)'s limit to point (c) incidents on that route too (open question 8).
Taken now: on the AI Office route (10) does not apply, so such a provider reports every serious incident, to the AI Office; as enacted, with no Art 75(1a), (10) still limits it.
Asserted (`aia-tests.l4`, "Article 75(1a) applies Article 73(2) to (9), not (10)").

Where else I looked for forks and found none worth recording: Art 73(5) and (6) (plain permissions and duties), Art 101(1)'s "whichever is higher" (plain), the dates in Art 113 (each is a day of a month).

## What check.sh prints

Target compiler: **main**.
`l4` used: `/Users/mengwong/.cache/l4-main/99/l4`, `1.6.99 (main, 6cc2c91, 2026-10-21)`; `check.sh` compared it with the main build `fetch-main-l4.sh` returned, the same build.
Run 2026-10-24, after rebasing onto origin/main and making the changes under "The independent test pass":

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.99 (main, 6cc2c91, 2026-10-21)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
aia-art73.l4                                   0         0       0        0         0 |      0         0       0        0  same
aia-dates.l4                                   0         0       0        0         0 |      0         0       0        0  same
aia-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
aia-domain.l4                                  0         0       0        0         0 |      0         0       0        0  same
aia-gpai.l4                                    0         0       0        0         0 |      0         0       0        0  same
aia-penalties.l4                               0         0       0        0         0 |      0         0       0        0  same
aia-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
aia-tests.l4                                   0       120       0        0         0 |      0       120       0        0  same
tests-independent.l4                           0       159       0        0         0 |      0       159       0        0  same
TOTAL (9 modules)                              0       279       0        0           |      0       279       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`aia-tests.l4` has 120 `#ASSERT` lines, 120 satisfied; `tests-independent.l4` has 159, 159 satisfied; `l4 run` on each printed no Error or Warning diagnostics.
No assertion is expected to fail.
The encoding has no regulative (`DEONTIC`) rules and no `#TRACE`, so nothing `check.sh` cannot see is in play.

Quotations: `python3 -I srcrefs.py check --refs ../../registers/source-bundle/eu-ai-act-2024-1689.txt aia-*.l4 tests-independent.l4` printed `93 src: lines, 33 runs, 81 locators, 0 problems`.
`--strict` reports problems of one kind only, a later rule citing a run above it more broadly or narrowly than the run's first `@ref` ("not exact"); the skill says to use `--refs` for a row that cites broadly.
No `@ref` sits at the end of a file or after code on its line, and no annotation is unknown (checked with `l4 check` on each module).

## The independent test pass

**Method.** A separate agent that had not seen this encoding decided every expected value from the deposited sources alone, and wrote them down in `tests-independent-answers-first.md` (copied here from the coordinator's scratchpad) before opening any file in this folder.
It then read the encoding only to learn its names, and wrote `tests-independent.l4`.
No expectation was adjusted to match the code.

**Result.** 159 satisfied, 0 failed, 0 refused, 0 errors, with the same counts on main, in the coordinator's run and again in the run above, after the changes below.
**Negative control**, as reported by the coordinator: four deliberately wrong expectations were added, and all four failed, so the harness can fail.
That control is recorded in neither file and was not re-run here.

**Where the readings differ.** Two forks, neither visible in the counts: F1 (whose awareness starts the clock; the tester takes the earlier of provider's and deployer's, and the difference is untestable because the encoding has no deployer input) and F3 (when Art 73 applies as amended; the readings agree on every consistent set of facts).

**What it led to, 2026-10-24.**
1. Art 73's reach is now judged on the day of awareness, not the date asked (F13, open question 7).
   Three of this encoding's own assertions put a date edge on the date asked while holding awareness at 10 February 2028; they failed after the change (the as-enacted Annex III and Section A edges, and the public-authority edge of 2 August 2030).
   Their facts were rewritten so that the awareness date carries the edge, asked on the same day; no expected value changed.
2. Art 73(10) no longer limits a provider on the AI Office route (F14, open question 8).
3. Eight assertions added to `aia-tests.l4`, four for each change.
   Control: run against the previous `aia-art73.l4`, five of the eight fail; the other three are the opposite sides of the same edges, which both versions answer alike.
4. The four Article 73 questions in `aia-seat.l4` now say in the `@desc` of `as_of_date` that the duty is judged on `aware_date`; no input was added or renamed.

## Modules, in reading order

1. `aia-domain.l4`: nouns only.
2. `aia-dates.l4`: the `YMD` shim, the vintage in force on a date, Articles 113 and 111.
3. `aia-definitions.l4`: Article 3(3), (49), (61).
4. `aia-art73.l4`: Articles 2(2), 73, 75(1) and (1a), 20(2), 26(5) quoted.
5. `aia-gpai.l4`: Articles 51, 52(1), 55(1)(c).
6. `aia-penalties.l4`: Articles 99, 75c(4), 101.
7. `aia-seat.l4`: the provider's nine questions with `@export` and `@desc`, over plain inputs; generated by a script so its long parameter lists agree.
8. `aia-tests.l4`: 120 assertions from the source.
9. `tests-independent.l4`: 159 assertions by the independent test author, with `tests-independent-answers-first.md`, the answers it wrote down before opening the encoding.

## Open questions for a domain expert

1. Fork F8: is a provider's failure to report under Art 73 reachable under Art 99(4)(a), or is it left to national law with no Union ceiling? National implementing laws were not read.
2. Fork F7: does Regulation 1182/71 extend an Art 73 deadline that ends on a weekend or public holiday?
3. Fork F1: does the deployer's earlier awareness start the provider's clock?
4. Fork F3: is there a reading on which Art 73 bites before the Chapter III date as amended, for example for a system placed before 2 December 2027 whose design changes significantly after it?
5. Has the Commission adopted a delegated act under Art 51(3) changing the 10^25 threshold?
6. Art 75(1)(a): what counts as "providers forming part of the same undertaking"? The encoding asks it as a fact.
7. Fork F13, raised by the independent pass: should Art 73's reach be judged on the day of awareness rather than the date asked? Decided yes and implemented on 2026-10-24, with four assertions. Still open: an incident that occurred before the Regulation reached the system and became known after it.
8. Fork F14, raised by the independent pass: Art 75(1a) applies Art 73(2) to (9), not (10). Checked against Omnibus line 434 and fixed on 2026-10-24, with four assertions: a medical device on the AI Office route reports every serious incident. Still open: is leaving out (10) deliberate, or a gap a court would fill by applying it?

## What would need doing before this is worth relying on

- A review (HG1) by someone qualified in EU law, provision by provision against the deposited text.
- Resolve the two forks the independent pass left standing, F1 and F3, by a person qualified to rule on them.
- Deposit and read Regulation 1182/71 (fork F7), Regulation (EU) 2019/1020 (Art 73(8)), and Directive (EU) 2022/2557 (Art 3(62)).
- Settle the licence of the Official Journal texts (`SOURCE-LICENSE.md`: UNDETERMINED).
- Encode Art 99(5) and Art 75c(5) (deferred).
