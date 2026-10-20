# Rates and Charges (Rebates and Deferments) Act 1992 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc`.

Files:

- `rcrd-rebates.l4`: the module. It covers who is an eligible pensioner or eligible senior, whether the home counts and the entitlement must be registered, arrears, the rebate and its prescribed limits, the deadline for the rebated amount, deferment, and when deferred charges become payable.
- `rcrd-cases-rebates.l4`: the worked cases, built by the scratchpad generator `gen_wa_rates-and-charges-rebates-and-deferments-act-1992_baseline.py`.

Conventions: a rating year runs 1 July to 30 June and is named by the calendar year in which it ends (2073/74 is 2074). A day is the number YYYYMMDD. A share of land is a fraction.

## Edition

- **The Act.** The compilation of the Rates and Charges (Rebates and Deferments) Act 1992 (No. 31 of 1992) deposited at `../../registers/source-bundle/mrdoc_47938.txt` (legislation.wa.gov.au mrdoc 47938, retrieved 2026-09-07). The latest amendment noted in the deposit is No. 42 of 2024 s 58 (s 29A).
- **The Regulations.** The Rates and Charges (Rebates and Deferments) Regulations 1992, version 04-h0-02 (currency from 13 Jun 2018), deposited at `subjects/au/wa/rates-and-charges-rebates-and-deferments-regulations-1992/registers/source-bundle/mrdoc_40959.txt` (mrdoc 40959, retrieved 2026-10-20). They hold only r 1 (citation), r 3 (seniors' limits) and r 4 (pensioners' limits). The plan listed them as not deposited; they now are, and their limits are used, not asked.
- **Missing from the deposit.** The equations in s 40(5), (6) and (7) are images in the original and did not survive conversion; only the symbols and glosses did. The formulas used are inferred (see finding 10).
- The charges used in the cases (council rates of $1,800, a levy of $90, a water supply charge of $250) are **illustrative**.

## Checks

One case file: **43 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). `l4 run rcrd-rebates.l4` reports "Checking succeeded" with no diagnostics.

As a control, a copy with two expected values altered (360 to 361, 1050 to 1051) was run. The runner reported both failures.

## Seat

**The pensioner or senior ratepayer.** The life asks "is he eligible for the rates rebate?". The Act's benefits go to the "eligible person" whose entitlement to the land is registered (ss 27(2), 40(1)).

The administrative authority (the council or the Water Corporation) registers, allows the rebate, permits or declines deferment and recovers deferred charges. The Minister may extend time. Those powers appear only as what they mean for the ratepayer.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed. The Regulations, which set the limits, are deposited and brought in.
- **The actors the text names.** Followed: the eligible pensioner and eligible senior, their spouse or de facto partner, co-owners, a dependant, the administrative authority, the Water Corporation, the Minister.
- **A judgment handed to someone else is answered conditionally.** Followed. These are inputs: the Minister's extension for exceptional circumstances (s 40(3A)), the authority's refusal of deferment because the land would not cover the charges (s 47), an arrears arrangement (s 33(6)), and the extra days the Water Corporation allows.
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed. Worked out: eligible pensioner, eligible senior, land belonging to a person, ordinary place of residence while away, rebate, rebated amount, final payment day. Asked as facts: holding each card, the Commonwealth pension means test, the veterans' categories under Commonwealth Acts, the kind of relevant interest.
- **One case is the text's natural unit.** Followed: one person, one home, one prescribed charge, one charged period.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Left out: purposes, ministerial directions and procedural manuals, delegation, reviews, compensation and reimbursement claims (ss 8–17), and the transitional provisions (ss 18–21, Schedule 1).

**Departures:**

- The relevant interests in ss 29–29C are one choice of interest, not worked out from their facts.
- Only rating years from 1 July 2018 are covered. The Regulations' tables for earlier years are left out; the life's event is in 2073.
- Separation and former joint occupation (s 31) and the surviving partner's registration (s 32A) are not modelled, except where s 44(2)(c) and s 45 use them.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Jake **k095** (2073-08-30), turns 67: the Disability Support Pension gives way to the Age Pension; the council rates rebate | `Am I an eligible pensioner`, `On which basis should I register`, `Must my entitlement be registered`, `Am I entitled to a rebate or deferment`, `How much is my rebate`, `What is my rebated amount`, `By what day must I pay my rebated rates`, `May I defer payment`, `What happens to the charge` | Yes. Jake holds a pensioner concession card and is within the means test (assumed, since he is paid the pension), so he is an eligible pensioner under s 23(1). He lives in the Cockburn Central strata apartment he owns alone, so his entitlement must be registered. On illustrative 2073/74 rates of $1,800 the rebate is 50%, held to the $750 limit, so he pays $1,050 by 30 June 2074. On a $90 levy it is $45 (no limit), and on a $250 water supply charge it is $108.86 (the limit). As sole owner of a strata lot he may defer instead. If he does not pay in time, the full charge is owed but deferred and not pursued. It falls due on his death, since he has no surviving partner. |

The plan cited only "ss 24-25 (pensioner rebate)" for this event. Jake's eligibility in fact comes from s 23(1). Section 24 needs an eligibility prescribed by regulation, and the deposited Regulations prescribe none. Section 25 only allows a means test to be prescribed, and none is.

## Why this scope

The scope is what the event asks: is a new Age Pensioner entitled to the rebate, and how much is it. It also covers what any pensioner or senior homeowner meets: the seniors' card and the Commonwealth seniors health card, a home shared with a partner or others, a stay in care, arrears, the deadline, deferment, and what happens to deferred charges on sale or death.

The Local Government Act 1995 and Emergency Services Levy baselines ask "am I entitled to a rebate or deferment under this Act?" as a fact. `Am I entitled to a rebate or deferment` answers that question here.

Left out, because no ratepayer in the lives meets them: administration and review machinery, back-dated charges (s 42), incorrect rebates (s 39) and the transitional provisions.

## What the Act turns out to say

1. **There is no age in the Act.** An eligible senior is simply the holder of a seniors' card (s 22), whose conditions are "determined by the chief executive officer of the senior's card department" (s 5). Asserted.
2. **A seniors' card together with a Commonwealth seniors health card makes you a pensioner, not a senior.** Under s 23(4) the holder of both is an eligible pensioner, with the 50% rebate and the right to defer, and no means test in this Act. Asserted.
3. **A pensioner concession card is not enough on its own.** Section 23(1)(c) adds the Commonwealth pension means test, "unless the person is permanently blind". Asserted.
4. **The plan's sections are the wrong ones for Jake.** Section 24 needs an eligibility "of a kind prescribed", and s 25 only lets a means test be prescribed. The deposited Regulations prescribe neither, so Jake's entitlement rests on s 23(1). Asserted for s 23(1).
5. **A person who neither owns nor lives in the home can qualify.** Under s 23(5), a parent, grandparent, brother or sister of a disabled person who lives there qualifies if no owner lives there. Such a person may not defer (s 43(1b)). Asserted.
6. **The home can still count while you are in care.** Under s 30(1) it does if you left through ill-health or frailty, your belongings remain, it is empty, or occupied by a dependant, or occupied rent-free, and nothing else is registered. Letting it at a rent ends this. Asserted.
7. **Arrears block the rebate, but not registration.** Registration happens "even if arrears ... remain payable" (s 32(3)), but no rebate or deferment is allowed while arrears are due (s 33(3)). The exception is a pensioner with an agreed arrears arrangement who keeps to it (s 33(6)–(7)). Seniors have no such exception. Asserted.
8. **The rebate is 50% for pensioners and 25% for seniors, held to the Regulations' limits.** Pensioners: rates $750, water $108.86, sewerage $436.15, drainage $54.99, with no limit on the emergency services levy or the underground electricity charge (r 4(1A), (2)). Seniors: rates $100, water $18.14, sewerage $72.69, drainage $9.17, underground electricity $100 (r 3(2)). Asserted for rates, the levy and water.
9. **No limit is prescribed for a senior's rebate on the emergency services levy.** Section 40(9)(a) caps it only "up to such limit as is prescribed", and r 3(2) prescribes none for the levy. So a senior's levy rebate is an uncapped 25% (inference). Not asserted as an amount.
10. **The proration equations are missing from the deposit.** The s 40(5)–(7) equations are images that were not converted. The encoding uses R = (PCS × DS + PCP × DP) / CY, inferred from the glosses. Whether a prescribed limit applies before or after apportionment for shared ownership is also not stated; it is applied after. Asserted under these inferences.
11. **A resident partner's share counts as yours** (s 27(5)). A couple who own their home together get the full 50% on the whole charge. With any other co-owner, the charge and the rebate are apportioned by share and by residential use (s 28), and never above 50% (s 28(3)). Asserted for a half share.
12. **Pay the rebated amount by the end of the rating year**, which is 30 June for rates and the levy (s 40(2)(b)). A Water Corporation charge must be paid by the "final payment day": the 50th day after the notice, extendable by up to 70 more (s 3(1)). Paying in time ends the liability (s 41). Asserted.
13. **A pensioner who misses the day is deferred automatically, not pursued.** The pensioner then owes the full charge without rebate, but the authority "shall not seek to recover" it, and it may be deferred (s 44(1)). A senior has no equivalent and owes the full charge (inference from s 40(2)). Asserted.
14. **Only pensioners may defer, and only sole owners of the fee simple or a strata lot**, or co-owners within s 43(3)–(4), such as a spouse. Retirement village, caravan-park and relocatable-home residents (s 43(1a)) may not, nor may s 23(5) relatives (s 43(1b)). The authority may decline if the land would not cover the charges (s 47). Asserted.
15. **Deferred charges fall due on death, sale or moving out, whichever comes first** (s 44(2)). Two exceptions keep them deferred. On death, they stay deferred while a surviving spouse or de facto partner lives on, even one who is not eligible (s 45(1)). On moving out, they stay deferred if the move was for ill-health or frailty, or a partner or eligible dependant stays (ss 44(2)(c), 45(2)). Meanwhile they are a charge on the land (s 46), and the Limitation Act 2005 does not bar their recovery (s 49). Asserted, except s 49.
16. **One application covers rates and the levy.** An application to the council for rates "is to be taken to include" the emergency services levy (s 32(1a)). Encoded, not asserted.
17. **A death or loss of eligibility during the year does not take away that year's rebate**, except on a Water Corporation charge (s 33(2), s 37(1)(c)). Failing to report a change is an offence with a penalty of $1 000, and a prosecution must start within 5 years (ss 35, 38). Asserted for the Water Corporation exception and the penalty.

## What would need doing before this is worth anything

- Recover the s 40(5)–(7) equations from the authorised PDF or Word text and check the inferred formulas.
- Bring in the earlier limit tables (rating years 2002/03 to 2017/18) if any earlier year is needed.
- Encode s 31 (separation), s 32A (surviving partner), s 42 (back-dated charges) and the detail of ss 29–29C.
- Link `Am I entitled to a rebate or deferment` to the `I am entitled to a rebate or deferment` inputs in the Local Government Act 1995 and Emergency Services Levy baselines.
- Correct Jake's facts and the plan, which cite "ss 24-25", to s 23(1).
- An independent test pass, a coverage table and a human gate.
