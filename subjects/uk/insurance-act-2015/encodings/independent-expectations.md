# Independent expectations: Insurance Act 2015 (Parts 1-4, s 22, Sch 1 Part 1)

Written from BRIEF.md and `../registers/source-bundle/ukpga-2015-4.txt` only, before any `.l4` file was opened.
Every scenario gives the inputs, the expected answer and the Act's words. Amounts are in pounds.

## Readings taken (ambiguities)

- R1. **Relevant period** (s 22(3)): "the period of 18 months beginning with the day on which this Act is passed" (12 Feb 2015) ends at the end of 11 Aug 2016. "Entered into after the end of the relevant period" means entered into on or after 12 Aug 2016 (brief).
- R2. **Consumer contracts**: s 2(1) confines Part 2 (fair presentation) to non-consumer contracts. Parts 3 and 4 (ss 10-12) speak of "a contract of insurance" and s 22(2) does not restrict them to non-consumer contracts. The brief's goal is about a business insured; I treat "consumer" as taking the contract outside Part 2 at least. I do not assert what the encoding does for ss 10-12 on a consumer contract beyond "Part 2 does not apply".
- R3. **Circumstance test**: a circumstance is a problem only if it is material (s 7(3)) and the insured knows or ought to know it (s 3(4)(a)). It is then satisfied if (i) disclosed, or (ii) "failing that" the disclosure put a prudent insurer on notice (s 3(4)(b)), or (iii) "in the absence of enquiry" an exception in s 3(5)(a)-(e) applies. If the insurer enquired, no s 3(5) exception helps.
- R4. **Fair presentation as a whole** (s 3(3)): every circumstance satisfied AND manner reasonably clear and accessible (b) AND representations substantially correct / made in good faith (c). Failure of any limb = breach.
- R5. **Qualifying breach** (s 8(1), (3)): breach AND insurer shows that but for the breach it would not have entered at all, or only on different terms. A higher premium is a "different term" for s 8(1)(b).
- R6. **Deliberate or reckless** (s 8(5)-(6)): knew it was in breach OR did not care, as shown by the insurer. Only meaningful for a qualifying breach.
- R7. **Sch 1 para 6**: X = (premium actually charged ÷ higher premium) × 100; payable = X% of what would otherwise be payable under the contract terms, or under the para 5 different terms if the insurer so requires.
- R8. **Para 5** applies only "if the insurer so requires"; otherwise the original terms govern.
- R9. **s 10(2) dates** (brief): suspended for a loss on a day strictly after the breach day and strictly before the remedy day. A loss on the breach day or on the remedy day is covered. A never-remedied breach suspends cover for every loss after the breach day.
- R10. **s 12(2)(a) dates** (brief): insurer may refuse liability for a relevant event on a day strictly after the fraudulent act day. An event on the fraud day itself is not "after", so termination does not let the insurer refuse it (s 12(3) protects "before"; the same day falls in neither; I take liability as unaffected).
- R11. **s 11**: if the term is risk-reducing (not defining the risk as a whole), was not complied with, and the insured shows the non-compliance could not have increased the risk of the loss as it occurred, the insurer may not rely on it. Otherwise the insurer may rely on the non-compliance and (in this model) pays nothing on the claim.
- R12. **Overall amount**: zero if the claim itself is fraudulent (s 12(1)(a)); zero if the contract was terminated for an earlier fraud and the loss is after the fraudulent act; zero if suspended (s 10(2)); zero if the insurer relies on s 11 non-compliance; zero if the insurer avoids (Sch 1 paras 2, 4); otherwise the claim (under para 5 terms where required) times X% where para 6 applies; otherwise the full claim.
- R13. Where the Act does not apply (contract entered on or before 11 Aug 2016) the Act gives no answer on the amount; I expect the encoding to refuse or to report "does not apply", not to compute an amount under the Act.

## A. Application (ss 1, 2(1), 22)

| # | Inputs | Expected | Act |
|---|---|---|---|
| A1 | non-consumer, entered 12 Aug 2016 | applies | s 22(1)(a),(2),(3) "after the end of the relevant period" |
| A2 | non-consumer, entered 11 Aug 2016 | does not apply | last day of the 18 months beginning with 12 Feb 2015 |
| A3 | non-consumer, entered 12 Feb 2015 | does not apply | first day of the period |
| A4 | non-consumer, entered 1 Jan 2020 | applies | |
| A5 | non-consumer, entered 12 Feb 2016 | does not apply | within period |
| A6 | consumer, entered 1 Jan 2020 | Part 2 does not apply | s 2(1) "non-consumer insurance contracts only" |
| A7 | consumer, entered 11 Aug 2016 | does not apply | both limbs fail |
| A8 | non-consumer, entered 13 Aug 2016 | applies | |

## B. Fair presentation, circumstance by circumstance (s 3)

Each circumstance is material unless stated.

| # | Inputs | Circumstance satisfied? | Act |
|---|---|---|---|
| B1 | known, disclosed | yes | s 3(4)(a) |
| B2 | known, not disclosed, no notice, no enquiry, no exception | no (breach) | s 3(4)(a) |
| B3 | ought to know (not actually known), not disclosed, nothing else | no | s 3(4)(a) "knows or ought to know" |
| B4 | neither knows nor ought to know, not disclosed | yes | s 3(4)(a) |
| B5 | known, not disclosed, notice given | yes | s 3(4)(b) "failing that ... put a prudent insurer on notice" |
| B6 | not disclosed, no enquiry, diminishes risk | yes | s 3(5)(a) |
| B7 | not disclosed, no enquiry, insurer knows | yes | s 3(5)(b) |
| B8 | not disclosed, no enquiry, insurer ought to know | yes | s 3(5)(c) |
| B9 | not disclosed, no enquiry, insurer presumed to know | yes | s 3(5)(d) |
| B10 | not disclosed, no enquiry, insurer waives information | yes | s 3(5)(e) |
| B11 | not disclosed, insurer enquired, diminishes risk | no | s 3(5) "In the absence of enquiry" |
| B12 | not disclosed, insurer enquired, insurer knows | no | same |
| B13 | not disclosed, insurer enquired, waiver | no | same |
| B14 | disclosed, insurer enquired | yes | s 3(4)(a) |
| B15 | not disclosed, insurer enquired, notice given | yes | s 3(4)(b) (enquiry only switches off s 3(5)) |
| B16 | not material, known, not disclosed | yes | s 3(4)(a) "material circumstance"; s 7(3) |

## C. Presentation as a whole (s 3(3)) and breach

| # | Inputs | Expected | Act |
|---|---|---|---|
| C1 | all circumstances ok, clear and accessible, reps correct/good faith | fair presentation, no breach | s 3(3) |
| C2 | all ok but not reasonably clear and accessible | breach | s 3(3)(b) |
| C3 | all ok, clear, but a material factual representation not substantially correct | breach | s 3(3)(c) |
| C4 | one of two circumstances fails (B2), rest fine | breach | s 3(3)(a),(4) "every material circumstance" |
| C5 | no circumstances at all, clear, correct | fair presentation | |
| C6 | two circumstances: one disclosed, one excepted under 3(5)(b) | fair presentation | |

## D. Qualifying breach and deliberate/reckless (s 8)

| # | Inputs | Expected | Act |
|---|---|---|---|
| D1 | breach; insurer would have entered on same terms, same premium | not qualifying; no remedy | s 8(1) "only if" |
| D2 | breach; would not have entered at all | qualifying | s 8(1)(a) |
| D3 | breach; different (non-premium) terms | qualifying | s 8(1)(b) |
| D4 | breach; higher premium only | qualifying | s 8(1)(b) |
| D5 | no breach; insurer says it would not have entered | not qualifying | no breach |
| D6 | qualifying, insured knew it was in breach | deliberate or reckless | s 8(5)(a) |
| D7 | qualifying, insured did not care | deliberate or reckless | s 8(5)(b) |
| D8 | qualifying, neither | not deliberate or reckless | s 8(4)(b) |
| D9 | not qualifying, insured knew | no remedy; amount unaffected | s 8(1) |

## E. Sch 1 Part 1 remedies and worked numbers (claim £100,000 unless stated)

| # | Inputs | Expected | Act |
|---|---|---|---|
| E1 | deliberate/reckless | avoid, refuse all claims, keep premiums; pay 0 | para 2(a),(b) |
| E2 | innocent; would not have entered on any terms | avoid, refuse all claims, return premiums; pay 0 | para 4 |
| E3 | innocent; different terms required by insurer, claim under those terms £60,000; same premium | pay £60,000 | para 5 |
| E4 | innocent; different terms, insurer does not require them; same premium | pay £100,000 | para 5 "if the insurer so requires" |
| E5 | innocent; premium charged £10,000, higher premium £15,000; same terms | X = 66.67; pay £66,666.67 (2/3) | para 6 |
| E6 | innocent; charged £1,000, higher £2,000 | X = 50; pay £50,000 | para 6 |
| E7 | innocent; different terms (claim £80,000) AND charged £8,000, higher £10,000 | X = 80; pay £64,000 | paras 5 and 6 "(or, if applicable, under the different terms ... paragraph 5)" |
| E8 | innocent; different terms (claim £0, excluded under those terms) AND higher premium | pay 0 | paras 5, 6 |
| E9 | deliberate even though insurer would have charged higher premium only | pay 0 (para 2 governs, paras 4-6 do not apply) | para 3 "Paragraphs 4 to 6 apply if ... neither deliberate nor reckless" |
| E10 | no qualifying breach (D1) | pay £100,000 | s 8(1) |
| E11 | innocent; charged £3,000, higher £4,000, claim £20,000 | X = 75; pay £15,000 | para 6 |
| E12 | innocent; would not have entered at all and also says higher premium | para 4: pay 0, return premiums | para 4 |

## F. s 10 suspension (loss date; breach and remedy dates)

Breach 10 Mar 2020, remedy 20 Mar 2020 unless stated.

| # | Inputs | Insurer liable? | Act |
|---|---|---|---|
| F1 | loss 15 Mar 2020 | no | s 10(2) |
| F2 | loss 10 Mar 2020 (breach day) | yes | brief R9: strictly after |
| F3 | loss 11 Mar 2020 | no | |
| F4 | loss 19 Mar 2020 | no | |
| F5 | loss 20 Mar 2020 (remedy day) | yes | brief R9: strictly before |
| F6 | loss 21 Mar 2020 | yes | s 10(4)(b) |
| F7 | loss 9 Mar 2020 | yes | s 10(4)(a) |
| F8 | never remedied, loss 1 Jan 2021 | no | s 10(2) "before the breach has been remedied" |
| F9 | never remedied, loss 10 Mar 2020 | yes | |
| F10 | never remedied, loss 11 Mar 2020 | no | |
| F11 | loss 15 Mar 2020, warranty ceased to be applicable | yes | s 10(3)(a) |
| F12 | loss 15 Mar 2020, compliance rendered unlawful | yes | s 10(3)(b) |
| F13 | loss 15 Mar 2020, insurer waived | yes | s 10(3)(c) |
| F14 | no breach of warranty, loss 15 Mar 2020 | yes | |
| F15 | never remedied, loss 1 Jan 2021, insurer waived | yes | s 10(3)(c) |
| F16 | breach 31 Dec 2020, remedy 1 Jan 2021, loss 1 Jan 2021 | yes (no intervening day) | R9 |

## G. s 11 terms not relevant to the actual loss

| # | Inputs | Insurer may rely on non-compliance? | Act |
|---|---|---|---|
| G1 | risk-reducing term, not complied with, insured shows could not have increased risk | no | s 11(2),(3) |
| G2 | same but insured cannot show | yes | s 11(2) "if the insured satisfies subsection (3)" |
| G3 | term defines the risk as a whole, not complied with, insured shows | yes (s 11 does not apply) | s 11(1) "other than a term defining the risk as a whole" |
| G4 | term complied with | no (nothing to rely on) | s 11(2) "the term has not been complied with" |
| G5 | term not risk-reducing of a kind/location/time | s 11 does not apply; reliance per contract (yes) | s 11(1) |

## H. s 12 fraudulent claims

Fraudulent act 1 Jun 2021.

| # | Inputs | Expected | Act |
|---|---|---|---|
| H1 | this claim fraudulent | insurer not liable for it; pay 0; may recover sums paid | s 12(1)(a),(b) |
| H2 | earlier claim fraudulent, contract treated as terminated; this event 2 Jun 2021 | may refuse; pay 0 | s 12(2)(a) |
| H3 | terminated; this event 31 May 2021 | not affected; pay | s 12(3) |
| H4 | terminated; this event 1 Jun 2021 (same day) | not refusable (R10); pay | s 12(2)(a) "after" |
| H5 | earlier fraud but insurer did not terminate; event 2 Jun 2021 | pay (no termination) | s 12(2) "If the insurer does treat the contract as having been terminated" |
| H6 | terminated; premiums | need not return premiums | s 12(2)(b) |
| H7 | no fraud | pay | |

## I. Overall amount payable (claim £100,000, contract entered 1 Jan 2020, non-consumer)

| # | Inputs | Expected |
|---|---|---|
| I1 | fair presentation, no warranty breach, no fraud | £100,000 |
| I2 | innocent breach, higher premium £10,000 vs £12,500 | £80,000 |
| I3 | as I2 + loss inside s 10 suspension | 0 |
| I4 | as I2 + loss on remedy day | £80,000 |
| I5 | fair presentation, fraudulent claim | 0 |
| I6 | deliberate breach | 0 |
| I7 | fair presentation, s 11 term breached and insured shows | £100,000 |
| I8 | fair presentation, s 11 term breached, insured cannot show | 0 |
| I9 | paras 5+6: different-terms claim £80,000; £8,000 vs £10,000 | £64,000 |
| I10 | contract entered 11 Aug 2016 | Act does not apply (refuse / not computed) |
| I11 | terminated for earlier fraud on 1 Jun 2021, loss 2 Jun 2021 | 0 |
| I12 | terminated for earlier fraud on 1 Jun 2021, loss 31 May 2021, innocent breach 50% premium | £50,000 |
