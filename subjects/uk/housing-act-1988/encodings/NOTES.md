# Housing Act 1988 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the possession position for` (`ha88-goal.l4`). It answers:

- **For a s 8 notice:** the earliest and latest dates for proceedings, and whether a Ground 7A notice was served in time.
- **For a s 21 notice (England):** whether it is valid as to timing, and the last day for proceedings.
- **For an unlawful eviction:** whether the landlord is liable, and the statutory damages.

Three goals sit under it:

1. **Section 8 notices** (`ha88-possession.l4`): s 8(1)(a), (3)(b)-(c), (3A), (4), (4A), (4B) and (4C)-(4F), in the version before the Renters' Rights Act 2025.
2. **Section 21 notices** (`ha88-possession.l4`): s 21(1)(b), (4)(a)-(b), (4ZA) and (4B)-(4E).
3. **Damages for unlawful eviction** (`ha88-damages.l4`): ss 27(1)-(3), (6)-(8) and 28(1).

## The two versions in the source

The revised text runs together the text before, and the text after, the Renters' Rights Act 2025. For s 8 the version is an input:

- The version **before** the 2025 amendments is computed.
- The **amended** version refuses in `the earliest date for proceedings under`, and the top-level goal gives NOTHING for it, because its table of periods (s 8(4AA)) is not in the deposited text. The Renters' Rights Act 2025 is its own subject.

Section 21 is encoded as printed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-7 | out of scope; the Schedule 2 grounds are inputs |
| s 8 | encoded (goal 1), pre-2025 version; (2), (5)-(7) are out of scope |
| ss 8ZA-20D | out of scope (rent increases in ss 13-14 run two versions together) |
| s 21 | encoded (goal 2); (1A)-(1B) (social providers), (2)-(3), (4A), (5)-(5A), (8)-(9) are out of scope |
| ss 21A-26 | out of scope |
| ss 27-28 | encoded (goal 3); the two valuations under s 28(1)-(3) are inputs |
| ss 29 onwards | out of scope |

## Forks (readings taken)

- **F1, s 8 precedence.** If Ground 7A is specified, (3A) governs. Otherwise, if Ground 14 is specified, (4) governs. Otherwise, a (4A) ground triggers (4A). Otherwise (4B) applies.
- **F2, "two months from", "one month after", "twelve months from".** Each is the corresponding date, or the last day of the month if it has none.
- **F3, "the expiry of the period of two weeks from the date of the service".** The date of service + 14.
- **F4, s 8(4C)-(4F).** The notice must be served within the 12 (or 3) months beginning with the trigger day. That day is the conviction, the finding or the order, or the end of any appeal, and is an input.
- **F5, s 21(4B).** The notice must be given after the last day of the four months beginning with the tenancy's start, or the original tenancy's start for a replacement tenancy.
- **F6, s 21(4E).** It applies where a periodic tenancy's notice-to-quit date is more than two months after the notice was given. Proceedings must then begin within the four months beginning with the date specified.
- **F7, s 27(8)(b).** The reasonable-grounds defence answers only liability arising from harassment. It does not answer deprivation of occupation.
- **F8, ss 27(7)-28.** The damages are the value without the occupier's right, less the value with it, less the court's reduction, and not below 0.
- **Known limits (from the independent pass).**
  - A notice listing Ground 7A with no condition input is treated as served in time.
  - The s 28 amount is the value without the right less the value with it, floored at 0, not an absolute difference.
  - s 27(2), including its knowledge test, is one input.
- **F4 (changed after the independent pass).** A Ground 7A notice served before the trigger day is not "within the period beginning with" it.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 6 modules: 129 assertions satisfied, 0 failed, 0 other errors — 35 the encoder's (`ha88-tests.l4`), 94 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F1:** confirm the precedence where Ground 7A or 14 is combined with other grounds.
