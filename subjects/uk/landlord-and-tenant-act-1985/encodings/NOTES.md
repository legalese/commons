# Landlord and Tenant Act 1985 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the lease position for` (`lta-goal.l4`). For a residential lease it answers:

- whether the s 11 repairing covenant and the s 9A fitness covenant are implied, and the first day the fitness covenant bites;
- if a service charge was demanded: the amount payable after ss 19, 20 and 20B, and whether it may be withheld under s 21B;
- the deadlines for information about the landlord: s 1, s 3(1), the end of the old landlord's liability under s 3(3A)-(3B), and s 22.

Three goals sit under it:

1. **Repair and fitness** (`lta-repair.l4`): ss 9A(1), 9B, 11(1), 13 and 14.
2. **Service charges** (`lta-service-charges.l4`): ss 19(1), 20(1), (7), 20B and 21B.
3. **Information** (`lta-information.l4`): ss 1(1), 3(1), (3A)-(3B), 22(2) and (4).

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the residential tenant**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "Must my landlord repair the property and keep it fit to live in, and from when; how much of my service charge must I pay, and can I withhold it; and by when must I be told who my landlord is, or that the landlord has changed?"

The facts it asks for are ones that person can state, or findings made about them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| s 1(1) | encoded (goal 3); (2)-(3) are out of scope |
| s 2 | out of scope |
| s 3(1), (3A)-(3B) | encoded (goal 3) |
| ss 3A-7 | out of scope: rent books, offences |
| ss 8-10B | out of scope: fitness in Wales, social housing hazards |
| ss 9A, 9B | encoded (goal 1); 9A(2)-(8) are out of scope |
| s 11(1) | encoded (goal 1): whether the covenant is implied; its content and exceptions in (1A)-(6) are not computed |
| ss 12, 15-17 | out of scope |
| ss 13-14 | encoded (goal 1); the s 14 exceptions, s 13(1A)/(1AA) and s 13(1ZC) are category inputs |
| ss 18-19 | encoded (goal 2): the reasonable part is an input |
| s 20 | encoded (goal 2): whether the works qualify and consultation failed, and the appropriate amount, are inputs |
| s 20B | encoded (goal 2) |
| ss 20A, 20C-20K | out of scope |
| ss 21, 21A | out of scope: regulations about service charge information |
| s 21B | encoded (goal 2) |
| s 22(2), (4) | encoded (goal 3) |
| ss 23-40, Schedule | out of scope |

## Forks (readings taken)

- **F1, ss 9B(8), 13(2): "a term of less than seven years".** The term counts from the grant and ends before the last day of the seven years beginning with the grant. A periodic tenancy is under seven years. A lessor's break within seven years makes the lease count as under seven years. A lessee's option that takes it to seven years or more makes it count as not under seven.
- **F2, s 13(1ZC).** An assured tenancy within (1ZC) is excluded from s 11 even if s 13(2)(b) would count it as under seven years. (1ZC) speaks of the grant "for a term of seven years or more". This is a reading.
- **F3, s 9B(4).** For a periodic or secure tenancy already in existence on the commencement date, the covenant bites on the day after the end of the 12 months beginning with that date. For a commencement date of 20 March 2019, that is 20 March 2020.
- **F4, s 9A(1)(a): "at the time the lease is granted or ... if later, at the beginning of the term".** The beginning of the term is not an input, so the grant date is used.
- **F5, s 9B(6).** A renewal on or after the commencement date "is to be treated as a grant", so enter the renewal date as `granted on`. If the original, earlier grant date is entered, the first day the covenant bites is not known, and the answer is NOTHING. This was changed after the independent pass (F9).
- **F6, s 20B(1): "incurred more than 18 months before a demand".** The bar applies when the demand is served after the last day of the 18 months beginning with the day the costs were incurred, unless the tenant was notified within those 18 months.
- **F7, s 20.** The cap is applied item by item, so enter one item for each set of qualifying works.
- **F8, s 3(1): "within two months of the assignment".** The two months end on the corresponding date two months after the assignment. If the next rent day falls on or before that date, notice is due by that date; otherwise it is due by the rent day.
- **F9, s 3(3B).** The old landlord's liability ends on the day the first notice is given. Whether a breach on that day falls inside the period is not decided.
- **F10, s 22(2) and (4).** "Within six months of" and "not later than one month after" are taken as on or before the corresponding date.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 7 modules: 162 assertions satisfied, 0 failed, 0 other errors — 48 the encoder's (`lta-tests.l4`), 114 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F2:** does s 13(1ZC) exclude a lease that s 13(2)(b) treats as under seven years?
- **F9:** is a breach on the day the first notice is given within the s 3(3B) period?
