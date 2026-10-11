# Casino Control Act 2006 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 29
of 2024 shown (parts in force 30 October 2024 and 21 September 2026).

**Checks:** two case files, 66 assertions satisfied (25 in `cca-cases-patrons.l4`, 41 in
`cca-family-exclusion-cases.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**13 of the 527 Singapore Acts** deposited here cite it. This row takes what a patron
and the patron's family meet: the entry levy, credit, minors and family exclusion
orders. Licensing, the Authority, games and equipment, junkets, AML duties,
disciplinary action, the other exclusion and visit-limit procedures, and taxes are not
encoded.

## What the Act turns out to say

### 1. A citizen with $100,000 on deposit can gamble on credit

s 108(1) prohibits lending and credit, but s 108(7) lets a casino give credit to (a)
anyone who is neither a citizen nor a PR, **or** (b) a "premium player": anyone with a
deposit account of at least $100,000. The premium-player limb does not depend on
nationality. Asserted.

### 2. The levy: $150 a day or $3,000 a year

s 116(1), as amended in 2024: citizens and PRs pay $150 for every 24 hours or $3,000
for annual membership. Foreigners pay nothing. From the 21st day in a year, the annual
membership is cheaper. Entering without paying costs up to $1,500 plus the $150 levy
(s 116(7)). Asserted.

### 3. "Minor" means under 21

s 132: a minor is anyone below **21**. Under s 133(5), the operator's defence for
admitting one applies only if the minor was **16 or over** and acceptable proof of age
was produced. A fake ID shown by a 15-year-old gives the operator no defence. Asserted.

### 4. Family exclusion

s 162: an order needs serious harm, which s 162(2) defines as irresponsible gambling
that ignores the family's needs, repeated over **at least 3 months**, or particularly
irresponsible over a shorter time. It also needs a likelihood that the behaviour will
continue, a chance for the respondent to object, and the best interests of all.
Events abroad count. Asserted.

## Family exclusion orders (added 11 October 2026 for REQ-0271)

REQ-0271 (Jun Hao scenario, event j081): a sister applies for a family exclusion order
against her brother, who gambles at the casino on paydays. Who may apply, on what
grounds, and who decides? Module `cca-family-exclusion.l4`, cases
`cca-family-exclusion-cases.l4` (the first six assertions are the requirement's own
question). Section numbers are the body's: the deposit's table of contents is shifted
by one line in this Subdivision, and the requirement's "ss 159-161, 163A" came from it.
The provisions are s 2 ("family member"), ss 157 to 164, 165C, 166, 167, and ss 125,
126, 128, 195 for the effect.

1. **The sister may apply herself, with no condition attached to being a sibling.**
   s 2 defines "family member" as a closed list: spouse, child (adopted and step
   included), parent (adoptive and step included), sibling (adoptive, step and half
   included). Grandparents, in-laws, cousins and former spouses are outside it. The
   condition sits on the applicant's position, not the relationship: s 159(1)(a)
   requires a family member "adversely affected by the respondent's gambling". A sister
   who is not yet affected cannot apply for an exclusion order, though she can apply
   for a family visit limit, which s 163A(1)(a) opens to a family member who "is, or is
   likely to be," adversely affected. Asserted.
2. **Under-21s and the incapacitated apply through others.** s 160: under 21, the
   person may apply personally only at 16 or over and with the Council's permission;
   otherwise a parent or guardian, or with permission another relative, applies on
   their behalf. s 161: for someone unable to apply, a relative with the Council's
   permission, or a person appointed by the Minister. INFERENCE: a parent filing for an
   incapacitated adult goes through s 161(a) and needs permission. Asserted.
3. **Who decides: a three-member Committee of Assessors, not the Council itself.** The
   application goes in writing to the National Council on Problem Gambling, which "must
   refer" it to a Committee (s 159(2)). The Council's chairperson constitutes the
   Committee: a chairperson who is a Council member or special affiliate, plus 2 members
   of the panel of assessors (s 157(1)). Facts on a balance of probabilities, no strict
   rules of evidence, no lawyers except a representative applicant (s 158(3), (6), (7)).
   The Council itself decides variation and revocation (s 166). Asserted.
4. **Grounds (s 162).** The Committee "may" make the order if satisfied of (a) a
   reasonable apprehension of serious harm to family members, (b) appropriateness,
   (c) an opportunity to object (subject to s 165C, absence orders), and (d) the best
   interests of respondent and family. Serious harm is irresponsible gambling without
   regard to the family's needs, repeated over at least 3 months or particularly
   irresponsible over less (s 162(2)); apprehension needs that past harm plus reason to
   believe it will continue or recur (s 162(3)). On the assumed facts (six months of
   payday gambling, likely to continue) the order may be made; on two paydays alone it
   may not, unless he consents (s 162(5)) or one night was particularly irresponsible.
   "Gambling" includes gambling outside the casino and remote gambling (s 2). Asserted.
5. **Provisional orders (s 164, not s 163A).** Serious harm under s 162(2) plus imminent
   further harm, while the application is pending; no opportunity to object is
   mentioned. Effective on service; lapses on withdrawal, dismissal, the final order
   taking effect, or the 28th day after it was made unless the Committee fixes a later
   date. A provisional order may do only the things in s 163(2). Asserted.
6. **Terms and effect.** The order must specify its period; the Act sets no minimum or
   maximum (s 163(1)). It may refer to counselling, ban casino entry or gambling, close
   deposit accounts, ban gaming machine rooms and remote gambling (s 163(2), not
   exhaustive). Binding only once served, except where the respondent could not be found
   (s 167(1)). The respondent becomes a casino-excluded person; entering knowing, or when
   he ought to know, is an offence (s 125). INFERENCE: s 125 has no penalty of its own, so
   s 195(2) applies, a fine up to $10,000 or 12 months or both. Winnings are forfeited
   (s 128). An operator admitting him without reasonable excuse faces disciplinary action,
   not prosecution (s 126). Asserted.
7. **No appeal.** The only appeal in Division 3 is for third party orders (s 165(10)).
   A family exclusion order can be set aside on the respondent's application if made in
   his absence (s 165C(3), within a prescribed time), or varied, revoked or swapped for a
   visit limit by the Council on application by a beneficiary family member, or by the
   respondent with permission granted only for a substantial change in circumstances
   (ss 166, 166A). The Council's decision is final (s 166(5)). Asserted.

**Against the expectation** ("a family member may apply; the Committee may make the
order on the statutory grounds"): right in outline, with three refinements. The
applicant must be adversely affected, not merely related. The Committee is the
three-member Committee of Assessors, receiving the application through the Council.
And the provisions are ss 159 to 162 and 164, not 159 to 161 and 163A (163A is the
family visit limit).

**Subsidiary legislation not retrieved:** the rules under s 170 (the prescribed time
and manner for applying to set aside an absence order, s 165C(3)), and the Council's
approved application form (s 159(2)).

## What would need doing before this is worth anything

- Self-exclusion, visit limits and third-party exclusion are the other main patron
  protections and are not encoded.
- The regulations prescribing the premium-player deposit conditions were not retrieved.
- No case law was searched.
