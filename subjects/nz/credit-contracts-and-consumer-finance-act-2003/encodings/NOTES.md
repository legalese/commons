# NOTES: the Credit Contracts and Consumer Finance Act 2003 (New Zealand), row `legalese-aswathy`

**Draft. No New Zealand lawyer has reviewed this encoding against the Act.**

## What is encoded

The computable rules of the Credit Contracts and Consumer Finance Act 2003 (version as at 1 July 2026, from the text converted from the PCO XML) on cancellation, continuing disclosure periods, interest, high-cost credit, hardship applications and statutory damages. They sit under one top-level goal, `the credit position for` (`cccfa-goal.l4`). For a contract it answers whether it is high-cost and may be entered into, the further costs of borrowing recoverable, whether a cancellation is effective and the last day to cancel, and the statutory damages for simultaneous breaches. Four goals sit under it:

1. **Cancellation and disclosure periods** (`cccfa-cancellation.l4`, `cccfa-dates.l4`): ss 18(2), 27, 29.
2. **Interest and high-cost credit** (`cccfa-interest.l4`): ss 5, 39, 40, 45C, 45E-45I.
3. **Hardship** (`cccfa-hardship.l4`): ss 55(3), 57, 57A.
4. **Statutory damages** (`cccfa-damages.l4`): s 89.

Modules: `cccfa-types.l4` (nouns only), `cccfa-dates.l4`, `cccfa-cancellation.l4`, `cccfa-interest.l4`, `cccfa-hardship.l4`, `cccfa-damages.l4`, `cccfa-goal.l4`; tests in `cccfa-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** Lender responsibility (s 9C) and the Responsible Lending Code; the content of disclosure (Schedule 1); unreasonable fees (ss 41-45, a matter for the court); repossession (Part 3A); oppression; leases and buy-backs beyond s 89; enforcement other than s 89. Rates, balances, fees, history and the s 89 measured amounts are inputs.

**Lost in conversion.** Paragraph labels: s 89(2)'s "(1)(d)" is read as the "any other breach" limb.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 5 | working day, daily interest rate | encoded |
| s 17 | initial disclosure | inert (its date is an input) |
| s 18(2) | continuing disclosure period | encoded |
| ss 19-26B | other disclosure | out of scope |
| s 27 | right to cancel | encoded |
| s 28 | notice and return | inert |
| s 29 | exceptions | encoded |
| ss 30-31 | effect of cancellation | out of scope |
| s 39 | limit on interest | encoded |
| s 40 | default interest | encoded: the base on which it may run |
| ss 41-45 | fees | out of scope: the court's judgement |
| s 45C | high-cost contract | encoded |
| s 45D | raising the rate | inert |
| s 45E | costs of borrowing cap | encoded |
| ss 45F-45G | prohibited high-cost contracts | encoded |
| s 45H | rate cap | encoded (regulations' method read simply) |
| s 45I | compound interest | encoded |
| s 45J | default fees | out of scope: prescribed amounts |
| s 55 | hardship applications | encoded: (3) |
| s 56 | changes that can be made | inert |
| s 57 | when an application may not be made | encoded |
| s 57A | creditor's obligations | encoded: (1)-(2) |
| s 88 | liability for statutory damages | inert |
| s 89 | amount of statutory damages | encoded |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 27, 57A | "Within n working days of/after" a day | By the nth working day after it | Ordinary reading |
| F2 | s 18(2) | When do 45 working days and 6 months beginning on a day end? | The 45th working day counted from it; 6 months under Legislation Act s 56 | s 56 (month-end case changed after the independent pass) |
| F3 | ss 45F, 45G | "Within the preceding n days" of day D | From D − n to D − 1 | The days before the contract |
| F4 | s 45H | 0.8% a day "calculated in accordance with the regulations" | 0.8% of the credit provided for each day | The regulations are not in the source |
| F5 | s 89(2) | Which limb is "(1)(d)"? | The "any other breach" limb | Labels lost; the only limb whose amount can be small |
| F6 | s 55(3)(a) | "Not less than 4 months after the previous application" | After the 4 months that start the day after it | Legislation Act ss 54, 56 (changed after the independent pass) |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `cccfa-tests.l4` (encoder) | 0 | 61 | 0 |
| `tests-independent.l4` | 0 | 162 | 0 |
| the 7 rule modules | 0 | 0 | 0 |
| **total** | 0 | 223 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 3 disagreements, all resolved in its favour: the s 56 end of a 6-month period, the s 55(3) 4 months (F6), and the s 57A(2) extension only for a timely request. **The encoder's test that encoded the old F6 reading was changed** and marked.

**Known limits.** Rates in s 39 are fractions; in s 45C they are percentages. The s 45E figure is floored at 0, so no s 48 refund is computed. Matariki Observance Days are an input.

## Open questions for a New Zealand lawyer

1. F5: which paragraph of s 89(1) does s 89(2)'s $200 minimum apply to?
2. F4: how do the regulations calculate the s 45H rate?
