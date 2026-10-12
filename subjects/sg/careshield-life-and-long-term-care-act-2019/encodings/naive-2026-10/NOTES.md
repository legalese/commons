# CareShield Life and Long-Term Care Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CLLTCA2019.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021"; later amendments are annotated in
the text, the latest being Act 18 of 2025 (CareShield Life and Long-Term Care
(Amendment) Act 2025, commencement 1 January 2026), the last entry in the deposited
legislative history. SSO's metadata calls it the "Current version as at 01 Oct 2026".

**Checks:** two modules, two case files, 102 assertions satisfied (50 in `cll-cases-careshield.l4`, 52 in
`cll-assessment-cases.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: CareShield Life is the compulsory
long-term care insurance for Singapore citizens and permanent residents born in or
after 1980, from age 30, with premiums deductible from MediSave (s 14(4)) and a
monthly insured sum on severe disability. This row takes what an insured person, a
payer or a caregiver meets: automatic coverage (s 6(1)(a), (b)), the two disability
tests (First and Fourth Schedules), entitlement and its end (ss 12, 18(7)), refusal
of a claim (s 16(4)), the premium deadline and the penalty cap (ss 14(3), 29(3)),
protection of payouts (s 20), the proper claimant of a deceased cash payer
(s 15(3), (5)), joint moneys (s 25(3), (9)), the bar on leaving Singapore
(s 28(6)), change of address (s 58), and the offences in ss 48 and 50 with
composition (s 56).

Not encoded: coverage under s 6(1)(c) and (d) (both turn on prescribed dates,
periods and conditions, none retrieved) and the Board's discretion in s 6(4); the
ElderShield transfer (Part 3); premium and insured-sum amounts (prescribed, not in
the Act); deferment and suspension (s 19); most of the recovery machinery
(ss 23-27); restricted information (Part 8); the Funds and the Council (Parts 9,
10); investigators (ss 46, 47); fraudulent assessments (s 49); and all
regulations.

## What the Act turns out to say

### 1. "Not disabled" is not the opposite of "severely disabled"

The First Schedule makes a person severely disabled when "unable to perform 3 or
more" of six activities of daily living. The Fourth Schedule, added by Act 18 of
2025, says a person is not disabled "only if he or she can perform all" six "without
assistance all the time". Someone who needs help with one or two activities is
neither. The difference bites in s 6(1)(b): a person born before 1980 who first
becomes a citizen or PR on or after 1 October 2020 is covered automatically only if
"not disabled" on the SCPR date where that date falls after the 2025 amendment
commenced, but only if "not severely disabled" where it fell before. A new PR in 2026
who needs help bathing is outside s 6(1)(b); the same person in 2023 was inside it.
Taking the commencement as 1 January 2026 is an inference from the annotation; the
deposit does not list the commencement of s 3(a) separately. Asserted.

### 2. The younger cohort is covered with no health condition at all

s 6(1)(a) covers "every citizen ... or permanent resident ... whose birthday is on or
after 1 January 1980 and who is at least 30 years of age". Unlike (b) and (c), it
says nothing about disability, so on the text a person already severely disabled at
30 is covered. Asserted.

### 3. Payouts can outlast the disability, until the next review

Entitlement ends when the insured person "is no longer severely disabled"
(s 12(3)(b)), but "Despite section 12(3)(b)" the Board may continue paying "until
the completion of the insured person's next periodic disability review" (s 18(7)).
Asserted.

### 4. Payouts are shielded from creditors, with two exceptions

s 20(1): benefits are not assignable, not attachable, excluded from any set-off and
do not pass to the Official Assignee on bankruptcy. The only set-offs allowed
(s 20(2)) are debts due to the Fund and care debts owed to the healthcare
institution that is itself the approved payee caring for the insured person. Care
fees owed to some other nursing home cannot be set off. Asserted.

### 5. The basic false-declaration penalty is a fixed multiple, not a maximum

s 48(2): an individual convicted of a knowingly false or misleading declaration or
claim is liable "to a penalty equal to the relevant amount"; any other person to 5
times. There is no fine and no imprisonment unless the person intended an
undercharge or overpayment (s 48(3)), which brings a fine (up to $5,000 or 12 months
for an individual; $10,000 otherwise) plus 2 or 4 times the relevant amount. The Act
does not say whether (3) displaces (2); the encoding treats it as replacing it (an
inference). Asserted.

### 6. A caregiver who diverts the payout faces four times the amount diverted

s 50: whoever receives benefits on an insured person's behalf "must first apply the
benefits for the care of the insured person". Without reasonable excuse it is an
offence: an individual, up to $10,000 or 2 years, plus a penalty of 4 times the
amount not applied for care; any other person, up to $20,000 plus 8 times. The
court may order repayment into the Fund with interest. Asserted.

### 7. Smaller points

- The premium is due within 30 days of the start of the insurance period, or a later
  date the Board permits (s 14(3)). Late-payment penalties may not total more than 17%
  of the premium plus interest for the period (s 29(3)). Asserted.
- A defaulter who, knowing of a direction, leaves or tries to leave Singapore without
  paying or giving security commits an offence (up to $5,000 or 12 months) and may be
  arrested without warrant (s 28(6)). Asserted.
- Reporting a new address under the National Registration Act counts as telling the
  Board (s 58(2)). The Act states no penalty for breaching s 58. Asserted.
- Joint account holders are presumed to own equal shares (s 25(3)); an account with a
  minor holder, a partnership account or a trust account is not a "joint account"
  (s 25(9)). Asserted.
- A cash payer's premium for a period not yet started may go, on death, to a
  personal representative or a listed relative, step-parents included, but not a
  cousin (s 15(3), (5)); the ceiling is set by Gazette notification, not retrieved.
  Asserted.
- Composition is capped at the lower of half the maximum fine and $1,000 (s 56(1)),
  for offences prescribed as compoundable (not retrieved). Asserted.

## What would need doing before this is worth anything

- The CareShield Life regulations (premiums, insured sums, cover ending, excluded
  events under s 16(4)(d), penalty rates, compoundable offences) and the s 6(1)(c)
  Gazette orders were not retrieved; most of the money in the scheme lives there.
- The commencement of s 3(a) of Act 18 of 2025 should be confirmed against the
  amending Act.
- The relation between s 48(2) and (3) needs a reading from case law or the
  Explanatory Statement.
- Age is taken as a number of whole years; the s 2(2) rules (29 February birthdays,
  unknown dates) are not encoded.

## Disability assessment (added 12 October 2026 for REQ-0278)

Module `cll-assessment.l4`, cases `cll-assessment-cases.l4` (52 assertions). Sources: the Act; the CareShield Life
and Long-Term Care (Disability Assessment Fees) Regulations 2020 (S 69/2020) at
`../../registers/source-bundle/CLLTCA2019-S69-2020.txt`; and the CareShield Life and Long-Term Care (CSHL Scheme)
Regulations 2020 (S 849/2020) at `../../registers/source-bundle/CLLTCA2019-S849-2020.txt`.

The question (Haziq scenario): after a stroke a claimant cannot bathe or dress unaided and can transfer only
sometimes. Who assesses whether he cannot perform three of the six activities of daily living, and how is
"sometimes" treated?

1. **Who assesses: an assessor approved by the Minister; the Administrator decides.** s 2(1) defines "assessor" as
   one "approved by the Minister under section 17(1) to conduct, and report on, disability assessments". s 17(1)
   lets the Minister approve individuals "having the necessary qualifications", subject to conditions. The Act does
   not say what the qualifications are and does not require an assessor to be a doctor. A doctor who has not been
   approved is not an assessor. The assessor only conducts and reports. Under s 16 and Part 2 of the Second Schedule
   the Administrator accepts or refuses the claim, and refuses it if the insured person "is not severely disabled"
   (s 16(4)(a)). The Board pays (s 18(1)). Asserted.
2. **How "sometimes" is treated: the Act does not say, and the answer decides this claim.** The First Schedule makes
   a person severely disabled when "unable to perform 3 or more" of the six activities. The words "all the time"
   appear only in the Fourth Schedule ("not disabled"). Bathing (a) and dressing (b) are two activities he cannot
   perform. Whether transferring "sometimes" makes a third depends on whether an activity done only some of the
   time counts as one he is "unable to perform". Neither the Act nor either deposited regulation defines "unable to
   perform" or says how an assessor scores an activity. The ledger expected the scoring to be in MOH guidelines
   rather than law, and the deposit bears that out: nothing in it settles the point. The encoding takes it as an
   open parameter, `sometimes counts as unable`. With FALSE his count is 2 and he is not severely disabled. With
   TRUE it is 3 and he is. Asserted both ways.
3. **Under the Fourth Schedule "sometimes" plainly counts against him.** He cannot do bathing, dressing or
   transferring "without assistance all the time", so he is not "not disabled". That matters for cover (s 6(1)(b),
   reg 2A, reg 6(1AA) and (1B)), not for a claim. Whatever the First Schedule answer, he is at least in the gap
   the Act leaves between "not disabled" and "severely disabled". Asserted.
4. **An assessment is a power, not a step every claim must take.** The Administrator "may" require one on a claim
   (s 16(3)(c)) or a periodic review (s 21(2)(c)). The Board "may" require one on an application for cover
   (s 7(5)(c)) or to establish disability for s 6(1)(b) and (c) (s 6(2)). If he does not attend, the claim may be
   refused (s 16(4)(c)), or payment stopped after a review (s 21(3)). Asserted (which body may require it on each
   occasion).
5. **The fee is capped.** s 17(2) with S 69/2020 reg 2 and the Schedule: at most $100 at the assessor's place of
   practice and $250 at any other premises (a home visit, say), "inclusive of GST, if applicable". The Fund may
   reimburse assessors' fees "as determined by the Board" (s 36(1)). How much is reimbursed is not in the
   deposit and is not encoded. Asserted.
6. **A stroke is not an excluded cause.** s 16(4)(d) with S 849/2020 reg 26 lets the Administrator refuse a claim
   only for war, invasion, act of foreign enemies, hostility, terrorist act, insurrection or military or usurped
   power. Asserted.
7. **A false assessment report is an offence (s 49).** It applies where an assessor gives false information or
   conceals information intending to affect cover or a claim. The punishment is a fine up to $10,000 or 2 years or
   both, plus 4 times the "relevant amount", defined as "the amount of overpayment and the amount of assessment fee
   charged". The encoding adds the two together, which is an inference from "and". Composition would be capped at
   $1,000 if the offence is prescribed as compoundable (s 56(1); which offences are prescribed was not retrieved).
   Asserted.
8. **Facts assumed.** The question does not mention feeding, toileting or walking. The fixture assumes he manages
   all three without assistance all the time. If he could not do any one of them, he would be severely disabled
   under either reading.

Needed for a full answer: MOH's disability assessment guidelines or the conditions of approval imposed on assessors
under s 17(1), for how an assessor scores an activity done "sometimes" (none retrieved); and any decision or appeal
practice on the Administrator's reading of "unable to perform". A search of the Act for "appeal" finds it only in
the premium-recovery provisions, not against refusal of a claim; nothing on reconsideration was found in the deposit.
