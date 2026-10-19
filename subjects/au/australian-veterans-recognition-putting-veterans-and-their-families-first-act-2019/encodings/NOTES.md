# Australian Veterans' Recognition (Putting Veterans and their Families First) Act 2019 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the veteran position for` (`avr-rules.l4`). It answers:

- whether I am a veteran;
- the committed decision date for an MRC Act claim;
- that Part 2 is not enforceable.

The encoded provisions are ss 4, 7(3) and 10.

## Seat

The encoding is written from the seat of **the veteran, or a family member**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Am I a veteran under this Act; by when has the Commonwealth committed to decide my MRC Act claim; and can I enforce any of Part 2?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope |
| s 4 | "veteran" encoded |
| ss 5-6, 8, Schedule 1 | inert: recognition, the Covenant and cooperation |
| s 7 | (3) encoded; (1)-(2) are inert commitments |
| s 9 | noted: pins and cards are discretionary |
| s 10 | encoded |
| s 11 | out of scope |

## Forks (readings taken)

- **F1, s 7(3), "within 90 days beginning on".** The last day is the later of the two days + 89.
- **F2, s 10.** The commitment in s 7(3) is part of Part 2, so it is not enforceable.
- **Known limits (from the independent pass).**
  - There is no input for which Act a claim is under; s 7(3) covers MRC Act claims only, so the date is given for any claim entered.
  - s 9 (pins, cards and family members) is not encoded.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 18 assertions satisfied, 0 failed, 0 other errors — 7 the encoder's (`avr-tests.l4`), 11 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
