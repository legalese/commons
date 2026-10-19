# Pensions Act 1956 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`, no
`BECAUSE`: a case the encoding does not cover answers `NOTHING`, with a comment
saying why. No pipeline, no coverage table, no independent test pass, no human
gate. Not for public use as advice.

This encoding replaces the encoding moved to solutions on 2026-10-19 and the
first-pass encoding `naive-2026-10`. It covers every provision the first pass
covered and reuses its hand-checked figures where they still hold (the reg 4
rate and cap, reg 16, reg 18, s 20). Two first-pass answers are changed: see
findings 4 and 6.

**Edition:** 2020 Revised Edition (all amendments up to and including
1 December 2021, in operation 31 December 2021), informal consolidation in force
from 14/1/2022, last amendment Act 33 of 2021, as deposited at
`../../registers/source-bundle/PA1956.txt`. The First Schedule Pensions
Regulations are part of that text. No later regulations varying them, and no
Gazette order varying the commutation factor (175.14) or the discount rate (5%),
were deposited.

**Checks:** one module (`pen-pension.l4`), one case file
(`pen-cases-pension.l4`, built by the scratchpad generator
`gen_pensions-act-1956_baseline.py`), 59 assertions satisfied, 0 errors, 0
warnings, with the stable `l4` of VS Code extension 1.6.98.

## Seat

**The public officer in a pensionable office, and the pensioner that officer
becomes**; for s 20, the officer's dependants, who receive the death gratuity.
The Act is about what that person may be granted, when, how much, and what can
take it away. Almost every provision is written as a power of the President or
a Pension Authority. Each is encoded as what it means for the officer: whether
a pension *can* be granted, whether it *can* be withheld or stopped, at what age
the officer *can* be made to retire or called back.

Decisions are phrased as the officer asks: `Does the Act apply to me`, `Am I old
enough to retire on pension`, `Can I be granted a pension on my retirement`,
`What is my minimum age`, `At what age can I be required to retire`, `What annual
pension can I be granted`, `What is the most gratuity I can be granted for too
short a service`, `What pension can I be granted on the abolition of my office`,
`Can my pension be withheld, cancelled or reduced`, `Can I choose`, `What am I
treated as having chosen`, `Will I be paid a monthly pension`, `What gratuity do
I get with a reduced pension`, `What reduced annual pension do I get`, `What
commuted pension gratuity do I get`, `Is my full pension restored`, `Can my
pension be assigned to satisfy`, `Can my pension be attached for`, `Can I be
called back to serve`, `Has my pension ceased for bankruptcy`, `Can my pension be
stopped for my conviction`, `Can my pension be stopped for taking up work`, `What
gratuity will my dependants get if I die in service`, `What will my dependants
get if I die within a year of retiring`, `What annual injury allowance can I be
granted before any reduction`.

The 2026-10-18 defaults:

- **The Act alone, instruments brought in:** followed. The instrument that sets
  the numbers, the Pensions Regulations, is the Act's own First Schedule and is
  brought in. The President's designations of schemes (s 3(4)(a)) and
  pensionable offices (s 2) were not deposited and are asked as facts.
- **The actors the text names:** followed. The officer, the President, the
  Pension Authority, the officer's dependants and legal personal representative,
  the Government as creditor, the wife, former wife or minor child under a
  maintenance order.
- **A judgment handed to someone else answered conditionally:** followed. The
  President's medical satisfaction (s 11(2)(c)), consent (s 11(2)(a), (h), (i)),
  direction of 55 (s 13), written permission (s 19), and the Pension Authority's
  satisfaction of misconduct (s 8(2)) and leave to opt late (reg 15(2)) are
  inputs. Where the law only lets an official act (ss 18, 19), the answer is
  "can be stopped", never "is stopped".
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts:** followed for "minimum age" (s 11(6)) and "commutation factor" (s 20(4),
  reg 16(3)). Departed from for "pensionable service" and "pensionable
  emoluments" (s 2, regs 3 and 5 to 13): working them out needs the whole
  service history, so the baseline takes two inputs, complete months of
  pensionable service and annual pensionable emoluments, and says so.
- **One case is the text's natural unit:** followed. One officer, one
  retirement (or one death).
- **The Act's own terms, each with a plain gloss:** followed, in comments beside
  each type, field and decision.
- **Operative sections in scope, machinery out:** followed. Pension
  Authorities, delegation, the regulation-making power, the Pension Fund, and
  repeal and saving (ss 4 to 7, 10, 21) are out.

## Why this scope

The Act and its regulations run to 29 regulations and two tables. The baseline
keeps to what a pensionable officer meets: whether the Act reaches them, the
grounds and ages on which a pension can be granted, the rate and the cap, the
option they must make before retiring, the things that can take the pension away
or reach it, the death gratuity and the injury allowance rate. Left out: the
transitional savings for officers in service in 1956 or on the Malayan
Establishment (s 3(2), (3), reg 4(2)); the Gurkha provisions; candidates for
election (s 11(3)); suspension under s 11(4), (5), (7) and the related s 20(3);
the caps for other public service (s 14(2) to (6)); s 20(1)(b) to (d) and
(2)(b); the discounted commuted gratuity (reg 16(2)(b)); re-employment (reg 17);
killed-on-duty and police compensation (regs 21 to 23); non-pensionable offices
(regs 24, 25, 27, Table B); Table A; the CPF split of the commuted gratuity
(reg 15(6) to (8)); and the injury allowance's reductions, caps and Work Injury
Compensation election (reg 20(2) to (14)).

## What the Act turns out to say

1. **If you don't choose, you lose the pension.** Reg 15(4): an officer who has
   not exercised an option "is deemed to have opted to receive a commuted pension
   gratuity ... without any pension". The option must be made by the day before
   retirement (reg 15(2)); a later choice counts only if the Pension Authority
   allows it as equitable. Once made it is irrevocable (reg 15(3)). The deadline
   is encoded as a decision, not a regulative rule, because missing it is not a
   breach: it is a deemed choice. Asserted.

2. **The commutation factor does not say what it multiplies.** Reg 16(2)(a) and
   s 20(1)(a): the lump sum is the commutation factor (175.14) times "the amount
   of such pension". Neither says annual or monthly. Times the annual pension it
   would be 175 years' pension; times the monthly pension, about 14.6 years'.
   **The encoding takes the monthly figure. That is an inference; the text does
   not state it.** On that reading, 30 years on $60,000 commutes to $525,420.
   Asserted.

3. **The rate, the cap, and the faster rate on abolition.** Reg 4: at least 10
   years, then 1/600 of annual pensionable emoluments per complete month; s 14
   caps the pension at two-thirds, so **400 months (33 years 4 months) reaches
   the cap**. Under 10 years, reg 26 allows a gratuity "not exceeding" 5/600 per
   month instead. On abolition or reorganisation, reg 18 accrues 1/500 per month
   for the first 240 months, but reg 18(2) caps it at the reg 4 pension the
   officer would have had by serving to compulsory retirement age: 25 years at
   abolition gives $34,800 on $60,000 if 400 months were possible, $30,000 if
   only 300. Asserted.

4. **On the text, a woman appointed after 1962 has no pension age of her own in
   s 11(2)(a).** s 11(2)(a) gives "55 years if a man, or of 45 years if a woman,
   except that in the case of a female officer she was in the service before
   1 March 1962 and has opted" for 45. Read as written, the woman's 45 is
   confined to that exception, and no age is given to any other woman: her age
   limb is (h), 50 with the President's consent. A woman of 56 appointed in 1980
   without consent is not "old enough to retire on pension" by age alone. **This
   is a reading, labelled as such**; the first-pass encoding gave her 55, which
   the text does not say. s 13 has a matching gap: it gives a compulsory
   retirement age to a woman appointed on or after 1 March 1962 (60, or 55 by
   direction) but none to a woman appointed before then. Asserted.

5. **Sex-specific rules remain on the face of the Act.** s 16: a pensioner can be
   called back until 50 if a man, 45 if a woman. s 15: a pension can be assigned
   to satisfy a maintenance order for the officer's "wife or former wife or minor
   child", but not one for a husband. s 17(3) and s 18(3) let the Authority pay a
   stopped pension to "any wife, child or children" (not encoded). Asserted for
   ss 15 and 16.

6. **Assignment and attachment are not the same.** s 15 lets a pension be
   assigned or transferred to satisfy a Government debt or a maintenance order
   for a wife, former wife or minor child, but it can be "attached, sequestered
   or levied upon" only for "a debt due to the Government". The first pass
   treated both maintenance claims as able to "reach" the pension; the baseline
   separates the two. Asserted.

7. **Bankruptcy stops the pension at once; conviction and private work only let
   it be stopped.** s 17(2): the pension "immediately ceases" on bankruptcy and
   is restored from discharge (s 17(5)); an undischarged bankrupt at retirement
   cannot be granted one (s 17(1)). s 18: a sentence of death, penal servitude
   or imprisonment (not a fine) lets the Authority stop it, undone by a free
   pardon. s 19: taking a directorship, employment or occupation for gain in
   Singapore or Malaysia without the President's prior written permission lets
   the President stop it, but only for 5 years after retirement. Asserted.

8. **Most officers appointed since 1 April 1986 are outside the Act, but not
   outside s 20.** s 3(4)(a) excludes them unless the President has designated
   their scheme. s 20(5) applies the death gratuity to officers "whether appointed
   before or after 1 April 1986". Asserted for s 3.

9. **The death-in-service gratuity is never less than a year's emoluments.**
   s 20(1)(a): the commuted value of the ill-health pension, but "in no case ...
   less than one year's pensionable emoluments". An officer with 5 years'
   service has no reg 4 pension, so dependants get the floor, $60,000 on
   $60,000. Under the minimum age the sum is discounted at 5% "in respect of each
   year or part thereof", but the text does not say whether simply or
   compounded, so that case answers `NOTHING`. Death within a year of retirement
   tops the dependants up to one year's emoluments, less what has been paid
   (s 20(2)). Asserted.

10. **The minimum age has a gap.** s 11(6)(c) gives an officer appointed on or
    after 12 September 1986 a minimum age of 50 if entitled to retire at 50 or
    55, and 55 if entitled to retire at 60. Any other retirement age falls in no
    limb, and answers `NOTHING`. Asserted.

11. **Nothing is of right.** s 8(1): no officer has "an absolute right" to a
    pension, so every "can be granted" is a permission. s 8(2) lets the Pension
    Authority withhold for negligence, irregularity or misconduct, and reg 28
    lets it cancel or reduce a pension obtained by wilful suppression or granted
    in ignorance of facts that would have justified dismissal. Asserted.

12. **The injury allowance rate is a table.** Reg 20(1): 5, 10, 15 or 20
    sixtieths of emoluments at the date of injury as capacity is slightly
    impaired, impaired, materially impaired or totally destroyed; reg 20(11)
    raises these to 7½, 15, 22½ and 30 for an injury in an aircraft on official
    instructions. Encoded as data, before any reduction under reg 20(3).
    Asserted.

## What would need doing before this is worth anything

- **Confirm the commutation factor's base** (finding 2) against the Pension
  Authority's practice or any amending order, and the discount method
  (finding 9).
- **Check finding 4** against how the Public Service Division actually applies
  s 11(2)(a) to women appointed after 1962; the reading here is literal.
- Reg 12 (which emoluments to use, including three-year averaging) and regs 3, 5
  to 11 and 13 (what counts as pensionable service) are reduced to two inputs.
- The President's designations under s 3(4)(a) and s 2, and any regulations
  varying the First Schedule, were not retrieved. Nor was any case law.
- An independent test pass, and a human gate, before anyone relies on it.
