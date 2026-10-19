# Taxes Management Act 1970 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the self-assessment position for` (`tma-goal.l4`). For an individual's income tax self-assessment for a tax year, it answers:

- **Returns:** the last day to notify chargeability, the filing deadline, the last day to amend, and the last day for a notice of enquiry.
- **Payment:** whether payments on account are due, with their amounts and dates; the balancing payment and its date.
- **Assessment:** the last day for an assessment.

Three goals sit under it:

1. **Returns** (`tma-returns.l4`): ss 7(1), (1A), (1C)(a), 8(1D)-(1G), 9ZA(2)-(3) and 9A(2).
2. **Payment** (`tma-payment.l4`): ss 59A(1)-(2) and 59B(1), (3)-(4), (6).
3. **Assessment time limits** (`tma-time-limits.l4`): ss 34(1), 36(1)-(1A) and 36A(2).

A tax year is written as the calendar year it begins in (2024 for 2024-25). Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the individual taxpayer**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "By when must I tell HMRC, file and amend my return; until when can HMRC open an enquiry into it; what must I pay on account and at the end, and when; and until when can HMRC still assess me?"

The facts it asks for are ones that person can state, or findings made about them.

The enquiry and assessment deadlines state HMRC's powers. For the taxpayer, they are the dates after which HMRC can no longer enquire or assess.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| s 7 | encoded (goal 1) for a person not given a notice to file; (1B), (1C)(b) and (3)-(9) are out of scope |
| s 8 | encoded (goal 1): (1D)-(1G); the content of returns is out of scope |
| ss 8A-8C, 12-12AE | out of scope: trustee, partnership and other returns |
| s 9 | the self-assessment is an input |
| s 9ZA(2)-(3) | encoded (goal 1) |
| s 9ZB | out of scope |
| s 9A(2) | encoded (goal 1); the scope of enquiries is out of scope |
| ss 9B-33A | out of scope |
| ss 34, 36, 36A | encoded (goal 3); ss 34A, 35, 40-43 are out of scope |
| s 59A(1)-(2) | encoded (goal 2); (3)-(10) (claims to reduce, later adjustments) are out of scope |
| s 59B(1), (3)-(4), (6) | encoded (goal 2); (2), (4ZA)-(5A) and (7) are out of scope |
| ss 86 onwards | out of scope: interest, penalties, and the rest |

## Forks (readings taken)

- **F1, "Year 2".** The tax year after the year of assessment. Its "31st October" is in the calendar year Y+1, and its "31st January" is in Y+2.
- **F2, "the period of 3 months beginning with the date of the notice".** It ends on the day before the corresponding date, or on the last day of that month if it has none.
- **F3, s 8(1F)-(1G).** A notice given on 31 July in Year 2 falls under s 8(1D), not Exception 1, because Exception 1 needs a notice "after 31st July". Likewise a notice on 31 October falls under Exception 1, not Exception 2.
- **F4, s 9A(2)(a): "up to the end of the period of twelve months after the day on which the return was delivered".** The corresponding date twelve months later.
- **F5, s 9A(2)(b)-(c): "the quarter day next following the first anniversary".** The first quarter day strictly after the anniversary. For an amended return, the later of the (a)/(b) date and the (c) date.
- **F6, s 59A(1)(d).** The relevant amount must be at least the prescribed proportion of the assessed amount.
- **F7, s 59B(6).** The due date is the notice date + 30.
- **F8, ss 34, 36, 36A.** The last day is 5 April, 4, 6, 12 or 20 years after the end of the tax year.
- **F4 (changed after the independent pass).** s 9A(6) defines "the filing date" for enquiries as the last day for delivery under s 8. That is the s 8 deadline, not the s 9ZA(3) date, so a paper return delivered after 31 October is late for s 9A.
- **Known limits (from the independent pass).**
  - The loss of tax is one choice: enter the most serious, because the longest period governs. The s 36A(7)-(9) exclusions are not modelled.
  - s 59B(3)(a) (notified in time) is an input, and s 59B(4ZA) is not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 7 modules: 135 assertions satisfied, 0 failed, 0 other errors — 35 the encoder's (`tma-tests.l4`), 100 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F5:** where the first anniversary is itself a quarter day, is that day the "quarter day next following", or is the next one?
