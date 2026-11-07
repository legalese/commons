# National Redress Scheme for Institutional Child Sexual Abuse Act 2018 — baseline encoding, the survivor's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a question that reaches a gap answers `not covered` with the reason, or `NOTHING`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is the first encoding of this Act. No ledger entry asked for it; it was written as part of a run over the Acts behind personal injury, compensation and other claims, with the focus "the provisions a claimant meets". For a survivor of institutional child sexual abuse, this Act is the redress scheme that runs beside (and, on acceptance, instead of) a civil claim against the institutions responsible.

Every question is a function named as the survivor would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud. There are 28 exported questions, grouped under `§§` headings in the order an application meets them (can I apply; am I eligible; after I apply; how much I get; my offer; review; once I have accepted; if the applicant dies; false information). Headings for situations the person may not be in say so in brackets.

**Regulative rules.** Each is run inside a question that takes plain dates; no question takes a DEONTIC or an EVENT.

| Rule | Party | Modal | Seat question that runs it |
|---|---|---|---|
| `s 42(3) -- I must give my acceptance document before the end of the acceptance period` | me | DO give the acceptance document WITHIN the days to the last day of the acceptance period; LEST breach (taken to have declined, s 45(2), unless s 45(3)) | `Where does my offer of redress stand question` |
| `s 73(2)(a) -- I must apply for review within the review period` | me | DO apply for review WITHIN the days to the last day of the review period; LEST breach (extension routes named) | `Am I in time to apply for review question` |
| `Rules s 15(2) -- the Operator must give me my notice before I turn 18` | the Operator | MUST give the notice, PROVIDED the day is not before the window opens (6 months before turning 18), WITHIN the days to 3 months before turning 18 | `Has the Operator given me my notice before I turn 18 question` |

The case file asserts, through a helper `ends fulfilled` (a `CONSIDER … WHEN FULFILLED`), that a trace ends FULFILLED or that it does not; each rule's breach is also `#TRACE`d with an `-- expect:` line, because on the stable `l4` a breached trace cannot be compared with `EQUALS`.

**Dates.** `nrs-dates.l4` uses the built-in date functions only (no daydate). Periods of months "starting on" a day (ss 34(6), 40(1)) are read with the Acts Interpretation Act 1901 s 2G (borrowed, not deposited): they include that day and end immediately before the corresponding day, or at the end of a month that has none (an offer of 31 August has an acceptance period to at least 28 February). Periods of weeks or days "beginning on" or "starting on" the date of a notice include that date (s 24(4): 4 weeks from 2 March end on 29 March). Weekend and holiday last days are not moved (fork F9).

## Edition

National Redress Scheme for Institutional Child Sexual Abuse Act 2018, No. 45, 2018, **Compilation No. 9, compilation date 28 September 2024** (register id C2024C00613, includes amendments up to Act No. 9, 2024), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2018A00045.txt`, with the s 30(2) formula `(1.019)^n` from `C2018A00045.formulas.md`. Part 2-2 is at line 255 of the deposit, Part 2-4 at 662, Part 3-2 at 1037, Part 4-1 at 1501, s 167 at 2668, s 193 at 2944.

**Brought in:** the National Redress Scheme for Institutional Child Sexual Abuse Rules 2018, **Compilation No. 9, compilation date 19 February 2025** (register id F2025C00180), retrieved 6 November 2026, deposited at `subjects/au/national-redress-scheme-for-institutional-child-sexual-abuse-rules-2018/registers/source-bundle/F2018L00975.txt` (ss 4B, 6, 11, 12, 15, 26(3)-(5), 33(3)). The Rules prescribe no later scheme sunset day (s 193(1)(b)), no further advance-payment circumstance (s 56B(1)(e)(v)) and no further relevant circumstance (s 15(4)(f)).

**Not deposited, so inputs:** the assessment framework (s 32 declaration: the maximum redress payment and the counselling amount), the assessment framework policy guidelines (s 33), the direct personal response framework (s 55), the Ministers' declarations of participating institutions and declared providers, and the States' referral Acts (which States are participating States, s 144). The Rules' own formulas (ss 21(1), 23(2), 24(1), 25(1), 26(6), 27(3)) were lost from the Rules deposit, which has no formulas sidecar; see finding 10.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nrs-dates.l4` | (exercised through the cases below) | 0 errors, 0 warnings |
| `nrs-survivor.l4` | `nrs-cases-survivor.l4` | 203 written, 203 satisfied; 3 traces, each a BREACH as its `-- expect:` line says |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text before the run; the s 30 amounts were worked with exact decimals (1.019^2 = 1.038361; 1.019^3 = 1.058089859) and rounded up to the cent. Every exported question has cases, with the edges: the last ordinary day to apply (30 June 2027) and the first day of the last 12 months (1 July 2027), the sunset day and the day after, the scheme start day for the abuse, the day before an 18th birthday, a child turning 18 on the sunset day and on the day before, the 70th and 55th birthdays for an advance payment, the $150,000 and $5,000 caps and just over, a prior payment one day before its second anniversary, an institution's share nil at the determination but not at the application, day 183 and 184 of an acceptance period, day 28 and 29 of a review period, an acceptance period starting on 31 August, the 4-months-before edge and both ends of the 6-to-3-month notice window.

## Seat

**The survivor**: a person who was sexually abused as a child, in circumstances where an institution was responsible for the abuser having contact with them, and who applies for redress under the scheme, receives (or does not receive) an offer, accepts or declines it, and may seek review. In ss 58-60 the seat is the family member or other person asking what happens to the redress payment when the applicant dies before accepting. The questions are the ones that person asks: "Can I apply?", "By when?", "Am I eligible?", "How much will I get?", "By when must I accept?", "Can I still sue after accepting?", "Am I in time to seek review?".

The Operator, the independent decision-makers, the Ministers, the institutions, the funders of last resort and the participating jurisdictions get no seat. Their duties are encoded as what they mean for the survivor (what must be given to me, by when), and their judgments are inputs.

The 2026-10-18 defaults:

- **The Act, with the Rules that set its numbers and dates.** The assessment framework and the other declarations are not deposited (see Edition); their figures are inputs.
- **The actors the text names:** the person applying, the Operator, the reviewer, participating and partly-participating institutions, listed and defunct institutions, funders of last resort, the Home Affairs Minister (security notices), specified advisors.
- **Judgments handed to others are answered conditionally:** the Operator's "reasonable likelihood" (ss 12, 29), its findings on responsibility (s 15(2)-(4)), "urgent" (s 24(4)), "exceptional circumstances" (ss 20(2), 34(7), 40(2), 56B(1)(e)(iv), 63(2B)), "satisfied" (ss 56B(1)(e), 63(2)(a)(iv), 63(5), 75(4)), "considers it appropriate" (s 56B(1)(g)). All are inputs. Where the Operator must be "satisfied" of a plain fact (age 70, age 55), the fact is worked out from the date of birth.
- **The Act's own definitions are worked out from facts:** child (s 6), within the scope (s 14), eligible (s 13), responsible, primarily and equally responsible (s 15, as findings), relevant prior payment (s 30(2) step 3, Rules s 26), the saved amount (ss 50, 53, 56D), released institution or official (s 42(2)(c)), scheme start and sunset days (ss 6, 193). Borrowed terms (Australian citizen, permanent resident, Aboriginal person, terminally ill, sexual offence, terrorism offence, unlawful killing) are asked as facts with a gloss.
- **One case:** one person's application, and its one offer.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (see Scope).

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

The rulings, word for word as section 5 of `docs/ENCODING-GUIDE.md` records them: a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit. Periods ruling: (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`.

Applied here: `JUST FALSE` for failed "if" conditions in ss 12(2), 13(1), 56B(1) and Rules s 4B; s 43(b) ("cannot ... bring or continue"); s 37(1) ("not admissible"); ss 49(1), 52(1), 56C(1) ("not to be treated"); s 75(4) ("must not ... unless"); s 64 and s 63(2) ("not entitled"); s 39(i)(iii), (ia)(iv) ("not available"); Rules s 26(3)-(5) and s 30(2) step 3 (a defined term: a payment outside it counts for nothing, `JUST 0`). `NOTHING` where the text is silent or out of reach: s 43 before any acceptance; s 37 for other documents, criminal proceedings and proceedings giving effect to the Act; s 49(3) for a liability insurance contract ("nothing in this Act prevents"); Rules s 26(6) (formula lost); s 40(1) for an offer stated shorter than the Act allows; s 54 where no direct personal response was asked for, or for an institution s 16(1)(c) does not name. The enumerated answers of the "Can I apply", scope, responsibility and status questions carry their own reasons.

Fork lines (case-by-case sites, for the reviewer to overrule):

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | s 20(1)(e) "in the period of 12 months before the scheme sunset day" | `Can I apply for redress question` | the sunset day (1 July 2028) itself is not in the period: an application that day is not barred by (e) | the bar runs through the sunset day, since the Act ceases at its end and no determination could follow |
| F2 | s 13(1) "eligible ... if", with s 13(2) leaving room for rules | `Am I eligible for redress question` | `JUST FALSE` when s 13(1), s 61 and Rules s 4B all fail | `NOTHING` (rules made later could prescribe more) |
| F3 | s 73(2)(a) "before the day specified in the notice"; s 34(3)(aa) has the notice specify a period | `Am I in time to apply for review question` | in time on the last day of the review period | in time only before the specified day, i.e. by the day before it |
| F4 | s 12(2) "entitled ... if", with s 12(3) | `Am I entitled to redress question` | `JUST FALSE` when (a)-(e) fail | `NOTHING` (Part 3-1 and rules may make a person entitled otherwise) |
| F5 | s 54(1) "If ... given a notice ... then ... must take reasonable steps" | `Must the institution give me a direct personal response question` | `NOTHING` where no response was asked for, or for a s 164A or 164C institution | `JUST FALSE` (a duty whose "if" is unmet) |
| F6 | s 43 before acceptance | `Can I still sue for the abuse after accepting redress question` | `NOTHING` (s 43 not engaged) | `JUST TRUE` (nothing in the Act stops a claim) |
| F7 | s 167(2)-(4) heads that may overlap | `Must I pay back an amount paid to me question` | the largest head, capped at the amount paid | the heads added, capped at the amount paid |
| F8 | a birthday or payment date of 29 February | `the anniversary` in `nrs-dates.l4` | 1 March in a year with no 29 February | 28 February |
| F9 | Acts Interpretation Act s 36(2), a last day on a Saturday, Sunday or holiday | the "by when" questions | the last day as counted, not moved | move to the next working day (needs a holiday calendar) |
| F10 | s 37(2) "Subsection (1) does not apply if ... for the purposes of giving effect to this Act" | `Can my redress documents be used as evidence question` | `NOTHING` (the general law of evidence decides) | `JUST TRUE` |
| F11 | s 40(1) "at least 6 months", an offer stating less | `By when must I accept my offer question` | `NOTHING` (the offer does not meet the Act) | the 6-month minimum governs |
| F12 | s 30(4) step 2 "the difference between" (a) and (b) | `s 30(4) -- the Commonwealth's share` | the absolute difference (it is never negative on these facts) | (a) less (b), which would be negative |
| F13 | Rules s 15(2) "at least 4 months before", "at least 3 months, but not more than 6 months, before" | `Has the Operator given me my notice before I turn 18 question` | measured to the same day-number in the earlier month (end of month where none) | measured as Acts Interpretation Act periods ending on the birthday |

## Scope

**In:** ss 6 (definitions used), 12, 13, 14, 15 (with Rules ss 11, 12), 16, 17, 19, 20, 21 (with Rules s 15), 22, 24(4), (7), 26(1), 28, 29(1)-(3), 30 (with Rules s 26(3)-(5)), 31(2), 34(4)-(10), 37, 39 (in the descriptions), 40, 42, 43, 45, 48(1D) (with Rules s 33(3)), 49, 50, 51(2)-(3), 52, 53, 54, 56B, 56C, 56D, 58, 59, 60, 61, 63, 64, 73, 75(4), 76(3), 78, 167, 193(1); Rules ss 4B, 6.

**Out, and why:**
- Chapter 1 and Part 2-1 (ss 1-10: preliminary, objects, outlines, establishment, the Operator, guiding principles): machinery; s 10's principles are named where s 75(4)(b) uses them.
- ss 23, 25, 27, 35, 35A, 36, 41, 41A, 44, 44A, 46, 46A, 46B, 79 (notices to institutions and funders of last resort; information from institutions; State laws not preventing disclosure): duties owed to institutions, not to the survivor; s 26(2) lets the Operator decide without an institution's information.
- s 29(2)(b)-(m), s 30's institutions' shares beyond one institution, s 31(3) and Rules ss 19-25, 27-29A (sharing costs among institutions and funders of last resort): the survivor's amount is encoded through s 30(5); the shares among several institutions need the Rules formulas lost from the deposit (finding 10) and are given as inputs in the internal `s 30(5)` function, which the cases exercise for two institutions.
- s 29(4)-(7) and Rules s 17 (revocation): a later layer could ask "can my determination be revoked?"; s 29(5) (no revocation after acceptance) is noted in the descriptions.
- ss 32, 33, 55, 56 (the assessment framework, guidelines, the direct personal response framework and its principles): instruments not deposited, or guidance with no threshold to compute.
- s 47, s 48(1)-(1C), (2), s 51(1), (3A)-(4) (payment to an administrator, instalments): administration of payment; the person's own question (where does my payment go) is in Rules s 33 and named in the death question.
- s 57 (outline), s 62 (outline), s 63(3)-(8) (the special assessment procedure, specified advisors, weight of advice): the Operator's process; its outcome is the s 63(5) input.
- ss 65-71 (security notices: issue, revocation, effect): ministers' powers; the person's position is the s 64 and s 20(1)(b) inputs.
- Part 3-3 (ss 71A-71Z: reassessment of determinations made before the 2021 amendments): a separate procedure for older determinations; a later layer could take it.
- ss 72, 74, 75(1)-(3), 75A-75C, 76(1)-(2), 77 (review procedure): the reviewer's process; the person's questions (am I in time, can it go down, what happens to my offer) are in.
- Part 4-2 (nominees), Part 4-3 (protected information), Chapter 5 (participating institutions, groups, jurisdictions), Chapter 6 (funding, funders of last resort, debt recovery other than s 167), Chapter 7 except ss 167 and 193 (application, rules, notices, delegation, protected names, reviews of the scheme), Chapter 8 (transitional): machinery, or other parties' liabilities.
- Rules ss 8-10 (equal responsibility of government institutions, defence cadets, child migrants): they make institutions equally responsible and shape cost sharing; the survivor's eligibility does not turn on them (Rules s 4B is in). Rules ss 15B, 16-17, 31-31A, 34-54A: notices, revocation, acceptance-document contents, protected information.

## What the Act turns out to say

1. **The scheme start day rests on text the Act says is not part of it.** Section 6 makes it "the day this Act commences"; s 2 item 1 gives 1 July 2018 only "if this Act receives the Royal Assent before 1 July 2018", and the answer ("1 July 2018 (paragraph (a) applies)") is in column 3, which s 2(2) says "is not part of this Act". The date of Royal Assent is not in the deposit. 1 July 2018 is taken. Asserted.
2. **The scheme ends at the end of 1 July 2028** (s 193(1)(a), the tenth anniversary), the deposited Rules prescribing no later day. The last 12 months run from 1 July 2027, so the last ordinary day to apply is 30 June 2027. Asserted.
3. **The sunset day itself falls outside the s 20(1)(e) bar** (fork F1): "in the period of 12 months before the scheme sunset day" ends with 30 June 2028, so an application on 1 July 2028 is not barred by (e), though the Act ceases at the end of that day and the Operator could not determine it. Asserted on the literal reading.
4. **A child born on or after 1 July 2010 has no day on which to apply.** Section 20(1)(c) bars a child "who will not turn 18 before the scheme sunset day"; by the time such a person turns 18 the last 12 months have begun (s 20(1)(e)), so only the Operator's exceptional-circumstances determination opens the scheme to them. Asserted (born 1 July 2010: none; born 30 June 2010: can apply as a child).
5. **The review deadline is drafted two ways** (fork F3). Section 73(2)(a) requires an application "before the day specified in the notice", but s 34(3)(aa) requires the notice to "specify the review period", not a day, and for an approved application s 34(4) makes the review period the acceptance period, within which s 42(3) requires acceptance "before the end". Read as: in time on the period's last day. Asserted (30 March in time, 31 March late).
6. **Section 30(4) says "the difference between" without a sign** (fork F12). With more whole years counted to the determination than to the application, (b) is never less than (a), so the Commonwealth's share is (b) less (a). And s 30(2) step 4's "whole years since the relevant prior payment was paid" names no end day: read as the day of the determination. Asserted (Commonwealth's share 394.58; and 120 where the institution's share is nil at the determination).
7. **The Commonwealth bears the inflation while the application is processed**, so the survivor's payment depends only on the years from the earlier payment to the application (s 30(4) note 1). Asserted: deciding a year later does not change the 79,232.78.
8. **An advance payment becomes a debt on a deemed decline too.** Section 167(4A)(b)(ii) applies where the person "declines the offer under section 45", and s 45(2) is a person "taken to have declined". Encoded so ("declined, or taken to have declined"). Asserted.
9. **"Sentenced to imprisonment for 5 years or longer" (s 63(1)) does not say whether sentences add up**; the length of the sentence is asked. Section 75(4) protects only the redress payment from reduction on review, not the counselling component.
10. **The Rules' formulas are missing from the Rules deposit.** Rules ss 21(1), 23(2), 24(1), 25(1), 26(6) and 27(3) each end "using the following formula:" with nothing after it: the Word equation images were dropped and the Rules subject has no formulas sidecar. Shares among several responsible institutions, and the split of a payment made for several institutions (s 26(6)), cannot be worked from the deposit; they are inputs or `NOTHING`. A sidecar like the Act's would let a later layer compute them.
11. **The Act's simplified outline (s 4) still says the scope excludes "a State that is not participating"**, while s 61 brings in abuse there for which a Commonwealth or participating Territory institution is primarily responsible. The operative rule is encoded. Asserted.
12. **Rules s 15(2)'s window can open before the application.** A child who applies 5 months before turning 18 meets "at least 4 months before", but the 6-to-3-month window has already opened; the notice is then due between the application and 3 months before the birthday. Encoded (the PROVIDED guard compares with a window start before day 0).
13. **A direct personal response is "not available" from a defunct institution** (s 39(i)(iii), (ia)(iv)), and s 16(1)(c) names no response from a s 164A or s 164C listed institution that is not partly participating. Asserted.

## Raised in the ledger

Nothing. The assessment framework (s 32), which gives every survivor's maximum redress payment and counselling amount, is the next instrument a survivor needs; it is not deposited. A formulas sidecar for the Rules deposit (finding 10) would complete the cost-sharing rules. The ledger `subjects/au/requirements.jsonl` was not changed.

## Links

- **National Redress Scheme for Institutional Child Sexual Abuse Rules 2018** (`subjects/au/national-redress-scheme-for-institutional-child-sexual-abuse-rules-2018/`): deposited, encoded here as far as the survivor meets it; it has no encoding folder of its own.
- **Territories Stolen Generations Redress Scheme (Facilitation) Act 2021** (`subjects/au/territories-stolen-generations-redress-scheme-facilitation-act-2021/`): a related redress scheme.
- The State civil liability and limitation Acts set the civil claim that acceptance releases (s 43); no link is made in code, as the stable `l4` cannot import across subjects.

## What would need doing before this is worth relying on

- An independent test pass against the text, and a lawyer's look at the fork lines F1-F13.
- The assessment framework deposited, so that the maximum amount and the counselling amount are worked out rather than entered.
- A formulas sidecar for the Rules deposit, then cost sharing among several institutions (Rules ss 21-25, 27) and Rules s 26(6).
- Part 3-3 (reassessment) as a further layer, for people whose determinations predate the 2021 amendments.
- A holiday calendar if last days are to be moved under the Acts Interpretation Act s 36(2).
- Checking that the deposited compilations (Act 28 September 2024; Rules 19 February 2025) are still current, and whether a rule has since prescribed a later scheme sunset day.
