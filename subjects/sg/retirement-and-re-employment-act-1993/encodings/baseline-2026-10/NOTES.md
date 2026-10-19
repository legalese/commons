# Retirement and Re-employment Act 1993 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`: where the
encoding cannot answer it says so with an explicit value (`NOTHING` when no
re-employment offer is due, `no direction, unless the Minister is satisfied`, or a
fact the employee states). No pipeline, no coverage table, no independent test
pass, no human gate. It is not for public use as advice.

This encoding replaces the encoding moved to solutions on 19 October 2026 and the
first-pass encoding `naive-2026-10`. It covers everything the first pass covered
(ss 2, 4, 6, 7, 7A(1), (6), (7), (11), 7C(1), (3), 8(1), 8A, 8B(2)-(4),
8C(1)-(2), 9(2), 9A(2), 9B, 9C, 10) and adds s 7(3), s 7A(2) and (9), s 7B(1) and
(2), s 7C(2)(a)-(b) and (4), s 8(3), (6), (8), s 8B(6), (12), (14) and s 11A. The
first pass's hand-checked values (the specified age as the higher of the two ages,
the 1 July 1952 boundary, the 12-month minimum term, the one-month and six-month
limits, the fines and the $1,000 composition cap) were re-derived from the text and
reused.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/7/2022"), as deposited at `../../registers/source-bundle/RRA1993.txt`. The latest
amendment annotated is Act 38 of 2021, with effect from 1 July 2022.

**Checks:** with the stable `l4` of VS Code extension 1.6.98,
`l4 run rra-cases-retirement.l4` (36 assertions) and
`l4 run rra-cases-remedies.l4` (24 assertions): 60 assertions satisfied,
0 errors, 0 warnings. Both modules also run clean on their own.

| file | what it holds |
|---|---|
| `rra-retirement.l4` | ss 2, 4(1), (2), 6, 7, 7A(1), (2), (6), (7), (9), (11), 7B(1)-(2), 7C(1)-(4), 11A |
| `rra-remedies.l4` | ss 8, 8A, 8B, 8C, and the penalties ss 4(3), 8(7), 8B(13), 9(2), 9A(2), 9B(1), 9C, 10(1) |
| `rra-cases-retirement.l4`, `rra-cases-remedies.l4` | generated fixtures, hand-written expected values |

## Seat

**The employee nearing, at or past retirement age.** The Act is addressed to
employers, the Minister and the Commissioner for Labour, but everything in it lands
on the older employee: when I can be retired, whether my employer must offer me
re-employment or a payment instead, how long a re-employment contract must run,
where I complain and by when, and what the Minister can order for me. Decisions are
named as that employee would ask them (`What is my specified age`,
`Am I eligible for re-employment`, `What must my employer offer me`,
`Where do I take my complaint first`, `Am I in time for the first step`), and the
inputs are facts the employee can state, collected in one record, `My employment`.
The penalties are asked from the same seat: what my employer faces for wronging
me, and the two offences that can be mine (obstructing or lying to an investigating
officer, s 9(2); ignoring a summons, s 9A(2)).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed
  as far as the deposit allows. The instruments that set the two ages — the Gazette
  notifications under s 4(1) and s 7A(11) — are not deposited, so the prescribed
  minimum retirement age and the prescribed re-employment age are facts the
  employee states, and the cases use hypothetical ages (63 and 68). The tripartite
  guidelines (s 11B) and the compounding regulations (s 10(3)) are not deposited
  either and are not encoded.
- **The actors the text names.** Followed: employer (E1), the other employer (E2),
  the Minister, the Commissioner, the Employment Claims Tribunal, investigating
  officers.
- **A judgment handed to someone else, answered conditionally.** Followed for the
  Minister: `What may the Minister direct my employer to do for me` returns
  `no direction, unless the Minister is satisfied` unless the employee states that
  the Minister is satisfied. The employer's assessment of performance (s 7(1)(b)(i))
  is the employer's judgment by the text's own words ("the employer assesses"), so
  the fact asked is that assessment; medical fitness is asked as whether the
  employer has *proved* unfitness, because s 7(2) presumes fitness. **Departed from
  for the suitable vacancy** (s 7C(1)): whether the employer could not find one
  "despite making reasonable attempts" is asked as a fact, though in a dispute it
  is the Minister's to decide (s 8B(6), (7)(b)); a conditional answer there would
  have doubled every outcome of the main decision.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Followed: "specified age", "eligible employee", being "treated as
  dismissed" and "re-employment dispute" are worked out; "contract of service" is
  the case itself, and "claim referral certificate" and "mediation request"
  (borrowed from the Employment Claims Act 2016) are named but not modelled.
- **One case is the text's natural unit.** One employment (`My employment`), one
  complaint, one offence.
- **The Act's own terms, each with a plain gloss.** Followed: "specified age",
  "prescribed minimum retirement age", "prescribed re-employment age",
  "employment assistance payment", "re-employment dispute" are used as the Act
  uses them and glossed in comments.
- **The operative sections in scope; the machinery out.** Followed: s 3
  (officers), s 9(1) and s 9A(1), (3) (investigation powers), delegation, s 11
  (exemptions), s 11B (guidelines), s 12 (regulations) and s 13 are out.
- **Time is counted in whole numbers.** Ages are completed years, which s 2(3)
  supports; the time limits are counted in months the caller supplies, and the
  minimum contract term in months. Calendar dates are not modelled.

## Why this scope

The Act is one of the twelve everyday topics used to choose which statutes to
source across jurisdictions: every older worker in Singapore meets it at the end of
a working life. The scope is what that worker meets: the age below which they
cannot be retired, whether they must be offered re-employment (or a payment in its
place), the length of the contract, and the remedies with their short deadlines.
Left out: s 7A(3) beyond its effect at s 7A(2), s 7A(4), (5) and (10), s 7B(3),
s 7C(2)(c) and (5)-(8), the amounts the Minister or Tribunal fixes (ss 8(4), 8B(10),
8C(3)), conciliation itself (s 8A(5)), the Minister's leave to mediate after
representations (s 8B(7)-(9)), and s 9B(2).

## What the Act turns out to say

1. **The Act does not say what the retirement or re-employment age is.** s 4(1)
   lets the Minister specify the prescribed minimum retirement age by Gazette
   notification, "at least 62 years but not more than 65 years"; s 7A(11) does the
   same for the prescribed re-employment age, 67 to 70. The ages in force are in
   notifications not deposited, so they are inputs, and only the ranges are
   checked. Asserted.

2. **The age I am protected up to and the age I can complain up to differ.** s 4(2)
   forbids dismissal on the ground of age only before the *prescribed minimum
   retirement age*; s 8(1) opens representations to an employee "below the
   *specified* age", which is the higher of that age and any contractual retirement
   age. So an employee whose contract sets a higher age can seek reinstatement for
   a dismissal that is no offence under s 4. (That the gap exists is an inference
   from the two provisions read together.) Asserted.

3. **The duty to re-employ gives way only to no vacancy plus a payment or a new
   employer.** s 7A(1) is "Subject to section 7C", and s 7C(1) displaces it only
   where the employer cannot find a suitable vacancy "despite making reasonable
   attempts" *and* either offers an employment assistance payment or another
   employer's offer is accepted. Read that way, taking up another employer's offer
   while my own employer has a vacancy does not, by s 7C(1), end my employer's
   obligation (an inference from how s 7C(1) is built). Asserted.

4. **Saying I will not continue ends both the offer and the payment.** s 7A(9) lets
   an eligible employee who does not wish to continue "retire or be retired", and
   s 7C(3) removes the payment for an employee who has said so, even where no
   vacancy was found. Asserted.

5. **Eligibility is a birth date and two employer findings, one of them presumed in
   my favour.** Born on or after 1 July 1952, assessed by the employer as at least
   satisfactory, and medically fit, which is presumed unless the employer proves
   otherwise on a balance of probabilities (s 7(1), (2)). An employer not intending
   to re-employ for performance or fitness must, "as far as it is reasonably
   practicable", give written notice "within a reasonable period" before ending the
   employment (s 7(3)); no number of days is set. Asserted.

6. **The deadlines are short, and the clock starts in different places.** One
   month from the dismissal for an age dismissal (s 8(1)); one month from the last
   day of employment to notify the Commissioner of a denial of re-employment or a
   dismissal without just cause (s 8A(1), (2)); six months from the last day for a
   mediation request over the terms offered or the amount of the payment (s 8A(3)).
   The just-cause route is only for an employee who attained the specified age on
   or after 1 January 2012. Asserted.

7. **s 8B says both "at any time" and "no later than one month".** s 8B(1) allows
   representations "at any time after any conciliation"; s 8B(2) requires them "no
   later than one month after the conclusion of any conciliation". The encoding
   follows s 8B(2). Asserted (the one-month limit).

8. **For a dismissed employee, choosing one route closes the other two.**
   Representations under s 8B, representations under s 35(3) of the Industrial
   Relations Act 1960, and a Tribunal claim over the amount of the payment each bar
   the others for that dismissal (ss 8B(3), (4), 8C(2)). Asserted.

9. **The Minister's direction is final and ends a damages claim.** What the Minister
   may direct is reinstatement with the lost salary or compensation (s 8(3)), or
   re-employment or compensation (s 8B(6)), each only if satisfied; a direction bars
   any action for damages (ss 8(6), 8B(12)); an unpaid amount is recoverable by the
   court as if it were a fine, but only after the employer is convicted
   (ss 8(8), 8B(14)). Asserted.

10. **A re-employment contract runs at least a year, unless less is left or I agree
    otherwise** (s 7A(6), (7)). Asserted.

11. **Earlier service is wiped for the re-employment contract, with two exceptions.**
    Unless agreed, service before re-employment "is disregarded" (s 7B(1)), except
    for the 3-month minimum for annual leave and the service period for paid sick
    leave under the Employment Act 1968 (s 7B(2)). Asserted.

12. **The $1,000 limb of composition always binds.** s 10(1) caps a composition sum
    at the lower of half the maximum fine and $1,000. Every fine in this Act is at
    least $5,000, so half is at least $2,500 and the cap is always $1,000 (an
    inference from the penalties read together). Which offences are compoundable is
    left to regulations not deposited. Asserted.

13. **The employee can be the offender.** Ignoring a summons (s 9A(2)) carries no
    stated penalty, so s 9C applies: $5,000 or 6 months, and $10,000 or 12 months
    for a subsequent offence under the same section. Asserted.

## What would need doing before this is worth anything

- Deposit the Gazette notifications fixing the prescribed minimum retirement age
  and the prescribed re-employment age, and bring the ages in as data.
- Deposit the tripartite guidelines on re-employment and the employment assistance
  payment, and the compounding regulations.
- Model dates and calendar months instead of whole numbers of months and years.
- Decide whether the suitable-vacancy question should be answered conditionally on
  the Minister's view, as the defaults would have it.
- An independent test pass; no case law, Ministry decisions or Tribunal awards were
  searched.
