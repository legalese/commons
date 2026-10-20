# Judges (Long Leave Payments) Act 1979 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the long leave position for` (`jllp-rules.l4`). It answers:

- the weeks of judicial salary payable;
- the amount payable;
- to whom it is payable.

The encoded provisions are ss 3, 3A, 3B, 4, 5(1)-(2) and 7. The source is the compilation of 1 September 2021.

## Seat

The encoding is written from the seat of **the Judge**, or on the Judge's death the survivors. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "When I stop being a Judge, is a long leave payment due, how much, and to whom?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery |
| s 3 | encoded: Judge (as a kind of office), judicial salary, retirement |
| s 3A | encoded |
| s 3B | applied: the kind of office is the office held apart from Division 2 |
| s 4 | encoded; service and qualifying service (s 4(3)) are inputs in years |
| s 5 | (1)-(2) encoded; (2A)-(4) (directions on distribution, trustees) are out of scope |
| s 6 | out of scope: appropriation |
| s 7 | encoded |

## Forks (readings taken)

- **F1, s 4(2).** Only completed years of qualifying service count; the weeks are 5.2 × the completed years, at most 52 under s 4(1).
- **F2, s 4(2A)-(2C).** They apply only where s 4(1) does not, and give 5.2 weeks per completed year with no cap.
- **F3, s 7.** A removal is a retirement (ceasing otherwise than by death); with a Governor-General's direction, s 4 applies as usual.
- **F4, s 4(2A).** Ceasing at the compulsory age is a retirement too, so with 10 years' service s 4(1) (and its cap) applies.
- **F5, s 5 (changed after the independent pass).** Where an amount is payable under s 4 but comes to nil weeks (death with under a year's qualifying service), it still has a payee under s 5.
- **Known limits (from the independent pass).**
  - Qualifying service greater than service is not rejected.
  - A Judge with no compulsory retirement age has no separate input (s 4(2A)(a)).
  - s 5(2A)-(4) are out of scope.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 43 assertions satisfied, 0 failed, 0 other errors — 19 the encoder's (`jllp-tests.l4`), 24 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
