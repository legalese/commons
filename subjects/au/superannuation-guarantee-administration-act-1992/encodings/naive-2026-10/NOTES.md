# Superannuation Guarantee (Administration) Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 78, compilation date 1 July 2026, includes amendments
up to Act No. 57, 2025 (the Treasury Laws Amendment (Payday Superannuation) Act
2025), register id C2026C00272, deposited at
`../../registers/source-bundle/C2004A04402.txt`.

**Checks:** one module (`sgaa-guarantee.l4`), one case file
(`sgaa-cases-guarantee.l4`), 51 assertions satisfied, 0 errors, 0 warnings. The
cases were built by a generator (scratchpad
`gen_superannuation-guarantee-administration-act-1992.py`). The expected values
were written by hand.

## Why this Act, and why scoped

This is requirement **REQ-0012** in `subjects/au/requirements.jsonl` (priority 1).
The three Western Australian cradle-to-grave lives raise it 6 times:

- Chloe **c020** (2018-03-14): turns 15, gets a TFN and a casual job at a supermarket. Is super payable? (The life cites s 28: for under-18s, only if they work more than 30 hours a week.)
- Chloe **c032** (2023-11-20): an internship at $25 an hour. Is an intern an employee, and is super payable? (s 12)
- Chloe **c041** (2024-02-29): first payslip, $5,833.33 a month. How much super, and where does it go? (ss 16, 19, 23. The life expects $641.67 at 11%.)
- Jake **k041** (2027-03-31): a delivery-platform contractor. Is super payable for a contractor? (s 12(3))
- Jake **k060** (2034-02-01): a security officer at Sentinel on the award. (s 16)
- Daniel **d044** (2031-06-01): Jarrah's first three employees. What does an employer owe from day one? (ss 16, 19)

The encoding is scoped to those questions, as the provisions read in this edition,
plus the definitions, conditions and exceptions needed to answer them. That covers:

- s 12 (employee);
- s 10A and "ordinary time earnings" (qualifying earnings);
- s 10A(6) and s 17B (the cap);
- s 17A (the amount and the charge percentage);
- "business day", "usual period" and "extended usual period" with s 18C(2) item 1 (when a contribution must arrive);
- ss 18C and 18D (shortfalls);
- s 19B (uplift);
- ss 20A, 20C and 20D (choice loading);
- s 16B (the shortfall);
- ss 32C(1)-(2A) and 32CA (which fund).

Not encoded:

- anything the regulations prescribe;
- defined benefit schemes;
- exemption certificates beyond their effect;
- assessments, collection, the s 59C penalty and Part 8;
- s 30, s 79;
- the rest of Part 3A.

## What the Act turns out to say

### 1. The deposited text is the Payday Super Act, and three of the six events ask about provisions it no longer contains

The endnotes record ss 11, 23, 27 and 28 as "rep No 57, 2025" and s 19 as
"rs No 57, 2025", commencing 1 July 2026. Part 3 now works payday by payday:

- a payment of qualifying earnings on a "QE day" gives rise to an individual superannuation guarantee amount (s 17A);
- the amount must be met by eligible contributions received within the usual period (s 18C);
- otherwise the employer owes a shortfall, with notional earnings, an uplift and any choice loading on top (ss 16B, 19A, 19B, 20A).

The quarterly scheme is gone, and so are the provisions three events cite:

- **c020:** the under-18, more-than-30-hours rule (old s 28);
- **c041:** the quarterly minimum (old s 23);
- **c041:** the 11% and 11.5% steps (old s 19).

The application provisions of Act No. 57, 2025 are not in the compilation.
INFERENCE: the repealed text still governs the 2018, 2023 and 2024 events. It was not
deposited. So c020's "no super under thirty hours" and c041's $641.67 at 11% cannot be
checked against this deposit, either way.

### 2. In this text, neither age nor hours matter. Any exclusion must come from the regulations

Nothing in ss 10A, 12 or 17A asks a worker's age or weekly hours. The only
30-hour rule left is s 12(11), which covers domestic or private work: a babysitter
working 20 hours a week, or exactly 30, is not an employee, but at 38 hours she is.
The definition of "part-time employee" in s 6(1) survives, but no encoded provision
uses it.

Under s 10A(3)(b), earnings are not qualifying earnings "to the extent that ... the
person is an employee of a kind prescribed by the regulations". So if a
fifteen-year-old's pay after 1 July 2026 is excluded at all, the exclusion has to be
in regulations that were not deposited. The encoding takes that as an input:

- not prescribed: Chloe's ordinary-hours pay is qualifying earnings;
- prescribed: it is not.

Asserted.

### 3. The charge percentage is a flat 12, with no table of dates

s 17A(2) defines "charge percentage means 12". On the inferred formula, a
$5,833.33 month paid after 1 July 2026 gives an individual superannuation guarantee
amount of $699.9996. The deposited text has no rounding rule. Asserted.

The scenario's note ("11% until 30 June 2024, 11.5% to 30 June 2025, 12% from
1 July 2025") is about the repealed s 19, which is not in this text. That was not
checked.

### 4. "Wholly *or principally*" for labour: Jake's platform contract is not settled by "not wholly"

s 12(3): "If a person works under a contract that is wholly or principally for the
labour of the person, the person is an employee of the other party to the contract."
The Jake narrative says the platform pays no super "because the contract is not
wholly for his labour". The text asks less than that: a contract *principally* for
his labour makes him an employee for this Act, whatever the Fair Work Act calls him.
The encoding asserts both answers, depending on that judgement, which is an input.

This Act does not mention minimum standards orders anywhere (a search of the deposit
for "minimum standards" finds nothing). So k041's second question is not answered
here. Asserted.

### 5. Super is due within seven business days of each payday, and a holiday in any State counts

"usual period" means the QE day to the seventh business day after it. A first
contribution to a new fund after starting or switching gets the "extended usual
period", which runs to the 20th business day (s 18C(2) item 1). A contribution received
in the 12 months before the QE day also counts (s 18C(1)(c)(ii)).

A "business day" excludes a day that is "a public holiday for the whole of ... any
State", the ACT or the NT. So a holiday in one eastern State only also lengthens a
Perth employer's period.

The d044 case uses a payday of Friday 6 June 2031 (hypothetical). The usual period
ends on 17 June, or on 18 June if 9 June is a holiday in some State. The extended
period ends on 4 July, or 7 July with that holiday. Asserted.

The Act has no small-employer exemption and no monthly threshold. Jarrah owes from its
first payday.

### 6. Overtime is not qualifying earnings; a shift loading is

"Ordinary time earnings" (s 6(1)) are earnings for ordinary hours plus "over-award
payments, shift-loading or commission". Overtime is in neither part, nor in any other
paragraph of s 10A(1). Termination lump sums for unused leave are excluded expressly.

For Jake's Sentinel fortnight (hypothetical amounts: $1,200 ordinary, $180 shift
loading, $300 overtime), qualifying earnings are $1,380 and the amount at 12% is
$165.60. Asserted.

### 7. A paid intern is caught by s 12(3) even if the ordinary meaning is doubtful

Chloe c032, at $25 an hour under a contract principally for her labour, is an
employee for this Act. The endnotes show s 12 last amended in 2006. INFERENCE: the
2023 answer is the same as this edition's. An unpaid placement with no contract for
labour is not caught. Asserted.

### 8. Late payment is expensive

- The individual final shortfall is what remains after late contributions (s 18D).
- The administrative uplift adds 60% of final shortfalls plus notional earnings (s 19B).
- The choice loading is 25% of contributions not made in compliance with the choice of fund requirements, capped by a $1,200 limit (s 20C). That limit shrinks by 25% of earlier non-complying contributions in the notice period. The notice period starts no earlier than 1 July 2026.
- Nothing is loaded where s 20D applies (the stapled fund the Commissioner named refused the money).

Asserted. On c041's "where does it go?", s 32C gives an order:

1. the employee's chosen fund;
2. failing a choice, the stapled fund the Commissioner names;
3. failing that, the employer's default fund with a MySuper product.

s 32CA overrides all of these if the employer charges the employee for the fund.
Asserted.

### 9. Six formulas did not survive conversion

The deposit has "equal to:" and then "where:" in ss 10A(5), 17A(2), 18A(3), 18C(1),
18D(2) and 19A(2). The formulas encoded for 17A(2), 18C(1) and 18D(2) are inferences
from the surrounding words: "a particular percentage of the payment", and "less than
nil". The maximum contributions base and the notional earnings component are inputs.

## What would need doing before this is worth anything

- **The formulas.** Re-fetch the compilation in a format that keeps them, and check the three inferred formulas.
- **The pre-2026 law.** Deposit the compilation in force before 1 July 2026, and the application provisions of Act No. 57, 2025 (sch 1 items 181-189). Only then can c020, c032 and c041 be answered for their own dates, including the life's $641.67 at 11%.
- **The regulations.** Deposit the Superannuation Guarantee (Administration) Regulations and read them for any prescribed exclusion under s 10A(3)(b), in particular for under-18s and hours.
- **The charge.** Read the Superannuation Guarantee Charge Act 1992, which imposes it.
- **Not encoded.** Notional earnings (s 19A), the general interest charge, uplift reductions by regulation, assessments, the s 59C penalty, and the rest of Part 3A, including standard choice forms and temporary visa holders.
- **Testing.** No ATO guidance, ruling or case law was consulted. The "wholly or principally" test for platform work is the live question, and it is left as an input.
