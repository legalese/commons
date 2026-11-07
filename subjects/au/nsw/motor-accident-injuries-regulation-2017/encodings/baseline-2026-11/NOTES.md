# Motor Accident Injuries Regulation 2017 (NSW) -- baseline encoding, the claimant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 22 September 2023; the parent Act's document dated 1 April 2023). It is unofficial and may be out of
> date: amendments after those versions are missing, and the monetary unit for 2025-26 onwards is not in it. Check
> legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules: the insurer's duty to
give written notice of review rights with its decision (cl 12), and the insurer's duty to pay assessed damages within the
period, with interest on breach (cl 16). Each is run by `EVALTRACE` inside an exported question that takes only plain
facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Regulation; nothing existing was touched. The Regulation is encoded nearly whole: every
clause a claimant meets is in, and what is left out is machinery or another party's business (see Scope). The parent
Act (`subjects/au/nsw/motor-accident-injuries-act-2017/`) had no encoding when this was written. Where a clause only makes
sense through an Act section (s 6.13(2) for cl 8A, s 7.11 for cl 10, s 7.34(1) for cl 14, s 7.38(2) for cl 16, s 7.52
for cl 18, among others), that section is read from the deposited Act and named in a comment.

## Edition

- **Regulation:** Motor Accident Injuries Regulation 2017 (2017-498), corpus document
  `nsw_legislation:2023-09-22/sl-2017-0498`, deposited at `../../registers/source-bundle/sl-2017-0498.txt` (text_sha256
  b05474c7...7f6 per its `.meta.json`), taken from the Open Australian Legal Corpus (collected 10 March 2025) because
  legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Act (for the sections the clauses work through):** Motor Accident Injuries Act 2017 No 10, corpus document
  `nsw_legislation:2023-04-01/act-2017-010`, deposited at
  `../../../motor-accident-injuries-act-2017/registers/source-bundle/act-2017-010.txt`.
- **Not deposited:** the Motor Accident Guidelines, the Authority's yearly orders under s 3.9 (the maximum weekly
  amount), the Civil Procedure Act 2005 s 101 rate, the AMA List, the Legal Profession Uniform Law, DSM-5, and the Act's
  former Schedule 2 cl 2(c) (kept by cl 42). What they decide is asked as a fact, or answered `NOTHING`.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `maireg-dates.l4` | 0 | 0 | 0 | 0 |
| `maireg-claims.l4` | 0 | 0 | 0 | 0 |
| `maireg-costs.l4` | 0 | 0 | 0 | 0 |
| `maireg-claims-cases.l4` | 0 | 0 | 101 | 101 |
| `maireg-costs-cases.l4` | 0 | 0 | 105 | 105 |

Every expected value was worked by hand from the text, with the edges: the 28th day after the accident and the day
after; three months ending in a leap February and in a 30-day April; an accident on 31 March and on 1 April 2023
(cl 8A(4)); a rejection of the explanation on the 14th day after receipt and on the 15th; acceptance received before,
on and after the 21st day; payment on the last day of the 28 and the day after, with and without deductions; a
cancellation exactly 72 hours ahead and 73; each adjustment year's first and last day for the monetary unit, and days
before and after the deposited table; a cost of $2,551.50 rounding down; merit reviews at 3 and 4 (the 60-unit cap);
assessment conferences at 2 and 4 hours; Table A stage 3 at $20,000 and $20,001, and stages 4 and 5; Table B at $20,000,
$30,000 and $60,000; cl 25 at $75,000 and $75,001; cl 26 at $25,000, $25,001, $50,000, $50,001, $75,000 and $75,001;
Schedule 2 caps at 9 and 36 units; cl 30 with excesses one dollar under and at $2,000, 20% and $200,000; GST at, under and
over 10%.

## Seat

**The claimant**: the person injured in a motor accident in NSW, or a person claiming in connection with another's injury
or death, who claims statutory benefits or damages under the Motor Accident Injuries Act 2017. Every exported question is
one that person would ask ("Is my injury a threshold injury?", "By when must I claim?", "Can I be back-paid?", "Must I
ask for an internal review first?", "Did the insurer have to tell me my review rights?", "Can I have my medical dispute
assessed again?", "Is my claim exempt from claims assessment?", "By when must the insurer pay me, and is interest
owed?", "Can I be charged for a missed assessment?", "What is the most my lawyer or a doctor may charge?", "Who pays the
costs if I rejected the assessment and went to court?"). The insurer, the lawyers and doctors whose charges are capped,
the Authority, the Commission and its President get no seat here: what they may do is encoded as what it means for the
claimant. An insurer seat or a legal-practitioner seat could be added beside this one (cl 22, 40 and 41 put duties on
lawyers).

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** Followed: the Regulation is itself the instrument that sets the
  Act's numbers. The Act's sections the clauses work through are read where a clause cannot be answered without them
  (named above); this is a departure only in that those Act sections are encoded here in the smallest form needed, not
  in the Act's own encoding (none existed).
- **The actors the text names.** Followed: the claimant, the insurer, the Authority, the President, the Commission, the
  court, Australian legal practitioners, health practitioners.
- **Judgments answered conditionally.** Followed: a "full and satisfactory explanation" (cl 8A), a "material effect"
  (cl 13), a "reasonable excuse" (cl 32), a "reasonable time" (cl 28(3)), reasonable accommodation and meals (Sch 2
  item 4), and any court direction as to costs are inputs.
- **Definitions worked out; borrowed terms asked.** Followed: the Regulation's own definitions (assessment acceptance
  day, exempt minor claim, associate, regulated merit review matter, monetary unit) are worked out; DSM-5 terms, "person
  under legal incapacity" (s 7.47), "health practitioner", the AMA List and the s 101 rate are asked.
- **One case.** One claim.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative provisions in; machinery out.** Followed (see Scope).

## Scope

**In:** cl 4 (threshold injury); cl 7 (minimum weekly amount); cl 8 (mental harm); cl 8A with s 6.13(2) (late claims,
back pay) and cl 42 (as a gate); cl 9 (accommodation and travel damages); cl 10, 11 with ss 7.11, 7.41 (no internal
review needed); cl 12 (review rights notice, a MUST rule); cl 13 with s 7.24(2)-(3) (further medical assessment); cl 14
with s 7.34(1) (claims exempt from assessment); cl 15 (acceptance day); cl 16 with s 7.38(2)-(3) (time for payment,
interest, a MUST rule); cl 17 (miscellaneous claims assessments binding or not); cl 18 with s 7.52 (evidence
restriction); cl 20 (costs outside the Part); cl 21-24 and Schedule 1 Part 1 (maximum costs for dispute-resolution and
court steps; internal review; compensation matter applications; exempt claims); Schedule 1 Part 2 cl 1-2 (maximum costs
by stage of a damages claim); cl 25 (costs agreements); cl 26 (minors); cl 27-28 and Schedule 2 (medico-legal fees);
cl 30-31 (costs after a claims assessment); cl 32 (missed medical assessment); cl 33 (car travel); cl 34 (treatment
fees); cl 35 (GST); cl 36(2)-(3) with s 11.5(2) (service on a lawyer or representative); Schedule 3 cl 1-3 (the
monetary unit and rounding).

**Out, and why:**

- cl 1, 2 (name, commencement), cl 3 and 19 (definitions, used where needed): machinery.
- cl 5, 6 (unregistered vehicle permit classes; notice before an insurer asks for registration to be suspended): these
  are the vehicle owner's business, not the claimant's. A vehicle-owner seat could take them.
- cl 22(2)-(5), 26(6)-(7) (apportioning costs between successive lawyers, and the disputes about it): between lawyers.
- cl 29 (the Commission may assess the costs of a direction to produce): a power with no claimant fact.
- cl 36(1), 36(4), 37, 38 (electronic service methods; service on the Authority and the Nominal Defendant): methods of
  service with no question a claimant needs answered beyond cl 36(2)-(3).
- cl 38A, 38B, 39 (between the Authority, the Lifetime Care and Support Authority and insurers): machinery.
- cl 40, 41 (a lawyer's duty to give the Authority a costs breakdown; referral fees): duties on lawyers; cl 40's
  breakdown appears only as a fact in cl 25(1)(d).
- Schedule 1 Part 2 cl 3-4 (advocates' country and interstate loadings, with a 61-town table): an advocate's
  entitlement, a lookup with no rule to encode; it could be added as a table.
- Schedule 1 Table A rows "(b) ... acting for an insurer -- nil": the insurer's side.
- Schedule 3 cl 4 (the Authority's notice of the indexed amounts): machinery; cl 4(2) says the amounts change without it.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** cl 4 with s 1.6(1) -- `Is my injury a threshold injury` -- an injury that is neither a threshold injury under
  the Act alone nor one cl 4 adds answers `JUST FALSE` (s 1.6(1) "a threshold injury is ... one or more of the
  following", and the Regulation adds no more) -- `NOTHING`, if the Motor Accident Guidelines' assessment rules (s 1.6(5))
  were thought to widen the class.
- **F2** cl 4(1) "(other than radiculopathy)" -- `Is my injury a threshold injury` -- a spinal nerve root injury showing
  radiculopathy gets nothing from cl 4(1) and follows the Act alone (which excludes "an injury to nerves" from soft tissue
  injury, so usually `JUST FALSE`) -- `NOTHING`, the clause being silent on radiculopathy.
- **F3** "within 28 days after", "within 14 days after", "21 days after", "within 28 days after" (s 6.13(2), cl 8A(3),
  15(3), 16) -- the date functions -- the day of the event is not counted and the last day counts (a rejection on the
  14th day after receipt is in time) -- the Interpretation Act 1987's counting rules (not deposited) might shift an end
  day that falls on a weekend or holiday.
- **F4** cl 8A(1)(a) "within 3 months after the date of the motor accident" -- `By what day must I claim to be back-paid
  ...` -- the same day of the month three months later, or that month's last day where shorter (30 November -> 29
  February in a leap year) -- the Interpretation Act's month rules might differ.
- **F5** cl 9 -- `Can I claim damages for this accommodation or travel` -- read as a definition of the kind ("is any
  accommodation or travel for which ..."), so a cost not caused by the injury answers `JUST FALSE` -- a grant limited in
  its own words, answering `NOTHING`.
- **F6** cl 10 with s 7.11(1) -- `Must I ask for an internal review before a merit review` -- for another merit review
  matter, `JUST TRUE`, assuming the decision is a reviewable decision (Schedule 2 of the Act, not encoded) -- `NOTHING`,
  leaving the Act to decide.
- **F7** cl 14 with s 7.34(1) -- `Is my claim exempt from claims assessment` -- none of (a)-(e) and no Commission
  determination answers `JUST FALSE` (s 7.34(1) "is exempt ... if") -- `NOTHING`, cl 14 not being closed with "only".
- **F8** s 7.38(2)(b) "accepts ... within 21 days after the certificate of assessment is issued" -- `the assessed damages
  are payable under s 7.38(2)` -- acceptance is dated by the insurer's receipt of the claimant's notice (cl 15(3)(a)), and
  the 21 days run from the certificate's issue to the insurer -- the day the claimant sends the notice; the day the
  certificate issues to the claimant.
- **F9** cl 18 with s 7.52(1) "not admissible unless" -- `Is this health practitioner's evidence barred` -- once the
  practitioner is treating or authorised, `JUST FALSE` (s 7.52 does not bar it) -- `NOTHING`, admissibility then being for
  the general law of evidence.
- **F10** cl 32(1)(b) "cancelling ... within 72 hours of the scheduled time" -- `Can the Authority recover the costs of my
  missed assessment` -- a cancellation exactly 72 hours ahead is within -- only less than 72 hours.
- **F11** Sch 3 cl 3 -- `the rounded maximum on` -- a maximum is rounded once, as a whole (units times the monetary unit
  plus any cents-per-dollar part) -- round only the monetary-unit part, or round each stage separately (the totals can
  differ by a dollar).
- **F12** Sch 1 cl 6 table "Conference directly related to a compensation matter application 3" -- `What is the most my
  lawyer may charge for this step` -- 3 units a conference, flat, because the row says no "per hour" -- 3 units an hour,
  as in cl 4 and 5.
- **F13** Sch 1 Part 2 cl 2(3) "Costs may be charged for more than one stage" -- `What is the most my lawyer may charge
  for my damages claim` -- stages 1 and 2 (7.24 units) are added to stage 3, 4 or 5, and stage 3 is not charged when the
  claim reaches a certificate (stage 4 is "determined, in accordance with stage 3") -- stages 1-2 might be thought
  included in stage 4's "as per stage 3" amount (stage 3 says "in addition to the 7.24 monetary units ... if chargeable").
- **F14** Sch 2 item 2(a) "for the first 1.5 hours" -- `What is the most a health practitioner may charge` -- expert
  evidence shorter than 1.5 hours still allows the 12 units -- pro rata.
- **F15** cl 30(3)(a) "by at least $2,000 or 20% (whichever is the greater)" -- `Who pays the costs after I rejected the
  assessed damages` -- 20% of the amount in the certificate -- 20% of the court's award.
- **F16** cl 31(1) "applies ... if ... the insurer does not admit liability" -- `Must the insurer pay my costs because it
  did not admit liability` -- an admission within 21 days answers `JUST FALSE` -- `NOTHING` (cl 31 silent; cl 30 or the
  court decides).
- **F17** cl 16(1), (4) -- `By what day must the insurer pay my assessed damages` -- where deductions must be made, the
  whole balance is due 28 days after the last advice -- the part of the damages not touched by deductions might still be
  due 28 days after the acceptance day.
- **F18** Sch 1 Part 2 cl 2(2) -- `What is the most my lawyer may charge for my damages claim` -- where the lawyer was
  first retained after the certificate, Table B applies whatever the route, on the settlement or award amount -- Table B
  only for claims ending after a certificate (a claim "resolved without a certificate" cannot have one).
- **F19** cl 7 -- `What is the minimum weekly statutory benefits amount` -- 2.5% unrounded -- rounded to the cent or
  dollar as the Authority's practice may be.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| cl 8A(1), (3) | the insurer | duty to pay back weekly payments; power to reject an explanation within 14 days | `Can I be paid weekly benefits for the time before my claim`, `Is my explanation ...` |
| cl 10, 11 | the claimant | privilege: no internal review needed | `Must I ask for an internal review ...` |
| cl 12 | the insurer | duty with a deadline (with the decision); offence, 5 penalty units | MUST rule, WITHIN 0 |
| cl 13 | the claimant | power to refer again, limited | `Can I have my medical dispute assessed again` |
| cl 15(1) | the claimant | duty to give written notice of acceptance or rejection (no deadline, no consequence) | a fact in cl 15-16 |
| cl 16 | the insurer | duty with a deadline (28 days); interest on breach | MUST rule, WITHIN 28 |
| cl 22, 25, 26, Sch 1-2 | lawyers, health practitioners | disability: cannot recover above the maximum | the cost questions |
| cl 28(3) | the claimant | disability: cannot claim item 5 or 6 for a first report unless ... | `Can I claim the fee for my treating doctor's first report` |
| cl 30, 31 | the claimant; the insurer | liability for costs | `Who pays the costs ...`, `Must the insurer pay my costs ...` |
| cl 32 | the claimant | liability to the Authority's recovery, unless a reasonable excuse | `Can the Authority recover ...` |

## What the Regulation turns out to say

1. **Section titles out of date.** Schedule 1 cl 3(2)(d), (e) and cl 18(b) give ss 3.11 and 3.28 their old titles
   ("after 26 weeks"); in the deposited Act (1 April 2023) both sections now say 52 weeks. Only the bracketed titles are
   stale, but a reader could take 26 weeks from them. Not asserted (no rule turns on it).
2. **cl 8A(2) speaks of "the period of 28 days for making the claim".** Under s 6.13(1) the period for making a claim is
   3 months; 28 days is only the s 6.13(2) cut-off for back pay. The clause means the 28 days of s 6.13(2). Encoded so.
3. **Back pay is tied to the ordinary deadline.** cl 8A(1)(a) requires the claim within 3 months of the accident, the
   same as the general deadline in s 6.13(1). A claim made late under s 6.13(3) (up to 3 years, or for serious injury)
   can never be back-paid for the period before it. Asserted (a claim on 11 September 2024 for a 10 June accident:
   `JUST FALSE`).
4. **Accidents before 1 April 2023.** cl 8A does not apply to them, and cl 42 keeps the Act's former Schedule 2
   cl 2(c), whose text is not deposited. Asserted as `NOTHING`.
5. **The monetary unit formula was lost, and there is a gap at the start.** Schedule 3 cl 2(1)(b)'s formula ("the amount
   calculated as follows--") is missing from the deposited text; the encoding uses the Editorial note's amounts to
   2024-25 (a `formulas.md` sidecar could restore it from the authorised text). The Regulation commenced on 8 September
   2017 but the first adjustment year (2017-18) starts on 1 October 2017: no monetary unit is given for 8-30 September
   2017. Asserted (`NOTHING` on 30 September 2017).
6. **Schedule 1 Table A has cliffs.** Stage 3 jumps at each band: for a claim with liability admitted, $50,000 gives
   7.24 units plus $3,600, and $50,001 gives 51.84 units plus 10 cents (about $1,954 more at 2024-25 values); for
   liability not admitted, $20,000 gives $2,000 and $20,001 gives 25.92 units (about $3,228). Row (b) also says
   "settlement amount" where the others say "resolution amount". Encoded as written.
7. **cl 30(3)(b) matters only above $1,000,000.** An excess of $200,000 is less than 20% of the certificate only when the
   certificate is over $1,000,000; below that, (a) always catches it first. Asserted (certificate $2,000,000).
8. **Some figures are indexed and some are not.** Schedules 1 and 2 move with the monetary unit; the $75,000 of cl 25,
   the $5,000/$10,000/$15,000 and $25,000/$50,000/$75,000 of cl 26, the $25,000 cap and $2,000/$200,000 of cl 30, the 66
   cents of cl 33 and Schedule 2 item 3, and the cents-per-dollar rates of Schedule 1 Part 2 are fixed.
9. **Schedule 1 cl 6's conference row has no "per hour"** where the matching rows in cl 4 and 5 do. Fork F12.
10. **cl 15(1) puts a duty on the claimant with no time or consequence.** The claimant "is to give" written notice of
    acceptance or rejection, but the only clock is cl 15(3)(b)'s 21 days, after which the acceptance day arrives anyway;
    and s 7.38(2) makes the assessed amount payable only if the claimant accepts within 21 days. A claimant who never
    answers gets an acceptance day but no payable damages. Asserted (`NOTHING` for the payment date).

## Questions (exported)

`maireg-claims.l4` (22), in the Regulation's order: `Is my injury a threshold injury` (cl 4), `What is the minimum weekly
statutory benefits amount` (cl 7), `Are my benefits limited by the victim's fault` (cl 8), `By what day must I claim to be
paid weekly benefits from the accident` (s 6.13(2)), `By what day must I claim to be back-paid for the weeks before a
late claim` (cl 8A(1)(a)), `Is my explanation for the late claim full and satisfactory` (cl 8A(1)(b)-(3)), `Can I be paid
weekly benefits for the time before my claim` (s 6.13(2), cl 8A, 42), `Can I claim damages for this accommodation or
travel` (cl 9), `Must I ask for an internal review before a merit review` (cl 10), `Must I ask for an internal review
before a miscellaneous claims assessment` (cl 11), `Did the insurer tell me my review rights` (cl 12, MUST rule), `Can I
have my medical dispute assessed again` (cl 13), `Is my claim exempt from claims assessment` (cl 14), `What is my
assessment acceptance day` (cl 15(3)), `By what day must the insurer pay my assessed damages` (cl 16(1), (4)), `Is
interest payable on my assessed damages` (cl 16, MUST rule), `At what rate is interest payable on my late assessed
damages` (cl 16(5)), `Is the miscellaneous claims assessment of my dispute binding` (cl 17), `Is this health
practitioner's evidence barred` (cl 18), `Can the Authority recover the costs of my missed assessment` (cl 32), `How much
is my car travel to an assessment worth` (cl 33), `Is a document served on my lawyer served on me` (cl 36).

`maireg-costs.l4` (13): `What is a monetary unit worth on this day` (Sch 3), `Is this cost outside the caps` (cl 20),
`What is the most my lawyer may charge for this step` (cl 22-24, Sch 1 Part 1), `What is the most my lawyer may charge
for my damages claim` (Sch 1 Part 2), `What is the most my lawyer may charge under a costs agreement` (cl 25), `What is
the most my lawyer may charge for my claim as a minor` (cl 26), `What is the most a health practitioner may charge`
(cl 27-28, Sch 2), `Can I claim the fee for my treating doctor's first report` (cl 28(3)), `Who pays the costs after I
rejected the assessed damages` (cl 30), `What is the most I can be made to pay in costs after rejecting the assessed
damages` (cl 30(2)), `Must the insurer pay my costs because it did not admit liability` (cl 31), `What is the most the
insurer must pay for this treatment` (cl 34), `What is the most that can be charged with GST` (cl 35).

## Before relying on it

- Replace the corpus texts with the current official texts from legislation.nsw.gov.au and re-check every quotation;
  add the monetary unit for 2025-26 and later, and restore the Schedule 3 formula (finding 5).
- Link to an encoding of the Act itself when one exists (threshold injury, s 6.13(3) late claims, the at-fault limits,
  reviewable decisions), so the facts asked here as "under the Act" can be worked out.
- Have a lawyer review the forks, especially F1/F2 (threshold injury), F8 (acceptance), F13 (stages), F15 (20%).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
