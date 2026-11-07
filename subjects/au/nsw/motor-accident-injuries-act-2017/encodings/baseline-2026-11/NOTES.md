# Motor Accident Injuries Act 2017 (NSW) -- baseline encoding, the person injured in a motor accident

> **Warning.** The texts encoded here are taken from the Open Australian Legal Corpus, collected on 10 March 2025: the
> Act as at 1 April 2023 and the Motor Accident Injuries Regulation 2017 as at 22 September 2023. They are unofficial
> and may be out of date: amendments after those versions are missing. Check legislation.nsw.gov.au before relying on
> anything here.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words, including a period the text fixes; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Three
regulative rules (the claim within 3 months with the late claim under `LEST`, s 6.13(1), (3); the insurer's notice on
liability, s 6.19; the claimant's compliance with an insurer's requirement, ss 3.14(2), 3.15(7)), each run by
`EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except
in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is Part 3 (statutory benefits) and the
claim steps around it: the 28-day and 3-month steps of s 6.13, the insurer's 4-week and 9-month notices of s 6.19, and
the 14-day and 7-day steps of ss 3.14 and 3.15. The Act is large (11 Parts); Part 4 (damages), Part 7 (disputes) and the
rest are left for other encodings (see Scope). The Motor Accident Injuries Regulation 2017 is a separate subject
(`subjects/au/nsw/motor-accident-injuries-regulation-2017/`); the clauses that set Part 3's numbers and terms (cl 4, 7,
8A) are encoded here, because the stable `l4` imports only from the same folder.

## Edition

- **Act:** Motor Accident Injuries Act 2017 No 10, corpus document `nsw_legislation:2023-04-01/act-2017-010` (in force
  1 April 2023), deposited at `../../registers/source-bundle/act-2017-010.txt` (sha256 94550e72...16a9 with LF line
  endings, as recorded in its meta.json), from the Open Australian Legal Corpus (collected 10 March 2025) because
  legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Regulation:** Motor Accident Injuries Regulation 2017, corpus document `nsw_legislation:2023-09-22/sl-2017-0498`,
  deposited at `../../../motor-accident-injuries-regulation-2017/registers/source-bundle/sl-2017-0498.txt` (sha256
  b05474c7...97f6). cl 4 (threshold injuries), cl 7 (minimum weekly amount) and cl 8A (weekly payments before a late
  claim) are encoded. The two versions are six months apart; nothing in the clauses used depends on the gap.
- **Not deposited:** the Authority's orders adjusting the maximum weekly amount (s 3.9) and the indexation factor
  (s 3.22), the Motor Accident Guidelines, the Workers Compensation Act 1987, the Social Security Act 1991 (Cth) (retiring
  age), the Road Transport Act 2013 (major offences), the Motor Accidents (Lifetime Care and Support) Act 2006 and the
  Motor Accident Injuries Amendment Act 2022. What they decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once to confirm that failures are reported).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `maia-dates.l4` | 0 | 0 | 0 | 0 |
| `maia-claims.l4` | 0 | 0 | 0 | 0 |
| `maia-benefits.l4` | 0 | 0 | 0 | 0 |
| `maia-cases-benefits.l4` | 0 | 0 | 193 | 193 |
| `maia-cases-claims.l4` | 0 | 0 | 61 | 61 |

Every expected value was worked by hand from the text, with the edges: the last day of each period and the day after
(13, 26, 52, 78, 104, 156 and 260 weeks; 28 days; 3 months, across a short February; 9 months; 3 years; 14 and 7 days;
90 days; 28-day certificates); 61% and 62% at fault; 10% and 11% impairment, and 6% + 6% not added (s 1.7); age 14 and
15 (earner), 15 and 16 (s 3.28), 17 and 18 (s 3.8); 13 and 26 weeks of work; 6 hours and 6 months (s 3.26); a weekly
payment just under and just over the maximum; the minimum floor raising a small payment, and the floor above the
ceiling; the retiring age before and after the accident; a Regulation cl 8A accident on each side of 1 April 2023.

## Seat

**The injured person**: the person injured in a motor accident who claims, or may claim, statutory benefits (and, for
the questions on claims for damages, damages). For funeral expenses (s 3.4) the seat is the legal personal
representative of the person who died, or the person who paid or must pay the funeral. Every exported question is one
that person would ask ("Are statutory benefits payable to me?", "Was I an earner?", "Am I entitled to weekly payments for
this day?", "How much is my weekly payment?", "By what day must I claim?", "Is my claim in time?", "Is my insurer taken
to have accepted liability?", "Can my insurer suspend my payments?"). The insurer is not given a seat in this baseline,
though the Act puts duties on it (ss 3.19, 6.19); an insurer seat could be added. Officials (the Authority, the
Commission, the court) get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulation's cl 4, 7 and 8A are brought
  in. The maximum weekly amount is an input (the Act's $3,853 as adjusted by the Authority's yearly orders, which are not
  deposited); a substitution changes the answers.
- **The actors the text names.** Followed: the injured person (claimant), the insurer, the relevant insurer, the
  Nominal Defendant, the Lifetime Care and Support Authority, the legal personal representative.
- **Judgments answered conditionally.** Followed: reasonableness and necessity of treatment and care, "full and
  satisfactory explanation" (s 6.2), the insurer's or Commission's determinations (permanence, s 3.21; contributory
  negligence percentage, s 3.38(3); earning capacity, s 3.16) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: earner (Sch 1 cl 2), the entitlement periods
  (s 3.5), threshold injury (s 1.6, Regulation cl 4), the impairment threshold (s 1.7), "mostly at fault" (61%), the
  uninsured vehicle (s 3.36(3), in the input's gloss), dependants (s 3.26(5)), the maximum weekly payment period
  (s 3.12) are worked out; retiring age, recognised psychiatric illness, serious driving offence, workers compensation
  and "pre-accident weekly earnings" (an averaging the person states) are asked. The weekly-payment question asks
  "earner" and "only threshold injuries" as yes/no, each pointing to the question that works it out (to keep that
  question's inputs within reach).
- **One case.** One motor accident, one injured person, one day (or week) asked about.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 1.6 and Regulation cl 4 (threshold injury); s 1.7 (impairment threshold); ss 1.8-1.10 (application); s 3.1
(entitlement); s 3.2 (relevant insurer) with s 3.45(2); s 3.4 (funeral expenses); s 3.5 (entitlement periods); ss 3.6-
3.8 (weekly payment rates, caps and floors); s 3.9 (maximum, an input) and s 3.10 with Regulation cl 7 (minimum); s 3.11
(52-week cessation); s 3.12 (maximum weekly payment period); s 3.13 (retiring age); ss 3.14, 3.15(3)-(7) (requirements,
certificates of fitness, suspension); s 3.18 (notice of work, with the penalty); s 3.19 (notice before stopping or
reducing, and recovery); s 3.21 (residence outside Australia); ss 3.24-3.29, 3.31(2), 3.32, 3.33 (treatment and care, and
paid domestic services); s 3.35(1), (6), (8) (workers compensation); s 3.36 (at-fault owner or driver of an uninsured
vehicle); s 3.37 (serious driving offence); s 3.38 (contributory negligence after 52 weeks, and the cases where a finding
must be made); s 3.40(1)(a), (3)(a) (damages recovered end weekly payments); Sch 1 cl 2 (earner); s 6.2 (in the
explanation inputs); s 6.13 with Regulation cl 8A; s 6.14(2), (3); s 6.19; Sch 4 cl 12, 15 and 16 (application of the
2022 amendments, as an input).

**Out, and why:** ss 1.1-1.3 (name, commencement, objects), 1.10A, 1.11, 3.3 (arrangements between insurers), 3.16,
3.41, 3.45(1), (3)-(5), Parts 9-11 and Schedules 2-4 otherwise: machinery. s 1.5 (owner): the person states whether they
owned the vehicle. s 3.17, 6.5, 6.6, 6.27: suspension is one input to the weekly-payment question; the duties themselves
are left to a later encoding of Division 6.2. s 3.20 and s 3.43 (refunds of overpayments): a Commission direction or a
debt, nothing for the person to compute beyond the subtraction. s 3.22 (indexation): the formula is missing from the
deposited text (finding 1) and the factors are Authority orders; the indexed amounts are inputs. s 3.23 (fortnightly):
no question turns on it. s 3.30 (rates paid to providers): Gazette orders and Part 8 maxima, not deposited. s 3.34
(effect of death): the seat is the living injured person. s 3.39 (mental harm): Civil Liability Act 2002 Part 3, a
separate subject. s 3.40(1)(b), (2), (3)(b) (deductions from damages) and s 3.42 (no lump-sum redemption): stated in
comments; no fact changes them. s 3.44: about the effect of determinations on a damages claim. Sch 1 cl 3-8 (how
earnings and capacity are measured): the person states the amounts. Part 2 (insurance), Part 4 (damages), Part 5, Part 6
Divisions 6.2, 6.3 (verification, under the Guidelines), 6.5, 6.6 and ss 6.10, 6.12, 6.14(4)-(8), 6.15-6.18, 6.20-6.28,
Part 7 (dispute resolution) and Part 8 (costs): outside the focus; candidates for further encodings.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 3 months" (s 6.13(1)), "9 months" (s 6.19(2)), "12 months" (s 3.13), "3 years" (ss 6.13(3), 6.14(2))
  -- `plus months` -- the same day of the month that many months later, or that month's last day where shorter (30
  November -> 28 or 29 February) -- the Interpretation Act 1987's counting (not deposited) might give another end day.
- **F2** "more than N weeks after the motor accident" (ss 3.11, 3.12, 3.28, 3.38) and the entitlement periods (s 3.5)
  -- `is more than ... weeks after` -- a day later than the accident day plus 7N days; the periods count from the day
  after the accident, so day 1-91 is the first period -- counting from the accident day itself (one day earlier).
- **F3** s 3.1(1) "If ... a motor accident in this State" -- `the Part 3 gate` -- an accident outside NSW answers
  `JUST FALSE` (an "if" condition) -- `NOTHING`, since other Parts or other States' schemes may still apply.
- **F4** s 3.37 -- `the Part 3 gate` -- a charge pending or a conviction on the day asked about bars benefits; an
  acquittal or discontinuance restores them (from the charge date) -- distinguishing the s 3.37(2) proviso (a guilty
  plea to another serious driving offence) as a separate fact.
- **F5** s 3.2(2)(a), (b), (c) -- `Who pays my statutory benefits` -- (a) read as one vehicle involved, which had
  cover; with several vehicles and an at-fault vehicle without cover, the Nominal Defendant (as the Act's note says) --
  (a) read as "only one of the vehicles involved had cover", which would name that vehicle's insurer.
- **F6** Sch 4 cl 15, 16 -- the s 3.11 and s 3.28 bars, the s 3.38 reduction, s 6.19 -- for an accident before the 2022
  amendments commenced, the encoding applies the current text where the old and new texts must agree (after 52 weeks)
  and answers `NOTHING` between 26 and 52 weeks and for s 6.19 -- the amending Act's items [16]-[51], [32], [33] might
  reach other sections, or the old text might differ in other ways.
- **F7** s 3.12(3) -- `Am I entitled to weekly payments for this day` -- a damages claim withdrawn, settled or finally
  determined after 104 weeks is no longer "pending", so the 104-week period applies and has passed -- reading "the
  maximum weekly payment period ends" as ending only on that day.
- **F8** ss 3.6(1), 3.7(1) "An earner who ..." -- `Am I entitled to weekly payments for this day` -- a non-earner in
  weeks 1-78 answers `NOTHING` (a grant limited by its own words; the Act's note, which says only earners are entitled,
  is not part of the Act, s 1.4(2)) -- `JUST FALSE`, as the note says.
- **F9** ss 3.7(2), 3.8(2) "total ... partial loss" -- `the weekly payment before any reduction` -- total when the
  greater of post-accident earning capacity and earnings is 0 -- total whenever the person cannot do their old work.
- **F10** ss 3.6-3.8 (3) and (4) -- `the weekly payment before any reduction` -- where the floor (the lesser of the
  minimum and the pre-accident amount) is above the ceiling (the maximum less post-accident earnings), `NOTHING` -- the
  floor wins, or the ceiling wins.
- **F11** s 3.19(5), (6) -- `How many weeks notice must my insurer give` -- a discontinuation for a return to work or a
  lower rate needs no notice, like a reduction -- (5) and (6) speak only of reductions, so a discontinuation for those
  reasons would need notice.
- **F12** s 3.18 -- `Must I tell my insurer about my work` -- no listed change: `JUST FALSE`; not receiving weekly
  payments: `NOTHING` -- both `JUST FALSE`.
- **F13** s 3.28(1)(a) "over 16 years of age" -- `the s 3.28 bar` -- 16 or more in whole years -- older than 16 only
  from the day after the 16th birthday, or 17 or more.
- **F14** s 3.31(2) "An insurer is not required to pay" -- `Can I get statutory benefits for this treatment and care
  expense` -- `JUST FALSE` -- `NOTHING`, since s 3.31(3) lets the insurer pay anyway.
- **F15** s 3.15(3)(b), (4) -- `Does my certificate of fitness count for this day` -- a certificate stating more than
  28 days without special reasons counts for its first 28 days, the rest `NOTHING` -- void altogether, or good for its
  whole period.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| ss 3.1, 3.6-3.8, 3.24, 3.26 | the injured person | right to statutory benefits | MAYBE BOOLEAN questions |
| ss 3.11-3.13, 3.21, 3.28, 3.33, 3.35, 3.36, 3.37, 3.40 | the injured person | no-right (bars) | `JUST FALSE` |
| s 6.13(1), (3) | the claimant | duty with a deadline (3 months; late claim with explanation, 3 years or none) | MUST rule with a MUST under LEST |
| s 6.13(2), Reg cl 8A | the claimant | no-right to weekly payments before a late claim, unless permitted | `JUST FALSE` |
| s 6.19 | the insurer | duty with a deadline (4 weeks, 9 months); deemed acceptance | MUST rule, breach read as deemed acceptance |
| ss 3.14(2), 3.15(7) | the claimant; the insurer | duty with a deadline; the insurer's power to suspend | MUST rule; power when breached and continuing |
| s 3.18 | the claimant | duty (immediately), offence | `Must I tell my insurer about my work`, penalty question |
| s 3.19 | the insurer | duty (notice); the claimant's right to recover | notice and recovery questions |

## What the Act turns out to say

1. **The indexation formula is missing.** s 3.22(1) ends "in accordance with the formula--" and goes straight to
   "where-- A is ... B is ... C is ...": the formula itself (an image in the official text) was lost in the corpus
   conversion. Indexed earnings are therefore inputs. A `act-2017-010.formulas.md` sidecar from the authorised rendering
   would restore it.
2. **The 2022 amendments cannot be placed from the deposited text.** Sch 4 cl 15 and 16 say that items [16], [18],
   [21], [23], [26], [27], [51] and [32], [33] of the 2022 amending Act do not apply to accidents before they commenced,
   under the heading "Statutory benefits after 26 weeks". The text gives neither the commencement day nor what those
   items amended; the Regulation's cl 8A(4) uses 1 April 2023 for its own purposes. Asked as a fact (fork F6); asserted.
3. **A late claim excused under s 6.13(3) still loses back pay.** Regulation cl 8A permits payment before the claim only
   for a claim made within 3 months with an explanation; a claim excused under s 6.13(3) (made within 3 years, or for a
   death or over 10%) gets weekly payments only from the day it is made. Asserted.
4. **The minimum can exceed the loss.** ss 3.6(4)-3.8(4) set a floor of the lesser of the minimum (2.5% of the maximum,
   Regulation cl 7, about $96 on the Act's $3,853) and the pre-accident amount, without regard to the size of the loss:
   a person who lost $100 a week gets $96.325, not $95. Where post-accident earnings are close to the maximum the floor
   rises above the ceiling and the two subsections cannot both hold (fork F10). Asserted.
5. **s 3.2 has a gap.** With more than one vehicle and an uninsured at-fault vehicle, (b) names an insurer that does
   not exist and (c) "in any other case" does not obviously reach the case; only the note (not part of the Act) says
   the Nominal Defendant pays. Fork F5.
6. **The heading of s 3.38 says "after 12 months"; the text says 52 weeks.** 52 weeks is 364 days, a day or two short of
   12 months. The text is encoded.
7. **The earner requirement rests on a note.** ss 3.6 and 3.7 grant weekly payments to "an earner who ..."; that only
   earners are entitled is said in a note, which s 1.4(2) excludes from the Act. Fork F8.
8. **s 3.28 and s 3.11 treat children differently.** An at-fault injured person under 16 (fork F13) keeps treatment and
   care after 52 weeks but loses weekly payments (s 3.11 has no age limit). Asserted.
9. **s 3.19(5), (6) speak only of reductions**, though (4) brings in discontinuations; whether a return to work allows
   payments to stop without notice is open. Fork F11.
10. **The Act does not give its commencement day.** s 1.2 leaves it to proclamation; Sch 4 cl 12 ("not before 1
    December 2017") points to it. Asked as a fact.

## Questions (exported)

`maia-benefits.l4` (16), in the Act's order: `Is my injury a threshold injury`, `Are statutory benefits payable to me`,
`Who pays my statutory benefits`, `Was I an earner`, `Which entitlement period is this day in`, `Am I entitled to weekly
payments for this day`, `How much is my weekly payment`, `Must a finding of contributory negligence be made against me`,
`How many weeks notice must my insurer give`, `How much can I recover for short notice`, `Must I tell my insurer about
my work`, `What is the most I can be fined for not telling my insurer`, `Can I get statutory benefits for this treatment
and care expense`, `Can I get statutory benefits for paid domestic services`, `Can I get statutory benefits for funeral
expenses`, `Do funeral expenses include transporting the body there`.

`maia-claims.l4` (11): `By when must I claim statutory benefits`, `By when must I claim to be paid weekly payments from
the start`, `Are weekly payments payable for the time before my claim`, `Is my claim for statutory benefits in time`,
`By when must my insurer tell me whether it accepts liability`, `Is my insurer taken to have accepted liability`, `By
when must I give my insurer what it asked for`, `Can my insurer suspend my weekly payments for this`, `Does my
certificate of fitness count for this day`, `By when must I claim damages`, `Can I make my claim for damages`.

## Before relying on it

- Replace the corpus texts with the current official texts from legislation.nsw.gov.au and re-check every quotation;
  restore the s 3.22 formula (finding 1).
- Deposit the Motor Accident Injuries Amendment Act 2022 (or the pre-2023 text) to settle fork F6, and the Authority's
  orders for the maximum weekly amount and indexation.
- Have a lawyer review the forks, especially F5, F8, F10 and F11.
- Encode Part 4 (damages), Divisions 6.2 and 6.4 beyond s 6.19, and Part 7 (internal and merit review), and link to the
  Civil Liability Act 2002 and Workers Compensation Act 1987 baselines.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
