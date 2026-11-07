# Motor Accidents Compensation Act 1999 (NSW) -- baseline encoding, the injured person (legacy CTP scheme)

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 16 June 2022). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Seven regulative rules (ss 48, 50, 70(4)/73(4)/
34A(2)/76(2) in two steps, 81, 85B, 110), each run by `EVALTRACE` inside an exported question that takes only plain
facts, through one helper (`the rule was kept`). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No
pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Focus: **legacy**. The Act is the CTP scheme for
motor accidents from its commencement in 1999 until the Motor Accident Injuries Act 2017 took over (s 3AA, 1 December
2017). Claims under it are now mostly made, settled or out of time; what a person still meets is the claims machinery
(late claims, the insurer's two months, the court time limit and leave, withdrawal and reinstatement) and the damages
rules. The Act is large (313,000 characters); the Parts a claimant meets are encoded, the rest is listed below as out.

## Edition

- **Act:** Motor Accidents Compensation Act 1999 No 41, corpus document `nsw_legislation:2022-06-16/act-1999-041` (in
  force 16 June 2022), deposited at `../../registers/source-bundle/act-1999-041.txt` (sha256 871d8338...b42fe74b0a as
  committed), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited, so asked as inputs:** the Authority's indexation orders under s 146 (the current s 125 weekly
  maximum and s 134 non-economic loss maximum), any Gazette order varying the $5,000 in s 51, the regulations (a
  discount rate under s 127, a different s 50 period, s 33(4)(d) exclusions, s 130(c) amounts), the Motor Accidents
  Medical Guidelines, the accident notification form's own period (s 48(c)), the Civil Procedure Act 2005 s 101 rate,
  the Australian Statistician's average weekly earnings (s 141B), and the commencement dates of the Act and of Part 1.2.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `mac-dates.l4` | 0 | 0 | 0 | 0 |
| `mac-claims.l4` | 0 | 0 | 0 | 0 |
| `mac-damages.l4` | 0 | 0 | 0 | 0 |
| `mac-cases-claims.l4` | 0 | 0 | 153 | 153 |
| `mac-cases-damages.l4` | 0 | 0 | 68 | 68 |

Every expected value was worked by hand from the text, with the edges: the 28th and 29th day (ss 48, 70); the 10th and
11th day (s 50); the last day of the insurer's two months and the day after, for each step and each ground (ss 34A, 70,
73, 76); the last day of three months (ss 81, 85B, 110) and the day after; six months from 31 August in a leap and a
common year (s 72); a month from 31 January into a leap February (s 82); recovery on the third anniversary and the day
after (s 82(4)(b)); a s 85B direction on the last day of the 2 years 6 months, on the last day of the 2 months after, and
a day later; the s 109 pause with a referral before, on and after the last day; damages exactly 25% of the s 134
maximum and one dollar under (ss 85B(7), 109(3)); impairment of exactly 10% (s 131); earnings one dollar over the s 125
maximum; a judgment exactly 20% over the best offer and one dollar more (s 137(4)(a)(iv)); 5.9 and 6 hours, 40 and 50
hours a week (s 141B); treatment expenses at, under and over the s 51 maximum.

## Seat

**The injured person** (the claimant), or the relative claiming for a death, or a parent for an injured or killed child.
Every exported question is one that person would ask ("Does the scheme cover my claim?", "Can I claim if no one was at
fault?", "Does my child have the special entitlement?", "Can I claim against the Nominal Defendant?", "Am I entitled to
early payment?", "By when must I report, notify and claim?", "Has the insurer lost the right to reject my late claim?",
"Has the insurer admitted liability?", "By when must it make me an offer?", "What is the last day to go to court?", "Is
my claim taken to be withdrawn?", "Can I get damages for pain and suffering, and how much at most?", "Do I get
interest?"). The CTP insurer and the owner or driver have duties under the Act (ss 77-87) and could be given seats of
their own; none is added here. Officials (the Authority, the Nominal Defendant as an agency, the Commission, medical
assessors, the court) get no seat: what they do is encoded as what it means for the claimant.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, but none of those instruments is deposited:
  every figure an order or regulation may replace is an input, with the Act's own figure named in the `@desc`.
  Departure, recorded: the base figures ($2,500, $284,000) were set in 1999 and have been indexed every year since, so
  a person must supply the current amount.
- **The actors the text names.** Followed: the claimant, the injured person, the insurer, the Nominal Defendant, the
  owner and the driver, the Commission, the medical assessor, the court.
- **Judgments answered conditionally.** Followed: fault, a full and satisfactory explanation, a serious offence that
  contributed materially (ss 7K, 47A), the Commission's assessment of a dispute, reasonable excuse, the court's leave,
  the court's percentage of contributory negligence, reasonableness of an offer (s 137) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "blameless motor accident" (s 7A), "child"
  (s 7J(6)), "non-economic loss" and "motor accident" (s 3), "motor accident insurance cover" (s 3B(2), in the `@desc`),
  "serious offence" (ss 7K(3), 47A(2)), "alcohol or other drug-related offence" (s 138(7), in the `@desc`) are worked out
  or glossed; "road related area", "registration", "work injury claim" (Workers Compensation Act 1987 Part 5) and "act
  of terrorism" (s 15A(2)) are asked.
- **One case.** One motor accident, one claimant's claim.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In** (`mac-claims.l4`): ss 3, 3AA, 3A, 3B, 67, 122 (whether the scheme applies); Part 1.2: ss 7A-7E, 7I (blameless
accidents), ss 7J, 7K, 7L, 7P (children; s 7F and s 7L-7P(2) on contributory negligence); ss 33, 34, 34A, 35A (the Nominal
Defendant); Part 3.2: ss 46A, 47, 47A, 48, 50, 51 (early payment of treatment expenses and lost earnings); s 70 (police
report), s 72 (time for claims), s 73 (late claims), s 76 (non-complying notice), with the shared "loses the right to
reject" machinery; s 81 (notice on liability); s 82 (offer of settlement); s 85(4), s 86(4) (consequences of not
co-operating); s 85B (particulars, withdrawal and reinstatement); s 108 (certificate first); s 109 (three years, the
pause, leave); s 110 (notice to commence proceedings).

**In** (`mac-damages.l4`): ss 122, 123 (in comments); s 125 (earnings maximum); s 126 (in a comment); s 127 (discount
rate); s 130 (reduction for payments); ss 131-134 (non-economic loss threshold and maximum); s 136 (in a comment); s 137
(interest); s 138 (contributory negligence) with ss 83(5), (6), 84A(3), (4); s 140 (voluntary assumption of risk); s 141
(in a comment); s 141A, 141B, 141C, 142, 144 (kinds of damages).

**Out, and why:**
- Chapter 2 (compulsory insurance, policies, premiums), Parts 7.1-7.3 (insurers), Chapter 8 (administration), Chapter 9
  (miscellaneous): the scheme's machinery, addressed to insurers and the Authority, not to the claimant.
- ss 35 (NSW-registered trailer on an unregistered vehicle), 36-41 (the Nominal Defendant's joinder, fund and recovery
  from owners and drivers): s 39 (recovery from the owner or driver) is a seat for the owner or driver, not the claimant;
  s 35 is rare and left for a later pass (fork F5).
- Part 3.1 (guidelines), Part 3.3 (payments to hospitals and bulk billing), Part 3.4 (medical assessment procedure):
  administered between insurers, providers and the Authority; s 61 (assessments conclusive) is noted in a comment.
- ss 77-80, 83, 84, 84A, 85(1)-(3), 85A, 86(1)-(3), 87 (the duties of the insured, the insurer and the owner or driver):
  the claimant's consequences (ss 85(4), 86(4), 85B) are encoded; the insurer's payment duties are reflected in s 130 and
  the contributory negligence question; the insured's and owner's duties belong to their seats.
- Part 4.4 (settlement conference, assessment, s 94A costs, s 95 binding assessments, s 96 special assessments) beyond
  the referral rules: procedure of the Personal Injury Commission, which turns on the Personal Injury Commission Act 2020
  and its rules (not deposited here).
- ss 111-121 (remitter, agency, proceedings against the insurer, disclosure, fraud, claims register, advertising) and
  Chapter 6 (costs): procedure and regulation-set costs (regulations not deposited).
- s 146 (indexation) is machinery; its effect is the inputs for the current maxima.
- Schedule 5 (savings and transitional): read for the dates (finding 9); not encoded.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within N months after", "within 28 days after" -- `mac-dates.l4`, every date question -- the last day is the
  same day of the month N months later (or that month's last day where shorter), or 28 days later, and the whole of it
  counts; the day itself is not counted -- the Interpretation Act 1987's counting rules (not deposited) might give another
  last day in a short month.
- **F2** ss 67(1), 122(2) -- `Does the 1999 scheme cover my claim` -- an accident before the Act commenced answers `JUST
  FALSE` (s 122(2) is a flat "does not apply"; the note points to the Motor Accidents Act 1988) -- s 67(1) is a grant
  without "only", so Chapter 4 alone would answer `NOTHING`.
- **F3** s 3A(1) with Part 1.2 -- `Does the 1999 scheme cover my claim` -- where no owner or driver was at fault the
  answer is `NOTHING`, because Part 1.2 may deem fault and is asked by its own questions -- `JUST FALSE` under s 3A(1)
  "applies only", which would be wrong for a blameless accident or a child.
- **F4** s 7J(3) "is an entitlement to recover damages for the following" -- `Does the special entitlement cover this
  expense` -- read as a closed definition: another kind of loss answers `JUST FALSE` -- an open list, answering
  `NOTHING`.
- **F5** s 33(4)(b), (d), s 33(5), s 35, s 35A(3) -- `Can I claim against the Nominal Defendant` -- not asked: the
  trailer case, regulation exclusions, the s 33(5) definition of motor vehicle (exempt from or capable of registration)
  and the end date for the terrorism exclusion are assumed not to arise -- ask each.
- **F6** s 48(c) "(or within such other period as the form requires)", s 50(3) "The regulations may shorten or extend
  that period" -- the early payment questions -- 28 days and 10 days are used -- the form or the regulations may set
  another period.
- **F7** s 50(4), (6) -- `Has the insurer accepted provisional liability` -- a late notice refusing provisional liability
  does not undo the acceptance s 50(4) deems; a late notice accepting it counts -- a late refusal displaces the deemed
  acceptance.
- **F8** s 109(2) "Time does not run ... from the time that a claim has been referred ... until 2 months after a
  certificate" -- `the last day without leave` -- the paused days are added to the end of the three years, and only
  where the referral came on or before the last day (a referral after the time had run revives nothing) -- the pause
  counts whenever the referral was made.
- **F9** s 110(1) -- `Is my claim withdrawn for not commencing proceedings` -- the 6-month and 18-month conditions are
  tested on the day the claimant received the notice (the text says when the insurer "may give" it) -- tested on the day
  it was given.
- **F10** s 130 "reduce ... by", ss 83(5), 84A(3) "a defence ... to the extent of its amount" -- `What economic loss is
  left after the s 130 reduction`, `How much is still to be paid after contributory negligence` -- the result stops at
  zero -- the text is silent on an excess, which might be recoverable or set off elsewhere.
- **F11** s 141A -- `What is the most per week for gratuitous attendant care` -- gratuitous attendant care for a Lifetime
  Care and Support participant during participation is a "treatment and care need" (as defined in the 2006 Act, not
  deposited), so nothing -- some care might fall outside that definition.
- **F12** s 85B(1) "within 2 months after the end of that period" -- `Is my claim withdrawn for want of particulars` -- a
  direction must come after the 2 years 6 months have ended (not on their last day) and by the last day of the next 2
  months; a direction outside that window has no s 85B effect (`JUST FALSE`) -- a direction given early takes effect
  when the period ends.
- **F13** s 81(3), (4) -- `Where does liability stand` -- a late notice denying liability leaves the insurer "taken to
  have wholly denied" it; a late admission (whole or in part) is an admission -- a late partial admission might leave the
  rest deemed denied (the answer says only "admits in part").
- **F14** s 47A(1) -- `Am I entitled to early payment` -- who decides the serious offence is not said; it is asked as a
  fact -- the insurer decides, reviewable.
- **F15** s 82(4)(b) "not sufficiently recovered within 3 years after the motor accident" -- `By when must the insurer
  make me an offer` -- recovery on the third anniversary is within 3 years -- the third anniversary is outside.
- **F16** s 76(2) -- `Has the insurer lost the right to reject my claim` -- for a non-complying notice only a rejection
  within 2 months keeps the right; a request for more does not, and there is no explanation step -- a request counts as
  in ss 70(4), 73(4).
- **F17** s 7L, s 7P(2) "in a case in which this Division would confer a special entitlement ... but for" --
  `Can my child's damages be reduced for contributory negligence` -- the child must otherwise meet every Division 2
  condition (asked as one fact) -- only some of them.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 48(b), (c) | the injured person | condition with a deadline (28 days) | MUST rule |
| s 50(1), (3), (4) | the insurer | duty with a deadline (10 days); deemed acceptance on breach | MUST rule |
| ss 34A(2), 70(4), 73(4), 76(2) | the insurer | power to reject that lapses after 2 months (two steps) | two MUST rules (lapse as breach) |
| s 81(1), (3) | the insurer | duty with a deadline (3 months); deemed denial on breach | MUST rule |
| s 82(1) | the insurer | duty with a deadline (the later of two days) | date question |
| s 85B(1), (3) | the claimant | duty under a direction (3 months); deemed withdrawal on breach | MUST rule |
| s 110(2), (3) | the claimant | duty under a notice (3 months); deemed withdrawal on breach | MUST rule |
| s 70(1) | the claimant | duty with a deadline (28 days) | date question |
| s 72(1) | the claimant | duty with a deadline (6 months), excusable under s 73 | date question |
| s 108, s 109 | the claimant | disability: no proceedings without a certificate, or after 3 years without leave | `Am I entitled to commence court proceedings` |
| ss 85(4), 86(4) | the claimant | disability while failing to co-operate | the same question |
| s 131, s 132 | the court | disability: no non-economic loss award at 10% or less | `Can I be awarded damages for non-economic loss` |
| s 144, s 142(1), s 141A | the court | disability | `Can damages of this kind be awarded` |
| s 140(1) | the defendant | no defence (volenti), except motor racing | `Can the defendant rely on voluntary assumption of risk` |

## What the Act turns out to say

1. **Two dates for one maximum.** The s 134 maximum for non-economic loss applies "as at the date the award is made"
   (s 134(2)) for the award, but the thresholds for late proceedings and reinstatement (ss 85B(7)(b), 109(3)(b)) use the
   maximum "as at the date of the motor accident". A person needs both figures; the encoding asks for the right one in
   each question.
2. **The base figures are 1999 figures.** $2,500 a week (s 125) and $284,000 (s 134) have been indexed every year under
   s 146; the deposited text names only the 2024 order in an editorial note. Every amount is an input; using the Act's
   figure would understate the current maximum by a large margin.
3. **The seat belt exception for minors does not reach helmets or drink-driving.** s 138(2)(b) and (c) exclude a minor;
   (a) (an alcohol or drug offence) and (d) (no helmet when required) do not. A minor without a required helmet must be
   found contributorily negligent. Asserted.
4. **A child's special entitlement is narrow.** s 7J(3) covers treatment, rehabilitation, respite care, attendant care
   and funeral expenses only: no loss of earnings or non-economic loss. Where the owner or driver was at fault, s 7L
   keeps those same kinds of damages from being reduced for the child's own contributory negligence. Asserted.
5. **The s 33(4) exclusions do not reach s 34.** A Commonwealth vehicle, or one registered elsewhere with its own
   compulsory cover, cannot found a claim against the Nominal Defendant under s 33; but s 34 (an unidentified vehicle)
   has no such exclusion, perhaps because an unidentified vehicle's owner cannot be known. Asserted on the text.
6. **Four "loses the right to reject" provisions are near-identical but not quite.** ss 70(4) and 73(4) let the insurer
   keep the right by asking for an explanation; s 34A(2) the same for due inquiry and search; s 76(2) only by rejecting.
   Encoded with one pair of rules and a per-ground switch (fork F16).
7. **s 50(5) singles out the Nominal Defendant.** For an unidentified vehicle, silence is not acceptance of provisional
   liability, unlike every other insurer. Asserted.
8. **References to the Personal Injury Commission.** The text as at 16 June 2022 refers to the Commission (Personal
   Injury Commission Act 2020) where the claims assessment service once stood, although the Act covers only accidents
   before 1 December 2017. Schedule 5 Part 12 cl 42 carries the old claims assessors across. A claimant with an old
   certificate meets the earlier names.
9. **Commencement dates are not in the text.** s 3AA, s 67, s 7D and s 7J(5) turn on commencement dates the deposited
   text does not give (the Act's in October 1999; the 2017 Act's on 1 December 2017; Part 1.2's under the 2006 amending
   Act). Schedule 5 cl 38 mentions 1 October 2006 only for the 2010 amendment of the definition of motor accident. They
   are asked as yes/no facts.
10. **s 130(a) names the Victims Compensation Act 1996.** That Act has (as far as is known here, not checked in a
    deposited source) been replaced by later victims support legislation; the reference may be stale. The encoding asks
    for compensation "under the Victims Compensation Act 1996" as the text says.
11. **The offer of settlement can wait on the claimant.** s 82(1) runs from the later of recovery and full particulars,
    so the insurer's duty does not arise until the claimant has given all relevant particulars (s 85A); s 82(6) stops an
    insurer delaying for insufficient particulars unless it asked within 2 weeks (not encoded: a dispute for the
    Commission, s 96(1)(d)).
12. **s 109(2) does not say what happens to a referral made after time has run.** Fork F8.

## Questions (exported)

`mac-claims.l4` (21), in the Act's order: `Does the 1999 scheme cover my claim` (ss 3, 3AA, 3A, 3B, 67, 122), `Can I claim
for a blameless accident` (ss 7A-7E), `Does my child have the special entitlement` (ss 7J, 7K, 7P), `Does the special
entitlement cover this expense` (s 7J(3), (4)), `Can my child's damages be reduced for contributory negligence` (ss 7F,
7K(5), 7L, 7P(2)), `Can I claim against the Nominal Defendant` (ss 33, 34, 35A), `By when must I submit the accident
notification form` (s 48(c)), `Am I entitled to early payment` (ss 46A, 47A, 48, 50(7), with the MUST rule), `Has the
insurer accepted provisional liability` (s 50, with the MUST rule), `How much early payment must the insurer make`
(ss 47, 51), `By when must I report the accident to police` (s 70(1)), `By when must I make my claim` (ss 72, 73(1)),
`Has the insurer lost the right to reject my claim` (ss 34A(2), 70(4), 73(4), 76(2), with two MUST rules), `Can my claim
still be referred for assessment` (ss 34A(1), 70(3), 73(3), 76(1)), `Where does liability stand` (s 81, with the MUST
rule), `By when must the insurer make me an offer` (s 82), `Is my claim withdrawn for want of particulars` (s 85B, with
the MUST rule), `Must my withdrawn claim be reinstated` (s 85B(4), (6), (7)), `What is the last day to commence
proceedings without leave` (s 109(1), (2)), `Am I entitled to commence court proceedings` (ss 85(4), 86(4), 108, 109),
`Is my claim withdrawn for not commencing proceedings` (s 110, with the MUST rule).

`mac-damages.l4` (12): `Can I be awarded damages for non-economic loss` (ss 131, 132), `What is the most I can get for
non-economic loss` (ss 131-134), `What weekly earnings are counted` (s 125), `What discount rate applies` (s 127), `What
economic loss is left after the s 130 reduction` (s 130), `Must a finding of contributory negligence be made`
(s 138(2)), `How much is still to be paid after contributory negligence` (ss 83(5), (6), 84A(3), (4), 138(3)), `Can the
defendant rely on voluntary assumption of risk` (s 140), `What is the most per week for gratuitous attendant care`
(ss 141A, 141B), `Can damages of this kind be awarded` (ss 141A, 141C, 142, 144), `Can I get interest on my damages`
(s 137(1)-(4)), `What is the interest rate on my damages` (s 137(6)).

## Rulings on negatives

The rulings of 2026-11-04 and 2026-11-05 recorded in `docs/ENCODING-GUIDE.md` section 5 govern every `JUST FALSE` and
`NOTHING` here: `JUST FALSE` where the text says no in its own words (a "means" definition; "if", "only if", "unless",
"where", "when"; a flat "does not", "cannot", "is not entitled", "must not"; a period the text fixes); `NOTHING` where it
lists without closing, is silent, points outside the sources, or limits a grant in its own words and the case falls
outside it. Questions with no convention were decided site by site and are in the fork register.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the s 146 indexation orders, the Motor Accidents Compensation Regulation and the s 51 Gazette orders, and
  replace the corresponding inputs with tables by date.
- Check the commencement dates (finding 9) and the s 130(a) reference (finding 10).
- Have a lawyer review the forks, especially F2, F3, F8, F12 and F16.
- Link the encoding to the Motor Accident Injuries Act 2017 (accidents from 1 December 2017), the Compensation to
  Relatives Act 1897 baseline (claims for a death, s 7J(4), s 142) and the Lifetime Care and Support Act (s 141A).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
