# Maternity Leave (Commonwealth Employees) Act 1973 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the maternity position for` (`ml-rules.l4`). It answers:

- when the compulsory absence starts and ends;
- how long my leave may last;
- when paid absence starts and ends.

The encoded provisions are ss 3 (confinement), 5 (as an input), 6(1)-(4), (4C), (4F) and 7. The source is the compilation of 1 September 2021.

## Seat

The encoding is written from the seat of **the pregnant Commonwealth employee**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "When must I be away from work; how long may my leave last; which weeks are paid?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2, 4 | out of scope |
| s 3 | confinement encoded; the other definitions are folded into the inputs |
| s 5 | whether the Act applies is an input |
| s 5A | out of scope |
| s 6 | (1)-(4), (4C), (4F) encoded; (4A)-(4B) are folded into the 12-months service day; (4D)-(4E), (4G), (5)-(9) are out of scope |
| s 7 | encoded |
| s 7A | out of scope: applications to resume duty (business-day periods) |
| ss 7B-11 | out of scope |

## Forks (readings taken)

- **F1, s 3 confinement.** A birth or other end of pregnancy no earlier than 20 weeks (140 days) before the expected date of birth.
- **F2, s 6(1)(b).** "6 weeks before the expected date of birth" is that date − 42. "A period of 6 weeks commencing on the date of her confinement" ends on the confinement + 41.
- **F3, s 7(2) (changed after the independent pass).** With permission to work until a date, the absence starts the next day, unless she is confined before that date (strictly before), when it starts on the confinement.
- **F4, s 6(1)(a), (c).** "52 weeks commencing on" the start of the compulsory absence ends on the start + 363.
- **F5, s 6(3)-(4) (changed after the independent pass).** Pay covers the first 12 weeks of absence (start to start + 83), or the whole absence if she resumes earlier under s 7(3), counting only days on or after continuous service first exceeds 12 months. The absence is taken as continuous from the start.
- **F6, ss 3, 6(2), 6(4C) (changed after the independent pass).** A pregnancy ending more than 20 weeks early gives no compulsory absence or leave. After an unexcused unauthorised absence, the other provisions do not apply, so leave ends with the compulsory absence.
- **Known limits (from the independent pass).**
  - The s 6(4F) leave limit is not tested, since the end of the unpaid leave is not an input.
  - The s 7(1)(a) timing of the medical certificate is not checked.
  - Pay assumes an absence of at least 12 weeks unless she resumes early under s 7(3).

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 66 assertions satisfied, 0 failed, 0 other errors — 16 the encoder's (`ml-tests.l4`), 50 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
