# Independent expectations — Consumer Insurance (Disclosure and Representations) Act 2012

Written from BRIEF.md and the source text (revised, PiT 12 August 2016) only, before
any `.l4` file was opened. Each scenario gives inputs, the expected answer, and the
words of the Act that give it.

Default facts unless a scenario says otherwise ("the base case"): an individual,
contracting wholly for private purposes, with a person carrying on the business of
insurance who becomes a party by way of that business; contract (not a variation)
entered into on 1 June 2014; consumer did not take reasonable care; premium actually
charged £300; premiums paid £300; claim under the actual terms £10,000.

## Readings taken where the Act is ambiguous or silent

1. **Commencement date.** The Act does not state the day it came into force; s 12(2)
   leaves it to a Treasury order, and s 12(3) bars a day earlier than one year from
   Royal Assent (8 March 2012). The order (SI 2013/450) appointed **6 April 2013**. I
   read "entered into ... after the Act comes into force" (s 12(4)) as covering a
   contract made on 6 April 2013 itself (the Act is in force from the start of that
   day, so a contract made during it is made after it came into force). Contracts on
   5 April 2013 or earlier are outside the Act. A contract made on 6 April 2013 is
   therefore *in* — flagged as a reading.
2. **"Different terms" in s 4(1)(b) includes the premium.** Para 7 ("whether the
   terms relating to matters other than the premium would have been the same or
   different") and para 6 ("different terms (excluding terms relating to the
   premium)") show that the premium is a term; so an insurer that would only have
   charged a higher premium "would have done so only on different terms" and the
   misrepresentation qualifies.
3. **A higher premium means strictly higher.** If the premium the insurer would have
   charged equals the premium charged, para 7 does not apply (X would be 100 anyway).
4. **Para 6 is at the insurer's option** ("if the insurer so requires"). Where the
   encoding asks whether the insurer requires it, I expect the claim to be measured
   under the different terms only when it does.
5. **Para 9 with an outstanding claim.** Para 9(1)(b) "does not relate to any
   outstanding claim" is read as limiting what para 9 governs (it does not change how
   a pending claim is treated), not as switching para 9 off whenever some claim is
   pending. The future-treatment rights are therefore still available.
6. **Para 9 where the insurer would not have contracted at all.** Para 9(2) applies
   para 5 for the future, so the insurer may avoid (returning premiums); para 9(4)
   (notice / termination) is triggered only by para 6 or 7 rights, so it is *not*
   available in that case.
7. **s 5(5)(a) — knowledge of a reasonable consumer.** If a reasonable consumer would
   have known the statement was untrue (and that the matter was relevant), the
   consumer is presumed to have known it unless the contrary is shown. Where the
   contrary is shown, the insurer must prove the actual state of mind (s 5(4)).
8. **Dishonesty and class.** s 3(5) makes dishonesty show lack of reasonable care
   (breach), but class under s 5 is decided only by s 5(2); I give no expectation that
   a "dishonest" flag alone makes the misrepresentation deliberate or reckless.
9. **Remedies require a qualifying misrepresentation.** s 4(1): the insurer has a
   remedy "only if" both limbs hold; otherwise the claim is paid in full under the
   actual terms and no premium question arises.
10. **Para 8 X.** X = (premium actually charged ÷ higher premium) × 100, not rounded;
    amount payable = X% of the claim under the actual (or para 6) terms.

## Goal 1 — does the Act apply (ss 1, 12(4))

| # | Inputs (differences from base) | Expected | Act's words |
|---|---|---|---|
| A1 | base case | applies | s 1 "an individual who enters into the contract wholly ... for purposes unrelated to ... trade"; s 12(4) "entered into ... after the Act comes into force" |
| A2 | individual, *mainly* private purposes | applies | s 1 "wholly or mainly" |
| A3 | individual, mainly business purposes | does not apply | s 1 "wholly or mainly for purposes unrelated to the individual's trade, business or profession" |
| A4 | policyholder is a company, not an individual | does not apply | s 1 "an individual" |
| A5 | other party does not carry on the business of insurance | does not apply | s 1 "a person who carries on the business of insurance" |
| A6 | insurer carries on insurance business but not party by way of that business | does not apply | s 1 "becomes a party to the contract by way of that business" |
| A7 | insurer lacks FSMA permission, otherwise base | applies | s 1 "(whether or not in accordance with permission ... FSMA 2000)" |
| A8 | entered 5 April 2013 | does not apply | s 12(4) "after the Act comes into force" |
| A9 | entered 7 April 2013 | applies | s 12(4) |
| A10 | entered 6 April 2013 | applies (reading 1) | s 12(4) |
| A11 | entered 8 March 2012 (Royal Assent) | does not apply | s 12(2) "otherwise this Act comes into force on such day as the Treasury ... appoint"; s 12(3) |
| A12 | entered 1 January 2013 | does not apply | s 12(3)/(4) |
| A13 | entered 1 June 2014 but mainly business | does not apply | s 1 |

## Goal 2 — qualifying misrepresentation (ss 2(2), 3(5), 4(1))

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| Q1 | no reasonable care; insurer would not have entered at all | qualifying | s 4(1)(a),(b) "would not have entered into the contract ... at all" |
| Q2 | reasonable care taken; not dishonest; insurer would not have entered | not qualifying | s 4(1)(a) "in breach of the duty set out in section 2(2)" |
| Q3 | finding of reasonable care, but misrepresentation dishonest; would not have entered | qualifying | s 3(5) "A misrepresentation made dishonestly is always to be taken as showing lack of reasonable care" |
| Q4 | no reasonable care; insurer would have entered on the same terms and same premium | not qualifying | s 4(1)(b) |
| Q5 | no reasonable care; same non-premium terms; would have charged £400 (charged £300) | qualifying | s 4(1)(b) "only on different terms"; reading 2 |
| Q6 | no reasonable care; would have added an exclusion; same premium | qualifying | s 4(1)(b) |
| Q7 | no reasonable care; exclusion and higher premium | qualifying | s 4(1)(b) |
| Q8 | reasonable care; higher premium only | not qualifying | s 4(1)(a) |
| Q9 | no reasonable care; higher premium equal to charged (£300) | not qualifying | s 4(1)(b); reading 3 |
| Q10 | dishonest, reasonable care, higher premium only | qualifying | s 3(5), s 4(1)(b) |
| Q11 | Act does not apply (company policyholder), otherwise as Q1 | no qualifying misrepresentation under the Act | s 4(1) "a consumer insurance contract" |

## Goal 2 — class (s 5)

All on a qualifying misrepresentation (as Q1).

| # | State of mind facts | Expected | Act's words |
|---|---|---|---|
| C1 | knew untrue; knew relevant | deliberate or reckless | s 5(2)(a) "knew that it was untrue", (b) "knew that the matter ... was relevant" |
| C2 | did not care whether untrue; knew relevant | deliberate or reckless | s 5(2)(a) "did not care whether or not it was untrue" |
| C3 | knew untrue; did not care whether relevant | deliberate or reckless | s 5(2)(b) "did not care whether or not it was relevant" |
| C4 | did not care untrue; did not care relevant | deliberate or reckless | s 5(2) |
| C5 | knew untrue; shown not to know relevant and cared; no clear question; no presumption | careless | s 5(2)(b) not met; s 5(3) |
| C6 | honestly believed true (shown not to know, cared); knew relevant | careless | s 5(2)(a) not met; s 5(3) |
| C7 | nothing shown about the state of mind; no clear question; reasonable consumer would not have known | careless | s 5(4) "It is for the insurer to show..."; s 5(3) |
| C8 | knew untrue shown; relevance not shown; insurer asked a clear and specific question about the matter; contrary not shown | deliberate or reckless | s 5(5)(b) "presumed ... that the consumer knew that a matter about which the insurer asked a clear and specific question was relevant" |
| C9 | as C8 but the contrary is shown (consumer did not know relevance) | careless | s 5(5) "unless the contrary is shown" |
| C10 | consumer's knowledge not shown; reasonable consumer would have known untrue and relevant; contrary not shown | deliberate or reckless | s 5(5)(a) "the consumer had the knowledge of a reasonable consumer" |
| C11 | as C10, contrary shown (consumer lacked that knowledge) | careless | s 5(5) "unless the contrary is shown"; s 5(4) |
| C12 | knew untrue; clear and specific question asked but question not about this matter... (encoded as no clear question) | careless | s 5(5)(b) applies only to "a matter about which the insurer asked" |
| C13 | not qualifying misrepresentation (reasonable care) | no class | s 5(1) classifies only "a qualifying misrepresentation" |

## Goal 3 — remedies (Sch 1 Part 1)

### Para 2 — deliberate or reckless

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R1 | D/R; premiums paid £1,200; nothing unfair | may avoid; refuse all claims (pay £0); return £0 | para 2(a) "may avoid the contract and refuse all claims", (b) "need not return any of the premiums paid" |
| R2 | D/R; paid £1,200; £300 unfair to retain | may avoid; pay £0; return £300 | para 2(b) "except to the extent (if any) that it would be unfair ... to retain them" |
| R3 | D/R; paid £1,200; whole £1,200 unfair | return £1,200 | para 2(b) |

### Para 5 — careless, not on any terms

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R4 | careless; would not have entered; paid £1,200 | may avoid; pay £0; return £1,200 | para 5 "may avoid the contract and refuse all claims, but must return the premiums paid" |
| R5 | as R4 but £300 "unfair" figure supplied | still return £1,200 (para 2(b) does not apply) | para 5 "must return the premiums paid" |

### Para 6 — different non-premium terms

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R6 | careless; would have entered with an exclusion that excludes this claim (claim under different terms £0); same premium; insurer requires | pay £0; not avoided; no premium return | para 6 "treated as if it had been entered into on those different terms if the insurer so requires" |
| R7 | careless; different terms (higher excess) give claim £8,000; same premium | pay £8,000 | para 6 |
| R8 | careless; different terms give £10,000 (same as actual); same premium | pay £10,000 | para 6 |

### Paras 7 and 8 — higher premium, proportionate reduction

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R9 | careless; same terms; charged £300, higher £400; claim £10,000 | X = 75; pay £7,500 | para 7 "may reduce proportionately"; para 8 X = 300/400 × 100 |
| R10 | charged £500, higher £1,000; claim £8,000 | X = 50; pay £4,000 | para 8 |
| R11 | charged £250, higher £750; claim £9,000 | X = 33⅓; pay £3,000 | para 8 |
| R12 | charged £999, higher £1,000; claim £1,000 | X = 99.9; pay £999 | para 8 |
| R13 | charged £100, higher £400; claim £2,000 | X = 25; pay £500 | para 8 |

### Paras 6 and 7 together

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R14 | careless; different terms claim £6,000; charged £200, higher £500 | X = 40; pay £2,400 | para 7 "In addition ... (whether the terms ... other than the premium would have been the same or different)"; para 8 "(or, if applicable, under the different terms provided for by virtue of paragraph 6)" |
| R15 | careless; different terms claim £0; higher premium | pay £0 | paras 6-8 |
| R16 | careless; different terms claim £5,000; charged £300, higher £600 | X = 50; pay £2,500 | paras 6-8 |

### No qualifying misrepresentation

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R17 | reasonable care; would have charged higher premium | no remedy; pay £10,000 | s 4(1) "only if" |
| R18 | no reasonable care, but same terms same premium | no remedy; pay £10,000 | s 4(1)(b) |

### Para 9 — the contract for the future (careless)

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| F1 | careless; would have entered on different terms (exclusion); not life | insurer may give notice (9(4)(a)) or terminate on reasonable notice (9(4)(b)) | para 9(2), 9(4) |
| F2 | careless; higher premium only; not life | may give notice; may terminate | para 9(3), 9(4) "either (or both) of the rights conferred by paragraph 6 or 7" |
| F3 | careless; both different terms and higher premium; not life | may give notice; may terminate | para 9(4) "(or both)" |
| F4 | careless; higher premium; wholly life insurance | may give notice; may NOT terminate | para 9(5) "may not terminate ... if it is wholly or mainly one of life insurance" |
| F5 | careless; different terms; mainly life insurance | may give notice; may NOT terminate | para 9(5) "wholly or mainly" |
| F6 | F4 and insurer gave notice under 9(4)(a) | consumer may terminate on reasonable notice | para 9(6) — no life-insurance bar on the consumer |
| F7 | F2 and insurer has not given notice | consumer has no para 9(6) right | para 9(6) "If the insurer gives notice" |
| F8 | careless; would not have entered at all | may avoid (return premiums); para 9(4) notice/termination not available | para 9(2) applies para 5; 9(4) only for paras 6/7 (reading 6) |
| F9 | deliberate or reckless | para 9 does not apply (para 2 governs: may avoid) | para 9(1)(a) "applies if ... careless" |
| F10 | termination; premiums paid for terminated cover for the balance of term £400 | refund £400 | para 9(7) "must refund any premiums paid for the terminated cover in respect of the balance of the contract term" |
| F11 | careless; higher premium; a claim is outstanding | para 9 rights still available (notice / terminate) | para 9(1)(b), reading 5 |

## Top-level chain

| # | Inputs | Expected |
|---|---|---|
| T1 | base case, Act applies, no reasonable care, higher premium £400, careless (nothing shown) | pay £7,500, no avoidance |
| T2 | as T1 but entered 1 January 2013 | Act does not apply → no remedy under the Act (claim £10,000 not reduced by the Act) |
| T3 | as T1 but knew untrue and clear question asked (presumption, not rebutted) | deliberate or reckless → avoid, pay £0, return £0 |
| T4 | as T3 with contrary shown on relevance | careless → pay £7,500 |
