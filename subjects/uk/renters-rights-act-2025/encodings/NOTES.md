# Renters' Rights Act 2025 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the renting position for` (`rra-goal.l4`). For an assured tenancy in England it answers:

- whether the tenancy runs as a periodic tenancy, and whether its rent periods are permitted;
- for a rent period: whether the term making the rent due in advance is of no effect, and the day the rent is due;
- for a letting: whether a rental bidding penalty may be imposed, and its maximum.

Three goals sit under it:

1. **Periodic tenancies and rent periods** (`rra-tenancy.l4`): HA 1988 s 4A(1)-(3), (5) and (8), as inserted by s 1.
2. **Rent in advance** (`rra-tenancy.l4`): HA 1988 s 4B(1)-(7) and (12), inserted by s 8; and TFA 2019 Sch 1 para 1(1A), inserted by s 9.
3. **Rental bidding** (`rra-bidding.l4`): ss 56 and 57(1)-(4), (9).

The text prints the sections it inserts into other Acts, so they are encoded from it. The formula in s 4A(6) is lost in the conversion, so the substitute monthly rent is not computed.

## Coverage

| Provision | Disposition |
|---|---|
| s 1 (HA 1988 s 4A) | encoded (goal 1); (6) the formula is lost |
| ss 2-7 | out of scope: they amend the grounds, s 8 and rent increases |
| s 8 (HA 1988 s 4B) | encoded (goal 2); (8)-(11) are out of scope |
| s 9 (TFA Sch 1 para 1(1A)) | encoded (goal 2); para 1A and s 5A-5B are out of scope |
| ss 10-55 | out of scope: repayment, pets, duties and penalties, guarantors, notices to quit (see the Protection from Eviction Act 1977 encoding), discrimination, and the Welsh and Scottish provisions |
| s 56 | encoded (goal 3) |
| s 57(1)-(4), (9) | encoded (goal 3); (5)-(8) are out of scope |
| ss 58 onwards | out of scope |

## Forks (readings taken)

- **F1, s 4A(3).** A period of exactly 28 days is permitted; 29 days is not. "Monthly" is taken as an input category (s 4A(8)).
- **F2, s 4B(12): "initial rent".** Rent for the first rent period, or for a later period that ends on or before the first day + 27.
- **F3, s 4B(12): "permitted pre-tenancy period".** From the day the tenancy is entered into to the day before its first day, both included.
- **F4, s 4B(1): "due in advance".** Due before the first day of the rent period.
- **F5, s 4B(3)-(5).** The substitute rent day is the regular rent day in the period (an input), or otherwise the first day of the period.
- **F6, s 57(2): "within the period of five years ending with the date".** A previous penalty imposed after the corresponding date five years earlier, and on or before the new date.
- **F7, the top-level "runs as a periodic tenancy".** Every assured tenancy within s 4A runs as periodic. Transitional cases (tenancies before the commencement date) are not separated.
- **Known limits (from the independent pass).**
  - A monthly tenancy's first period over 30 days (s 4A(8)) cannot be stated.
  - Rent periods that change over the tenancy (s 4A(4)) cannot be stated.
  - The substitute monthly periods of s 4A(5) are not computed.
  - s 56's "relevant person", "a specific amount" and the comparison with the stated rent are inputs.
  - s 57(2) takes one earlier penalty at a time.
  - The regular rent day is an input and is not checked against the period.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 6 modules: 117 assertions satisfied, 0 failed, 0 other errors — 37 the encoder's (`rra-tests.l4`), 80 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F2:** confirm that a later period ending exactly on the 28th day of the initial 28-day period counts as initial rent.
